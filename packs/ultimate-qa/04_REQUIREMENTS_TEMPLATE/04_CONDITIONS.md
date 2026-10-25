# 04 – Conditions (the decision register)

Every judgement call made during the review lives here: the defaults chosen because nobody specified one, the disagreements between the written requirements and the checklist, the places where the agent advised one thing and the user wanted another.

Two rules govern this file (full explanation in the template's `06_INTAKE_AND_CONDITIONS.md`):

1. **Not reviewed = the agent's decision is applied.** Work never waits for a condition to be ticked. Unreviewed decisions are applied and marked, so you can overrule them any time.
2. **Overriding needs a justification.** If your decision differs from the agent's, the agent builds yours – and the row must say why. If you give no reason, the row says `Justification: none given`. The agent's original recommendation and risk note are never edited away.

**How to use it:** read the rows, change `Reviewed by user:` to `yes`, and fill in `User decision:` (and `Justification:` when you disagree). Leave the rest alone – the agent maintains it. Add your own conditions with the next free number if you want a decision recorded before the agent raises it.

**Numbering:** `CON-001`, `CON-002` … never reused, never renumbered, carried across every QA version. A condition proven wrong later is not edited – it is marked `superseded by CON-nnn`.

---

## Conditions

### CON-001 – <short title of the decision>   <- example, delete or overwrite
- **Area:** <data / security / performance / scope / process> (checklist section if there is one)
- **Raised by:** agent (audit run <date>, v1)  |  user
- **Options:** (a) <option>  (b) <option>  (c) <option>
- **Agent decision:** (b)
- **Rationale:** <why, in one or two sentences a non-specialist can follow>
- **Risk if the other option is taken:** <the concrete consequence>
- **Reviewed by user:** no
- **User decision:** -
- **Justification:** -
- **Applied:** agent decision (unreviewed)
- **Status:** open
- **Carried from:** -

### CON-002 – Page size for list screens   <- example, delete or overwrite
- **Area:** data / section 2
- **Raised by:** agent (audit run 2026-03-04, v1)
- **Options:** (a) 25 per page  (b) 50 per page  (c) infinite scroll
- **Agent decision:** (a) 25 per page, maximum 100, page and sort in the URL
- **Rationale:** nothing in the requirements specifies a page size; 25 keeps the orders list under a second on the current data and matches the kit's default so every project behaves the same.
- **Risk if the other option is taken:** infinite scroll makes rows unlinkable and breaks the "send me this page" workflow the staff use.
- **Reviewed by user:** no
- **User decision:** -
- **Justification:** -
- **Applied:** agent decision (unreviewed)
- **Status:** open
- **Carried from:** -

### CON-003 – Keep the single barcode per title   <- example of an override, delete or overwrite
- **Area:** data model / section 15 (gap G-002)
- **Raised by:** agent (gap hunt 2026-03-05, v1)
- **Options:** (a) give every physical copy its own identity and barcode  (b) keep one barcode per title and a quantity counter
- **Agent decision:** (a)
- **Rationale:** returns, damage, loss and stock counts all need to name the individual copy; the counter cannot be reconciled with the shelf.
- **Risk if the other option is taken:** the library can never say which copy was returned, damaged or lost, and the availability number drifts from reality with no way to correct it.
- **Reviewed by user:** yes
- **User decision:** (b) for now
- **Justification:** "The 4,000 existing books are already labelled and we cannot re-label them before the defence in May. Revisit in v2 after the semester." - user, 2026-03-06
- **Applied:** user decision - counter kept; the agent's model change stays in the plan as P-09, deferred, and the risk is repeated in the change log
- **Status:** settled (revisit in v2)
- **Carried from:** -
