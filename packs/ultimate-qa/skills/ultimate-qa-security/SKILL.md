---
name: ultimate-qa-security
description: Review authorization, data integrity, dependency exposure, and safe failure behavior as part of a software QA audit.
---

# Ultimate QA Security and Data

Trace important data from untrusted input through validation, authorization, persistence, output, and deletion. Check role and tenant boundaries, direct object access, secret handling, session and token handling, data retention, migration rollback, backups, and concurrent writes. Run the project's existing security and dependency checks in a disposable environment; wait for completed results and verify tool findings against code and behavior before reporting defects.

Use test accounts and synthetic data. For each finding include the affected role, entry point, precondition, observed result, expected result, and a safe reproduction. Redact secrets. Where testing would modify or expose real data, use code review and mark the runtime claim unverified. Destructive and active attack checks require an isolated environment, a restore path, and the kit's permission gate in `08_DESTRUCTIVE_TESTING.md`.
