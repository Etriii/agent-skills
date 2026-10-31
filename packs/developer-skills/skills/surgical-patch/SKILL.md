---
name: surgical-patch
description: Fix a specific defect or small behavior change with focused regression evidence at the responsible layer.
---

# Surgical Patch

Input: A specific defect or small behavior change, affected behavior and authorized scope.

Output: A root-cause correction with focused regression evidence and preserved surrounding behavior.

1. Reproduce the failure when practical; otherwise record the strongest available evidence and the limits of that evidence. Trace the incorrect behavior to the layer that owns its invariant.

2. Check whether an existing guard, type or helper already owns the rule. Correct that owner rather than scattering duplicate checks across callers.

3. Make the smallest coherent correction. Preserve unrelated changes, error behavior and public contracts; widen the edit only when required to fix the responsible mechanism.

4. Use an existing regression check or add a focused case that distinguishes the old failure from correct behavior. Run the nearest affected gate and report any unrelated failures separately.

Limits: Stop after the scoped defect and required checks are resolved. Do not include unrelated cleanup or let the helper expand a coordinator's authorized scope.

## Generated artifacts

Apply this section only when the workflow saves generated reports, logs, previews, or run evidence. Use a stable skill-owned root in the target workspace, never the installed skill directory. Allocate each new run with an exclusively created `YYYYMMDDTHHMMSSZ-<unique-id>/` directory (UTC); preserve earlier runs and resume the identified active run. Reject linked paths, traversal, and unrelated same-name folders.

Before saving inside Git, resolve the intended repository root, refuse already tracked output, and inspect its `.gitignore`. Preserve existing bytes and line endings; append a root-anchored rule for only the generated output root when needed, creating `.gitignore` if absent. Verify exclusion with `git check-ignore`; never untrack files automatically. Outside Git, disclose that exclusion is unverified; workflows requiring Git retain that prerequisite. If safe storage or required exclusion fails, report the exact limitation before saving and use chat only when this workflow permits it.

Preserve existing state schemas, version identifiers, historical files, and resume paths; timestamp new run evidence beneath its existing owner without an implicit migration. Application source and project documents explicitly intended for version control retain their own contracts. This section does not authorize extra output for a chat-only request or expand the workflow's scope.
