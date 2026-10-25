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
