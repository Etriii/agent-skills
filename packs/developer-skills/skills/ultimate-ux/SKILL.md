---
name: ultimate-ux
description: Review and improve existing application navigation content grouping task flows and interaction states across all pages or selected routes. Use for UX-only audits and wireframes with approval checkpoints or explicitly autonomous usability fixes while preserving the visual identity.
---

# Ultimate UX

Input: Target application, optional page selectors, user journeys and runtime access.

Output: A journey/page inventory, evidence-linked usability recommendations, authorized before/after previews, and authorized UX changes with verification.

This is the independently installable UX-only entrypoint of the Ultimate UI/UX suite. Use its local resources; no sibling skill is required. In Codex use `$ultimate-ux`; in Claude Code use `/ultimate-ux`. These are agent-chat instructions, not terminal commands.

- Bare invocation or `run` reviews all discovered pages for UX only and stops after showing the proposal.
- Add `--page <URL|route|file|name>` to limit pages; repeat it for several pages. Unresolved selectors never broaden scope.
- Add `--auto` to review, decide, preview, implement and verify usability changes without skill approval pauses. Explicit task-specific no-approval requests also select auto mode.
- Use `continue <run-folder>` to resume the exact recorded scope and checkpoint, `verify <run-folder>` for verification without fixes, or `help` for usage only.
- Focus is fixed to `ux`; reject conflicting focus options. Use `ultimate-ui-ux` for both disciplines or `ultimate-ui` for UI-only work.

Read [workflow](references/workflow.md) for every run. This entrypoint overrides that reference's coordinator default focus with `ux`. Read [UX review](references/ux-review.md), then [wireframes and verification](references/preview-and-verify.md) for previews/implementation/checks. Consult [source guidance](references/source-guidance.md) only when relevant.

For responsive web work, also read [mobile review](references/mobile-review.md); apply its journey/navigation checks within UX-only scope. Mobile account-menu access, filter discoverability and dialog recovery are part of the default review, not an optional extra.

Gated mode shows the review before any proposed layout; proposal approval authorizes sketches, and design approval authorizes application edits. Auto mode executes those stages without pausing while retaining artifacts and rationale. Preserve current visual identity except where the interaction requires an accessible presentation change. Keep roles, data access, validation and business policy intact. Choose tabs, sections, disclosure or routes per journey; never apply tabs to every long page.

Limits: Source evidence is not observed user behavior. Auto mode does not bypass platform permissions or expand scope. No fixed framework, external runtime, hosted service, other installed skill or network access is required. Publication, dependency installation and Git changes need separate task authorization.
