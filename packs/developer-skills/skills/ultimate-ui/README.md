# Ultimate UI

Inspect and improve visual hierarchy, layout, spacing, typography, consistency, responsive composition and visual accessibility, then verify. Formal review and previews are optional. This independent UI-only entrypoint preserves routes, information architecture and task order. Structural UX opportunities are reported separately.

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

## Use in agent chat

Open the target application or name its source path. These are agent-chat requests, not terminal commands. Codex uses `$ultimate-ui`; Claude Code uses `/ultimate-ui`. Replace example paths, routes and URLs with actual inputs.

```text
$ultimate-ui Improve /orders and verify the changes.
$ultimate-ui Improve all in "D:\My App".
$ultimate-ui Improve "D:\My App\src\pages\Orders.vue".
$ultimate-ui Improve https://localhost:3000/orders using the source in "D:\My App".
```

The default inspects the established scope, chooses justified UI-only visual improvements, implements and verifies without routine skill approval pauses. No flag is required. Correct pages stay unchanged. Formal reviews and wireframes are optional. Bare invocation/`run` uses scope already established in context; unclear target/scope requires clarification, never an implicit all-pages redesign. **Improve all** explicitly covers every discovered page of the identified application within this entrypoint's discipline, with compact changed/kept/deferred coverage and gaps. It does not include sibling projects or external sites.

An absolute application directory identifies the project, not every page; name the feature or say improve all. An absolute page/component file selects affected pages. Relative paths resolve against the identified application. A URL identifies a runtime page and needs matching editable source for implementation; URL-only inspection cannot claim source changes. Invalid or unresolved targets never broaden scope. Quote paths containing spaces. Platform permissions and material unresolved policy choices still apply; publication, dependency installation, Git operations and unrelated features need separate authorization.

## Optional review and previews

Each agent-chat example is independent:

```text
$ultimate-ui Review /orders only. Do not edit.
$ultimate-ui Improve /orders. Include before/after previews.
$ultimate-ui Improve /orders. Show previews and wait for my approval before editing.
$ultimate-ui Create previews for /orders only. Do not edit application code.
```

Review-only stops at findings without edits or automatic previews. Requested previews precede implementation, with an approval pause only when requested; preview-only never authorizes edits. New previews share one run-local `previews/index.html`, linking feature indexes such as `previews/orders/index.html` and preserved comparison revisions/assets. Existing paths remain valid. See the installed [feature layout](references/preview-and-verify.md#feature-based-preview-folder).

## Existing commands and continuation

Natural-language requests above are recommended. Existing command combinations remain supported:

```text
$ultimate-ui run --page /orders --page /settings
$ultimate-ui run --page "D:\My App\src\pages\Orders.vue"
$ultimate-ui run --page /orders --auto
$ultimate-ui run --page /orders --skip-review Fix mobile filter wrapping.
$ultimate-ui continue <run-folder>
$ultimate-ui verify <run-folder>
$ultimate-ui help
```

Repeated `--page` accepts URLs, routes, absolute/relative files or page names. Focus stays fixed to this entrypoint; reject conflicts. Scoped `run` now improves and verifies without formal review/previews. For compatibility, `--auto` retains the full review/comparison/implementation workflow without skill approval pauses; it is not needed for the default. `--skip-review <task>` retains the concrete-fix shortcut; missing/vague tasks require clarification. Adding `--auto` to it is redundant. Reject `--skip-review` on `continue`, `verify` and `help`. Explicit review-only/preview-only instructions never authorize edits.

Default runs create no `.ui-ux/` or `.uiux/` files, logs, saved captures, status/verification records or related `.gitignore` changes. Inspect, improve, run necessary checks and report briefly in chat; keep improve-all coverage in context. Saving reports, logs, captures or a resumable run requires an explicit request. Requested file-based previews and compatibility/saved runs retain their artifact contracts; a no-files/chat-only constraint suppresses persistence. Review-only returns findings in chat unless saving is requested. Replace `<run-folder>` with the actual saved path. Continue checks drift and preserves recorded scope/authorization, including older proposal/design gates; the new default does not approve old designs. Verify checks recorded acceptance/design without fixes or missing-artifact demands. See the [workflow](references/workflow.md) for compatibility and resume details.

## Outputs and prerequisites

Provide the application path/URL, relevant pages, design constraints and authorized runtime access when available. Source-only inspection is supported and labeled; actual screenshots, contrast and keyboard claims need suitable rendered/browser evidence. No fixed UI framework, online design service, API key or sibling skill is needed. Opted-in outputs live under `.ui-ux/runs/` in the application, preserving earlier runs and preview revisions.

For combined work use [ultimate-ui-ux](../ultimate-ui-ux/README.md), or its `run --focus ui` mode as an alternative entrypoint. The [agent instructions](SKILL.md) and local references are self-contained after a one-skill install. Bundled sources retain [third-party notices and licenses](THIRD_PARTY.md); local material retains the collection's unresolved license status.

Read the [collection installation guide](../../../../INSTALL.md), [updates/removal](../../../../docs/NPX_INSTALLATION.md#updates-and-removal), and [contribution guide](../../../../CONTRIBUTING.md). Copy integrity does not establish native discovery or model adherence.

## Generated artifact storage

When this workflow saves reports or run evidence, use its target-workspace output owner and a new UTC `YYYYMMDDTHHMMSSZ-<unique-id>/` run directory; preserve earlier runs. Before saving in Git, the skill preserves or creates the root `.gitignore`, adds only the required scoped output rule, and verifies exclusion. Tracked output is refused without automatic untracking. Non-Git exclusion remains unverified, and workflows requiring Git retain that prerequisite. Unsafe storage or failed exclusion is reported before persistence. Existing state/resume paths and deliberately tracked project documents remain compatible. See the installed [artifact instructions](SKILL.md#generated-artifacts); chat-only requests create no extra output.
