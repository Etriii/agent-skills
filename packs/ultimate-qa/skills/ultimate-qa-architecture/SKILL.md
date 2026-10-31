---
name: ultimate-qa-architecture
description: Assess code architecture, ownership, coupling, maintainability, and change risk during a QA review. Use for clean architecture or code quality analysis.
---

# Ultimate QA Architecture

Read `references/checks.md` for the review dimensions and evidence scale. Inspect the project architecture, then trace representative user journeys from UI/API through domain logic to persistence. Use project-native tests, static analysis, import graphs, and churn/history where available. Report concrete path:line examples and the effect on a real change or defect.

Distinguish confirmed defects from maintainability risks. A large file alone is not proof of poor architecture. Score each dimension 0–3 only when the evidence supports it; leave unassessed dimensions blank. Give a short repair sequence ordered by risk and dependency, and link architecture findings to functional findings when the same root cause appears. Avoid prescribing a framework or layer pattern where simpler ownership fits.

## Generated artifacts

Apply this section only when the workflow saves generated reports, logs, previews, or run evidence. Use a stable skill-owned root in the target workspace, never the installed skill directory. Allocate each new run with an exclusively created `YYYYMMDDTHHMMSSZ-<unique-id>/` directory (UTC); preserve earlier runs and resume the identified active run. Reject linked paths, traversal, and unrelated same-name folders.

Before saving inside Git, resolve the intended repository root, refuse already tracked output, and inspect its `.gitignore`. Preserve existing bytes and line endings; append a root-anchored rule for only the generated output root when needed, creating `.gitignore` if absent. Verify exclusion with `git check-ignore`; never untrack files automatically. Outside Git, disclose that exclusion is unverified; workflows requiring Git retain that prerequisite. If safe storage or required exclusion fails, report the exact limitation before saving and use chat only when this workflow permits it.

Preserve existing state schemas, version identifiers, historical files, and resume paths; timestamp new run evidence beneath its existing owner without an implicit migration. Application source and project documents explicitly intended for version control retain their own contracts. This section does not authorize extra output for a chat-only request or expand the workflow's scope.
