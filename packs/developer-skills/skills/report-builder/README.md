# Report Builder

Discover reporting needs across an application, specify useful business reports, and implement role-aware report pages with styled PDF and Excel exports.

## Automatic scan and build

Open the target application in your coding agent. If this skill is not installed there, follow [Install](#install) first. Paste this into **agent chat**, not PowerShell or another terminal:

```text
$report-builder build all clearly justified missing reports across this project --detail detailed
```

This is one continuous scan, selection, implementation, and verification request. You do not need to run `scan` or `plan` first. The words after `build` define the authorized scope; there is no separate `auto` subcommand or `--auto` flag.

For core report content, use:

```text
$report-builder build all clearly justified missing reports across this project --detail mid
```

For Claude Code, use the same request with `/report-builder`:

```text
/report-builder build all clearly justified missing reports across this project --detail detailed
```

If the target is outside the open project, identify it in the same chat message, for example:

```text
$report-builder build all clearly justified missing reports across this project --detail detailed
Target application: D:\My App
```

The run should:

1. Trace features, pages, workflows, source data, roles, permissions, and existing reports across the selected application.
2. Classify reporting needs as Required, Recommended, Covered, Unknown, or Unnecessary. Select Required and Recommended gaps only when the audience, decision, metrics, and data boundaries are supported by evidence. Reuse existing reports that already meet the need.
3. Specify each eligible report and implement it through the existing owners, including necessary shared reporting infrastructure. Do not stop after producing an inventory or plan when implementation is authorized and unblocked.
4. Deliver the agreed PDF/Excel design, effective filters, status/type colors and counts, permission/data isolation, dedicated Generated Reports page, durable background generation with recoverable progress, and configurable 24-hour retention from successful completion.
5. Run relevant checks and return implemented reports, reused coverage, deferred candidates with reasons, executed verification, and remaining setup or manual checks.

Detailed mode adds supported analysis and explanations; mid mode keeps essential content. Both retain the same access, export design, correctness, progress, and retention requirements. Do not equate every page with a necessary report or invent historical data to fill a detailed section.

The agent continues without routine approval pauses for the authorized scope. It asks when material business rules, sharing authority, or another consequential choice cannot be established, and continues independent unblocked work. Missing source data, runtime services, credentials, or rendering tools remain explicit limitations. Covered reports are not duplicated, and Unknown or Unnecessary candidates are not automatically built. If no justified gap exists, the result can be no application changes with evidence explaining why.

This chat request runs in the current agent session; it does not install a recurring scanner or unattended agent. Background workers are part of the application reporting behavior it implements. It does not automatically execute itself on future feature changes. Existing installed copies must receive this documentation/instruction update before relying on the clarified workflow.

## Use

Run these in agent chat from the target application, or include its path:

```text
$report-builder scan
$report-builder scan inventory and sales
$report-builder plan sales --detail mid
$report-builder plan sales --detail detailed
$report-builder build sales --detail detailed
$report-builder verify sales
$report-builder help
```

Claude Code uses `/report-builder` with the same arguments. These are instructions to the agent, not terminal commands. Bare invocation scans; the default report detail is `mid`. Scan and plan are read-only unless a saved artifact is requested. Build implements only the selected scope and does not require repeating existing authorization.

Mid reports contain core figures, meaningful status/type counts, essential records, and metric notes. Detailed reports add supported analysis, exceptions, reconciliation, drilldowns, and fuller explanations. Both levels require effective-filter disclosure, role and data isolation, clean PDF and actual `.xlsx` exports, and retained generated files.

PDFs start with a system/organization cover, contents from page two, then a separate summary and report sections. Workbooks use Cover, Contents, Summary, Breakdowns, record sheets, and Reading Notes. Status/type colors follow the application's palette across screen and exports; counts reflect the full matching scope.

A dedicated Generated Reports page lists files available to their authorized audiences. Default availability is 24 hours from successful generation, configurable through backend settings or environment configuration. Shared downloads require access to every included section, record scope, and field; matching role names alone are insufficient.

Read the [agent instructions](SKILL.md) for command boundaries and linked discovery, document, access, lifecycle, and verification guidance.

## Background processing

Both export formats use durable backend jobs, preferably the application's existing workers. Generate returns a persisted request reference promptly. The dedicated Generated Reports table owns status and progress, showing queued/generating/ready/failed/expired states and measured stages or counts. Unknown totals use an indeterminate indicator rather than a fabricated percentage.

Reloading, navigating away, or closing the tab does not stop generation. Returning to Generated Reports reloads current authorized state from the server, using realtime updates or bounded polling. Retries and worker restarts must not lose accepted requests, publish duplicate/partial files, or leave stale jobs falsely running. The 24-hour retention clock starts when the complete file becomes ready.

## Install

This skill was previously named `report-creator`. Existing installed copies retain that name until replaced; no automatic alias or profile migration is performed. Use the same installer and scope that created the old copy, preserving any local edits. Python-managed copies remain removable by their recorded old name using the [removal guide](../../../../UNINSTALL.md); external CLI copies use its [removal workflow](../../../../docs/NPX_INSTALLATION.md#updates-and-removal). Install `report-builder` below and refresh the agent session.

### Direct install with npx (recommended)

No manual clone, ZIP download, or Python checkout is required to install this skill. The external CLI obtains the published source for you.

Prerequisites: [Node.js 22.20+](https://nodejs.org/en/download) with npm/npx, network access to npm/GitHub, and [Git](https://git-scm.com/downloads) for repository fallback. If a command is missing, install that prerequisite and reopen the terminal. These are installer prerequisites; the skill's runtime requirements are listed separately below.

PowerShell, from any folder, check tools first:

```powershell
node --version
npm --version
npx --version
git --version
```

PowerShell: replace `D:\My App` with your existing target application, then run each line separately:

```powershell
Set-Location 'D:\My App'
npx skills@1.7.4 add https://github.com/Etriii/agent-skills --skill report-builder --agent codex claude-code --copy
```

This selects only `report-builder` for Codex and Claude Code in the current project. Review the selected source, agents, scope and destinations in the CLI summary. npm may ask to download the pinned CLI; the skill installer may also prompt. These examples do not force noninteractive approval.

Still in the application folder, confirm the project copies:

```powershell
Test-Path '.agents/skills/report-builder/SKILL.md'
Test-Path '.claude/skills/report-builder/SKILL.md'
```

Both should return `True` for the two-agent project install. Refresh the coding-agent session, then use the chat requests in this README. Installation copies instructions; it does not run the skill.

For one agent, replace `--agent codex claude-code` with `--agent codex` or `--agent claude-code`. For an intended global installation across projects, choose this alternative command after the same prerequisites; do not run both scope examples unless you want both copies:

```powershell
npx skills@1.7.4 add https://github.com/Etriii/agent-skills --skill report-builder --agent codex claude-code -g --copy
```

Global destinations are shown by the CLI; the project-relative `Test-Path` checks above do not verify global copies. Remote URLs install published files, so local unpushed changes are not included. PowerShell execution-policy errors can use `npx.cmd` instead of `npx`; see [troubleshooting](../../../../docs/NPX_INSTALLATION.md#troubleshooting) for missing tools, names, network access and refresh issues.

### Optional recorded or offline installation with Python

Keep this route when you want manifest verification, retained backups and Markdown operation history. It requires Python 3.11+ and a **complete local collection** first. Follow [download/extract or clone steps](../../../../INSTALL.md#optional-local-copy-for-python-and-offline-use), then identify the root containing `tools/`, `packs/`, and `README.md`. `tools/install_skills.py` is a file in that root, not a global command.

PowerShell: replace `D:\Tools\agent-skills` with that actual collection root and `D:\My App` with the existing destination application. For a ZIP, the extracted root may instead end in `agent-skills-main`.

```powershell
Set-Location 'D:\Tools\agent-skills'
python --version
python tools/install_skills.py --pack developer-skills --agent both --project "D:\My App" --skills report-builder --dry-run
python tools/install_skills.py --pack developer-skills --agent both --project "D:\My App" --skills report-builder
```

The first installer command previews and writes nothing. The second requests the existing confirmation and performs the copy with operation records. Run them separately. Python uses `--agent both`; npx uses `--agent codex claude-code`. For Python-only Codex or Claude choose `--agent codex` or `--agent claude`. User-scope options are in the [installation guide](../../../../INSTALL.md#choose-a-pack-agent-and-scope).

Use the installer that owns an existing copy for updates/removal; npx and Python maintain different records and protections. Preserve local edits before replacement. See the [pack guide](../../README.md), [npx lifecycle](../../../../docs/NPX_INSTALLATION.md#updates-and-removal), and [recorded removal guide](../../../../UNINSTALL.md).

## Prerequisites and evidence limits

Provide source access and the reporting scope. Runtime verification additionally needs the application's normal database, test tools, PDF/Excel libraries, worker, storage, scheduler, and permitted test accounts as applicable. Reuse installed tools; this skill adds no runtime dependencies or environment keys of its own.

Missing policy, source fields, historical data, rendering tools, roles, or runtime services remain explicit gaps. Static inspection, installation, and passing tests do not prove visual quality, model adherence, scheduled cleanup, or production behavior. Compatibility metadata records only verified native agent discovery.

License status remains [UNDECIDED](../../../../LICENSE.md). Follow the [contribution guide](../../../../CONTRIBUTING.md).

## Generated artifact storage

When this workflow saves reports or run evidence, use its target-workspace output owner and a new UTC `YYYYMMDDTHHMMSSZ-<unique-id>/` run directory; preserve earlier runs. Before saving in Git, the skill preserves or creates the root `.gitignore`, adds only the required scoped output rule, and verifies exclusion. Tracked output is refused without automatic untracking. Non-Git exclusion remains unverified, and workflows requiring Git retain that prerequisite. Unsafe storage or failed exclusion is reported before persistence. Existing state/resume paths and deliberately tracked project documents remain compatible. See the installed [artifact instructions](SKILL.md#generated-artifacts); chat-only requests create no extra output.
