---
name: ultimate-qa-environment
description: Check and prepare an isolated Docker-based application environment for QA, including Compose services and databases. Use before runtime QA or when environment setup fails.
---

# Ultimate QA Environment

Run `python <kit>/tools/qa_preflight.py --project <root> --out <project>/qa-findings/vN/recommendations/evidence/preflight.json` when the kit is available. Inspect the project's own Compose files, Dockerfiles, environment examples, migrations, test scripts, health checks, and service dependencies. Do not print secret values. Use a disposable database and test accounts; identify production connections before running writes.

Check Docker CLI, daemon, Compose, configuration validity, service status, DB readiness, and the app health endpoint in that order. A service listed as starting is pending: wait for health or process exit before classifying it. Choose timeouts from the project's documented startup behavior; record timeout as inconclusive. Start services with the project's documented Compose command when authorized and safe. Keep database fixtures isolated and resettable. Use explicit Compose project names to avoid collisions.

Run application checks inside containers when the project provides that workflow. If Docker is unavailable, record the precise blocker and use safe source checks; do not report application failure. Do not build a new Docker stack into the reviewed project solely for an audit without a scoped change request. Never point destructive tests at production or third-party live services.
