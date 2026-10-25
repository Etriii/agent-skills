"""Stage local copies, preserve backups and recover interrupted installations."""

import json
from pathlib import Path
import re
import shutil
import uuid

from catalog import digest, files_in, safe_path


TRANSACTION = ".skills-install-transaction"
BACKUPS = ".skills-install-backups"
TARGET = re.compile(r"(?:\.(?:agents|claude|codex)/skills/[a-z0-9]+(?:-[a-z0-9]+)*|\.agent-skills/history/[0-9a-f]{32})")


def write_journal(folder: Path, journal: dict) -> None:
    pending = folder / "journal.tmp"
    pending.write_text(json.dumps(journal, indent=2) + "\n", encoding="utf-8")
    pending.replace(folder / "journal.json")


def finish(root: Path, folder: Path, journal: dict) -> None:
    if any((folder / "backups").iterdir()):
        archive = safe_path(root / BACKUPS)
        archive.mkdir(exist_ok=True)
        folder.rename(archive / journal["id"])
    else:
        shutil.rmtree(folder)


def recover(root: Path) -> str:
    """Roll back only journaled copies whose current content still matches."""
    folder = safe_path(root / TRANSACTION)
    files_in(folder)
    journal = json.loads((folder / "journal.json").read_text(encoding="utf-8"))
    if not isinstance(journal, dict) or not isinstance(journal.get("id"), str) or not re.fullmatch(r"[0-9a-f]{32}", journal["id"]) or journal.get("state") not in ("prepared", "committed"):
        raise ValueError("Invalid recovery journal; preserve transaction for inspection")
    entries = journal.get("entries")
    if not isinstance(entries, list) or any(not isinstance(e, dict) or set(e) != {"target", "before", "after"} for e in entries):
        raise ValueError("Invalid recovery entries")
    if any(not isinstance(e["target"], str) for e in entries) or len({e["target"] for e in entries}) != len(entries):
        raise ValueError("Invalid recovery targets")
    created = journal.get("created")
    if not isinstance(created, list) or any(not isinstance(p, str) or not re.fullmatch(r"(?:\.(?:agents|claude|codex)(?:/skills)?|\.agent-skills(?:/history)?)", p) for p in created):
        raise ValueError("Unsafe recovery directory")
    for i, entry in enumerate(entries):
        if not TARGET.fullmatch(entry["target"]):
            raise ValueError("Unsafe recovery target/digest")
        after = entry["after"]
        if after is not None and (not isinstance(after, str) or not re.fullmatch(r"[0-9a-f]{64}", after)):
            raise ValueError("Invalid recovery destination digest")
        before = entry["before"]
        if before is not None and (not isinstance(before, str) or not re.fullmatch(r"[0-9a-f]{64}", before)):
            raise ValueError("Invalid recovery source digest")
        target = safe_path(root / entry["target"])
        backup = folder / "backups" / str(i)
        if backup.exists() and (before is None or digest(backup) != before):
            raise ValueError(f"Backup changed; manual review required: {backup}")
        if target.exists() and digest(target) not in {entry["after"], before}:
            raise ValueError(f"Destination changed; manual review required: {target}")
        staged = folder / "staged" / str(i)
        if journal["state"] == "prepared" and before is not None and not backup.exists():
            if not target.exists() or digest(target) != before:
                raise ValueError(f"Original content missing; preserve transaction for inspection: {target}")
        if journal["state"] == "prepared" and before is None and staged.exists() and target.exists():
            raise ValueError(f"Unrelated destination appeared; preserve transaction for inspection: {target}")
        if journal["state"] == "committed" and (digest(target) if target.exists() else None) != after:
            raise ValueError(f"Committed destination changed; manual review required: {target}")
    if journal["state"] == "committed":
        finish(root, folder, journal)
        return "Completed backup archival for committed installation"
    for i, entry in reversed(list(enumerate(entries))):
        target = root / entry["target"]
        backup = folder / "backups" / str(i)
        if backup.exists():
            if target.exists():
                shutil.rmtree(target)
            backup.rename(target)
        elif entry["before"] is None and not (folder / "staged" / str(i)).exists() and target.exists():
            shutil.rmtree(target)
    shutil.rmtree(folder)
    # Only remove empty adapter directories; custom content always wins.
    for parent in sorted(created, key=len, reverse=True):
        try:
            safe_path(root / parent).rmdir()
        except OSError:
            pass
    return "Recovered previous installation state"


def install(root: Path, copies: list[tuple[Path | None, Path, str | None, str | None]], *, additions=None, guards=None, transaction_id=None) -> None:
    """Stage everything before the first destination swap and journal rollback data."""
    identity = transaction_id or uuid.uuid4().hex
    if not re.fullmatch(r"[0-9a-f]{32}", identity):
        raise ValueError("Invalid transaction identity")
    for source, target, before, after in copies:
        safe_path(target)
        if not target.is_relative_to(root) or not TARGET.fullmatch(target.relative_to(root).as_posix()):
            raise ValueError(f"Unsafe transaction target: {target}")
        if (source is None) != (after is None):
            raise ValueError("Transaction source and destination digest disagree")
    folder = safe_path(root / TRANSACTION)
    folder.mkdir()  # Exclusive lock shared by both adapters in this scope.
    created = {parent.relative_to(root).as_posix() for _, target, _, _ in copies
               for parent in (target.parent, target.parent.parent) if not parent.exists()}
    entries = [{"target": target.relative_to(root).as_posix(), "before": before, "after": after}
               for _, target, before, after in copies]
    journal = {"id": identity, "state": "prepared", "entries": entries, "created": sorted(created)}
    try:
        (folder / "staged").mkdir()
        (folder / "backups").mkdir()
        for path, expected in (guards or {}).items():
            actual = digest(safe_path(path)) if path.exists() else None
            if actual != expected:
                raise ValueError(f"Content changed since preview: {path}")
        write_journal(folder, journal)
        for i, (source, target, before, after) in enumerate(copies):
            if source is None:
                continue
            stage = folder / "staged" / str(i)
            shutil.copytree(source, stage)
            for name, content in (additions or {}).get(target, {}).items():
                if name != "kit-location.txt":
                    raise ValueError("Unsupported generated skill file")
                (stage / name).write_bytes(content)
            if digest(stage) != after:
                raise ValueError(f"Staged checksum mismatch: {source}")
        # Guard owner history again after staging, before the first destination swap.
        for path, expected in (guards or {}).items():
            actual = digest(safe_path(path)) if path.exists() else None
            if actual != expected:
                raise ValueError(f"Content changed during staging: {path}")
        for i, (_, target, before, after) in enumerate(copies):
            safe_path(target)
            actual = digest(target) if target.exists() else None
            if actual != before:
                raise ValueError(f"Destination changed since preview: {target}")
            target.parent.mkdir(parents=True, exist_ok=True)
            if before is not None:
                target.rename(folder / "backups" / str(i))
            if after is not None:
                (folder / "staged" / str(i)).rename(target)
            if (digest(target) if target.exists() else None) != after:
                raise ValueError(f"Installed checksum mismatch: {target}")
        journal["state"] = "committed"
        write_journal(folder, journal)
    except BaseException:
        if (folder / "journal.json").exists():
            recover(root)
        else:
            shutil.rmtree(folder)
        raise
    finish(root, folder, journal)
