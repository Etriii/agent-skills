"""Keep standalone UI/UX skill payloads portable from one canonical resource owner."""

import argparse
from pathlib import Path
import sys

from catalog import safe_path


ROOT = Path(__file__).resolve().parents[1] / "packs/developer-skills/skills"
CANONICAL = "ultimate-ui-ux"
STANDALONE = ("ultimate-ui", "ultimate-ux", "ultimate-mobile")
RESOURCE_DIRS = ("references", "assets", "vendor")


def resources(skills_root: Path = ROOT) -> dict[str, bytes]:
    canonical = safe_path(skills_root / CANONICAL)
    paths = [canonical / "THIRD_PARTY.md"]
    for directory in RESOURCE_DIRS:
        paths.extend(path for path in (canonical / directory).rglob("*") if path.is_file())
    return {path.relative_to(canonical).as_posix(): safe_path(path).read_bytes() for path in paths}


def sync(skills_root: Path = ROOT, *, check: bool = False) -> list[str]:
    """Copy only suite-owned resources; check mode reports drift without writing."""
    payloads = resources(skills_root)
    drift = []
    for name in STANDALONE:
        root = safe_path(skills_root / name)
        existing = {"THIRD_PARTY.md"} if (root / "THIRD_PARTY.md").exists() else set()
        for directory in RESOURCE_DIRS:
            existing.update(path.relative_to(root).as_posix()
                            for path in (root / directory).rglob("*") if path.is_file())
        for relative in sorted(existing - payloads.keys()):
            drift.append(f"Unexpected resource: {name}/{relative}; review and remove explicitly")
        if not check and existing - payloads.keys():
            raise ValueError(f"Unexpected resources in {name}; review before synchronizing")
        for relative, data in payloads.items():
            target = safe_path(root / relative)
            if target.is_file() and target.read_bytes() == data:
                continue
            drift.append(f"Resource differs: {name}/{relative}")
            if not check:
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes(data)
    return drift


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Report resource drift without writing")
    args = parser.parse_args()
    try:
        drift = sync(check=args.check)
        if args.check and drift:
            print("\n".join(drift), file=sys.stderr)
            return 1
        print("UI/UX resources match" if args.check else "UI/UX resources synchronized; refresh the pack manifest")
        return 0
    except (OSError, ValueError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
