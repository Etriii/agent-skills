# Security Privacy Review

Trace trust boundaries, permissions and data handling for a scoped change.

## Install

Install globally for Codex with Node.js 22.20+ and npm:

```powershell
npx skills@1.7.4 add https://github.com/Etriii/agent-skills --skill security-privacy-review --agent codex -g --copy
```

For a project install, run from the application directory and omit `-g`. For Claude Code, use `--agent claude-code`. Review the displayed destinations before proceeding.

For installation with checksums, retained backups and Markdown records, use Python 3.11+ from the downloaded collection root:

```powershell
python tools/install_skills.py --pack developer-skills --agent codex --project "D:\My App" --skills security-privacy-review --dry-run
python tools/install_skills.py --pack developer-skills --agent codex --project "D:\My App" --skills security-privacy-review
```

To install all 15 related skills, follow the [Developer Skills pack guide](../../README.md).

## Use

Refresh the agent session, open the target application, and invoke this in agent chat:

```text
$security-privacy-review Review the export workflow for object authorization, secret exposure, recipients and retention policy.
```

In Claude Code use `/security-privacy-review`. These are agent chat instructions, not terminal commands.

## Prerequisites and limits

Provide data flows, roles and authoritative policy. Intrusive testing, production access and privacy-policy decisions require their own authorization.

The skill itself needs no private runner, API key or third-party runtime package. It uses the target repository's existing tools where the requested checks require them. Installing instructions does not execute them or prove model adherence.

Read the complete [agent instructions](SKILL.md), [installation options](../../../../INSTALL.md), and [npx update/removal guide](../../../../docs/NPX_INSTALLATION.md#updates-and-removal). Use the installer that owns the copy for updates and removal. [Contribute](../../../../CONTRIBUTING.md).
