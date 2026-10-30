# Standalone catalog

Version 0.1.0; each stable skill ID equals its generic directory/frontmatter name. Each row links to actual independent instructions. Installation does not execute a skill or prove it was used.

| Skill | Responsibility | Default mode |
|---|---|---|
| [plan-review](skills/plan-review/README.md) | Whole-plan coverage and dependencies | Planning |
| [blocker-check](skills/blocker-check/README.md) | Evidence-linked blockers and independent policy questions | Planning |
| [phase-handoff](skills/phase-handoff/README.md) | Bounded Markdown handoff and checkpoint | Execution aid |
| [completion-check](skills/completion-check/README.md) | Acceptance and integration evidence | Verification |
| [environment-doctor](skills/environment-doctor/README.md) | Read-only deterministic local diagnostics | Diagnostics guidance |
| [phase-runner](skills/phase-runner/README.md) | Exactly one authorized phase | Execution aid |
| [version-manager](skills/version-manager/README.md) | Preserved plan-version transition | Versioning |
| [architecture-review](skills/architecture-review/README.md) | Boundaries, ownership and tradeoffs | Planning advisor |
| [frontend-review](skills/frontend-review/README.md) | UI states, accessibility and visual evidence | Planning advisor |
| [table-ux-review](skills/table-ux-review/README.md) | Table inventory, detail navigation and role-aware row-action placement | Review |
| [ultimate-ui-ux](skills/ultimate-ui-ux/README.md) | Combined interface audit, before/after previews and scoped improvements | Gated review; explicit auto mode |
| [ultimate-ui](skills/ultimate-ui/README.md) | Visual hierarchy, layout, typography and responsive review | UI-only gated review |
| [ultimate-ux](skills/ultimate-ux/README.md) | Navigation, content grouping, task flows and interaction review | UX-only gated review |
| [ultimate-mobile](skills/ultimate-mobile/README.md) | Mobile web layout, headers, filters, dialogs and journeys | Mobile UI/UX gated review |
| [backend-review](skills/backend-review/README.md) | API contracts, authorization and side effects | Planning advisor |
| [database-review](skills/database-review/README.md) | Integrity, migration and recovery | Planning advisor |
| [security-privacy-review](skills/security-privacy-review/README.md) | Trust boundaries and data policy | Planning advisor |
| [business-rules-review](skills/business-rules-review/README.md) | Eligibility, authority and transitions | Planning advisor |
| [delivery-readiness](skills/delivery-readiness/README.md) | Configuration, rollout and delivery evidence | Planning advisor |
| [critical-review](skills/critical-review/README.md) | Substantiated challenges and simpler alternatives | Planning advisor |
| [deep-critique](skills/deep-critique/README.md) | Generic assessment with ratings, combined modes and categorized immutable reports | Full critique |
| [prompt-intake](skills/prompt-intake/README.md) | Prompt analysis with recommended choices, versioned question files, continuation and next-action hints | Intake before execution |
| [investigate-first](skills/investigate-first/README.md) | Evidence-led diagnosis before code changes | Task helper |
| [lean-build](skills/lean-build/README.md) | Bounded feature implementation through existing owners | Task helper |
| [report-creator](skills/report-creator/README.md) | Reporting discovery, styled exports, scoped access and retained files | Read-only scan |
| [surgical-patch](skills/surgical-patch/README.md) | Root-cause correction and focused regression proof | Task helper |
| [safe-refactor](skills/safe-refactor/README.md) | Structural change with behavior-preservation proof | Task helper |
| [migration](skills/migration/README.md) | Compatibility-sensitive transition and recovery | Task helper |
| [verify-and-stop](skills/verify-and-stop/README.md) | Acceptance verification without implementation expansion | Task helper |

Essential contains the first four only. The library has no default background loading, invocation telemetry or private runtime requirement. `environment-doctor` provides deterministic command guidance; it does not ship a diagnostics engine. Execution aids are agent instructions, not command runners.

Metadata records provenance, capabilities, version and undecided license status for local material. The four UI/UX skills declare `local-with-third-party` provenance and bundle source notices/licenses. Before the later additions, isolated native protocol checks discovered the then-shipping 23 skills in Codex CLI 0.165.0 and Claude Code 2.1.299, including the six optional implementation helpers. Those skills' compatible_agents metadata records both agents; report-creator, table-ux-review and the UI/UX suite remain unverified in native agent discovery. This proves project discovery for the observed skills, not model compliance, user-scope discovery or every future agent version. See [current evidence](../../docs/TEST_EVIDENCE.md) and [historical compatibility evidence](docs/COMPATIBILITY.md).

For suggested usage order and the boundary between public advisors and PhasePilot's engine, see the [workflow guide](../../docs/SKILL_WORKFLOWS.md). Primary category assignments live in the [collection catalog](../../SKILL_CATALOG.md).
