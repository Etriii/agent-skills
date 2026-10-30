# Ultimate UI

Review visual hierarchy, layout, spacing, typography, consistency, responsive composition and visual accessibility. This independent UI-only entrypoint preserves routes, information architecture and task order. Structural UX opportunities are reported separately.

Mobile is included by default. Inspect label/control alignment, crowded headers, touch presentation and primary/secondary/destructive button distinctions. Use `ultimate-mobile` when the selected task needs mobile UI and UX together.

## Install

### Direct install with npx (recommended)

No manual clone, ZIP download, or Python checkout is required to install this skill. The external CLI obtains the published source for you.

Prerequisites: [Node.js 22.20+](https://nodejs.org/en/download) with npm/npx, network access to npm/GitHub, and [Git](https://git-scm.com/downloads) for repository fallback. If a command is missing, install that prerequisite and reopen the terminal. These are installer prerequisites; the skill's runtime requirements are listed separately below.

PowerShell, from any folder, check tools first:

```powershell
node --version
npm --version
npx --version
git --version
```

PowerShell: replace `D:\My App` with your existing target application, then run each line separately:

```powershell
Set-Location 'D:\My App'
npx skills@1.7.4 add https://github.com/Etriii/agent-skills --skill ultimate-ui --agent codex claude-code --copy
```

This selects only `ultimate-ui` for Codex and Claude Code in the current project. Review the selected source, agents, scope and destinations in the CLI summary. npm may ask to download the pinned CLI; the skill installer may also prompt. These examples do not force noninteractive approval.

Still in the application folder, confirm the project copies:

```powershell
Test-Path '.agents/skills/ultimate-ui/SKILL.md'
Test-Path '.claude/skills/ultimate-ui/SKILL.md'
```

Both should return `True` for the two-agent project install. Refresh the coding-agent session, then use the chat requests in this README. Installation copies instructions; it does not run the skill.

For one agent, replace `--agent codex claude-code` with `--agent codex` or `--agent claude-code`. For an intended global installation across projects, choose this alternative command after the same prerequisites; do not run both scope examples unless you want both copies:

```powershell
npx skills@1.7.4 add https://github.com/Etriii/agent-skills --skill ultimate-ui --agent codex claude-code -g --copy
```

Global destinations are shown by the CLI; the project-relative `Test-Path` checks above do not verify global copies. Remote URLs install published files, so local unpushed changes are not included. PowerShell execution-policy errors can use `npx.cmd` instead of `npx`; see [troubleshooting](../../../../docs/NPX_INSTALLATION.md#troubleshooting) for missing tools, names, network access and refresh issues.

### Optional recorded or offline installation with Python

Keep this route when you want manifest verification, retained backups and Markdown operation history. It requires Python 3.11+ and a **complete local collection** first. Follow [download/extract or clone steps](../../../../INSTALL.md#optional-local-copy-for-python-and-offline-use), then identify the root containing `tools/`, `packs/`, and `README.md`. `tools/install_skills.py` is a file in that root, not a global command.

PowerShell: replace `D:\Tools\agent-skills` with that actual collection root and `D:\My App` with the existing destination application. For a ZIP, the extracted root may instead end in `agent-skills-main`.

```powershell
Set-Location 'D:\Tools\agent-skills'
python --version
python tools/install_skills.py --pack developer-skills --agent both --project "D:\My App" --skills ultimate-ui --dry-run
python tools/install_skills.py --pack developer-skills --agent both --project "D:\My App" --skills ultimate-ui
```

The first installer command previews and writes nothing. The second requests the existing confirmation and performs the copy with operation records. Run them separately. Python uses `--agent both`; npx uses `--agent codex claude-code`. For Python-only Codex or Claude choose `--agent codex` or `--agent claude`. User-scope options are in the [installation guide](../../../../INSTALL.md#choose-a-pack-agent-and-scope).

Use the installer that owns an existing copy for updates/removal; npx and Python maintain different records and protections. Preserve local edits before replacement. See the [pack guide](../../README.md), [npx lifecycle](../../../../docs/NPX_INSTALLATION.md#updates-and-removal), and [recorded removal guide](../../../../UNINSTALL.md).

## Use

Enter these in agent chat with the target application open; they are not terminal commands. Claude Code uses `/ultimate-ui`.

```text
$ultimate-ui run
$ultimate-ui run --page /stores/:slug
$ultimate-ui run --page /orders --page /settings --auto
$ultimate-ui continue <run-folder> I approve the selected findings for sketches.
$ultimate-ui verify <run-folder>
$ultimate-ui help
```

Bare/run defaults to all discovered pages and approval checkpoints. Replace `<run-folder>` with the exact path supplied by the agent. The default workflow shows findings, waits for proposal approval, shows low-fidelity comparisons, waits for design approval, then implements and verifies. Generic continuation does not grant new approval. Relevant drift invalidates affected approvals.

`--auto`, or explicit task-specific no-approval authorization, completes those stages for UI-only scope without skill pauses. It retains decisions, previews and proof. Platform permissions and material unresolved policy choices still apply. It does not authorize a broader UX redesign, dependency installation, publication or Git operations.

## Outputs and prerequisites

Provide the application path/URL, relevant pages, design constraints and authorized runtime access when available. Source-only inspection is supported and labeled; actual screenshots, contrast and keyboard claims need suitable rendered/browser evidence. No fixed UI framework, online design service, API key or sibling skill is needed. Outputs normally live under `.ui-ux/runs/` in the application, preserving earlier runs and preview revisions.

For combined work use [ultimate-ui-ux](../ultimate-ui-ux/README.md), or its `run --focus ui` mode as an alternative entrypoint. The [agent instructions](SKILL.md) and local references are self-contained after a one-skill install. Bundled sources retain [third-party notices and licenses](THIRD_PARTY.md); local material retains the collection's unresolved license status.

Read the [collection installation guide](../../../../INSTALL.md), [updates/removal](../../../../docs/NPX_INSTALLATION.md#updates-and-removal), and [contribution guide](../../../../CONTRIBUTING.md). Copy integrity does not establish native discovery or model adherence.
