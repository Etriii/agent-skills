---
name: blocker-check
description: Find source-backed requirement and policy blockers before implementing a selected phase or feature.
---

# Blocker Check

Input: The selected scope, authoritative requirements, dependencies and existing evidence.

Output: Blockers and questions with severity, source, owner, mitigation, status and the smallest safe next action.

1. Check authority, requirements, dependency, business policy, privacy, security, authorization, migration, external integration, network, environment, Git, verification, manual review and production safety where relevant.

2. Separate hard blockers from advisory risks. An absent authoritative form or template blocks exact reproduction; do not invent one.

3. Ask eligibility, treatment of previously approved records and reminder behavior as separate policy questions. Do not collapse independent choices.

4. Give justified recommended-first options and allow a custom answer. Reuse still-applicable recorded decisions with provenance; changed policy requires revalidation.

5. Continue independent authorized work while awaiting a decision; stop dependent work. Record unavailable evidence explicitly.

Limits: Works from ordinary files without a runner or tracking directory. Do not decide normative policy or silently run missing prerequisite phases.

## Generated artifacts

Apply this section only when the workflow saves generated reports, logs, previews, or run evidence. Use a stable skill-owned root in the target workspace, never the installed skill directory. Allocate each new run with an exclusively created `YYYYMMDDTHHMMSSZ-<unique-id>/` directory (UTC); preserve earlier runs and resume the identified active run. Reject linked paths, traversal, and unrelated same-name folders.

Before saving inside Git, resolve the intended repository root, refuse already tracked output, and inspect its `.gitignore`. Preserve existing bytes and line endings; append a root-anchored rule for only the generated output root when needed, creating `.gitignore` if absent. Verify exclusion with `git check-ignore`; never untrack files automatically. Outside Git, disclose that exclusion is unverified; workflows requiring Git retain that prerequisite. If safe storage or required exclusion fails, report the exact limitation before saving and use chat only when this workflow permits it.

Preserve existing state schemas, version identifiers, historical files, and resume paths; timestamp new run evidence beneath its existing owner without an implicit migration. Application source and project documents explicitly intended for version control retain their own contracts. This section does not authorize extra output for a chat-only request or expand the workflow's scope.
