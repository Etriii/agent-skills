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

## Generated artifacts

Apply this section only when the workflow saves generated reports, logs, previews, or run evidence. Use a stable skill-owned root in the target workspace, never the installed skill directory. Allocate each new run with an exclusively created `YYYYMMDDTHHMMSSZ-<unique-id>/` directory (UTC); preserve earlier runs and resume the identified active run. Reject linked paths, traversal, and unrelated same-name folders.

Before saving inside Git, resolve the intended repository root, refuse already tracked output, and inspect its `.gitignore`. Preserve existing bytes and line endings; append a root-anchored rule for only the generated output root when needed, creating `.gitignore` if absent. Verify exclusion with `git check-ignore`; never untrack files automatically. Outside Git, disclose that exclusion is unverified; workflows requiring Git retain that prerequisite. If safe storage or required exclusion fails, report the exact limitation before saving and use chat only when this workflow permits it.

Preserve existing state schemas, version identifiers, historical files, and resume paths; timestamp new run evidence beneath its existing owner without an implicit migration. Application source and project documents explicitly intended for version control retain their own contracts. This section does not authorize extra output for a chat-only request or expand the workflow's scope.
