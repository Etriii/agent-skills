# Ultimate QA Environment

Check an isolated QA environment in dependency order and identify precise runtime blockers.

## Install

For automatic kit pointers, checksums, retained backups and Markdown records, use Python 3.11+ from the downloaded collection root:

```powershell
python tools/install_skills.py --pack ultimate-qa --agent codex --project "D:\My App" --skills ultimate-qa-environment --dry-run
python tools/install_skills.py --pack ultimate-qa --agent codex --project "D:\My App" --skills ultimate-qa-environment
```

For the external CLI, keep the complete collection in a durable folder and run from its root with Node.js 22.20+ and npm:

```powershell
npx skills@1.7.4 add ./packs/ultimate-qa --skill ultimate-qa-environment --agent codex -g --copy
```

For a project install, run from the application directory, use the absolute local pack path, and omit `-g`. For Claude Code use `--agent claude-code`. Review the destinations before proceeding. See the [npx guide](../../../../docs/NPX_INSTALLATION.md#ultimate-qa-support-files) for support-file setup and differences in installation records.

To install all nine skills or choose related specialists, follow the [Ultimate QA pack guide](../../README.md).

## Use

Refresh the agent session, open the target application repository, and invoke this in agent chat:

```text
$ultimate-qa-environment Check this application's documented Docker stack and database readiness. Report required setup before making environment changes.
```

In Claude Code use `/ultimate-qa-environment`. These are agent chat instructions, not terminal commands. For versioned reports integrated with the core workflow, also install `ultimate-qa` and invoke `$ultimate-qa run`.

## Expected result and stopping point

Expect ordered checks of Docker/Compose, service and database readiness, and app health, with concrete setup blockers. The example request stops before environment changes. Service starts require an authorized safe target; missing Docker does not prove an application defect.

Supply the target application, selected journeys/endpoints and authorized test environment in the request or conversation. This specialist accepts natural-language scope; it defines no generic `run`, `build` or `--auto` mode. When a current QA version exists, evidence belongs to that review. A standalone review does not silently create a complete versioned QA run.

## Prerequisites and limits

Uses the application's Docker/Compose configuration and documented health checks. Python 3.11+ and the full kit provide `tools/qa_preflight.py` when available. Missing tools block their dependent checks.

Starting services or changing the environment requires the applicable authorization. Never substitute production connections for disposable test data.

Read the full [agent instructions](SKILL.md), [recorded installation guide](../../../../INSTALL.md), and [npx update/removal guide](../../../../docs/NPX_INSTALLATION.md#updates-and-removal). Use the installer that owns the copy for updates and removal. [Contribute](../../../../CONTRIBUTING.md).
