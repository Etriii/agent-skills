---
name: backend-review
description: Review API validation authorization state transitions and failure behavior for backend changes.
---

# Backend Review

Input: Affected endpoints, schemas, domain services, persistence and executed integration evidence.

Output: Source-backed API findings and focused regression cases including database effects.

1. Trace request parsing through validation, authorization, business rules, transaction boundaries and response serialization.

2. Check object-level permissions and trusted identity at every entrypoint, including jobs and alternate endpoints.

3. Inspect idempotency, retries, concurrency, timeouts and error translation where relevant; verify side effects occur only after required validation.

4. Compare public request and response contracts and migration compatibility. Distinguish fixture behavior from the installed database/provider.

5. Recommend tests for denied actions, invalid inputs and state changes, with exact expected persistence effects.

Limits: Planning advisor unless implementation is separately authorized. Do not alter business policy or use production data for review.

## Generated artifacts

Apply this section only when the workflow saves generated reports, logs, previews, or run evidence. Use a stable skill-owned root in the target workspace, never the installed skill directory. Allocate each new run with an exclusively created `YYYYMMDDTHHMMSSZ-<unique-id>/` directory (UTC); preserve earlier runs and resume the identified active run. Reject linked paths, traversal, and unrelated same-name folders.

Before saving inside Git, resolve the intended repository root, refuse already tracked output, and inspect its `.gitignore`. Preserve existing bytes and line endings; append a root-anchored rule for only the generated output root when needed, creating `.gitignore` if absent. Verify exclusion with `git check-ignore`; never untrack files automatically. Outside Git, disclose that exclusion is unverified; workflows requiring Git retain that prerequisite. If safe storage or required exclusion fails, report the exact limitation before saving and use chat only when this workflow permits it.

Preserve existing state schemas, version identifiers, historical files, and resume paths; timestamp new run evidence beneath its existing owner without an implicit migration. Application source and project documents explicitly intended for version control retain their own contracts. This section does not authorize extra output for a chat-only request or expand the workflow's scope.
