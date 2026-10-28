---
name: safe-refactor
description: Restructure code while preserving defined behavior and verifying public contracts before and after the change.
---

# Safe Refactor

Input: A requested structural change, its behavior-preservation boundary and existing verification.

Output: Clearer ownership or structure with evidence that the specified behavior remains intact.

1. Define what must remain stable, including public interfaces, ordering, errors, side effects and data semantics. Inspect the callers and establish relevant baseline verification before moving ownership.

2. Reuse the architecture's existing boundaries. Consolidate repeated rules at their proper owner; avoid adding an interface or service merely to wrap a single implementation.

3. Keep intermediate changes buildable and preserve unrelated edits. Separate any newly discovered feature or bug change from the refactor unless it is already within the authorized scope.

4. Run the same behavioral checks after the structural change, plus any affected integration checks. Explain which contracts were verified and which external behavior remains untested.

Limits: A refactor does not authorize changing public behavior, schema or policy. Stop at the requested structural outcome and keep the coordinator's acceptance process authoritative.
