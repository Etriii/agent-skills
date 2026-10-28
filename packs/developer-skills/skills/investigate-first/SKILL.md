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
