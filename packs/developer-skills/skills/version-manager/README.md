# Version Manager

Plan and record a development-plan version transition while preserving accepted history.

## Install

Install globally for Codex with Node.js 22.20+ and npm:

```powershell
npx skills@1.7.4 add https://github.com/Etriii/agent-skills --skill version-manager --agent codex -g --copy
```

For a project install, run from the application directory and omit `-g`. For Claude Code, use `--agent claude-code`. Review the displayed destinations before proceeding.

For installation with checksums, retained backups and Markdown records, use Python 3.11+ from the downloaded collection root:

```powershell
python tools/install_skills.py --pack developer-skills --agent codex --project "D:\My App" --skills version-manager --dry-run
python tools/install_skills.py --pack developer-skills --agent codex --project "D:\My App" --skills version-manager
```

To install all related skills, follow the [Developer Skills pack guide](../../README.md).

## Use

Refresh the agent session, open the target application, and invoke this in agent chat:

```text
$version-manager Compare the current plan with the proposed next version. Preview the mapping and decisions requiring revalidation before writing.
```

In Claude Code use `/version-manager`. These are agent chat instructions, not terminal commands.

## Expected result and stopping point

Expect an old-to-new plan mapping, REUSE/REVALIDATE decisions and affected-file preview before transition consent. After consent, prior plans/evidence stay intact and the new version receives its own record. It does not execute the new plan.

Supply the selected task or subject and relevant paths in the request or conversation. This skill uses natural-language scope rather than a fixed set of subcommands; do not add another skill's `run`, `build` or `--auto` syntax.

## Prerequisites and limits

Provide both plans, completion evidence and the requested transition. Prior history remains immutable; transition consent precedes writes.

The skill itself needs no private runner, API key or third-party runtime package. It uses the target repository's existing tools where the requested checks require them. Installing instructions does not execute them or prove model adherence.

Read the complete [agent instructions](SKILL.md), [installation options](../../../../INSTALL.md), and [npx update/removal guide](../../../../docs/NPX_INSTALLATION.md#updates-and-removal). Use the installer that owns the copy for updates and removal. [Contribute](../../../../CONTRIBUTING.md).
