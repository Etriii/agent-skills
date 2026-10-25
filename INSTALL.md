# Installation

Use Python 3.11+ from the extracted collection root. No third-party package, API key, environment variable, database migration or network connection is required for installation. Existing optional QA document generation still requires `python-docx`; it is unrelated to installation.

## Choose a pack, agent and scope

```powershell
python tools/install_skills.py --pack developer-skills --list
python tools/install_skills.py --pack ultimate-qa --list
python tools/install_skills.py --pack developer-skills --agent both --project "D:\My App" --skills blocker-check phase-handoff --dry-run
python tools/install_skills.py --pack developer-skills --agent both --project "D:\My App" --skills blocker-check phase-handoff
```

Selection is explicit: `--skills <names...>`, `--bundle essential` (four developer skills), or `--bundle all` (the selected pack only). Essential contains plan-review, blocker-check, phase-handoff and completion-check. `--pack` defaults to developer-skills for the previous developer CLI; new commands should name the pack.

| Scope | Required arguments | Codex | Claude | Records |
|---|---|---|---|---|
| Project (default) | `--project <existing-root>` | `<root>/.agents/skills/<name>` | `<root>/.claude/skills/<name>` | `<root>/.agent-skills/history/` |
| User | `--scope user --user-home <existing-home>` | `<home>/.agents/skills/<name>` | `<home>/.claude/skills/<name>` | `<home>/.agent-skills/history/` |

`--agent` accepts codex, claude or both. The installer does not discover custom configuration homes or search legacy `.codex/skills` paths. Confirm your runtime's configured discovery location. The target root must already exist. It must be disjoint from the pack source; the tool never creates an application or Git repository. QA execution separately requires the application's Git root.

For a user install:

```powershell
python tools/install_skills.py --pack ultimate-qa --agent both --scope user --user-home "$env:USERPROFILE" --skills ultimate-qa ultimate-qa-client --dry-run
python tools/install_skills.py --pack ultimate-qa --agent both --scope user --user-home "$env:USERPROFILE" --skills ultimate-qa ultimate-qa-client
```

Review the displayed destinations and hashes, then type `y`. `--yes` approves that local operation for reviewed automation. `--dry-run` never writes destination files or records, even with `--yes`. Exit codes: 0 success/unchanged/preview; 1 validation or filesystem failure; 2 cancellation or argument parsing failure.

## Integrity and dependencies

Each selected skill must exactly match its pack's `SHA256SUMS`, including added or missing payload files. Developer metadata is validated when present. Ultimate QA also verifies the support files listed in its manifest. Paths, ancestors and descendants must be regular directories/files; links, junctions, traversal and special files are rejected.

`--source "D:\Reviewed Pack"` overrides the local pack directory. The source must contain `skills/` and `SHA256SUMS`; it is never fetched or executed. A separately trusted manifest can be pinned with `--expected-manifest-sha256 <64-lowercase-hex>`. A manifest provides integrity, not publisher authentication or a license grant.

Ultimate QA core/client copies receive `kit-location.txt` pointing at `packs/ultimate-qa`. Keep that pack and its support files available. After moving the collection, reinstall core/client with `--replace`; the prior copies are retained as backups. No `ULTIMATE_QA_KIT` environment setting is needed for these installed copies.

## Existing copies and replacement

Identical managed copies are unchanged, including history. An identical unrecorded copy can be adopted: installation records its digest without rewriting it, making later tracked uninstall possible. A conflicting tree, including added files or empty directories, is preserved unless replacement is explicit:

```powershell
python tools/install_skills.py --pack developer-skills --agent codex --project "D:\My App" --skills blocker-check --replace --dry-run
python tools/install_skills.py --pack developer-skills --agent codex --project "D:\My App" --skills blocker-check --replace
```

Replacement retains the exact old tree in `<scope-root>/.skills-install-backups/<operation-id>/backups/<entry-number>`. Its `journal.json` maps entry numbers to original paths. The Markdown record links the backup directory. Existing backups are never automatically pruned.

## Transactions and recovery

All selected copies and their Markdown record stage before changes begin. A shared `.skills-install-transaction/` directory excludes concurrent mutating operations in one scope. Content is checked after approval and again before each swap. File changes and their record commit together. Ordinary failures roll back; abrupt termination leaves a journal. Records are provisional while a transaction remains active.

After confirming the interrupted process has stopped:

```powershell
python tools/install_skills.py --agent both --project "D:\My App" --recover --dry-run
python tools/install_skills.py --agent both --project "D:\My App" --recover
```

Recovery rolls back prepared operations, including their records, or finishes backup archival for committed operations. Changed destinations/backups and malformed journals require inspection; preserve them. A command can return 1 after commit if archival fails: its record is already committed, and `--recover` finishes cleanup. Process interruption is tested; power-loss durability is not claimed.

For removal, use [UNINSTALL.md](UNINSTALL.md). For the persistent record schema, use [INSTALLATION_RECORDS.md](docs/INSTALLATION_RECORDS.md).
