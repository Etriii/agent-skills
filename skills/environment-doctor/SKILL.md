---
name: environment-doctor
description: Diagnose local workspace Git and Docker prerequisites with deterministic read-only commands.
---

# Environment Doctor

Input: An explicit workspace path and its documented required tools and services.

Output: Tool availability, Git/worktree state, required Docker health and actionable diagnostics with exit codes.

1. Use local filesystem inspection and installed command-line tools only. Suggested commands are git status --short, git rev-parse --show-toplevel, git worktree list and tool version queries.

2. Only inspect Docker when the project requires it. Use docker version, docker compose version and docker compose ps from the declared project; report missing or unhealthy components.

3. Inspect declared configuration names and file presence without printing secret values. Check writable scope without creating probe files.

4. Record command output and deterministic pass/fail/unknown results. Distinguish unavailable tooling from an unhealthy application.

5. Keep doctor read-only and make no LLM API or network request, install, container start, build or Git repair.

Limits: The agent interpreting this skill is not a deterministic executable. Only the suggested local diagnostics are deterministic; no bundled automation or runtime skill integrity engine is claimed.
