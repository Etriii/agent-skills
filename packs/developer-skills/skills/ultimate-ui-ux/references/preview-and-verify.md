# Before/after previews and implementation proof

## Build a reviewable comparison

Follow the current run's authorization in [workflow](workflow.md). A proposal approval authorizes previews. In auto mode create them before application changes without pausing. Use the existing design/prototyping environment if it fits; otherwise generate local HTML/CSS with minimal JavaScript for the proposed interactions. No hosted service, image model, paid API, package installation or application rewrite is required for a low-fidelity preview.

Create an easy-to-open comparison with:

- Exact page/role/state, selected finding IDs and current preview revision.
- **Before:** actual pre-change captures at recorded viewports when available. Otherwise reconstruct the current layout from inspected source and label it `Reconstructed from source; runtime appearance unverified`. Never present a sketch or the starter's illustrative baseline as an application screenshot.
- **Proposed:** grayscale or restrained wireframes showing hierarchy, layout, grouping, labels, main controls and relevant loading/empty/error variants. Keep content/data comparable; do not hide difficult states or remove features to make the preview look cleaner.
- Narrow and wide layouts, clear change annotations, alternatives/tradeoffs and expected preserved behavior.
- Functional controls for the interactions being proposed, such as tabs or disclosure. Other controls must either work meaningfully inside the prototype or be clearly marked as nonfunctional; no real network writes.

Use [the comparison starter](../assets/comparison.html) as an illustrative store example only. Replace its page content, baseline, labels, controls, finding IDs and responsive composition for the target; a stock store template does not satisfy a dashboard or form review. For several pages, create a linked preview index; show distinct changed page layouts and relevant shared-component variants. The preview should not replace every unaffected page with another mockup.

Keep assets local and references portable inside the run. Respect image and font rights. Do not embed private screenshots in publicly hosted artifacts. If opening a browser requires platform permission, use the normal permission mechanism. If no browser renderer is available, provide the HTML/sketch and clearly state that it has not been visually inspected; do not claim a successful render.

Review the prototype at the requested widths. Check content completeness, focus, switching states, text wrapping and overflow. Show the current preview/index links in chat before requesting design approval. Revisions preserve earlier files and approval bindings. The approved artifact is the implementation specification, not proof the application behaves that way.

## Implement the approved or autonomous selection

Recheck current edits and affected owners. Reuse the existing router, state management, tokens, accessible components and tests. Keep behavior shared only where the existing owner has the necessary context. Avoid blanket layout rewrites, duplicate guards, package/framework replacements or new API/business behavior to support a cosmetic change.

Preserve data, role/tenant access, confirmation, validation, nested controls and return state. For a page-limited request, examine shared callers and keep unselected page behavior stable. If UI-only review reveals a structural UX issue, or UX-only review reveals a brand overhaul opportunity, report it outside the implementation selection. Apply only changes supported by the selected focus and user authorization.

## Verify observable outcomes

Choose the smallest sufficient target-project proof based on what changed:

- Changed visual composition: run relevant build/type/lint checks; inspect actual narrow/wide renders and long/empty/error content. Check focus, contrast and zoom/reflow where affected.
- Changed interactions: test main and recovery journeys, keyboard access and mobile/touch behavior. For tabs, exercise all panels, direct link/reload/back behavior when supported, focus/selection semantics and retained filters/scroll.
- Changed shared components: inspect affected callers and relevant role/state variants, including unselected callers where behavior must remain stable. Add focused regressions for changed state/navigation behavior or confirmed defects when the project supports them.
- Changed data access or requests: verify existing permissions, query boundaries, loading/error behavior, caching and duplicate request handling. Do not claim provider/production behavior from local fixtures.

Capture actual post-change application screens in comparable conditions and link them separately from proposed sketches. A passing build, screenshot file, prototype or source search does not establish a complete user journey, screen-reader acceptance or production behavior. Report the command, result, scope and evidence type; mark skipped or blocked checks honestly.

Map implemented/kept/deferred findings to changed files and proof in `verification.md`. Update `status.md` with the final stage and remaining actions. Show a concise final report with artifact links, coverage counts, changes, verification and material limitations. Stop after the selected scope; never start another feature or publish automatically.
