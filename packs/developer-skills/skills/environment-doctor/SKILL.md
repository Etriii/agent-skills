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

## Generated artifacts

Apply this section only when the workflow saves generated reports, logs, previews, or run evidence. Use a stable skill-owned root in the target workspace, never the installed skill directory. Allocate each new run with an exclusively created `YYYYMMDDTHHMMSSZ-<unique-id>/` directory (UTC); preserve earlier runs and resume the identified active run. Reject linked paths, traversal, and unrelated same-name folders.

Before saving inside Git, resolve the intended repository root, refuse already tracked output, and inspect its `.gitignore`. Preserve existing bytes and line endings; append a root-anchored rule for only the generated output root when needed, creating `.gitignore` if absent. Verify exclusion with `git check-ignore`; never untrack files automatically. Outside Git, disclose that exclusion is unverified; workflows requiring Git retain that prerequisite. If safe storage or required exclusion fails, report the exact limitation before saving and use chat only when this workflow permits it.

Preserve existing state schemas, version identifiers, historical files, and resume paths; timestamp new run evidence beneath its existing owner without an implicit migration. Application source and project documents explicitly intended for version control retain their own contracts. This section does not authorize extra output for a chat-only request or expand the workflow's scope.
