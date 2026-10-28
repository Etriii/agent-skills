# Investigate First

Diagnose unclear or intermittent failures before proposing code changes using evidence and bounded reproduction.

## Install

Use Python 3.11+ from the local collection root to preview and install into an existing application:

```powershell
python tools/install_skills.py --pack developer-skills --agent both --project "D:\My App" --skills investigate-first --dry-run
python tools/install_skills.py --pack developer-skills --agent both --project "D:\My App" --skills investigate-first
```

Choose `--agent codex` or `--agent claude` for a single agent. The installer verifies payloads and records approved changes with retained backups. See the [pack guide](../../README.md), [installation options](../../../../INSTALL.md) and [removal guide](../../../../UNINSTALL.md).

## Use

Refresh the agent session and invoke this in agent chat:

```text
$investigate-first Diagnose the intermittent request failure and identify its responsible owner before editing.
```

In Claude Code use `/investigate-first`. This is an agent instruction, not a terminal command.

With PhasePilot, add the skill to the project's desired selection and review the existing sync preview. Invoke it explicitly for the already authorized scope; the helper does not change automatic advisor routing, defaults or approvals. Follow the [workflow guide](../../../../docs/SKILL_WORKFLOWS.md#implementation-and-change-safety).

## Prerequisites and limits

Provide the selected scope and relevant repository evidence. The skill needs no private runner, API key or third-party package; actual checks use the target project's tools and permissions. Installation and native discovery do not establish model adherence.

Read the complete [agent instructions](SKILL.md). License status remains [UNDECIDED](../../../../LICENSE.md). [Contribute](../../../../CONTRIBUTING.md).
