---
name: phase-handoff
description: Write a bounded evidence-based phase handoff and checkpoint for another development session.
---

# Phase Handoff

Input: Selected phase scope, current Git state, changed files, decisions and executed checks.

Output: A standalone Markdown handoff with a 20-35-line digest and normally 100-300 meaningful lines.

1. Verify current repository roots, branch, HEAD and dirty state. Name the phase, status, author, observed time and agent version when known.

2. Map acceptance criteria to implementation and evidence. Record interfaces, configuration, file ownership and cross-repository integration separately.

3. List exact test commands, exit codes and source revisions; distinguish implementation, rendered output, manual acceptance and unavailable proof.

4. Include decisions with source and scope, blockers, risks, selected skills actually used or UNKNOWN, and minimal next-session reading.

5. Record checkpoints after milestones, tests and before risky actions. Resume by comparing the checkpoint with current HEAD/files before editing.

6. Separate tested work from merged work. End at the selected phase; recommend the next phase without executing it.

Limits: Use the user's report location or an ordinary Markdown file. No private state format is required. Do not pad a trivial handoff; explain any shorter length.

## Generated artifacts

Apply this section only when the workflow saves generated reports, logs, previews, or run evidence. Use a stable skill-owned root in the target workspace, never the installed skill directory. Allocate each new run with an exclusively created `YYYYMMDDTHHMMSSZ-<unique-id>/` directory (UTC); preserve earlier runs and resume the identified active run. Reject linked paths, traversal, and unrelated same-name folders.

Before saving inside Git, resolve the intended repository root, refuse already tracked output, and inspect its `.gitignore`. Preserve existing bytes and line endings; append a root-anchored rule for only the generated output root when needed, creating `.gitignore` if absent. Verify exclusion with `git check-ignore`; never untrack files automatically. Outside Git, disclose that exclusion is unverified; workflows requiring Git retain that prerequisite. If safe storage or required exclusion fails, report the exact limitation before saving and use chat only when this workflow permits it.

Preserve existing state schemas, version identifiers, historical files, and resume paths; timestamp new run evidence beneath its existing owner without an implicit migration. Application source and project documents explicitly intended for version control retain their own contracts. This section does not authorize extra output for a chat-only request or expand the workflow's scope.
