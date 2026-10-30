# Choosing and ordering skills

Use the [catalog](../SKILL_CATALOG.md) to find skills by purpose. Categories describe what a skill does; this guide describes when it can help. Packs remain installation sources. The suggested order is guidance, not an automatic pipeline: invoke only skills relevant to the authorized task.

## Standalone development

Public skills work without PhasePilot. Use these stages when the corresponding need exists:

| When | Skills | Expected result |
|---|---|---|
| The task needs clarification | `prompt-intake` | Versioned questions, recommendations, custom answers and a concrete next action. |
| An implementation plan needs review | `plan-review`; optionally `critical-review` or `deep-critique` | Coverage, dependency findings and justified changes. Choose a short planning challenge or a broader assessment as needed. |
| Decisions or technical risks remain | `blocker-check` and relevant engineering reviewers | Evidence-linked blockers and decisions before dependent implementation. |
| Execution prerequisites need checking | `environment-doctor` | Available tools, services, Git state and explicit missing prerequisites. |
| One selected scope is ready and authorized | `phase-runner` | Implementation, checkpoints and verification within that scope. |
| Work needs acceptance verification | `completion-check`; `delivery-readiness` when delivering | Acceptance evidence and remaining integration or delivery gates. |
| Another session needs to continue | `phase-handoff` | Current scope, decisions, files, verification, blockers and the next action. |
| An accepted plan needs a version transition | `version-manager` | A reviewed new version preserving prior history and relevant decisions. |

Select engineering reviewers by the change: `architecture-review` for boundaries, `frontend-review` for UI behavior, `backend-review` for request paths, `database-review` for persistence, `security-privacy-review` for trust and data handling, and `business-rules-review` for policy. Independent checks can happen together; unresolved decisions stop only work that depends on them.

These are agent-chat requests for an installed skill, not shell commands:

```text
$prompt-intake Review docs/plan.md against the current application before implementation.
$plan-review docs/plan.md
$blocker-check Check unresolved decisions for the selected feature in docs/plan.md.
```

A review does not authorize implementation. Each invocation must retain the requested scope; completing one stage does not automatically start the next.

## UI and UX reviews with previews

Use `ultimate-ui-ux` to inventory all application pages or selected routes, review visual and task-flow problems, choose fitting patterns, and save findings before creating proposed layouts. The main skill contains both disciplines and includes mobile checks by default; `ultimate-ui` and `ultimate-ux` are independently installable focused entrypoints. `ultimate-mobile` is an independent shortcut for mobile web UI/UX work with desktop regression checks.

These are agent-chat requests in the target application:

```text
$ultimate-ui-ux run
$ultimate-ui-ux run --page /stores/:slug
$ultimate-ui run --page /orders
$ultimate-ux run --page /checkout --auto
$ultimate-mobile run --page /orders --auto
```

Default execution stops after the proposal, then after low-fidelity before/after comparisons. Proposal approval authorizes previews; design approval authorizes implementation. Explicit `--auto` or a task-specific no-approval request authorizes review, sketches, changes and verification inside the selected scope without skill approval pauses. Platform permissions and material unresolved policy choices still apply. Generic continuation is not new approval.

The agent saves coverage, recommendations, revisions, decisions and proof under the target's `.ui-ux/runs/` directory, preserving previous runs. It does not assume every long page needs tabs, alter unselected shared callers, fabricate rendered evidence or change business/data policy to finish a redesign. Refer to [the suite guide](../packs/developer-skills/skills/ultimate-ui-ux/README.md) for commands, continuation and source licenses.

## Implementation and change safety

Select a helper according to the authorized work. Diagnose an unclear failure first; for implementation, normally choose one of the feature, fix, refactor or migration helpers. Use verification-only guidance when the task is to check existing work.

| Task | Optional helper |
|---|---|
| Unclear or intermittent failure | `investigate-first` |
| New feature | `lean-build` |
| Runtime settings discovery, design, implementation or verification | `system-settings` |
| Specific defect or small behavior change | `surgical-patch` |
| Structural change preserving behavior | `safe-refactor` |
| Compatibility-sensitive transition | `migration` |
| Verification without new implementation | `verify-and-stop` |

Suggested flow: review the plan, resolve blockers, select the applicable helper, perform the authorized work, verify acceptance and record a handoff. A helper is optional at each stage. `completion-check` remains the Essential acceptance reviewer; `verify-and-stop` supplies a bounded verification method rather than a competing completion record.

Use `$system-settings scan` to inspect application behavior, existing configuration, real consumers and audit coverage before deciding whether runtime settings are justified. It supports applications with no settings infrastructure and can recommend no new settings. `plan` remains read-only; `build <scope>` implements selected settings, category-first loading and audit reuse within that authorization. `verify` checks existing work without automatic fixes. See the [skill guide](../packs/developer-skills/skills/system-settings/README.md).

For a PhasePilot-managed project, include the desired helper names in `selected_skills`, review `skills sync --dry-run`, then approve the exact local copies through the existing lifecycle. Once the selected scope is authorized, invoke the installed helper in the same coding-agent session, for example:

```text
$lean-build Implement only the currently authorized feature using the existing owners and approved acceptance conditions.
```

PhasePilot keeps ownership of scope, readiness, approvals, checkpoints, integration and handoff. These helpers have work-type capabilities rather than the router's technical-domain tags, so their addition does not automatically insert them into its advisor routes. Explicit use does not grant extra permissions or start another phase.

## How PhasePilot uses the skills

PhasePilot is a separate private coordinator. Its coding-agent wrapper reviews source and performs authorized implementation; its Python engine records and validates planning, consent, readiness, checkpoints and integration. Installing public skills supplies advisors, not a second execution engine.

| Step | Agent request | What owns the result |
|---|---|---|
| Review the complete plan | `$phasepilot plan docs/plan.md` | The selected project's versioned review and `answers.md`. Relevant public reviewers can supply findings. |
| Resolve and approve decisions | `$phasepilot approve` | The engine's exact preview and recorded consent; editing answers alone grants no approval. |
| Inspect the selected scope | `$phasepilot check phase-01` | Dependency and blocker review, installed-advisor recommendations and the remaining preparation requirements. |
| Implement one authorized scope | `$phasepilot run phase-01` | The agent implements; the engine validates readiness and records checkpoints and evidence. Terminal `run` does not launch an agent. |
| Inspect completion and pending gates | `$phasepilot status` | Recorded tests, manual acceptance, integration and handoff status. Finish required gates before dependent execution. |
| Propose another plan version | `$phasepilot next docs/next-plan.md` | A separately reviewed version transition after acceptance, or an explicit documented exception. |

These are agent-chat examples. Use actual registered identifiers and paths. Native agent command spelling varies. Follow PhasePilot's installed wrapper and command documentation for exact preparation, consent and recovery commands. Do not automatically continue to another phase, merge or publish.

The current advisor router reads installed metadata. It recommends one eligible `critical-review` advisor for the whole plan and at most three relevant installed advisors per subtask, based on capabilities. Required unavailable advisors remain blockers. The category table and this suggested order do not change that routing, install missing skills or prove invocation; usage remains `UNKNOWN` without observation.

## Keep one owner for each record

- During PhasePilot planning, keep canonical questions and decisions in its versioned records. A separate `prompt-intake` can clarify an earlier standalone request, but its answers do not approve PhasePilot decisions or replace its `answers.md`.
- `deep-critique` is an optional assessment. Its report can support findings; its recommendations do not grant consent and it is not automatically substituted for the router's `critical-review` capability.
- Use the PhasePilot wrapper to coordinate implementation when that is the selected workflow. Standalone `phase-runner` remains an alternative instruction set, not another concurrent scheduler for the same work.
- Use PhasePilot's version transition for engine-managed plans. Standalone `version-manager` guidance does not create another authoritative version history.
- Ultimate QA remains a separately installed audit workflow with its own kit requirements. It is not imported into every PhasePilot project merely because it appears in the collection catalog.

## Select and update public skills in PhasePilot

New PhasePilot projects default to four Essential skills: `plan-review`, `blocker-check`, `phase-handoff` and `completion-check`. Its distributor selects the local `agent-skills` collection and `developer-skills` pack. All 23 pack skills are selectable; installing all is explicit. Existing projects retain their recorded provider and selected skills.

To add optional skills to an existing project, preserve its configuration and add the desired names to `selected_skills` in `.phasepilot/config.md`. For example, this selection adds standalone clarification and generic critique tools to the four Essential skills:

```yaml
selected_skills: [plan-review, blocker-check, phase-handoff, completion-check, prompt-intake, deep-critique]
```

Adding names is a desired selection, not proof of installation or invocation. Preview copies, approve them through the existing lifecycle, then inspect installed integrity. These are terminal commands, with an example target to replace:

```powershell
phasepilot skills sync --project 'D:\My App' --dry-run
phasepilot skills sync --project 'D:\My App'
phasepilot skills doctor --project 'D:\My App'
```

For already managed copies, check and preview current local payload updates separately:

```powershell
phasepilot skills update --check --project 'D:\My App'
phasepilot skills update --project 'D:\My App' --dry-run
phasepilot skills update --project 'D:\My App'
```

Sync fills missing copies while preserving installed pins. Update reviews managed payload or metadata changes and retains backups. Both preserve unmanaged or locally modified files; active execution can freeze mutations. No source download, global installation or automatic provider adoption follows from these commands.

Native project discovery of all 23 skills was observed in Codex CLI 0.165.0 and Claude Code 2.1.299 using isolated homes and no model prompt. See [verification evidence](TEST_EVIDENCE.md). Discovery does not prove model adherence or automatic selection for every task.
