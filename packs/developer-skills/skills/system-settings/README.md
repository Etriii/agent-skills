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

PowerShell, starting in the local collection root; Python 3.11+:

```powershell
python tools/install_skills.py --pack developer-skills --agent both --project "D:\My App" --skills system-settings --dry-run
python tools/install_skills.py --pack developer-skills --agent both --project "D:\My App" --skills system-settings
```

The preview selects only this skill for both agents. Use `--agent codex` or `--agent claude` for one agent. The changing command uses the installer's existing confirmation and operation records. Refresh the target agent session after installation.

To install from a local checkout with the external CLI, run this in PowerShell from the target application and replace the source path:

```powershell
npx skills@1.7.4 add "D:\Path\To\agent-skills\packs\developer-skills" --skill system-settings --agent codex --copy
```

This route requires Node.js 22.20+ and npm, with network access if the pinned CLI is not cached. Remote GitHub installation requires the skill to be published first. See the [pack guide](../../README.md), [installation options](../../../../INSTALL.md), [npx guide](../../../../docs/NPX_INSTALLATION.md), and [removal guide](../../../../UNINSTALL.md).

## Prerequisites and evidence limits

Provide application source access and the requested scope. Runtime verification additionally needs the application's normal test tools, services, database, and permitted accounts as applicable. Reuse installed dependencies; the skill adds no service, runtime package, environment variable, or dependency on another skill.

Installation and structural checks do not prove native discovery, model adherence, browser behavior, database concurrency, or production safety. Compatibility metadata records only separately verified native discovery adapters. Application builds, migrations, deployment, and profile installation remain subject to task authorization.

Primary category: Implementation and change safety. Essential defaults remain unchanged. License status remains [UNDECIDED](../../../../LICENSE.md). Follow the [contribution guide](../../../../CONTRIBUTING.md).
