# Collection verification

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
