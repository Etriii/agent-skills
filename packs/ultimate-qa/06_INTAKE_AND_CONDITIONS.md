# 06 – Intake and the conditions file

Two things happen before any checking starts on a project: the **intake** (a short conversation, once per project) and the **conditions file** (a written record of every judgement call, who made it, and why). Everything later in the kit – the plan, the client checklist, the next QA version – reads from the conditions file, so it is worth getting right.

---

## Part 1 – Intake: ask before you run anything

On the **first run in a project** (no `qa-findings/` yet, or no `qa-findings/requirements/04_CONDITIONS.md`), stop after identifying the project and ask the user these questions in one short chat message. Number them so the user can answer `1 – none, 2 – ./docs/spec`, and keep the whole message under about fifteen lines.

> **Before I start the review, five quick questions.**
>
> 1. **Requirements / specification** – do you have written requirements you want the review to check against (a spec, an SRS, a client brief, user stories, acceptance criteria, a Figma)? If yes, give me the file or folder path and I will read it. If there is none, say "none" and I will review against the checklist and what the code implies.
> 2. **Existing plans** – is there an implementation plan, roadmap, backlog or to-do list you already wrote? Path please. I will read it, merge it into the improvement plan, and tell you honestly where I think a part of it is wrong or risky.
> 3. **Work already done** – is there a progress file or folder (a done-list, a sprint board export, a changelog) that says what has already been built or fixed? Path please, so I do not re-report what is already handled.
> 4. **Environment and limits** – which environment may I use (local / staging / never production), may I start the app, may I create test data, and is anything off limits (folders, payment code, live integrations)?
> 5. **Destructive testing** – may I try to break the system on purpose (abuse input, overload, kill dependencies, corrupt state)? Yes / no / staging only. Default is **no** unless you say otherwise. See `08_DESTRUCTIVE_TESTING.md` for exactly what that means.
>
> Answer what you can. For anything you skip I will use my own judgement, write the decision in the conditions file, and mark it *unreviewed* so you can overrule it later.

Rules for the intake:

- **Ask once.** Record the answers, then never ask the same questions again in that project. Later runs only ask about something genuinely new (a new version, destructive testing being switched on).
- **A path is enough.** If the user gives a folder, read every file in it that you can parse, and list in `01_Project_Map` § *Inputs we were given* what you read and what you could not (binary, image-only PDF, password-protected).
- **Explicit skips use defaults.** If the user replies "just go" or sets `INTAKE: skip`, use safe defaults, write them into the conditions file as `Decided by: agent (unreviewed)`, and continue. Silence does not answer pending questions or grant permission for environment changes or destructive tests.
- **Copy, do not move.** Requirements the user points at stay where they are. Reference them by path in `qa-findings/requirements/02_PROJECT_CONTEXT.md` § *Source documents*; copy only short extracts you actually rely on.
- **Requirements beat the checklist for intent, never for safety.** If the written spec asks for something the checklist calls a security or data-integrity failure, build it as specified only after raising it as a condition (below) – the spec does not override *Must*-severity findings without a written justification.

---

## Part 2 – Reviewing the plans the user already has

The user's own plan is an input, not an instruction. For each item in it, write one line in `04_Improvement_Plan` § *Developer ideas – where they ended up* and, when you disagree, one condition row. Use exactly these verdicts:

| Verdict | Means | What you do |
|---|---|---|
| **Sound** | Good idea, keep as written | Merge into the plan with its own `P-nn` |
| **Sound, resequenced** | Right thing, wrong order (for example a feature scheduled before the security fix it depends on) | Merge, move to the phase that makes sense, say why in one sentence |
| **Needs change** | The goal is right, the approach will cause a problem | Raise a condition: their approach, your approach, the risk, your recommendation |
| **Already covered** | The code already does this | Say where (file, line) and drop it from the backlog |
| **Advise against** | The item would create a defect, a security hole, data loss, or work that must be undone later | Raise a condition with severity, and do **not** silently drop it – the user decides |

Never delete a user's plan item without a row somewhere they can see. "I left it out because it was a bad idea" is not acceptable; "CON-004 records that we advised against it, the user insisted, here is their justification and what we built" is.

---

## Part 3 – The conditions file

`qa-findings/requirements/04_CONDITIONS.md` is the decision register for the project. It exists so that six months and three QA versions later, anyone can see **what was decided, who decided it, and why** – including the decisions the user made against advice.

### What goes in it

One row per judgement call that could reasonably have gone another way:

- a default applied because nobody specified one (page size, rate limit, session length, browser support);
- a conflict between the written requirements and a checklist item;
- a conflict between the user's plan and a finding;
- a scope decision (a module skipped, an environment not reachable);
- anything under `ASK_BEFORE` that had to be decided alone;
- anything the user overruled the agent on.

### The two rules that matter

1. **Unreviewed means the agent's decision stands.** If the user has not ticked *Reviewed* on a condition, the agent's decision is applied and work continues. The kit never blocks waiting for a condition to be reviewed – it records and proceeds.
2. **An override needs a justification.** If the user takes the other side of a condition the agent advised against, the agent implements the user's choice, but the row must carry the user's **Justification** text. If the user gives none, write `Justification: none given` – never invent one, never quietly drop the risk note. The agent's original recommendation and its risk note stay in the row untouched.

### Row format

Each condition is one block (the file template is in `04_REQUIREMENTS_TEMPLATE/04_CONDITIONS.md`):

```
### CON-003 – Soft delete or hard delete for cancelled orders
- Area: data / section 10
- Raised by: agent (audit run 2026-03-04, v1)
- Options: (a) hard delete  (b) soft delete with deleted_at  (c) archive table
- Agent decision: (b) soft delete with deleted_at
- Rationale: refunds and disputes need the row for 12 months; hard delete makes the audit log point at nothing.
- Risk if the other option is taken: cancelled orders disappear from the finance export and refunds cannot be traced.
- Reviewed by user: no          # no | yes
- User decision: -              # same | (a) | (b) | (c) | free text
- Justification: -              # REQUIRED when User decision differs from Agent decision
- Applied: agent decision (unreviewed)
- Status: open                  # open | settled | superseded by CON-nnn
- Carried from: -               # the version this condition first appeared in
```

### How conditions are used later

- **In the audit** – a finding that only exists because of a condition names it (`see CON-003`).
- **In the plan** – any item whose shape depends on a condition names it, so the client checklist and the change log inherit the reasoning.
- **During separately instructed implementation** – build according to `Applied:`. If `$ultimate-qa-client report` is later invoked, record a user override in `client/after_implementation/02_Change_Log` § *Built against our recommendation*: what was asked, what we advised, the user's justification, and the risk that remains.
- **In the next QA version** – every condition carries forward. A condition the new version proves wrong is not edited: mark it `superseded by CON-nnn` and write the new one. Conditions are append-only, like findings.

### What never goes in the conditions file

Preferences with no consequence (naming, wording), anything already stated plainly in the requirements, and anything the client must decide – when the optional client workflow is used, client questions belong in `client/questions/` and returned decisions in `client/decisions/`; only the answer comes back here as a condition row.
