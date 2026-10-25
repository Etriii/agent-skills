# Uninstall and reinstall

Use the same pack, agent and scope as installation. Run from the collection root. Preview first:

```powershell
python tools/install_skills.py --pack ultimate-qa --agent codex --project "D:\My App" --skills ultimate-qa-client --uninstall --dry-run
python tools/install_skills.py --pack ultimate-qa --agent codex --project "D:\My App" --skills ultimate-qa-client --uninstall
```

Remove every managed skill from one pack, for the selected agents:

```powershell
python tools/install_skills.py --pack developer-skills --agent both --project "D:\My App" --bundle all --uninstall --dry-run
python tools/install_skills.py --pack developer-skills --agent both --project "D:\My App" --bundle all --uninstall
```

For a user installation:

```powershell
python tools/install_skills.py --pack ultimate-qa --agent codex --scope user --user-home "$env:USERPROFILE" --bundle all --uninstall --dry-run
python tools/install_skills.py --pack ultimate-qa --agent codex --scope user --user-home "$env:USERPROFILE" --bundle all --uninstall
```

The tool validates the entire selection before removal. It removes only copies owned by the chosen pack in Markdown history and whose current digest matches the recorded installed digest. Unrecorded copies, local edits, linked paths and corrupted history stop the operation. `--bundle all --uninstall` uses installed history, so removed/renamed source skills remain removable. An absent copy is skipped; an already recorded missing copy is recorded as absent. Repeating an unchanged uninstall writes nothing.

Each removal moves the complete tree into `.skills-install-backups/<operation-id>/backups/<entry-number>`. Nothing is permanently deleted from the retained content backup. The accompanying `journal.json` maps each number to its former destination. A committed `operation.md` records the removal, old digest, prior install record and backup location. Application code, `.gitignore`, `qa-findings/`, other packs, other agents and old history remain intact. Empty agent directories can remain.

If removal fails before commit, the transaction restores removed trees and does not publish a success record. For abrupt interruption or incomplete archival, follow [INSTALL.md](INSTALL.md#transactions-and-recovery).

## Unrecorded or edited copies

For an existing copy identical to the reviewed source, run its install command first. This adopts the matching copy and records ownership without overwriting it. Then uninstall normally. Older standalone copies under `.codex/skills/` or custom paths are not scanned or claimed; use their original installer or inspect and remove their exact paths separately.

If you edited an installed skill, save those edits before proceeding. An approved install with `--replace` retains the edited tree as a backup and installs a known copy; that managed copy can then be uninstalled. There is no force-delete option.

## Reinstall or restore

Repeat the original install command to reinstall; a new Markdown event records the new installation. Refresh the agent's skill list afterward.

To restore a retained tree manually, inspect the backup's `journal.json`, confirm its exact original destination and verify the destination is absent. Copy only that numbered skill tree back. Preserve any existing destination first. A manual restore does not create an installation record; run a matching install to adopt it if tracked removal is needed later. Do not delete an entire agent directory or the history to uninstall one skill.

Backups and history remain until you explicitly archive or remove them. Keep `.agent-skills/`, `.skills-install-backups/` and `.skills-install-transaction/` out of application commits if they contain local paths or private skill content; the installer does not change application ignore rules.
