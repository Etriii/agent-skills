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
