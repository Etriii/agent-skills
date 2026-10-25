"""Install and uninstall local skill packs with transactional Markdown records."""

import argparse
from hashlib import sha256
from pathlib import Path
import sys

from catalog import NAME, bundle, digest, safe_path
from lifecycle import plan, scope_root, selected_names
from records import STATE, inventory
from operations import commit
from transaction import BACKUPS, TRANSACTION, install, recover


ROOT = Path(__file__).resolve().parents[1]


def parser() -> argparse.ArgumentParser:
    result = argparse.ArgumentParser(description=__doc__)
    result.add_argument("--pack", default="developer-skills", help="Collection under packs/ (default: developer-skills)")
    result.add_argument("--source", type=Path, help="Reviewed local pack root; no network or archive execution")
    result.add_argument("--agent", choices=("codex", "claude", "both"))
    result.add_argument("--scope", default="project", choices=("project", "user"))
    result.add_argument("--project", type=Path, help="Existing project root")
    result.add_argument("--user-home", type=Path, help="Explicit existing runtime home for user scope")
    selection = result.add_mutually_exclusive_group()
    selection.add_argument("--skills", nargs="+")
    selection.add_argument("--bundle", choices=("essential", "all"))
    actions = result.add_mutually_exclusive_group()
    actions.add_argument("--uninstall", action="store_true")
    actions.add_argument("--recover", action="store_true")
    actions.add_argument("--list", action="store_true", help="List the selected pack's skills without writing")
    result.add_argument("--expected-manifest-sha256")
    result.add_argument("--dry-run", action="store_true")
    result.add_argument("--yes", action="store_true", help="Approve the displayed local operation")
    result.add_argument("--replace", action="store_true", help="Replace changed content with a retained backup")
    return result


def main(argv: list[str] | None = None) -> int:
    args = parser().parse_args(argv)
    try:
        if not NAME.fullmatch(args.pack) or len(args.pack) > 64:
            raise ValueError("Invalid pack name")
        default_source = ROOT / "packs" / args.pack if (ROOT / "packs").is_dir() else ROOT
        source = safe_path(args.source or default_source)
        if args.list:
            for path in sorted((source / "skills").iterdir()):
                if (path / "SKILL.md").is_file():
                    print(path.name)
            return 0
        if not args.agent:
            raise ValueError("Select --agent codex, claude, or both")
        root = scope_root(args)
        transaction = safe_path(root / TRANSACTION)
        safe_path(root / BACKUPS)
        state = safe_path(root / STATE)
        if args.recover:
            if args.skills or args.bundle or args.replace:
                raise ValueError("Recovery cannot be combined with skill selection or replacement")
            print(f"Recover transaction: {transaction}")
            if args.dry_run:
                return 0
            if not args.yes and input("Approve recovery? [y/N] ").strip().lower() != "y":
                return 2
            print(recover(root))
            return 0
        if args.uninstall and (args.replace or args.expected_manifest_sha256):
            raise ValueError("Uninstall uses recorded ownership; --replace and manifest pins apply to installation")
        if transaction.exists():
            raise ValueError(f"Active or interrupted transaction: {transaction}; stop its process before --recover")
        if source == root or source in root.parents or root in source.parents:
            raise ValueError("Source bundle and destination scope must not overlap")
        owners, sequence = inventory(root)
        history_digest = digest(state) if state.exists() else None
        agents = ("codex", "claude") if args.agent == "both" else (args.agent,)
        names = selected_names(args, source, owners, agents)
        copies, additions, entries, guards = plan(args, source, root, owners, agents, names)
        if not entries:
            print("No changes; history left unchanged")
            return 0
        print(f"Markdown history: {root / STATE / 'history'}")
        print(f"Removed or replaced content is retained under: {root / BACKUPS}")
        if args.dry_run:
            return 0
        if not args.yes and input("Approve this local operation and its Markdown record? [y/N] ").strip().lower() != "y":
            print("Cancelled; no files written")
            return 2
        if not args.uninstall:
            bundle(source, names, args.expected_manifest_sha256)
        guards[state] = history_digest
        events = commit(root, [dict(operation="uninstall" if args.uninstall else "install",
            pack=args.pack, agent=args.agent, scope=args.scope,
            source=None if args.uninstall else str(source),
            manifest_sha256=sha256((source / "SHA256SUMS").read_bytes()).hexdigest() if not args.uninstall else None,
            entries=entries, copies=copies, additions=additions, guards=guards)])
        print(f"COMMITTED: {root / STATE / 'history' / events[0]['id'] / 'operation.md'}")
        return 0
    except (OSError, ValueError, EOFError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 1
    except KeyboardInterrupt:
        print("Cancelled; inspect --recover if a transaction remains", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
