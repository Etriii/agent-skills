# Ultimate QA API

Test API contracts, authentication, idempotency, error handling and persisted effects.

## Install

For automatic kit pointers, checksums, retained backups and Markdown records, use Python 3.11+ from the downloaded collection root:

```powershell
python tools/install_skills.py --pack ultimate-qa --agent codex --project "D:\My App" --skills ultimate-qa-api --dry-run
python tools/install_skills.py --pack ultimate-qa --agent codex --project "D:\My App" --skills ultimate-qa-api
```

For the external CLI, keep the complete collection in a durable folder and run from its root with Node.js 22.20+ and npm:

```powershell
npx skills@1.7.4 add ./packs/ultimate-qa --skill ultimate-qa-api --agent codex -g --copy
```

For a project install, run from the application directory, use the absolute local pack path, and omit `-g`. For Claude Code use `--agent claude-code`. Review the destinations before proceeding. See the [npx guide](../../../../docs/NPX_INSTALLATION.md#ultimate-qa-support-files) for support-file setup and differences in installation records.

To install all nine skills or choose related specialists, follow the [Ultimate QA pack guide](../../README.md).

## Use

Refresh the agent session, open the target application repository, and invoke this in agent chat:

```text
$ultimate-qa-api Review the cancellation API with authorized test accounts and disposable data. Verify denied requests and duplicate submission effects.
```

In Claude Code use `/ultimate-qa-api`. These are agent chat instructions, not terminal commands. For versioned reports integrated with the core workflow, also install `ultimate-qa` and invoke `$ultimate-qa run`.

## Prerequisites and limits

Needs route/schema information, the project's integration tooling and an authorized disposable database for writes. Use the documented test container when available.

Capture response and persistence evidence together. The skill does not authorize production writes or invent undocumented endpoints.

Read the full [agent instructions](SKILL.md), [recorded installation guide](../../../../INSTALL.md), and [npx update/removal guide](../../../../docs/NPX_INSTALLATION.md#updates-and-removal). Use the installer that owns the copy for updates and removal. [Contribute](../../../../CONTRIBUTING.md).
