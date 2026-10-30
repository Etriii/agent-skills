# Table UX Review

Audit application tables and data grids for detail navigation, crowded row actions, and accessible interactions. The review inventories every table in scope, traces shared owners and role restrictions, and recommends which interactions to keep, move, or leave unchanged.

Same-tab detail links are the default, with native options to open a new tab. Explicit new-tab requirements are supported. More than three visible row actions triggers a review rather than automatic removal. Selection, editing, bulk workflows, and authorized access must survive any cleanup.

## Install

PowerShell, starting in the downloaded collection root, with Python 3.11+:

```powershell
python tools/install_skills.py --pack developer-skills --agent codex --project "D:\My App" --skills table-ux-review --dry-run
python tools/install_skills.py --pack developer-skills --agent codex --project "D:\My App" --skills table-ux-review
```

Replace the project path with the target application. The first command previews the destination; the second requests confirmation and installs the skill with payload checksums and Markdown records. Use `--agent claude` or `--agent both` for the other supported installer destinations. Cancel the install if the preview identifies the wrong application.

After the skill is published to the remote repository, Node.js 22.20+ and npm offer another option. From the application directory, install a project copy for Codex:

```powershell
npx skills@1.7.4 add https://github.com/Etriii/agent-skills --skill table-ux-review --agent codex --copy
```

For Claude Code, use `--agent claude-code`. Remote commands use the published version and cannot install an unpushed local change. See the [Developer Skills pack guide](../../README.md) for whole-pack installation.

## Use

Refresh the agent session, open the target application, and enter this in agent chat:

```text
$table-ux-review Audit all tables in this application. Inventory detail navigation and row actions by role, recommend action placement, and identify unverified coverage. Report before editing.
```

For implementation, authorize the desired scope in the same request:

```text
$table-ux-review Audit and fix the orders tables. Reuse existing detail routes and menus, preserve selection and bulk approval, and verify keyboard navigation and relocated actions.
```

Claude Code uses `/table-ux-review`. These are agent chat instructions, not terminal commands. Expected output is an inventory with decisions and evidence, plus prioritized findings or authorized changes and their verification. A missing detail route is reported as a gap rather than created automatically.

## Prerequisites and limits

Provide the target application source, scope, and relevant workflows. Authorized local or staging browser access and suitable test roles/data are needed for runtime claims. If those are unavailable, the skill reports source findings and coverage gaps; browser or screen-reader acceptance remains unverified.

No private runner, API key, additional skill, or third-party runtime package is required by the skill itself. It uses the application's existing tools. Compatibility metadata remains unverified until native agent discovery is observed; installing files alone does not prove model adherence.

Read the [agent instructions](SKILL.md), [collection installation guide](../../../../INSTALL.md), and [update/removal options](../../../../docs/NPX_INSTALLATION.md#updates-and-removal). Use the installer that owns the copy for updates and removal. [Contribute](../../../../CONTRIBUTING.md).
