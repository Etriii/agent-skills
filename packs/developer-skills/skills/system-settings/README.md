# System Settings

Inspect an application's workflows and configuration, decide whether runtime system settings are justified, and plan or implement only the selected scope. Works with established settings, partial implementations, and applications with none. A scan can recommend no new settings.

## Use

Run these in agent chat from the target application, or include its path:

```text
$system-settings scan
$system-settings scan checkout and delivery
$system-settings plan category loading and settings history
$system-settings build category loading using existing settings and audit owners
$system-settings verify category loading and settings history
$system-settings help
```

Claude Code uses `/system-settings` with the same arguments. These are agent instructions, not terminal commands. Bare invocation scans. Scan and plan do not edit application code or create files unless a saved artifact is requested. Build and equivalent natural-language requests authorize only the stated implementation scope; completing discovery never automatically starts implementation.

Discovery follows feature behavior and real consumers, not just settings folders. It distinguishes runtime business policy from deployment configuration, secrets, personal preferences, fixed invariants, feature flags, and tenant/store policy. Recommendations include source evidence, operator need, defaults, validation, categories, and exclusions. Missing source is an explicit coverage gap.

For a web administration interface, the preferred layout is one page with Settings and Change history tabs. Initial loading fetches category metadata. Expansion fetches that category's settings, preserving drafts and independent retry state. History loads only when opened and remains paginated and usable without loading every current setting. Existing framework and component conventions still apply.

The skill reuses existing settings history and central auditing before proposing new storage. When auditing is absent, it specifies minimal transactional settings history. It covers permissions, actor identity, truthful previous/new values, stale edits, concurrent writes, cache freshness, migration compatibility, and relevant verification. It does not add unrelated configurable policies or a general audit platform.

Read the complete [agent instructions](SKILL.md) and their linked discovery and implementation references.

## Inspect and implement in one request

For a known implementation objective, use this in agent chat:

```text
$system-settings build category loading and transactional settings history using existing settings, consumers and audit owners
```

`build` inspects the current implementation, specifies the selected changes, implements them and verifies them without requiring a preceding `scan` or `plan`. Reuse already-covered behavior. A scan may still conclude that no settings should be added; it does not grant permission to implement every candidate. This skill defines no `--auto` flag. Material unresolved policy choices block dependent work while independent authorized work continues.

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
npx skills@1.7.4 add https://github.com/Etriii/agent-skills --skill system-settings --agent codex claude-code --copy
```

This selects only `system-settings` for Codex and Claude Code in the current project. Review the selected source, agents, scope and destinations in the CLI summary. npm may ask to download the pinned CLI; the skill installer may also prompt. These examples do not force noninteractive approval.

Still in the application folder, confirm the project copies:

```powershell
Test-Path '.agents/skills/system-settings/SKILL.md'
Test-Path '.claude/skills/system-settings/SKILL.md'
```

Both should return `True` for the two-agent project install. Refresh the coding-agent session, then use the chat requests in this README. Installation copies instructions; it does not run the skill.

For one agent, replace `--agent codex claude-code` with `--agent codex` or `--agent claude-code`. For an intended global installation across projects, choose this alternative command after the same prerequisites; do not run both scope examples unless you want both copies:

```powershell
npx skills@1.7.4 add https://github.com/Etriii/agent-skills --skill system-settings --agent codex claude-code -g --copy
```

Global destinations are shown by the CLI; the project-relative `Test-Path` checks above do not verify global copies. Remote URLs install published files, so local unpushed changes are not included. PowerShell execution-policy errors can use `npx.cmd` instead of `npx`; see [troubleshooting](../../../../docs/NPX_INSTALLATION.md#troubleshooting) for missing tools, names, network access and refresh issues.

### Optional recorded or offline installation with Python

Keep this route when you want manifest verification, retained backups and Markdown operation history. It requires Python 3.11+ and a **complete local collection** first. Follow [download/extract or clone steps](../../../../INSTALL.md#optional-local-copy-for-python-and-offline-use), then identify the root containing `tools/`, `packs/`, and `README.md`. `tools/install_skills.py` is a file in that root, not a global command.

PowerShell: replace `D:\Tools\agent-skills` with that actual collection root and `D:\My App` with the existing destination application. For a ZIP, the extracted root may instead end in `agent-skills-main`.

```powershell
Set-Location 'D:\Tools\agent-skills'
python --version
python tools/install_skills.py --pack developer-skills --agent both --project "D:\My App" --skills system-settings --dry-run
python tools/install_skills.py --pack developer-skills --agent both --project "D:\My App" --skills system-settings
```

The first installer command previews and writes nothing. The second requests the existing confirmation and performs the copy with operation records. Run them separately. Python uses `--agent both`; npx uses `--agent codex claude-code`. For Python-only Codex or Claude choose `--agent codex` or `--agent claude`. User-scope options are in the [installation guide](../../../../INSTALL.md#choose-a-pack-agent-and-scope).

Use the installer that owns an existing copy for updates/removal; npx and Python maintain different records and protections. Preserve local edits before replacement. See the [pack guide](../../README.md), [npx lifecycle](../../../../docs/NPX_INSTALLATION.md#updates-and-removal), and [recorded removal guide](../../../../UNINSTALL.md).

## Prerequisites and evidence limits

Provide application source access and the requested scope. Runtime verification additionally needs the application's normal test tools, services, database, and permitted accounts as applicable. Reuse installed dependencies; the skill adds no service, runtime package, environment variable, or dependency on another skill.

Installation and structural checks do not prove native discovery, model adherence, browser behavior, database concurrency, or production safety. Compatibility metadata records only separately verified native discovery adapters. Application builds, migrations, deployment, and profile installation remain subject to task authorization.

Primary category: Implementation and change safety. Essential defaults remain unchanged. License status remains [UNDECIDED](../../../../LICENSE.md). Follow the [contribution guide](../../../../CONTRIBUTING.md).
