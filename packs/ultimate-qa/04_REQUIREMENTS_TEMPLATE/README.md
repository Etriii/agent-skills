# requirements/ – inputs for the QA review of this project

This folder lives at `<project root>/qa-findings/requirements/`. The AI agent reads every file here, in numeric order, before it checks anything. You own this folder: fill in what you can and add as many extra files as you like. It is **shared by every QA version** (v1, v2, v3 …) – the inputs and the decisions carry forward, the outputs do not.

| # | File | What it is | Fill it in when |
|---|---|---|---|
| 01 | `01_RUN_SETTINGS.md` | How to run the review: mode, sections, destructive testing, output language | Rarely – defaults audit and plan, then stop |
| 02 | `02_PROJECT_CONTEXT.md` | What the app is, the roles and their **test accounts**, the **core user journeys**, environments, integrations, your **source documents** (spec, plan, brief) and your decisions. The agent pre-fills what it can detect on the first run | Before the plan run – 5 to 10 minutes. Test accounts and core journeys matter most: they decide *which role* the reviewer logs in as and *which pages* it walks through |
| 03 | `03_IMPLEMENTATION_IDEAS.md` | The improvements you already intend to build (`IDEA-001`, `IDEA-002` …) so they are merged into the plan and not proposed twice. The agent appends its questions for the client at the bottom | Before the plan run. Delete the examples or overwrite them |
| 04 | `04_CONDITIONS.md` | The decision register: every judgement call, who made it, and why – including the ones you made against the agent's advice, with your justification | The agent maintains it. Read it, tick *Reviewed*, and overrule anything you disagree with |
| 05 | `05_PHASE_MAP.md` | Only if the project has its own phases, sprints or milestones – how the review's phases map onto them | The agent fills it in when you run `qa adopt <path> : <instructions>` |
| 06 | `06_PROGRESS_SOURCES.md` | Where "what has already been done" is recorded, so a new QA version does not re-report finished work | Before running `qa v2`. The agent asks for it if it is empty |
| 07+ | Anything else, numbered | The client's returned *What we need from you* form (from the template's `12_CLIENT_PACK/`), a permission matrix, a design brief or Figma link, the client's brief, an old bug list, an email thread with decisions, screenshots of problems. Markdown, text, PDF, images – the agent reads what it can and cites the file where it uses it | Any time |

## Rules

- Keep the number prefixes. Add new files with the next free number (`07_…`, `08_…`). Do not renumber existing ones.
- Put **test / staging** accounts only. Never real customer accounts or production passwords. The whole of `qa-findings/` is git-ignored, so nothing here is committed.
- The agent never rewrites your files here. It appends: questions under *Questions for the client* in `03_IMPLEMENTATION_IDEAS.md`, new rows in `04_CONDITIONS.md`, new sections in `05_PHASE_MAP.md` and `06_PROGRESS_SOURCES.md`. Your own text is left exactly as you wrote it.
- **Unreviewed conditions are applied as the agent decided them** – the review never stalls waiting for you. When you disagree, the agent builds your version and records your justification. See `04_CONDITIONS.md`.
- **The client never sees this folder** and is never told it exists. When client documents are requested, questions go in the current version's `client/questions/`; answers are copied into the appropriate internal record.
- Outputs never appear here. QA outputs go into `qa-findings/v<N>/recommendations/`. Optional client outputs go into `qa-findings/v<N>/client/`, with Markdown in `md/` and Word files in `docs/`.

## What to type to run the review

Open the project in your AI coding agent and type:

```
Read <path to the qa-template folder>/README.md and follow it for this project.
```

The agent works out the next QA step from what already exists (audit → gaps → plan), then stops. Add a keyword to steer it:

| Type this after the line above | It does |
|---|---|
| `… and run the audit again` | Re-audit the current version |
| `… : plan only` / `… only sections 7 and 8` | Limit the run |
| `… : qa v2` | Start a new QA version, carrying v1 forward |
| `… : qa gaps` | Only the system-gap hunt |
| `… : qa destroy` | Only destructive testing (needs permission in the run settings) |
| `… : qa adopt docs/ROADMAP.md : use their milestones` | Fit the plan to the project's own phases |
| `… : qa status` | Report where things stand, write nothing |
