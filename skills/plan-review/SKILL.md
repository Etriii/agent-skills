---
name: plan-review
description: Review a complete implementation plan for coverage and dependency ordering before development begins.
---

# Plan Review

Input: A source plan, available repository evidence and the requested review boundary.

Output: A requirement-to-phase map, dependency findings with source lines, unanswered decisions and a recommended next review.

1. Read every phase at a high level before inspecting the next phase deeply. Preserve original phase IDs, subtask IDs, acceptance criteria and source line references.

2. Map shared prerequisites once; identify backward dependencies, cycles and missing interfaces. Distinguish a frozen interface from a functioning implementation.

3. Compare existing source and tests with proposed work. Report already implemented, missing, conflicting and unknown behavior separately.

4. Preview any reordering with an old-to-new mapping and coverage proof; obtain approval before replacing a plan. Preserve completed history.

Limits: Review and recommend by default. Do not implement phases, invent dependencies or treat unchecked boxes as evidence.
