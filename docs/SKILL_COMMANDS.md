# Skill command guide

Use this guide to choose a supported request and understand its effects. Every shipping skill is listed below; its linked README owns installation and detailed usage. The directory currently contains 39 skills across both packs. These examples were checked against the corresponding instructions and documentation; they are not evidence of model or target-application execution.

## Before entering a request

Use the [direct npx installation steps](../INSTALL.md#direct-installation-with-npx-recommended) first; ordinary skills require no manual clone. Then refresh the agent session and open the target application or establish the subject in the conversation. The skill installation directory is not the application target. Include an absolute target path when it is outside the open project. Replace example routes, filenames, feature names, and `<run-folder>` placeholders with actual inputs. The optional Python route needs a complete local checkout/ZIP and its collection root; QA core/client additionally need a durable kit as documented in the installation guide.

All requests below go in **agent chat**, not PowerShell, Bash, or a terminal. Codex uses `$skill-name`; Claude Code uses `/skill-name` with the same request text. Installation commands are separate terminal operations in each README. A skill name followed by a sentence is a natural-language request, not proof of a fixed CLI parser.

## Continuous work: use the actual interface

**Discover and build justified missing reports:**

```text
$report-builder build all clearly justified missing reports across this project --detail detailed
```

This includes discovery, evidence-based selection, specification, implementation and checks in one session. `--detail mid` selects essential report content without weakening access, export, progress or retention requirements. Covered reports are reused; Unknown and Unnecessary candidates are not built. No preceding scan/plan is required.

**Review and improve selected UI/UX without skill approval pauses:**

```text
$ultimate-ui-ux run --page /orders --auto
$ultimate-ui run --page /orders --auto
$ultimate-ux run --page /checkout --auto
$ultimate-mobile run --page /orders --auto
```

Each line is an independent example, not a sequence to run all four. Without `--auto`, the workflow stops for proposal approval, then design approval. The main skill supports `--focus ui` or `--focus ux`; shortcuts fix their focus and reject conflicts. Repeat `--page` to select more pages. Unresolved selectors never expand to all pages.

**Inspect and implement a known settings objective:**

```text
$system-settings build category loading and transactional settings history using existing settings, consumers and audit owners
```

The named objective supplies implementation scope; inspection does not justify adding every discovered setting. No generic `--auto` option is defined.

**Run the full QA assessment through recommendations:**

```text
$ultimate-qa run
$ultimate-qa run --client
```

Choose one line. The first initializes/resumes, audits and plans. The second additionally requests client preparation when its dependencies exist. Both stop before implementing or sending recommendations; `--client` does not approve proposed work. Intake can require answers. Use the original invocation again after supplying a missing prerequisite.

These are current-session workflows. They do not install a recurring scanner, scheduler, or unattended agent. Report-generation workers inside an application are separate from the agent's own execution. Do not copy `--auto` onto skills that do not define it.

## Developer Skills requests

Natural-language reviewers/helpers need the selected subject, files, acceptance and authorization in the request or conversation. With no identifiable subject, supply one rather than expecting a universal bare-invocation default. No fixed `run`, `build`, or `help` subcommand is implied for these sentence-based interfaces.

| Skill and detailed guide | Copyable agent-chat example | Expected result and boundary |
|---|---|---|
| [architecture-review](../packs/developer-skills/skills/architecture-review/README.md) | `$architecture-review Review the proposed API extraction in docs/plan.md. Trace existing ownership and recommend the smallest coherent change.` | Expect source-linked ownership and dependency findings, tradeoffs, and a minimal recommendation with regression needs. This is a planning review; stop before refactoring unless that work is separately authorized. |
| [backend-review](../packs/developer-skills/skills/backend-review/README.md) | `$backend-review Review the order cancellation endpoint, including denied requests, retry behavior and database effects.` | Expect findings that trace request validation, authorization, transactions and side effects, plus focused success/denial/retry test cases. Review remains advisory; recommendations do not silently become endpoint changes. |
| [blocker-check](../packs/developer-skills/skills/blocker-check/README.md) | `$blocker-check Check blockers for phase 2 in docs/plan.md. Cite authoritative sources and separate independent policy questions.` | Expect a source-backed blocker list with severity, owner, mitigation, status and next action, plus separate questions for independent policy choices. Missing authoritative requirements block dependent decisions; the skill does not choose policy or execute prerequisite work. |
| [business-rules-review](../packs/developer-skills/skills/business-rules-review/README.md) | `$business-rules-review Review the approval workflow, including existing approved records, cancellation and role boundaries.` | Expect a rule/source matrix, unresolved policy questions and boundary-case acceptance examples. The default is advice: no policy is selected or implemented from UI wording or convenience. |
| [completion-check](../packs/developer-skills/skills/completion-check/README.md) | `$completion-check Verify phase 2 against docs/plan.md and the current revision. Report pass, fail, blocked and unavailable evidence.` | Expect a criterion-by-criterion pass, fail, unavailable or blocked result with executed checks and remaining proof. It verifies existing work; application fixes, merging and deployment are outside this request. |
| [critical-review](../packs/developer-skills/skills/critical-review/README.md) | `$critical-review Challenge docs/plan.md using the current source. Report only substantiated concerns and the evidence needed to resolve them.` | Expect a short ranked set of evidence-backed objections, simpler alternatives and the checks that would settle each concern. If no concern survives source review, the result says so. This is critique, not implementation. |
| [database-review](../packs/developer-skills/skills/database-review/README.md) | `$database-review Review the account migration for old/new reader compatibility, backfill locking and rollback requirements.` | Expect integrity/migration findings with old/new reader compatibility, concurrency risks, preservation and recovery checks. Stop at the review; this request does not run schema changes or modify data. |
| [deep-critique](../packs/developer-skills/skills/deep-critique/README.md) | `$deep-critique` | Bare invocation reviews the current subject in full and normally saves a report plus a Git ignore entry. Critique never implements recommendations. |
| [delivery-readiness](../packs/developer-skills/skills/delivery-readiness/README.md) | `$delivery-readiness Assess this release against CI evidence, required configuration, migration order and recovery plans.` | Expect a gate report for the tested revision, required configuration, CI evidence, rollout and recovery, with owners for remaining blockers. It reports readiness; it does not publish, deploy or merge. |
| [environment-doctor](../packs/developer-skills/skills/environment-doctor/README.md) | `$environment-doctor Diagnose this workspace using its documented prerequisites. Report command exits without starting services or exposing secrets.` | Expect local command results and exit codes for Git, required tooling/configuration, and Docker only when the project requires it. It remains read-only: missing tools are reported without installations, builds, service starts, network requests or secret output. |
| [frontend-review](../packs/developer-skills/skills/frontend-review/README.md) | `$frontend-review Review the request form's loading, validation, permission and mobile states. Identify any missing browser evidence.` | Expect prioritized findings by source/route with reproduction steps and required UI acceptance checks. Source, automated accessibility, rendered and manual evidence remain separate. The default review does not redesign screens. |
| [investigate-first](../packs/developer-skills/skills/investigate-first/README.md) | `$investigate-first Diagnose the intermittent request failure and identify its responsible owner before editing.` | Expect a supported cause or ranked remaining hypotheses, reproduction limits, the responsible owner and the smallest useful next check. Diagnosis alone stops before code edits; a request that also authorizes the scoped fix can continue into that fix after tracing the cause. |
| [lean-build](../packs/developer-skills/skills/lean-build/README.md) | `$lean-build Implement the approved search feature using the existing request and UI owners.` | Expect the complete authorized feature through existing owners, focused verification and required configuration/setup notes. Discovery, implementation and checks run within that feature request without a separate command at each stage; the skill stops when its scope is satisfied. |
| [migration](../packs/developer-skills/skills/migration/README.md) | `$migration Migrate the configuration format while preserving existing values and verifying recovery after interruption.` | Expect only the authorized transition stage, with reader/writer compatibility, data-preservation checks and a documented rollback or recovery path. Later destructive contraction does not follow automatically unless it is already authorized. Unexecuted restore behavior is not reported as proven. |
| [phase-handoff](../packs/developer-skills/skills/phase-handoff/README.md) | `$phase-handoff Write docs/handoff.md for the selected phase using the current Git state and completed checks. Stop at this phase.` | Expect a standalone Markdown handoff at the requested path with scope, current Git state, acceptance/evidence, decisions, blockers and next-session reading. The document distinguishes tested from integrated work. It does not start the recommended next task. |
| [phase-runner](../packs/developer-skills/skills/phase-runner/README.md) | `$phase-runner Execute only phase 2 in docs/plan.md after checking prerequisites and repository rules. Stop after its tests and handoff.` | Expect implementation of only the identified ready scope, relevant tests/checkpoints and a truthful handoff. It verifies prerequisites first and stops before another scope. Required integration without authorization remains MERGE_PENDING; the invocation is not a private CLI or unattended scheduler. |
| [plan-review](../packs/developer-skills/skills/plan-review/README.md) | `$plan-review Review docs/plan.md for requirement coverage and dependency order. Inspect phase 2 deeply after reading all phases.` | Expect requirement coverage, source-referenced dependency findings, already-covered/missing/unknown work and unanswered decisions. Reordering is previewed before approved plan replacement; the review does not implement the plan. |
| [prompt-intake](../packs/developer-skills/skills/prompt-intake/README.md) | `$prompt-intake Add CSV export for the transactions page. Ask about decisions that could block correct implementation before editing.` | Clarifies the current task, saves a versioned intake, and resumes only already-authorized work after required answers. Questions-only requests stop at intake. |
| [report-builder](../packs/developer-skills/skills/report-builder/README.md) | `$report-builder build all clearly justified missing reports across this project --detail detailed` | Bare invocation scans. The broad build example scans, selects justified gaps, implements and verifies them; unknown policy is not invented. |
| [safe-refactor](../packs/developer-skills/skills/safe-refactor/README.md) | `$safe-refactor Consolidate the duplicated validation owner while preserving the existing API and error behavior.` | Expect the requested structural change with baseline/after proof that the specified public behavior, errors and side effects are preserved. It does not silently add features or schema/policy changes; any required external behavior left untested stays explicit. |
| [security-privacy-review](../packs/developer-skills/skills/security-privacy-review/README.md) | `$security-privacy-review Review the export workflow for object authorization, secret exposure, recipients and retention policy.` | Expect evidence-ranked findings with impact, safe reproduction and narrow mitigation, plus unresolved authoritative privacy decisions. This review does not authorize intrusive testing, production access or a new policy. |
| [surgical-patch](../packs/developer-skills/skills/surgical-patch/README.md) | `$surgical-patch Fix the stale response overwrite and verify that the latest request remains authoritative.` | Expect a root-cause fix, focused regression evidence and preserved surrounding behavior. The scoped fix request includes tracing, correction and checks; unrelated cleanup and failures remain separate. |
| [system-settings](../packs/developer-skills/skills/system-settings/README.md) | `$system-settings scan` | Bare invocation scans. Build inspects and implements only the named settings scope with audit/consumer integration; discovery can recommend no new settings. |
| [table-ux-review](../packs/developer-skills/skills/table-ux-review/README.md) | `$table-ux-review Audit all tables in this application. Inventory detail navigation and row actions by role, recommend action placement, and identify unverified coverage. Report before editing.` | Reviews by default. An explicit audit-and-fix request authorizes the selected cleanup; it preserves routes, roles and existing row workflows. |
| [ultimate-mobile](../packs/developer-skills/skills/ultimate-mobile/README.md) | `$ultimate-mobile run` | Bare/run reviews mobile web UI and UX with proposal/design gates. --auto includes responsive fixes and desktop regression checks. |
| [ultimate-ui](../packs/developer-skills/skills/ultimate-ui/README.md) | `$ultimate-ui run` | Bare/run reviews UI only with proposal/design gates. --auto authorizes the bounded visual workflow without skill pauses. |
| [ultimate-ui-ux](../packs/developer-skills/skills/ultimate-ui-ux/README.md) | `$ultimate-ui-ux run` | Bare/run reviews both disciplines and stops at proposal approval. Run with --auto includes sketches, implementation and checks for the selected pages. |
| [ultimate-ux](../packs/developer-skills/skills/ultimate-ux/README.md) | `$ultimate-ux run` | Bare/run reviews UX only with proposal/design gates. --auto authorizes the bounded usability workflow without skill pauses. |
| [verify-and-stop](../packs/developer-skills/skills/verify-and-stop/README.md) | `$verify-and-stop Verify the completed export behavior against its acceptance criteria and report remaining proof gaps.` | Expect acceptance results with exact checks/outcomes and remaining proof gaps. Failed checks produce a responsible issue and next action; the verification request does not authorize fixes or polish. |
| [version-manager](../packs/developer-skills/skills/version-manager/README.md) | `$version-manager Compare the current plan with the proposed next version. Preview the mapping and decisions requiring revalidation before writing.` | Expect an old-to-new plan mapping, REUSE/REVALIDATE decisions and affected-file preview before transition consent. After consent, prior plans/evidence stay intact and the new version receives its own record. It does not execute the new plan. |

## Ultimate QA requests

Core/client workflows need the complete durable QA kit and valid kit location. Specialist reviews use the selected application's existing tools and evidence. Missing environments or accounts block their checks rather than proving an application defect.

| Skill and detailed guide | Copyable agent-chat example | Expected result and boundary |
|---|---|---|
| [ultimate-qa](../packs/ultimate-qa/skills/ultimate-qa/README.md) | `$ultimate-qa run` | Use run explicitly for initialization/resume, audit and improvement plan. It never automatically implements that plan. |
| [ultimate-qa-accessibility](../packs/ultimate-qa/skills/ultimate-qa-accessibility/README.md) | `$ultimate-qa-accessibility Audit the request form and approval dialog for keyboard access, focus recovery and announced errors.` | Expect page/role/state findings with affected elements, rule or criterion where known, and automated/keyboard/screen-reader coverage separated. Retesting checks the same state; it does not automatically fix application defects. |
| [ultimate-qa-api](../packs/ultimate-qa/skills/ultimate-qa-api/README.md) | `$ultimate-qa-api Review the cancellation API with authorized test accounts and disposable data. Verify denied requests and duplicate submission effects.` | Expect contract, authorization, retry and persistence results with redacted request/response and database evidence. Schema drift and coverage gaps remain distinct from reproduced defects. Fixes or new regressions in application code require implementation authorization. |
| [ultimate-qa-architecture](../packs/ultimate-qa/skills/ultimate-qa-architecture/README.md) | `$ultimate-qa-architecture Trace the request approval journey from UI through persistence. Distinguish confirmed defects from maintainability risks.` | Expect source-linked journey findings, evidence-supported dimension scores, and a risk/dependency-ordered repair recommendation. Unassessed dimensions remain blank; the review does not refactor the application. |
| [ultimate-qa-browser](../packs/ultimate-qa/skills/ultimate-qa-browser/README.md) | `$ultimate-qa-browser Exercise request creation on local staging with the provided test roles. Cover validation, permission denial and narrow layouts.` | Expect journey results with URL, role, steps, expected/observed behavior and available screenshots/traces. Pending navigation is awaited; missing browser/runtime access is a coverage limit. Application fixes or new regression tests require implementation authorization. |
| [ultimate-qa-client](../packs/ultimate-qa/skills/ultimate-qa-client/README.md) | `$ultimate-qa-client prepare` | Use prepare explicitly for client artifacts from a completed audit/plan. Further operations record actual intake, decisions or implemented results. |
| [ultimate-qa-environment](../packs/ultimate-qa/skills/ultimate-qa-environment/README.md) | `$ultimate-qa-environment Check this application's documented Docker stack and database readiness. Report required setup before making environment changes.` | Expect ordered checks of Docker/Compose, service and database readiness, and app health, with concrete setup blockers. The example request stops before environment changes. Service starts require an authorized safe target; missing Docker does not prove an application defect. |
| [ultimate-qa-performance](../packs/ultimate-qa/skills/ultimate-qa-performance/README.md) | `$ultimate-qa-performance Measure the search workflow against its baseline using the existing benchmark and disposable seeded data.` | Expect reproducible workload/baseline measurements with latency, throughput, errors and resource limits, followed by evidence-ranked slow-path findings. Use disposable data; overload tests need the kit's separate safety gate and no fix is implied. |
| [ultimate-qa-security](../packs/ultimate-qa/skills/ultimate-qa-security/README.md) | `$ultimate-qa-security Review download authorization and tenant isolation using synthetic records and the existing security tests.` | Expect role/entrypoint findings with prerequisites, safe reproduction, observed/expected behavior and redacted evidence. Use synthetic data; active/destructive checks require the isolated environment and restore gate. This review does not implement fixes or authorize production testing. |

## Additional operations and continuation

| Skill/workflow | Supported operations and defaults | Resume, output and stopping rules |
|---|---|---|
| Report Builder | `scan [scope]`, `plan <scope> --detail mid`, `build <scope> --detail detailed`, `verify <scope>`, `help`. Bare defaults to scan; omitted detail defaults to mid. | Scan/plan are read-only unless a saved artifact is requested. Build includes discovery for its authorized scope. Verify reports gaps without automatically fixing them. |
| System Settings | `scan [scope]`, `plan [scope]`, `build <scope>`, `verify [scope]`, `help`. Bare defaults to scan. | The result can be create, extend, no new settings needed, or insufficient evidence. Scan/plan do not start implementation. |
| UI/UX suite, all four entrypoints | `run`, repeated `--page <selector>`, `--auto`, `continue <run-folder>`, `verify <run-folder>`, `help`. Main entrypoint also supports `--focus ui` or `--focus ux`; default is both. | Run/bare saves the proposal and stops. Proposal approval permits sketches; design approval permits edits. Continue uses the actual saved run and valid approvals; generic continuation is not approval. Outputs normally live under `.ui-ux/runs/`. Verify adds no fixes. |
| Deep Critique | `full`, `review`, `roast`, `question`, `rate`, `compare`, `help`. Bare means full on the established subject. Modes can combine; order/duplicates are normalized. | Help has precedence and creates no report. Question mode interviews before assessment. Reports normally live under `.deep-critique/`; a chat-only request suppresses persistence. Continue the same unfinished question session in context; a fresh invocation creates a new run. |
| Prompt Intake | Supply the task after the name; ask for questions only when implementation is not wanted. Bare uses the clearly pending task or asks for one. | Saves `.prompt-intake/questions-vNNN.md`. Answer the active file/menu, then reply `continue`, `answered` or `done`. These reread the active file and do not choose defaults. A new intake creates a new version; required answers precede dependent work. |
| Table UX Review | A natural-language audit request reviews; explicitly request audit and fix to authorize selected changes. | Returns table inventory, decisions and evidence. It does not invent missing detail routes or turn an audit into implementation automatically. |
| Ultimate QA core | `run [--client]`, `initialize`, `audit [scope]`, `plan`, `status`, `next-version`. Use run explicitly. | State/evidence live in application `qa-findings/`. Status is read-only. Repeat the original run to resume after a blocker. Next-version reconciles evidence and preserves history; a repeated completed run does not silently create a new version. |
| Ultimate QA Client | `prepare`, `intake`, `decisions`, `report`, `next-version`. Use the operation explicitly. | Client output lives under the active version's `client/`. Report requires actual separately authorized implementation evidence. Decisions remain pending until supplied; no operation sends documents or approves its own proposals. |

Examples of continuation are agent-chat requests, with placeholders to replace:

```text
$ultimate-ui-ux continue <run-folder> I approve the selected findings for sketches.
$ultimate-ui-ux continue <run-folder> I approve the current design for implementation.
$ultimate-ui-ux verify <run-folder>
$ultimate-ui-ux continue <run-folder> --auto
$ultimate-qa status
$deep-critique roast rate
```

For an active Prompt Intake, answer the actual questions before replying:

```text
continue
```

Do not copy a continuation example as approval unless it expresses your real decision for the identified run.

The main UI/UX entrypoint's `continue <run-folder> --auto` authorizes remaining work only for that run's recorded scope, with its artifacts preserved. It does not approve a different run or expanded page selection.

## When a run cannot proceed

- **Skill unavailable:** install/update the selected copy using the installer that owns it, then refresh the session. A source change does not update existing profile/project installations.
- **Target or input unclear:** supply the application path, subject, scope and actual run/report paths. Do not run an audit against the skill's own folder by accident.
- **Material decision unresolved:** resolve the business, data or sharing choice; independent authorized work can continue. No mode treats silence as approval.
- **Tools/services/accounts unavailable:** provide the prerequisite or accept explicitly limited source-only results. A passing install/build is not browser, provider, device, worker/scheduler or production proof.
- **Interrupted or stale work:** use that skill's actual saved state and continuation contract. Recheck source/evidence before resuming; do not restart a completed immutable report or approve a later stage implicitly.
- **No justified change:** preserve already-correct behavior and explain the evidence. Automation is not a requirement to manufacture features or findings.

For installation, see [the collection guide](../INSTALL.md). For choosing workflow owners, see [skill workflows](SKILL_WORKFLOWS.md). Maintainers must follow the [usage documentation contract](../CONTRIBUTING.md#document-skill-commands-and-automation).
