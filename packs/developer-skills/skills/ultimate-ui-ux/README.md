# Ultimate UI and UX

Review existing application interfaces across all pages or selected routes. The suite finds visual and usability problems, decides whether sections, tabs, disclosure or routes fit the actual task, and produces reviewable before/after wireframes before application changes.

The main skill includes both specialists and mobile checks by default. Install it alone for combined or focused work, or install the independent `ultimate-ui`, `ultimate-ux` and `ultimate-mobile` shortcuts. Every entrypoint carries its own required resources; no sibling skill, private kit or online design service is required.

## Install

PowerShell, starting in the downloaded collection root, with Python 3.11+:

```powershell
python tools/install_skills.py --pack developer-skills --agent codex --project "D:\My App" --skills ultimate-ui-ux --dry-run
python tools/install_skills.py --pack developer-skills --agent codex --project "D:\My App" --skills ultimate-ui-ux
```

Replace the application path. The first command previews the installation; the second asks for confirmation and records the copy with payload checksums and Markdown history. Use `--agent claude` or `--agent both` for other supported destinations. To install all four commands, select `--skills ultimate-ui-ux ultimate-ui ultimate-ux ultimate-mobile`. See the [pack guide](../../README.md) for whole-pack and user-scope options.

After publication, from the application directory, Node.js 22.20+ and npm offer a project install:

```powershell
npx skills@1.7.4 add https://github.com/Etriii/agent-skills --skill ultimate-ui-ux --agent codex --copy
```

Use `--agent claude-code` for Claude Code. Remote commands install published files; they cannot install an unpushed local change. Refresh the agent session after installation.

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
