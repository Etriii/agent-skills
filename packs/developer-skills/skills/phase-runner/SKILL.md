---
name: phase-runner
description: Execute exactly one authorized ready development phase with checkpoints and evidence gates.
---

# Phase Runner

Input: A selected phase, repository instructions, dependency evidence and current approval scope.

Output: Only that phase's implementation, tests, checkpoints and truthful handoff.

1. Read repository rules and the selected phase's direct prerequisites. Verify source, tests, decisions and current Git state rather than assuming earlier execution.

2. Inspect existing behavior before editing. Require a clear scope, resolved blocking questions, applicable environment readiness, permissions, acceptance criteria and safe isolation.

3. Implement only missing selected-phase work at its responsible layer. Preserve unrelated staged, unstaged and custom files.

4. Checkpoint code milestones, test results and pre-integration state; after interruption verify HEAD and files before resuming.

5. Run applicable checks and report limitations. Merge, network downloads, protected operations and policy changes require their existing specific authorization.

6. Stop when the selected phase is tested and reported. If integration is pending, report MERGE_PENDING and stop.

Limits: No private CLI is required. Do not create an execution engine, auto-run a next phase or interpret a document checkbox as approval.

## Generated artifacts

Apply this section only when the workflow saves generated reports, logs, previews, or run evidence. Use a stable skill-owned root in the target workspace, never the installed skill directory. Allocate each new run with an exclusively created `YYYYMMDDTHHMMSSZ-<unique-id>/` directory (UTC); preserve earlier runs and resume the identified active run. Reject linked paths, traversal, and unrelated same-name folders.

Before saving inside Git, resolve the intended repository root, refuse already tracked output, and inspect its `.gitignore`. Preserve existing bytes and line endings; append a root-anchored rule for only the generated output root when needed, creating `.gitignore` if absent. Verify exclusion with `git check-ignore`; never untrack files automatically. Outside Git, disclose that exclusion is unverified; workflows requiring Git retain that prerequisite. If safe storage or required exclusion fails, report the exact limitation before saving and use chat only when this workflow permits it.

Preserve existing state schemas, version identifiers, historical files, and resume paths; timestamp new run evidence beneath its existing owner without an implicit migration. Application source and project documents explicitly intended for version control retain their own contracts. This section does not authorize extra output for a chat-only request or expand the workflow's scope.
