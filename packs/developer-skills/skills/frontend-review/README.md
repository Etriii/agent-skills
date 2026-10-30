# Frontend Review

Review UI state ownership, forms, accessibility and responsive behavior with explicit evidence limits.

## Install

Install globally for Codex with Node.js 22.20+ and npm:

```powershell
npx skills@1.7.4 add https://github.com/Etriii/agent-skills --skill frontend-review --agent codex -g --copy
```

For a project install, run from the application directory and omit `-g`. For Claude Code, use `--agent claude-code`. Review the displayed destinations before proceeding.

For installation with checksums, retained backups and Markdown records, use Python 3.11+ from the downloaded collection root:

```powershell
python tools/install_skills.py --pack developer-skills --agent codex --project "D:\My App" --skills frontend-review --dry-run
python tools/install_skills.py --pack developer-skills --agent codex --project "D:\My App" --skills frontend-review
```

To install all related skills, follow the [Developer Skills pack guide](../../README.md).

## Use

Refresh the agent session, open the target application, and invoke this in agent chat:

```text
$frontend-review Review the request form's loading, validation, permission and mobile states. Identify any missing browser evidence.
```

In Claude Code use `/frontend-review`. These are agent chat instructions, not terminal commands.

## Expected result and stopping point

Expect prioritized findings by source/route with reproduction steps and required UI acceptance checks. Source, automated accessibility, rendered and manual evidence remain separate. The default review does not redesign screens.

Supply the selected task or subject and relevant paths in the request or conversation. This skill uses natural-language scope rather than a fixed set of subcommands; do not add another skill's `run`, `build` or `--auto` syntax.

## Prerequisites and limits

Provide routes, components, journeys and design references. A browser is required for rendered-state claims; source review alone cannot establish visual acceptance.

The skill itself needs no private runner, API key or third-party runtime package. It uses the target repository's existing tools where the requested checks require them. Installing instructions does not execute them or prove model adherence.

Read the complete [agent instructions](SKILL.md), [installation options](../../../../INSTALL.md), and [npx update/removal guide](../../../../docs/NPX_INSTALLATION.md#updates-and-removal). Use the installer that owns the copy for updates and removal. [Contribute](../../../../CONTRIBUTING.md).
