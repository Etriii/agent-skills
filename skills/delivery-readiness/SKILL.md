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
