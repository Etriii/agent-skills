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

## Generated artifacts

Apply this section only when the workflow saves generated reports, logs, previews, or run evidence. Use a stable skill-owned root in the target workspace, never the installed skill directory. Allocate each new run with an exclusively created `YYYYMMDDTHHMMSSZ-<unique-id>/` directory (UTC); preserve earlier runs and resume the identified active run. Reject linked paths, traversal, and unrelated same-name folders.

Before saving inside Git, resolve the intended repository root, refuse already tracked output, and inspect its `.gitignore`. Preserve existing bytes and line endings; append a root-anchored rule for only the generated output root when needed, creating `.gitignore` if absent. Verify exclusion with `git check-ignore`; never untrack files automatically. Outside Git, disclose that exclusion is unverified; workflows requiring Git retain that prerequisite. If safe storage or required exclusion fails, report the exact limitation before saving and use chat only when this workflow permits it.

Preserve existing state schemas, version identifiers, historical files, and resume paths; timestamp new run evidence beneath its existing owner without an implicit migration. Application source and project documents explicitly intended for version control retain their own contracts. This section does not authorize extra output for a chat-only request or expand the workflow's scope.
