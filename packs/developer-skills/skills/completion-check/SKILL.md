---
name: completion-check
description: Verify selected acceptance criteria and integration evidence before declaring development work complete.
---

# Completion Check

Input: Acceptance criteria, relevant source revisions, test records and repository integration requirements.

Output: A criterion-by-criterion result marked pass, fail, unavailable or blocked with remaining work.

1. Trace each acceptance condition to observable behavior and the smallest sufficient check. Reuse evidence only when source and inputs still match.

2. Check required packages, environment examples, migrations, feature flags and runtime setup before calling a feature functional.

3. Run focused checks before broader gates. Capture exact commands, exits and revision; do not convert a fixture into installed-system evidence.

4. Verify each touched repository's branch and integration status. Use MERGE_PENDING for tested work awaiting required integration.

5. Keep manual visual, hardware, provider, production and hosting checks explicit when required. Stop after the requested verification.

Limits: Verification does not authorize product edits, merges or deployment. Report unknowns without inventing passing tests or approvals.

## Generated artifacts

Apply this section only when the workflow saves generated reports, logs, previews, or run evidence. Use a stable skill-owned root in the target workspace, never the installed skill directory. Allocate each new run with an exclusively created `YYYYMMDDTHHMMSSZ-<unique-id>/` directory (UTC); preserve earlier runs and resume the identified active run. Reject linked paths, traversal, and unrelated same-name folders.

Before saving inside Git, resolve the intended repository root, refuse already tracked output, and inspect its `.gitignore`. Preserve existing bytes and line endings; append a root-anchored rule for only the generated output root when needed, creating `.gitignore` if absent. Verify exclusion with `git check-ignore`; never untrack files automatically. Outside Git, disclose that exclusion is unverified; workflows requiring Git retain that prerequisite. If safe storage or required exclusion fails, report the exact limitation before saving and use chat only when this workflow permits it.

Preserve existing state schemas, version identifiers, historical files, and resume paths; timestamp new run evidence beneath its existing owner without an implicit migration. Application source and project documents explicitly intended for version control retain their own contracts. This section does not authorize extra output for a chat-only request or expand the workflow's scope.
