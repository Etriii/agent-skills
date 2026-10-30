---
name: ultimate-ui
description: Review and improve existing interface layout hierarchy typography spacing consistency and responsive presentation across all pages or selected routes. Use for UI-only audits and wireframes with approval checkpoints or explicitly autonomous visual fixes while preserving task flows.
---

# Ultimate UI

Input: Target application, optional page selectors, design references and runtime access.

Output: A visual page inventory, evidence-linked recommendations, authorized before/after previews, and authorized UI changes with verification.

This is the independently installable UI-only entrypoint of the Ultimate UI/UX suite. Use its local resources; no sibling skill is required. In Codex use `$ultimate-ui`; in Claude Code use `/ultimate-ui`. These are agent-chat instructions, not terminal commands.

- Bare invocation or `run` reviews all discovered pages for UI only and stops after showing the proposal.
- Add `--page <URL|route|file|name>` to limit pages; repeat it for several pages. Unresolved selectors never broaden scope.
- Add `--auto` to review, decide, preview, implement and verify visual changes without skill approval pauses. Explicit task-specific no-approval requests also select auto mode.
- Use `continue <run-folder>` to resume the exact recorded scope and checkpoint, `verify <run-folder>` for verification without fixes, or `help` for usage only.
- Focus is fixed to `ui`; reject conflicting focus options. Use `ultimate-ui-ux` for both disciplines or `ultimate-ux` for UX-only work.

Read [workflow](references/workflow.md) for every run. This entrypoint overrides that reference's coordinator default focus with `ui`. Read [UI review](references/ui-review.md), then [wireframes and verification](references/preview-and-verify.md) for previews/implementation/checks. Consult [source guidance](references/source-guidance.md) only when relevant.

Gated mode shows the review before any proposed layout; proposal approval authorizes sketches, and design approval authorizes application edits. Auto mode executes those stages without pausing while retaining artifacts and rationale. Preserve information architecture, routes, task order, permissions and current business behavior. Report structural UX opportunities separately; do not implement them under UI-only scope. Leave good pages unchanged.

Limits: Source evidence is not rendered proof. Auto mode does not bypass platform permissions or expand scope. No fixed framework, external runtime, hosted service, other installed skill or network access is required. Publication, dependency installation and Git changes need separate task authorization.
