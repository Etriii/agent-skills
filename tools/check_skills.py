"""Check local shipping skills without installing or executing their payloads."""

import argparse
from dataclasses import dataclass
import os
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit

from catalog import NAME, bundle, safe_path, validate_skill


ROOT = Path(__file__).resolve().parents[1]
POLICY_HEADING = "## Generated artifacts"


@dataclass(frozen=True)
class Check:
    status: str
    subject: str
    detail: str


def prose(text: str) -> str:
    """Ignore fenced examples and inline code when finding Markdown links."""
    lines = []
    fence = None
    for line in text.splitlines():
        marker = re.match(r"^\s{0,3}(`{3,}|~{3,})", line)
        if marker:
            token = marker[1]
            if fence is None:
                fence = token
            elif token[0] == fence[0] and len(token) >= len(fence):
                fence = None
            continue
        if fence is None:
            lines.append(line)
    return re.sub(r"(`+).*?\1", "", "\n".join(lines))


def link_targets(text: str) -> list[str]:
    """Read inline destinations and reference definitions, including image links."""
    text = prose(text)
    targets = []
    for match in re.finditer(r"!?\[[^\]\n]*\]\(\s*(<[^>\n]+>|[^\s)]+)", text):
        targets.append(match[1].removeprefix("<").removesuffix(">"))
    for match in re.finditer(r"^\s{0,3}\[[^\]\n]+\]:\s*(<[^>\n]+>|\S+)", text, re.M):
        targets.append(match[1].removeprefix("<").removesuffix(">"))
    return targets


def broken_links(document: Path, boundary: Path) -> list[str]:
    errors = []
    for target in link_targets(document.read_text(encoding="utf-8")):
        if target.startswith(("#", "//")) or urlsplit(target).scheme:
            continue
        relative = unquote(target.split("#", 1)[0].split("?", 1)[0])
        if not relative:
            continue
        if any(char in relative for char in "<>{}"):
            errors.append(f"unresolved local link: {target}")
            continue
        destination = Path(os.path.abspath(document.parent / relative))
        if not destination.is_relative_to(boundary):
            errors.append(f"missing or out-of-tree local link: {target}")
            continue
        try:
            destination = safe_path(destination)
            if not destination.is_relative_to(boundary) or not destination.exists():
                errors.append(f"missing or out-of-tree local link: {target}")
        except (OSError, ValueError) as error:
            errors.append(f"unsafe local link {target}: {error}")
    return errors


def artifact_instructions(body: str) -> bool:
    """Check the required declaration exists; do not infer behavior from keywords."""
    lines = prose(body).splitlines()
    for index, line in enumerate(lines):
        if line.strip() == POLICY_HEADING:
            section = []
            for following in lines[index + 1:]:
                if re.match(r"^#{1,2} ", following):
                    break
                section.append(following)
            return bool("\n".join(section).strip())
    return False


def check_collection(root: Path, selected: list[str] | None = None) -> list[Check]:
    """Reuse bundle validation and report each failed skill without hiding others."""
    root = safe_path(root)
    checks = []
    discovered = {}
    for pack in sorted((root / "packs").iterdir()):
        if not pack.is_dir():
            continue
        skills = safe_path(pack / "skills")
        if not skills.is_dir():
            checks.append(Check("FAIL", pack.name, "missing skills directory"))
            continue
        for skill in sorted(skills.iterdir()):
            if not skill.is_dir():
                checks.append(Check("FAIL", pack.name, f"unexpected skill entry: {skill.name}"))
                continue
            if skill.name in discovered:
                checks.append(Check("FAIL", skill.name, "duplicate skill name across packs"))
            else:
                discovered[skill.name] = (pack, skill)
    if not discovered:
        checks.append(Check("FAIL", "collection", "no shipping skills found"))
    names = sorted(discovered) if selected is None else sorted(set(selected))
    for name in names:
        if not NAME.fullmatch(name) or len(name) > 64 or name not in discovered:
            checks.append(Check("FAIL", name, "unknown or invalid shipping skill"))
            continue
        pack, skill = discovered[name]
        try:
            metadata = validate_skill(skill)
            if pack.name == "developer-skills" and not (skill / "metadata.toml").is_file():
                raise ValueError("Developer Skills requires metadata.toml")
            if not (skill / "README.md").is_file():
                raise ValueError("missing README.md")
            bundle(pack, [name])
            body = (skill / "SKILL.md").read_text(encoding="utf-8")
            if not artifact_instructions(body):
                raise ValueError(f"missing nonempty {POLICY_HEADING} declaration")
            errors = []
            # Vendored upstream documentation retains its original link context.
            documents = [skill / "SKILL.md", skill / "README.md"]
            documents.extend((skill / "references").rglob("*.md"))
            for document in documents:
                for error in broken_links(document, root):
                    errors.append(f"{document.relative_to(root).as_posix()}: {error}")
            if errors:
                raise ValueError("; ".join(errors))
        except (OSError, ValueError) as error:
            checks.append(Check("FAIL", name, str(error)))
            continue
        checks.append(Check("PASS", name, "structure, metadata, manifest, local file links, artifact declaration"))
        if not metadata.get("compatible_agents"):
            checks.append(Check("NOT VERIFIED", name, "native agent compatibility"))
    checks.append(Check("NOT VERIFIED", "behavior", "artifact declaration presence does not prove ignore rules, run safety, or agent adherence; run helper tests and agent trials separately"))
    checks.append(Check("NOT VERIFIED", "links", "remote destinations and heading anchors are not checked"))
    checks.append(Check("NOT VERIFIED", "publication", "license approval and redistribution rights require owner review"))
    return checks


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    selection = parser.add_mutually_exclusive_group(required=True)
    selection.add_argument("--all", action="store_true", help="Check every shipping skill")
    selection.add_argument("--skill", metavar="NAME", help="Check one shipping skill")
    args = parser.parse_args(argv)
    try:
        checks = check_collection(ROOT, None if args.all else [args.skill])
    except (OSError, ValueError) as error:
        checks = [Check("FAIL", "collection", str(error))]
    for check in checks:
        print(f"{check.status}: {check.subject}: {check.detail}")
    failures = sum(check.status == "FAIL" for check in checks)
    passes = sum(check.status == "PASS" for check in checks)
    unverified = sum(check.status == "NOT VERIFIED" for check in checks)
    print(f"Static checks: {passes} PASS, {failures} FAIL, {unverified} NOT VERIFIED")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
