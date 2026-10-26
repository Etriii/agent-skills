# Developer Skills pack

Fifteen independent development skills for planning, reviews, delivery checks and handoff. Original skill bodies and metadata are preserved; each README is included in the payload manifest. No private runner, Docker or API key is required. The Python installer works offline once the source is downloaded.

This pack belongs to [Agent Skills](../../README.md). Each skill has its own README with installation, usage and prerequisites.

## Install with npx

Requires Node.js 22.20+ and npm. Install one skill or all 15 globally for Codex:

```powershell
npx skills@1.7.4 add https://github.com/Etriii/agent-skills --skill blocker-check --agent codex -g --copy
npx skills@1.7.4 add https://github.com/Etriii/agent-skills/tree/main/packs/developer-skills --skill '*' --agent codex -g --copy
```

Omit `-g` from your application directory for project scope. Use `--agent claude-code` for Claude Code. Quote `'*'` and use this pack-specific source to avoid selecting other packs. Review the displayed destinations. The [npx guide](../../docs/NPX_INSTALLATION.md) covers scope, updates and removal. External installs do not write the collection's Markdown history.

## Install with Markdown records

Use Python 3.11+ from the collection root:

```powershell
python tools/install_skills.py --pack developer-skills --list
python tools/install_skills.py --pack developer-skills --agent both --project "D:\My App" --bundle essential --dry-run
python tools/install_skills.py --pack developer-skills --agent both --project "D:\My App" --bundle essential
```

Essential contains plan-review, blocker-check, phase-handoff and completion-check. Use `--skills blocker-check` for one or `--bundle all` explicitly for all fifteen. Installation executes no skill. The pack-local `tools/install_skills.py` is an entry point to the same collection tool.

The [installation guide](../../INSTALL.md) covers user scope, integrity, matching-copy adoption, backup replacement and recovery. The [removal guide](../../UNINSTALL.md) gives tracked uninstall/reinstall commands. Completed changing operations create scoped Markdown history; removal preserves records and content backups.

Read [SKILL_CATALOG.md](SKILL_CATALOG.md) for selection and [docs/SKILL_STANDARD.md](docs/SKILL_STANDARD.md) for metadata and payload hashes. Other historical pack contracts and compatibility reports retain their original evidence limits. Current collection proof is [TEST_EVIDENCE.md](../../docs/TEST_EVIDENCE.md).

## Included skills

| Skill | Purpose |
|---|---|
| [architecture-review](skills/architecture-review/README.md) | Review ownership, coupling and dependency direction across a proposed change. |
| [backend-review](skills/backend-review/README.md) | Review validation, authorization, transactions and side effects across backend request paths. |
| [blocker-check](skills/blocker-check/README.md) | Find requirement, policy, dependency and environment blockers before implementation. |
| [business-rules-review](skills/business-rules-review/README.md) | Map workflow rules to authoritative policy, server enforcement and boundary cases. |
| [completion-check](skills/completion-check/README.md) | Check acceptance criteria against executed evidence, configuration and integration state. |
| [critical-review](skills/critical-review/README.md) | Challenge unsupported assumptions and complexity using concrete failure paths and simpler alternatives. |
| [database-review](skills/database-review/README.md) | Review integrity, concurrency, migration ordering and recovery across database changes. |
| [delivery-readiness](skills/delivery-readiness/README.md) | Check configuration, tested artifacts, rollout sequencing and recovery before delivery. |
| [environment-doctor](skills/environment-doctor/README.md) | Inspect local tool availability, Git state and required services with read-only diagnostics. |
| [frontend-review](skills/frontend-review/README.md) | Review UI state ownership, forms, accessibility and responsive behavior with explicit evidence limits. |
| [phase-handoff](skills/phase-handoff/README.md) | Write a standalone Markdown handoff connecting scope, decisions, Git state and executed checks. |
| [phase-runner](skills/phase-runner/README.md) | Execute one authorized ready phase with checkpoints, verification and a bounded handoff. |
| [plan-review](skills/plan-review/README.md) | Review complete-plan coverage, dependencies and existing implementation before development. |
| [security-privacy-review](skills/security-privacy-review/README.md) | Trace trust boundaries, permissions and data handling for a scoped change. |
| [version-manager](skills/version-manager/README.md) | Plan and record a development-plan version transition while preserving accepted history. |

Invoke skills in agent chat with `$blocker-check` in Codex or `/blocker-check` in Claude Code, followed by the scope and relevant files. Refresh the agent session after installation. Reviews do not authorize implementation unless that skill's explicit scope and the user's instruction provide it.

## Contribute

Follow [CONTRIBUTING.md](../../CONTRIBUTING.md) for skill documentation, manifests, checks and pull requests.

Run collection tests from the root with `python -B -m unittest discover -s tests -v`. License status remains UNDECIDED; see [collection license status](../../LICENSE.md).
