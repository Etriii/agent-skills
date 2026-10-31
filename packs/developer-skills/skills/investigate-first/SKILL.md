---
name: investigate-first
description: Diagnose unclear or intermittent failures before proposing code changes using evidence and bounded reproduction.
---

# Investigate First

Input: An observed failure, its environment and any available reproduction, logs or affected paths.

Output: An evidence-backed cause or ranked remaining hypotheses, with the smallest discriminating next check.

1. Trace the failing entry point, state changes and ownership boundaries. Separate observed facts from inferred explanations; preserve the original error and relevant environment details.

2. Try the cheapest bounded reproduction. For each credible cause, seek counter-evidence or a check that distinguishes it from competing causes. An unrelated passing test does not disprove the reported failure.

3. Stop expanding the investigation once the evidence identifies a responsible mechanism or a concrete missing prerequisite. If reproduction remains unavailable, state uncertainty and the next useful check.

4. Report the cause, supporting and conflicting evidence, affected owner and proposed next action. Change code only if fixing it is already authorized.

Limits: Diagnosis does not authorize a fix, new infrastructure or an open-ended benchmark. Use the selected coordinator's existing scope and records when present.

## Generated artifacts

Apply this section only when the workflow saves generated reports, logs, previews, or run evidence. Use a stable skill-owned root in the target workspace, never the installed skill directory. Allocate each new run with an exclusively created `YYYYMMDDTHHMMSSZ-<unique-id>/` directory (UTC); preserve earlier runs and resume the identified active run. Reject linked paths, traversal, and unrelated same-name folders.

Before saving inside Git, resolve the intended repository root, refuse already tracked output, and inspect its `.gitignore`. Preserve existing bytes and line endings; append a root-anchored rule for only the generated output root when needed, creating `.gitignore` if absent. Verify exclusion with `git check-ignore`; never untrack files automatically. Outside Git, disclose that exclusion is unverified; workflows requiring Git retain that prerequisite. If safe storage or required exclusion fails, report the exact limitation before saving and use chat only when this workflow permits it.

Preserve existing state schemas, version identifiers, historical files, and resume paths; timestamp new run evidence beneath its existing owner without an implicit migration. Application source and project documents explicitly intended for version control retain their own contracts. This section does not authorize extra output for a chat-only request or expand the workflow's scope.
