# UX specialist

Review how users find information and complete tasks. UX-only work can change grouping, navigation and interactions, while preserving the current visual language except where presentation must change to make the interaction understandable and accessible. Do not use UX scope to introduce a new brand or unrelated visual makeover.

## Follow actual journeys

Identify primary users, their permissions, page entry points, main job, secondary jobs, success state and recovery paths. Trace actions through handlers, state owners and server boundaries. Check whether users can discover, start, complete, cancel, retry and return without lost work or accidental side effects.

Inspect information hierarchy, navigation depth, labels, redundant actions, hidden features, forms, search/filter/sort/pagination, bulk actions and detail navigation. Check loading, empty, error, validation, offline and restricted states where relevant. Preserve authorization and confirmation at the existing responsible layer. Relocating controls must not grant access or remove the only path for an authorized role.

Use product requirements, observed behavior and real evidence for frequency or importance. Label hypotheses. A longer flow may be correct when it prevents consequential mistakes; fewer clicks is not a universal objective.

## Decide content grouping per page

| Pattern | Fits when | Check before choosing |
|---|---|---|
| Visible sections | People need to read, compare or use the content together. | Clear headings, meaningful order and jump links may solve the problem. |
| Local tabs | Peer views share a context and users usually work with one view at a time. | Discoverable labels, essential summaries outside panels, state retention, keyboard behavior and link/history needs. |
| Accordion/disclosure | Secondary, independent details are useful on demand. | Important content must remain findable; allow multiple sections when comparison matters. |
| Separate routes | Views have distinct tasks, permissions or meaningful standalone destinations. | Stable direct links, browser back, navigation context and preserved list state. |
| Progressive form/step flow | Tasks have genuine dependencies or require staged validation. | Preserve entered data, show progress, support back and avoid artificial extra steps. |

Do not turn every long page into tabs, hide key purchase/safety information, or move every action into menus. Consider search/find-in-page, printing, discoverability, accessibility and comparison before hiding content. Distinguish page navigation from in-page panels: use route links for navigation, tab semantics for local panel switching. Choose meaningful labels instead of generic Tab 1/2/3.

### Store example, not a global template

If a store page primarily supports shopping and stacks Products, Channel and Reviews, a reasonable candidate is a shared store header plus Products/Channel/Reviews views, with Products selected on a fresh visit. Keep useful trust cues such as rating/review count visible near store identity, and make secondary views discoverable. Decide based on actual store journeys whether local panels or nested routes fit better.

Preserve valid direct links, reload and back behavior; a direct Reviews link should not be reset to Products. Retain product query, filters, sort, pagination, selection and scroll where useful. Decide whether inactive content stays mounted or its state lives in an existing store; avoid duplicate fetches, stale data and focus inside a hidden panel. Keep review submission/channel actions available to the same roles, with their existing validation and server authorization. Provide appropriate loading, empty and error states inside each view.

If tabs are selected, use the established accessible component or follow the [WAI-ARIA tabs pattern](https://www.w3.org/WAI/ARIA/apg/patterns/tabs/): labeled tablist, linked tabs/panels, selected state, roving focus, appropriate arrow/Home/End behavior and keyboard activation. Only auto-activate on focus when content appears without noticeable delay; otherwise use manual activation. Ensure tab labels remain reachable on narrow screens. Test history/state and tab accessibility separately.

## Tables and actions

When relevant, reuse existing table/detail/navigation patterns and optionally consult an available `table-ux-review`. Keep explicit native links, modified-click behavior and independent nested controls. Preserve selection, editing, bulk workflows, effective permissions and return-to-list state. More than three visible row buttons is a review signal, not a deletion quota. Move only secondary actions whose replacement remains reachable for every relevant role/state.

## Recommendation and proof

Explain the current friction, user task, evidence, chosen pattern, rejected alternative and affected roles/states. Define acceptance as an observable journey, such as finding a review, switching back to Products without losing a filter, or recovering from a failed save. Include unchanged pages and counterexamples where sections are better than tabs. For relevant heuristics consult [source guidance](source-guidance.md); the product's actual task determines the choice.
