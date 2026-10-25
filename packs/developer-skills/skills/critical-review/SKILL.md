---
name: critical-review
description: Challenge a proposed technical plan for unsupported assumptions unnecessary complexity and missed failure modes.
---

# Critical Review

Input: A specific plan or diff, acceptance criteria and raw repository evidence.

Output: A short ranked set of substantiated challenges with simpler alternatives and verification needs.

1. Identify the highest-impact assumptions about ownership, user intent, policy, compatibility and prerequisite completion.

2. Trace concrete failure paths and counterexamples before alleging a defect. Cite source locations and separate facts from hypotheses.

3. Ask whether existing behavior, a responsible helper or native capability already satisfies the requirement.

4. Compare the total maintenance and migration cost of alternatives. Avoid speculative extension points and requirements absent from scope.

5. State what evidence would resolve each challenge. If none is substantiated, say so rather than manufacturing findings.

Limits: Planning advisor. Do not implement, expand scope or turn stylistic preference into a blocker.
