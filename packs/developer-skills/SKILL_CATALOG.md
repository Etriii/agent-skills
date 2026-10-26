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
| [backend-review](skills/backend-review/README.md) | API contracts, authorization and side effects | Planning advisor |
| [database-review](skills/database-review/README.md) | Integrity, migration and recovery | Planning advisor |
| [security-privacy-review](skills/security-privacy-review/README.md) | Trust boundaries and data policy | Planning advisor |
| [business-rules-review](skills/business-rules-review/README.md) | Eligibility, authority and transitions | Planning advisor |
| [delivery-readiness](skills/delivery-readiness/README.md) | Configuration, rollout and delivery evidence | Planning advisor |
| [critical-review](skills/critical-review/README.md) | Substantiated challenges and simpler alternatives | Planning advisor |
| [deep-critique](skills/deep-critique/README.md) | Generic assessment with ratings, combined modes and categorized immutable reports | Full critique |

Essential contains the first four only. The library has no default background loading, invocation telemetry or private runtime requirement. `environment-doctor` provides deterministic command guidance; it does not ship a diagnostics engine. Execution aids are agent instructions, not command runners.

Metadata records local authorship, capabilities, version and undecided license status. Both installed agents discovered the original 15 names through isolated local protocol checks; that compatibility statement covers discovery only, not model compliance, user-scope discovery or every future agent version. The new deep-critique skill has unverified native compatibility and records an empty compatible_agents list. See [compatibility evidence](docs/COMPATIBILITY.md).
