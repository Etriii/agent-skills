# Installation

## Direct installation with npx (recommended)

Ordinary skills install directly from GitHub through npx. You do not need to clone this collection or find a local Python script first. Install [Node.js 22.20+](https://nodejs.org/en/download), which supplies npm/npx, and [Git](https://git-scm.com/downloads) for repository fallback. Remote installation needs network access to npm and GitHub. Open a fresh terminal after installing missing tools.

PowerShell, from any folder, check prerequisites:

```powershell
node --version
npm --version
npx --version
git --version
```

Replace `D:\My App` with your existing target project. Run each line separately:

```powershell
Set-Location 'D:\My App'
npx skills@1.7.4 add https://github.com/Etriii/agent-skills --skill system-settings --agent codex claude-code --copy
```

This selects only `system-settings` for Codex and Claude Code in that project. Replace its name with another skill from the [catalog](SKILL_CATALOG.md). Review the selected source, names, agents, scope and destinations in the CLI summary. npm may ask to download the pinned CLI; the external installer can prompt too. These examples do not force approval. For one agent use `--agent codex` or `--agent claude-code`.

From that same project folder, verify the requested copies:

```powershell
Test-Path '.agents/skills/system-settings/SKILL.md'
Test-Path '.claude/skills/system-settings/SKILL.md'
```

Expect `True` for both. Refresh the coding-agent session, open the application, then type the skill's chat request, for example `$system-settings scan`. Installation does not execute the skill. For global availability, add `-g` to the npx command intentionally and verify the absolute destinations in its summary instead of the project-relative checks.

Remote commands use the published source; local unpushed changes are not available through them. Use `npx skills@1.7.4 add https://github.com/Etriii/agent-skills --list` to inspect published names. See the [npx guide](docs/NPX_INSTALLATION.md) for complete packs, scope, [troubleshooting](docs/NPX_INSTALLATION.md#troubleshooting), and update/removal ownership. No curl-to-shell installer is shipped; curl below downloads an archive without executing it.

**Ultimate QA core/client exception:** their templates/helpers must stay available after installation. Follow the [curl ZIP and npx setup](docs/NPX_INSTALLATION.md#ultimate-qa-support-files) to keep the kit and installed skills on the same source snapshot. This does not require a manual Git clone. Standalone QA specialists have their own runtime requirements.

## Optional local copy for Python and offline use

Keep the Python workflow when you want manifest checks, retained backups, recovery and Markdown operation history, or local/offline installation. It requires Python 3.11+ and the complete collection on disk. `python tools/install_skills.py` means run that **local file**; it is not a globally installed command and does not download its own source.

Choose one acquisition route. Skip acquisition when you already have a reviewed complete copy, and use its actual root. Do not overwrite an existing checkout or extracted kit.

**Download ZIP with curl, without Git clone.** PowerShell, from any folder; replace the durable destination if needed:

This Windows example uses `curl.exe` and PowerShell's `Expand-Archive`. Check availability with `curl.exe --version` and `Get-Command Expand-Archive`; a browser ZIP download/extraction is the alternative below if those tools are unavailable.

```powershell
$collectionFolder = 'D:\Tools\agent-skills-download'
if (Test-Path -LiteralPath $collectionFolder) { throw 'Reuse the existing collection, or choose a new destination folder.' }
New-Item -ItemType Directory -Path $collectionFolder -ErrorAction Stop | Out-Null
curl.exe --fail --location --output "$collectionFolder\agent-skills-main.zip" 'https://github.com/Etriii/agent-skills/archive/refs/heads/main.zip'
if ($LASTEXITCODE -ne 0) { throw 'Collection download failed.' }
Expand-Archive -LiteralPath "$collectionFolder\agent-skills-main.zip" -DestinationPath $collectionFolder -ErrorAction Stop
Set-Location "$collectionFolder\agent-skills-main"
Get-Item '.\tools\install_skills.py'
```

Expected result: the extracted collection root contains `tools/`, `packs/`, `README.md`, and `tools/install_skills.py`. You can also use GitHub **Code > Download ZIP** and extract the complete archive manually, then open PowerShell in that same inner root. The folder containing only the ZIP is not the collection root.

**Optional Git clone alternative.** PowerShell, from any folder; the final destination must not already contain a checkout:

```powershell
New-Item -ItemType Directory -Path 'D:\Tools' -Force | Out-Null
git clone https://github.com/Etriii/agent-skills.git 'D:\Tools\agent-skills'
if ($LASTEXITCODE -ne 0) { throw 'Clone failed; resolve the error before using the destination.' }
Set-Location 'D:\Tools\agent-skills'
Get-Item '.\tools\install_skills.py'
```

For unpublished local changes, you may also use the complete local copy as an npx source, from the destination application:

```powershell
Set-Location 'D:\My App'
npx skills@1.7.4 add 'D:\Tools\agent-skills' --skill system-settings --agent codex claude-code --copy
```

Replace the source with the actual extracted/cloned root. This local-source alternative does require a local copy; the ordinary GitHub npx route above does not require you to acquire one manually.

## Optional recorded installation with Python

After obtaining the collection, open PowerShell in its actual root, then check `python --version` for Python 3.11+. The Python installer uses only the standard library and works offline once the full source is available. No API key, third-party Python installation package, database migration or network connection is needed for the local copy operation. Skill execution can have additional runtime prerequisites.

Keep the collection root and destination application distinct: source scripts run from the collection; `--project` identifies the existing application. Substitute actual paths below. If `tools/install_skills.py` cannot be found, change to the root shown in the preceding steps before retrying. A failed preview is not an installation.

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
