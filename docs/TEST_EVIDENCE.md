# Collection verification

## UI and UX reviews, previews and autonomous improvements, 2026-10-31

Added `ultimate-ui-ux`, `ultimate-ui` and `ultimate-ux`. The main entrypoint contains both disciplines; each focused entrypoint also works after a one-skill install. Shared resources have one maintained owner in `ultimate-ui-ux` and checked distribution copies for portable standalone installation. The collection now contains 28 Developer Skills and 37 total skills; the four Essential defaults are unchanged.

The instructions cover all-pages or selected-page inventories, UI-only/UX-only boundaries, deliberate choices among sections/tabs/disclosure/routes, source/runtime evidence limits, saved proposals, before/after wireframes, continuation and revision-bound approval records. Default execution stops before sketches and again before application edits. Explicit auto mode completes review, design, implementation and verification without skill approval pauses while retaining selected scope and platform permissions. These are agent instructions, not a separate command parser or approval enforcement service.

Selected Taste-Skill and UI UX Pro Max excerpts/data retain their MIT licenses. Selected Anthropic frontend-design excerpts retain Apache-2.0. Pinned revisions, original and local SHA256 hashes, excerpt boundaries and complete licenses are bundled in every standalone payload. Mixed provenance requires a bundled notice file in the catalog validator. This does not resolve the existing collection/local-material license decision.

Executed on Windows with Python 3.14.7:

- Collection suite: 85 tests passed; QA-pack suite: 10 tests passed. The collection includes six new tests for independent installations to both agents, installed runtime reference containment, pinned source/license integrity, required notices, read-only synchronization checks and preservation of unexpected resources.
- Windows sandbox execution initially blocked the installer's atomic journal rename with `WinError 5`. The focused six tests and full suites passed outside the sandbox from a C: working directory, using absolute source-test paths. This is the existing fixture/environment limitation, not product runtime proof.
- Public-contract checks passed, including 37 shipping-only entrypoints, complete/unique catalog categories and valid README/pack links.
- Cached external `skills@1.7.4` discovered all 37 skills. Each of the three new entrypoints installed alone to both agents in separate disposable projects; full Developer Skills installation copied 28 per agent. Every installed file hash matched source. No global or real application install was used.
- `node tests/ui_ux_preview.cjs <existing-playwright-core-path> <existing-browser-executable>` passed against headless Edge. It exercised all panels, manual arrow/Enter/Space activation, Home/End/wraparound, selected-state/panel consistency, roving focus and tablist re-entry. No horizontal page overflow occurred at 1280, 390 or 320 pixels. No script errors or HTTP requests occurred. Wide and narrow screenshots were visually inspected; they show the labeled illustrative starter, not a target application.
- All 90 local Markdown links in the suite's 33 Markdown files resolved. Runtime references stayed inside each copied skill. Resource synchronization, portable frontmatter/metadata, payload manifests, repeatable archive checks and whitespace validation passed.

The optional skill-creator validator could not import host PyYAML; no dependency was installed. The repository's portable validation and real installer/package checks provide structural evidence. The new compatible_agents lists remain empty because native agent protocol discovery was not run.

No independent model-adherence trial, real-application redesign, user acceptance, screen-reader trial, global skill installation, remote publication or production behavior was verified. Approval decisions and review quality remain model-executed instructions; packaging and the sample interaction tests do not prove every future design decision. See [external CLI evidence](NPX_COMPATIBILITY.md#ui-and-ux-suite-2026-10-31).

## Report Creator, 2026-10-31

Added one portable report-creator skill with scan, plan, build, verify, and help commands. Bare invocation scans; mid and detailed select report content without weakening discovery, access, document, or lifecycle requirements.

The integrated source contains 25 Developer Skills and 34 skills across both packs. It preserves the table-ux-review payload from commit 25d43d2 unchanged; earlier evidence below retains its original snapshot counts.

Four self-contained references cover discovery/metric semantics, PDF/Excel design, access/generated-file retention, and verification. They specify feature necessity classifications, full-population categorical counts, status/type palettes, effective filter disclosure, separate PDF front matter, usable workbook sheets, role/tenant/field restrictions, permitted cross-user downloads, a dedicated Generated Reports page, and configurable 24-hour availability from successful completion. Direct builds load the metric reference without requiring a prior planning command. Essential selections remain unchanged.

Executed on Windows with Python 3.14.7 in an isolated C: worktree, avoiding the pre-existing cross-drive fixture limitation:

- Baseline and updated public-contract checks passed all 5 tests.
- Final collection suite passed all 79 tests: `python -B -m unittest discover -s tests -v`.
- QA-pack suite passed all 10 tests: `python -B -m unittest discover -s packs/ultimate-qa/tests -v`.
- The added selected-install regression copies report-creator alone to both agents, compares every file hash, and resolves the installed instruction references within each copied skill.
- Cached external CLI discovery found all 34 shipping skills. Selected and full 25-skill developer-pack copies matched source hashes for both agents, with all references accessible. See [external CLI evidence](NPX_COMPATIBILITY.md#report-creator-2026-10-31).
- All 11 local Markdown links in the new skill's 6 Markdown files resolved. Portable metadata and all seven payload files passed manifest/catalog checks. Whitespace checks passed.

The optional skill-creator quick validator could not import host PyYAML; no dependency was installed. Repository portable validation, manifests, installer tests, and public-contract checks provide structural proof. The new compatible_agents list remains empty because native agent discovery was not run.

These results establish packaging and local installation integrity. No model adherence trial, target-application change, rendered PDF/workbook, browser journey, worker/scheduler run, global installation, remote publication, or production behavior was verified. Application behavior remains instructions to be tested in each target project.

## Table navigation and row-action review, 2026-10-31

Added table-ux-review as a self-contained Developer Skills review with a usage README, schema-1 metadata and three payload-manifest entries. The pack now contains 24 skills, with 33 across the collection. The skill inventories table instances and shared owners, decides detail navigation per workflow, reviews more than three visible actions without imposing a hard cap, and preserves role access, nested controls, selection, editing and bulk workflows. Review remains the default; an explicit audit-and-fix request authorizes bounded implementation without a second approval step.

Executed verification on Python 3.14.7:

- All 5 focused public-contract checks passed, including complete categorized catalog coverage and shipping-only discovery.
- All 78 collection tests and all 10 QA-pack tests passed outside the Windows sandbox from a C: temporary working directory with absolute source-test paths. Initial sandbox runs failed on temporary Git configuration and atomic fixture writes; those failures did not recur outside the sandbox.
- Existing packaging checks validated complete payload manifests, exact archive checksums, included READMEs and repeatable ZIP bytes. Installer lifecycle checks now verify 33 skills per agent and 66 owned destinations across both packs.
- Offline cached skills@1.7.4 discovery listed all 33 shipping skills, including table-ux-review, and excluded the sample fixture. Selected table-ux-review and full 24-skill Developer Skills installs ran in separate disposable projects for Codex and Claude Code; every copied payload file matched its source hash. No global installation or remote source was used.
- The optional skill-creator quick validator could not import PyYAML. Repository portable-frontmatter, metadata, catalog and integrity validation passed; no dependency was installed for the optional helper.

Native Codex/Claude protocol discovery for this new skill, model adherence, and application/browser trials remain unverified. Its compatible_agents metadata is empty rather than inheriting older skills' discovery evidence. No application table behavior was changed by this addition.

## Optional implementation and change-safety helpers, 2026-10-28

The Developer Skills pack now contains 23 skills, with 32 across both packs. Six optional helpers are categorized under Implementation and Change Safety: investigate-first, lean-build, surgical-patch, safe-refactor, migration and verify-and-stop. Each has self-contained instructions, a usage and installation README, task-specific metadata and payload hashes. The Essential selection is unchanged.

The installed reference folders did not include an authorship or license record. Their files and UI metadata were not imported. The new local instruction bodies implement the six workflow purposes without profile-specific Core dependencies; metadata records local authorship and the existing UNDECIDED license status. This update grants no redistribution license.

Native discovery passed for all 23 skills in Codex CLI 0.165.0 and Claude Code 2.1.299 using local installer copies, disposable projects, isolated configuration homes and initialization/skill-list requests only. No model prompt or real-profile installation was performed. The temporary-home Codex PATH-helper warning did not prevent discovery. Compatibility metadata records these observed project-discovery adapters, not model adherence.

The optional skill-creator validator was attempted but could not import host PyYAML. The repository's portable catalog, metadata, manifest and discovery checks are the available validation path; no dependency was installed to enable the optional validator.

Final verification for this addition:

- Python 3.14: all 78 collection tests and 10 QA-pack tests passed. The collection suite used its documented C: working-directory workaround and absolute source-test path outside the sandbox. The installation/ownership fixtures now verify 32 skills per agent and 64 total owned destinations across both packs.
- PhasePilot: 16 current-provider tests passed on each of Python 3.11 and 3.14. Coverage includes full-pack setup for both agents, explicit helper sync and read-only preview, unchanged Essential defaults, no automatic domain-based helper routing, source drift, ownership protection, interrupted recovery and mixed builtin/custom transactions.
- Full-pack setup initially reproduced Windows error 206 on both runtimes because 46 installation rows were serialized onto the provider child command line. The narrow private transport correction sends argument data over standard input and reconstructs the existing script argv. Isolated imports, reviewed provider identity, a fixed executable/script, shell=False and the timeout remain in place. The new actual-child regression round-trips a 70,000-character argument, quotes, newlines, Unicode, empty strings and flag-like data. The full-pack integration regression then passed on both runtimes.
- The full private suite and six legacy-provider cases were not run because the required sibling `skills` checkout is absent. Current-provider results do not establish legacy migration or real-project acceptance.
- Cached `skills@1.7.4` local discovery listed all 32 shipping skills and excluded the sample fixture. A selected lean-build install and the full 23-skill developer pack copied to both agents in separate disposable projects; every copied payload hash matched source. No network source, global scope or model prompt was used.

## Developer skill discovery and workflow guidance, 2026-10-28

The workflow guide separates purpose categories, suggested standalone order and PhasePilot's existing engine-owned records and installed-capability routing. Essential selections remain the same four skills; optional selection does not authorize installation or execution.

Native project discovery passed for all 17 Developer Skills in Codex CLI 0.165.0 and Claude Code 2.1.299, including prompt-intake and deep-critique. A temporary adaptation of the existing PhasePilot discovery probe installed the complete local pack into a disposable project through the collection installer. It used separate temporary Codex/Claude homes, disabled nonessential traffic, a loopback-only Claude provider and only initialization/skill-list protocol requests. No model prompt was submitted and no real-profile skill files were changed. Codex reported that PATH helper creation was refused under the temporary home; skill discovery still returned all expected names.

The two skills' compatible_agents metadata now records both discovered agents. This establishes native project availability only, not observed model use, user-scope discovery, production behavior or future runtime compatibility. Earlier unverified compatibility notes below describe the prior snapshots.

Verification against the current source:

- Python 3.14: 78 collection tests and 10 QA-pack tests passed. The collection suite ran outside the sandbox from C: with an absolute source-test path, using the documented same-drive fixture workaround.
- PhasePilot: four focused integration checks passed on both Python 3.11 and 3.14. They verify full-pack installation for both agents, optional prompt-intake/deep-critique sync with a read-only preview and unchanged Essential defaults, existing Essential setup, and missing-provider refusal without fallback.
- The focused private methods are `test_all_bundle_uses_pack_payload_and_missing_pack_is_not_flat_fallback`, `test_new_optional_skills_sync_without_expanding_essential_defaults`, `test_new_setup_uses_pack_transactions_and_verified_current_bytes` and `test_unavailable_explicit_collection_never_uses_legacy` in `tests.test_provider_transition.ProviderTransitionTests`.
- The full private suite was not run: its legacy-provider fixtures require the sibling `skills` checkout, which is absent here. Current-pack fixture success is not legacy compatibility proof or a real-project update.
- The existing PhasePilot `.gitignore` edit retained SHA256 `bfa4f60a22da6ad2b206f045c123187a08b9d191180621975d31aee18aebdf51`. No default selections, application skill installations, private runtime logic or approval rules were changed.

## Versioned Prompt Intake and unfinished work, 2026-10-28

Prompt Intake now records each identifiable intake in a flat `.prompt-intake/questions-vNNN.md` sequence. The instructions distinguish answer state from work state, carry relevant unfinished items into later versions of the same task, preserve origins and earlier files, accept recommended or custom answers, and provide file-specific continuation hints. `Needs confirmation` carries forward even when earlier work was marked `Implemented`. Versioning and state reconciliation are agent instructions; no background interceptor or separate state engine is shipped.

Final source verification on Windows with Python 3.14:

- `python -B -m unittest discover -s tests -v`: 77 tests passed.
- `python -B -m unittest discover -s packs/ultimate-qa/tests -v`: 10 tests passed.
- The four existing public-contract tests also passed separately. They check public source, metadata and shipping discovery boundaries; they do not exercise the conversational state transitions.
- Both suites ran from a temporary working directory on the same drive as their fixtures, using absolute source paths. This avoids an existing cross-drive relative-path test limitation. Execution outside the sandbox was required for temporary Git and atomic transaction writes.
- Skill identity, metadata, payload manifests and ZIP packaging were validated through the repository suites. Whitespace checks passed before staging; the staged check is required before committing.

The host accepted a native question-tool trial request. No submitted answer was observed at the time of this record. This establishes request acceptance only. Visible menu rendering, recommended-option preselection, custom-answer submission and the complete versioned-file, carry-forward and continuation workflow remain unverified end to end. Source inspection and installation tests do not prove model adherence. The optional skill-creator validator remains unavailable because PyYAML is not installed.

No real-profile skill installation, Git ignore change, push or publication is part of this update. The task-folder proposal was superseded by flat versioned question files.

## Combined Deep Critique modes and report storage, 2026-10-26

Deep Critique now combines modes into one assessment and saves categorized timestamp/unique-ID runs under the target workspace's `.deep-critique/`. Two self-contained standard-library helper modules own mode normalization, root resolution, ignore-file preparation, OS locking, immutable publication and ordered question transcripts. A completion record is published last; identical publication can recover an interrupted completion without replacing the report.

Final Windows verification:

- `py -3.11 -B -m unittest discover -s tests -q`: 77 tests passed.
- `py -3.14 -B -m unittest discover -s tests -q`: 77 tests passed.
- `py -3.11 -B -m unittest discover -s packs/ultimate-qa/tests -q`: 10 tests passed.
- The collection suites include 31 mode/storage tests covering canonical combinations, help without writes, Git and non-Git roots, unique reruns, collisions, preserved BOM/CRLF, negated and partial ignore rules, tracked and unowned output, hard links and junctions, malformed metadata, idempotent completion, ordered transcripts, six concurrent processes, initialization races and actual process death inside hard-link publication.
- An independent source review reproduced storage defects before repair, then confirmed their regression cases pass: actual output exclusion, interrupted publication, preservation before ownership/tracking refusal, and concurrent initialization. A generic gardening-workshop `roast rate` assessment produced one saved report with a detailed scorecard, actionable findings, counterarguments and uncertainty in an explicitly selected isolated non-Git workspace.
- Cached `skills@1.7.4` local discovery and isolated selected/full-pack installations copied matching payloads to both agents. Both copied helpers normalized modes; the installed helper reserved and published an actual report. See [CLI evidence](NPX_COMPATIBILITY.md#combined-modes-and-storage-follow-up-2026-10-26).

Payload manifests and installation documentation include both helper modules and the storage reference. No third-party import, new environment setting, database hook, migration, real-profile install, commit or push is required or performed. Saving requires Python 3.11+, a writable target root, and atomic hard-link support; Git is used when present. Chat assessment remains available when persistence is unavailable. Native agent discovery, all possible model responses, other operating systems and power-loss durability remain outside this local proof. Earlier quick-validator/PyYAML limitations still apply; portable identity and integrity checks pass in the collection suites.

## Deep Critique addition, 2026-10-26

Added the independent deep-critique skill to Developer Skills: 16 developer skills and 25 shipping skills across the collection. Bare invocation uses the current subject and runs full assessment without a mode menu. Optional review, roast, question, rate, compare and help modes remain available. Ratings adapt to the subject, disclose the overall calculation and uncertainty, and withhold an overall score when essential evidence is unresolved.

Verification from the collection root:

- `py -3.11 -B -m unittest discover -s tests -q`: 46 tests passed. Catalog identity, payload hashes, complete-pack installation, lifecycle records, discovery boundaries and reproducible ZIP payloads cover the new skill.
- `py -3.11 -B -m unittest discover -s packs/ultimate-qa/tests -q`: 10 tests passed.
- A separate temporary ZIP build and extraction passed manifest validation for all 16 developer and 9 QA skill payloads. The extracted deep-critique instructions matched the working-tree bytes; existing `dist/` artifacts were preserved.
- Cached `skills@1.7.4` local repository listing found deep-critique and excluded the non-shipping fixture. Isolated single-skill and complete developer-pack installs copied matching payload bytes for Codex and Claude Code; see [external CLI evidence](NPX_COMPATIBILITY.md#deep-critique-local-addition-2026-10-26).
- An independent behavioral evaluation used a non-software neighborhood book-exchange proposal with bare invocation, help without a subject, interactive questioning about a gardening guide, and comparison without supplied alternatives. Responses respectively completed a scored full assessment, listed modes without reviewing, asked one question, and requested the missing alternatives. These four examples support those observed behaviors, not universal model adherence.

The skill-creator quick validator could not start because PyYAML is absent from the available Python environments. The repository's stricter portable-frontmatter, TOML metadata and full manifest validators passed through the collection suite. No dependency was installed to run the optional helper.

No new runtime import, environment variable, database hook, migration, installer behavior or real-profile installation was introduced. Native agent discovery for deep-critique remains unverified; its compatibility metadata is empty. Earlier native compatibility records cover the original 15 developer skills only.

## Documentation and external installation update, 2026-10-26

All 24 shipping skills now include installation and usage READMEs. The main README and pack guides link to them and to contribution guidance. ZIP packaging includes `CONTRIBUTING.md`, and manifests include every new skill README. Original SKILL.md bodies, metadata, QA runtime scripts and templates remain unchanged. The sample fixture is named `SKILL.md.example` to exclude it from external discovery.

Python 3.11 verification: `py -3.11 -B -m unittest discover -s tests -q` passed 46 tests; `py -3.11 -B -m unittest discover -s packs/ultimate-qa/tests -q` passed 10 tests. The new discovery boundary check excludes generated trees ignored by the external CLI. The packaging suite checks that contribution instructions and all skill READMEs ship in the ZIP. [External CLI evidence](NPX_COMPATIBILITY.md) records local and remote installation checks and their limits.

No new environment variable, third-party Python import, database hook or migration was introduced. The optional npx route requires Node.js 22.20+ and npm, and QA's external installation uses its existing `ULTIMATE_QA_KIT` setting. The recorded Python installer still needs no environment setting.

## Original collection verification, 2026-10-25

Local Windows verification, 2026-10-25. All application/profile destinations used isolated UUID fixture folders. No real user skill installation, PhasePilot integration, GitHub push or publication was performed.

| Check | Result |
|---|---|
| Original Developer Skills baseline, Python 3.11 | 27 tests passed before collection edits |
| Collection suite, Python 3.11 | 45 tests passed, exit 0 |
| Collection suite, Python 3.14 | 45 tests passed, exit 0 |
| QA pack suite, Python 3.11 | 10 tests passed, exit 0 |
| QA pack suite, Python 3.14 | 10 tests passed, exit 0 |
| Original skill payload preservation | 41 files across 24 skills byte-identical to their original sources |
| QA template/helper preservation | Both template directories and qa_preflight.py/md_to_docx.py byte-identical |
| Developer payload manifest | Byte-identical to the original source |
| Configuration/import review | Standard library only for the new lifecycle/build code; no new environment setting, database hook, migration or package |

Commands from the collection root:

```powershell
py -3.11 -B -m unittest discover -s tests -q
py -3.14 -B -m unittest discover -s tests -q
py -3.11 -B -m unittest discover -s packs/ultimate-qa/tests -q
py -3.14 -B -m unittest discover -s packs/ultimate-qa/tests -q
```

The collection suite retains the original installer regression coverage and adds both complete packs/both agents, isolated user installs, QA kit pointers, Markdown ownership/adoption, selective and all-pack removal, before/after hashes, direct retained-tree paths, edited/unmanaged-copy protection, history integrity/ownership chains, history-write rollback, abrupt-exit removal recovery, committed-archive cleanup recovery, support-file tampering and pack entry points. Packaging checks verify all packaged payload hashes, required QA templates/helpers, unique skill names and repeatable ZIP bytes.

An early QA install check exposed Windows filename ordering in generated-file fingerprints. The shared fingerprint now sorts exact relative filenames; its regression check is platform-independent. QA state test fixtures use inherited ACLs and scoped read-only Git-object cleanup; the production QA state helper is unchanged.

The downloadable artifact and checksum are generated under `dist/`. Fresh-extraction verification, archive hash and command results are recorded separately in `dist/VERIFICATION.md` after building the final snapshot. This avoids embedding the ZIP's own checksum into its payload.

The source worktrees remain intact. The new checkout retains Developer Skills baseline history and the committed collection changes. The original `Development/skills` provider remains available to PhasePilot.

Native agent discovery, model adherence, real host-profile installation, live application QA, provider/device behavior and power-loss durability are not established by these filesystem/fixture tests. Existing historical compatibility documents keep their original scope. GitHub hosting, license selection, immutable release tags and external publisher authentication remain unresolved.
