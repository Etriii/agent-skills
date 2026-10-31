---
name: ultimate-qa-environment
description: Check and prepare an isolated Docker-based application environment for QA, including Compose services and databases. Use before runtime QA or when environment setup fails.
---

# Ultimate QA Environment

Run `python <kit>/tools/qa_preflight.py --project <root>` when the kit is available. Before QA initialization, keep the result in command output so preflight does not create an unowned `qa-findings/` folder. After initialization and verified exclusion, exclusively reserve `qa-findings/vN/recommendations/evidence/YYYYMMDDTHHMMSSZ-<unique-id>/` and add `--out "<reserved-run>/preflight.json"` to save a new check. Replace `vN` with the active QA version and use the actual reserved path; never overwrite an earlier preflight result. Inspect the project's own Compose files, Dockerfiles, environment examples, migrations, test scripts, health checks, and service dependencies. Do not print secret values. Use a disposable database and test accounts; identify production connections before running writes.

Check Docker CLI, daemon, Compose, configuration validity, service status, DB readiness, and the app health endpoint in that order. A service listed as starting is pending: wait for health or process exit before classifying it. Choose timeouts from the project's documented startup behavior; record timeout as inconclusive. Start services with the project's documented Compose command when authorized and safe. Keep database fixtures isolated and resettable. Use explicit Compose project names to avoid collisions.

Run application checks inside containers when the project provides that workflow. If Docker is unavailable, record the precise blocker and use safe source checks; do not report application failure. Do not build a new Docker stack into the reviewed project solely for an audit without a scoped change request. Never point destructive tests at production or third-party live services.

## Generated artifacts

Apply this section only when the workflow saves generated reports, logs, previews, or run evidence. Use a stable skill-owned root in the target workspace, never the installed skill directory. Allocate each new run with an exclusively created `YYYYMMDDTHHMMSSZ-<unique-id>/` directory (UTC); preserve earlier runs and resume the identified active run. Reject linked paths, traversal, and unrelated same-name folders.

Before saving inside Git, resolve the intended repository root, refuse already tracked output, and inspect its `.gitignore`. Preserve existing bytes and line endings; append a root-anchored rule for only the generated output root when needed, creating `.gitignore` if absent. Verify exclusion with `git check-ignore`; never untrack files automatically. Outside Git, disclose that exclusion is unverified; workflows requiring Git retain that prerequisite. If safe storage or required exclusion fails, report the exact limitation before saving and use chat only when this workflow permits it.

Preserve existing state schemas, version identifiers, historical files, and resume paths; timestamp new run evidence beneath its existing owner without an implicit migration. Application source and project documents explicitly intended for version control retain their own contracts. This section does not authorize extra output for a chat-only request or expand the workflow's scope.
