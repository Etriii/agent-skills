# Portable skill and integrity standard

Each shipping skill is `skills/<name>/SKILL.md` plus `metadata.toml`. Names use lowercase ASCII letters/digits separated by single hyphens, at most 64 characters. Folder, frontmatter name and stable `skill_id` match. Frontmatter contains only name and a useful plain scalar description; instructions state inputs, outputs, evidence and limits without a private runtime dependency.

Metadata schema 1 fields are `skill_id`, `name`, `version` (three integer components), nonempty `capabilities`, `compatible_agents`, `license_status`, and `provenance`. Current content is version 0.1.0, locally authored, with license UNDECIDED. Compatible agent names record only verified discovery adapters. See `COMPATIBILITY.md`; an empty list means unverified. An approved license requires an explicit metadata/validator/documentation update and owner-selected license file before distribution.

`SHA256SUMS` lists lowercase file SHA256 plus two spaces and a repository-relative path. Every file in a selected skill must be listed exactly once and match; omitted or extra files fail. The installer never executes payload scripts. This release ships no payload scripts. Directory links, junctions, special files, traversal and duplicate manifest entries fail closed. `.gitattributes` fixes payload line endings to LF so archive and checkout bytes agree.

The displayed tree digest hashes sorted file digest/path records followed by sorted `dir  <relative-path>` records, all UTF-8 with LF. It includes empty directories to preserve custom additions. It is distinct from the manifest file's SHA256 and from Git revision IDs. Installation checks staged and installed tree digests against the manifest-verified source snapshot.

Each skill also includes a human-facing `README.md` with installation, invocation and prerequisites. It is part of the validated payload and must appear in `SHA256SUMS`. After an intentional skill edit, follow the collection [contribution guide](../../../CONTRIBUTING.md#refresh-integrity-manifests) to regenerate the selected pack's manifest from the collection root, then review the hashes and run the documented checks.

The validator intentionally supports this constrained portable frontmatter rather than general YAML. Tests exercise actual installation outcomes and integrity failures using only Python's standard library. Native discovery checks are optional environment proof, recorded separately. Never infer a publishing license or trusted source identity from a filename, prefix, checksum or synthetic fixture.
