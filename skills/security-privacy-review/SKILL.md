---
name: security-privacy-review
description: Review trust boundaries authorization and data handling for a scoped software change.
---

# Security Privacy Review

Input: Affected data flows, roles, storage, integrations and authoritative privacy requirements.

Output: Evidence-ranked security and privacy findings with reproduction, impact and narrow mitigation.

1. Map untrusted inputs, identities and permission checks through every changed entrypoint and stored side effect.

2. Inspect object ownership, role separation, injection, path containment, secret exposure and supply-chain boundaries relevant to scope.

3. Identify collected data, purpose, recipients, retention and deletion requirements. Ask the authorized owner about missing or conflicting policy.

4. Preserve historical attribution and explicit consent boundaries. Do not infer privacy policy from an unrelated classification field.

5. Prefer local fixtures and bounded authorized probes. Redact sensitive output and distinguish potential issues from reproduced findings.

Limits: Review does not authorize intrusive testing, production access or normative privacy decisions. Do not add speculative compliance requirements.
