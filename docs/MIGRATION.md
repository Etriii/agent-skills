# Collection migration

The canonical new checkout is `C:\Users\ACER\Downloads\Development\agent-skills`. The existing `Development\skills` checkout and the original Ultimate QA checkout remain intact. PhasePilot continues using its original sibling provider; this change does not switch or upgrade PhasePilot.

The new checkout preserves Developer Skills Git history through `dd35335bbd308099a9edf42acb6ce54357185f7f`. The imported QA source was read from `C:\Users\ACER\OneDrive\Desktop\Softwares\vibe-coding\ultimate-qa`, commit `ba4205384968f1f9e3dec4290d29dc58c2293ef2`. Both source worktrees were clean at import. No source `.git`, local skill installations, caches or secret configuration were imported.

| Previous location | Collection location |
|---|---|
| Developer `skills/` | `packs/developer-skills/skills/` |
| Developer catalog, manifest and docs | `packs/developer-skills/` |
| Developer provider helpers | Root `tools/`, extended for recorded lifecycle |
| QA kit and numbered templates | `packs/ultimate-qa/` |
| QA skill/helper payloads | Same paths relative to the QA pack |

All 24 original `SKILL.md` bodies, developer metadata, QA references, QA runtime helpers and templates are retained. QA's installer is replaced with a thin shared-tool entry point. Its installer tests cover the unified interface; the QA state tests remain. Historical developer contract/compatibility documents describe their original verification, not new collection acceptance.

The new collection deliberately uses one CLI: `--pack`, `--agent`, explicit skill selection and explicit project/user scope. QA's old `--target`, implicit global/all selection and custom `--destination` are not this CLI. Both adapters use `.agents/skills` for Codex and `.claude/skills` for Claude in either scope. The prior developer user path `.codex/skills` is not changed, searched or removed. Review old copies separately to avoid duplicate discovery.

Existing copies are not automatically owned. Reinstall an identical copy to adopt it into Markdown history; use explicit `--replace` with retained backups for differing copies. Existing QA core/client pointers continue referring to the original kit until explicitly reinstalled. After moving the new collection, repeat a core/client install with `--replace` to update its pointer.

To revert adoption of this collection, uninstall its managed copies with this tool, retain the records/backups, and use the untouched original repositories. No real user/profile installation is migrated by building this collection.

No new third-party runtime dependencies, environment variables, database hooks, migrations or feature flags were introduced. Optional QA Word export still uses its existing `python-docx` dependency. Collection license selection, GitHub destination and public release remain separate owner decisions.
