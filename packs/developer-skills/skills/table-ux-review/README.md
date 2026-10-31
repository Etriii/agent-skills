# Table UX Review

Audit application tables and data grids for detail navigation, crowded row actions, and accessible interactions. The review inventories every table in scope, traces shared owners and role restrictions, and recommends which interactions to keep, move, or leave unchanged.

Same-tab detail links are the default, with native options to open a new tab. Explicit new-tab requirements are supported. More than three visible row actions triggers a review rather than automatic removal. Selection, editing, bulk workflows, and authorized access must survive any cleanup.

## Install

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
npx skills@1.7.4 add https://github.com/Etriii/agent-skills --skill table-ux-review --agent codex claude-code --copy
```

This selects only `table-ux-review` for Codex and Claude Code in the current project. Review the selected source, agents, scope and destinations in the CLI summary. npm may ask to download the pinned CLI; the skill installer may also prompt. These examples do not force noninteractive approval.

Still in the application folder, confirm the project copies:

```powershell
Test-Path '.agents/skills/table-ux-review/SKILL.md'
Test-Path '.claude/skills/table-ux-review/SKILL.md'
```

Both should return `True` for the two-agent project install. Refresh the coding-agent session, then use the chat requests in this README. Installation copies instructions; it does not run the skill.

For one agent, replace `--agent codex claude-code` with `--agent codex` or `--agent claude-code`. For an intended global installation across projects, choose this alternative command after the same prerequisites; do not run both scope examples unless you want both copies:

```powershell
npx skills@1.7.4 add https://github.com/Etriii/agent-skills --skill table-ux-review --agent codex claude-code -g --copy
```

Global destinations are shown by the CLI; the project-relative `Test-Path` checks above do not verify global copies. Remote URLs install published files, so local unpushed changes are not included. PowerShell execution-policy errors can use `npx.cmd` instead of `npx`; see [troubleshooting](../../../../docs/NPX_INSTALLATION.md#troubleshooting) for missing tools, names, network access and refresh issues.

### Optional recorded or offline installation with Python

Keep this route when you want manifest verification, retained backups and Markdown operation history. It requires Python 3.11+ and a **complete local collection** first. Follow [download/extract or clone steps](../../../../INSTALL.md#optional-local-copy-for-python-and-offline-use), then identify the root containing `tools/`, `packs/`, and `README.md`. `tools/install_skills.py` is a file in that root, not a global command.

PowerShell: replace `D:\Tools\agent-skills` with that actual collection root and `D:\My App` with the existing destination application. For a ZIP, the extracted root may instead end in `agent-skills-main`.

```powershell
Set-Location 'D:\Tools\agent-skills'
python --version
python tools/install_skills.py --pack developer-skills --agent both --project "D:\My App" --skills table-ux-review --dry-run
python tools/install_skills.py --pack developer-skills --agent both --project "D:\My App" --skills table-ux-review
```

The first installer command previews and writes nothing. The second requests the existing confirmation and performs the copy with operation records. Run them separately. Python uses `--agent both`; npx uses `--agent codex claude-code`. For Python-only Codex or Claude choose `--agent codex` or `--agent claude`. User-scope options are in the [installation guide](../../../../INSTALL.md#choose-a-pack-agent-and-scope).

Use the installer that owns an existing copy for updates/removal; npx and Python maintain different records and protections. Preserve local edits before replacement. See the [pack guide](../../README.md), [npx lifecycle](../../../../docs/NPX_INSTALLATION.md#updates-and-removal), and [recorded removal guide](../../../../UNINSTALL.md).

## Use

Refresh the agent session, open the target application, and enter this in agent chat:

```text
$table-ux-review Audit all tables in this application. Inventory detail navigation and row actions by role, recommend action placement, and identify unverified coverage. Report before editing.
```

For implementation, authorize the desired scope in the same request:

```text
$table-ux-review Audit and fix the orders tables. Reuse existing detail routes and menus, preserve selection and bulk approval, and verify keyboard navigation and relocated actions.
```

Claude Code uses `/table-ux-review`. These are agent chat instructions, not terminal commands. Expected output is an inventory with decisions and evidence, plus prioritized findings or authorized changes and their verification. A missing detail route is reported as a gap rather than created automatically.

## Prerequisites and limits

Provide the target application source, scope, and relevant workflows. Authorized local or staging browser access and suitable test roles/data are needed for runtime claims. If those are unavailable, the skill reports source findings and coverage gaps; browser or screen-reader acceptance remains unverified.

No private runner, API key, additional skill, or third-party runtime package is required by the skill itself. It uses the application's existing tools. Compatibility metadata remains unverified until native agent discovery is observed; installing files alone does not prove model adherence.

Read the [agent instructions](SKILL.md), [collection installation guide](../../../../INSTALL.md), and [update/removal options](../../../../docs/NPX_INSTALLATION.md#updates-and-removal). Use the installer that owns the copy for updates and removal. [Contribute](../../../../CONTRIBUTING.md).

## Generated artifact storage

When this workflow saves reports or run evidence, use its target-workspace output owner and a new UTC `YYYYMMDDTHHMMSSZ-<unique-id>/` run directory; preserve earlier runs. Before saving in Git, the skill preserves or creates the root `.gitignore`, adds only the required scoped output rule, and verifies exclusion. Tracked output is refused without automatic untracking. Non-Git exclusion remains unverified, and workflows requiring Git retain that prerequisite. Unsafe storage or failed exclusion is reported before persistence. Existing state/resume paths and deliberately tracked project documents remain compatible. See the installed [artifact instructions](SKILL.md#generated-artifacts); chat-only requests create no extra output.
