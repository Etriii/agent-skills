# Ultimate UX

Review navigation, content grouping, discoverability, forms, task flows, interaction states and recovery. This independent UX-only entrypoint preserves the current visual identity except where an interaction needs an accessible presentation change. It chooses patterns per journey rather than turning every long page into tabs.

Mobile is included by default. Inspect account-menu and store-context access, filter discoverability, dialog consequences and cancellation. Use `ultimate-mobile` when the selected task needs mobile UI and UX together.

## Install

PowerShell, starting in the downloaded collection root, with Python 3.11+:

```powershell
python tools/install_skills.py --pack developer-skills --agent codex --project "D:\My App" --skills ultimate-ux --dry-run
python tools/install_skills.py --pack developer-skills --agent codex --project "D:\My App" --skills ultimate-ux
```

Replace the application path; review the preview and confirm the second command. Use `--agent claude` or `--agent both` for other destinations. This skill includes all needed references and preview assets; installing the coordinator is optional. See the [pack guide](../../README.md) for whole-pack and scope options.

After publication, Node.js 22.20+ and npm can install a project copy from the application directory:

```powershell
npx skills@1.7.4 add https://github.com/Etriii/agent-skills --skill ultimate-ux --agent codex --copy
```

Use `--agent claude-code` for Claude Code. Remote installs use published files, not unpushed local work. Refresh the agent session after installation.

## Use

Enter these in agent chat with the target application open; they are not terminal commands. Claude Code uses `/ultimate-ux`.

```text
$ultimate-ux run
$ultimate-ux run --page /stores/:slug
$ultimate-ux run --page /checkout --auto
$ultimate-ux continue <run-folder> I approve the selected findings for sketches.
$ultimate-ux verify <run-folder>
```

Bare/run defaults to all discovered pages and approval checkpoints. Replace `<run-folder>` with the exact path supplied by the agent. The default workflow shows findings, waits for proposal approval, shows low-fidelity comparisons, waits for design approval, then implements and verifies. Generic continuation does not grant new approval. Relevant drift invalidates affected approvals.

`--auto`, or explicit task-specific no-approval authorization, completes those stages for UX-only scope without skill pauses. It retains decisions, previews and proof. Platform permissions and material unresolved policy choices still apply. It does not authorize rebranding, dependency installation, publication or Git operations.

## Outputs and prerequisites

Provide the application path/URL, relevant journeys/roles and authorized runtime access when available. Source-only inspection is supported and labeled; actual screenshots, keyboard journeys and observed behavior need suitable runtime evidence. No fixed UI framework, online design service, API key or sibling skill is needed. Outputs normally live under `.ui-ux/runs/` in the application, preserving earlier runs and preview revisions.

For combined work use [ultimate-ui-ux](../ultimate-ui-ux/README.md), or its `run --focus ux` mode as an alternative entrypoint. The [agent instructions](SKILL.md) and local references are self-contained after a one-skill install. Bundled sources retain [third-party notices and licenses](THIRD_PARTY.md); local material retains the collection's unresolved license status.

Read the [collection installation guide](../../../../INSTALL.md), [updates/removal](../../../../docs/NPX_INSTALLATION.md#updates-and-removal), and [contribution guide](../../../../CONTRIBUTING.md). Copy integrity does not establish native discovery or model adherence.
