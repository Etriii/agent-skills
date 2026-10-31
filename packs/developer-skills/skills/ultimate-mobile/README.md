# Ultimate Mobile

Inspect and improve mobile web UI and UX across selected routes or explicitly all pages, then verify. Formal review and previews are optional. Check crowded headers, account menus, filter alignment/reflow, dialogs, button hierarchy, touch access and state preservation. Keep a desktop baseline to detect regressions without redesigning desktop.

Mobile checks also run in the main `ultimate-ui-ux`, `ultimate-ui` and `ultimate-ux` reviews. This independent shortcut selects mobile web work directly; it does not enable an otherwise missing check.

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
npx skills@1.7.4 add https://github.com/Etriii/agent-skills --skill ultimate-mobile --agent codex claude-code --copy
```

This selects only `ultimate-mobile` for Codex and Claude Code in the current project. Review the selected source, agents, scope and destinations in the CLI summary. npm may ask to download the pinned CLI; the skill installer may also prompt. These examples do not force noninteractive approval.

Still in the application folder, confirm the project copies:

```powershell
Test-Path '.agents/skills/ultimate-mobile/SKILL.md'
Test-Path '.claude/skills/ultimate-mobile/SKILL.md'
```

Both should return `True` for the two-agent project install. Refresh the coding-agent session, then use the chat requests in this README. Installation copies instructions; it does not run the skill.

For one agent, replace `--agent codex claude-code` with `--agent codex` or `--agent claude-code`. For an intended global installation across projects, choose this alternative command after the same prerequisites; do not run both scope examples unless you want both copies:

```powershell
npx skills@1.7.4 add https://github.com/Etriii/agent-skills --skill ultimate-mobile --agent codex claude-code -g --copy
```

Global destinations are shown by the CLI; the project-relative `Test-Path` checks above do not verify global copies. Remote URLs install published files, so local unpushed changes are not included. PowerShell execution-policy errors can use `npx.cmd` instead of `npx`; see [troubleshooting](../../../../docs/NPX_INSTALLATION.md#troubleshooting) for missing tools, names, network access and refresh issues.

### Optional recorded or offline installation with Python

Keep this route when you want manifest verification, retained backups and Markdown operation history. It requires Python 3.11+ and a **complete local collection** first. Follow [download/extract or clone steps](../../../../INSTALL.md#optional-local-copy-for-python-and-offline-use), then identify the root containing `tools/`, `packs/`, and `README.md`. `tools/install_skills.py` is a file in that root, not a global command.

PowerShell: replace `D:\Tools\agent-skills` with that actual collection root and `D:\My App` with the existing destination application. For a ZIP, the extracted root may instead end in `agent-skills-main`.

```powershell
Set-Location 'D:\Tools\agent-skills'
python --version
python tools/install_skills.py --pack developer-skills --agent both --project "D:\My App" --skills ultimate-mobile --dry-run
python tools/install_skills.py --pack developer-skills --agent both --project "D:\My App" --skills ultimate-mobile
```

The first installer command previews and writes nothing. The second requests the existing confirmation and performs the copy with operation records. Run them separately. Python uses `--agent both`; npx uses `--agent codex claude-code`. For Python-only Codex or Claude choose `--agent codex` or `--agent claude`. User-scope options are in the [installation guide](../../../../INSTALL.md#choose-a-pack-agent-and-scope).

Use the installer that owns an existing copy for updates/removal; npx and Python maintain different records and protections. Preserve local edits before replacement. See the [pack guide](../../README.md), [npx lifecycle](../../../../docs/NPX_INSTALLATION.md#updates-and-removal), and [recorded removal guide](../../../../UNINSTALL.md).

## Use in agent chat

Open the target application or name its source path. These are agent-chat requests, not terminal commands. Codex uses `$ultimate-mobile`; Claude Code uses `/ultimate-mobile`. Replace example paths, routes and URLs with actual inputs.

```text
$ultimate-mobile Improve /orders and verify the changes.
$ultimate-mobile Improve all in "D:\My App".
$ultimate-mobile Improve "D:\My App\src\pages\Orders.vue".
$ultimate-mobile Improve https://localhost:3000/orders using the source in "D:\My App".
```

The default inspects the established scope, chooses justified mobile web UI/UX improvements, implements and verifies without routine skill approval pauses. No flag is required. Correct pages stay unchanged. Formal reviews and wireframes are optional. Bare invocation/`run` uses scope already established in context; unclear target/scope requires clarification, never an implicit all-pages redesign. **Improve all** explicitly covers every discovered page of the identified application within this entrypoint's discipline, with compact changed/kept/deferred coverage and gaps. It does not include sibling projects or external sites.

An absolute application directory identifies the project, not every page; name the feature or say improve all. An absolute page/component file selects affected pages. Relative paths resolve against the identified application. A URL identifies a runtime page and needs matching editable source for implementation; URL-only inspection cannot claim source changes. Invalid or unresolved targets never broaden scope. Quote paths containing spaces. Platform permissions and material unresolved policy choices still apply; publication, dependency installation, Git operations and unrelated features need separate authorization.

## Optional review and previews

Each agent-chat example is independent:

```text
$ultimate-mobile Review /orders only. Do not edit.
$ultimate-mobile Improve /orders. Include before/after previews.
$ultimate-mobile Improve /orders. Show previews and wait for my approval before editing.
$ultimate-mobile Create previews for /orders only. Do not edit application code.
```

Review-only stops at findings without edits or automatic previews. Requested previews precede implementation, with an approval pause only when requested; preview-only never authorizes edits. New previews share one run-local `previews/index.html`, linking feature indexes such as `previews/orders/index.html` and preserved comparison revisions/assets. Existing paths remain valid. See the installed [feature layout](references/preview-and-verify.md#feature-based-preview-folder).

## Existing commands and continuation

Natural-language requests above are recommended. Existing command combinations remain supported:

```text
$ultimate-mobile run --page /orders --page /settings
$ultimate-mobile run --page "D:\My App\src\pages\Orders.vue"
$ultimate-mobile run --page /orders --auto
$ultimate-mobile run --page /orders --skip-review Keep filter controls within the phone viewport.
$ultimate-mobile continue <run-folder>
$ultimate-mobile verify <run-folder>
$ultimate-mobile help
```

Repeated `--page` accepts URLs, routes, absolute/relative files or page names. Focus stays fixed to this entrypoint; reject conflicts. Scoped `run` now improves and verifies without formal review/previews. For compatibility, `--auto` retains the full review/comparison/implementation workflow without skill approval pauses; it is not needed for the default. `--skip-review <task>` retains the concrete-fix shortcut; missing/vague tasks require clarification. Adding `--auto` to it is redundant. Reject `--skip-review` on `continue`, `verify` and `help`. Explicit review-only/preview-only instructions never authorize edits.

Default runs save concise status/proof under the application's `.ui-ux/runs/`, with compact coverage for improve-all. Formal review/previews are added only when requested or required by a compatibility/saved run; no empty placeholders. Chat-only creates no run artifacts. Replace `<run-folder>` with the actual saved path. Continue checks drift and preserves recorded scope/authorization, including older proposal/design gates; the new default does not approve old designs. Verify checks recorded acceptance/design without fixes or missing-artifact demands. See the [workflow](references/workflow.md) for compatibility and resume details.

## Prerequisites and evidence limits

Provide the application path/URL, important workflows/roles and supported devices/viewports if known. Browser access and representative data are needed for rendered mobile claims. Without them, the skill labels source-only findings and reconstructed previews. Browser emulation does not establish real-device, virtual-keyboard or mobile screen-reader acceptance.

No native app project, fixed UI library, hosted design service, API key, additional package or sibling skill is required. For combined wide/mobile reviews use [ultimate-ui-ux](../ultimate-ui-ux/README.md); use its existing focused entrypoints for UI-only/UX-only work.

Read the [agent instructions](SKILL.md), [mobile playbook](references/mobile-review.md), [third-party notices](THIRD_PARTY.md), [collection installation guide](../../../../INSTALL.md), [updates/removal](../../../../docs/NPX_INSTALLATION.md#updates-and-removal), and [contribution guide](../../../../CONTRIBUTING.md). Copied material retains its original licenses; local/collection license status remains unresolved. Installation integrity does not prove native discovery or model adherence.

## Generated artifact storage

When this workflow saves reports or run evidence, use its target-workspace output owner and a new UTC `YYYYMMDDTHHMMSSZ-<unique-id>/` run directory; preserve earlier runs. Before saving in Git, the skill preserves or creates the root `.gitignore`, adds only the required scoped output rule, and verifies exclusion. Tracked output is refused without automatic untracking. Non-Git exclusion remains unverified, and workflows requiring Git retain that prerequisite. Unsafe storage or failed exclusion is reported before persistence. Existing state/resume paths and deliberately tracked project documents remain compatible. See the installed [artifact instructions](SKILL.md#generated-artifacts); chat-only requests create no extra output.
