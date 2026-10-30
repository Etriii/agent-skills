# Developer Skills pack

Twenty-four independent skills for prompt intake, planning, implementation, generic critique, development reviews, delivery checks and handoff. Each README and metadata file is included in the payload manifest. No private runner, Docker or API key is required. The Python installer works offline once the source is downloaded.

This pack belongs to [Agent Skills](../../README.md). Each skill has its own README with installation, usage and prerequisites.

Browse by purpose in the [categorized collection catalog](../../SKILL_CATALOG.md), or follow the [workflow guide](../../docs/SKILL_WORKFLOWS.md) for suggested standalone order and PhasePilot integration. The pack remains one installation source; categories do not change skill paths or require invoking every skill.

## Install with npx

Requires Node.js 22.20+ and npm. Install one skill or all 24 globally for Codex:

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

Essential contains plan-review, blocker-check, phase-handoff and completion-check. Use `--skills blocker-check` for one or `--bundle all` explicitly for all 24. Installation executes no skill. The pack-local `tools/install_skills.py` is an entry point to the same collection tool.

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
| [deep-critique](skills/deep-critique/README.md) | Full generic critique and ratings by default, with optional focused modes. |
| [delivery-readiness](skills/delivery-readiness/README.md) | Check configuration, tested artifacts, rollout sequencing and recovery before delivery. |
| [environment-doctor](skills/environment-doctor/README.md) | Inspect local tool availability, Git state and required services with read-only diagnostics. |
| [investigate-first](skills/investigate-first/README.md) | Diagnose unclear failures before proposing code changes. |
| [lean-build](skills/lean-build/README.md) | Implement a bounded feature through existing owners. |
| [migration](skills/migration/README.md) | Make compatibility-sensitive transitions with preservation and recovery proof. |
| [frontend-review](skills/frontend-review/README.md) | Review UI state ownership, forms, accessibility and responsive behavior with explicit evidence limits. |
| [phase-handoff](skills/phase-handoff/README.md) | Write a standalone Markdown handoff connecting scope, decisions, Git state and executed checks. |
| [phase-runner](skills/phase-runner/README.md) | Execute one authorized ready phase with checkpoints, verification and a bounded handoff. |
| [plan-review](skills/plan-review/README.md) | Review complete-plan coverage, dependencies and existing implementation before development. |
| [prompt-intake](skills/prompt-intake/README.md) | Clarify a task with recommended choices, custom answers, versioned question files and next-action hints. |
| [safe-refactor](skills/safe-refactor/README.md) | Restructure code while preserving defined behavior and contracts. |
| [security-privacy-review](skills/security-privacy-review/README.md) | Trace trust boundaries, permissions and data handling for a scoped change. |
| [surgical-patch](skills/surgical-patch/README.md) | Fix a specific defect with focused regression evidence. |
| [table-ux-review](skills/table-ux-review/README.md) | Audit table detail navigation and row actions with role-aware recommendations and accessibility checks. |
| [verify-and-stop](skills/verify-and-stop/README.md) | Verify acceptance conditions without adding implementation scope. |
| [version-manager](skills/version-manager/README.md) | Plan and record a development-plan version transition while preserving accepted history. |

Invoke skills in agent chat with `$blocker-check` in Codex or `/blocker-check` in Claude Code, followed by the scope and relevant files. Refresh the agent session after installation. Reviews do not authorize implementation unless that skill's explicit scope and the user's instruction provide it.

Use `$prompt-intake <task>` to inspect a prompt before starting dependent work. Each new intake saves `.prompt-intake/questions-v001.md` or the next version and gives a next-action hint. Answer material questions through an available native question tool or in the file, then reply `continue` to resume the active intake. Clear tasks are recorded and proceed directly; automatic matching is not a global prompt interception hook.

For a generic assessment of the current idea, plan, design, implementation, document or decision, type only `$deep-critique`. Full review and ratings run by default; `$deep-critique help` lists optional modes and combinations such as `roast rate`. Python 3.11+ enables categorized reports in the target's ignored `.deep-critique/` folder; each run preserves earlier results. Use `critical-review` for a short planning-specific challenge instead.

## Contribute

Follow [CONTRIBUTING.md](../../CONTRIBUTING.md) for skill documentation, manifests, checks and pull requests.

Run collection tests from the root with `python -B -m unittest discover -s tests -v`. License status remains UNDECIDED; see [collection license status](../../LICENSE.md).
