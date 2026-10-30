# Ultimate UI and UX

Review existing application interfaces across all pages or selected routes. The suite finds visual and usability problems, decides whether sections, tabs, disclosure or routes fit the actual task, and produces reviewable before/after wireframes before application changes.

The main skill includes both specialists and mobile checks by default. Install it alone for combined or focused work, or install the independent `ultimate-ui`, `ultimate-ux` and `ultimate-mobile` shortcuts. Every entrypoint carries its own required resources; no sibling skill, private kit or online design service is required.

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
npx skills@1.7.4 add https://github.com/Etriii/agent-skills --skill ultimate-ui-ux --agent codex claude-code --copy
```

This selects only `ultimate-ui-ux` for Codex and Claude Code in the current project. Review the selected source, agents, scope and destinations in the CLI summary. npm may ask to download the pinned CLI; the skill installer may also prompt. These examples do not force noninteractive approval.

Still in the application folder, confirm the project copies:

```powershell
Test-Path '.agents/skills/ultimate-ui-ux/SKILL.md'
Test-Path '.claude/skills/ultimate-ui-ux/SKILL.md'
```

Both should return `True` for the two-agent project install. Refresh the coding-agent session, then use the chat requests in this README. Installation copies instructions; it does not run the skill.

For one agent, replace `--agent codex claude-code` with `--agent codex` or `--agent claude-code`. For an intended global installation across projects, choose this alternative command after the same prerequisites; do not run both scope examples unless you want both copies:

```powershell
npx skills@1.7.4 add https://github.com/Etriii/agent-skills --skill ultimate-ui-ux --agent codex claude-code -g --copy
```

Global destinations are shown by the CLI; the project-relative `Test-Path` checks above do not verify global copies. Remote URLs install published files, so local unpushed changes are not included. PowerShell execution-policy errors can use `npx.cmd` instead of `npx`; see [troubleshooting](../../../../docs/NPX_INSTALLATION.md#troubleshooting) for missing tools, names, network access and refresh issues.

### Optional recorded or offline installation with Python

Keep this route when you want manifest verification, retained backups and Markdown operation history. It requires Python 3.11+ and a **complete local collection** first. Follow [download/extract or clone steps](../../../../INSTALL.md#optional-local-copy-for-python-and-offline-use), then identify the root containing `tools/`, `packs/`, and `README.md`. `tools/install_skills.py` is a file in that root, not a global command.

PowerShell: replace `D:\Tools\agent-skills` with that actual collection root and `D:\My App` with the existing destination application. For a ZIP, the extracted root may instead end in `agent-skills-main`.

```powershell
Set-Location 'D:\Tools\agent-skills'
python --version
python tools/install_skills.py --pack developer-skills --agent both --project "D:\My App" --skills ultimate-ui-ux --dry-run
python tools/install_skills.py --pack developer-skills --agent both --project "D:\My App" --skills ultimate-ui-ux
```

The first installer command previews and writes nothing. The second requests the existing confirmation and performs the copy with operation records. Run them separately. Python uses `--agent both`; npx uses `--agent codex claude-code`. For Python-only Codex or Claude choose `--agent codex` or `--agent claude`. User-scope options are in the [installation guide](../../../../INSTALL.md#choose-a-pack-agent-and-scope).

Use the installer that owns an existing copy for updates/removal; npx and Python maintain different records and protections. Preserve local edits before replacement. See the [pack guide](../../README.md), [npx lifecycle](../../../../docs/NPX_INSTALLATION.md#updates-and-removal), and [recorded removal guide](../../../../UNINSTALL.md).

## Use in agent chat

These are chat requests, not executable shell commands. Open the target application in the agent first. Claude Code uses `/ultimate-ui-ux` instead of `$ultimate-ui-ux`.

```text
$ultimate-ui-ux run
$ultimate-ui-ux run --page /stores/:slug
$ultimate-ui-ux run --page /orders --page /orders/:id
$ultimate-ui-ux run --focus ui --page src/pages/StorePage.vue
$ultimate-ui-ux run --focus ux
```

Bare invocation defaults to all discovered pages, both disciplines, and approval checkpoints. A page selector accepts a URL, route, page file or unambiguous page name. Invalid or unresolved selectors do not fall back to a full audit. Shared callers are inspected for impact without redesigning unselected pages.

Mobile is included in normal responsive web reviews. Checks cover misaligned controls, crowded headers, readable store/account context, filter reflow, dialog sizing and distinct primary/cancel/destructive actions. For mobile-only work install [ultimate-mobile](../ultimate-mobile/README.md) and use `$ultimate-mobile run --page /orders`, optionally with `--auto`. It uses the same approval/artifact workflow and checks desktop for regressions.

Default workflow:

1. Inspect source/runtime, capture available baseline evidence, save the page inventory and proposal, and show it. No proposed layout or application edit yet.
2. After proposal approval, generate and show low-fidelity before/after comparisons for the selected findings. No application edit yet.
3. After design approval, implement that selection and verify it. Leave good pages unchanged.

The agent supplies exact run-folder and artifact links at each checkpoint. To resume, give the actual path shown by the agent and your decision:

```text
$ultimate-ui-ux continue <run-folder> I approve findings UX-001 and UI-003 for sketches.
$ultimate-ui-ux continue <run-folder> I approve the current design for implementation.
$ultimate-ui-ux verify <run-folder>
$ultimate-ui-ux help
```

Replace `<run-folder>` with the generated path. A generic `continue` resumes authorized work; it does not silently approve the next stage. Proposal approval authorizes sketches; design approval authorizes application changes. Relevant source/design drift is rechecked before using an approval.

## Automatic mode

```text
$ultimate-ui-ux run --auto
$ultimate-ui-ux run --page /stores/:slug --auto
$ultimate-ui-ux run --focus ux --page /checkout --auto
$ultimate-ui-ux continue <run-folder> --auto
```

`--auto`, or an explicit task-specific instruction to proceed without approvals, authorizes review, design decisions, previews, implementation and verification for the selected scope. The agent creates previews before edits and retains rationale/evidence without waiting for skill approvals. Required platform permissions still apply. Unresolved material business/data/billing decisions are deferred rather than invented; independent work continues. Publication, dependency installation, Git operations and unrelated features need their own authorization.

On `continue`, `--auto` authorizes only remaining work within that saved run's recorded scope. Replace `<run-folder>` with its actual path; it does not select another run or broaden the approved pages.

## Outputs and prerequisites

Runs normally live in the application's `.ui-ux/runs/<UTC-time>-<unique-suffix>/` directory with `review.md`, `status.md`, authorized `previews/`, and later `verification.md`. Prior runs and design revisions are preserved. The skill does not automatically change `.gitignore` or commit generated files. URL-only reviews record a suitable writable output root.

Provide source or an authorized runtime, relevant workflows/roles, and any real design constraints. Browser access and suitable data are required for runtime/screenshots and keyboard claims. Without them, output identifies source-only findings and reconstructed wireframes. A prototype or passing build does not prove application accessibility or user acceptance. No application screenshot is fabricated from source.

The [interactive comparison starter](assets/comparison.html) illustrates Products/Channel/Reviews panel switching. It is explicitly sample content, not an application capture or a universal layout. The agent adapts previews to the selected pages and compares actual before/after captures when possible.

## Sources and maintenance

Selected Taste-Skill, UI UX Pro Max and Anthropic frontend-design excerpts, plus Pro Max UX data, are bundled offline with pinned revisions, hashes and complete licenses in [THIRD_PARTY.md](THIRD_PARTY.md). These references inform decisions; they do not impose a framework, override approvals, or require upstream scripts. Local authored material retains the collection's unresolved license status.

Maintainers edit shared resources here, then run `python -B tools/sync_ui_ux.py` from the collection root and refresh the pack manifest. `python -B tools/sync_ui_ux.py --check` detects distribution drift without writes. Copies exist so each separately installed skill works offline; runtime has no dependency on this maintenance tool.

Read the [agent instructions](SKILL.md), [installation guide](../../../../INSTALL.md), [updates and removal](../../../../docs/NPX_INSTALLATION.md#updates-and-removal), and [contribution guide](../../../../CONTRIBUTING.md). Native discovery and model adherence are separate from file-copy verification; see [test evidence](../../../../docs/TEST_EVIDENCE.md).
