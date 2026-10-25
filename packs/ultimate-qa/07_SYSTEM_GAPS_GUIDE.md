# 07 – System gaps: finding the holes nobody thought about

The checklist in `02_QA_CHECKLIST.md` finds things that are **wrong**. This file finds things that are **missing from the model of the world** – the cases the team never considered, so there is no code to be wrong. These are the findings clients value most, and no scanner produces them.

Output: `06_System_Gaps_Report` (template §N in `03_OUTPUT_TEMPLATES.md`), written during the audit stage, feeding `04_Improvement_Plan`. Findings here are numbered `G-001`, `G-002` … and, like `F-nnn`, the numbers are permanent for the project.

---

## The worked example – read this first

A library management system. Books have a `quantity_available` column. Lending decrements it, returning increments it. Barcodes are printed per **book**, so all five copies of *Clean Code* carry the same barcode. Every checklist item passes: the form validates, the permissions hold, the pagination works, the loan is saved.

The system is still broken, and here is the chain:

1. The library owns **copies**, but the database only models **titles**. `quantity_available: 5` is a counter, not five things.
2. A loan therefore points at a title, not at a copy. When a book comes back, nobody – not the system, not the librarian – can say **which** copy came back.
3. The barcode is printed from the title, so scanning cannot resolve it either. Two physical books scan identically.
4. Consequences the team has never seen in a bug report because the system cannot detect them: a damaged copy cannot be marked damaged without withdrawing the whole title; a copy lost by a borrower silently becomes "everyone's" loss because the counter is just decremented; the counter drifts out of step with the shelf after any manual correction and there is no way to reconcile it; per-copy history (who has had this copy, how often it is repaired) does not exist; a copy donated by a specific donor, or belonging to the reference-only shelf, cannot be distinguished.
5. The fix is not a bug fix, it is a modelling change: introduce a `book_copy` entity with its own identity and barcode; a loan references a **copy**; availability becomes a derived count of copies with no open loan rather than a stored number.

That is the shape of every gap finding: **the real world has an entity, a state or an event that the system does not represent**, and everything downstream (barcodes, returns, reports, reconciliation) inherits the hole.

Note the second half of it, which is what makes the recommendation credible: copies of the same title *do* share the same ISBN and the same catalogue record – that part of the design is right. The gap is that the thing a borrower borrows, and the thing a scanner scans, is the copy, so the copy needs its own identity and its own barcode alongside the shared ISBN.

---

## How to hunt for gaps

Work from the data model outwards, not from the screens inwards. For every important record in `01_Project_Map` § *Data*, walk the eleven gap classes below and ask the probe questions. Aim for depth on the two or three records that carry the business (loans, orders, bookings, invoices) rather than one shallow pass over everything.

Two habits do most of the work:

- **Follow the physical object.** If something exists outside the database – a book, a room, a seat, a delivery van, a SIM card, a serial-numbered device – ask whether the database can tell two of them apart. Counters (`quantity`, `slots_left`, `available`) are the usual sign that it cannot.
- **Walk the unhappy end of a lifecycle.** Teams model creation carefully and endings badly. Cancelled, returned, expired, refunded, merged, deceased, resigned, closed, withdrawn, transferred – ask what happens to every related record at that moment.

---

## The eleven gap classes

### 1. Identity and granularity (the library case)
The system counts what it should be tracking individually.
- Is there a counter (`quantity`, `stock`, `seats`, `available`) standing in for a set of real, distinguishable things?
- When one of them comes back, is returned, is damaged or is lost, can the system say **which one**?
- Do the printed / scanned identifiers (barcode, QR, serial, plate, room number) resolve to exactly one row?
- Does the thing being transacted (borrowed, booked, sold, assigned) have its own identity, or only its category?

### 2. Lifecycle and end-states
- List every state the record can be in, including the ones no screen shows. Which transitions exist in code, and which real-world transitions have no transition in code?
- What happens to children when a parent ends? A cancelled order's shipment, a deleted user's comments, a closed account's invoices, a withdrawn title's open loans.
- Is there a state the record can enter and never leave, or a state a human can only fix in the database?

### 3. Reversal, correction and the undo path
Teams build the forward path and forget the way back.
- How is a mistake corrected – a wrong loan, a wrong charge, a double booking, a typo in a name that is already on a printed document?
- Is a correction a new event (good: an adjustment, a credit note, a reversal row) or an in-place edit that destroys the history (bad)?
- Who is allowed to correct, is it logged, and can it be corrected twice?

### 4. Concurrency and the last-writer
- Two people act on the same record at the same second: two librarians lend the last copy, two staff approve the same refund, a user double-clicks Submit. What does the system do?
- Is the availability check and the write one atomic operation, or a read followed later by a write?
- Are there unique constraints in the **database**, or only validation in the form?

### 5. Reconciliation with reality
- Where the database mirrors something physical or external (shelf stock, cash drawer, payment provider, warehouse, calendar), how does anyone find out when the two disagree?
- Is there a count / audit / reconcile function at all, and what does it do with a discrepancy – correct silently, or record it as an event?
- If a stored aggregate exists (`total`, `balance`, `available`), can it be recomputed from the underlying rows? If not, it will drift.

### 6. Time, calendars and rules that change
- Overdue, expiry, grace periods, renewals: which timezone, whose working days, what happens over a holiday or a closure?
- Rules that change (a new fine rate, new prices, a new tax): do historical records keep the rule that applied when they were created, or do old records silently re-price?
- Does anything depend on a job actually running (overdue notices, expiry, auto-cancel)? What happens on the day it does not run?

### 7. Money, quantity and rounding
- Is money stored as an integer of minor units, or as a float?
- Where are totals recomputed, and could the total shown to the user differ from the total charged?
- Partial cases: partial payment, partial refund, partial delivery, partial return of a multi-item loan.

### 8. People and roles in the real world
- One person with two roles (a staff member who is also a borrower), a person who leaves and comes back, a duplicate record for the same person, a person acting on behalf of another (parent, secretary, guardian).
- What happens to their records when the account is deleted or the role is removed – to the loans they still hold, to the approvals they gave?

### 9. Uniqueness, matching and merging
- What makes two records "the same"? Email, phone, ISBN, name+birthdate? Can the same real thing be entered twice, and is there any way to merge them afterwards?
- Where an external identifier is trusted (ISBN, SKU, VAT number), what happens when it is wrong, reused, or absent?

### 10. Evidence and accountability
- For every action that could be disputed (a fine, a refund, a deletion, a grade, a payment), can the system answer *who did this, when, and from where* a year later?
- Is the log append-only, and does it survive the deletion of the record it refers to?

### 11. Scale and the second customer
- What breaks at 10x the data, at a second branch / tenant / campus, at a second currency, at a second language?
- Is anything keyed on something that will not stay unique (a name, a title, a date) or hard-coded to one location, one branch, one admin?

---

## Writing a gap finding

Same discipline as an audit finding, plus the modelling part. Every `G-nnn` has:

1. **What the system assumes** – one sentence, stated as the team would state it ("one row per book title, availability is a number").
2. **What is actually true** – the reality it does not capture ("the library owns and lends individual copies, and staff handle them one at a time").
3. **Where you saw it** – the tables and columns, the file and line, and the screen where the assumption surfaces.
4. **The chain of consequence** – three to six numbered steps from the assumption to real harm, as in the example above. This is the part that convinces a client.
5. **A scenario a person can act out today** – "Borrow *Clean Code*, return it damaged, then try to record which copy is damaged" – so the gap is demonstrable, not theoretical.
6. **What the right model looks like** – entity, key, relationships, what becomes derived. Say what stays the same too (the shared ISBN), so the recommendation reads as a correction, not a rewrite.
7. **Migration reality** – how existing data would be converted (five counter units become five copy rows with new barcodes), what has to be re-printed or re-labelled, and what cannot be recovered (which copy each past loan involved – it is gone; say so).
8. **Severity and effort**, using the checklist's definitions. Model changes are usually **Should** or **Must** with **M/L** effort; be honest about that rather than making them sound cheap.

Two failure modes to avoid: proposing a redesign of a system that works (if the counter genuinely is enough – identical, disposable, non-tracked items – say so and move on), and listing generic advice ("consider normalising your schema"). Every gap is specific to this app, with this app's nouns.

---

## Where gaps go in the rest of the kit

- `06_System_Gaps_Report` holds the full write-up.
- Section 15 of `02_QA_CHECKLIST.md` holds the checks that trigger a gap hunt, so gaps get a status in the audit report like everything else.
- Each `G-nnn` accepted for work becomes a `P-nn` in `04_Improvement_Plan`, and a row the client can accept or reject in `05_Client_Approval_Checklist`, phrased without jargon ("the system cannot tell one copy of a book from another").
- A gap the client rejects is not re-raised as new in the next QA version: it is carried forward with its history and the client's earlier reason (see `09_VERSIONING_GUIDE.md`).
