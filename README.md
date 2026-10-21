# Developer Skills

Fifteen independent development skills and an offline installer. Each skill is ordinary Markdown with portable name/description frontmatter and a metadata sidecar. No private runner, package installation, Docker, API key or network is required to install or read them.

Requires Python 3.11 or newer. From this checkout, preview an install into an existing project:

```powershell
py -3.11 .\tools\install_skills.py --agent both --project "D:\My App" --bundle essential --dry-run
py -3.11 .\tools\install_skills.py --agent both --project "D:\My App" --bundle essential
```

The second command asks for approval before writing. Essential contains only plan-review, blocker-check, phase-handoff and completion-check. Select one with `--skills blocker-check`; use `--bundle all` explicitly for all fifteen. No skill is executed by installation.

Read [INSTALL.md](INSTALL.md) for scoped paths, replacement, cancellation, recovery and troubleshooting; [SKILL_CATALOG.md](SKILL_CATALOG.md) for selection; [docs/SKILL_STANDARD.md](docs/SKILL_STANDARD.md) for validation and integrity; and [docs/COMPATIBILITY.md](docs/COMPATIBILITY.md) for actual native discovery proof and its limits.

Run the reproducible standard-library checks:

```powershell
py -3.11 -m unittest discover -s tests -v
```

The suite covers offline isolated projects, both agent destinations, one-skill/Essential/all selection, dry-run/cancel, idempotency, collisions, backups, junction rejection, checksums and interrupted-write recovery. Skill instructions have been inspected for standalone operation; discovery does not prove model behavior.

This checkout has no remote or published release. License selection is pending owner approval; `license_status = "UNDECIDED"` grants no redistribution rights. See [docs/PUBLISHING.md](docs/PUBLISHING.md).

Use [docs/RELEASE_CHECKLIST.md](docs/RELEASE_CHECKLIST.md) for both-runtime standalone checks, fresh committed-archive validation and the unresolved publication gates. Local source validation does not create a release or authenticate an external publisher.
