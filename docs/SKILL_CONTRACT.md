# Public skill and installer interface baseline

Schema version: 1. Phase 01 defines contracts and fixtures only.
No skill in `tests/fixtures/` is a shipping catalog entry or installation source.

## Skill layout and metadata

Each public skill lives at `skills/<name>/SKILL.md`.
Names use lowercase ASCII words/digits separated by single hyphens; no prefix is added.
Directory and frontmatter `name` must match. Frontmatter includes a useful scalar `description`.
Optional metadata belongs in a separate `metadata.toml` sidecar to keep portable frontmatter minimal.
The sidecar fields are `schema_version`, `name`, `version`, `capabilities`, `compatible_agents`, and `license_status`.
Version is a release version string; capabilities are a nonempty list; compatible agents list tested adapters only.
An empty compatibility list means not verified, not universal support.
`license_status` is `UNDECIDED` until an owner chooses a license; do not infer a legal grant.
Source revision/digest and verified license identifier may be added only with actual verification evidence.
Instructions define inputs, outputs, limits and evidence expectations and operate independently of any private runner.
No private imports, required private tracking folder, secrets, global writes or automatic hook execution.

## Initial catalog names

`plan-review`, `blocker-check`, `phase-handoff`, `completion-check`, `environment-doctor`, `phase-runner`, `version-manager`, `architecture-review`, `frontend-review`, `backend-review`, `database-review`, `security-privacy-review`, `business-rules-review`, `delivery-readiness`, `critical-review`.

These 15 entries are Phase 02 implementation targets, not implemented skills.
Custom skills remain where discovered; optional custom prefixes never prove ownership.
Installing a skill does not prove that an agent invoked it.

## Standalone installer contract for Phase 02

Owner: future `tools/install_skills.py` in this public repository; use Python standard library where sufficient.
Inputs: explicitly selected local source, selected skill names and agent destination; support project/user scope, dry-run and cancellation.
Default scope is project. User-global scope requires an explicit request.
Preview exact paths and copies before mutation. No unapproved overwrite, download, shell hook or automatic private setup.
Resolve and contain source/destination paths; reject escaping symlinks, traversal and malformed names.
Copy through verified staging, preserve existing data, offer approved backup on collisions, and recover interrupted writes.
Repeat installation is idempotent. One-skill installation changes only that skill's approved destination.
Offline installation requires local assets and never uses a remote fallback.
Codex project destination is `.agents/skills/<name>`; Claude project destination is `.claude/skills/<name>`.
Actual agent discovery and exact installer flags remain Phase 02 evidence gates.

## Acceptance ownership

Phase 02 owns standalone tests PUB-01–PUB-10: metadata, one-skill/both-agent install, dry-run/cancel, collisions, traversal/symlink rejection, offline copies, checksum mismatch, and no private runtime dependency.
Phase 01 tests only the metadata fixture and this repository's independence.
Publication, license, release checksums and remote configuration require later decisions and are not implied by creating a local repository.
