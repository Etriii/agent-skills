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
