# Surgical Patch

Fix a specific defect or small behavior change with focused regression evidence at the responsible layer.

## Install

Use Python 3.11+ from the local collection root to preview and install into an existing application:

```powershell
python tools/install_skills.py --pack developer-skills --agent both --project "D:\My App" --skills surgical-patch --dry-run
python tools/install_skills.py --pack developer-skills --agent both --project "D:\My App" --skills surgical-patch
```

Choose `--agent codex` or `--agent claude` for a single agent. The installer verifies payloads and records approved changes with retained backups. See the [pack guide](../../README.md), [installation options](../../../../INSTALL.md) and [removal guide](../../../../UNINSTALL.md).

## Use

Refresh the agent session and invoke this in agent chat:

```text
$surgical-patch Fix the stale response overwrite and verify that the latest request remains authoritative.
```

In Claude Code use `/surgical-patch`. This is an agent instruction, not a terminal command.

With PhasePilot, add the skill to the project's desired selection and review the existing sync preview. Invoke it explicitly for the already authorized scope; the helper does not change automatic advisor routing, defaults or approvals. Follow the [workflow guide](../../../../docs/SKILL_WORKFLOWS.md#implementation-and-change-safety).

## Expected result and stopping point

Expect a root-cause fix, focused regression evidence and preserved surrounding behavior. The scoped fix request includes tracing, correction and checks; unrelated cleanup and failures remain separate.

Supply the selected task or subject and relevant paths in the request or conversation. This skill uses natural-language scope rather than a fixed set of subcommands; do not add another skill's `run`, `build` or `--auto` syntax.

## Prerequisites and limits

Provide the selected scope and relevant repository evidence. The skill needs no private runner, API key or third-party package; actual checks use the target project's tools and permissions. Installation and native discovery do not establish model adherence.

Read the complete [agent instructions](SKILL.md). License status remains [UNDECIDED](../../../../LICENSE.md). [Contribute](../../../../CONTRIBUTING.md).
