# Collection verification

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
