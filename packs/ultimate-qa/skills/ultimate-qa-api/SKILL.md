---
name: ultimate-qa-api
description: Test API contracts, authentication, error behavior, idempotency, and database effects with repeatable integration checks.
---

# Ultimate QA API

Discover the project's OpenAPI/schema, route definitions, existing API tests, and fixture setup. Run checks in its documented test container with a disposable database. Exercise representative success and failure cases for each critical resource: required fields, type and boundary validation, auth and role denial, cross-tenant IDs, pagination, filtering, duplicate submission, and retry behavior.

Compare requests and responses with the documented contract. For writes, verify persisted side effects and rollback on failed requests; for async APIs, wait for job completion or a documented timeout. Avoid treating HTTP 200 alone as a pass. Capture request shape with secrets redacted, response status/body excerpt, role, database observation, and command/test output.

Report schema drift, behavior defects, and missing contract coverage separately. Add focused regression tests in the project's existing test framework when code changes are authorized. Do not invent endpoints or claim provider behavior from mocks.

## Generated artifacts

Apply this section only when the workflow saves generated reports, logs, previews, or run evidence. Use a stable skill-owned root in the target workspace, never the installed skill directory. Allocate each new run with an exclusively created `YYYYMMDDTHHMMSSZ-<unique-id>/` directory (UTC); preserve earlier runs and resume the identified active run. Reject linked paths, traversal, and unrelated same-name folders.

Before saving inside Git, resolve the intended repository root, refuse already tracked output, and inspect its `.gitignore`. Preserve existing bytes and line endings; append a root-anchored rule for only the generated output root when needed, creating `.gitignore` if absent. Verify exclusion with `git check-ignore`; never untrack files automatically. Outside Git, disclose that exclusion is unverified; workflows requiring Git retain that prerequisite. If safe storage or required exclusion fails, report the exact limitation before saving and use chat only when this workflow permits it.

Preserve existing state schemas, version identifiers, historical files, and resume paths; timestamp new run evidence beneath its existing owner without an implicit migration. Application source and project documents explicitly intended for version control retain their own contracts. This section does not authorize extra output for a chat-only request or expand the workflow's scope.
