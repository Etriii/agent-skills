# 10 – Phase adapter: fitting the kit to someone else's phases

The kit plans work in four phases – **1 Protect · 2 Stabilise · 3 Grow · 4 Sustain** – during QA review and planning. Implementation is a separate task. Real projects already have their own structure: sprints, milestones, a client's contract phases, a school capstone's chapters, a company's SDLC gates, another agent's roadmap file.

Rather than forcing the project onto the kit's phases, the kit adopts theirs. The user gives **a path and an instruction**; the agent produces a mapping and then speaks the project's own language in every document.

---

## 1. How the user asks

```
Read <template folder>/README.md and follow it for this project: qa adopt docs/ROADMAP.md : use the four milestones in that file; anything security-related must land in M1 even if the plan calls it phase 2
```

The shape is `qa adopt <path> : <instructions>` where

- **`<path>`** is a file or folder describing the phases: a roadmap, a sprint plan, a project timeline, a methodology document, an existing agent's plan file, a Gantt export, a milestone list in a README. Anything readable.
- **`<instructions>`** (optional, after the colon) is free text saying how to fit into it: which of their phases is which, what must go where, how strictly to follow their order, whether to write into their file or only into `qa-findings/`.

If the user gives no instruction, use the defaults in §4. If the user gives an instruction but no path (`qa adopt : we work in two-week sprints, name them Sprint 12, Sprint 13 …`), that is fine too – the instruction alone becomes the mapping.

---

## 2. What the agent does with it

1. **Read the phase source** at the given path. Extract the phases in their order, with their exact names and numbering, their goals, and any dates, owners or entry/exit criteria. Quote their names exactly – `M1 – Core booking`, not "Phase 1".
2. **Write `qa-findings/requirements/05_PHASE_MAP.md`** (template in `04_REQUIREMENTS_TEMPLATE/05_PHASE_MAP.md`) with:
   - where the phase definition came from (path, date read, and the version or commit of that file);
   - the user's instruction, verbatim;
   - the **mapping table** – each kit phase to one of their phases, with a one-line reason;
   - the **reverse table** – each of their phases, and what kind of QA work belongs in it;
   - anything that does not fit, and what you did with it;
   - a mode: `mapped` (their names, kit order kept underneath) or `transformed` (their structure wins completely).
3. **Use their names everywhere afterwards.** In `04_Improvement_Plan`, in `05_Client_Approval_Checklist`, in the change log, in commit messages. The kit's own four phase names appear only once, in the mapping table, so the correspondence stays auditable.
4. **Record a condition** (`CON-nnn` in `04_CONDITIONS.md`) for every judgement call the mapping required – above all for anything you had to reorder, split, or park. If the user's instruction forces a security fix into a late phase, that is a condition with a risk note, applied as the user asked.

### Mapped vs transformed

| Mode | Use it when | What happens |
|---|---|---|
| **mapped** (default) | Their phases are a different labelling of the same idea – milestones, sprints, releases | The plan keeps the kit's internal ordering logic (protect first) and prints their names; a Must-severity item still sorts to the earliest phase it is allowed into |
| **transformed** | Their phases are a genuinely different model – a methodology with its own gates, a capstone's chapters, a compliance programme | The plan is restructured to their model: their phase order, their entry/exit criteria, their vocabulary, and their document sections if they specify them. The kit's phase names disappear from the output entirely |

Ask for `transformed` explicitly (`qa adopt docs/SDLC.md : transform, follow their gates exactly`); otherwise use `mapped`.

---

## 3. A worked mapping

Source: `docs/ROADMAP.md` with `M1 – Launch blockers`, `M2 – Stability`, `M3 – New features`, `M4 – Handover`. Instruction: *"anything security-related must land in M1"*.

| Kit phase | Their phase | Why |
|---|---|---|
| 1 – Protect | **M1 – Launch blockers** | Same intent: nothing ships until these are done. The instruction also pulls every security item here regardless of the kit's own priority |
| 2 – Stabilise | **M2 – Stability** | Direct match: error handling, throttling, monitoring |
| 3 – Grow | **M3 – New features** | The developer's ideas and the nice-to-have improvements |
| 4 – Sustain | **M4 – Handover** | Documentation, tests, CI, runbooks, the client's own maintenance |

| Their phase | QA work that belongs in it |
|---|---|
| M1 | Every Must finding, every security and permission item, every data-loss risk, plus `G-002` (the copy-identity gap) because later work depends on the model being right |
| M2 | Should findings, destructive-test failures around dependency handling, monitoring |
| M3 | `IDEA-001`, `IDEA-003`, Nice findings that improve the experience |
| M4 | Test harness, change-log discipline, the re-test list, the client sign-off pack |

Items that did not fit: the plan's *Decisions needed* section has no equivalent in their roadmap → kept as its own section at the top of the plan and referenced from M1. Recorded as `CON-009`.

---

## 4. Defaults when the instruction is silent

- Phase names come from their document; if it numbers them, keep the numbers and the exact spelling.
- A **Must** item never moves later than the earliest phase that is still open, even if their structure would put that work later – if the instruction forces it later anyway, apply the instruction and raise a condition with the risk.
- Work that has no home in their model goes into the nearest later phase, and is listed under *Did not fit the phase model* in `05_PHASE_MAP.md`.
- Their extra phases with no QA work get a row saying "nothing from this review lands here" rather than being left out.
- Their dates and owners are copied into the plan where they exist; the kit never invents dates.

---

## 5. Writing into their files

By default the kit writes **only** inside `qa-findings/` – the project's own roadmap, board or plan file is read, never edited.

If the user explicitly asks for it (`… : and add the accepted items to that roadmap file`), then:

- append only, in their file's existing format and heading style;
- one clearly marked block (for example `### From the QA review (v1, 2026-03-04)`) so it can be found and removed;
- never renumber, reorder or reword their existing entries;
- keep the same refs (`P-03`, `F-012`) so the two documents can be read side by side;
- say in the run summary exactly which file you touched and what you added.

---

## 6. Adapting later, and across versions

The phase map lives in `requirements/`, so it is shared by every version and survives `qa v2`. If their roadmap changes, run `qa adopt` again with the new path: the old mapping is not edited – append a new dated section to `05_PHASE_MAP.md` and mark the previous one *superseded*, the same way conditions work. Documents already written keep the phase names that were correct when they were written; the carry-over document in the new version notes the change in one line.
