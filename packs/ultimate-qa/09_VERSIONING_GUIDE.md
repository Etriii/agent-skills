# 09 – Versioning: v1, v2, v3 … without losing anything

A QA review is not a one-off. The first pass finds what it finds, the team builds some of it, the product moves, and then someone asks for another review. This file defines how the second (and fifth) review reuses everything the earlier ones learned instead of starting from a blank page.

For `$ultimate-qa next-version`, also use the state snapshots in `qa-findings/state.json` and `vN/state.json` described in `13_SKILLS_AND_AUTOMATION.md`. Reconcile all prior items first; the new active state carries unresolved items only. Keep closed items in historical reports and snapshots.

The rule behind all of it: **nothing is ever deleted, only carried forward, closed, or removed with a reason.**

---

## 1. Keywords

Type one of these after the standard one-liner, in any AI coding agent. The words in **bold** are the keyword the agent looks for; everything around them is free text.

```
Read <template folder>/README.md and follow it for this project: qa v2
```

| Keyword | What it does |
|---|---|
| *(nothing)* | Continue the current version: audit → plan, then stop |
| **`qa v2`**, `qa v3` … (also `next version`, `new qa version`, `start v2`) | Open a new QA version: ask for the progress folder, carry everything forward, re-audit against the current code |
| **`qa gaps`** | Run (or re-run) only the system-gap hunt → `06_System_Gaps_Report` |
| **`qa destroy`** | Run (or re-run) only destructive testing → `07_Destructive_Test_Report` (needs the gate in `08_DESTRUCTIVE_TESTING.md`) |
| **`qa adopt <path> : <instructions>`** | Make the kit follow another project's phase structure – see `10_PHASE_ADAPTER.md` |
| **`qa intake`** | Redo the intake questions and update the conditions file |
| **`qa status`** | Write nothing; report where the project stands: current version, open items, what is waiting on whom |

The version keyword is the important one. `qa v2` means: *read everything in `qa-findings/`, find out what has been done since, and produce a version 2 that supersedes version 1 without losing its history.*

---

## 2. Folder layout with versions

```
<project root>/qa-findings/
├── VERSIONS.md                       ← the version register: one section per version
├── requirements/                     ← shared across all versions (inputs, context, conditions, ideas)
│   ├── 01_RUN_SETTINGS.md
│   ├── 02_PROJECT_CONTEXT.md
│   ├── 03_IMPLEMENTATION_IDEAS.md
│   ├── 04_CONDITIONS.md              ← append-only decision register
│   ├── 05_PHASE_MAP.md               ← only when the kit was adapted to another phase model
│   └── 06_PROGRESS_SOURCES.md        ← where "what is already done" is tracked, per version
├── v1/
│   ├── recommendations/
│   │   ├── md/    QA reports and plan ← markdown sources
│   │   ├── docs/  matching Word files
│   │   ├── evidence/
│   │   └── archive/YYYYMMDDTHHMMSSZ-<unique-id>/           ← previous drafts within this version
│   └── client/                       ← only when `$ultimate-qa-client prepare` runs
│       ├── md/    client report and approval checklist
│       ├── docs/  matching Word files
│       ├── decisions/                 ← returned client choices
│       └── after_implementation/      ← only after separately authorized work
├── v2/                               ← same shape; created by `qa v2`
│   └── recommendations/              ← client/ remains absent until requested
│       ├── md/    00_Carry_Over.md   ← what came from v1 and in what state (v2+ only), then 01_… as in v1
│       └── docs/  00_Carry_Over.docx
└── removed/
    └── v2/
        ├── REMOVED_ITEMS.md          ← the list: what was removed, from where, why, who decided
        └── <the removed files>       ← whole documents dropped in this version, moved here intact
```

Older projects may have `qa-findings/recommendations/` directly under `qa-findings/`, or a legacy `after_recommendations/` folder. Preserve and migrate those historical outputs into `qa-findings/v1/` when opening a versioned review; do not treat them as files to generate in a new review.

---

## 3. Opening a new version

### Step 1 – Ask for the progress first (do not skip this)

Before creating any `vN/` folder, ask:

> **Starting QA v2.** Before I carry version 1 forward, where is the record of what has already been done? A progress file, a done-list, a sprint board export, a changelog, a folder of notes, a branch or a range of commits – any of those. Give me the path (or "none" and I will work it out from the code and from version 1's change log).
>
> Also: anything from version 1 you want **dropped** rather than carried – items that no longer apply because the feature was removed or the decision changed? Tell me which and why, and I will move them to the removed folder with your reason.

Wait for the answer to that first question. It is the one input that decides whether v2 is accurate; guessing it produces a version 2 that re-reports work the team already finished. If the user says "none" or does not answer within the run, proceed using v1's `02_Change_Log`, the git history since v1's date, and the current code – and record that in `06_PROGRESS_SOURCES.md` as the source used.

Record what you were given in `qa-findings/requirements/06_PROGRESS_SOURCES.md`: path, what kind of source it is, the date range it covers, and how much you trust it.

### Step 2 – Reconcile every open item against reality

Take every `F-nnn`, `G-nnn`, `D-nnn`, `IDEA-nnn`, `P-nn` and `CON-nnn` from all previous versions and give each one a **carry state**, verified against the code – not against what the progress file claims. The progress file tells you where to look; the code tells you the truth.

| Carry state | Meaning | Where it goes in vN |
|---|---|---|
| `CLOSED-VERIFIED` | Fixed, and you confirmed it in the code or by using the app | Listed in `00_Carry_Over.md`, not re-opened |
| `CLOSED-CLAIMED` | The progress source says done, you could not verify it | Carried as open with a note; re-tested in this version |
| `OPEN-CARRIED` | Still present, unchanged | Carried with its original number and its full history |
| `OPEN-CHANGED` | Still present but different now (smaller, larger, moved) | Carried with its original number, plus a "what changed since v1" line |
| `REGRESSED` | Was fixed in an earlier version, is broken again | Carried with its original number, severity raised one step, and the version it regressed from named |
| `REJECTED-STANDING` | The client rejected it and the reason still holds | Listed once in `00_Carry_Over.md` with the client's original words. **Not** re-proposed as if new |
| `REJECTED-REVISIT` | The client rejected it but the circumstances changed (it now causes a live problem) | Re-proposed **as the same number**, with a short "why we are raising this again" |
| `SUPERSEDED` | A newer finding replaces it | Points at the new number |
| `REMOVED` | Deliberately dropped from the scope of the review | Moved to `removed/vN/` with a reason (below) |

Numbers never change and never get reused. `F-012` is `F-012` in v1, v2 and v5. A finding closed in v1 and regressed in v3 is still `F-012`, with three history lines under it.

### Step 3 – Write `vN/00_Carry_Over.md`

The first document of a new version, before any new checking. Sections:

1. **What version this is, what came before it, and the dates.**
2. **Where the progress information came from** (the paths given in step 1, and what you verified rather than took on trust).
3. **The carry table** – every previous item, its carry state, one line of evidence for that state.
4. **Closed since the last version** – the wins, so the client can see progress. Counts by severity.
5. **Regressions** – anything that came back, called out plainly.
6. **Removed in this version** – a short list pointing at `removed/vN/REMOVED_ITEMS.md`.
7. **Conditions still standing** – conditions from `04_CONDITIONS.md` that still shape this version, and any the new code has proven wrong (superseded).

### Step 4 – Run the version

Then run QA normally – audit, gaps, destructive (if enabled), plan – with three differences:

- Carried-open items are **not re-discovered from scratch**: re-verify each one, update it, keep the number and the history.
- New findings continue the numbering from the highest number ever used in the project.
- Every document's cover block says `Version: v2` and `Supersedes: v1 (date)`.

---

## 4. The removed folder

Removing something from the review is legitimate – a module was deleted, a feature was cancelled, a finding turned out to be a misunderstanding, the client rescoped. Removing it silently is not.

When an item or a whole document is removed in version N:

1. Move the file (or write the item's full previous text) into `qa-findings/removed/vN/`.
2. Add a row to `qa-findings/removed/vN/REMOVED_ITEMS.md`:

   | Ref | Title | First appeared | Removed in | Reason | Decided by | Restore how |
   |---|---|---|---|---|---|---|
   | F-018 | Booking form accepts past dates | v1 | v2 | The booking module was replaced by the new scheduler; the form no longer exists | User (chat, 2026-04-02) | Re-run section 1 against the new scheduler |
   | D-004 | Export times out at 50k rows | v1 | v2 | Export moved to a background job; superseded by F-051 | Agent | See F-051 |

3. Never re-report a removed item as a new finding in a later version. If it comes back, restore it under its original number and note that it was previously removed.
4. The reason must be a reason, not a category. "Out of scope" alone is not enough – say why it is out of scope and who decided.

`REMOVED_ITEMS.md` is cumulative per version folder and is listed in `VERSIONS.md`. The client-facing summary mentions removals in one plain sentence ("three items from the last review no longer apply because the booking module was replaced"); the detail stays internal unless the client asks.

---

## 5. `VERSIONS.md`

One section per version, newest at the top, written or updated at the end of every version:

```
## v2 – 2026-04-10 (supersedes v1, 2026-03-04)
- Trigger: user typed "qa v2"
- Progress sources: docs/PROGRESS.md (given by user), optional v1/client/after_implementation/md/02_Change_Log.md, git log v1.0.0..HEAD
- Carried: 41 items (12 closed-verified, 3 closed-claimed, 21 open, 2 regressed, 3 rejected-standing)
- Removed: 3 (see removed/v2/REMOVED_ITEMS.md)
- New in this version: 17 findings, 4 gaps, 6 destructive findings
- Conditions: 2 new (CON-011, CON-012), 1 superseded (CON-004 -> CON-011)
- Outcome: plan P-01..P-14; client accepted 9, rejected 3, on hold 2
```

Anyone – a person or the next agent – should be able to read `VERSIONS.md` alone and know the shape of the project's QA history.
