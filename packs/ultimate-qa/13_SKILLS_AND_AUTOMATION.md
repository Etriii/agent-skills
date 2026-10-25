# 13 – Installable QA skills and automated review

The skills in `skills/` are small, separately installable agent workflows. The numbered kit documents remain the shared checklist, report format, and safety rules. Install the core skill for a versioned audit; add only the specialist skills you need. The same `SKILL.md` format works in Codex and Claude installations that support skills. Other agents can read the files directly as instructions.

This kit lives at `packs/ultimate-qa/` in Agent Skills. Keep its templates and helpers together with its skills.

## Install

Use the collection root and shared lifecycle tool:

```powershell
python tools/install_skills.py --pack ultimate-qa --list
python tools/install_skills.py --pack ultimate-qa --agent codex --project "D:\My App" --skills ultimate-qa ultimate-qa-architecture --dry-run
python tools/install_skills.py --pack ultimate-qa --agent codex --project "D:\My App" --skills ultimate-qa ultimate-qa-architecture
```

Choose `--agent claude` or `--agent both` when needed. `--bundle all` selects all nine QA skills explicitly. For a user installation, replace `--project` with `--scope user --user-home <existing-home>`. Both scopes use `.agents/skills/` for Codex and `.claude/skills/` for Claude. The core and client copies receive `kit-location.txt`; use install `--replace` to update their pointers after moving the collection. Old copies under `.codex/skills/` or custom destinations are not scanned or removed.

The [installation guide](../../INSTALL.md) documents checksums, approval, backups and recovery. Completed changing operations write scoped Markdown records. Installation controls where skills are found; the application's open agent session still controls the QA target.

| Skill | Use independently for |
|---|---|
| `ultimate-qa` | Combined run, intake, audit, plan, status, finding state, version transitions |
| `ultimate-qa-client` | Optional client report from completed recommendations, decisions, approval history |
| `ultimate-qa-environment` | Docker/Compose preflight, isolated services, DB readiness |
| `ultimate-qa-browser` | User journeys, roles, visual states, accessibility evidence |
| `ultimate-qa-accessibility` | Automated and keyboard accessibility checks with precise manual remainder |
| `ultimate-qa-api` | API contracts, roles, validation, idempotency and persisted effects |
| `ultimate-qa-performance` | Repeatable latency, throughput, resource and query measurements |
| `ultimate-qa-architecture` | Ownership, coupling, state, testability and maintainability |
| `ultimate-qa-security` | Authorization, data integrity, secrets, dependency exposure |

Each optional skill works alone when given a target project and enough context. Without the kit, it reports its findings in the project's preferred format. The core skill runs the same relevant checks itself when a specialist is not installed; a missing optional skill is not a reason to label a check manual.

## Uninstall and reinstall

Use the same scope and agent as installation. The shared tool checks the whole selection, recorded ownership and current content hashes before moving removed copies to retained backups:

```powershell
python tools/install_skills.py --pack ultimate-qa --agent codex --project "D:\My App" --bundle all --uninstall --dry-run
python tools/install_skills.py --pack ultimate-qa --agent codex --project "D:\My App" --bundle all --uninstall
```

Use `--skills ultimate-qa-client` instead of `--bundle all` for selective removal. For a user installation, replace `--project` with `--scope user --user-home <existing-home>`. History, other packs/agents, application code, ignore rules and `qa-findings/` remain intact. Modified or unrecorded copies are preserved; see [UNINSTALL.md](../../UNINSTALL.md) for adoption and edited copies. Failures before commit roll back the changes and provisional record.

The removal is recorded in `.agent-skills/history/<operation-id>/operation.md`, linking the old installation and retained backup. Reinstall with the original install command and refresh the agent's skill list. Removing the client skill leaves core QA available; `run --client` reports the missing client skill until reinstalled.

## Interactive commands

Invoke these in Codex chat; they are skill instructions, not shell commands. In Claude Code, replace `$` with `/`, for example `/ultimate-qa run --client`:

```text
$ultimate-qa run
$ultimate-qa run --client
$ultimate-qa initialize
$ultimate-qa audit
$ultimate-qa plan
$ultimate-qa status
$ultimate-qa next-version
$ultimate-qa-client intake
$ultimate-qa-client prepare
$ultimate-qa-client report
$ultimate-qa-client decisions
```

`run` initializes the current application if needed, audits it, and writes the QA plan without requiring another command between stages. On rerun it checks state, report contents, evidence, and source changes before reusing completed stages; it finishes drafts and stale checks in the current version. `--client` then invokes the installed client skill's `prepare` workflow; without that flag no client documents are generated. It can pause for first-run intake answers or an initialization or permission blocker, while missing runtime tools block only dependent checks. Resume with the original invocation, retaining `--client` when needed. A completed current review is reported without opening a new version. Neither form starts implementation or grants destructive-testing permission. The standalone commands remain available for staged reviews.

On `initialize`, the agent confirms the Git root of the application opened in its session, asks whether requirements and an existing plan exist, and runs `python <kit>/tools/qa_preflight.py --project <app>`. If it is in the kit or an ambiguous parent folder, it asks for the target application before writing. It checks Docker, daemon, Compose, and Compose configuration before service and database health checks. It creates `<app>/qa-findings/`, appends `qa-findings/` to the app's `.gitignore` only when needed, and verifies Git ignores that directory. If Git already tracks it, initialization stops with a specific repair instruction. This avoids silently exposing review output. Runtime checks should use the project's existing containers and a disposable database. A missing Docker setup is an environment blocker, not an app defect.

The agent can use the deterministic state helper directly:

```sh
python skills/ultimate-qa/scripts/qa_state.py init --project /path/to/app
python skills/ultimate-qa/scripts/qa_state.py add --project /path/to/app --id F-001 --title "Wrong invoice owner" --evidence "v1/recommendations/evidence/access.txt"
python skills/ultimate-qa/scripts/qa_state.py set-status --project /path/to/app --id F-001 --status resolved --evidence "test access::owner_isolation passed at commit abc123"
python skills/ultimate-qa/scripts/qa_state.py next-version --project /path/to/app
python skills/ultimate-qa/scripts/qa_state.py status --project /path/to/app
```

`qa-findings/state.json` points to the current version. Each `vN/state.json` records its stage (`initialized`, `auditing`, `planned`, `awaiting_client`, `implementing`, or `complete`) and machine-readable finding IDs, titles, statuses, evidence, origin version, and carry/reopen provenance. Core QA stops at `planned`; `awaiting_client` applies only when the optional client workflow is invoked, and `implementing` requires separately instructed development. Use `qa_state.py set-stage --project /path/to/app --stage auditing` when the stage changes. `next-version` copies only `open`, `blocked`, and `pending` items. The agent must verify progress and update statuses first; closed items remain in old snapshots and the human-readable version history. A regression reopens the original ID with new evidence. Never delete a prior version. The state file is an index, not a substitute for the report and raw evidence. IDs remain unique across the project.

## Evidence and manual work

For every executed check, wait for exit or a documented timeout. A launch, queued job, or service still starting is pending. Record command, environment, commit, role, result, and evidence. Use `inconclusive` for timeouts and tool failures; use `blocked` for a missing prerequisite. Mark `NEEDS-MANUAL` only when the remaining step truly needs human judgment, an unavailable device, or an inaccessible external system. Give exact steps. Browser automation can cover many role and journey checks; it cannot certify subjective usability or all assistive technology behavior.

## Further improvements

1. Add project-specific smoke recipes for the top user journeys, with seeded Docker data and a known reset command. This makes the largest share of repeat audits reliable.
2. Record a coverage map from each checklist ID and requirement to its test, environment, evidence, and latest outcome. This exposes gaps without inflating pass counts.
3. Add contract tests for external APIs and mail/payment sandbox integrations. Keep real provider acceptance separate from sandbox proof.
4. Add repeatable database migration and backup/restore drills on disposable data. Record both forward and rollback outcomes.
5. Render Word reports and inspect page images in CI where a compatible renderer is available. Package structure checks alone cannot prove layout.
6. Track flaky checks separately with rerun count and cause; do not transform a transient failure into a pass by retrying until green.

No universal Docker file can safely infer every app's database, startup order, or secrets. The environment skill reuses the target project's Compose setup and reports what is missing so a stack-specific recipe can be added deliberately.
