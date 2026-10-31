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

## Generated artifacts

Apply this section only when the workflow saves generated reports, logs, previews, or run evidence. Use a stable skill-owned root in the target workspace, never the installed skill directory. Allocate each new run with an exclusively created `YYYYMMDDTHHMMSSZ-<unique-id>/` directory (UTC); preserve earlier runs and resume the identified active run. Reject linked paths, traversal, and unrelated same-name folders.

Before saving inside Git, resolve the intended repository root, refuse already tracked output, and inspect its `.gitignore`. Preserve existing bytes and line endings; append a root-anchored rule for only the generated output root when needed, creating `.gitignore` if absent. Verify exclusion with `git check-ignore`; never untrack files automatically. Outside Git, disclose that exclusion is unverified; workflows requiring Git retain that prerequisite. If safe storage or required exclusion fails, report the exact limitation before saving and use chat only when this workflow permits it.

Preserve existing state schemas, version identifiers, historical files, and resume paths; timestamp new run evidence beneath its existing owner without an implicit migration. Application source and project documents explicitly intended for version control retain their own contracts. This section does not authorize extra output for a chat-only request or expand the workflow's scope.
