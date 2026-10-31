---
name: database-review
description: Review schema migrations data invariants concurrency and recovery before database changes.
---

# Database Review

Input: Schemas, migrations, queries, data compatibility requirements and backup evidence.

Output: Integrity and migration findings with preservation, rollback and concurrency verification steps.

1. Identify authoritative constraints, foreign keys, uniqueness, nullability and transaction isolation needed by the change.

2. Trace old and new readers/writers across deployment order; preserve historical meaning and existing records.

3. Check backfill batching, locking, concurrent writes and failure recovery. Avoid destructive conversion before compatibility and backup proof.

4. Differentiate reversible schema rollback from restoration of lost data. Record recovery prerequisites and who owns approval.

5. Use the actual database engine for engine-specific claims; mark in-memory fixtures and mock races as limited evidence.

Limits: Review only by default. Do not run migrations, delete records or declare restoration proven without an executed restore.

## Generated artifacts

Apply this section only when the workflow saves generated reports, logs, previews, or run evidence. Use a stable skill-owned root in the target workspace, never the installed skill directory. Allocate each new run with an exclusively created `YYYYMMDDTHHMMSSZ-<unique-id>/` directory (UTC); preserve earlier runs and resume the identified active run. Reject linked paths, traversal, and unrelated same-name folders.

Before saving inside Git, resolve the intended repository root, refuse already tracked output, and inspect its `.gitignore`. Preserve existing bytes and line endings; append a root-anchored rule for only the generated output root when needed, creating `.gitignore` if absent. Verify exclusion with `git check-ignore`; never untrack files automatically. Outside Git, disclose that exclusion is unverified; workflows requiring Git retain that prerequisite. If safe storage or required exclusion fails, report the exact limitation before saving and use chat only when this workflow permits it.

Preserve existing state schemas, version identifiers, historical files, and resume paths; timestamp new run evidence beneath its existing owner without an implicit migration. Application source and project documents explicitly intended for version control retain their own contracts. This section does not authorize extra output for a chat-only request or expand the workflow's scope.
