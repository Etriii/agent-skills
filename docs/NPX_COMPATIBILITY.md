# External CLI compatibility evidence

## System Settings, 2026-10-31

Cached skills@1.7.4 ran through Node.js against local sources in disposable projects, with an isolated profile and telemetry disabled:

- Root discovery listed exactly 39 shipping skills, including system-settings; sample-review and report-creator were absent.
- Selected installation copied only system-settings for Codex and Claude Code. Every payload hash matched source, and both instruction references were accessible in each copy.
- A separate complete Developer Skills installation copied exactly 30 skills per agent. Every copied payload hash matched source, with both system-settings references accessible.

The changing commands used explicit agents, project scope, --copy and fixture-only -y. No remote source, downloads, global installation, real-profile change or target-application implementation was involved. These checks prove external discovery and copy integrity, not native agent discovery, model adherence, database behavior or browser interaction. Earlier entries retain their original snapshot counts.

## Report Builder rename, 2026-10-31

Cached skills@1.7.4 local discovery listed all 38 shipping skills with report-builder present and report-creator/sample-review absent. Selected report-builder and the complete 29-skill Developer Skills pack installed into separate disposable projects for Codex and Claude Code. Every copied payload hash matched source; all four instruction references resolved in each installed report-builder copy.

The check used an isolated profile, disabled telemetry, and local project copies only. No real-profile migration, global installation, remote source, native agent discovery, or model prompt was exercised. Earlier report-creator entries below retain their original names and snapshot evidence.

## Mobile review, 2026-10-31

Using cached `skills@1.7.4` directly through Node.js with telemetry disabled and local sources:

- Root discovery found exactly 38 shipping skills, including `ultimate-mobile`; vendored excerpts did not become extra entrypoints.
- A mobile-only install copied exactly one skill to each of Codex and Claude Code in a disposable project. All payload hashes matched, including its local mobile/UI/UX playbooks, notices/licenses and preview resources.
- A separate full Developer Skills copy installed exactly 29 skills per agent with every file matching source hashes.

Fixtures used explicit agents, `--copy` and fixture-only `-y`; no global scope, remote installation source or real application was used. These checks prove discovery/copy integrity, not native agent protocol discovery, model adherence, application redesign or mobile-device behavior.

## UI and UX suite, 2026-10-31

The cached `skills@1.7.4` CLI checked local source directly through Node.js with telemetry disabled and project-only copies in disposable directories.

- Collection discovery listed all 37 shipping skills, including `ultimate-ui-ux`, `ultimate-ui` and `ultimate-ux`. Renamed source excerpts did not become extra skills; sample-review remained excluded.
- Each new skill was installed alone in its own temporary project for Codex and Claude Code with `--copy`, explicit agents and fixture-only `-y`. Exactly the selected skill was present for each agent, and every copied file hash matched source.
- A separate complete Developer Skills copy contained exactly 28 skills per agent with all payload hashes matching, including local references, preview assets, third-party source records and licenses.

No remote installation source, global scope, real application install, model prompt or native agent protocol discovery was used. Downloads of pinned public reference material for authorship/license review are separate from these offline local-install checks. These checks establish external discovery and copy integrity, not approval adherence, design quality or target-application behavior. Earlier evidence retains its original counts.

## Report Creator, 2026-10-31

The cached `skills@1.7.4` CLI checked the local report-creator source in disposable projects with an isolated profile, telemetry disabled, and project copies only.

- Collection discovery listed all 34 shipping skills and excluded sample-review.
- Selected installation copied exactly report-creator for Codex and Claude Code. Every payload hash matched source and all four instruction references were accessible in each installed copy.
- Full Developer Skills installation copied exactly 25 skills per agent with matching payload hashes, including the complete report-creator payload.

No remote source, global installation, model prompt, or native agent discovery was exercised. The new skill's compatible_agents metadata remains empty. These checks prove external CLI packaging and local copy integrity, not runtime/model behavior. Earlier counts below describe earlier snapshots.

## Optional implementation helpers, 2026-10-28

Using the cached `skills@1.7.4` executable through Node.js against local source, with telemetry and Node compile-cache writes disabled:

| Check | Observed result |
|---|---|
| Collection listing | All 32 shipping skills present; sample-review absent |
| Selected lean-build install | Exactly one skill for each of Codex and Claude Code |
| Full Developer Skills install | Exactly 23 skills for each agent, including the six new helpers |
| Installed payload integrity | Every copied file hash matched its source, including instructions, README and metadata |

Each install used a separate disposable project with `--copy`, `--agent codex claude-code` and fixture-only `--yes`. Sources were the local root or developer pack; no download, global install or model prompt occurred. Native project discovery is recorded separately in [collection evidence](TEST_EVIDENCE.md). Earlier counts below retain their original snapshot scope.

## Combined modes and storage follow-up, 2026-10-26

Repeated local discovery and installation with the cached `skills@1.7.4` CLI after adding the report-storage payload:

| Check | Observed result |
|---|---|
| Collection listing | deep-critique present; sample-review absent |
| Selected deep-critique install | Exactly one skill for each of Codex and Claude Code; all six payload files matched source hashes |
| Complete Developer Skills install | Exactly 16 skills for each agent; every copied payload matched source bytes |
| Copied helper execution | Both agents' copies normalized `rate roast roast` to `roast rate` without source-relative imports |
| Installed report persistence | Helper reserved and finalized a categorized report in each isolated test project |

All installations used separate temporary projects, local source, `--copy`, and `--yes` limited to the fixtures. Telemetry and Node compile-cache writes were disabled for child processes. No global flag, real profile, remote publication or collection lifecycle ownership was involved. This checks payload portability and helper execution; native agent discovery remains unverified.

## Deep Critique local addition, 2026-10-26

Using the already cached `skills@1.7.4` CLI directly through Node.js, with telemetry disabled and isolated temporary project destinations:

| Check | Observed result |
|---|---|
| Local collection listing | deep-critique listed; sample-review absent |
| Local root single-skill selection | Only deep-critique installed for Codex and Claude Code |
| Local complete Developer Skills selection | Exactly 16 skills installed for each agent |
| Selected and full-pack copied payloads | Every relative file and SHA256 matched the source, including all three deep-critique files |
| External installation state | No collection `.agent-skills/` records created |

Commands used `node <cached-skills-1.7.4>/bin/cli.mjs add <local-source>` with `--list`, or `--skill deep-critique` / `--skill '*'` plus `--agent codex claude-code --copy --yes`. The approval flag applied only to isolated fixture installs. No global flag or real profile was used. This verifies local CLI selection and copy behavior, not native agent discovery, remote availability, or general model adherence. Remote evidence below remains tied to its recorded older revision.

## Previous collection verification

Verified on Windows PowerShell, 2026-10-26, using Node.js 24.19.0, npm 11.17.0 and `skills@1.7.4`. All installs used isolated temporary project scopes outside the checkout. No real profile install, push or publication was performed.

## Executed checks

| Check | Observed result |
|---|---|
| Local collection `add <checkout> --list` | Exactly 24 shipping skills; no `sample-review` fixture |
| Local Developer Skills pack listing | Exactly 15 skills |
| Local Developer Skills `--skill '*' --agent codex claude-code --copy` | Both agents received all 15; every copied file matched the source bytes, including READMEs |
| Local Ultimate QA pack listing | Exactly 9 skills |
| Local Ultimate QA `--skill '*' --agent codex claude-code --copy` | Both agents received all 9; copied scripts, references and READMEs matched source bytes |
| Local root with `--skill blocker-check --agent codex --copy` | Only blocker-check copied; README included |
| External installation records | No collection `.agent-skills/` state created; external lock files remained separate |
| Targeted Codex removal | CLI returned 0 but retained the shared copy while another detected agent used its canonical directory |
| Named removal without an agent filter | Selected skill directory removed across agents in the isolated scope |
| Remote GitHub root listing | Existing published revision discoverable; still exposes the old sample fixture until this rename is published |
| Remote GitHub single-skill installation | Only blocker-check installed for Codex |
| Remote GitHub Developer Skills subpath listing | Exactly 15 skills; no QA skills or fixture |
| Remote GitHub Developer Skills complete-pack install | All 15 installed; SKILL.md bytes matched the unchanged local instructions |
| Persistent QA kit access | Prompt, checklist, requirements template, client guide and preflight helper present at the documented kit root |
| QA helper execution | Source preflight `--help` and externally copied core state helper `--help` both exited 0 |

Remote source: `https://github.com/Etriii/agent-skills`; verified default branch `main`, revision `033e5716646d28717ab6bbf167555b7dc5a1935c`. Remote checks cover that published revision; new READMEs and fixture exclusion were verified against the local checkout. Publishing this revision is a separate action.

Commands used the [documented installation forms](NPX_INSTALLATION.md). Fixture installs added `--yes` only inside the isolated project scope, and set `DISABLE_TELEMETRY=1` for the child process. Remote full-pack selection used `https://github.com/Etriii/agent-skills/tree/main/packs/developer-skills` with the literal `--skill '*'`; it did not use `--all`.

## Interpretation and limits

The existing `skills` CLI supplies discovery, selection, terminal summaries and copy operations. No collection-owned npm wrapper is needed. Test fixtures use `SKILL.md.example` so repository discovery cannot offer them as shipping skills. The collection regression suite also checks that boundary.

Ultimate QA remains a kit-dependent workflow. Its existing `ULTIMATE_QA_KIT` setting or an explicitly provided path resolves persistent templates/helpers after an external copy. The Python installer continues to generate `kit-location.txt` and own its recorded lifecycle. This change introduces no new third-party Python import, environment setting or database hook. Node/npm are prerequisites only for the external installation route; optional QA Word generation still uses `python-docx`.

Global/user-profile writes, native agent discovery after these installs, model adherence, application QA and external security-assessment badges were not exercised. The actual external CLI removal limitation is documented in the [removal guide](NPX_INSTALLATION.md#updates-and-removal). Licenses remain unchanged. [Collection checks](TEST_EVIDENCE.md) cover manifest validation, lifecycle preservation and archive packaging.
