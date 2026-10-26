# External CLI compatibility evidence

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
