# Safe Refactor

Restructure code while preserving defined behavior and verifying public contracts before and after the change.

## Install

Use Python 3.11+ from the local collection root to preview and install into an existing application:

```powershell
python tools/install_skills.py --pack developer-skills --agent both --project "D:\My App" --skills safe-refactor --dry-run
python tools/install_skills.py --pack developer-skills --agent both --project "D:\My App" --skills safe-refactor
```

Choose `--agent codex` or `--agent claude` for a single agent. The installer verifies payloads and records approved changes with retained backups. See the [pack guide](../../README.md), [installation options](../../../../INSTALL.md) and [removal guide](../../../../UNINSTALL.md).

## Use

Refresh the agent session and invoke this in agent chat:

```text
$safe-refactor Consolidate the duplicated validation owner while preserving the existing API and error behavior.
```

In Claude Code use `/safe-refactor`. This is an agent instruction, not a terminal command.

With PhasePilot, add the skill to the project's desired selection and review the existing sync preview. Invoke it explicitly for the already authorized scope; the helper does not change automatic advisor routing, defaults or approvals. Follow the [workflow guide](../../../../docs/SKILL_WORKFLOWS.md#implementation-and-change-safety).

## Prerequisites and limits

Provide the selected scope and relevant repository evidence. The skill needs no private runner, API key or third-party package; actual checks use the target project's tools and permissions. Installation and native discovery do not establish model adherence.

Read the complete [agent instructions](SKILL.md). License status remains [UNDECIDED](../../../../LICENSE.md). [Contribute](../../../../CONTRIBUTING.md).
