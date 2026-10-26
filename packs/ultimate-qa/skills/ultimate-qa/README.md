# Ultimate QA

Run a versioned initialize → audit → plan review of an existing application.

## Install

For automatic kit pointers, checksums, retained backups and Markdown records, use Python 3.11+ from the downloaded collection root:

```powershell
python tools/install_skills.py --pack ultimate-qa --agent codex --project "D:\My App" --skills ultimate-qa --dry-run
python tools/install_skills.py --pack ultimate-qa --agent codex --project "D:\My App" --skills ultimate-qa
```

For the external CLI, keep the complete collection in a durable folder and run from its root with Node.js 22.20+ and npm:

```powershell
npx skills@1.7.4 add ./packs/ultimate-qa --skill ultimate-qa --agent codex -g --copy
$env:ULTIMATE_QA_KIT = (Resolve-Path ./packs/ultimate-qa).Path
```

Start the agent from this terminal so it inherits the existing `ULTIMATE_QA_KIT` setting, or provide the absolute kit path when asked. The setting lasts for this terminal and child processes; repeat it in a new terminal. Keep this kit available and update its path if moved. For a project install, run from the application directory, use the absolute local pack path, and omit `-g`. For Claude Code use `--agent claude-code`. Review the destinations before proceeding. See the [npx guide](../../../../docs/NPX_INSTALLATION.md#ultimate-qa-support-files) for support-file setup and differences in installation records.

To install all nine skills or choose related specialists, follow the [Ultimate QA pack guide](../../README.md).

## Use

Refresh the agent session, open the target application repository, and invoke this in agent chat:

```text
$ultimate-qa run
```

In Claude Code use `/ultimate-qa`. These are agent chat instructions, not terminal commands. Use `status` to inspect progress; add `--client` only when client deliverables are wanted and the client skill is installed.

## Prerequisites and limits

Requires the complete QA kit, Python 3.11+, Git and an existing application repository. Use the application's own runtime, test accounts and safe environment. Docker-dependent checks remain blocked when Docker is unavailable. Client documents require the optional client skill.

The workflow stops at recommendations. Code implementation, destructive tests, deployment and sending documents need separate authorization.

Read the full [agent instructions](SKILL.md), [recorded installation guide](../../../../INSTALL.md), and [npx update/removal guide](../../../../docs/NPX_INSTALLATION.md#updates-and-removal). Use the installer that owns the copy for updates and removal. [Contribute](../../../../CONTRIBUTING.md).
