# Offline installation

Use a reviewed local checkout and Python >=3.11. Run commands from this repository. The target root must already exist; the installer never creates an application or initializes Git.

## Preview, approve, use

```powershell
py -3.11 .\tools\install_skills.py --agent both --scope project --project "D:\My App" --bundle essential --dry-run
py -3.11 .\tools\install_skills.py --agent both --scope project --project "D:\My App" --bundle essential
```

Review the exact source, destination and content digests, then type `y`. Any other response cancels (exit 2); EOF fails without writing (exit 1). For previously reviewed automation, `--yes` supplies local-copy approval. `--dry-run` writes nothing even with `--yes`. Successful and unchanged runs exit 0; validation/I/O errors exit 1.

Project destinations are `.agents/skills/<name>` for Codex and `.claude/skills/<name>` for Claude. No project ignore file or runtime state is edited. Restart or refresh the agent's skill list after installation; invoke the chosen generic name through its supported skill UI. See the compatibility evidence before assuming a runtime supports it.

```powershell
# Install exactly one skill into Codex only
py -3.11 .\tools\install_skills.py --agent codex --project "D:\My App" --skills blocker-check

# Explicit full catalog selection
py -3.11 .\tools\install_skills.py --agent both --project "D:\My App" --bundle all --dry-run
```

Essential is plan-review, blocker-check, phase-handoff and completion-check. Other skills are never implicitly added. Selection is mandatory. `--source "D:\Reviewed Skills"` chooses a different local bundle with `skills/` and `SHA256SUMS`. URLs and archives are unsupported; no remote fallback, extracted archive handling or hooks run.

## User scope

Project scope is the default. User scope requires both `--scope user` and an explicit existing `--user-home`; verify that the installed runtime uses the standard home layout before approval:

```powershell
py -3.11 .\tools\install_skills.py --agent both --scope user --user-home "C:\Users\me" --skills blocker-check --dry-run
```

This maps Codex to `<user-home>/.codex/skills` and Claude to `<user-home>/.claude/skills`. Custom runtime config-home layouts are unsupported; use project scope instead. User-scope layout tests use an isolated home, not the real host profile. No global install was performed during development verification.

## Integrity and repeat installs

Every selected payload must match its entries in `SHA256SUMS`. The manifest is integrity evidence, not a signature or a license grant. For a trusted separately obtained manifest digest, add `--expected-manifest-sha256 <64-lowercase-hex>`. A mismatch fails before destination writes. Do not trust a digest merely because it arrived with an untrusted source.

Repeated copies with identical files and directories are unchanged. Added custom files or empty directories count as a collision. Links and Windows junctions in source, destinations, ancestors or transaction paths are rejected. Source and scope roots cannot overlap.

## Collisions, backup and recovery

Existing changed/unmanaged content is preserved by default. Review the selected collision and request a backup replacement explicitly:

```powershell
py -3.11 .\tools\install_skills.py --agent codex --project "D:\My App" --skills blocker-check --replace --dry-run
py -3.11 .\tools\install_skills.py --agent codex --project "D:\My App" --skills blocker-check --replace
```

The approval covers only listed skill destinations. Exact old trees are retained in `<scope-root>/.skills-install-backups/<transaction-id>/backups/<entry-number>`; `journal.json` maps each entry number to its original relative target. There is no automatic deletion of retained backups.

Copies stage and verify before the first destination change. A shared `<scope-root>/.skills-install-transaction` directory prevents concurrent installers. Ordinary exceptions and keyboard cancellation roll back swaps; an abrupt process exit leaves its journal for explicit recovery. Ensure the previous installer is stopped before recovery:

```powershell
py -3.11 .\tools\install_skills.py --agent both --project "D:\My App" --recover --dry-run
py -3.11 .\tools\install_skills.py --agent both --project "D:\My App" --recover
```

Recovery rolls back a prepared transaction or finishes backup archival for an already committed transaction. It checks all recorded targets and backups before changing them. Changed content or a corrupt/missing journal requires manual inspection; preserve the transaction directory and backups. Recovery is explicit and does not perform a new install. Process-interruption recovery is tested; power-loss durability is not claimed.

To restore an older backup after a successful replacement, review its journal and target, preserve the current target separately, and copy the exact backed-up skill to its recorded destination under your normal file-change approval. No automatic restore or uninstall command is supplied. Remove a skill manually only after verifying its selected path and ownership; never remove an entire agent directory to uninstall one skill.

## Troubleshooting

- Missing project/home: supply an existing root; a typo never creates one.
- Collision: inspect the current content and use an approved `--replace` with retained backup.
- Checksum mismatch: restore the reviewed source or pin; do not fall back to an unpinned version.
- Linked path: use a real directory; junction destinations are intentionally unsupported.
- Interrupted transaction: inspect its journal, stop any active installer and review `--recover`.
- Permission error: choose a permitted scope; the installer does not elevate itself.
- Skill absent from the agent UI: refresh/restart, confirm the path and consult `docs/COMPATIBILITY.md`.

No third-party Python imports, environment variables, database migrations or feature flags are required.
