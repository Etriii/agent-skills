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

## Generated artifacts

Apply this section only when the workflow saves generated reports, logs, previews, or run evidence. Use a stable skill-owned root in the target workspace, never the installed skill directory. Allocate each new run with an exclusively created `YYYYMMDDTHHMMSSZ-<unique-id>/` directory (UTC); preserve earlier runs and resume the identified active run. Reject linked paths, traversal, and unrelated same-name folders.

Before saving inside Git, resolve the intended repository root, refuse already tracked output, and inspect its `.gitignore`. Preserve existing bytes and line endings; append a root-anchored rule for only the generated output root when needed, creating `.gitignore` if absent. Verify exclusion with `git check-ignore`; never untrack files automatically. Outside Git, disclose that exclusion is unverified; workflows requiring Git retain that prerequisite. If safe storage or required exclusion fails, report the exact limitation before saving and use chat only when this workflow permits it.

Preserve existing state schemas, version identifiers, historical files, and resume paths; timestamp new run evidence beneath its existing owner without an implicit migration. Application source and project documents explicitly intended for version control retain their own contracts. This section does not authorize extra output for a chat-only request or expand the workflow's scope.
