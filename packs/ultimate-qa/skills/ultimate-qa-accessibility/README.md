# Ultimate QA Accessibility

Audit critical pages with automated accessibility checks, keyboard journeys and assistive-technology evidence.

## Install

For automatic kit pointers, checksums, retained backups and Markdown records, use Python 3.11+ from the downloaded collection root:

```powershell
python tools/install_skills.py --pack ultimate-qa --agent codex --project "D:\My App" --skills ultimate-qa-accessibility --dry-run
python tools/install_skills.py --pack ultimate-qa --agent codex --project "D:\My App" --skills ultimate-qa-accessibility
```

For the external CLI, keep the complete collection in a durable folder and run from its root with Node.js 22.20+ and npm:

```powershell
npx skills@1.7.4 add ./packs/ultimate-qa --skill ultimate-qa-accessibility --agent codex -g --copy
```

For a project install, run from the application directory, use the absolute local pack path, and omit `-g`. For Claude Code use `--agent claude-code`. Review the destinations before proceeding. See the [npx guide](../../../../docs/NPX_INSTALLATION.md#ultimate-qa-support-files) for support-file setup and differences in installation records.

To install all nine skills or choose related specialists, follow the [Ultimate QA pack guide](../../README.md).

## Use

Refresh the agent session, open the target application repository, and invoke this in agent chat:

```text
$ultimate-qa-accessibility Audit the request form and approval dialog for keyboard access, focus recovery and announced errors.
```

In Claude Code use `/ultimate-qa-accessibility`. These are agent chat instructions, not terminal commands. For versioned reports integrated with the core workflow, also install `ultimate-qa` and invoke `$ultimate-qa run`.

## Prerequisites and limits

Needs an authorized running application, role-specific test accounts and an available browser. Use the project's installed accessibility tools; screen-reader acceptance requires actual assistive-technology evidence.

Report automated, keyboard and screen-reader coverage separately. A clean scanner result does not certify accessibility.

Read the full [agent instructions](SKILL.md), [recorded installation guide](../../../../INSTALL.md), and [npx update/removal guide](../../../../docs/NPX_INSTALLATION.md#updates-and-removal). Use the installer that owns the copy for updates and removal. [Contribute](../../../../CONTRIBUTING.md).
