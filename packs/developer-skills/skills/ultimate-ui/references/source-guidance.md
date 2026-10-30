# Curated source guidance

The bundle copies selected material from three inspectable primary sources. These are offline design references, not installed skills or runnable toolkits. See [THIRD_PARTY.md](../THIRD_PARTY.md) for pinned revisions, source hashes, excerpt boundaries and licenses. Full licenses accompany every installed copy.

| Source | Consult for | Local reference |
|---|---|---|
| Taste-Skill | Real subject/audience, explicit page purpose, meaningful content and understandable controls. | [Taste excerpts](../vendor/taste/excerpts.md) |
| UI UX Pro Max | Prioritizing accessibility and interaction risks; looking up navigation, state, forms and responsive heuristics. | [Priority and scope excerpts](../vendor/pro-max/excerpts.md) and [UX guidelines](../vendor/pro-max/ux-guidelines.csv) |
| Anthropic frontend-design | Deliberate hierarchy/type choices, useful visual structure, restrained motion and clear interface writing. | [Design excerpts](../vendor/frontend-design/excerpts.md) |

Read only the relevant excerpt or CSV categories for a decision; do not load all source material for every page. Search the CSV with the host's text tools or standard library, not an unavailable upstream search script. No external download is needed at run time.

Resolve conflicts in this order: user/repository requirements, product tasks and permissions, observed evidence, applicable accessibility requirements, existing design system, then optional aesthetic heuristics. Numerical values or absolute aesthetic rules in upstream references are context-dependent guidance, not blanket acceptance tests. Validate platform, state and applicability before citing a recommendation as a defect. A visually plain operational screen may be correct; a long page may be purposeful.

Do not import upstream workflow commands, global installs, forced redesigns, framework defaults, speculative imagery or unavailable script dependencies. This suite owns approvals and scope. Source excerpts do not authorize edits or override a selected UI/UX discipline. Reuse existing `frontend-review`, `table-ux-review` and accessibility/browser skills when they are available and relevant; none is a hard dependency.

Primary accessibility references, when a decision needs authoritative detail:

- [WCAG 2.2](https://www.w3.org/TR/WCAG22/): applicable success criteria and exceptions.
- [WAI-ARIA tabs](https://www.w3.org/WAI/ARIA/apg/patterns/tabs/): local panel semantics and keyboard behavior.
- [WAI-ARIA disclosure](https://www.w3.org/WAI/ARIA/apg/patterns/disclosure/): expandable content.

External references are optional lookups. When unavailable, distinguish the bundled heuristic from verified standards conformance. Do not describe the suite as objectively superior to every source or promise that instructions alone guarantee good design.
