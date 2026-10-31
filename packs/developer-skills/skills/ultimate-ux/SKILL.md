---
name: ultimate-ux
description: Inspect and improve existing application UX-only navigation and task flows, implement justified scoped fixes and verify them. Use for selected pages or explicitly all pages, with optional review-only reports and feature-based previews.
---

# Ultimate UX

Input: Target application and selected pages or explicit all-pages scope; absolute application/page paths, relative paths and authorized URLs are supported.

Output: Scoped UX-only navigation and task flows improvements with verification by default; formal review reports or previews only when requested. Keep source, prototype and observed runtime evidence distinct.

This independently installable entrypoint uses local resources; no sibling skill is required. Codex uses `$ultimate-ux`; Claude Code uses `/ultimate-ux`. These are agent-chat requests, not terminal commands.

## Use

- Natural-language requests, bare invocation and `run` inspect the established scope, choose justified improvements, implement and verify without routine skill approval pauses. Ask for target/scope if unclear; never silently select all pages.
- `Improve all` explicitly selects every discovered page of the identified application within this entrypoint's discipline. Keep correct pages unchanged and record coverage/gaps.
- `Review ... only. Do not edit.` requests findings without implementation or automatic previews. `Show previews and wait for my approval before editing` adds a design checkpoint. Previews are otherwise optional; a preview-only request never authorizes edits.
- An absolute application directory identifies the project, not all pages. An absolute page/component file selects affected pages. Resolve relative paths against the target application; a URL selects its page. URL-only access needs matching editable source for implementation; otherwise report that limitation.
- Existing `run --page <URL|route|absolute-or-relative-file|name>` supports repeated selectors. `--auto` keeps the full review/preview/implementation workflow without skill pauses; it is not needed for default improvements. `run --skip-review <task>` keeps the concrete-fix shortcut; task text or established context must identify the fix. Adding `--auto` to it is redundant. Unresolved selectors and vague concrete-fix requests require clarification without widening scope.
- `continue <run-folder>` resumes the recorded scope and checkpoints, including older gated runs. `verify <run-folder>` checks recorded acceptance/design without fixes. `help` shows defaults and copyable natural-language/option combinations without creating a run. Reject `--skip-review` on these operations.
- Focus is fixed to `ux` (UX-only navigation and task flows); reject conflicting focus options. Explicit narrower user constraints take precedence over implementation modes.

Independent agent-chat examples; replace paths, routes and task text with actual inputs:

```text
$ultimate-ux Improve /orders and verify the changes.
$ultimate-ux Improve all in "D:\My App".
$ultimate-ux Improve "D:\My App\src\pages\Orders.vue".
$ultimate-ux Improve https://localhost:3000/orders using the source in "D:\My App".
$ultimate-ux Review /orders only. Do not edit.
$ultimate-ux Improve /orders. Show previews and wait for my approval before editing.
$ultimate-ux run --page /orders --skip-review Preserve entered values after validation errors.
```

Read [workflow](references/workflow.md) for scope, authorization, storage and continuation. It uses this entrypoint's fixed focus. Consult [UX-only navigation and task flows guidance](references/ux-review.md) and [mobile guidance](references/mobile-review.md) only for affected decisions. Read [implementation and verification](references/preview-and-verify.md) for changes/checks; preview sections apply only when previews are requested or required by an existing run. Consult [source guidance](references/source-guidance.md) only when relevant.

Preserve visual identity, permissions, data boundaries and working routes. Do not add a brand overhaul under UX-only scope. Inspect affected owners and shared callers, preserve accessibility and role/data boundaries, and verify the changed behavior. New previews share one run-local feature index; existing links and revisions stay valid.

Limits: Source inspection is not rendered proof; browser emulation is not real-device or screen-reader acceptance. No fixed framework, hosted service, external package, other skill or network access is required. Platform permissions and selected scope still apply. Publication, dependency installation and Git operations require separate task authorization.
