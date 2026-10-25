---
project: <Client or project name>
document: How to read your QA report
date: <date sent>
reviewer: <your name or company>
status: For information
---

# How to read your QA report

**About this document.** A short guide to the documents you have received: what to read first, what the words and numbers mean, and what we need back from you. Keep it next to the report.

## 1. Where to start

**If you have fifteen minutes:** open the **Client QA Report**. It gives the overall picture, the top verified risks, the evidence limits, and the proposed changes in plain words.

**If you have an hour:** go through the **Client Approval Checklist** row by row and mark your decisions. Your developer can read the detailed QA reports and improvement plan separately.

**For your developer:** Project Map, Access Matrix, QA Audit Report (all parts), System Gaps Report, Destructive Test Report if there is one, then the Improvement Plan.

## 2. What the results mean

Every one of the 191 checks has one of these results:

| Result | Meaning |
|---|---|
| PASS | Works as it should. We say where we confirmed it. |
| FAIL | Exists but does not work correctly. Written up as a finding. |
| MISSING | Not built at all – for example there is no backup, no rate limit, no activity log. Written up as a finding and proposed as an improvement. |
| N/A | Does not apply to your system, with the reason. |
| NEEDS-MANUAL | Could not be checked from here – it needs a real phone, a real inbox, your live site or a designer's eye. Part 3 of the audit report gives your team the exact steps. |
| FIXED (pending re-test) | Changed after you approved it; waiting for your team to confirm it. |

## 3. Severity, priority, effort and phases

**Severity** says how bad a finding is today:

| Severity | Meaning |
|---|---|
| Critical | The system cannot be used, data can be lost or stolen, or money can be charged wrongly. Fix before anything else. |
| High | A main feature is broken with no reasonable workaround. Fix before release. |
| Medium | Works incorrectly or awkwardly; there is a workaround. |
| Low | Cosmetic or minor. |

**Priority** says how urgent the proposed work is: **Must** – needed before the system is safe to rely on · **Should** – important, next · **Nice** – valuable but optional.

**Effort** is our estimate: **S** – up to a day · **M** – two to five days · **L** – more than five days.

**Phases** are the order we propose to do the work in:

| Phase | What goes in it |
|---|---|
| 1 – Protect | Security, permissions, backups, anything that could cause a breach, a loss of data or a wrong charge |
| 2 – Stabilise | Broken core functions, error handling, speed, lists that will not scale, protection against overload |
| 3 – Grow | Ease of use, accessibility, mobile, messages, search engines, analytics |
| 4 – Sustain | Automated tests, monitoring, a safe release process, documentation and hand-over |

## 4. The reference numbers

You will see short codes throughout. They let every document point at the same thing, and they never change – a finding keeps its number for the life of the system, even across future reviews.

| Code | What it is |
|---|---|
| **QA 8.4** | One of the 191 checks (area 8, check 4) |
| **F-012** | A finding – something wrong or missing, from the audit report |
| **G-002** | A gap – a situation the design cannot represent, from the System Gaps Report |
| **D-001** | A destructive-test finding – what broke when we tried to break it |
| **P-05** | An item in the Improvement Plan and the approval checklist |
| **IDEA-003** | Something your own team already planned to build, merged into the plan |

## 5. How to fill in the Client Approval Checklist

One row per proposed item. For each row, tick exactly one decision:

- **Accepted** – build it.
- **Rejected** – do not build it. Please write why in the *Reason* column; "too expensive for now", "we are retiring that page", "need to ask our lawyer" are all fine reasons.
- **On hold** – not now. Write why, and if you like, when or under what condition ("after the holiday freeze", "once our accountant has confirmed how deposits should appear").

The last column, *Client recommendation*, is for what you would like done instead. Then tick the overall decision at the bottom, sign and date it, and send it back – or simply reply with your decisions in a message.

Accepted rows record your preferred scope. Development starts only after a separate agreement on the work. Rejected and on-hold rows retain your reason in your words.

## 6. If we asked you questions

A separate short document, *Questions for you*, appears only when a decision is genuinely yours to make – for example who may delete a record, or whether an unpaid invoice should block closing an account. Each question gives the options and our recommendation. Nothing that depends on a question is built until it is answered.

## 7. If you disagree with something

Say so, in the checklist or in a message. Your view and your reason are recorded next to ours. If you decide to go a different way from what we recommend, we build your version and note the remaining risk once – it is a record, not an argument.

## 8. What happens next

1. You return the checklist (and answers to any questions).
2. If development is separately arranged, the selected items are built and tested. You then receive the **Client Summary** and **Change Log**.
3. Your team re-tests each delivered change using the steps in the Change Log and signs off.
4. Whenever you want a second review – after a few months of changes, before a big launch – it starts from exactly where this one ended.

## 9. A few terms you may meet

| Term | What it means |
|---|---|
| Staging / test site | A separate copy of the system for testing, with made-up data, so nothing done there affects real customers. |
| Rate limiting / throttling | Limiting how many times one person or program can try something (a login, a code request) in a given time, so it cannot be abused. |
| Pagination | Splitting a long list into numbered pages instead of loading everything at once. |
| Permission / role | What a kind of user is allowed to see and do. A role (Customer, Staff, Admin) is a named bundle of permissions. |
| Audit trail / activity log | A record of who did what and when, so disputes and mistakes can be traced. |
| Backup and restore | A copy of the data kept elsewhere – and the proven ability to bring the system back from it. An untested backup is not a backup. |
| Migration | A scripted change to the structure of the database, applied during a release. |
| Idempotent | An action that has the same effect however many times it is repeated – pressing Pay twice results in one payment. |
| Webhook | An automatic message one service sends to another when something happens, e.g. a payment provider telling your system a payment succeeded. |
| Two-factor authentication (2FA) | A second step at login – a code from an app or a text message – in addition to the password. |
| WCAG | The international standard for making websites usable by people with disabilities; Level AA is the usual target. |
| Penetration test | A security assessment where a specialist tries to break in, with permission, and reports the weaknesses. Recommended where the system handles payments, health or financial data. |
