# 03 – Implementation ideas (the developer's own planned work)

List here what **you** already intend to build or change. In plan mode the agent treats every idea as a backlog item: it checks whether the code already covers it, maps it to checklist sections, merges it with the audit findings, and gives everything one priority and phase – so your ideas and the review's findings end up in one plan instead of two.

Delete the three example ideas or overwrite them. Keep IDs unique and sequential (`IDEA-001`, `IDEA-002` …). Leave blank what you do not know.

**Priority:** Must = needed before the app is safe to rely on · Should = important, next · Nice = valuable but optional.
**Effort guess:** S = up to 1 day · M = 2–5 days · L = more than 5 days.
**Status:** Idea / Approved / In progress / Done.

---

## Ideas

### IDEA-001: Server-side pagination on all list screens   ← example, edit or delete
- **Related checklist section(s):** 2 (Data handling), 6 (Performance)
- **What:** Replace client-side lists with server-side paginated endpoints (page, page size, sort, filter in the URL) on Orders, Customers and Products.
- **Why / business value:** Screens stay fast as data grows; avoids the site freezing at 10k+ records.
- **Priority:** Must
- **Effort guess:** M
- **Constraints / notes:** keep current URLs working; default 25 per page; add database indexes on sort / filter columns.
- **Status:** Idea

### IDEA-002: Rate limiting on login, OTP and contact forms   ← example, edit or delete
- **Related checklist section(s):** 6 (items 6.8–6.10), 7 (7.3)
- **What:** Add a rate limiter (per IP and per account) on login, password reset, OTP and the contact form; return a friendly "too many attempts" message (HTTP 429).
- **Why / business value:** Stops password guessing and prevents bots running up the SMS bill.
- **Priority:** Must
- **Effort guess:** S
- **Constraints / notes:** use the framework's built-in throttle middleware if available; Redis is available in staging / production.
- **Status:** Idea

### IDEA-003: Audit log for sensitive actions   ← example, edit or delete
- **Related checklist section(s):** 8 (8.11), 7 (7.18)
- **What:** Append-only log of logins, role changes, deletions, refunds, exports and settings changes (who, what, when, from where), viewable by Admin.
- **Why / business value:** Lets the client answer "who changed this?" and resolve disputes.
- **Priority:** Should
- **Effort guess:** M
- **Constraints / notes:** no personal data beyond user ID and IP; keep for 12 months.
- **Status:** Idea

### IDEA-004: <title>
- **Related checklist section(s):**
- **What:**
- **Why / business value:**
- **Priority:** Must / Should / Nice
- **Effort guess:** S / M / L
- **Constraints / notes:**
- **Status:** Idea

### IDEA-005: <title>
- **Related checklist section(s):**
- **What:**
- **Why / business value:**
- **Priority:**
- **Effort guess:**
- **Constraints / notes:**
- **Status:** Idea

---

## Questions for the client

The agent appends here anything that needs a decision (numbered, with options and its recommendation). Answer inline under each question and run again.

-
