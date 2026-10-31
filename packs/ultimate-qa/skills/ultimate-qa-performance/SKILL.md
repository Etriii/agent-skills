---
name: ultimate-qa-performance
description: Measure application latency, throughput, resource use, and slow data paths in a controlled QA environment.
---

# Ultimate QA Performance

Confirm a disposable test stack, representative seeded data, workload, and baseline before measuring. Use the project's existing benchmark or load tool when possible, preferably inside Docker. Warm the app consistently, measure multiple runs, and record latency distributions, error rate, throughput, CPU/memory, DB query count, and environment limits. Wait until the load run and service metrics collection finish before interpreting results.

Compare the same scenario and data volume across versions. Investigate slow paths with traces, query plans, and profiles before proposing a fix. Keep overload tests behind the kit's destructive-testing gate; avoid production and shared third-party services. A single slow response or a saturated laptop is a lead, not proof of a product regression. State confidence and reproducibility with each finding.

## Generated artifacts

Apply this section only when the workflow saves generated reports, logs, previews, or run evidence. Use a stable skill-owned root in the target workspace, never the installed skill directory. Allocate each new run with an exclusively created `YYYYMMDDTHHMMSSZ-<unique-id>/` directory (UTC); preserve earlier runs and resume the identified active run. Reject linked paths, traversal, and unrelated same-name folders.

Before saving inside Git, resolve the intended repository root, refuse already tracked output, and inspect its `.gitignore`. Preserve existing bytes and line endings; append a root-anchored rule for only the generated output root when needed, creating `.gitignore` if absent. Verify exclusion with `git check-ignore`; never untrack files automatically. Outside Git, disclose that exclusion is unverified; workflows requiring Git retain that prerequisite. If safe storage or required exclusion fails, report the exact limitation before saving and use chat only when this workflow permits it.

Preserve existing state schemas, version identifiers, historical files, and resume paths; timestamp new run evidence beneath its existing owner without an implicit migration. Application source and project documents explicitly intended for version control retain their own contracts. This section does not authorize extra output for a chat-only request or expand the workflow's scope.
