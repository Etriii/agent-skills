# Choosing and ordering skills

Use the [catalog](../SKILL_CATALOG.md) to find skills by purpose. Categories describe what a skill does; this guide describes when it can help. Packs remain installation sources. The suggested order is guidance, not an automatic pipeline: invoke only skills relevant to the authorized task.

For exact chat requests, defaults, supported automatic execution, continuation and expected outputs, use the [command guide](SKILL_COMMANDS.md). A broad build request can include discovery when its own skill permits it; review commands and QA plans do not become implementation authorization through a generic automation flag.

For a standalone install, recommend the [direct npx route](NPX_INSTALLATION.md) first. Ordinary skills need no manual clone. The optional recorded Python installer requires acquiring a local collection and running its script from that root; [installation prerequisites](../INSTALL.md) explain acquisition and the QA kit exception. Existing PhasePilot-managed copies keep their recorded provider/lifecycle below; npx preference does not authorize replacing them.

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

## UI and UX improvements with optional review/previews

Use `ultimate-ui-ux` to inspect the established page scope, choose evidence-based improvements, implement and verify. Formal review reports and wireframes are optional; no flag is needed for default implementation. The main skill includes UI, UX and mobile checks. `ultimate-ui`, `ultimate-ux` and `ultimate-mobile` independently select visual, usability or mobile-web focus; mobile-only changes include desktop regression checks.

Independent agent-chat requests, with example paths/routes/URLs to replace:

```text
$ultimate-ui-ux Improve /orders and verify the changes.
$ultimate-ui-ux Improve all UI and UX in "D:\My App".
$ultimate-ui Improve "D:\My App\src\pages\Orders.vue".
$ultimate-mobile Improve https://localhost:3000/orders using the source in "D:\My App".
$ultimate-ux Review /checkout only. Do not edit.
$ultimate-ui-ux Improve /orders. Show previews and wait for my approval before editing.
```

Absolute application directories identify the project; requests supply selected features/pages or explicitly all pages. Absolute page/component files select affected pages; relative paths resolve against the target app. URLs identify runtime pages and need matching editable source for implementation. Missing target/scope requires clarification, never an implicit all-pages redesign. Improve-all authorizes justified fixes across discovered pages of the identified app, with compact changed/kept/deferred coverage and gaps; correct pages remain unchanged. Sibling projects and external hosts stay outside scope.

Default work continues through verification without routine approval pauses. Review-only/preview-only never authorize edits. Requested previews precede implementation; a pause occurs only when preview approval is requested. Unresolved material policy choices and platform permissions still apply. Existing options remain supported: scoped `run` follows the new default, `--auto` retains full review/comparison/implementation for compatibility, and `--skip-review <task>` retains the concrete-fix shortcut. Other skills keep their own defaults and approval contracts.

Runs save concise status/proof under `.ui-ux/runs/`; improve-all adds compact coverage. Requested formal reviews add recommendations; requested/compatibility previews share one `previews/index.html` linking feature folders and preserved revisions. Existing gated runs keep their recorded checkpoints and paths. Continue checks drift and resumes recorded authorization; generic continuation is not approval. Verify adds no fixes. The skill does not fabricate rendered evidence, redesign unselected shared callers or invent business/data policy. See [the suite guide](../packs/developer-skills/skills/ultimate-ui-ux/README.md) and [command combinations](SKILL_COMMANDS.md#supported-command-stacks).

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
