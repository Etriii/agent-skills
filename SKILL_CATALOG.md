# Skill catalog

Browse available skills by their primary purpose. Each skill appears once and links to its own README with installation, invocation and prerequisites. The install pack identifies its source; categories do not change skill paths or installation commands. Agent instructions remain in each skill's `SKILL.md`.

This is the authoritative category directory. Follow the [categorization rules](CONTRIBUTING.md#categorize-a-skill) when adding a skill or category.

Use the [workflow guide](docs/SKILL_WORKFLOWS.md) to choose when to use a skill. A category is a browsing aid, not an execution order or an automatic routing rule.

## Planning and decisions

Clarify scope and policy, inspect dependencies and preserve plan decisions before development.

| Skill | Purpose | Install pack |
|---|---|---|
| [blocker-check](packs/developer-skills/skills/blocker-check/README.md) | Find requirement, policy, dependency and environment blockers before implementation. | `developer-skills` |
| [plan-review](packs/developer-skills/skills/plan-review/README.md) | Review complete-plan coverage, dependencies and existing implementation before development. | `developer-skills` |
| [prompt-intake](packs/developer-skills/skills/prompt-intake/README.md) | Clarify a task with recommended choices, custom answers, versioned question files and next-action hints. | `developer-skills` |
| [version-manager](packs/developer-skills/skills/version-manager/README.md) | Plan and record a development-plan version transition while preserving accepted history. | `developer-skills` |

## Critique and evaluation

Challenge assumptions and assess the soundness, feasibility and complexity of proposed or completed work.

| Skill | Purpose | Install pack |
|---|---|---|
| [critical-review](packs/developer-skills/skills/critical-review/README.md) | Challenge unsupported assumptions and complexity using concrete failure paths and simpler alternatives. | `developer-skills` |
| [deep-critique](packs/developer-skills/skills/deep-critique/README.md) | Full generic critique and ratings with combined modes and categorized reports that preserve earlier runs. | `developer-skills` |

## Engineering reviews

Inspect design and implementation at the responsible technical or business boundary.

| Skill | Purpose | Install pack |
|---|---|---|
| [architecture-review](packs/developer-skills/skills/architecture-review/README.md) | Review ownership, coupling and dependency direction across a proposed change. | `developer-skills` |
| [backend-review](packs/developer-skills/skills/backend-review/README.md) | Review validation, authorization, transactions and side effects across backend request paths. | `developer-skills` |
| [business-rules-review](packs/developer-skills/skills/business-rules-review/README.md) | Map workflow rules to authoritative policy, server enforcement and boundary cases. | `developer-skills` |
| [database-review](packs/developer-skills/skills/database-review/README.md) | Review integrity, concurrency, migration ordering and recovery across database changes. | `developer-skills` |
| [frontend-review](packs/developer-skills/skills/frontend-review/README.md) | Review UI state ownership, forms, accessibility and responsive behavior with explicit evidence limits. | `developer-skills` |
| [security-privacy-review](packs/developer-skills/skills/security-privacy-review/README.md) | Trace trust boundaries, permissions and data handling for a scoped change. | `developer-skills` |

## Implementation and change safety

Choose a helper for the authorized type of work. These skills work independently and remain optional alongside a coordinator; they do not add a scheduler or automatic advisor-selection rule.

| Skill | Purpose | Install pack |
|---|---|---|
| [investigate-first](packs/developer-skills/skills/investigate-first/README.md) | Diagnose unclear failures using reproduction and competing evidence before proposing edits. | `developer-skills` |
| [lean-build](packs/developer-skills/skills/lean-build/README.md) | Implement a bounded feature through existing owners with focused verification. | `developer-skills` |
| [migration](packs/developer-skills/skills/migration/README.md) | Make compatibility-sensitive transitions with preservation and recovery evidence. | `developer-skills` |
| [report-creator](packs/developer-skills/skills/report-creator/README.md) | Discover reporting needs and implement scoped reports with styled PDF and Excel exports and retained generated files. | `developer-skills` |
| [safe-refactor](packs/developer-skills/skills/safe-refactor/README.md) | Change structure while preserving defined behavior and public contracts. | `developer-skills` |
| [surgical-patch](packs/developer-skills/skills/surgical-patch/README.md) | Correct a specific defect at its responsible owner with regression proof. | `developer-skills` |
| [verify-and-stop](packs/developer-skills/skills/verify-and-stop/README.md) | Verify existing work against acceptance without adding implementation scope. | `developer-skills` |

## Execution and handoff

Carry out bounded, authorized implementation and record enough context for the next session.

| Skill | Purpose | Install pack |
|---|---|---|
| [phase-handoff](packs/developer-skills/skills/phase-handoff/README.md) | Write a standalone Markdown handoff connecting scope, decisions, Git state and executed checks. | `developer-skills` |
| [phase-runner](packs/developer-skills/skills/phase-runner/README.md) | Execute one authorized ready phase with checkpoints, verification and a bounded handoff. | `developer-skills` |

## Verification and readiness

Check completion evidence, local prerequisites and delivery conditions.

| Skill | Purpose | Install pack |
|---|---|---|
| [completion-check](packs/developer-skills/skills/completion-check/README.md) | Check acceptance criteria against executed evidence, configuration and integration state. | `developer-skills` |
| [delivery-readiness](packs/developer-skills/skills/delivery-readiness/README.md) | Check configuration, tested artifacts, rollout sequencing and recovery before delivery. | `developer-skills` |
| [environment-doctor](packs/developer-skills/skills/environment-doctor/README.md) | Inspect local tool availability, Git state and required services with read-only diagnostics. | `developer-skills` |

## QA workflows

Run a structured application audit or a specialist check within the Ultimate QA workflow.

| Skill | Purpose | Install pack |
|---|---|---|
| [ultimate-qa](packs/ultimate-qa/skills/ultimate-qa/README.md) | Run a versioned initialize, audit and plan review of an existing application. | `ultimate-qa` |
| [ultimate-qa-accessibility](packs/ultimate-qa/skills/ultimate-qa-accessibility/README.md) | Audit critical pages with automated accessibility checks, keyboard journeys and assistive-technology evidence. | `ultimate-qa` |
| [ultimate-qa-api](packs/ultimate-qa/skills/ultimate-qa-api/README.md) | Test API contracts, authentication, idempotency, error handling and persisted effects. | `ultimate-qa` |
| [ultimate-qa-architecture](packs/ultimate-qa/skills/ultimate-qa-architecture/README.md) | Assess architecture ownership, coupling and maintainability through representative user journeys. | `ultimate-qa` |
| [ultimate-qa-browser](packs/ultimate-qa/skills/ultimate-qa-browser/README.md) | Exercise authorized application journeys, role boundaries and visual states in a browser. | `ultimate-qa` |
| [ultimate-qa-client](packs/ultimate-qa/skills/ultimate-qa-client/README.md) | Prepare optional client reports and approval checklists, preserving returned decisions. | `ultimate-qa` |
| [ultimate-qa-environment](packs/ultimate-qa/skills/ultimate-qa-environment/README.md) | Check an isolated QA environment in dependency order and identify precise runtime blockers. | `ultimate-qa` |
| [ultimate-qa-performance](packs/ultimate-qa/skills/ultimate-qa-performance/README.md) | Measure application latency, throughput, resource use and slow paths against a reproducible baseline. | `ultimate-qa` |
| [ultimate-qa-security](packs/ultimate-qa/skills/ultimate-qa-security/README.md) | Review role boundaries, data integrity, secrets and safe failure behavior with verified evidence. | `ultimate-qa` |

Core/client workflows need the persistent QA kit. The Python installer generates a kit pointer; the external CLI needs the [documented kit setup](docs/NPX_INSTALLATION.md#ultimate-qa-support-files).

## Install by pack

For installation options and pack-specific guidance, see [Developer Skills](packs/developer-skills/README.md), its [detailed catalog](packs/developer-skills/SKILL_CATALOG.md), or [Ultimate QA](packs/ultimate-qa/README.md) and its [automation guide](packs/ultimate-qa/13_SKILLS_AND_AUTOMATION.md).

The Developer Skills Essential selection contains plan-review, blocker-check, phase-handoff and completion-check. Categories do not define installable bundles.

Use `--bundle all` with Python for one selected pack, or a pack-specific source plus `--skill '*'` with the external CLI. Neither requires installing unrelated packs. Read [installation options](README.md) and [contribution guidance](CONTRIBUTING.md).
