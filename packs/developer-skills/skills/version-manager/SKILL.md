---
name: version-manager
description: Plan and record a development-plan version transition while preserving prior accepted history.
---

# Version Manager

Input: Current and proposed plans, completion evidence and an explicit requested transition.

Output: A version mapping, carried-forward decisions requiring reuse or revalidation and a transition record.

1. Verify current version acceptance and integration. If incomplete, require an explicit exception and record the unfinished work without relabeling it complete.

2. Compare requirements and policy sources. Cite unchanged decisions as REUSE and changed assumptions as REVALIDATE.

3. Preview the new version identifier, copied references, mapping and affected files; obtain transition consent before writing.

4. Keep previous plans, decisions, handoffs and evidence immutable. Create the next version separately at the user's established location.

5. Validate references and report the exact resulting files and checks. Do not execute new-version phases as part of transition.

Limits: Use ordinary project documents; no private state required. Never silently migrate history or choose a new business or retention policy.

## Generated artifacts

Apply this section only when the workflow saves generated reports, logs, previews, or run evidence. Use a stable skill-owned root in the target workspace, never the installed skill directory. Allocate each new run with an exclusively created `YYYYMMDDTHHMMSSZ-<unique-id>/` directory (UTC); preserve earlier runs and resume the identified active run. Reject linked paths, traversal, and unrelated same-name folders.

Before saving inside Git, resolve the intended repository root, refuse already tracked output, and inspect its `.gitignore`. Preserve existing bytes and line endings; append a root-anchored rule for only the generated output root when needed, creating `.gitignore` if absent. Verify exclusion with `git check-ignore`; never untrack files automatically. Outside Git, disclose that exclusion is unverified; workflows requiring Git retain that prerequisite. If safe storage or required exclusion fails, report the exact limitation before saving and use chat only when this workflow permits it.

Preserve existing state schemas, version identifiers, historical files, and resume paths; timestamp new run evidence beneath its existing owner without an implicit migration. Application source and project documents explicitly intended for version control retain their own contracts. This section does not authorize extra output for a chat-only request or expand the workflow's scope.
