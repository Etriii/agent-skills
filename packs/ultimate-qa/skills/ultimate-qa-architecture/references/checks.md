# Architecture review checks

Use 0 = clear ownership, 1 = localized friction, 2 = recurring risk, 3 = active defect or pervasive obstruction. `Unassessed` means insufficient evidence; never convert it to zero. Record at least one representative path and the practical effect for every nonzero score.

| Dimension | Inspect | Evidence that matters |
|---|---|---|
| Boundaries | UI, business rules, API calls, persistence, background work | A rule duplicated across layers, direct persistence in views, bypassed validation |
| Dependency direction | Module imports and package structure | Cycles, domain logic coupled to framework details, changes that ripple across unrelated modules |
| Cohesion and duplication | Shared logic and file responsibilities | Two implementations of the same policy diverge; one file changes for unrelated reasons |
| State and data ownership | Transactions, concurrency, cache, migrations | Lost updates, inconsistent derived state, irreversible migration, undocumented source of truth |
| Security boundaries | Authentication, authorization, input validation, secrets | One route bypasses a policy, trust of client-supplied identity, leaked secret |
| Testability and observability | Tests around contracts, logging, failure modes | Critical behavior cannot be exercised in isolation; errors lack diagnosis |
| Change hygiene | Naming, dead code, configuration, dependency lifecycle | Ambiguous naming causes misuse; configuration required for a feature is absent from examples |

Report: dimension and score, evidence (`path:line` and behavior), impact, recommended smallest coherent repair, verification step, and confidence. Include one overall assessment only after the dimensions. Explain any weighting; do not imply a precise scientific grade.
