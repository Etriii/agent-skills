# Developer Skills pack

Fifteen independent development skills for planning, reviews, delivery checks and handoff. Original skill bodies, metadata and the payload manifest are preserved. No private runner, Docker, API key or network access is required for installation.

This pack belongs to [Agent Skills](../../README.md). Use Python 3.11+ from the collection root:

```powershell
python tools/install_skills.py --pack developer-skills --list
python tools/install_skills.py --pack developer-skills --agent both --project "D:\My App" --bundle essential --dry-run
python tools/install_skills.py --pack developer-skills --agent both --project "D:\My App" --bundle essential
```

Essential contains plan-review, blocker-check, phase-handoff and completion-check. Use `--skills blocker-check` for one or `--bundle all` explicitly for all fifteen. Installation executes no skill. The pack-local `tools/install_skills.py` is an entry point to the same collection tool.

The [installation guide](../../INSTALL.md) covers user scope, integrity, matching-copy adoption, backup replacement and recovery. The [removal guide](../../UNINSTALL.md) gives tracked uninstall/reinstall commands. Completed changing operations create scoped Markdown history; removal preserves records and content backups.

Read [SKILL_CATALOG.md](SKILL_CATALOG.md) for selection and [docs/SKILL_STANDARD.md](docs/SKILL_STANDARD.md) for metadata and payload hashes. Other historical pack contracts and compatibility reports retain their original evidence limits. Current collection proof is [TEST_EVIDENCE.md](../../docs/TEST_EVIDENCE.md).

Run collection tests from the root with `python -B -m unittest discover -s tests -v`. License status remains UNDECIDED; see [collection license status](../../LICENSE.md).
