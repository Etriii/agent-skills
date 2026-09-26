"""Offline standalone skill installer. Run --help for reviewed scope options."""

import argparse
from pathlib import Path
import sys

from catalog import ESSENTIAL, bundle, digest, safe_path
from transaction import BACKUPS, TRANSACTION, install, recover


def parser() -> argparse.ArgumentParser:
    result = argparse.ArgumentParser(description=__doc__)
    result.add_argument("--source", type=Path, default=Path(__file__).resolve().parents[1], help="Local bundle root; archives and network sources are unsupported")
    result.add_argument("--agent", required=True, choices=("codex", "claude", "both"))
    result.add_argument("--scope", default="project", choices=("project", "user"))
    result.add_argument("--project", type=Path, help="Existing project root")
    result.add_argument("--user-home", type=Path, help="Explicit verified runtime home for user scope; required with --scope user")
    selection = result.add_mutually_exclusive_group()
    selection.add_argument("--skills", nargs="+")
    selection.add_argument("--bundle", choices=("essential", "all"))
    result.add_argument("--expected-manifest-sha256", help="Optional trusted pin for SHA256SUMS")
    result.add_argument("--dry-run", action="store_true")
    result.add_argument("--yes", action="store_true", help="Approve the displayed local copy plan without an interactive prompt")
    result.add_argument("--replace", action="store_true", help="Approve replacement of selected collisions with retained backups")
    result.add_argument("--recover", action="store_true", help="Recover a stopped transaction in the explicit scope; do not install")
    return result


def main(argv: list[str] | None = None) -> int:
    args = parser().parse_args(argv)
    try:
        if args.scope == "project":
            if args.project is None or args.user_home is not None:
                raise ValueError("Project scope requires --project and forbids --user-home")
            root = safe_path(args.project)
        else:
            if args.user_home is None or args.project is not None:
                raise ValueError("User scope requires an explicit --user-home and forbids --project")
            root = safe_path(args.user_home)
        if not root.is_dir():
            raise ValueError(f"Scope root must already exist: {root}")
        transaction = safe_path(root / TRANSACTION)
        safe_path(root / BACKUPS)
        if args.recover:
            if args.skills or args.bundle or args.replace:
                raise ValueError("Recovery cannot be combined with installation selection")
            print(f"Recover transaction: {transaction}")
            if args.dry_run:
                return 0
            if not args.yes and input("Approve recovery? [y/N] ").strip().lower() != "y":
                return 2
            print(recover(root))
            return 0
        if transaction.exists():
            raise ValueError(f"Active or interrupted transaction: {transaction}; ensure no installer is running, then review --recover")
        source = safe_path(args.source)
        if source == root or source in root.parents or root in source.parents:
            raise ValueError("Source bundle and destination scope must not overlap")
        if args.bundle == "all":
            names = sorted(p.name for p in (source / "skills").iterdir())
        elif args.bundle == "essential":
            names = list(ESSENTIAL)
        else:
            names = args.skills
        if not names or len(set(names)) != len(names):
            raise ValueError("Select unique --skills or an explicit --bundle")
        sources = bundle(source, names, args.expected_manifest_sha256)
        agents = ("codex", "claude") if args.agent == "both" else (args.agent,)
        copies = []
        for agent in agents:
            directory = ".agents" if agent == "codex" and args.scope == "project" else f".{agent}"
            for name, skill in sources.items():
                target = safe_path(root / directory / "skills" / name)
                before = digest(target) if target.exists() else None
                after = skill.content_sha256
                if before == after:
                    print(f"UNCHANGED {target}")
                    continue
                if before is not None and not args.replace:
                    raise ValueError(f"Collision preserved: {target}; review --replace with backup")
                print(f"{'REPLACE with backup' if before else 'COPY'} {skill.path} -> {target} sha256={after}")
                copies.append((skill.path, target, before, after))
        if not copies or args.dry_run:
            return 0
        if not args.yes and input("Approve these local copies? [y/N] ").strip().lower() != "y":
            print("Cancelled; no files written")
            return 2
        install(root, copies)
        print(f"Installed {len(copies)} selected copies; retained backups, if any: {root / BACKUPS}")
        return 0
    except (OSError, ValueError, EOFError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 1
    except KeyboardInterrupt:
        print("Cancelled; inspect --recover if a transaction remains", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
