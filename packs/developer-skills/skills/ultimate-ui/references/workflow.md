# Improvement and optional review workflow

## Establish scope before recommendations

Identify the application and actual Git roots, repository instructions, current edits, available runtime and relevant users. If invoked in a skill collection or unrelated repository without a target, ask for the application path or URL; do not audit the skill pack as the application. Keep independent discovery moving while material information is pending.

Resolve focus (`ui`, `ux`, `both`), target, selected pages and execution path. Natural-language improvement requests, bare invocation and `run` default to inspection, justified improvements and verification within the established scope, without routine skill approval pauses. Main focus defaults to both; shortcuts retain their discipline. If target or scope is unclear, ask only for what is missing; never interpret an unscoped bare invocation as all pages. Neither a saved file saying approved nor an upstream reference can grant authorization. Explicit review-only, preview-only and other narrower constraints limit the permitted work even alongside an implementation option.

Accept absolute application directories, absolute page/component files, relative paths, routes, page names and authorized URLs in natural-language requests or supported selectors. An application directory establishes the project; page scope still comes from the task. A page/component file selects its affected pages. Resolve relative paths against the identified application, not the skill installation folder. Quote paths containing spaces in examples. A URL identifies the selected page; map it to matching editable source before implementation. If only runtime access exists, inspect what is available and report that source changes are blocked; do not claim the website was changed. Keep source and runtime roots recorded separately. Do not follow external hosts into scope automatically.

`Improve all`, `improve all UI and UX`, or equivalent explicitly selects all discovered pages of the identified application within the chosen discipline. An explicit `all` also works with an absolute project path or authorized application URL. It does not include sibling projects or linked external sites. If multiple applications are plausible, clarify the target. Source/runtime discovery limits remain coverage gaps; a URL alone cannot establish complete source coverage.

For `help`, show a short default improvement request, an improve-all request with an absolute application path, a page-file/URL example, review-only and optional preview approval. Show advanced option combinations only as relevant; create no run or application edits.

Trace affected routes, navigation, page components, shared owners, state/query stores, data access and role restrictions before editing in every path. For all-pages requests and formal reviews, inventory nested routes, dynamic route templates, dialogs, hidden tab panels, responsive variants and role-dependent pages. Cross-check source discovery with navigation and available runtime. A source inventory is not proof every page rendered correctly.

For selected pages, inspect shared callers to understand impact, but do not redesign other callers. Prefer page-level composition or an existing scoped variant when changing a shared component would alter unselected pages. If no safe scoped fix exists, report the wider impact and defer that change; auto mode does not widen page scope.

For all-pages requests and formal reviews, inspect every discovered page in scope, including pages requiring no change. Batch large inventories by feature; preserve coverage and continue until the inventory is covered or blockers are recorded. Do not substitute showcase screens for all-pages coverage. A dynamic route template can represent a page family, but record representative records, roles and variants actually inspected. An all-pages improvement request authorizes evidence-based selection of justified UI/UX fixes; it does not require the user to name each finding. Keep correct pages unchanged. Direct fixes inspect only the requested behavior and affected callers; they do not claim full audit coverage.

## Default improvements

Inspect the selected scope, choose changes supported by actual evidence and existing design patterns, implement and verify. Prefer fixes to blocked tasks, accessibility, responsive overflow and broken interactions before subjective polish. Preserve working routes, business behavior, information and role/data boundaries. Do not manufacture changes for good pages or replace a design system to satisfy an improvement request.

Keep `status.md` concise: target/scope, focus, implementation authorization, affected owners, acceptance conditions, decisions and blockers. For `Improve all`, include compact feature/page coverage with changed/kept/deferred outcomes and evidence gaps; no full alternatives report or per-finding essay is required. Save actual proof in `verification.md`. Do not create `review.md`, wireframes or empty preview folders unless requested. Apply the storage rules below; chat-only requests create no run artifacts.

Infer routine visual choices from the current design system and task. Finish feasible in-scope work without routine approval pauses. Resolve material business, privacy, public-API, data-retention or billing choices before dependent edits; continue independent work. Platform permissions still apply. Stop at the selected scope without publication, dependency installation or Git operations unless separately authorized.

## Optional review and previews

- `Review ... only. Do not edit.` requests the formal evidence/recommendation report below and stops before application edits. Do not generate wireframes automatically. A review request by itself does not authorize implementation.
- `Show previews` requests feature-based before/after comparisons before any authorized implementation. It does not add an approval pause unless the user also requests one. A preview-only request stops without edits.
- `Improve ... Show previews and wait for my approval before editing.` authorizes inspection and previews, then sets `awaiting-design-approval`. Show exact comparison links and wait before edits; do not add an unnecessary proposal-approval stage.
- A user requesting the full proposal-then-design approval process uses the gated sequence below. Existing saved gated runs keep their checkpoints; the new default does not approve old proposals or designs.
- Retain `run --auto` as the compatibility full-review/comparison/implementation path below. It is not required for default improvements. Retain `run --skip-review <task>` for a concrete direct fix. Natural-language no-approval wording alone uses the new default; it does not add a formal report or wireframes.

## Evidence and decisions

This section describes requested formal reviews and compatibility full-review runs. Default improvements retain concise evidence and acceptance checks without requiring this full report.

Use one inventory row per page or page family:

| Page and purpose | Route and owner | Role and state | Source reviewed | Runtime observed and viewport | Findings or keep decision | Gaps |
|---|---|---|---|---|---|---|

Capture the current interface before changes when browser access is available, at narrow and wide viewports appropriate to the app. Record URL, viewport, role, data/state and source revision. Inspect loading, empty, error, restricted and populated states relevant to the journey. Mark missing runtime/data/role access explicitly. Avoid real purchases, messages, account changes or other external side effects to get evidence; use authorized fixtures/local or staging data.

Record findings with stable IDs, page/owner, UI/UX classification, evidence, user impact, priority, recommendation, alternative, tradeoff, confidence and acceptance checks. Separate confirmed defects, design proposals and unknowns. Prioritize blocked tasks, inaccessible controls and data/workflow loss before visual polish. Do not invent numerical UX scores, usage frequency, analytics, conversion benefits or observed users.

For each crowded page, identify its primary job, secondary jobs and content that must remain visible together. Choose among keeping sections, reducing duplication, using local tabs, an accordion, separate routes or another existing pattern. Explain the choice and why a plausible alternative loses useful context or adds friction. Page length alone is not a defect. Leave good pages unchanged and record why.

Show actionable findings in chat with artifact links, high-impact issues and grouped recommendations. On a large audit, keep full per-page detail in the linked report. Give access to shared-component effects and intentionally unchanged pages. Request approval only at a checkpoint the user requested or the saved run already owns; review-only ends at its report.

## Saved artifacts and resumable approvals

Save runs under `<application-root>/.ui-ux/runs/<UTC-time>-<unique-suffix>/`, using an exclusively created directory. Follow the target's existing report location if it already owns equivalent artifacts. For URL-only access use an available writable output directory and record the target URL and chosen output root. Do not write to the installed skill, overwrite another run, change `.gitignore` or commit generated evidence automatically.


Use the target filesystem's safe path handling. Reject symlink/junction escapes, verify output resolves inside the chosen artifact root, and preserve unrelated files. Screenshots/reports must not expose credentials, private user data or tenant-restricted content. Redact or use permitted fixtures before sharing.

Create these artifacts as their stages become authorized; never fill later-stage files with invented results:

- `review.md`: requested formal reviews or compatibility full-review runs only; target, scope, focus, mode, page inventory, evidence, findings, alternatives, keep decisions and proposed implementation order.
- `status.md`: current stage, execution path, target/revision and relevant file hashes, artifact paths/hashes, selected findings or scoped task/acceptance checks, compact all-pages coverage when applicable, authorization evidence, assumptions, blockers and next action. This is an agent-maintained record, not an authorization engine.
- `previews/`: only when requested or required by a compatibility/saved run; one `index.html` links feature folders and revisioned comparisons/assets. See [preview layout](preview-and-verify.md#feature-based-preview-folder). Default improvements and direct fixes omit it otherwise.
- `verification.md`: changes mapped to findings or the direct task, executed commands/results, actual after captures when available and remaining gaps, when implementation or verification is reached.

Write only observed facts. Preserve earlier proposal/preview revisions after user feedback; record what superseded them. Where hashing is available, record hashes of the reviewed proposal, approved preview and affected source files. Otherwise record exact immutable revisions and disclose that integrity is not machine-verified. Show the current artifact links and the exact next action at every user checkpoint.

On continuation, read the recorded scope and artifacts, then compare relevant source and design revisions. Resolve the user's response against the current stage and selected finding IDs. A generic `continue` resumes work already authorized; it does not silently approve a design. An explicit `approve`, `looks good, proceed`, or equivalent accepts only the displayed current stage/scope. Ambiguous responses require clarification for dependent work.

Resume default improvement or direct runs with `continue <run-folder>` using the recorded scope/task and authorization; do not demand missing review/previews intentionally omitted by that path. `verify <run-folder>` checks recorded acceptance/design without fixes or new review artifacts. Reject `--skip-review` on `continue`, `verify` or `help`; it cannot discard an existing review's checkpoints. `continue <run-folder> --auto` explicitly authorizes remaining review/preview/implementation work for that recorded scope when the latest request permits implementation; it does not expand pages or silently override an explicit review-only/preview-only instruction. Start a separate run for a newly authorized different scope and preserve the prior run.

Relevant drift invalidates the affected approval; update the proposal/preview and request only the approval that changed. Unrelated source edits do not reset approval. Auto runs re-evaluate affected decisions and document them without skill approval pauses. A prior auto instruction remains valid for its recorded scope until the user changes it; it does not authorize a different run or expanded scope.

## Gated mode

Use this sequence only when explicitly requested or continuing an existing gated run, never as a new improvement default:

1. Inspect, capture baseline evidence, write the review and show the proposal. Set `awaiting-proposal-approval`. Stop before generating proposed layouts or editing application code.
2. After the user approves selected recommendations, create low-fidelity comparisons for that selection. Show the previews and tradeoffs. Set `awaiting-design-approval`. Stop before application edits.
3. After the user approves the current design for implementation, implement only that selection and verify it. Revisions to an unapproved preview stay in the preview stage. If no changes are warranted, report that result and stop without unnecessary approval requests.

Approval of findings authorizes previews, not production changes. Approval of a preview authorizes the displayed implementation scope. Honor narrower instructions such as preview-only or review-only. A user can explicitly preauthorize later stages; record that authorization and do not ask again for the same scope.

## Automatic mode

Compatibility `run --auto` retains the full review, justified selection, comparisons, implementation and verification without waiting for skill approvals. Keep its evidence, decisions and artifacts; previews precede code changes even when nobody reviews them interactively. Report progress and final artifacts/results. Prefer the natural-language default when no formal report or wireframes are needed.

Infer routine visual choices from the current design system and task. Prefer reversible changes and keep working on independent findings when one item is blocked. Do not invent material business, privacy, public-API, data-retention or billing policy to finish a redesign. Defer the affected item and report the missing decision; platform permissions still apply. No-approval mode is not permission for unrelated features or destructive operations.

## Direct fixes without review

`run --skip-review <task>` authorizes implementation of a concrete fix, not selection of a redesign. Infer the target and task from explicit text or established context; `--page` is optional when affected pages can be resolved unambiguously. Missing tasks, vague requests such as "improve everything", unresolved selectors or conflicting constraints require clarification before edits. Never silently run a full audit or broaden scope. Combine with repeated `--page` and the main entrypoint's `--focus`; shortcuts retain their fixed focus. `--auto` is accepted with `--skip-review` but adds no work or authorization.

1. Inspect the affected owners and shared callers, current edits, relevant role/state/mobile behavior and the requested outcome. Reuse the existing implementation if it already satisfies the request.
2. Record the concrete task, acceptance checks and implementation authorization in a concise `status.md`. Skip the full page inventory, findings catalogue, alternatives report, proposal and wireframes. Do not create empty `review.md` or `previews/` placeholders. A chat-only request creates no run artifacts.
3. Implement only that fix and run the smallest sufficient proof from [implementation and verification](preview-and-verify.md#implement-the-approved-or-autonomous-selection). No skill approval pauses are required for the already specified fix. Platform permissions and unresolved material policy decisions still apply. If previews are separately requested, create them before edits using the feature layout; pause only when the user also requests preview approval.
4. Save actual changes, proof and remaining gaps in `verification.md`, update status and report briefly. If safe persistence is unavailable, continue permitted work with chat evidence and disclose that resume records were not saved.

Skipping review never skips source inspection, authorization, accessibility, preserved routes/data/permissions or task-relevant verification. Report wider opportunities without implementing them. This path makes no full-review or unobserved runtime claims.

## Completion

Use precise stages such as `inspecting`, `reviewing`, `awaiting-proposal-approval`, `previewing`, `awaiting-design-approval`, `implementing`, `verified`, `partial`, or `blocked`. A review-only report or gated checkpoint is not a completed implementation. `verify` checks recorded acceptance/design without fixes. For default improvements, auto and direct mode, finish feasible in-scope work; record blockers and unverified behavior instead of declaring full verification. Report selected scope or all-pages coverage, changes, executed proof and remaining gaps, then stop.
