# Ultimate Mobile

Review mobile web UI and UX across all pages or selected routes. Check crowded headers, account menus, filter alignment/reflow, dialogs, button hierarchy, touch access and state preservation. Keep a desktop baseline to detect regressions without redesigning desktop.

Mobile checks also run in the main `ultimate-ui-ux`, `ultimate-ui` and `ultimate-ux` reviews. This independent shortcut selects mobile web work directly; it does not enable an otherwise missing check.

## Install

PowerShell, starting in the downloaded collection root, with Python 3.11+:

```powershell
python tools/install_skills.py --pack developer-skills --agent codex --project "D:\My App" --skills ultimate-mobile --dry-run
python tools/install_skills.py --pack developer-skills --agent codex --project "D:\My App" --skills ultimate-mobile
```

Replace the application path, inspect the preview and confirm the second command. Use `--agent claude` or `--agent both` for other destinations. All runtime references, third-party notices/licenses and preview assets are included; a coordinator install is optional. The [pack guide](../../README.md) covers whole-pack and user scope.

After publication, Node.js 22.20+ and npm can install a project copy from the application directory:

```powershell
npx skills@1.7.4 add https://github.com/Etriii/agent-skills --skill ultimate-mobile --agent codex --copy
```

Use `--agent claude-code` for Claude Code. Remote installs use published files, not unpushed changes. Refresh the agent session after installation.

## Use in agent chat

These are chat requests with the target application open, not terminal commands. Claude Code uses `/ultimate-mobile`.

```text
$ultimate-mobile run
$ultimate-mobile run --page /orders
$ultimate-mobile run --page /orders --page /settings --auto
$ultimate-mobile continue <run-folder> I approve the selected findings for sketches.
$ultimate-mobile verify <run-folder>
$ultimate-mobile help
```

Bare/run reviews all discovered pages for mobile UI and UX, shows a saved proposal and stops. Approval authorizes low-fidelity comparisons; subsequent design approval authorizes application edits. Replace `<run-folder>` with the exact path provided by the agent. Generic continuation is not new approval.

`--auto`, or explicit task-specific no-approval authorization, completes review, previews, implementation and verification without skill approval pauses. It retains evidence and decisions. Platform permissions, selected page scope and unresolved material policy choices still apply. Default outputs live under the application's `.ui-ux/runs/`, preserving earlier runs and design revisions.

The skill chooses patterns based on actual tasks. A profile name may move into an accessible account dropdown, while current store/tenant context remains identifiable. Search/date controls align intentionally and wrap or stack on small screens. Dialog actions distinguish Cancel from the consequential action through labels, emphasis and semantic styling; Sign out is not automatically treated as deletion.

## Prerequisites and evidence limits

Provide the application path/URL, important workflows/roles and supported devices/viewports if known. Browser access and representative data are needed for rendered mobile claims. Without them, the skill labels source-only findings and reconstructed previews. Browser emulation does not establish real-device, virtual-keyboard or mobile screen-reader acceptance.

No native app project, fixed UI library, hosted design service, API key, additional package or sibling skill is required. For combined wide/mobile reviews use [ultimate-ui-ux](../ultimate-ui-ux/README.md); use its existing focused entrypoints for UI-only/UX-only work.

Read the [agent instructions](SKILL.md), [mobile playbook](references/mobile-review.md), [third-party notices](THIRD_PARTY.md), [collection installation guide](../../../../INSTALL.md), [updates/removal](../../../../docs/NPX_INSTALLATION.md#updates-and-removal), and [contribution guide](../../../../CONTRIBUTING.md). Copied material retains its original licenses; local/collection license status remains unresolved. Installation integrity does not prove native discovery or model adherence.
