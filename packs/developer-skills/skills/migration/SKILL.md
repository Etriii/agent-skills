---
name: migration
description: Implement an authorized compatibility-sensitive transition with preservation checks and a concrete rollback or recovery path.
---

# Migration

Input: The current and target contracts, affected readers and writers, existing data and approved transition scope.

Output: The requested transition stage with compatibility, preservation and rollback or recovery evidence.

1. Map all relevant readers, writers and stored forms before editing. Identify mixed-version operation, missing prerequisites and any step that could lose data or break existing clients.

2. Define a concrete forward sequence and rollback or recovery path. Use the existing migration or versioning owner. Separate reversible expansion from destructive contraction, and respect the authorized stopping boundary.

3. Preserve user data and unknown fields where compatibility requires it. Validate trust boundaries and make retries or partial completion safe and observable; do not silently reinterpret existing values.

4. Verify old and new readers at the required transition stages, preservation of representative existing data and the recovery path when practical. State any untested restoration or external dependency.

5. Report the applied stage, evidence and remaining steps. Continue to contraction only when it is within the existing authorization.

Limits: Use the target project's existing tools; no new migration engine is implied. Never manufacture a backup or successful rollback claim, and do not broaden data or policy authority.

## Generated artifacts

Apply this section only when the workflow saves generated reports, logs, previews, or run evidence. Use a stable skill-owned root in the target workspace, never the installed skill directory. Allocate each new run with an exclusively created `YYYYMMDDTHHMMSSZ-<unique-id>/` directory (UTC); preserve earlier runs and resume the identified active run. Reject linked paths, traversal, and unrelated same-name folders.

Before saving inside Git, resolve the intended repository root, refuse already tracked output, and inspect its `.gitignore`. Preserve existing bytes and line endings; append a root-anchored rule for only the generated output root when needed, creating `.gitignore` if absent. Verify exclusion with `git check-ignore`; never untrack files automatically. Outside Git, disclose that exclusion is unverified; workflows requiring Git retain that prerequisite. If safe storage or required exclusion fails, report the exact limitation before saving and use chat only when this workflow permits it.

Preserve existing state schemas, version identifiers, historical files, and resume paths; timestamp new run evidence beneath its existing owner without an implicit migration. Application source and project documents explicitly intended for version control retain their own contracts. This section does not authorize extra output for a chat-only request or expand the workflow's scope.
