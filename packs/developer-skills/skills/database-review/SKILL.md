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
