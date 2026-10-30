# Ultimate QA

Run a versioned initialize → audit → plan review of an existing application.

## Install

### Direct setup with curl and npx (recommended)

This skill needs the complete QA kit's templates and helpers after installation. This route downloads a ZIP with curl, retains it in a durable folder, and installs from that same snapshot with npx. A manual Git clone is not required. The QA workflow also requires Python 3.11+ at runtime; Word/client work has additional prerequisites below.

Prerequisites: [Node.js 22.20+](https://nodejs.org/en/download) with npm/npx, network access to npm/GitHub, and [Git](https://git-scm.com/downloads) for repository fallback. If a command is missing, install that prerequisite and reopen the terminal. These are installer prerequisites; the skill's runtime requirements are listed separately below.

PowerShell, from any folder, check tools first:

```powershell
node --version
npm --version
npx --version
git --version
curl.exe --version
Get-Command Expand-Archive
```

PowerShell: replace `D:\My App` with your existing application folder. Choose a new, durable kit directory for `$qaKitFolder`; do not use an external CLI's temporary source directory.

```powershell
$qaKitFolder = 'D:\Tools\agent-skills-qa'
if (Test-Path -LiteralPath $qaKitFolder) { throw 'Reuse the existing QA kit below, or choose a new kit folder.' }
New-Item -ItemType Directory -Path $qaKitFolder -ErrorAction Stop | Out-Null
curl.exe --fail --location --output "$qaKitFolder\agent-skills-main.zip" 'https://github.com/Etriii/agent-skills/archive/refs/heads/main.zip'
if ($LASTEXITCODE -ne 0) { throw 'QA kit download failed.' }
Expand-Archive -LiteralPath "$qaKitFolder\agent-skills-main.zip" -DestinationPath $qaKitFolder -ErrorAction Stop
$env:ULTIMATE_QA_KIT = Join-Path $qaKitFolder 'agent-skills-main\packs\ultimate-qa'
Set-Location 'D:\My App'
npx skills@1.7.4 add "$env:ULTIMATE_QA_KIT" --skill ultimate-qa --agent codex claude-code --copy
```

The selected skill and support files now come from the same downloaded source. Keep the kit folder available. To reuse that existing kit instead of downloading again, use:

```powershell
$env:ULTIMATE_QA_KIT = 'D:\Tools\agent-skills-qa\agent-skills-main\packs\ultimate-qa'
Set-Location 'D:\My App'
npx skills@1.7.4 add "$env:ULTIMATE_QA_KIT" --skill ultimate-qa --agent codex claude-code --copy
```

Set the kit path again in a new terminal and start the coding agent from this terminal in the application, or provide the absolute kit path to an already-running agent. The environment assignment applies to this process and its children; it does not reconfigure an agent already running elsewhere. The kit is not the application to review. See the [full QA setup](../../../../docs/NPX_INSTALLATION.md#ultimate-qa-support-files) for the complete pack and helper verification.

This selects only `ultimate-qa` for Codex and Claude Code in the current project. Review the selected source, agents, scope and destinations in the CLI summary. npm may ask to download the pinned CLI; the skill installer may also prompt. These examples do not force noninteractive approval.

Still in the application folder, confirm the project copies:

```powershell
Test-Path '.agents/skills/ultimate-qa/SKILL.md'
Test-Path '.claude/skills/ultimate-qa/SKILL.md'
```

Both should return `True` for the two-agent project install. Refresh the coding-agent session, then use the chat requests in this README. Installation copies instructions; it does not run the skill.

For one agent, replace `--agent codex claude-code` with `--agent codex` or `--agent claude-code`. For an intended global installation across projects, choose this alternative command after the same prerequisites and kit setup; do not run both scope examples unless you want both copies:

```powershell
npx skills@1.7.4 add "$env:ULTIMATE_QA_KIT" --skill ultimate-qa --agent codex claude-code -g --copy
```

Global destinations are shown by the CLI; the project-relative `Test-Path` checks above do not verify global copies. Remote URLs install published files, so local unpushed changes are not included. PowerShell execution-policy errors can use `npx.cmd` instead of `npx`; see [troubleshooting](../../../../docs/NPX_INSTALLATION.md#troubleshooting) for missing tools, names, network access and refresh issues.

### Optional recorded or offline installation with Python

Keep this route when you want manifest verification, retained backups and Markdown operation history. It requires Python 3.11+ and a **complete local collection** first. Follow [download/extract or clone steps](../../../../INSTALL.md#optional-local-copy-for-python-and-offline-use), then identify the root containing `tools/`, `packs/`, and `README.md`. `tools/install_skills.py` is a file in that root, not a global command.

PowerShell: replace `D:\Tools\agent-skills` with that actual collection root and `D:\My App` with the existing destination application. For a ZIP, the extracted root may instead end in `agent-skills-main`.

```powershell
Set-Location 'D:\Tools\agent-skills'
python --version
python tools/install_skills.py --pack ultimate-qa --agent both --project "D:\My App" --skills ultimate-qa --dry-run
python tools/install_skills.py --pack ultimate-qa --agent both --project "D:\My App" --skills ultimate-qa
```

The first installer command previews and writes nothing. The second requests the existing confirmation and performs the copy with operation records. Run them separately. Python uses `--agent both`; npx uses `--agent codex claude-code`. For Python-only Codex or Claude choose `--agent codex` or `--agent claude`. Core/client copies receive a persistent kit pointer to this local collection; keep that kit on disk. User-scope options are in the [installation guide](../../../../INSTALL.md#choose-a-pack-agent-and-scope).

Use the installer that owns an existing copy for updates/removal; npx and Python maintain different records and protections. Preserve local edits before replacement. See the [pack guide](../../README.md), [npx lifecycle](../../../../docs/NPX_INSTALLATION.md#updates-and-removal), and [recorded removal guide](../../../../UNINSTALL.md).

## Use

Refresh the agent session, open the target application repository, and invoke this in agent chat:

```text
$ultimate-qa run
```

In Claude Code use `/ultimate-qa`. These are agent chat instructions, not terminal commands. Use `status` to inspect progress; add `--client` only when client deliverables are wanted and the client skill is installed.

## Commands, continuation and expected output

Enter these in the same target application's agent chat:

| Request | Behavior and stopping point |
|---|---|
| `$ultimate-qa run` | Initialize or reconcile the active review, audit relevant areas, and produce the improvement plan in one workflow. Stop before implementation. |
| `$ultimate-qa run --client` | Complete that review, then prepare optional client deliverables when the client skill and document tools are available. Stop before implementing or sending them. |
| `$ultimate-qa initialize` | Complete intake, preflight and versioned state/template preparation. Use when setup alone is wanted. |
| `$ultimate-qa audit request creation and approval` | Audit the named scope in an initialized review; save findings and executed evidence. Replace the example scope. |
| `$ultimate-qa plan` | Build the improvement plan from current findings/gaps and existing plans. No automatic client files or implementation. |
| `$ultimate-qa status` | Read current version state, findings and next action without file changes. |
| `$ultimate-qa next-version` | Reconcile unresolved work against current evidence, preserve earlier versions, create the next version and audit for new issues. |

There is no `--auto` switch: `run` is the supported continuous intake/audit/plan request. It asks only unanswered intake questions and resumes after the reply. If setup or checks are blocked, provide the missing input/service and repeat the original invocation, retaining `--client` if supplied. `status` identifies the recorded next action; repeating a still-applicable completed `run` does not create another version. Use `next-version` explicitly for that transition.

Expected output lives under the verified application's `qa-findings/` root: version state, requirements, audit/gap reports, improvement plan, and evidence with commands/results. Optional client files appear only when requested. A missing state directs standalone `audit` or `plan` back to initialization. Bare invocation is not documented as a complete run; use `run` explicitly. `--client` does not convert the plan into implementation approval.

## Prerequisites and limits

Requires the complete QA kit, Python 3.11+, Git and an existing application repository. Use the application's own runtime, test accounts and safe environment. Docker-dependent checks remain blocked when Docker is unavailable. Client documents require the optional client skill.

The workflow stops at recommendations. Code implementation, destructive tests, deployment and sending documents need separate authorization.

Read the full [agent instructions](SKILL.md), [recorded installation guide](../../../../INSTALL.md), and [npx update/removal guide](../../../../docs/NPX_INSTALLATION.md#updates-and-removal). Use the installer that owns the copy for updates and removal. [Contribute](../../../../CONTRIBUTING.md).
