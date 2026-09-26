---
name: architecture-review
description: Review ownership boundaries coupling and dependency tradeoffs for a proposed software change.
---

# Architecture Review

Input: A concrete change or plan and the affected modules and dependency graph.

Output: Source-linked architecture findings, tradeoffs and a minimal coherent recommendation.

1. Trace the behavior and invariants across entrypoints, domain logic, persistence and external boundaries.

2. First consider existing behavior and responsible abstractions, then native or installed capabilities, then a small implementation where the invariant belongs.

3. Identify duplicated authority, misplaced validation, cyclic dependencies and modules with unrelated responsibilities. Separate observed problems from speculative future needs.

4. Compare migration and compatibility costs of recommendations; prefer a coherent ownership change over duplicated guards or single-use scaffolding.

5. Specify focused regression proof and decision points for any public interface or irreversible change.

Limits: Planning advisor by default. Do not refactor the repository or introduce frameworks merely to satisfy stylistic preferences.
