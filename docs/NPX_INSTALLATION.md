# Install with the skills CLI

The external [skills CLI](https://github.com/vercel-labs/skills) can install this collection's individual skills or all skills in a selected pack. These examples pin the verified CLI version, `1.7.4`, which requires Node.js 22.20+ and npm. Remote sources require network access; Git is needed when the CLI falls back to cloning. No collection-owned npm package or additional installer is required.

This is the recommended direct route. Ordinary skills do not require a manual Git clone, ZIP download or local Python script. The CLI obtains the published source. Keep the [optional Python installer](../INSTALL.md#optional-local-copy-for-python-and-offline-use) for offline installation, manifest checks, generated QA kit pointers, retained backups and Markdown operation history. Its examples require obtaining a complete local collection first. The tools have separate lifecycle records; use the owner of an existing copy for updates/removal.

## Prerequisites and starting folder

Install [Node.js 22.20+](https://nodejs.org/en/download), which supplies npm/npx, and [Git](https://git-scm.com/downloads) for repository fallback. Open a fresh terminal after installing missing tools. PowerShell, from any folder:

```powershell
node --version
npm --version
npx --version
git --version
```

Remote installation needs npm/GitHub connectivity and any access required for the selected source. Commands below run in PowerShell. Replace example paths and skill names before running them. npm can ask to download the pinned CLI; installation prompts vary by host. Run each command on its own line. `--list` discovers names; it is not a Python-style dry-run or proof that copies were installed.

## Individual skills

For a project install, change to the existing application folder first. This example selects only system-settings for both agents:

```powershell
Set-Location 'D:\My App'
npx skills@1.7.4 add https://github.com/Etriii/agent-skills --skill system-settings --agent codex claude-code --copy
```

Expected project result: `.agents/skills/system-settings/SKILL.md` for Codex and `.claude/skills/system-settings/SKILL.md` for Claude Code. From the same folder:

```powershell
Test-Path '.agents/skills/system-settings/SKILL.md'
Test-Path '.claude/skills/system-settings/SKILL.md'
```

Both should be `True` for the selected two-agent project install. Refresh the coding-agent session and invoke `$system-settings scan` in Codex chat or `/system-settings scan` in Claude Code. These chat requests are not terminal commands. For a different skill replace its name in the install, checks and chat request.

For global availability across projects, choose this alternative from any folder:

```powershell
npx skills@1.7.4 add https://github.com/Etriii/agent-skills --skill system-settings --agent codex claude-code -g --copy
```

Do not run both scope examples unless both copies are intended. Read the global destinations in the CLI summary; the relative project checks do not verify them. Select multiple skills with `--skill plan-review blocker-check`. For one agent use `--agent codex` or `--agent claude-code`. npx does not use Python's `--agent both`. Canonical storage and agent copies are managed by the external CLI.

Review the displayed source, selection, scope and destinations. `--copy` avoids requiring symlink privileges on Windows. Interactive terminal runs normally ask for approval; agent-driven runs may be noninteractive. These commands do not include `-y`. Security assessment availability and results are controlled by the external service; no assessment is promised by this repository.

## Complete packs

PowerShell, starting in the target application. List a pack, then select all skills in that source for both agents:

```powershell
npx skills@1.7.4 add https://github.com/Etriii/agent-skills/tree/main/packs/developer-skills --list
npx skills@1.7.4 add https://github.com/Etriii/agent-skills/tree/main/packs/developer-skills --skill '*' --agent codex claude-code --copy
```

Quote `'*'` so PowerShell passes it literally. Use a pack-specific source to select only that pack. Avoid the CLI's `--all` shorthand when targeting only Codex: that option also selects every agent and skips approval. The local developer pack has 30 skills; Ultimate QA has 9. Remote counts depend on the published revision. The [catalog](../SKILL_CATALOG.md) links to each skill's README.

## Ultimate QA support files

Core/client QA needs a durable kit containing templates, checklists and helpers after installation. Ordinary standalone skills do not require this extra source folder. Download the full collection ZIP with curl and install the QA selection from that same snapshot, without a manual Git clone. Python 3.11+ is a QA runtime requirement, not an npx installation requirement.

This Windows route also needs `curl.exe` and PowerShell's `Expand-Archive`. Verify them with `curl.exe --version` and `Get-Command Expand-Archive`; manual browser ZIP download/extraction can supply the same complete kit when needed.

PowerShell, from any folder. Replace `D:\My App` with the existing application. Choose a new durable `$qaKitFolder`; if you already have a matching kit, skip download/extraction and use the reuse instructions below.

```powershell
$qaKitFolder = 'D:\Tools\agent-skills-qa'
if (Test-Path -LiteralPath $qaKitFolder) { throw 'Reuse the existing QA kit, or choose a new kit folder.' }
New-Item -ItemType Directory -Path $qaKitFolder -ErrorAction Stop | Out-Null
curl.exe --fail --location --output "$qaKitFolder\agent-skills-main.zip" 'https://github.com/Etriii/agent-skills/archive/refs/heads/main.zip'
if ($LASTEXITCODE -ne 0) { throw 'QA kit download failed.' }
Expand-Archive -LiteralPath "$qaKitFolder\agent-skills-main.zip" -DestinationPath $qaKitFolder -ErrorAction Stop
$env:ULTIMATE_QA_KIT = Join-Path $qaKitFolder 'agent-skills-main\packs\ultimate-qa'
Set-Location 'D:\My App'
npx skills@1.7.4 add "$env:ULTIMATE_QA_KIT" --skill ultimate-qa ultimate-qa-client --agent codex claude-code --copy
```

`ULTIMATE_QA_KIT` is an existing skill setting, not a new runtime dependency. It must point to the actual pack root containing `01_QA_AGENT_PROMPT.md`, the checklist, templates and `tools/qa_preflight.py`. The PowerShell assignment applies to this terminal and child processes. Start the agent from this terminal, or give an already-running agent the absolute kit path when asked. Repeat the setting in a new terminal. Moving the collection requires updating the path. Do not point at the external CLI's temporary clone, which is removed after installation.

Expected result: the retained kit files exist, the selected core/client skills appear under the application's agent directories, and their installed source matches the kit snapshot. Check the kit without starting QA:

```powershell
Test-Path "$env:ULTIMATE_QA_KIT\01_QA_AGENT_PROMPT.md"
python "$env:ULTIMATE_QA_KIT\tools\qa_preflight.py" --help
Test-Path '.agents/skills/ultimate-qa/SKILL.md'
Test-Path '.claude/skills/ultimate-qa-client/SKILL.md'
```

Expect `True` for the file checks and helper usage output. To reuse the same kit later or install all nine QA skills from it:

```powershell
$env:ULTIMATE_QA_KIT = 'D:\Tools\agent-skills-qa\agent-skills-main\packs\ultimate-qa'
Set-Location 'D:\My App'
npx skills@1.7.4 add "$env:ULTIMATE_QA_KIT" --skill '*' --agent codex claude-code --copy
```

Choose the desired selection once; `'*'` means the complete QA pack at that kit path. To install only one standalone specialist, use the direct repository command with its explicit name and its documented prerequisites. Keep installed core/client copies and the retained kit on the same revision when updating.

Core and client workflows require the kit. Environment checks can use its preflight helper. Other QA specialists inspect the application's own tools and evidence; runtime requirements still depend on the selected checks. Python 3.11+ is needed for kit helpers, and optional Word reports require `python-docx` plus visual rendering. See the [QA pack guide](../packs/ultimate-qa/README.md).

The Python installer remains the simpler route when you want it to generate `kit-location.txt` automatically without setting an environment variable.

## Troubleshooting

| Symptom | Action |
|---|---|
| `node`, `npm` or `npx` is not recognized | Install Node.js 22.20+ with npm, reopen the terminal, and rerun the version checks. An old terminal may still have an old PATH. |
| PowerShell blocks `npx.ps1` or `npm.ps1` | Use `npx.cmd` or `npm.cmd` for the same command. Changing execution policy is not required for these examples. |
| GitHub/npm cannot be reached, Git is unavailable, or private access fails | Restore the required connectivity/tool/access and rerun the same selected source. Do not report an installation or silently choose an unrelated source. |
| A skill name is not found | Run `npx skills@1.7.4 add https://github.com/Etriii/agent-skills --list`. Confirm spelling and the published revision. New local edits may not be published. |
| You need an unpublished local skill | Acquire the complete source using the [optional ZIP/clone steps](../INSTALL.md#optional-local-copy-for-python-and-offline-use), then use that actual local root as the npx source. A remote command does not read an unpushed local branch. |
| `python tools/install_skills.py` cannot open the file | That optional route needs a local copy. Change to its inner root containing `tools/` and `packs/`; do not run the script relative to the target application folder. |
| A Python dry-run finished but no skill appears | Dry-run writes nothing. Run the separate changing command from the collection root and complete its confirmation. |
| Installed files exist but the skill is absent from chat | Confirm agent and scope, refresh/reopen the coding-agent session, then use the documented `$name` or `/name` request. A copy is not proof of native discovery in every runtime. |
| QA cannot find its kit | Check the retained kit path and helper files, set `ULTIMATE_QA_KIT` in the launching terminal, or provide that absolute path to the active agent. Never point it at the application or a deleted CLI temp folder. |
| The directory already contains a managed or edited copy | Save custom edits and use the owning installer's update/removal workflow. Do not use one installer's command to force ownership over the other's copy. |

This repository does not publish a curl-to-shell installation script. curl examples download a ZIP for the QA kit or optional local source; they do not execute downloaded code through a shell pipe.

## Updates and removal

Rerun the selected `add` command with the same source, agent and scope after reviewing changes. Keep the QA kit and installed skills on the same revision. External installs do not produce `.agent-skills/history/` records, validate this collection's `SHA256SUMS`, or use its guarded uninstall and retained backups.

Remove a skill installed by the external CLI with that CLI:

```powershell
npx skills@1.7.4 remove --skill blocker-check --agent codex -g
```

Omit `-g` for project scope and run from the original application directory. Supply explicit names for multiple removals. `--skill '*'` can remove unrelated skills in that scope; it does not mean only this collection or one pack. Save local edits before updates or removals. To remove copies managed by Python, follow [UNINSTALL.md](../UNINSTALL.md).

In CLI 1.7.4, removing only Codex can retain the shared `.agents/skills/<name>` directory and lock entry when another detected agent uses that same directory. The CLI can report success while the skill remains discoverable there. Check the actual directory after removal. If you intend to remove that named skill from **all agents in this scope**, omit `--agent`:

```powershell
npx skills@1.7.4 remove --skill blocker-check -g
```

This broader command removes only the named skill, but includes its copies for other agents. Use targeted removal when those copies should remain. The recorded Python installer has different ownership rules; do not use it to force-remove an external install.

## Verify a local change

Use an empty temporary application directory outside the collection. These commands use the current checkout rather than an unpushed remote branch:

```powershell
$collectionPath = (Get-Location).Path
$testProject = Join-Path ([System.IO.Path]::GetTempPath()) ('agent-skills-check-' + [guid]::NewGuid().ToString('N'))
New-Item -ItemType Directory -Path $testProject | Out-Null
Push-Location $testProject
try {
    npx skills@1.7.4 add $collectionPath --list
    npx skills@1.7.4 add $collectionPath --skill blocker-check --agent codex --copy
    Get-ChildItem .agents/skills
    npx skills@1.7.4 remove --skill blocker-check
} finally {
    Pop-Location
}
```

Repository discovery must list exactly the shipping skills, with no `sample-review` fixture. Repeat in separate empty temporary projects using `Join-Path $collectionPath 'packs/developer-skills'` and `Join-Path $collectionPath 'packs/ultimate-qa'` with `--skill '*'` to check 30 and 9 copied skills. Compare the installed files with the source, including READMEs and the core QA state script. Resolve the QA kit path and run its helper `--help` to verify access without starting a review. Do not use `-g` for fixture checks.

Remote GitHub commands install published files; they cannot validate local unpushed edits. Actual local and remote proof is recorded in [NPX_COMPATIBILITY.md](NPX_COMPATIBILITY.md). Installation and file discovery do not prove model adherence, actual application QA or security-service assessments.
