---
name: delivery-readiness
description: Review delivery gates environment setup rollout and recovery using actual executed evidence.
---

# Delivery Readiness

Input: Release scope, configuration, CI results, environment requirements and deployment/recovery plans.

Output: A delivery gate report with pass, fail, unavailable and blocked results and responsible owners.

1. Verify declared dependencies, runtime versions, configuration examples, migrations and feature visibility prerequisites.

2. Compare the tested revision with the delivery artifact; inspect CI and required reviews when available without assuming a hosting policy.

3. Check rollout sequencing, compatibility, rollback and backup/restore evidence proportional to the change.

4. Separate unit, integration, browser, installed environment, provider, device and manual acceptance proof.

5. Record remaining approvals and material risks. Report MERGE_PENDING when required integration remains open and stop at the requested boundary.

Limits: Review does not authorize deployment, publication, remote writes or bypassing required checks. No release-readiness claim from fixtures alone.

## Generated artifacts

Apply this section only when the workflow saves generated reports, logs, previews, or run evidence. Use a stable skill-owned root in the target workspace, never the installed skill directory. Allocate each new run with an exclusively created `YYYYMMDDTHHMMSSZ-<unique-id>/` directory (UTC); preserve earlier runs and resume the identified active run. Reject linked paths, traversal, and unrelated same-name folders.

Before saving inside Git, resolve the intended repository root, refuse already tracked output, and inspect its `.gitignore`. Preserve existing bytes and line endings; append a root-anchored rule for only the generated output root when needed, creating `.gitignore` if absent. Verify exclusion with `git check-ignore`; never untrack files automatically. Outside Git, disclose that exclusion is unverified; workflows requiring Git retain that prerequisite. If safe storage or required exclusion fails, report the exact limitation before saving and use chat only when this workflow permits it.

Preserve existing state schemas, version identifiers, historical files, and resume paths; timestamp new run evidence beneath its existing owner without an implicit migration. Application source and project documents explicitly intended for version control retain their own contracts. This section does not authorize extra output for a chat-only request or expand the workflow's scope.
