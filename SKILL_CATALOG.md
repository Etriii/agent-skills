# Standalone catalog

Version 0.1.0; each stable skill ID equals its generic directory/frontmatter name. Each row links to actual independent instructions. Installation does not execute a skill or prove it was used.

| Skill | Responsibility | Default mode |
|---|---|---|
| [plan-review](skills/plan-review/SKILL.md) | Whole-plan coverage and dependencies | Planning |
| [blocker-check](skills/blocker-check/SKILL.md) | Evidence-linked blockers and independent policy questions | Planning |
| [phase-handoff](skills/phase-handoff/SKILL.md) | Bounded Markdown handoff and checkpoint | Execution aid |
| [completion-check](skills/completion-check/SKILL.md) | Acceptance and integration evidence | Verification |
| [environment-doctor](skills/environment-doctor/SKILL.md) | Read-only deterministic local diagnostics | Diagnostics guidance |
| [phase-runner](skills/phase-runner/SKILL.md) | Exactly one authorized phase | Execution aid |
| [version-manager](skills/version-manager/SKILL.md) | Preserved plan-version transition | Versioning |
| [architecture-review](skills/architecture-review/SKILL.md) | Boundaries, ownership and tradeoffs | Planning advisor |
| [frontend-review](skills/frontend-review/SKILL.md) | UI states, accessibility and visual evidence | Planning advisor |
| [backend-review](skills/backend-review/SKILL.md) | API contracts, authorization and side effects | Planning advisor |
| [database-review](skills/database-review/SKILL.md) | Integrity, migration and recovery | Planning advisor |
| [security-privacy-review](skills/security-privacy-review/SKILL.md) | Trust boundaries and data policy | Planning advisor |
| [business-rules-review](skills/business-rules-review/SKILL.md) | Eligibility, authority and transitions | Planning advisor |
| [delivery-readiness](skills/delivery-readiness/SKILL.md) | Configuration, rollout and delivery evidence | Planning advisor |
| [critical-review](skills/critical-review/SKILL.md) | Substantiated challenges and simpler alternatives | Planning advisor |

Essential contains the first four only. The library has no default background loading, invocation telemetry or private runtime requirement. `environment-doctor` provides deterministic command guidance; it does not ship a diagnostics engine. Execution aids are agent instructions, not command runners.

Metadata records local authorship, capabilities, version and undecided license status. Both installed agents discovered all 15 names through isolated local protocol checks; that compatibility statement covers discovery only, not model compliance, user-scope discovery or every future agent version. See [compatibility evidence](docs/COMPATIBILITY.md).
