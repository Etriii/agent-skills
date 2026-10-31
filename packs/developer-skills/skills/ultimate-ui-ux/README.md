# Ultimate UI and UX

Inspect and improve selected application pages, or explicitly all pages, with implementation and verification by default. Formal review reports and feature-based before/after previews are optional.

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

Open the target application or name its source path. These are agent-chat requests, not terminal commands. Codex uses `$ultimate-ui-ux`; Claude Code uses `/ultimate-ui-ux`. Replace all example paths, routes and URLs with your actual inputs. No implementation flag is needed.

```text
$ultimate-ui-ux Improve /orders and verify the changes.
$ultimate-ui-ux Improve all UI and UX in this application.
$ultimate-ui-ux Improve all UI and UX in "D:\My App".
```

The default inspects the selected scope, chooses justified improvements, implements and verifies without routine skill approval pauses. It preserves working behavior, accessibility, roles and data boundaries. Correct pages stay unchanged. Formal review reports and wireframes are optional; they are not generated by default. Material unresolved choices and platform permissions still apply. Publication, dependency installation, Git operations and unrelated features need separate authorization.

Bare invocation or `run` uses the target and page scope already established in context. If either is unclear, the agent asks only for missing input. A project folder alone does not silently select every page. Say **Improve all** to authorize assessment and justified fixes across every discovered page of that application, within the chosen discipline. Large requests are grouped by feature with changed/kept/deferred coverage and explicit gaps; they do not become a few showcase screens or include sibling projects/external sites. No extra command is required between discovery and in-scope implementation.

Mobile checks are included by default. The independently installable `ultimate-ui`, `ultimate-ux` and `ultimate-mobile` shortcuts use the same default with their fixed visual, usability or mobile-web focus. Mobile-only changes include desktop regression checks.

## Supply an absolute path, relative path or URL

You do not need to use a relative route. An absolute application directory identifies the project, while the request identifies selected pages or explicitly all pages. An absolute page/component path selects its affected pages. Relative filesystem paths resolve against the identified application; `/orders` is an application route. Quote paths containing spaces.

```text
$ultimate-ui-ux Improve the orders feature in "D:\My App".
$ultimate-ui-ux Improve "D:\My App\src\pages\Orders.vue".
$ultimate-ui-ux Improve src/pages/Orders.vue in "D:\My App".
$ultimate-ui-ux Improve https://localhost:3000/orders using the source in "D:\My App".
$ultimate-ui-ux Improve all at https://localhost:3000 using the source in "D:\My App".
```

Replace the example application/page paths and URL with actual inputs. The agent maps files and URLs to concrete owners before editing. Invalid or unresolved targets never fall back to all pages. A URL identifies runtime pages; it does not supply editable source or authorize deployment/production writes. With URL-only access the agent can inspect available pages, but must report implementation blocked until matching editable source is available. Missing browser/data access limits rendered coverage; a source inventory or passing build does not prove runtime, accessibility or user acceptance.

## Optional review or previews

Use ordinary language to select the result you need. Each line is independent:

```text
$ultimate-ui-ux Review /orders only. Do not edit.
$ultimate-ui-ux Improve /orders. Include before/after previews.
$ultimate-ui-ux Improve /orders. Show previews and wait for my approval before editing.
$ultimate-ui-ux Create previews for /orders only. Do not edit application code.
```

Review-only produces findings/recommendations and stops without edits or automatic wireframes. An improvement request with previews creates comparisons before edits and continues unless you explicitly request approval. A preview-only request never authorizes implementation. Asking to wait for design approval adds that checkpoint without an extra proposal-approval stage. The full proposal-then-design approval workflow remains available when explicitly requested.

New previews have one entry page grouped by the application's actual features:

```text
.ui-ux/runs/<run-id>/previews/
  index.html
  orders/
    index.html
    revisions/v001/index.html
    revisions/v001/assets/
  checkout/
    index.html
    revisions/v001/index.html
```

`<run-id>` is the generated UTC timestamp plus unique suffix. Open `previews/index.html` to select a feature; each feature index links current before/after comparisons and preserved revisions. Comparisons identify routes, roles, states and viewports. Assets exist only when needed. Existing preview paths and approvals remain valid; see [layout and revision rules](references/preview-and-verify.md#feature-based-preview-folder).

## Existing commands and combinations

Natural-language requests above are the recommended entry point. Existing options remain supported; these are independent agent-chat alternatives:

```text
$ultimate-ui-ux run --focus ux --page /orders --page /checkout
$ultimate-ui-ux run --page "D:\My App\src\pages\Orders.vue"
$ultimate-ui-ux run --page /orders --auto
$ultimate-ui-ux run --focus ui --page /orders --skip-review Fix mobile filter wrapping.
$ultimate-ui-ux continue <run-folder>
$ultimate-ui-ux verify <run-folder>
$ultimate-ui-ux help
```

`--page` accepts a URL, route pattern, absolute/relative page file or unambiguous name; repeat it for several pages. The main entrypoint supports `--focus ui` or `--focus ux`, default both. Without `--auto`, a scoped `run` now improves and verifies without a formal review/previews. This replaces the previous new-run gated default.

For compatibility, `run --auto` still performs the full review, comparisons, implementation and verification without skill approval pauses; it is optional and costs more work than the lean default. `run --skip-review <task>` retains the concrete-fix shortcut: the task comes from text or established context, and missing/vague tasks require clarification. It combines with repeated `--page` and `--focus`; adding `--auto` is accepted but redundant. Reject `--skip-review` on `continue`, `verify` and `help`. Explicit review-only/preview-only constraints never authorize edits, even with implementation options.

## Outputs, continuation and prerequisites

Runs normally live in `.ui-ux/runs/YYYYMMDDTHHMMSSZ-<unique-id>/` inside the target application. Default improvements save concise `status.md` and `verification.md`; improve-all includes compact feature/page coverage. Formal reviews add `review.md` only when requested or using compatibility `--auto`. `previews/` exists only when requested or required by a compatibility/saved run. No empty later-stage placeholders are created. An explicit chat-only request creates no run artifacts.

Replace `<run-folder>` with the actual path supplied by the agent. Continue uses that recorded scope/authorization and checks relevant source/design drift. Existing gated runs retain their proposal/design checkpoints; the new default does not approve them. Generic continuation grants no new approval. `verify` checks recorded acceptance/design without adding fixes or demanding intentionally omitted review/previews. `continue <run-folder> --auto` explicitly authorizes remaining work within the recorded scope when implementation is permitted; it never expands pages or overrides explicit review-only/preview-only limits.

Prior runs and design revisions are preserved. The skill does not automatically change `.gitignore` or commit generated files. URL-only reviews record a suitable writable output root.

Provide source or an authorized runtime, relevant workflows/roles and real design constraints. Browser access and suitable data are needed for actual screenshots and keyboard/rendered claims. Without them, results identify source-only findings and reconstructed previews. No fixed framework, API key, hosted service or sibling skill is required. The [comparison starter](assets/comparison.html) is illustrative content, not an application capture; use it only for requested/compatibility previews and adapt it to the selected pages.

## Sources and maintenance

Selected Taste-Skill, UI UX Pro Max and Anthropic frontend-design excerpts, plus Pro Max UX data, are bundled offline with pinned revisions, hashes and complete licenses in [THIRD_PARTY.md](THIRD_PARTY.md). These references inform decisions; they do not impose a framework, override approvals, or require upstream scripts. Local authored material retains the collection's unresolved license status.

Maintainers edit shared resources here, then run `python -B tools/sync_ui_ux.py` from the collection root and refresh the pack manifest. `python -B tools/sync_ui_ux.py --check` detects distribution drift without writes. Copies exist so each separately installed skill works offline; runtime has no dependency on this maintenance tool.

Read the [agent instructions](SKILL.md), [installation guide](../../../../INSTALL.md), [updates and removal](../../../../docs/NPX_INSTALLATION.md#updates-and-removal), and [contribution guide](../../../../CONTRIBUTING.md). Native discovery and model adherence are separate from file-copy verification; see [test evidence](../../../../docs/TEST_EVIDENCE.md).
