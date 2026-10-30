---
name: ultimate-mobile
description: Audit and improve mobile web layouts navigation headers filters dialogs and touch usability across all pages or selected routes with before and after previews. Use for phone viewport reviews with approval checkpoints or explicitly autonomous responsive fixes while preserving desktop behavior.
---

# Ultimate Mobile

Input: Target web application, optional page selectors, mobile constraints, relevant users and runtime access.

Output: A mobile page/state inventory, evidence-linked UI/UX recommendations, authorized before/after previews, and authorized responsive changes with verification and desktop preservation checks.

This is the standalone mobile web entrypoint of the Ultimate UI/UX suite. Required resources are local; no sibling installation is needed. Codex uses `$ultimate-mobile`; Claude Code uses `/ultimate-mobile`. These are agent-chat instructions, not terminal commands.

- Bare invocation or `run` reviews all discovered pages for mobile UI and UX, then shows the proposal and stops for approval.
- Add `--page <URL|route|file|name>` to limit pages; repeat it for several pages. Unresolved selectors never broaden scope.
- Add `--auto` to review, decide, preview, implement and verify mobile improvements without skill approval pauses. Explicit task-specific no-approval requests also select auto mode.
- Use `continue <run-folder>` to resume the recorded scope/checkpoint, `verify <run-folder>` for checks without fixes, or `help` for usage only.
- Focus is mobile web UI and UX, with desktop checked for regressions. Reject conflicting focus options; use the discipline-specific entrypoints for UI-only/UX-only work. Honor user-specified viewports and narrower natural-language scope.

Read [workflow](references/workflow.md) for each run; this entrypoint sets its defaults to both disciplines with mobile web as the target. Read [mobile review](references/mobile-review.md) plus [UI review](references/ui-review.md) and [UX review](references/ux-review.md) for affected decisions. Read [previews and verification](references/preview-and-verify.md) before sketches, implementation or verification. Consult [source guidance](references/source-guidance.md) only when relevant.

Gated mode requires proposal approval before sketches and design approval before application edits. Auto mode executes those stages without pausing while retaining artifacts and rationale. Keep names/actions reachable when simplifying headers, preserve filter/form state, distinguish cancel/primary/destructive actions and retain role/tenant boundaries. Do not force one responsive pattern on every page or redesign desktop under mobile-only scope.

Limits: Main UI/UX skills already include mobile checks; this shortcut does not enable them. Source inspection and browser emulation do not establish real-device or screen-reader acceptance. No native app, fixed framework, hosted service, external package, other skill or network access is required. Platform permissions and the selected scope still apply; publication, dependency installation and Git operations require separate authorization.
