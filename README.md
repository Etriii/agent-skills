# Agent Skills

A collection of installable skill packs for Codex and Claude. Each pack keeps related skills, templates and helpers together. One shared tool installs and uninstalls selected skills, records completed operations in Markdown, and retains removed or replaced content as backups.

Install through the external `skills` CLI with Node.js 22.20+ and npm, or use our recorded installer with Python 3.11+. The Python route uses the standard library and works offline after downloading or cloning this repository.

| Pack | Skills | Purpose |
|---|---:|---|
| [Developer Skills](packs/developer-skills/README.md) | 30 | Prompt intake, planning, UI/UX and mobile improvements, reports, system settings, reviews and handoff |
| [Ultimate QA](packs/ultimate-qa/README.md) | 9 | Versioned QA reviews, specialist checks and optional client documents |

Each skill has a README covering its purpose, installation, usage and prerequisites. Browse the [skill catalog](SKILL_CATALOG.md) or read [CONTRIBUTING.md](CONTRIBUTING.md) to contribute.

Use the [command guide](docs/SKILL_COMMANDS.md) for copyable requests, supported automatic workflows, expected outputs, and review/implementation boundaries across every skill.

## Find a skill by purpose

Categories describe what a skill helps you do; packs select what you install. The [catalog](SKILL_CATALOG.md) assigns every available skill one primary category and lists its installation pack.

| Category | Use it to |
|---|---|
| [Planning and decisions](SKILL_CATALOG.md#planning-and-decisions) | Clarify tasks, review plans, resolve blockers and manage plan versions. |
| [Critique and evaluation](SKILL_CATALOG.md#critique-and-evaluation) | Challenge assumptions and assess ideas, plans or other work. |
| [Engineering reviews](SKILL_CATALOG.md#engineering-reviews) | Review architecture, UI, backend, databases, security and business rules. |
| [UI and UX design](SKILL_CATALOG.md#ui-and-ux-design) | Audit pages, choose interface improvements, compare wireframes and implement approved or autonomous changes. |
| [Implementation and change safety](SKILL_CATALOG.md#implementation-and-change-safety) | Diagnose failures, implement features, fix bugs, refactor, migrate and verify scoped work. |
| [Execution and handoff](SKILL_CATALOG.md#execution-and-handoff) | Carry out authorized work and preserve a usable handoff. |
| [Verification and readiness](SKILL_CATALOG.md#verification-and-readiness) | Check acceptance evidence, prerequisites and delivery readiness. |
| [QA workflows](SKILL_CATALOG.md#qa-workflows) | Run structured audits and specialist QA checks. |

For a suggested order, read [skill workflows](docs/SKILL_WORKFLOWS.md). It covers standalone use and how these advisors fit PhasePilot's plan, approval, execution and verification workflow.

## Quick install with npx

Install one skill globally for Codex:

```powershell
npx skills@1.7.4 add https://github.com/Etriii/agent-skills --skill blocker-check --agent codex -g --copy
```

List available skills or install the complete Developer Skills pack:

```powershell
npx skills@1.7.4 add https://github.com/Etriii/agent-skills --list
npx skills@1.7.4 add https://github.com/Etriii/agent-skills/tree/main/packs/developer-skills --skill '*' --agent codex -g --copy
```

Run without `-g` from your application directory for a project install. For Claude Code, use `--agent claude-code`. `--copy` selects copies instead of links. Review the CLI's installation summary before proceeding; when an agent invokes the command, the external CLI may run without an interactive prompt.

For Ultimate QA, follow the [pack setup](packs/ultimate-qa/README.md#install-with-npx) to retain its templates and helpers. A copied skill alone does not include the complete QA kit. [The npx guide](docs/NPX_INSTALLATION.md) covers individual skills, complete packs, removal and the existing kit-path setting.

The external CLI owns its prompts, security assessments and lock files. Its installs do not write this collection's Markdown operation history or use our backup/recovery engine. Choose the Python installer below when those records and protections are required. Use the same installer for updates and removal of a given copy.

## Download

Use [GitHub](https://github.com/Etriii/agent-skills) **Code > Download ZIP**, extract it, and open a terminal in the extracted `agent-skills` folder. Alternatively:

```powershell
git clone https://github.com/Etriii/agent-skills.git
cd agent-skills
```

Keep the complete collection, including `tools/` and the selected pack's support files. Remote commands install the version currently on GitHub; local changes become available there only after publication.

To build a local downloadable snapshot:

```powershell
python tools/package_skills.py
```

This creates `dist/agent-skills-0.1.0.zip` and `dist/SHA256SUMS`. A local ZIP is a working-tree snapshot, not proof of a published GitHub release. [Publishing instructions](docs/PUBLISHING.md) cover repository setup, license decisions and releases.

## Install with Markdown records

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
