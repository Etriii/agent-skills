# Developer Skills installation

Use the shared [collection installation guide](../../INSTALL.md) and [uninstall guide](../../UNINSTALL.md). Select this pack with `--pack developer-skills`.

```powershell
# From the collection root
python tools/install_skills.py --pack developer-skills --agent codex --project "D:\My App" --skills blocker-check --dry-run
python tools/install_skills.py --pack developer-skills --agent codex --project "D:\My App" --skills blocker-check
python tools/install_skills.py --pack developer-skills --agent codex --project "D:\My App" --skills blocker-check --uninstall --dry-run
python tools/install_skills.py --pack developer-skills --agent codex --project "D:\My App" --skills blocker-check --uninstall
```

Every completed changing operation has a Markdown record under the chosen scope's `.agent-skills/history/`. The collection uses `.agents/skills/` for Codex in project and user scope; legacy `.codex/skills/` copies are preserved. See [migration notes](../../docs/MIGRATION.md).
