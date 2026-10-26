# Blocker Check

Find requirement, policy, dependency and environment blockers before implementation.

## Install

Install globally for Codex with Node.js 22.20+ and npm:

```powershell
npx skills@1.7.4 add https://github.com/Etriii/agent-skills --skill blocker-check --agent codex -g --copy
```

For a project install, run from the application directory and omit `-g`. For Claude Code, use `--agent claude-code`. Review the displayed destinations before proceeding.

For installation with checksums, retained backups and Markdown records, use Python 3.11+ from the downloaded collection root:

```powershell
python tools/install_skills.py --pack developer-skills --agent codex --project "D:\My App" --skills blocker-check --dry-run
python tools/install_skills.py --pack developer-skills --agent codex --project "D:\My App" --skills blocker-check
```

To install all 15 related skills, follow the [Developer Skills pack guide](../../README.md).

## Use

Refresh the agent session, open the target application, and invoke this in agent chat:

```text
$blocker-check Check blockers for phase 2 in docs/plan.md. Cite authoritative sources and separate independent policy questions.
```

In Claude Code use `/blocker-check`. These are agent chat instructions, not terminal commands.

## Prerequisites and limits

Provide the selected scope, requirements and existing decisions. The skill identifies unresolved policy; it does not decide it.

The skill itself needs no private runner, API key or third-party runtime package. It uses the target repository's existing tools where the requested checks require them. Installing instructions does not execute them or prove model adherence.

Read the complete [agent instructions](SKILL.md), [installation options](../../../../INSTALL.md), and [npx update/removal guide](../../../../docs/NPX_INSTALLATION.md#updates-and-removal). Use the installer that owns the copy for updates and removal. [Contribute](../../../../CONTRIBUTING.md).
