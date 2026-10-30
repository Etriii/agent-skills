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

PowerShell, starting in the local collection root; Python 3.11+:

```powershell
python tools/install_skills.py --pack developer-skills --agent both --project "D:\My App" --skills report-builder --dry-run
python tools/install_skills.py --pack developer-skills --agent both --project "D:\My App" --skills report-builder
```

Preview should select only this skill for both agents. The changing command uses the installer's existing confirmation and records. Choose `--agent codex` or `--agent claude` for one agent. Refresh the agent session after installation.

For a published copy, the external CLI can install it with Node.js 22.20+ and npm:

```powershell
npx skills@1.7.4 add https://github.com/Etriii/agent-skills --skill report-builder --agent codex --copy
```

Run from the target application for project scope. The remote command requires the change to have been published; a local merge does not publish it. See the [pack guide](../../README.md), [installation options](../../../../INSTALL.md), [npx guide](../../../../docs/NPX_INSTALLATION.md), and [removal guide](../../../../UNINSTALL.md).

## Prerequisites and evidence limits

Provide source access and the reporting scope. Runtime verification additionally needs the application's normal database, test tools, PDF/Excel libraries, worker, storage, scheduler, and permitted test accounts as applicable. Reuse installed tools; this skill adds no runtime dependencies or environment keys of its own.

Missing policy, source fields, historical data, rendering tools, roles, or runtime services remain explicit gaps. Static inspection, installation, and passing tests do not prove visual quality, model adherence, scheduled cleanup, or production behavior. Compatibility metadata records only verified native agent discovery.

License status remains [UNDECIDED](../../../../LICENSE.md). Follow the [contribution guide](../../../../CONTRIBUTING.md).
