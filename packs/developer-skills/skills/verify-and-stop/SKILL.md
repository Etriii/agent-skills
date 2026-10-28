---
name: verify-and-stop
description: Verify existing work against acceptance conditions without adding implementation scope or treating unknown evidence as a pass.
---

# Verify and Stop

Input: Existing work, acceptance conditions, relevant source state and available checks.

Output: A supported result for each condition with commands, outcomes and unresolved proof gaps.

1. Map each acceptance condition to observable evidence. Reuse prior results only when their source, relevant inputs and environment still match; recorded completion alone is not proof.

2. Run the smallest sufficient checks, starting with the affected behavior. Broaden testing only for required gates, failures or unresolved concerns.

3. Distinguish passed, failed, unavailable and blocked conditions. Keep local tests separate from browser, hosted CI, provider, device or production evidence when those are required.

4. Report what was checked and what remains. If a check fails, name the responsible issue and next action; fix it only if the current authorization includes fixes.

5. Stop when the requested verification is complete. Do not add polish, refactors or speculative tests.

Limits: This helper does not grant implementation, integration or deployment permission. A coordinator's completion and acceptance records remain authoritative.
