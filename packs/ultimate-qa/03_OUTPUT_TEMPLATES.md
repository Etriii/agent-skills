# 03 – Output Templates

Every QA review produces the numbered audit and plan documents inside `<project root>/qa-findings/v<N>/recommendations/`. Optional client documents are generated separately under `client/` only when `$ultimate-qa-client prepare` runs. Markdown sources go in `md/`, matching Word files in `docs/`. Write each document using these templates, then convert it with `tools/md_to_docx.py` (see `01_QA_AGENT_PROMPT.md` §10).

**Phase 1 → `v<N>/recommendations/md/` and `docs/`**

| # | File | Written in | One-line purpose |
|---|---|---|---|
| 00 | `00_Carry_Over.md` → `.docx` | v2 and later, before anything else | What the previous versions found, what has happened to each item since, and what this version starts from |
| 01 | `01_Project_Map.md` → `.docx` | audit | How the app is built and how to run it – pages, roles, data, integrations, tests |
| 02 | `02_Access_Matrix.md` → `.docx` | audit (future pages added in plan) | Every page and endpoint against every role: current access, intended access, and the pages the plan will create |
| 03 | `03_QA_Audit_Report.md` → `.docx` | audit (statuses updated in implement) | Every checklist item with a status, and every problem written up as a finding |
| 04 | `04_Improvement_Plan.md` → `.docx` | plan | Findings, gaps, destructive-test failures and the developer's ideas merged into one prioritised, phased backlog |
| 06 | `06_System_Gaps_Report.md` → `.docx` | audit stage, when `GAP_HUNT` is on | The holes in the design – what the system has no way to represent, and what follows from that |
| 07 | `07_Destructive_Test_Report.md` → `.docx` | audit stage, only when destructive testing is authorised | What happened when we deliberately tried to break it, and what the data looked like afterwards |

Documents 06 and 07 are written during the audit stage, before the plan, even though their numbers come after it: the numbers identify the document, not the order of work. The order of QA work is 00 → 01 → 02 → 03 → 06 → 07 → 04.

**Optional client workflow → `v<N>/client/md/` and `docs/`** (created only by `$ultimate-qa-client prepare` or its later report command)

| # | File | Written in mode | One-line purpose |
|---|---|---|---|
| 01 | `01_Client_QA_Report.md` → `.docx` | prepare | Plain-language summary of verified findings, evidence limits, and recommendations |
| 05 | `05_Client_Approval_Checklist.md` → `.docx` | prepare | One row per plan item for the client to Accept / Reject / put On hold; client choices remain blank until returned |
| 01 | `after_implementation/01_Client_Summary.md` → `.docx` | report, after implementation | What was checked, fixed, left undone, and why |
| 02 | `after_implementation/02_Change_Log.md` → `.docx` | report, after implementation | Changes and exact manual re-test steps |

Client returns go in `client/decisions/`; client questions go in `client/questions/`. Neither folder is created by core QA. Keep `evidence/` and `archive/` under `recommendations/`, `qa-findings/VERSIONS.md` (§Q), and, whenever something is dropped, `qa-findings/removed/v<N>/REMOVED_ITEMS.md` (§R).

---

## A. Writing rules (apply to every document)

The reader is first a business owner or project manager, second a developer. Write so the first one understands every finding without help, and the second one can act on it without asking questions.

### A1. What every finding must contain

| Part | What to write | Bad | Good |
|---|---|---|---|
| **Title** | The problem, in the words a user would use, with the place | "IDOR in invoice endpoint" | "Patients can open other patients' invoices by changing the number in the address bar" |
| **Where** | Page / screen name **and** its address; for code-only findings the file and line, and the page it affects | "invoice controller" | "*My Invoices → invoice detail*, `/invoices/{id}` (handled by `app/Http/Controllers/InvoiceController.php`, line 42)" |
| **Logged in as** | Role and the test account name from `requirements/02_PROJECT_CONTEXT.md` (never the password) | – | "Patient – test account `patient1`" |
| **How checked** | Used the app (browser or browser tool, device, width) / Ran a command (which) / Read the code (which file) / Not checked | "verified" | "Used the app – Chrome 128 on Windows, local dev build; then read the code" or "Used the app – Playwright (Chromium), 1366 px and 375 px" |
| **What I did** | Numbered steps someone can repeat tomorrow | "tested access control" | "1. Logged in as `patient1`. 2. Opened My Invoices and clicked invoice 1001. 3. Changed 1001 to 1002 in the address bar, pressed Enter." |
| **What happened** | The actual result, plain words, exact on-screen text in quotes | "unauthorised access" | "Invoice 1002 opened in full – another patient's name, address and amount due were visible. No error." |
| **What should happen** | One sentence | – | "An 'Access denied' message, or a redirect back to my own invoices." |
| **Why it matters** | Business impact in plain English (use Appendix A of the checklist) | "security risk" | "Any patient who edits the web address can read other patients' billing details – a data-protection breach and a legal risk for the clinic." |
| **Note for the developer** | Technical cause and location; short | – | "`InvoiceController@show` does `Invoice::findOrFail($id)` with no ownership check. The `Invoice` model has `patient_id`, so the check is one line or a policy." |
| **Suggested fix** | What to do, and the test that proves it | – | "Add an `InvoicePolicy@view` (or `where('patient_id', auth()->id())`) and a feature test: log in as patient A, request patient B's invoice, expect 403." |
| **Severity** | Critical / High / Medium / Low per the checklist definitions | – | "Critical" |
| **Evidence** | File in `evidence/`, or "not captured – code review only" | – | "`evidence/F-003_invoice_1002.png`" |

### A2. Voice

- Plain sentences; specific nouns. "The Save button on Edit Patient" not "buttons". "The Bookings list" not "list views".
- "We" for the review team ("We could not reach the staging site"). Short first-person notes are fine ("I tried this twice").
- No: "leverage", "robust", "seamless", "delve", "it's worth noting", "in conclusion", "as an AI", emoji, exclamation marks, bullet-point summaries after every section, or a closing paragraph that restates the section.
- Explain a technical word the first time it appears: "rate limiting (limiting how many times one person can try something in a minute)".
- Copy exact on-screen text in quotes. Copy exact commands in code formatting.
- When something is fine, say where it is enforced in one line – do not pad.
- When something could not be checked, say so and give the steps. This is a normal, respectable outcome.
- **Client-facing documents never reveal the machinery.** In `client/`: no mention of the `requirements/` folder or its files, the run settings, the template folder, or modes. Ask for what you need through a `client/questions/` document ("question 1 below") and refer to what they gave you as "the decisions you gave us". Internal QA documents may reference `requirements/` in their technical parts.

### A3. Numbering and references

- Findings: `F-001`, `F-002` … in the order they appear in the audit report. Numbers are permanent for the project – on a re-run, a finding that still exists keeps its number; a fixed one keeps its number and changes status; new findings continue the sequence.
- Design gaps: `G-001` (Section 15, written up in `06_System_Gaps_Report`). Destructive-test failures: `D-001` (Section 16, written up in `07_Destructive_Test_Report`). Same rule – permanent for the project, never reused.
- Decisions: `CON-001` in `requirements/04_CONDITIONS.md`. Cite the condition wherever a finding, a plan item or a built change depends on it.
- Checklist items: `QA 8.4`. Recommendations: `R-8.1`. Developer ideas: `IDEA-002`.
- Across versions: numbers never change and are never reused. A finding closed in v1 and broken again in v3 is still the same number, with its history under it.
- Refer to documents by number: "see 01 Project Map, page list".

---

## B. Markdown conventions the converter understands

`tools/md_to_docx.py` turns the markdown into Word. It supports what is listed here – stay within it.

- **Front matter** (metadata) at the very top, between two `---` lines. It becomes the cover block. Every document must have it:
  ```
  ---
  project: Lakeside Clinic – Appointment Booking Portal
  document: 03 – QA Audit Report
  date: 2026-09-05
  reviewer: QA review
  version: v1
  supersedes: -
  status: Draft
  reviewed: Local dev build, commit a1b2c3d (staging not reachable)
  ---
  ```
  `status` is one of: Draft · For approval · Approved · Final. `version` is the QA version (`v1`, `v2` …) and `supersedes` names the version this one replaces, with its date (`-` in v1).
- Headings `#` (document title – use once, right after the front matter) `##` `###` `####`.
- Paragraphs, **bold**, *italic*, `code`, links `[text](url)`.
- Bullet lists (`- `) and numbered lists (`1. `), one level of nesting by two-space indent.
- Tables in pipe format. A header row of empty cells (`| | |`) is treated as "no header" – use it for the key/value block of a finding. Use `<br>` for a line break inside a cell.
- `> ` blockquote → shaded note box.
- Fenced code blocks (```) → monospace box.
- A line with only `---` (after the front matter) → thin horizontal line. A line with only `\pagebreak` → page break. Put a page break before each major part (each checklist section in the audit report).
- `![caption](../evidence/F-003_invoice_1002.png)` on its own line → the picture, scaled to the page width, with the caption underneath. The path is relative to the markdown file; a missing file becomes a visible *[image not found]* note rather than an error.
- `<!-- widths: 1.2, 3, 7.5, 2.3, 3 -->` on the line before a table → column widths in centimetres, scaled to fit the page. Only for tables where the automatic widths come out wrong (a fill-in column that must stay wide, for example).
- These words are colour-coded automatically wherever they appear in a table cell on their own or at the start: `PASS`, `FAIL`, `MISSING`, `N/A`, `NEEDS-MANUAL`, `FIXED`, `Critical`, `High`, `Medium`, `Low`, `Must`, `Should`, `Nice`.

---

## C. Cover block (top of every document)

The front matter renders as the cover. Then the body begins with the document title as a `#` heading and a short *About this document* paragraph (two or three sentences: what it is, who it is for, what to do with it).

---

## D. Template – `01_Project_Map.md`

```markdown
---
project: <project name>
document: 01 – Project Map
date: <YYYY-MM-DD>
reviewer: <REVIEWER_NAME or "QA review">
version: <v1>
supersedes: <previous version and date, or "-">
status: Draft
reviewed: <environment / branch / commit reviewed>
---

# 01 – Project Map

**About this document.** How <project> is built, seen from the outside in: what the app does, who uses it, every page and API endpoint, how permissions and data are handled, and how to run it. Written so a new developer or a project manager can orient themselves in ten minutes. It is the reference the access matrix (02) and the audit report (03) point back to.

## 1. What this app is
Two or three plain-English sentences. Who the users are. Type (public website / web app / API / mobile backend).

## 2. Stack at a glance
| Part | What is used | Version | Where it is defined |
|---|---|---|---|
| Language / framework | | | |
| Database | | | |
| Front end | | | |
| Cache / queue | | | |
| Hosting / infrastructure | | | |
| Package manager | | | |

## 3. How to run it locally
The commands we ran, in order, and what happened (worked / failed and why). What is needed that we did not have (env vars, services, seed data).

## 4. Roles and how permissions are enforced
| Role | Where it is defined | What it can do (from the code) | How it is enforced (middleware / policy / inline / nothing) |
|---|---|---|---|

Test accounts available (names only, from `requirements/02_PROJECT_CONTEXT.md` or seeders): …

## 5. Pages and screens (what a user sees)
| Page / screen | Address | Who can open it | Handled by (file) | Notes |
|---|---|---|---|---|

## 6. API endpoints
| Method | Path | Plain-English purpose | Handler | Login required | Role required | Paginated | Rate limited |
|---|---|---|---|---|---|---|---|

## 7. Data – main records and who owns them
| Record | Table / model | Belongs to (user / organisation / nobody) | Has created_at / updated_at / updated_by | Notes |
|---|---|---|---|---|

## 8. Lists and pagination
| List (page) | Server-side / client-side / none | Default page size | Maximum | Sort / filter in URL |
|---|---|---|---|---|

## 9. Sign-in, sessions and passwords
How login works, where passwords are hashed, session lifetime, 2FA, password reset flow – with file references.

## 10. Rate limiting, caching, background jobs, scheduled tasks
What exists and where; what is absent.

## 11. Integrations
| Service | Used for | Where credentials come from | Test / live separation |
|---|---|---|---|

## 12. Environments and configuration
How dev / staging / production are separated; debug flags; where secrets are expected to live.

## 13. Tests and CI/CD
Framework, what is covered, how to run, current result (with the command and a pointer to `evidence/`). Pipeline if any.

## 14. Errors, logging and monitoring
Global error handling, custom error pages, logging, error tracker, uptime monitoring.

## 15. Inputs we were given
| # | What it is | Path or link | Read? | Notes |
|---|---|---|---|---|
The documents pointed at during intake (spec, user stories, plan, brief, progress list, a returned client pack), one row each: whether it could be read, and what it was used for. List anything that could not be read (image-only PDF, password-protected link) and what that leaves unchecked.

## 16. Things we noticed while mapping
Anything unusual, risky or surprising, one bullet each, with a pointer. These usually become findings in 03 – QA Audit Report.
```

---

## E. Template – `02_Access_Matrix.md`

Written in **audit** mode from the pages and roles found in 01 – Project Map; **plan** mode adds the future pages. On a re-run it is rebuilt from the code, so it doubles as the living permission matrix (checklist QA 8.1).

```markdown
---
project: <project name>
document: 02 – Access Matrix
date: <YYYY-MM-DD>
reviewer: <REVIEWER_NAME or "QA review">
version: <v1>
supersedes: <previous version and date, or "-">
status: Draft
reviewed: <environment / commit>; pages from 01 – Project Map, plan refs from 04 – Improvement Plan
---

# 02 – Access Matrix

**About this document.** Every page and API endpoint against every role: who can open it today, who should, which plan item closes the gap, and the pages the plan will create. Rebuilt on every run, so it stays true.

## 1. How to read the tables
Roles (from 01 – Project Map §4) and test account names. Cell values: **Yes** · **Own only** · **No** (all correct today) · **Open** in bold with a finding number (reachable today but should not be). State that access was checked by using the app and reading the routes – not menu visibility.

## 2. Web pages – current access by role
| Page (address) | <Role 1> | <Role 2> | … | Should be / fixed by |
|---|---|---|---|---|
One row per page from 01 – Project Map §5. The last column: intended rule + plan ref where today is wrong; a dash where today is correct.

## 3. Future pages – do not exist yet, created by the plan
| Future page (planned address) | Created by | Who will open it | What it is for |
|---|---|---|---|
Every **(new page)** from the plan entries. When delivered, rows move up into §2.

## 4. API endpoints – current access by role
Same format as §2, one row per endpoint from 01 – Project Map §6.

## 5. Where the rules live
Two or three lines: how access is enforced today (middleware / policies / nothing, with file references) and what enforces it after the plan. Note that on a re-run every bold cell should have turned plain.
```

---

## F. Template – `03_QA_Audit_Report.md`

```markdown
---
project: <project name>
document: 03 – QA Audit Report
date: <YYYY-MM-DD>
reviewer: <REVIEWER_NAME or "QA review">
version: <v1>
supersedes: <previous version and date, or "-">
status: Draft
reviewed: <environment / branch / commit; browsers / devices used; accounts used (names only)>
---

# 03 – QA Audit Report

**About this document.** The result of checking <project> against the 191-item QA checklist. Part 1 is the summary. Part 2 goes section by section: every item with its status and how it was checked, followed by the findings written up in full. Part 3 lists what a person still needs to test by hand. Part 4 lists assumptions and open questions. Numbers in the summary match the section tables.

## Part 1 – Summary

**Scope:** sections <list or "all 16">. **Checked:** <n> items – PASS <n> · FAIL <n> · MISSING <n> · N/A <n> · NEEDS-MANUAL <n>.

**Overall picture (three or four sentences a client can read):** …

**Top risks (plain English, one line each):**
1. F-003 – Patients can open other patients' invoices … (QA 8.4, Critical)
2. …
3. …
4. …
5. …

**Blockers – must be fixed before the app is safe to rely on:** F-003, F-007 (or "none").

### Summary by section
| Section | Items | PASS | FAIL | MISSING | N/A | NEEDS-MANUAL | Main gaps found |
|---|---|---|---|---|---|---|---|
| 1. Functional Testing | 14 | | | | | | |
| 2. Data Handling: Pagination, Sorting, Filtering & Lists | 14 | | | | | | |
| 3. User Interface (UI) & Design | 11 | | | | | | |
| 4. Usability & Accessibility | 11 | | | | | | |
| 5. Cross-Browser & Cross-Device Compatibility | 8 | | | | | | |
| 6. Performance, Load & Throttling | 14 | | | | | | |
| 7. Security | 18 | | | | | | |
| 8. Permissions, Roles & Access Control | 14 | | | | | | |
| 9. APIs & Third-Party Integrations | 13 | | | | | | |
| 10. Error Handling, Edge Cases & Reliability | 12 | | | | | | |
| 11. Notifications & Communications | 10 | | | | | | |
| 12. Content, SEO & Analytics | 10 | | | | | | |
| 13. Deployment & Release Readiness | 12 | | | | | | |
| 14. Regression Testing & Final Sign-off | 8 | | | | | | |
| 15. Design Gaps & Unmodelled Reality | 12 | | | | | | |
| 16. Destructive & Abuse Resilience | 10 | | | | | | |
| **Total** | **191** | | | | | | |

### All findings at a glance
| ID | Title | Checklist | Severity | Where | Status |
|---|---|---|---|---|---|
| F-001 | | QA 1.3 | High | Booking form `/book` | FAIL |

\pagebreak

## Part 2 – Section by section

## Section 1 – Functional Testing

**How we checked this section:** one or two sentences – what we could run, which accounts, which browser; what we could not.

| ID | Check | Status | How checked | Where / evidence | Finding |
|---|---|---|---|---|---|
| 1.1 | Links | NEEDS-MANUAL | Not checked | Needs a browser crawl of the live site – steps in Part 3 | – |
| 1.3 | Forms – required fields and validation | FAIL | Read the code | Booking form `/book` – `resources/js/pages/Book.vue`; server rules in `app/Http/Requests/BookingRequest.php` miss `phone` | F-001 |
| 1.4 | Forms – valid submission | PASS | Used the app | Booked as `patient1`, confirmation shown and row created (`bookings` id 41) | – |

**Findings in this section**

### F-001 – Booking form accepts a booking with no phone number

| | |
|---|---|
| **Checklist item** | QA 1.3 – Forms: required fields and validation |
| **Status / severity** | FAIL – High |
| **Where** | *Book an appointment* page, `/book` (front end `resources/js/pages/Book.vue`; server `app/Http/Requests/BookingRequest.php`) |
| **Logged in as** | Patient – test account `patient1` |
| **How checked** | Used the app (Chrome 128, local dev build), then read the code |

**What I did**
1. …
2. …
3. …

**What happened:** …

**What should happen:** …

**Why it matters:** …

**Note for the developer:** …

**Suggested fix:** …

**Evidence:** `evidence/F-001_booking_no_phone.png`

(repeat per finding)

### Recommendations for this section (R-1.n)
| Ref | Recommendation | Already in place? | Our view for this project |
|---|---|---|---|
| R-1.1 ★ | Acceptance criteria before building | No | Proposed – Phase 4 |
| R-1.2 ★ | Validate on both sides | Partly – client only | Proposed – with F-001 |

\pagebreak

## Section 2 – …
(repeat for every section in scope; for sections out of scope write one line: "Not in scope for this run.")

\pagebreak

## Part 3 – Still to be tested by a person

Everything marked NEEDS-MANUAL, grouped by what is needed (a phone, a real inbox, the live site, a designer's eye), each with exact steps for **this** app: which page, which account, what to do, what to look for.

| ID | What to test | Needs | Steps (specific to this app) | Result (fill in) |
|---|---|---|---|---|
| 3.1 | Responsive layout | A phone and the staging site | Open `/book` on an iPhone and an Android phone; scroll the whole form; nothing should be cut off or need sideways scrolling | |

## Part 4 – Assumptions and open questions

- **Assumptions we made** (defaults used because nothing was specified): …
- **Questions for the developer / client** (also appended to `requirements/03_IMPLEMENTATION_IDEAS.md`): …
- **Commands run and where their output is:** `evidence/…`
```

---

## G. Template – `04_Improvement_Plan.md`

```markdown
---
project: <project name>
document: 04 – Improvement Plan
date: <YYYY-MM-DD>
reviewer: <REVIEWER_NAME or "QA review">
version: <v1>
supersedes: <previous version and date, or "-">
status: Draft
reviewed: Based on 03 – QA Audit Report v<n> and requirements/03_IMPLEMENTATION_IDEAS.md
---

# 04 – Improvement Plan

**About this document.** One backlog that merges every Fail and Missing from the audit (03 – QA Audit Report), every gap from 06 – System Gaps Report, every failure from 07 – Destructive Test Report, the developer's own ideas (`requirements/03_IMPLEMENTATION_IDEAS.md`) and the ★ recommendations we propose adopting. Each item has a priority, an effort estimate and a delivery phase. This plan does not authorize implementation. An optional client checklist can be prepared separately from it.

## 1. The backlog at a glance
| Plan ref | Title | Closes | Priority | Effort | Phase | Notes |
|---|---|---|---|---|---|---|
| P-01 | Block cross-patient access to invoices, bookings and files | F-003, F-004 (QA 8.4) | Must | S | 1 | One policy covers both |
| P-02 | Rate limiting on login, OTP and the contact form | F-009 (QA 6.8, 6.9), IDEA-002 | Must | S | 1 | |

**Priority:** Must = needed before the app is safe to rely on · Should = important, next · Nice = valuable but optional.
**Effort:** S = up to 1 day · M = 2–5 days · L = more than 5 days.
**Phase:** 1 Protect (security, permissions, backups, data integrity) · 2 Stabilise (broken core functions, errors, performance, pagination, throttling) · 3 Grow (usability, accessibility, mobile, notifications, SEO, analytics) · 4 Sustain (tests, monitoring, CI/CD, documentation, hand-over).

## 2. Phases and totals
| Phase | Items | Total effort | What the client gets at the end of it |
|---|---|---|---|
| 1 – Protect | P-01, P-02, … | ~3 days | … |
| 2 – Stabilise | | | |
| 3 – Grow | | | |
| 4 – Sustain | | | |

\pagebreak

## 3. Plan entries

### P-01 – Block cross-patient access to invoices, bookings and files
- **Closes:** F-003, F-004 (QA 8.4); relates to R-8.1 ★
- **Priority / effort / phase:** Must · S · 1 – Protect
- **What the client will notice:** Patients can only ever see their own records; anything else shows "Access denied".
- **Technical approach:** …
- **Pages affected:** page name(s) with address; write **(new page)** after any page this item creates
- **Files affected:** …
- **Tests to add:** …
- **Risks / assumptions:** …
- **Depends on:** –

(repeat per item, in phase then priority order)

## 4. Where each item lands – page and file
The same plan sorted by *where you will see it* – one row per plan item. Roles use the names from 01 – Project Map §4; write "None – behind the scenes" for config/CI-only items and "Everyone" where all roles are touched. Pages marked **(new page)** do not exist yet; list them again in 02 – Access Matrix (future pages section).
| Plan ref | Page / screen (address) | Roles affected | New page? | Main files |
|---|---|---|---|---|
| P-01 | Invoice detail `/invoices/{id}` · Booking detail `/bookings/{id}` | Patient (locked to own records) | – | policies (new), controllers, `routes/web.php` |

## 5. Developer ideas – where they ended up
| Idea | Our assessment | Result |
|---|---|---|
| IDEA-001 – Server-side pagination on all lists | Bookings list already paginated server-side (`BookingController@index`, 25/page); Patients and Invoices are not | Merged into P-05 |
| IDEA-003 – Audit log | Not present anywhere | P-08, Should, Phase 2 |
| IDEA-004 – … | Already covered by `spatie/activitylog` config | Already covered – no work |

## 6. Decisions needed before we start
Numbered questions, each with the options and our recommendation.

## 6a. Conditions this plan rests on
Every decision from `requirements/04_CONDITIONS.md` that shapes an item here. Say which way it was decided and by whom, so a reader can see why the plan looks like this.

| Condition | Decision applied | Decided by | Plan items affected |
|---|---|---|---|
| CON-002 | 25 rows per page, max 100 | agent (unreviewed) | P-05 |
| CON-003 | counter kept for now, per-copy model deferred | user - see their justification | P-09 |

## 6b. Where the phases came from
Only when the project has its own phase model (`requirements/05_PHASE_MAP.md`). One line: whose phases these are, the mode (mapped or transformed), and anything that did not fit.

## 7. Out of scope for now
What we deliberately left out and why.

Closing line:

> **QA plan complete.** The findings and recommendations are ready for review. Run `$ultimate-qa-client prepare` if client-facing documents are needed. Implementation requires a separate instruction.
```

---

## G2. Template – `client/01_Client_QA_Report.md`

Written only by `$ultimate-qa-client prepare`, using the completed QA audit and improvement plan. Include the QA version, review environment and date, checks run, evidence limits, top verified findings with stable IDs, business impact, priority, and a plain-language summary of proposed fixes. Clearly label every proposal as pending. Never describe a proposed fix as implemented. The client reads this before the approval checklist. Use the same cover block and evidence rules as the other templates.

```markdown
---
project: <project name>
document: 01 – Client QA Report
date: <YYYY-MM-DD>
reviewer: <reviewer>
version: <vN>
status: For approval
reviewed: <environment and commit or date reviewed>
---

# 01 – Client QA Report

## What we checked
<Scope, roles, environment, methods and the checks that could not be completed.>

## What we found
| Ref | Where | What happened | Why it matters | Evidence | Priority |
|---|---|---|---|---|---|

## What we recommend
| Plan ref | Proposed change | Finding refs | Effort | Phase | Decision needed |
|---|---|---|---|---|---|

## What remains uncertain
<Questions and manual or external checks still required, with exact next steps.>

Proposed changes have not been implemented. Record item decisions in 05 – Client Approval Checklist.
```

---

## H. Template – `client/05_Client_Approval_Checklist.md`

Written only by `$ultimate-qa-client prepare` into `client/md/`. The agent fills the left-hand columns from the existing improvement plan and leaves the three client columns empty. The client fills in Decision, Reason and Client recommendation. Returned decisions are stored in `client/decisions/` and preserved verbatim on re-runs. Approval of a proposed item is recorded separately from authorization to implement it.

```markdown
---
project: <project name>
document: 05 – Client Approval Checklist
date: <YYYY-MM-DD>
reviewer: <REVIEWER_NAME or "QA review">
version: <v1>
supersedes: <previous version and date, or "-">
status: For approval
reviewed: Based on 04 – Improvement Plan v<n>
---

# 05 – Client Approval Checklist

**About this document.** Every item we propose to build, one per row, for you to accept or not. Tick one decision per row. If you do **not** accept an item (Rejected or On hold), please write **why** in the Reason column – and, if you want, tell us what to do instead (or under what condition you would accept it) in the last column. Your choices are recorded for planning. The accompanying Client QA Report explains the findings and proposals; work starts only when separately arranged.

## 1. How to fill this in
- **Decision:** ☐ Accepted · ☐ Rejected · ☐ On hold – tick exactly one per row.
- **Reason (required if not Accepted):** your words, one or two sentences. "Too expensive for now", "we are retiring this page next quarter", "need to ask our lawyer" are all fine reasons.
- **Client recommendation (optional):** what you would like done instead, or the condition for accepting later ("do it, but only after the holiday freeze", "use our existing logging service instead").
- Leave a row blank only if you want us to treat it as On hold with no reason given.

## 2. The items
| Plan ref | What we propose (plain words) | Closes | Priority | Effort | Phase | Decision | Reason (required if not Accepted) | Client recommendation (optional) |
|---|---|---|---|---|---|---|---|---|
| P-01 | Block cross-patient access to invoices, bookings and files | F-003, F-004 (QA 8.4) | Must | S | 1 | ☐ Accepted ☐ Rejected ☐ On hold | | |
| P-02 | Rate limiting on login, one-time codes and the contact form | F-009, IDEA-002 | Must | S | 1 | ☐ Accepted ☐ Rejected ☐ On hold | | |

(one row per plan item, in phase then priority order – same order as 04 – Improvement Plan §1)

*Priority: Must = needed before the app is safe to rely on; Should = important, next; Nice = valuable but optional. Effort: S = up to a day, M = 2–5 days, L = more than 5 days.*

## 3. Overall decision
| | |
|---|---|
| **Overall** | ☐ Accept all rows as ticked above ☐ Accept Must items only ☐ Discuss first (list refs): ______________ |
| **Client / product owner – name, signature, date** | |

## 4. Anything else you want us to know
Free space for the client: constraints, dates, budget, priorities we got wrong, items we missed.
```

---

## I. Template – `client/questions/01_Questions_For_The_Client.md`

Written only during the optional client workflow when information is needed from the client. Lives in `client/questions/`, numbered like every other output (`01_Questions_For_The_Client`, `02_Information_We_Need`, …), plain language only, converted to `.docx`. When answers come back, record them in `client/decisions/` and update internal inputs where appropriate.

```markdown
---
project: <project name>
document: client question 01 – Questions for the client
date: <YYYY-MM-DD>
reviewer: <REVIEWER_NAME or "QA review">
version: <v1>
supersedes: <previous version and date, or "-">
status: For approval
reviewed: Questions arising from the review and the improvement plan
---

# Questions for the client

**About this document.** A few things only you can decide or provide. Each question is numbered, with the options and our recommendation where we have one – write your answer in the space under it (or just reply to us with the numbers). Nothing gets built on an open question: the items that depend on one are on hold until it is answered.

## 1. <Question in plain words>
- **Why we ask:** one sentence – what depends on this.
- **Options:** a) … b) … c) …
- **Our recommendation:** …
- **Your answer:** ______________________________________________

## 2. <Next question>
…

## Information we still need
| # | What we need | Why | How to give it to us | Received? |
|---|---|---|---|---|
| 1 | e.g. the clinic's price list | To check the fee calculations | Email or a photo is fine | ☐ |
```

---

## J. Template – `client/after_implementation/01_Client_Summary.md`

Written only by `$ultimate-qa-client report` after separately authorized implementation, into `client/after_implementation/`. Plain language only. No file paths, no code, no jargon without an explanation.

```markdown
---
project: <project name>
document: 01 – Client Summary (after implementation)
date: <YYYY-MM-DD>
reviewer: <REVIEWER_NAME or "QA review">
version: <v1>
supersedes: <previous version and date, or "-">
status: Draft
reviewed: <environment reviewed, in plain words – e.g. "the test copy of the site as of 5 Sep 2026">
---

# 01 – Client Summary and proposal

**About this document.** A plain-language account of what we checked in <project>, what we found, what was implemented under the separately agreed scope, what remains open, and what your team needs to re-test. The technical detail and original proposals remain in the QA reports and improvement plan.

## 1. What we checked
Two or three sentences: which version, where, with which accounts (roles, not passwords), on which devices; what could not be checked and why.

| Area | Items checked | Pass | Fail | Missing | Not applicable | Still to test by hand | Main gaps found |
|---|---|---|---|---|---|---|---|
| 1. Functional Testing | 14 | | | | | | |
| … | | | | | | | |
| **Total** | **191** | | | | | | |

## 2. What we found – the important things
For each of the top issues (usually 5–10): a heading in plain words, where it shows up (page name), what it means for the business, and the reference.

### Patients can see other patients' bills
On the *My Invoices* page, a patient who changes the number in the web address can open any other patient's invoice. **This means:** private billing information is exposed – a data-protection breach and a legal risk. *(F-003, Critical)*

## 3. What we fixed
One row per delivered item: what changed and how the reader can see it for themselves.

| Ref | What changed | How you can see it |
|---|---|---|

## 3a. Not implemented, and why
One row per item that was not built. For rows you rejected or put on hold, the Reason column repeats **your own words** from 05 – Client Approval Checklist ("no reason given" if the column was blank), plus your recommendation if you wrote one. For rows we could not do (needed a decision, server access, or permission under our ask-first rules), the reason says what is needed to unblock it.

| Ref | What it was | Decided by | Reason | Your recommendation / what unblocks it |
|---|---|---|---|---|
| P-07 | Confirm-before-delete on patient records | Client – On hold | "Need to check retention rules with our lawyer first" | Revisit after legal advice |

## 4. What remains proposed
| Ref | Finding (what is missing or broken) | Impact on the business | What we will implement | Priority | Effort | Phase |
|---|---|---|---|---|---|---|
| P-01 | Patients can open other patients' records | Data breach and legal risk | Server-side checks so every record is only visible to its owner, plus automated tests for each role | Must | S | 1 |

*Priority: Must = needed before the app is safe to rely on; Should = important, next; Nice = valuable but optional. Effort: S = up to a day, M = 2–5 days, L = more than 5 days.*

## 5. Proposed delivery phases
| Phase | Focus | Items | Estimated duration | Notes |
|---|---|---|---|---|
| 1 – Protect | Security, permissions, backups, data integrity | | | |
| 2 – Stabilise | Broken core functions, error handling, performance, pagination, throttling | | | |
| 3 – Grow | Usability, accessibility, mobile, notifications, SEO, analytics | | | |
| 4 – Sustain | Automated tests, monitoring, pipeline, documentation, hand-over | | | |

## 6. Decisions we need from you
Numbered, each with options and our recommendation, in plain words.

## 7. Sign-off for the delivered work
| | |
|---|---|
| **Decision** | ☐ Delivered items accepted after re-test ☐ Accepted with remarks (list): ______________ ☐ Not accepted |
| **Client / product owner – name, signature, date** | |
| **Developer / supplier – name, signature, date** | |

*Approving or rejecting future work happens in 05 – Client Approval Checklist (in `client/`), not here.*
```

---

## K. Template – `client/after_implementation/02_Change_Log.md`

```markdown
---
project: <project name>
document: 02 – Change Log (after implementation)
date: <YYYY-MM-DD>
reviewer: <REVIEWER_NAME or "QA review">
version: <v1>
supersedes: <previous version and date, or "-">
status: Draft
reviewed: Implemented on branch <name>, commits <first>..<last>
---

# 02 – Change Log

**About this document.** What was changed in <project> to close the approved items, in the order it was done, with the exact steps a tester should follow to confirm each change. Every entry corresponds to one commit. Items are marked *FIXED (pending re-test)* in 03 – QA Audit Report until a person has re-tested them.

## 1. Approved and done
| Plan ref | Closes | Commit | Status |
|---|---|---|---|
| P-01 | F-003, F-004 | `a1b2c3d` | FIXED (pending re-test) |

## 2. Accepted but not done, and why
Word the "What is needed" column for the client: point at a numbered question in `client/questions/` or at a person – never at internal files or settings.
| Plan ref | Reason | What is needed |
|---|---|---|

## 2a. Rejected or on hold by the client
The client's Decision, Reason and recommendation, copied verbatim from 05 – Client Approval Checklist ("no reason given" where the column was blank). Nothing in these rows was built.
| Plan ref | Decision | Client's reason | Client's recommendation |
|---|---|---|---|

## 2b. Built against our recommendation
Where the decision went the other way. A record, not a complaint: what was asked for, what we advised, the reason given, and the risk that therefore remains. One row per condition where the applied decision differs from ours.

| Condition | What was built | What we recommended | Reason given | Risk that remains |
|---|---|---|---|---|
| CON-003 | Kept one barcode per title and a quantity counter | One identity and barcode per physical copy | "The 4,000 existing books are already labelled and we cannot re-label them before May." | Returns, damage and loss still cannot name the individual copy; the availability number will keep drifting from the shelf |

\pagebreak

## 3. Changes in detail

### P-01 – Block cross-patient access to invoices, bookings and files
- **Closes:** F-003, F-004 (QA 8.4)
- **Commit:** `a1b2c3d` – `F-003: block cross-patient invoice access (QA 8.4)`
- **Files changed:** …
- **What changed, in plain words:** …
- **New behaviour:** …
- **How to verify by hand:** 1. Log in as `patient1`. 2. Open My Invoices, click any invoice. 3. Change the number in the address bar to another invoice. **Expect:** "Access denied" page, not the invoice.
- **Tests added:** `tests/Feature/InvoiceAccessTest.php` – patient A requesting patient B's invoice gets 403; owner gets 200.
- **Assumptions:** …
- **Rollback:** revert the commit; no data changes.

(repeat per item)

## 4. Re-test list for the tester
| Ref | Page / address | Log in as | Steps | Expect | Result (fill in) |
|---|---|---|---|---|---|

## 5. Test suite and linter after the changes
Command run, result, pointer to `evidence/`.
```

---

## L. Template – `recommendations/README.md`

```markdown
# Recommendations – Phase 1 QA review outputs for <project>, version <vN>

Generated by the QA template. This folder is ignored by git. Markdown sources are in `md/`, Word documents in `docs/`. The optional client package is created separately under `../client/` only when requested.

| # | File (in `docs/`) | What it is | Who should read it |
|---|---|---|---|
| 00 | `00_Carry_Over.docx` | v2 and later: what earlier versions found, what has happened since, what this version starts from | Everyone |
| 01 | `01_Project_Map.docx` | How the app is built and how to run it: pages, roles, data, integrations, tests | Developers, project manager |
| 02 | `02_Access_Matrix.docx` | Every page and endpoint against every role: current access, intended access, future pages | Everyone – it is the permission picture of the app |
| 03 | `03_QA_Audit_Report.docx` | Every checklist item with a status, plus each problem written up as a finding (where, who, steps, what happened, why it matters, note for the developer) | Everyone – Part 1 for the client, Part 2 for developers |
| 04 | `04_Improvement_Plan.docx` | Findings, gaps, destructive-test failures and the developer's ideas merged into one prioritised, phased backlog | Developers, project manager |
| 06 | `06_System_Gaps_Report.docx` | The holes in the design: what the system has no way to represent, and what follows from that | Client (first two paragraphs of each gap), developers |
| 07 | `07_Destructive_Test_Report.docx` | What happened when we deliberately tried to break it, on a test environment, with permission | Developers, project manager |
| – | `evidence/` | Command outputs, screenshots and logs referred to by the findings | Developers |
| – | `archive/<date>/` | Previous drafts within this version, kept automatically on every re-run | – |

**Reading order for QA:** 01, 02, 03, 06, 07, 04. The optional client package has its own reading order.
```

---

## M. Template – `client/README.md`

```markdown
# Client QA package for <project>, version <vN>

Generated only by `$ultimate-qa-client prepare` from the completed QA recommendations. This folder is ignored by git. Read the QA report, then mark decisions on the approval checklist. Returned decisions belong in `decisions/`; implementation requires a separate instruction.

| # | File | What it is | Who should read it |
|---|---|---|---|
| 01 | `01_Client_QA_Report.docx` | Plain-language QA findings and recommendations | Client / business owner |
| 05 | `05_Client_Approval_Checklist.docx` | Decisions on proposed items | Client / business owner |
| – | `after_implementation/` | Summary and change log, created only after separately authorized work | Tester, client |
| – | `archive/<date>/` | Previous drafts within this version, kept automatically on every re-run | – |

**Reading order:** 01, then 05. Markdown sources are in `md/`, Word documents in `docs/`.
```

---

## N. Template – `06_System_Gaps_Report.md`

Written in the audit stage, after the checklist pass, whenever `GAP_HUNT` is on. Method and the worked example: `07_SYSTEM_GAPS_GUIDE.md`. Findings are `G-nnn`.

```markdown
---
project: <project name>
document: 06 – System Gaps Report
date: <YYYY-MM-DD>
reviewer: <REVIEWER_NAME or "QA review">
version: <v1>
supersedes: <v0 date, or "-">
status: Draft
reviewed: <environment / branch / commit reviewed>
---

# 06 – System Gaps Report

*About this document.* The audit report lists things that are wrong. This one lists things that are **missing from the design** – cases the system has no way to represent, so nothing in the code can be blamed for them. Each gap is written as an assumption, the reality it does not cover, and what follows from that. Read the first two paragraphs of each gap even if you skip the technical parts.

## 1. Summary

| Gap | Title | Area | Severity | Effort | Client decision needed |
|---|---|---|---|---|---|
| G-001 | | | | | |

<one paragraph in plain English: how many gaps, which one matters most, and what happens if none of them are addressed>

## 2. The gaps

### G-001 – <short title in the project's own nouns>

| | |
|---|---|
| **Checklist** | QA 15.1, QA 15.2 |
| **Where** | <tables and columns, file:line, and the screen where it shows> |
| **Found by** | <Read the code / Used the app – which account, which page> |
| **Severity** | <Critical / High / Medium / Low> |
| **Effort** | <S / M / L> |
| **Condition** | <CON-nnn, or "-"> |

**What the system assumes.** <one sentence, as the team would state it>

**What is actually true.** <the reality it does not capture>

**What follows from it.**
1. <step>
2. <step>
3. <the real harm, in the client's terms>

**See it for yourself.** <a scenario a person can act out today, with the account and the screens>

**What the right model looks like.** <entity, key, relationships, what becomes derived – and what stays exactly as it is>

*Note for the developer.* <schema sketch, constraints, where the code would change>

**Migrating the existing data.** <how today's rows convert, what must be re-issued or re-printed, and what cannot be recovered>

## 3. Considered and not raised

Places we looked at and decided were fine, so nobody re-opens them later.

| Area | Why it is fine as it is |
|---|---|

## 4. Needs a person

Gaps we suspect but could not confirm from here, with the exact question to ask the client or the developer.
```

---

## O. Template – `07_Destructive_Test_Report.md`

Written only when the gate in `08_DESTRUCTIVE_TESTING.md` is satisfied. Findings are `D-nnn`. If the gate is not satisfied, do not write this document – record in the audit report that Section 16 was not run and why.

```markdown
---
project: <project name>
document: 07 – Destructive Test Report
date: <YYYY-MM-DD>
reviewer: <REVIEWER_NAME or "QA review">
version: <v1>
supersedes: <v0 date, or "-">
status: Draft
reviewed: <environment / branch / commit reviewed>
---

# 07 – Destructive Test Report

*About this document.* We deliberately tried to break the system: bad input, too much of it, interrupted operations, and dependencies switched off. Everything here was done on a test environment with test data, with permission, and the environment was restored afterwards. "We tried this and it held" entries are as important as the failures.

## 1. Authorisation and environment

| | |
|---|---|
| **Permission given by** | <who, where, when> |
| **Environment** | <exact target – never production> |
| **Data** | <test data / anonymised copy> |
| **Third-party services** | <sandbox only / simulated locally> |
| **Snapshot taken** | <dump file or reset command, and the app version / commit> |
| **Restored afterwards** | <yes – how it was verified> |
| **Blocks not run** | <which, and why> |

## 2. Summary

| Block | Tests run | Held | Broke | Worst outcome |
|---|---|---|---|---|
| D-A Input abuse | | | | |
| D-B Boundaries | | | | |
| D-C Concurrency and repetition | | | | |
| D-D Resource pressure | | | | |
| D-E Dependency failure | | | | |
| D-F Interruption and state corruption | | | | |
| D-G Recovery | | | | |

<one paragraph in plain English: what would happen today if the system met a bad day – a burst of traffic, a provider outage, a user hammering the button>

## 3. What held

| Ref | What we tried | What the system did |
|---|---|---|

## 4. What broke

### D-001 – <short title>

| | |
|---|---|
| **Block** | <D-E Dependency failure> |
| **Checklist** | QA 16.7 |
| **Where** | <page + address, or endpoint, or job – and file:line> |
| **Account / role** | <test account used> |
| **Severity** | <Critical / High / Medium / Low> |

**What we did to it.** <the exact abuse: the input, the request, the command – verbatim, so it can be repeated>

**What happened.** <what the user saw, what the logs said>

**The state of the data afterwards.** <the important part: what was left half-written, wrong, or unrecoverable>

**Did it recover by itself?** <a retry / refresh / the next job run fixed it | needs a human with database access>

**What should have happened.** <one sentence>

**Why it matters.** <plain English, in the client's terms>

*Note for the developer.* <transaction boundary, timeout, retry, constraint – where the fix belongs>

**Evidence.** `evidence/<file>`

## 5. Left for a person

Tests that need a real device, a real provider account, or a bigger environment than we had – with the exact steps.

## 6. Clean-up

What was created or changed during testing, and confirmation that it is gone.
```

---

## P. Template – `v<N>/00_Carry_Over.md` (second and later versions only)

The first document written when a new QA version opens, before any new checking. Rules: `09_VERSIONING_GUIDE.md`.

```markdown
---
project: <project name>
document: 00 – Carry Over
date: <YYYY-MM-DD>
reviewer: <REVIEWER_NAME or "QA review">
version: <v2>
supersedes: <v1, YYYY-MM-DD>
status: Draft
reviewed: <environment / branch / commit reviewed>
---

# 00 – Carry Over from <v1>

*About this document.* What the previous review found, what has happened to each of those items since, and what this version starts from. Nothing from an earlier version is forgotten: every item below is either closed, still open, removed with a reason, or coming back.

## 1. This version

| | |
|---|---|
| **Version** | v2 |
| **Previous version** | v1, <date> |
| **Trigger** | <the keyword the user typed> |
| **Code reviewed** | <branch / commit / date range since the last version> |

## 2. Where the progress information came from

| Source | Kind | Covers | How much we relied on it |
|---|---|---|---|

<one line on what was verified in the code rather than taken on trust>

## 3. Carry table

| Ref | Title | From | Carry state | Evidence for that state |
|---|---|---|---|---|
| F-012 | | v1 | CLOSED-VERIFIED | <file:line, or the journey we re-ran> |
| G-002 | | v1 | OPEN-CARRIED | <still present at file:line> |

## 4. Closed since the last version

| Severity | Closed | Still open |
|---|---|---|
| Critical | | |
| High | | |
| Medium | | |
| Low | | |

<one plain-English paragraph the client can read: what the team achieved between the versions>

## 5. Regressions

| Ref | Title | Fixed in | Broken again in | What changed |
|---|---|---|---|---|

## 6. Removed in this version

<short list pointing at `../removed/v2/REMOVED_ITEMS.md`>

## 7. Conditions still standing

| Ref | Decision | Applied | Still valid? |
|---|---|---|---|
| CON-003 | | user decision | <yes | superseded by CON-011> |
```

---

## Q. Template – `qa-findings/VERSIONS.md`

Plain markdown, no front matter, never converted to Word. Newest version at the top; append a section at the end of every version.

```markdown
# QA versions for <project>

One section per QA version, newest first. Read this to see the whole history at a glance.

## v2 – <date> (supersedes v1, <date>)
- Trigger: <keyword typed>
- Progress sources: <paths>
- Carried: <n> items (<n> closed-verified, <n> closed-claimed, <n> open, <n> regressed, <n> rejected-standing)
- Removed: <n> (see `removed/v2/REMOVED_ITEMS.md`)
- New in this version: <n> findings, <n> gaps, <n> destructive findings
- Conditions: <n> new, <n> superseded
- Outcome: <plan refs; what the client accepted, rejected, put on hold>

## v1 – <date>
- Trigger: first review
- ...
```

---

## R. Template – `qa-findings/removed/v<N>/REMOVED_ITEMS.md`

One file per version folder, cumulative. Every removal needs a real reason and a named decider.

```markdown
# Removed in v<N>

Items that were part of an earlier version of this review and are no longer carried forward. Nothing here is deleted – the original text of each item is kept in this folder. If any of them becomes relevant again it comes back under its original reference, never as a new finding.

| Ref | Title | First appeared | Removed in | Reason | Decided by | Restore how |
|---|---|---|---|---|---|---|
| F-018 | | v1 | v2 | <why – a reason, not a category> | <user (chat, date) / client (approval checklist) / agent> | <what would bring it back> |

## Documents removed

| File | From | Reason | Kept at |
|---|---|---|---|
```

---
