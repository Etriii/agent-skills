---
name: table-ux-review
description: Audit application tables and data grids for detail navigation and crowded row actions with role-aware recommendations and accessibility checks. Use when reviewing table interactions or implementing a requested table UX cleanup rather than database schemas.
---

# Table UX Review

Input: Target application or selected routes, relevant roles and workflows, and available source and browser access. If no application is identified, report the missing target instead of claiming a table audit.

Output: A table inventory with evidence, navigation and action-placement decisions, prioritized findings, and explicit coverage gaps. Review by default; implement changes when the user's task authorizes them. An audit-and-fix request already authorizes in-scope fixes and does not require a second approval step.

## Establish coverage and ownership

- For an all-tables request, trace routes and screens, shared table components, native tables, library data grids, and custom row lists that function as tables. Include tables in dialogs, tabs, responsive variants, and role-dependent views. Classify layout-only tables separately.
- Search component definitions and their callers; a search for `<table>` alone is insufficient. Record each table instance even when several reuse one component. Cross-check source discoveries against available application navigation and rendered states.
- Trace row identity, route builders, nested-control events, selection, inline editing, bulk actions, and permission rules before recommending changes. Follow actions through their handlers to the existing detail page and server boundary where available.
- Record source-reviewed and browser-verified coverage separately. Mark unavailable roles, routes, data, or runtime access as unverified; do not claim complete runtime coverage from static discovery.

## Decide detail navigation per table

- Determine whether a row represents an entity with a meaningful, existing detail destination. Verify the correct identifier, route, and access rules. Summary, comparison, editable, or selection-only rows may need no detail navigation. Report a missing destination rather than inventing a route or expanding into a new detail-page feature.
- Prefer a real link on the item name or identifier, using the application's router link with a valid href where appropriate. Default to same-tab navigation while retaining native Ctrl/Cmd-click, middle-click, context-menu, and copy-link behavior. Honor an explicit new-tab requirement or established workflow; indicate that a new tab opens and use appropriate opener protection.
- Treat whole-row clicking as an optional convenience, never the only keyboard-accessible path. Preserve table semantics and the explicit link. Do not wrap a row containing controls in a link or replace native link behavior with a click-only handler.
- Keep clicks on checkboxes, menus, buttons, other links, and editable controls independent of row navigation. Preserve text selection and existing modified-click behavior; check the actual event path instead of applying propagation stops everywhere.
- Check whether returning to the list preserves necessary filters, sorting, pagination, scroll, and selection. Report navigation-state loss when it affects the workflow; reuse existing state owners for authorized fixes.

## Decide action placement per role and state

- Inventory each action's visibility, availability, frequency evidence, consequence, and existing destination. Inspect workflow requirements or observed usage; label frequency assumptions when no evidence exists. Count visible row actions for each relevant role and state.
- More than three visible action buttons is a review trigger, not a hard limit. Keep frequent or time-sensitive actions visible when justified. Consider the existing overflow-menu pattern for secondary actions and the detail page for infrequent or complex actions that benefit from context. A detail link may make a separate View button redundant.
- Preserve list-level and bulk workflows when processing many records. Do not move actions solely to reach a button count or hide a critical action behind extra navigation without assessing the cost.
- Before removing a list action, verify its replacement is reachable by the same authorized roles in all relevant states. Preserve confirmation, validation, disabled-state explanations, loading and error feedback, and server authorization. Relocation must neither grant access nor remove the only available path. Report gaps that require a separate feature or policy decision.

## Report and verify

Use one inventory row per table instance with these fields, splitting into supporting action notes when needed:

| Page and table | Shared owner and source | Role and state | Current detail route and trigger | Actions and proposed placement | Decision and reason | Evidence and gaps |
|---|---|---|---|---|---|---|

Include unchanged tables and explain deliberate exceptions. Prioritize findings by broken access, accidental navigation, lost workflows, and usability impact. Distinguish confirmed defects from proposals and missing evidence; state the discovered, source-reviewed, and browser-verified totals with the audit scope.

For authorized changes, reuse existing route helpers, table components, menus, and state owners. Check affected callers before changing a shared component; keep entity-specific decisions at the owner that knows the workflow. Do not perform a blanket rewrite or introduce a new component framework.

Use the target project's existing tools for the smallest sufficient verification:

- Verify correct entity navigation, direct detail access and permissions, normal and modified link activation, and explicitly requested new-tab behavior.
- Exercise checkbox selection, inline editing, nested controls, text selection, bulk actions, and list-state recovery where present; confirm they do not trigger unintended navigation.
- Check keyboard access, visible focus, meaningful link names, table/header semantics, and accessible overflow-menu focus and dismissal. Inspect touch/narrow layouts and relevant loading, empty, error, and disabled states.
- Verify relocated actions for the affected roles and lifecycle states, including restricted access and failure feedback. Add focused regressions for confirmed defects or changed shared behavior when warranted; do not add wording-matching tests for every checklist item.

Limits: Do not infer browser, screen-reader, or production acceptance from source inspection, automated scans, or a successful build. Report executed checks and remaining manual steps precisely. This skill requires no other installed skill, private runner, fixed UI library, or external service, and does not authorize installation, deployment, or unrelated product changes.

## Generated artifacts

Apply this section only when the workflow saves generated reports, logs, previews, or run evidence. Use a stable skill-owned root in the target workspace, never the installed skill directory. Allocate each new run with an exclusively created `YYYYMMDDTHHMMSSZ-<unique-id>/` directory (UTC); preserve earlier runs and resume the identified active run. Reject linked paths, traversal, and unrelated same-name folders.

Before saving inside Git, resolve the intended repository root, refuse already tracked output, and inspect its `.gitignore`. Preserve existing bytes and line endings; append a root-anchored rule for only the generated output root when needed, creating `.gitignore` if absent. Verify exclusion with `git check-ignore`; never untrack files automatically. Outside Git, disclose that exclusion is unverified; workflows requiring Git retain that prerequisite. If safe storage or required exclusion fails, report the exact limitation before saving and use chat only when this workflow permits it.

Preserve existing state schemas, version identifiers, historical files, and resume paths; timestamp new run evidence beneath its existing owner without an implicit migration. Application source and project documents explicitly intended for version control retain their own contracts. This section does not authorize extra output for a chat-only request or expand the workflow's scope.
