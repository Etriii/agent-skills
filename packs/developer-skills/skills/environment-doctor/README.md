# Environment Doctor

Inspect local tool availability, Git state and required services with read-only diagnostics.

## Install

Install globally for Codex with Node.js 22.20+ and npm:

```powershell
npx skills@1.7.4 add https://github.com/Etriii/agent-skills --skill environment-doctor --agent codex -g --copy
```

For a project install, run from the application directory and omit `-g`. For Claude Code, use `--agent claude-code`. Review the displayed destinations before proceeding.

For installation with checksums, retained backups and Markdown records, use Python 3.11+ from the downloaded collection root:

```powershell
python tools/install_skills.py --pack developer-skills --agent codex --project "D:\My App" --skills environment-doctor --dry-run
python tools/install_skills.py --pack developer-skills --agent codex --project "D:\My App" --skills environment-doctor
```

To install all related skills, follow the [Developer Skills pack guide](../../README.md).

## Use

Refresh the agent session, open the target application, and invoke this in agent chat:

```text
$environment-doctor Diagnose this workspace using its documented prerequisites. Report command exits without starting services or exposing secrets.
```

In Claude Code use `/environment-doctor`. These are agent chat instructions, not terminal commands.

## Prerequisites and limits

Needs the project's documented local CLI tools. Docker is checked only when required. No diagnostics engine is bundled; the agent runs read-only checks.

The skill itself needs no private runner, API key or third-party runtime package. It uses the target repository's existing tools where the requested checks require them. Installing instructions does not execute them or prove model adherence.

Read the complete [agent instructions](SKILL.md), [installation options](../../../../INSTALL.md), and [npx update/removal guide](../../../../docs/NPX_INSTALLATION.md#updates-and-removal). Use the installer that owns the copy for updates and removal. [Contribute](../../../../CONTRIBUTING.md).
