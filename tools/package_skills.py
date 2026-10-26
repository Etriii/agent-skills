"""Build a reproducible collection ZIP and SHA256 checksums from reviewed local files."""

from hashlib import sha256
from pathlib import Path
import re
import sys
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo

from catalog import bundle, safe_path


ROOT = Path(__file__).resolve().parents[1]
TOP_FILES = ("README.md", "CONTRIBUTING.md", "INSTALL.md", "UNINSTALL.md", "SKILL_CATALOG.md", "CHANGELOG.md", "LICENSE.md", "VERSION", ".gitattributes", ".gitignore")
EXCLUDED = {".git", "__pycache__", ".venv", "dist", ".agent-skills", ".skills-install-backups", ".skills-install-transaction"}


def distribution_files(root: Path) -> dict[str, bytes]:
    """Include collection-owned source trees and reject linked distribution content."""
    paths = [root / name for name in TOP_FILES]
    for tree in ("packs", "tools", "tests", "docs"):
        for path in (root / tree).rglob("*"):
            parts = path.relative_to(root).parts
            if any(part in EXCLUDED for part in parts):
                continue
            if path.name == ".env" or (path.name.startswith(".env.") and path.name != ".env.example") or path.suffix in {".pyc", ".pyo"}:
                continue
            safe_path(path)
            if path.is_file():
                paths.append(path)
    return {path.relative_to(root).as_posix(): safe_path(path).read_bytes() for path in sorted(paths)}


def build(root: Path, output: Path) -> tuple[Path, str]:
    root, output = safe_path(root), safe_path(output)
    version = (root / "VERSION").read_text().strip()
    if not re.fullmatch(r"\d+\.\d+\.\d+", version):
        raise ValueError("Invalid collection version")
    for pack in (root / "packs").iterdir():
        names = sorted(path.name for path in (pack / "skills").iterdir())
        bundle(pack, names)
    payloads = distribution_files(root)
    payloads["SNAPSHOT_SHA256SUMS"] = "".join(f"{sha256(data).hexdigest()}  {name}\n" for name, data in payloads.items()).encode()
    output.mkdir(parents=True, exist_ok=True)
    archive = safe_path(output / f"agent-skills-{version}.zip")
    pending = safe_path(output / f"agent-skills-{version}.zip.tmp")
    with ZipFile(pending, "w", compression=ZIP_DEFLATED) as zipped:
        for name, data in sorted(payloads.items()):
            entry = ZipInfo(f"agent-skills/{name}", date_time=(1980, 1, 1, 0, 0, 0))
            entry.compress_type = ZIP_DEFLATED
            entry.external_attr = 0o100644 << 16
            zipped.writestr(entry, data)
    pending.replace(archive)
    checksum = sha256(archive.read_bytes()).hexdigest()
    safe_path(output / "SHA256SUMS").write_text(f"{checksum}  {archive.name}\n", encoding="utf-8", newline="\n")
    return archive, checksum


def main() -> int:
    try:
        archive, checksum = build(ROOT, ROOT / "dist")
        print(f"Built {archive}\nSHA256 {checksum}\nLocal working-tree snapshot; no GitHub publication performed")
        return 0
    except (OSError, ValueError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
