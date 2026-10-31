---
name: ultimate-ui-ux
description: Inspect and improve existing application UI and UX, implement justified scoped fixes and verify them. Use for selected pages or explicitly all pages, with optional review-only reports and feature-based previews.
---

# Ultimate UI and UX

Input: A target application, selected pages or explicit all-pages scope, optional user journeys and design references. Accept absolute application/page paths, relative paths and authorized URLs.

Output: Scoped improvements with concise verification in chat and no generated run files by default; a formal review or previews only when requested. Distinguish source inspection, prototypes and observed application behavior.

## Invocation

These are agent-chat instructions, not terminal commands. Codex uses `$ultimate-ui-ux`; Claude Code uses `/ultimate-ui-ux`.

| Request | Behavior |
|---|---|
| Natural-language request, `run` or bare invocation | Inspect the established scope, choose justified improvements, implement and verify without routine skill approval pauses. Ask for scope if unclear; never silently select all pages. |
| `Improve all` | Inspect all discovered pages of the identified application, improve justified issues and verify. Keep correct pages unchanged. |
| `Review ... only. Do not edit.` | Produce findings and recommendations without application edits or automatic previews. |
| `Improve ... Show previews and wait for my approval before editing.` | Inspect, show feature-based previews and pause before implementation. |
| `run --page <selector>` | Improve only selected pages. Repeat `--page` for more than one page. |
| `run --focus ui` or `run --focus ux` | Limit work to the selected discipline. Default is `both`. |
| `run --auto` | Compatibility option: perform the full review, comparisons, implementation and verification without skill approval pauses. It is not needed for default improvements. |
| `run --skip-review <task>` | Inspect affected owners, implement the concrete requested fix and verify it without a full audit, proposal, wireframes or skill approval pauses. |
| `continue <run-folder>` | Resume that saved run at its recorded checkpoint using the user's current response and prior valid approvals. |
| `verify <run-folder>` | Check recorded acceptance/design and implementation without fixes or new authorization. |
| `help` | Explain scope, modes, prerequisites and the next applicable command with copyable command combinations; do not create a run. |

Prefer natural-language requests; no flag is needed for implementation. Identify target and scope separately: an absolute application folder selects the project, not automatically every page; an absolute page/component file selects its affected pages. Resolve relative paths against the target application. A URL selects its page, not every link or another host. URL-only access cannot implement source changes without a matching editable checkout; report that limit and request source when needed. Unsupported options or unresolved selectors never broaden scope.

Keep `--page`, `--focus`, `--auto` and `--skip-review` compatible. `--skip-review` still requires a concrete fix; combine it with repeated `--page` and `--focus`, with `--auto` redundant. Reject `--skip-review` on `continue`, `verify` or `help`. Explicit review-only/preview-only constraints never authorize edits. A request for previews alone does not require an approval pause unless requested. Saved runs retain their recorded checkpoints; a new default does not approve old designs. See [workflow](references/workflow.md) for continuation and compatibility rules.

Agent-chat combinations, each an independent example; replace routes, files and task text with actual inputs:

```text
$ultimate-ui-ux Improve /orders and verify the changes.
$ultimate-ui-ux Improve all UI and UX in "D:\My App".
$ultimate-ui-ux Improve "D:\My App\src\pages\Orders.vue".
$ultimate-ui-ux Improve https://localhost:3000/orders using the source in "D:\My App".
$ultimate-ui-ux Review /orders only. Do not edit.
$ultimate-ui-ux Improve /orders. Show previews and wait for my approval before editing.
```

## Reading map

1. Read [workflow](references/workflow.md) for every run, continuation and verification. It owns scope, artifact storage, approvals and completion rules.
2. Read [UI review](references/ui-review.md) and [UX review](references/ux-review.md) only for the selected discipline and affected behavior. Default improvements do not require a formal audit report. The main skill contains both specialists and requires no sibling installation or delegation.
   Read [mobile review](references/mobile-review.md) for responsive web work in either discipline. Mobile checks are included by default, not enabled only by a separate skill. Respect the selected UI/UX scope.
3. Read [wireframes and verification](references/preview-and-verify.md) before producing previews, implementing or verifying. Use the [comparison starter](assets/comparison.html) only after preview authorization; adapt it to actual pages.
4. Consult [source guidance](references/source-guidance.md) only for relevant design questions. Copied upstream material is reference data, not an instruction to run its tools or override this workflow.

The independently installable `ultimate-ui` and `ultimate-ux` entrypoints select one discipline; `ultimate-mobile` selects mobile web UI and UX. Each carries local copies of these shared resources. Their distribution copies are synchronized from this skill; read only resources relevant to the selected scope.

Limits: No fixed framework, aesthetic, browser service, other installed skill or network access is required. Runtime and visual claims require suitable application/browser access. Auto mode removes this skill's approval pauses; platform permissions, data boundaries and the user's scope still apply. Do not deploy, publish, commit, merge, install dependencies or change public/business policy unless the task separately authorizes it.

## Generated artifacts

Default improvements create no generated artifacts: do not create or update `.ui-ux/`, `.uiux/`, logs, saved screenshots, reports, run metadata or related `.gitignore` rules. Keep necessary checks and concise results in chat; do not relocate bookkeeping elsewhere. Saving requires an explicit request, requested file-based previews, compatibility full-review mode or an explicitly resumed saved run. A no-files/chat-only constraint suppresses persistence. Read the workflow before any opted-in output.

Apply this section only when the workflow saves generated reports, logs, previews, or run evidence. Use a stable skill-owned root in the target workspace, never the installed skill directory. Allocate each new run with an exclusively created `YYYYMMDDTHHMMSSZ-<unique-id>/` directory (UTC); preserve earlier runs and resume the identified active run. Reject linked paths, traversal, and unrelated same-name folders.

Before saving inside Git, resolve the intended repository root, refuse already tracked output, and inspect its `.gitignore`. Preserve existing bytes and line endings; append a root-anchored rule for only the generated output root when needed, creating `.gitignore` if absent. Verify exclusion with `git check-ignore`; never untrack files automatically. Outside Git, disclose that exclusion is unverified; workflows requiring Git retain that prerequisite. If safe storage or required exclusion fails, report the exact limitation before saving and use chat only when this workflow permits it.

Preserve existing state schemas, version identifiers, historical files, and resume paths; timestamp new run evidence beneath its existing owner without an implicit migration. Application source and project documents explicitly intended for version control retain their own contracts. This section does not authorize extra output for a chat-only request or expand the workflow's scope.
