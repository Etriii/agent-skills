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

**Improve selected UI/UX or explicitly all pages:**

```text
$ultimate-ui-ux Improve /orders and verify the changes.
$ultimate-ui-ux Improve all UI and UX in "D:\My App".
$ultimate-ui-ux Improve "D:\My App\src\pages\Orders.vue".
$ultimate-ui-ux Improve https://localhost:3000/orders using the source in "D:\My App".
```

Each line is independent. Replace example application/page paths, routes and URLs. All four UI/UX entrypoints inspect, select justified improvements, implement and verify by default, without routine skill approval pauses or formal review/previews. An absolute application directory identifies the project; the task supplies page scope or explicitly all pages. Absolute page files select affected pages; relative paths resolve against the identified application. URL-only access can support inspection but needs matching editable source before source changes. Unclear targets/scope and unresolved selectors never become all-pages redesigns. Improve-all covers discovered pages of the identified app, with compact changed/kept/deferred coverage and gaps, not sibling projects or external sites.

**Request review-only or optional preview approval:**

```text
$ultimate-ui-ux Review /orders only. Do not edit.
$ultimate-ui-ux Improve /orders. Include before/after previews.
$ultimate-ui-ux Improve /orders. Show previews and wait for my approval before editing.
```

Review-only stops at recommendations without edits or automatic previews. Requested previews precede implementation; approval pauses are added only when requested. Preview-only never authorizes edits. Platform permissions and material unresolved decisions still apply. Correct pages stay unchanged. Bare invocation/`run` uses established scope or asks for missing input; it no longer silently selects all pages or adds proposal/design gates. Existing gated runs preserve their recorded checkpoints.

Default runs improve and verify with brief chat results: no `.ui-ux/` or `.uiux/` files, logs, saved captures, reports, run metadata or related `.gitignore` changes. Necessary checks still apply; routine capture passes and optional evidence work do not. Saving requires an explicit request, requested file-based previews or a compatibility/saved run. Review-only returns findings in chat unless saving is requested. A no-files/chat-only constraint suppresses persistence even with another mode. Existing `--page`, `--focus`, `--auto`, `--skip-review`, continuation and verification remain supported; see combinations below. Other skills retain their own defaults and approval contracts.

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

## Supported command stacks

A stack combines supported options or modes in one agent-chat request. It does not chain arbitrary subcommands or automatically invoke another skill. Each line below is independent. Replace routes, file paths, subjects and report scopes with actual inputs; Claude Code uses `/skill-name` in place of `$skill-name`.

| Skill | Copyable combination | Effect |
|---|---|---|
| UI/UX default | `$ultimate-ui-ux run --focus ux --page /orders --page /checkout` | Inspect, improve and verify selected journeys without formal review/previews. |
| UI/UX compatibility full review | `$ultimate-ui-ux run --focus ux --page /orders --page /checkout --auto` | Review selected journeys, preview, implement and verify without skill approval pauses. |
| UI/UX direct fix | `$ultimate-ui-ux run --focus ui --page /orders --skip-review Fix mobile filter wrapping.` | Inspect affected owners, implement that visual fix and verify; no full review or previews. |
| UI-only | `$ultimate-ui run --page /orders --page /settings` | Inspect, improve and verify only visual presentation on those pages, without formal review/previews. |
| UX-only | `$ultimate-ux run --page /checkout --skip-review Preserve entered values after validation errors.` | Apply that usability fix while preserving visual identity. |
| Mobile | `$ultimate-mobile run --page /orders --skip-review Keep filter controls within the phone viewport.` | Apply that responsive fix and check desktop regressions. |
| Deep Critique | `$deep-critique roast rate docs/design.md` | One sharp assessment with detailed scoring; mode order/duplicates do not multiply reports. |
| Deep Critique alternatives | `$deep-critique review compare Proposal A vs Proposal B` | Review the supplied alternatives under common criteria; replace both example subjects. |
| Report Builder | `$report-builder build sales reports --detail detailed` | Discover/implement the named reporting scope with detailed content and verification. |
| Ultimate QA | `$ultimate-qa run --client` | Intake, audit, plan and client preparation when prerequisites exist; no implementation or sending. |

Natural-language UI/UX requests are recommended first. Compatibility `--auto` still includes a formal review and previews; it is not required for default improvements. The concrete-fix `--skip-review` combines with repeated `--page` and the main skill's `--focus`. Adding `--auto` is accepted but redundant; it does not restore audit or wireframes. Shortcut skills reject conflicting focus options. Explicit review-only/preview-only constraints never authorize implementation.

Do not stack `scan plan build` on Report Builder or System Settings; choose the operation with its own scope/options. Their `build` operation already includes inspection. Natural-language review skills take a scoped sentence rather than invented `run`, `--auto` or `--skip-review` flags. Deep Critique explicitly supports multiple modes; `help` takes precedence and creates no assessment. Approval and continuation operations remain separate where the skill requires them.

New UI/UX previews use one run-local `previews/index.html` linking feature folders such as `orders/` and `checkout/`, with preserved comparison revisions/assets. Existing run links remain valid. Default improvements and direct fixes omit previews unless requested. See the [preview layout](../packs/developer-skills/skills/ultimate-ui-ux/references/preview-and-verify.md#feature-based-preview-folder).

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
| [ultimate-mobile](../packs/developer-skills/skills/ultimate-mobile/README.md) | `$ultimate-mobile Improve all mobile web UI and UX in "D:\My App".` | Inspect, improve and verify mobile pages, with desktop regression checks. Formal review/previews are optional; replace the absolute application path. |
| [ultimate-ui](../packs/developer-skills/skills/ultimate-ui/README.md) | `$ultimate-ui Improve /orders and verify the changes.` | Inspect, improve and verify UI-only presentation in the established app. Formal review/previews are optional. |
| [ultimate-ui-ux](../packs/developer-skills/skills/ultimate-ui-ux/README.md) | `$ultimate-ui-ux Improve all UI and UX in "D:\My App".` | Inspect all discovered app pages, implement justified improvements and verify; keep correct pages and record coverage/gaps. Replace the absolute application path. |
| [ultimate-ux](../packs/developer-skills/skills/ultimate-ux/README.md) | `$ultimate-ux Review /checkout only. Do not edit.` | Optional UX-only review with findings and no edits. An improvement request instead implements and verifies by default. |
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
| UI/UX suite, all four entrypoints | Natural-language improve/review/preview requests; `run`, repeated `--page <selector>`, compatibility `--auto`, `run --skip-review <task>`, `continue <run-folder>`, `verify <run-folder>`, `help`. Main also supports `--focus ui` or `--focus ux`; default both. | Default improves/verifies established scope with chat results and no generated run files. Improve-all explicitly covers the identified app. Review-only returns chat findings; preview-only stops without edits. Requested preview approval pauses before implementation. Continue preserves recorded scope/gates, including older runs. Verify adds no fixes. Only opted-in outputs live under `.ui-ux/runs/`. |
| Deep Critique | `full`, `review`, `roast`, `question`, `rate`, `compare`, `help`. Bare means full on the established subject. Modes can combine; order/duplicates are normalized. | Help has precedence and creates no report. Question mode interviews before assessment. Reports normally live under `.deep-critique/`; a chat-only request suppresses persistence. Continue the same unfinished question session in context; a fresh invocation creates a new run. |
| Prompt Intake | Supply the task after the name; ask for questions only when implementation is not wanted. Bare uses the clearly pending task or asks for one. | Saves `.prompt-intake/YYYYMMDDTHHMMSSZ-<unique-id>/questions-vNNN.md` after verifying Git exclusion when applicable. Existing flat files resume in place. Answer the active file/menu, then reply `continue`, `answered` or `done`. These reread the active file and do not choose defaults. A new intake creates a new version; required answers precede dependent work. |
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
