# Developer Skills pack

Thirty independent skills for prompt intake, planning, UI/UX and mobile review, reports, system settings, implementation, generic critique, development reviews, delivery checks and handoff. Each README and metadata file is included in the payload manifest. No private runner, Docker or API key is required. The Python installer works offline once the source is downloaded.

This pack belongs to [Agent Skills](../../README.md). Each skill has its own README with installation, usage and prerequisites.

The [command guide](../../docs/SKILL_COMMANDS.md) lists copyable requests, supported continuous workflows, expected outputs and stopping points for every skill. Natural-language reviewers do not inherit another skill's automation flags.

Browse by purpose in the [categorized collection catalog](../../SKILL_CATALOG.md), or follow the [workflow guide](../../docs/SKILL_WORKFLOWS.md) for suggested standalone order and PhasePilot integration. The pack remains one installation source; categories do not change skill paths or require invoking every skill.

## Install with npx

Recommended route: install Node.js 22.20+ with npm/npx, ensure Git is available for repository fallback, and use network access to npm/GitHub. No manual clone of this collection is required. PowerShell, starting in an existing target application; replace the example path:

```powershell
Set-Location 'D:\My App'
npx skills@1.7.4 add https://github.com/Etriii/agent-skills --skill system-settings --agent codex claude-code --copy
```

Expected result: only system-settings is selected for Codex and Claude Code, with `.agents/skills/system-settings/SKILL.md` and `.claude/skills/system-settings/SKILL.md` under the application. Review the CLI summary, refresh the agent session, then use `$system-settings scan` or `/system-settings scan` in agent chat. For one agent choose `--agent codex` or `--agent claude-code`; add `-g` only for intended global availability.

For all 30 Developer Skills instead, run this separate selection from the same application folder:

```powershell
npx skills@1.7.4 add https://github.com/Etriii/agent-skills/tree/main/packs/developer-skills --skill '*' --agent codex claude-code --copy
```

Quote `'*'` and use this pack-specific source to avoid selecting other packs. Remote commands use published files; an unpushed local change is not installed from GitHub. The [npx guide](../../docs/NPX_INSTALLATION.md) gives prerequisite checks, expected files, troubleshooting, scope, updates and removal. External installs do not write this collection's Markdown operation history.

## Install with Markdown records

This is the optional recorded/offline alternative. Obtain the complete collection first using the [ZIP/curl or Git clone steps](../../INSTALL.md#optional-local-copy-for-python-and-offline-use). Use Python 3.11+ from its actual inner root containing `tools/` and `packs/`, not from the destination application. `tools/install_skills.py` is a local file. Run preview and install as separate commands:

```powershell
python tools/install_skills.py --pack developer-skills --list
python tools/install_skills.py --pack developer-skills --agent both --project "D:\My App" --bundle essential --dry-run
python tools/install_skills.py --pack developer-skills --agent both --project "D:\My App" --bundle essential
```

Essential contains plan-review, blocker-check, phase-handoff and completion-check. Use `--skills blocker-check` for one or `--bundle all` explicitly for all 30. Installation executes no skill. The pack-local `tools/install_skills.py` is an entry point to the same collection tool.

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
| [report-builder](skills/report-builder/README.md) | Discover reporting needs and build scoped report pages with styled PDF and Excel exports and retained generated files. |
| [safe-refactor](skills/safe-refactor/README.md) | Restructure code while preserving defined behavior and contracts. |
| [security-privacy-review](skills/security-privacy-review/README.md) | Trace trust boundaries, permissions and data handling for a scoped change. |
| [surgical-patch](skills/surgical-patch/README.md) | Fix a specific defect with focused regression evidence. |
| [system-settings](skills/system-settings/README.md) | Assess runtime settings needs and implement scoped settings with category loading and audit reuse. |
| [table-ux-review](skills/table-ux-review/README.md) | Audit table detail navigation and row actions with role-aware recommendations and accessibility checks. |
| [ultimate-ui-ux](skills/ultimate-ui-ux/README.md) | Coordinate UI/UX audits, before/after wireframes and gated or autonomous scoped improvements. |
| [ultimate-ui](skills/ultimate-ui/README.md) | Review and improve visual presentation while preserving task flows. |
| [ultimate-ux](skills/ultimate-ux/README.md) | Review and improve navigation and task flows while preserving visual identity. |
| [ultimate-mobile](skills/ultimate-mobile/README.md) | Review and improve mobile web headers, filters, dialogs and journeys with desktop regression checks. |
| [verify-and-stop](skills/verify-and-stop/README.md) | Verify acceptance conditions without adding implementation scope. |
| [version-manager](skills/version-manager/README.md) | Plan and record a development-plan version transition while preserving accepted history. |

Invoke skills in agent chat with `$blocker-check` in Codex or `/blocker-check` in Claude Code, followed by the scope and relevant files. Refresh the agent session after installation. Reviews do not authorize implementation unless that skill's explicit scope and the user's instruction provide it.

Use `$prompt-intake <task>` to inspect a prompt before starting dependent work. Each new intake saves `.prompt-intake/questions-v001.md` or the next version and gives a next-action hint. Answer material questions through an available native question tool or in the file, then reply `continue` to resume the active intake. Clear tasks are recorded and proceed directly; automatic matching is not a global prompt interception hook.

For a generic assessment of the current idea, plan, design, implementation, document or decision, type only `$deep-critique`. Full review and ratings run by default; `$deep-critique help` lists optional modes and combinations such as `roast rate`. Python 3.11+ enables categorized reports in the target's ignored `.deep-critique/` folder; each run preserves earlier results. Use `critical-review` for a short planning-specific challenge instead.

Use `$ultimate-ui-ux run` for a combined all-pages interface review, or add `--page /route` and `--auto` for selected-page autonomous work. Mobile checks run by default; `$ultimate-mobile run` is a mobile-focused shortcut. The default shows findings before sketches and sketches before application edits, with approval between stages. Each of the four UI/UX entrypoints works alone and bundles licensed reference material; see [the suite guide](skills/ultimate-ui-ux/README.md).

## Contribute

Follow [CONTRIBUTING.md](../../CONTRIBUTING.md) for skill documentation, manifests, checks and pull requests.

Run collection tests from the root with `python -B -m unittest discover -s tests -v`. License status remains UNDECIDED; see [collection license status](../../LICENSE.md).
