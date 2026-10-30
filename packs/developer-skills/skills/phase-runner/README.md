# Phase Runner

Execute one authorized ready phase with checkpoints, verification and a bounded handoff.

## Install

Install globally for Codex with Node.js 22.20+ and npm:

```powershell
npx skills@1.7.4 add https://github.com/Etriii/agent-skills --skill phase-runner --agent codex -g --copy
```

For a project install, run from the application directory and omit `-g`. For Claude Code, use `--agent claude-code`. Review the displayed destinations before proceeding.

For installation with checksums, retained backups and Markdown records, use Python 3.11+ from the downloaded collection root:

```powershell
python tools/install_skills.py --pack developer-skills --agent codex --project "D:\My App" --skills phase-runner --dry-run
python tools/install_skills.py --pack developer-skills --agent codex --project "D:\My App" --skills phase-runner
```

To install all related skills, follow the [Developer Skills pack guide](../../README.md).

## Use

Refresh the agent session, open the target application, and invoke this in agent chat:

```text
$phase-runner Execute only phase 2 in docs/plan.md after checking prerequisites and repository rules. Stop after its tests and handoff.
```

In Claude Code use `/phase-runner`. These are agent chat instructions, not terminal commands.

## Expected result and stopping point

Expect implementation of only the identified ready scope, relevant tests/checkpoints and a truthful handoff. It verifies prerequisites first and stops before another scope. Required integration without authorization remains MERGE_PENDING; the invocation is not a private CLI or unattended scheduler.

Supply the selected task or subject and relevant paths in the request or conversation. This skill uses natural-language scope rather than a fixed set of subcommands; do not add another skill's `run`, `build` or `--auto` syntax.

## Prerequisites and limits

Needs explicit phase scope, resolved blockers and the application's own tools. It does not provide a command runner or authorize later phases or integration.

The skill itself needs no private runner, API key or third-party runtime package. It uses the target repository's existing tools where the requested checks require them. Installing instructions does not execute them or prove model adherence.

Read the complete [agent instructions](SKILL.md), [installation options](../../../../INSTALL.md), and [npx update/removal guide](../../../../docs/NPX_INSTALLATION.md#updates-and-removal). Use the installer that owns the copy for updates and removal. [Contribute](../../../../CONTRIBUTING.md).
