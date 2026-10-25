"""Build validated installation and removal plans for one selected pack."""

from hashlib import sha256
from pathlib import Path

from catalog import ESSENTIAL, NAME, bundle, digest, files_in, fingerprint, safe_path


def scope_root(args) -> Path:
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
    return root


def selected_names(args, source, owners, agents) -> list[str]:
    if args.bundle == "essential":
        if args.pack != "developer-skills":
            raise ValueError("Essential belongs to developer-skills; select QA skills or --bundle all")
        names = list(ESSENTIAL)
    elif args.bundle == "all" and args.uninstall:
        directories = {".agents" if agent == "codex" else ".claude" for agent in agents}
        names = sorted({Path(target).name for target, owner in owners.items()
                        if owner["pack"] == args.pack and target.split("/")[0] in directories})
    elif args.bundle == "all":
        names = sorted(p.name for p in (source / "skills").iterdir())
    else:
        names = args.skills
    if names is None or len(set(names)) != len(names):
        raise ValueError("Select unique --skills or an explicit --bundle")
    if any(not NAME.fullmatch(name) or len(name) > 64 for name in names):
        raise ValueError("Invalid selected skill name")
    return names


def plan(args, source, root, owners, agents, names):
    """Validate the whole selection before approval or any destination changes."""
    sources = {} if args.uninstall else bundle(source, names, args.expected_manifest_sha256)
    copies, additions, entries, guards = [], {}, [], {}
    for agent in agents:
        directory = ".agents" if agent == "codex" else ".claude"
        for name in names:
            relative = f"{directory}/skills/{name}"
            target = safe_path(root / relative)
            before = digest(target) if target.exists() else None
            guards[target] = before
            owner = owners.get(relative)
            if owner and owner["pack"] != args.pack:
                raise ValueError(f"Destination belongs to another pack: {target}")
            if args.uninstall:
                if before is not None and not owner:
                    raise ValueError(f"Unmanaged skill preserved: {target}; install the matching copy first to record ownership")
                if owner and before is not None and before != owner["digest"]:
                    raise ValueError(f"Modified skill preserved: {target}; save edits or use install --replace before uninstalling")
                after = None
                action = "REMOVE" if before is not None else "MISSING"
                if before is not None:
                    copies.append((None, target, before, None))
                elif not owner:
                    print(f"NOT INSTALLED {target}")
                    continue
            else:
                skill = sources[name]
                generated = {}
                if name in {"ultimate-qa", "ultimate-qa-client"} and args.pack == "ultimate-qa":
                    generated["kit-location.txt"] = (str(source) + "\n").encode("utf-8")
                if generated:
                    rows = files_in(skill.path)
                    rows.update({key: sha256(value).hexdigest() for key, value in generated.items()})
                    directories = sorted(p.relative_to(skill.path).as_posix() for p in skill.path.rglob("*") if p.is_dir())
                    after = fingerprint(dict(sorted(rows.items())), directories)
                    additions[target] = generated
                else:
                    after = skill.content_sha256
                if before == after:
                    if owner and owner["digest"] == after:
                        print(f"UNCHANGED {target}")
                        continue
                    action = "ADOPT MATCHING COPY"
                else:
                    if before is not None and not args.replace:
                        raise ValueError(f"Collision preserved: {target}; review --replace with backup")
                    action = "REPLACE WITH BACKUP" if before is not None else "COPY"
                    copies.append((skill.path, target, before, after))
            print(f"{action} {target} before={before or 'absent'} after={after or 'absent'}")
            entries.append(dict(target=relative, action=action, before=before, after=after,
                                installed_record=owner["record"] if owner else None, backup_path=None))
    return copies, additions, entries, guards
