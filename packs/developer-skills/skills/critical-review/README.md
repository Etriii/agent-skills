# Critical Review

Challenge unsupported assumptions and complexity using concrete failure paths and simpler alternatives.

## Install

Install globally for Codex with Node.js 22.20+ and npm:

```powershell
npx skills@1.7.4 add https://github.com/Etriii/agent-skills --skill critical-review --agent codex -g --copy
```

For a project install, run from the application directory and omit `-g`. For Claude Code, use `--agent claude-code`. Review the displayed destinations before proceeding.

For installation with checksums, retained backups and Markdown records, use Python 3.11+ from the downloaded collection root:

```powershell
python tools/install_skills.py --pack developer-skills --agent codex --project "D:\My App" --skills critical-review --dry-run
python tools/install_skills.py --pack developer-skills --agent codex --project "D:\My App" --skills critical-review
```

To install all related skills, follow the [Developer Skills pack guide](../../README.md).

## Use

Refresh the agent session, open the target application, and invoke this in agent chat:

```text
$critical-review Challenge docs/plan.md using the current source. Report only substantiated concerns and the evidence needed to resolve them.
```

In Claude Code use `/critical-review`. These are agent chat instructions, not terminal commands.

## Prerequisites and limits

Provide a specific plan or diff and acceptance criteria. This review does not implement changes or expand the requested scope.

The skill itself needs no private runner, API key or third-party runtime package. It uses the target repository's existing tools where the requested checks require them. Installing instructions does not execute them or prove model adherence.

Read the complete [agent instructions](SKILL.md), [installation options](../../../../INSTALL.md), and [npx update/removal guide](../../../../docs/NPX_INSTALLATION.md#updates-and-removal). Use the installer that owns the copy for updates and removal. [Contribute](../../../../CONTRIBUTING.md).
