"""Store Markdown lifecycle evidence and derive ownership from committed operations."""

from contextlib import contextmanager
from datetime import datetime, timezone
import json
from pathlib import Path
import re
import shutil
import tempfile
import uuid

from catalog import NAME, digest, safe_path


STATE = ".agent-skills"
SKILL_TARGET = re.compile(r"\.(?:agents|claude|codex)/skills/[a-z0-9]+(?:-[a-z0-9]+)*")
FIELDS = {"schema_version", "id", "status", "timestamp", "sequence", "operation", "pack", "agent", "scope", "root", "source", "manifest_sha256", "entries", "backup"}
ENTRY_FIELDS = {"target", "action", "before", "after", "installed_record", "backup_path"}


def valid_digest(value) -> bool:
    return isinstance(value, str) and re.fullmatch(r"[0-9a-f]{64}", value) is not None


def read_record(path: Path) -> dict:
    """Read strict JSON-valued Markdown frontmatter without a YAML dependency."""
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0] != "---" or "---" not in lines[1:]:
        raise ValueError(f"Malformed lifecycle record: {path}")
    fields = {}
    for line in lines[1:lines.index("---", 1)]:
        key, separator, value = line.partition(": ")
        if not separator or key in fields:
            raise ValueError(f"Malformed lifecycle field: {path}")
        fields[key] = json.loads(value)
    return fields


def inventory(root: Path) -> tuple[dict, int]:
    """Replay committed records; matching directory names alone never prove ownership."""
    history = safe_path(root / STATE / "history")
    owners, sequence = {}, 0
    if not history.exists():
        return owners, sequence
    digest(history)
    events = []
    for folder in history.iterdir():
        if not folder.is_dir() or not re.fullmatch(r"[0-9a-f]{32}", folder.name):
            raise ValueError(f"Unknown lifecycle history content: {folder}")
        fields = read_record(folder / "operation.md")
        if (set(fields) != FIELDS or type(fields.get("schema_version")) is not int or fields["schema_version"] != 1 or fields.get("id") != folder.name
                or fields.get("status") != "COMMITTED" or type(fields.get("sequence")) is not int
                or fields["sequence"] < 1 or not isinstance(fields.get("pack"), str)
                or not NAME.fullmatch(fields["pack"]) or fields.get("operation") not in ("install", "uninstall")
                or fields.get("agent") not in ("codex", "claude", "both") or fields.get("scope") not in ("project", "user")
                or not isinstance(fields.get("root"), str) or not isinstance(fields.get("entries"), list)
                or not fields["entries"] or not isinstance(fields.get("timestamp"), str)
                or (fields.get("backup") is not None and not isinstance(fields["backup"], str))):
            raise ValueError(f"Invalid lifecycle identity: {folder}")
        if fields["operation"] == "install":
            if not isinstance(fields["source"], str) or not valid_digest(fields["manifest_sha256"]):
                raise ValueError(f"Invalid install provenance: {folder}")
        elif fields["source"] is not None or fields["manifest_sha256"] is not None:
            raise ValueError(f"Invalid removal provenance: {folder}")
        if datetime.fromisoformat(fields["timestamp"]).utcoffset() is None:
            raise ValueError(f"Lifecycle time requires an explicit timezone: {folder}")
        events.append(fields)
    for event in sorted(events, key=lambda item: item["sequence"]):
        if event["sequence"] != sequence + 1:
            raise ValueError("Lifecycle history sequence is incomplete or duplicated")
        sequence = event["sequence"]
        seen = set()
        for entry in event["entries"]:
            if (not isinstance(entry, dict) or set(entry) != ENTRY_FIELDS
                    or not SKILL_TARGET.fullmatch(str(entry.get("target", ""))) or entry["target"] in seen):
                raise ValueError("Invalid lifecycle skill target")
            seen.add(entry["target"])
            after = entry.get("after")
            if after is not None and not valid_digest(after):
                raise ValueError("Invalid lifecycle skill digest")
            if entry["before"] is not None and not valid_digest(entry["before"]):
                raise ValueError("Invalid prior lifecycle digest")
            owner = owners.get(entry["target"])
            if (entry["installed_record"] != (owner["record"] if owner else None)
                    or (owner and owner["pack"] != event["pack"])):
                raise ValueError("Lifecycle ownership chain is inconsistent")
            actions = ("COPY", "REPLACE WITH BACKUP", "ADOPT MATCHING COPY") if event["operation"] == "install" else ("REMOVE", "MISSING")
            if entry["action"] not in actions or ((after is None) != (event["operation"] == "uninstall")):
                raise ValueError("Lifecycle action disagrees with operation")
            if entry["backup_path"] is not None and not isinstance(entry["backup_path"], str):
                raise ValueError("Invalid lifecycle backup path")
            if after is None:
                owners.pop(entry["target"], None)
            else:
                owners[entry["target"]] = {"pack": event["pack"], "digest": after, "record": event["id"]}
    return owners, sequence


def cell(value) -> str:
    return str(value if value is not None else "absent").replace("|", "&#124;").replace("\n", "<br>").replace("\r", "")


def markdown(event: dict) -> str:
    header = "---\n" + "".join(f"{key}: {json.dumps(value, ensure_ascii=True)}\n" for key, value in event.items()) + "---\n"
    body = f"\n# {event['operation'].capitalize()} record\n\n"
    body += f"Status: **{event['status']}**. UTC: {event['timestamp']}.\n\n"
    body += f"Pack: `{event['pack']}`. Scope: `{event['scope']}`. Agent: `{event['agent']}`.\n\n"
    body += f"Source: {cell(event['source'])}\n\nScope root: {cell(event['root'])}\n\n"
    body += f"Source manifest SHA256: `{event['manifest_sha256']}`.\n\n"
    body += "| Destination | Action | Before SHA256 | After SHA256 | Previous install record | Retained tree |\n|---|---|---|---|---|---|\n"
    for entry in event["entries"]:
        body += "| " + " | ".join(cell(entry[key]) for key in ("target", "action", "before", "after", "installed_record", "backup_path")) + " |\n"
    body += f"\nRetained content backup: {cell(event['backup'])}\n\n"
    body += "This records local file installation or removal. Agent discovery and execution are separate evidence.\n"
    return header + body


@contextmanager
def staged_record(event: dict):
    """Prepare a record outside the destination for the shared atomic transaction."""
    folder = Path(tempfile.gettempdir()) / f"agent-skills-record-{uuid.uuid4().hex}"
    folder.mkdir()
    try:
        (folder / "operation.md").write_text(markdown(event), encoding="utf-8", newline="\n")
        yield folder
    finally:
        shutil.rmtree(folder)


def new_event(**fields) -> dict:
    return dict(schema_version=1, id=uuid.uuid4().hex, status="COMMITTED",
                timestamp=datetime.now(timezone.utc).isoformat(), **fields)
