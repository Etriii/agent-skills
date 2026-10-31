---
name: business-rules-review
description: Review eligibility approval and lifecycle rules against authoritative business decisions.
---

# Business Rules Review

Input: A scoped workflow, policy sources, state model and example records.

Output: A rule/source matrix, independent policy questions and boundary-case acceptance examples.

1. Trace actors, eligibility, approval authority and allowed state transitions, including denied and reversed actions.

2. Preserve distinctions between signing, approving and assigning when the workflow treats them separately.

3. Review existing approved records, amendments, cancellations, refunds and reminders independently when applicable.

4. Identify ambiguous rules with concrete counterexamples. Ask separate questions for independent choices, with recommendations and a custom-answer path.

5. Map each agreed rule to server enforcement and a testable outcome; preserve historical attribution and grouped entities.

Limits: Advisor by default. Do not choose policy from convenience, UI wording or an unrelated data field.

## Generated artifacts

Apply this section only when the workflow saves generated reports, logs, previews, or run evidence. Use a stable skill-owned root in the target workspace, never the installed skill directory. Allocate each new run with an exclusively created `YYYYMMDDTHHMMSSZ-<unique-id>/` directory (UTC); preserve earlier runs and resume the identified active run. Reject linked paths, traversal, and unrelated same-name folders.

Before saving inside Git, resolve the intended repository root, refuse already tracked output, and inspect its `.gitignore`. Preserve existing bytes and line endings; append a root-anchored rule for only the generated output root when needed, creating `.gitignore` if absent. Verify exclusion with `git check-ignore`; never untrack files automatically. Outside Git, disclose that exclusion is unverified; workflows requiring Git retain that prerequisite. If safe storage or required exclusion fails, report the exact limitation before saving and use chat only when this workflow permits it.

Preserve existing state schemas, version identifiers, historical files, and resume paths; timestamp new run evidence beneath its existing owner without an implicit migration. Application source and project documents explicitly intended for version control retain their own contracts. This section does not authorize extra output for a chat-only request or expand the workflow's scope.
