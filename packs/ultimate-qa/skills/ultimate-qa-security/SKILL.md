---
name: ultimate-qa-security
description: Review authorization, data integrity, dependency exposure, and safe failure behavior as part of a software QA audit.
---

# Ultimate QA Security and Data

Trace important data from untrusted input through validation, authorization, persistence, output, and deletion. Check role and tenant boundaries, direct object access, secret handling, session and token handling, data retention, migration rollback, backups, and concurrent writes. Run the project's existing security and dependency checks in a disposable environment; wait for completed results and verify tool findings against code and behavior before reporting defects.

Use test accounts and synthetic data. For each finding include the affected role, entry point, precondition, observed result, expected result, and a safe reproduction. Redact secrets. Where testing would modify or expose real data, use code review and mark the runtime claim unverified. Destructive and active attack checks require an isolated environment, a restore path, and the kit's permission gate in `08_DESTRUCTIVE_TESTING.md`.

## Generated artifacts

Apply this section only when the workflow saves generated reports, logs, previews, or run evidence. Use a stable skill-owned root in the target workspace, never the installed skill directory. Allocate each new run with an exclusively created `YYYYMMDDTHHMMSSZ-<unique-id>/` directory (UTC); preserve earlier runs and resume the identified active run. Reject linked paths, traversal, and unrelated same-name folders.

Before saving inside Git, resolve the intended repository root, refuse already tracked output, and inspect its `.gitignore`. Preserve existing bytes and line endings; append a root-anchored rule for only the generated output root when needed, creating `.gitignore` if absent. Verify exclusion with `git check-ignore`; never untrack files automatically. Outside Git, disclose that exclusion is unverified; workflows requiring Git retain that prerequisite. If safe storage or required exclusion fails, report the exact limitation before saving and use chat only when this workflow permits it.

Preserve existing state schemas, version identifiers, historical files, and resume paths; timestamp new run evidence beneath its existing owner without an implicit migration. Application source and project documents explicitly intended for version control retain their own contracts. This section does not authorize extra output for a chat-only request or expand the workflow's scope.
