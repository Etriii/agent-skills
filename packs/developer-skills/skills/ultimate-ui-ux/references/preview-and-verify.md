# Before/after previews and implementation proof

## Build a reviewable comparison

Follow the current run's authorization in [workflow](workflow.md). Default improvements and direct fixes omit previews unless requested; use the implementation and verification sections below for those paths. Requested previews precede authorized edits, with a design-approval pause only when the user requests one. Preview-only never authorizes edits. Compatibility `--auto` and existing gated runs retain their recorded preview requirements; proposal approval authorizes previews in those gated runs. Use the existing design/prototyping environment if it fits; otherwise generate local HTML/CSS with minimal JavaScript for proposed interactions. No hosted service, image model, paid API, package installation or application rewrite is required for a low-fidelity preview.

Create an easy-to-open comparison with:

- Exact page/role/state, selected finding IDs and current preview revision.
- **Before:** actual pre-change captures at recorded viewports when available. Otherwise reconstruct the current layout from inspected source and label it `Reconstructed from source; runtime appearance unverified`. Never present a sketch or the starter's illustrative baseline as an application screenshot.
- **Proposed:** grayscale or restrained wireframes showing hierarchy, layout, grouping, labels, main controls and relevant loading/empty/error variants. Keep content/data comparable; do not hide difficult states or remove features to make the preview look cleaner.
- Narrow and wide layouts, clear change annotations, alternatives/tradeoffs and expected preserved behavior.
- Functional controls for the interactions being proposed, such as tabs or disclosure. Other controls must either work meaningfully inside the prototype or be clearly marked as nonfunctional; no real network writes.

Use [the comparison starter](../assets/comparison.html) as an illustrative store example only. Replace its page content, baseline, labels, controls, finding IDs and responsive composition for the target; a stock store template does not satisfy a dashboard or form review. For several pages, create a linked preview index; show distinct changed page layouts and relevant shared-component variants. The preview should not replace every unaffected page with another mockup.

Keep assets local and references portable inside the run. Respect image and font rights. Do not embed private screenshots in publicly hosted artifacts. If opening a browser requires platform permission, use the normal permission mechanism. If no browser renderer is available, provide the HTML/sketch and clearly state that it has not been visually inspected; do not claim a successful render.

Review the prototype at the requested widths. Check content completeness, focus, switching states, text wrapping and overflow. Show the current preview/index links in chat before requesting design approval. Revisions preserve earlier files and approval bindings. The approved artifact is the implementation specification, not proof the application behaves that way.

## Feature-based preview folder

For new previews, keep one `previews/` root inside the existing run. Its `index.html` is the entry page, linking feature folders named after the application's actual features. Even a single-feature run uses this entry page. For example:

```text
.ui-ux/runs/<run-id>/
  review.md                 Review runs only
  status.md
  verification.md           When checks run
  previews/                 Only when previews are required/requested
    index.html
    orders/
      index.html
      revisions/
        v001/
          index.html        Before/after comparison
          assets/
    checkout/
      index.html
      revisions/
        v001/
          index.html
          assets/
```

`<run-id>` is the existing UTC timestamp plus unique suffix. Use filesystem-safe lowercase feature slugs, such as `orders` or `account-settings`; disambiguate duplicate feature names by their real module. Never use raw URLs, route parameters or user-supplied path segments as output paths. Validate all destinations within the run root using the workflow's path rules.

Each feature index links its current comparison and preserved earlier revisions. Comparison pages identify the feature, concrete routes, roles, states, viewports and related finding IDs or direct task. One feature may contain several page comparisons; keep them clearly labeled. Add revision directories only when producing previews, and asset folders only when assets exist. Preserve published comparison files and their assets; create `v002` and update indexes for a revision rather than replacing an approved comparison. Record exact comparison paths/hashes in status so a changing index never grants approval to another revision.

Use relative links and keep generated preview assets within this root. Reuse common assets under `previews/assets/` when useful instead of duplicating them. Do not create separate top-level preview directories per feature. Existing saved runs, links and approval paths remain valid; do not move historical previews into this layout automatically.

## Implement the approved or autonomous selection

Recheck current edits and affected owners. Reuse the existing router, state management, tokens, accessible components and tests. Keep behavior shared only where the existing owner has the necessary context. Avoid blanket layout rewrites, duplicate guards, package/framework replacements or new API/business behavior to support a cosmetic change.

Preserve data, role/tenant access, confirmation, validation, nested controls and return state. For a page-limited request, examine shared callers and keep unselected page behavior stable. If UI-only review reveals a structural UX issue, or UX-only review reveals a brand overhaul opportunity, report it outside the implementation selection. Apply only changes supported by the selected focus and user authorization.

## Verify observable outcomes

Choose the smallest sufficient target-project proof based on what changed:

- Changed visual composition: run relevant build/type/lint checks; inspect actual narrow/wide renders and long/empty/error content. Check focus, contrast and zoom/reflow where affected.
- Changed interactions: test main and recovery journeys, keyboard access and mobile/touch behavior. For tabs, exercise all panels, direct link/reload/back behavior when supported, focus/selection semantics and retained filters/scroll.
- Changed shared components: inspect affected callers and relevant role/state variants, including unselected callers where behavior must remain stable. Add focused regressions for changed state/navigation behavior or confirmed defects when the project supports them.
- Changed data access or requests: verify existing permissions, query boundaries, loading/error behavior, caching and duplicate request handling. Do not claim provider/production behavior from local fixtures.

Inspect actual post-change application renders in comparable conditions when needed for the changed behavior. Do not save screenshots or run routine capture passes by default. Save and link post-change screens only when screenshots/previews are requested or the compatibility/saved run requires them; keep them separate from proposed sketches. A passing build, screenshot file, prototype or source search does not establish a complete user journey, screen-reader acceptance or production behavior. Report the command, result, scope and evidence type briefly in chat; mark skipped or blocked checks honestly.

Map implemented/kept/deferred findings or direct-task acceptance checks to changed files and proof in working context. Write `verification.md` and update `status.md` only for an opted-in saved run, not as default bookkeeping. Return scope, changes, executed checks and material limitations briefly in chat; add artifact links only when saving was requested. Do not create optional logs, reports or follow-up tasks to finish an ordinary improvement. Stop after the selected scope; never start another feature or publish automatically.
