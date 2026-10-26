# Skill catalog

Every entry links to a human-facing README with installation, invocation and runtime prerequisites. Agent instructions remain in each skill's `SKILL.md`.

## Developer Skills

| Skill | Purpose |
|---|---|
| [architecture-review](packs/developer-skills/skills/architecture-review/README.md) | Review ownership, coupling and dependency direction across a proposed change. |
| [backend-review](packs/developer-skills/skills/backend-review/README.md) | Review validation, authorization, transactions and side effects across backend request paths. |
| [blocker-check](packs/developer-skills/skills/blocker-check/README.md) | Find requirement, policy, dependency and environment blockers before implementation. |
| [business-rules-review](packs/developer-skills/skills/business-rules-review/README.md) | Map workflow rules to authoritative policy, server enforcement and boundary cases. |
| [completion-check](packs/developer-skills/skills/completion-check/README.md) | Check acceptance criteria against executed evidence, configuration and integration state. |
| [critical-review](packs/developer-skills/skills/critical-review/README.md) | Challenge unsupported assumptions and complexity using concrete failure paths and simpler alternatives. |
| [database-review](packs/developer-skills/skills/database-review/README.md) | Review integrity, concurrency, migration ordering and recovery across database changes. |
| [delivery-readiness](packs/developer-skills/skills/delivery-readiness/README.md) | Check configuration, tested artifacts, rollout sequencing and recovery before delivery. |
| [environment-doctor](packs/developer-skills/skills/environment-doctor/README.md) | Inspect local tool availability, Git state and required services with read-only diagnostics. |
| [frontend-review](packs/developer-skills/skills/frontend-review/README.md) | Review UI state ownership, forms, accessibility and responsive behavior with explicit evidence limits. |
| [phase-handoff](packs/developer-skills/skills/phase-handoff/README.md) | Write a standalone Markdown handoff connecting scope, decisions, Git state and executed checks. |
| [phase-runner](packs/developer-skills/skills/phase-runner/README.md) | Execute one authorized ready phase with checkpoints, verification and a bounded handoff. |
| [plan-review](packs/developer-skills/skills/plan-review/README.md) | Review complete-plan coverage, dependencies and existing implementation before development. |
| [security-privacy-review](packs/developer-skills/skills/security-privacy-review/README.md) | Trace trust boundaries, permissions and data handling for a scoped change. |
| [version-manager](packs/developer-skills/skills/version-manager/README.md) | Plan and record a development-plan version transition while preserving accepted history. |

The Essential selection contains plan-review, blocker-check, phase-handoff and completion-check. See the [pack guide](packs/developer-skills/README.md) and [detailed catalog](packs/developer-skills/SKILL_CATALOG.md).

## Ultimate QA

| Skill | Purpose |
|---|---|
| [ultimate-qa](packs/ultimate-qa/skills/ultimate-qa/README.md) | Run a versioned initialize → audit → plan review of an existing application. |
| [ultimate-qa-accessibility](packs/ultimate-qa/skills/ultimate-qa-accessibility/README.md) | Audit critical pages with automated accessibility checks, keyboard journeys and assistive-technology evidence. |
| [ultimate-qa-api](packs/ultimate-qa/skills/ultimate-qa-api/README.md) | Test API contracts, authentication, idempotency, error handling and persisted effects. |
| [ultimate-qa-architecture](packs/ultimate-qa/skills/ultimate-qa-architecture/README.md) | Assess architecture ownership, coupling and maintainability through representative user journeys. |
| [ultimate-qa-browser](packs/ultimate-qa/skills/ultimate-qa-browser/README.md) | Exercise authorized application journeys, role boundaries and visual states in a browser. |
| [ultimate-qa-client](packs/ultimate-qa/skills/ultimate-qa-client/README.md) | Prepare optional client reports and approval checklists, preserving returned decisions. |
| [ultimate-qa-environment](packs/ultimate-qa/skills/ultimate-qa-environment/README.md) | Check an isolated QA environment in dependency order and identify precise runtime blockers. |
| [ultimate-qa-performance](packs/ultimate-qa/skills/ultimate-qa-performance/README.md) | Measure application latency, throughput, resource use and slow paths against a reproducible baseline. |
| [ultimate-qa-security](packs/ultimate-qa/skills/ultimate-qa-security/README.md) | Review role boundaries, data integrity, secrets and safe failure behavior with verified evidence. |

Core/client workflows need the persistent QA kit. The Python installer generates a kit pointer; the external CLI needs the [documented kit setup](docs/NPX_INSTALLATION.md#ultimate-qa-support-files). See the [pack guide](packs/ultimate-qa/README.md) and [QA automation](packs/ultimate-qa/13_SKILLS_AND_AUTOMATION.md).

Use `--bundle all` with Python for one selected pack, or a pack-specific source plus `--skill '*'` with the external CLI. Neither requires installing unrelated packs. Read [installation options](README.md) and [contribution guidance](CONTRIBUTING.md).
