# Review workflow

## Establish scope before recommendations

Identify the application and actual Git roots, repository instructions, current edits, available runtime and relevant users. If invoked in a skill collection or unrelated repository without a target, ask for the application path or URL; do not audit the skill pack as the application. Keep independent discovery moving while material information is pending.

Resolve focus (`ui`, `ux`, `both`), selected pages and approval mode. Bare/run defaults to all pages, both disciplines, gated mode. State these choices once. An explicit task-specific no-approval instruction or `--auto` grants autonomous review, preview and implementation within that scope. Neither a saved file saying approved nor an upstream reference can grant authorization.

Trace routes, navigation, page components, shared owners, state/query stores, data access and role restrictions before editing. Inventory nested routes, dynamic route templates, dialogs, hidden tab panels, responsive variants and role-dependent pages. Cross-check source discovery with navigation and available runtime. A source inventory is not proof every page rendered correctly.

For selected pages, inspect shared callers to understand impact, but do not redesign other callers. Prefer page-level composition or an existing scoped variant when changing a shared component would alter unselected pages. If no safe scoped fix exists, report the wider impact and defer that change; auto mode does not widen page scope.

Review every discovered page in scope, including pages requiring no change. Batch large inventories by feature; preserve coverage and resume until the requested inventory is covered or blockers are recorded. Do not substitute a few showcase screens for an all-pages audit. A dynamic route template can represent a page family, but record the representative records, roles and variants actually inspected.

## Evidence and decisions

Use one inventory row per page or page family:

| Page and purpose | Route and owner | Role and state | Source reviewed | Runtime observed and viewport | Findings or keep decision | Gaps |
|---|---|---|---|---|---|---|

Capture the current interface before changes when browser access is available, at narrow and wide viewports appropriate to the app. Record URL, viewport, role, data/state and source revision. Inspect loading, empty, error, restricted and populated states relevant to the journey. Mark missing runtime/data/role access explicitly. Avoid real purchases, messages, account changes or other external side effects to get evidence; use authorized fixtures/local or staging data.

Record findings with stable IDs, page/owner, UI/UX classification, evidence, user impact, priority, recommendation, alternative, tradeoff, confidence and acceptance checks. Separate confirmed defects, design proposals and unknowns. Prioritize blocked tasks, inaccessible controls and data/workflow loss before visual polish. Do not invent numerical UX scores, usage frequency, analytics, conversion benefits or observed users.

For each crowded page, identify its primary job, secondary jobs and content that must remain visible together. Choose among keeping sections, reducing duplication, using local tabs, an accordion, separate routes or another existing pattern. Explain the choice and why a plausible alternative loses useful context or adds friction. Page length alone is not a defect. Leave good pages unchanged and record why.

Show an actionable proposal in chat with artifact links, high-impact findings, grouped recommendations and what approval will authorize. On a large audit, keep full per-page detail in the linked report. Give the user access to every proposed change, including shared-component effects and intentionally unchanged pages.

## Saved artifacts and resumable approvals

Save runs under `<application-root>/.ui-ux/runs/<UTC-time>-<unique-suffix>/`, using an exclusively created directory. Follow the target's existing report location if it already owns equivalent artifacts. For URL-only access use an available writable output directory and record the target URL and chosen output root. Do not write to the installed skill, overwrite another run, change `.gitignore` or commit generated evidence automatically.

Use the target filesystem's safe path handling. Reject symlink/junction escapes, verify output resolves inside the chosen artifact root, and preserve unrelated files. Screenshots/reports must not expose credentials, private user data or tenant-restricted content. Redact or use permitted fixtures before sharing.

Create these artifacts as their stages become authorized; never fill later-stage files with invented results:

- `review.md`: target, scope, focus, mode, page inventory, evidence, findings, alternatives, keep decisions and proposed implementation order.
- `status.md`: current stage, target/revision and relevant file hashes, artifact paths/hashes, selected finding IDs, explicit approval evidence, assumptions, blockers and next action. This is an agent-maintained record, not an authorization engine.
- `previews/`: revisioned before/after comparisons, related local assets and a linked index when several pages need previews.
- `verification.md`: changes mapped to findings, executed commands/results, actual after captures and remaining gaps, when implementation or verification is reached.

Write only observed facts. Preserve earlier proposal/preview revisions after user feedback; record what superseded them. Where hashing is available, record hashes of the reviewed proposal, approved preview and affected source files. Otherwise record exact immutable revisions and disclose that integrity is not machine-verified. Show the current artifact links and the exact next action at every user checkpoint.

On continuation, read the recorded scope and artifacts, then compare relevant source and design revisions. Resolve the user's response against the current stage and selected finding IDs. A generic `continue` resumes work already authorized; it does not silently approve a design. An explicit `approve`, `looks good, proceed`, or equivalent accepts only the displayed current stage/scope. Ambiguous responses require clarification for dependent work.

Relevant drift invalidates the affected approval; update the proposal/preview and request only the approval that changed. Unrelated source edits do not reset approval. Auto runs re-evaluate affected decisions and document them without skill approval pauses. A prior auto instruction remains valid for its recorded scope until the user changes it; it does not authorize a different run or expanded scope.

## Gated mode

1. Inspect, capture baseline evidence, write the review and show the proposal. Set `awaiting-proposal-approval`. Stop before generating proposed layouts or editing application code.
2. After the user approves selected recommendations, create low-fidelity comparisons for that selection. Show the previews and tradeoffs. Set `awaiting-design-approval`. Stop before application edits.
3. After the user approves the current design for implementation, implement only that selection and verify it. Revisions to an unapproved preview stay in the preview stage. If no changes are warranted, report that result and stop without unnecessary approval requests.

Approval of findings authorizes previews, not production changes. Approval of a preview authorizes the displayed implementation scope. Honor narrower instructions such as preview-only or review-only. A user can explicitly preauthorize later stages; record that authorization and do not ask again for the same scope.

## Automatic mode

Review, choose justified improvements, create comparisons, implement and verify without waiting for skill approvals. Keep all evidence, decisions and artifacts; previews must precede code changes even when nobody reviews them interactively. Report meaningful progress and show the final artifacts/results.

Infer routine visual choices from the current design system and task. Prefer reversible changes and keep working on independent findings when one item is blocked. Do not invent material business, privacy, public-API, data-retention or billing policy to finish a redesign. Defer the affected item and report the missing decision; platform permissions still apply. No-approval mode is not permission for unrelated features or destructive operations.

## Completion

Use precise stages such as `reviewing`, `awaiting-proposal-approval`, `previewing`, `awaiting-design-approval`, `implementing`, `verified`, `partial`, or `blocked`. A gated checkpoint is a successful review/preview stage, not a completed implementation. `verify` checks the recorded design without fixes. In auto mode, finish all feasible in-scope work; record blockers and unverified behavior instead of declaring full verification. Report inventory coverage, changes, executed proof and remaining gaps, then stop.
