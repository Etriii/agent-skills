"""Validate portable local skill bundles and their content manifest."""

from dataclasses import dataclass
from hashlib import sha256
from pathlib import Path
import re
import stat
import tomllib


NAME = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*")
ESSENTIAL = ("plan-review", "blocker-check", "phase-handoff", "completion-check")


@dataclass(frozen=True)
class Skill:
    path: Path
    content_sha256: str


def safe_path(path: Path) -> Path:
    """Reject links and Windows junctions before resolving any existing ancestor."""
    path = Path(path.absolute())
    for part in (path, *path.parents):
        try:
            info = part.lstat()
        except FileNotFoundError:
            continue
        if stat.S_ISLNK(info.st_mode) or getattr(info, "st_file_attributes", 0) & 0x400:
            raise ValueError(f"Linked path is not allowed: {part}")
    return path.resolve(strict=False)


def files_in(root: Path) -> dict[str, str]:
    """Fingerprint regular files; never follow links or accept special files."""
    safe_path(root)
    if not root.is_dir():
        raise ValueError(f"Not a directory: {root}")
    result = {}
    for path in sorted(root.rglob("*")):
        safe_path(path)
        if path.is_dir():
            continue
        if not stat.S_ISREG(path.stat().st_mode):
            raise ValueError(f"Not a regular file: {path}")
        result[path.relative_to(root).as_posix()] = sha256(path.read_bytes()).hexdigest()
    return result


def fingerprint(rows: dict[str, str], directories: list[str]) -> str:
    data = "".join(f"{value}  {name}\n" for name, value in sorted(rows.items()))
    data += "".join(f"dir  {name}\n" for name in directories)
    return sha256(data.encode()).hexdigest()


def digest(root: Path) -> str:
    rows = files_in(root)
    # Include empty directories so custom additions cannot disappear on a repeat install.
    directories = sorted(p.relative_to(root).as_posix() for p in root.rglob("*") if p.is_dir())
    return fingerprint(rows, directories)


def validate_skill(root: Path) -> dict:
    files_in(root)
    if not NAME.fullmatch(root.name) or len(root.name) > 64:
        raise ValueError(f"Invalid skill name: {root.name}")
    body = (root / "SKILL.md").read_text(encoding="utf-8")
    match = re.fullmatch(r"---\nname: ([^\n]+)\ndescription: ([^\n]+)\n---\n(.+)", body, re.S)
    if not match or match[1] != root.name or len(match[2].split()) < 6:
        raise ValueError(f"Invalid portable frontmatter: {root}")
    if any(char in match[2] for char in ":#{}[]"):
        raise ValueError(f"Description must be a plain YAML scalar: {root}")
    if not (root / "metadata.toml").exists():
        return {"name": root.name}
    metadata = tomllib.loads((root / "metadata.toml").read_text(encoding="utf-8"))
    if metadata.get("schema_version") != 1 or metadata.get("name") != root.name:
        raise ValueError(f"Invalid metadata identity: {root}")
    if metadata.get("skill_id") != root.name or not re.fullmatch(r"\d+\.\d+\.\d+", metadata.get("version", "")):
        raise ValueError(f"Invalid stable ID/version: {root}")
    capabilities = metadata.get("capabilities")
    if not isinstance(capabilities, list) or not capabilities or any(not isinstance(c, str) or not NAME.fullmatch(c) for c in capabilities):
        raise ValueError(f"Invalid capabilities: {root}")
    agents = metadata.get("compatible_agents")
    if not isinstance(agents, list) or any(a not in {"codex", "claude"} for a in agents):
        raise ValueError(f"Invalid compatible agents: {root}")
    if metadata.get("license_status") != "UNDECIDED" or metadata.get("provenance") != "local-authored":
        raise ValueError(f"Unsupported license/provenance: {root}")
    return metadata


def bundle(source: Path, names: list[str], expected_manifest: str | None = None) -> dict[str, Skill]:
    safe_path(source)
    manifest_path = safe_path(source / "SHA256SUMS")
    raw = manifest_path.read_bytes()
    if expected_manifest is not None and (not re.fullmatch(r"[0-9a-f]{64}", expected_manifest) or sha256(raw).hexdigest() != expected_manifest):
        raise ValueError("Manifest checksum mismatch")
    manifest = {}
    for line in raw.decode("utf-8").splitlines():
        match = re.fullmatch(r"([0-9a-f]{64})  ([A-Za-z0-9_.-]+(?:/[A-Za-z0-9_.-]+)*)", line)
        if not match or any(p in {".", "..", ".git"} for p in match[2].split("/")) or match[2] in manifest:
            raise ValueError("Malformed or duplicate manifest entry")
        manifest[match[2]] = match[1]
    for relative, expected in manifest.items():
        if not relative.startswith("skills/"):
            path = safe_path(source / relative)
            if not path.is_file() or sha256(path.read_bytes()).hexdigest() != expected:
                raise ValueError(f"Pack support checksum mismatch: {relative}")
    result = {}
    for name in names:
        if not NAME.fullmatch(name) or len(name) > 64:
            raise ValueError(f"Invalid selected skill name: {name}")
        root = source / "skills" / name
        validate_skill(root)
        rows = files_in(root)
        actual = {f"skills/{name}/{p}": h for p, h in rows.items()}
        expected = {p: h for p, h in manifest.items() if p.startswith(f"skills/{name}/")}
        if not actual or actual != expected:
            raise ValueError(f"Skill checksum mismatch: {name}")
        directories = sorted(p.relative_to(root).as_posix() for p in root.rglob("*") if p.is_dir())
        result[name] = Skill(root, fingerprint(rows, directories))
    return result
