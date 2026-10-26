# Ultimate QA Client

Prepare optional client reports and approval checklists, preserving returned decisions.

## Install

For automatic kit pointers, checksums, retained backups and Markdown records, use Python 3.11+ from the downloaded collection root:

```powershell
python tools/install_skills.py --pack ultimate-qa --agent codex --project "D:\My App" --skills ultimate-qa-client --dry-run
python tools/install_skills.py --pack ultimate-qa --agent codex --project "D:\My App" --skills ultimate-qa-client
```

For the external CLI, keep the complete collection in a durable folder and run from its root with Node.js 22.20+ and npm:

```powershell
npx skills@1.7.4 add ./packs/ultimate-qa --skill ultimate-qa-client --agent codex -g --copy
$env:ULTIMATE_QA_KIT = (Resolve-Path ./packs/ultimate-qa).Path
```

Start the agent from this terminal so it inherits the existing `ULTIMATE_QA_KIT` setting, or provide the absolute kit path when asked. The setting lasts for this terminal and child processes; repeat it in a new terminal. Keep this kit available and update its path if moved. For a project install, run from the application directory, use the absolute local pack path, and omit `-g`. For Claude Code use `--agent claude-code`. Review the destinations before proceeding. See the [npx guide](../../../../docs/NPX_INSTALLATION.md#ultimate-qa-support-files) for support-file setup and differences in installation records.

To install all nine skills or choose related specialists, follow the [Ultimate QA pack guide](../../README.md).

## Use

Refresh the agent session, open the target application repository, and invoke this in agent chat:

```text
$ultimate-qa-client prepare
```

In Claude Code use `/ultimate-qa-client`. These are agent chat instructions, not terminal commands. For the combined review plus client preparation, install the core skill too and invoke `$ultimate-qa run --client`.

## Prerequisites and limits

Requires the complete QA kit, a completed audit and improvement plan, Python 3.11+, and the optional `python-docx` package for Word output. Word deliverables also need a compatible renderer and visual inspection.

Use only when client-facing output is requested. Preparing an approval checklist does not approve fixes, start implementation or send documents.

Read the full [agent instructions](SKILL.md), [recorded installation guide](../../../../INSTALL.md), and [npx update/removal guide](../../../../docs/NPX_INSTALLATION.md#updates-and-removal). Use the installer that owns the copy for updates and removal. [Contribute](../../../../CONTRIBUTING.md).
