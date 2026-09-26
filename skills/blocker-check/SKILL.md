---
name: blocker-check
description: Find source-backed requirement and policy blockers before implementing a selected phase or feature.
---

# Blocker Check

Input: The selected scope, authoritative requirements, dependencies and existing evidence.

Output: Blockers and questions with severity, source, owner, mitigation, status and the smallest safe next action.

1. Check authority, requirements, dependency, business policy, privacy, security, authorization, migration, external integration, network, environment, Git, verification, manual review and production safety where relevant.

2. Separate hard blockers from advisory risks. An absent authoritative form or template blocks exact reproduction; do not invent one.

3. Ask eligibility, treatment of previously approved records and reminder behavior as separate policy questions. Do not collapse independent choices.

4. Give justified recommended-first options and allow a custom answer. Reuse still-applicable recorded decisions with provenance; changed policy requires revalidation.

5. Continue independent authorized work while awaiting a decision; stop dependent work. Record unavailable evidence explicitly.

Limits: Works from ordinary files without a runner or tracking directory. Do not decide normative policy or silently run missing prerequisite phases.
