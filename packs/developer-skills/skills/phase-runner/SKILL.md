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
