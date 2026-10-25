# Agent Skills

A collection of installable skill packs for Codex and Claude. Each pack keeps related skills, templates and helpers together. One shared tool installs and uninstalls selected skills, records completed operations in Markdown, and retains removed or replaced content as backups.

Requires Python 3.11 or newer. Installation uses the Python standard library and works offline after downloading or cloning this repository.

| Pack | Skills | Purpose |
|---|---:|---|
| [Developer Skills](packs/developer-skills/README.md) | 15 | Planning, architecture, implementation review and handoff |
| [Ultimate QA](packs/ultimate-qa/README.md) | 9 | Versioned QA reviews, specialist checks and optional client documents |

## Download

Once the repository is hosted on GitHub, use **Code > Download ZIP**, extract it, and open a terminal in the extracted `agent-skills` folder. Alternatively, clone the actual repository URL shown by GitHub. Keep the complete collection, including `tools/` and the selected pack's support files.

To build a local downloadable snapshot:

```powershell
python tools/package_skills.py
```

This creates `dist/agent-skills-0.1.0.zip` and `dist/SHA256SUMS`. A local ZIP is a working-tree snapshot, not proof of a published GitHub release. [Publishing instructions](docs/PUBLISHING.md) cover repository setup, license decisions and releases.

## Install

Run commands from the collection root. List either pack:

```powershell
python tools/install_skills.py --pack developer-skills --list
python tools/install_skills.py --pack ultimate-qa --list
```

Preview selected skills in an existing application folder, then run the same command without `--dry-run` and approve the displayed plan:

```powershell
python tools/install_skills.py --pack developer-skills --agent codex --project "D:\My App" --bundle essential --dry-run
python tools/install_skills.py --pack developer-skills --agent codex --project "D:\My App" --bundle essential

python tools/install_skills.py --pack ultimate-qa --agent both --project "D:\My App" --skills ultimate-qa ultimate-qa-api --dry-run
python tools/install_skills.py --pack ultimate-qa --agent both --project "D:\My App" --skills ultimate-qa ultimate-qa-api
```

Project scope is the default. For availability across projects, choose user scope explicitly:

```powershell
python tools/install_skills.py --pack ultimate-qa --agent codex --scope user --user-home "$env:USERPROFILE" --bundle all --dry-run
python tools/install_skills.py --pack ultimate-qa --agent codex --scope user --user-home "$env:USERPROFILE" --bundle all
```

Codex copies go under `.agents/skills/`; Claude copies go under `.claude/skills/`. Refresh the agent's skill list after installation. Installing files does not run a skill or prove native discovery. See [INSTALL.md](INSTALL.md) for integrity checks, collisions and recovery.

## Uninstall and records

```powershell
python tools/install_skills.py --pack ultimate-qa --agent codex --project "D:\My App" --skills ultimate-qa-api --uninstall --dry-run
python tools/install_skills.py --pack ultimate-qa --agent codex --project "D:\My App" --skills ultimate-qa-api --uninstall
```

Every completed changing operation writes `<scope-root>/.agent-skills/history/<operation-id>/operation.md`. Records include UTC time, pack, agent, scope, source manifest hash, exact destinations, before/after content hashes, previous installation records and backup location. Records survive uninstall.

Previews, cancellations, validation failures, rolled-back operations and unchanged reruns create no success records. An interrupted transaction blocks further changes until explicit recovery. Uninstall requires recorded ownership and unchanged installed content; it preserves other packs, other agents, application files and QA reports. Removed content remains in `.skills-install-backups/` until you explicitly remove those backups. See [UNINSTALL.md](UNINSTALL.md) and [record format](docs/INSTALLATION_RECORDS.md).

## Structure and checks

```text
agent-skills/
  packs/
    developer-skills/{skills,tools,docs,...}
    ultimate-qa/{skills,tools,tests,04_REQUIREMENTS_TEMPLATE,...}
  tools/             shared catalog, lifecycle, transaction and packaging tools
  tests/             collection and installer regression tests
  docs/              architecture, records, migration and publication
```

```powershell
python -B -m unittest discover -s tests -v
python -B -m unittest discover -s packs/ultimate-qa/tests -v
```

Read [creating a pack](docs/creating-a-pack.md) before adding another collection. [Migration notes](docs/MIGRATION.md) identify preserved sources and CLI changes. [LICENSE.md](LICENSE.md) records the existing license boundaries; no open-source license has been selected for the collection.
