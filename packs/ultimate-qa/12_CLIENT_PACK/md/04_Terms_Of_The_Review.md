---
project: <Client or project name>
document: Terms of the review
date: <date sent>
reviewer: <your name or company>
status: For agreement
---

# Terms of the review

**About this document.** The terms on which we carry out the QA review of your system: what is included, how we handle your access and data, what you receive, what you decide, and the limits of the work. Read it together with *About the QA review*. Signing the last page, or confirming in writing that you agree, starts the engagement.

## 1. What is covered

| | |
|---|---|
| **The system** | <name of the system, and the address of the test copy> |
| **Version reviewed** | <branch, release or date of the code we will review> |
| **Areas** | All sixteen areas listed in *About the QA review*, unless limited here: <none / list> |
| **Phase 1 – review** | Reading the code, using the test copy with the accounts you provide, running automated checks, looking for design gaps, and writing the documents listed in section 4. |
| **Phase 2 – building, if separately agreed** | Only the selected items at the fee and timing agreed in section 6. Your checklist records proposed scope; development starts only under a separate agreement. |
| **Destructive testing** | ☐ Not included ☐ Included, on this test copy only: <address>. Never on the live system. |
| **Not covered** | A redesign or rewrite, a penetration test by a security specialist, legal or regulatory compliance advice, and any system, service or repository not named above. |

## 2. What you provide

The items in *What we need from you*: contacts, access to the code, a test copy of the system, one test account per kind of user, the documents you have, and your decisions on what we may and may not do. Delays in providing them move the timeline by the same amount.

## 3. Access, data and confidentiality

- We use test accounts on the test copy only. We never log in as a real customer or a real administrator, and we never touch the live system.
- We do not need, and will not ask for, production passwords, payment-provider dashboards or customer databases.
- No password, key, token or other secret is written into any document we produce, even when we find one where it should not be. We describe where; we never quote the value.
- Everything you give us, and everything we learn about your system, is confidential. We share it only with the people working on this review, and we do not use it for any other purpose.
- When the engagement ends, we delete our working copies of your code and data within <30> days, keeping only the documents we delivered to you.
- You agree not to share our checklist, method or templates outside your organisation; the reports themselves are yours (section 4).

## 4. What you receive, and who owns it

At the end of Phase 1: the Client QA Report and Client Approval Checklist, based on the detailed QA reports and improvement plan. Where needed, a *Questions for you* document is included. After any separately agreed development: the Client Summary and Change Log. These documents are supplied as Word files.

The reports and every other document written about your system belong to you. You may share them with your team, your developers and your advisers. The checklist, the templates and the method behind the documents remain ours; delivering a report does not transfer them.

## 5. Decisions and changes

- Nothing is built as part of the QA review. Any later development follows the separately agreed scope and your recorded decisions.
- Anything you reject or put on hold is recorded with your reason, in your words, and is not raised again as if it were new.
- If you ask us to do something we have advised against, we do it your way and record the remaining risk once, in the final documents.
- Code changes are made one at a time, each with a test and a written way to check it by hand. We do not change anything you have marked out of bounds, add significant dependencies, change the database structure or touch payment code without asking you first.
- Work outside section 1 – another system, a second review some months later, extra rounds of re-testing – is agreed separately in writing before it starts.

## 6. Fees and payment

| | |
|---|---|
| **Phase 1 – review** | <fixed fee or hours × rate> |
| **Phase 2 – building** | <per accepted item, per phase of the plan, or hours × rate> – confirmed after the checklist is returned |
| **Invoicing** | <e.g. 50 % at the start of Phase 1, 50 % on delivery of the documents; Phase 2 on completion of each delivery phase> |
| **Payment terms** | <e.g. 14 days from the invoice date> |
| **Expenses** | None unless agreed in advance in writing (for example a paid device-testing service). |

## 7. Timeline

| | |
|---|---|
| **Start** | When we have received the items in section 2, expected <date> |
| **Phase 1 documents delivered** | <date or number of working days after the start> |
| **Your decisions on the checklist** | Within <10> working days of delivery; later returns move Phase 2 by the same amount |
| **Phase 2** | Agreed when the checklist is returned |

## 8. Limits

- The review is thorough and documented, but no review finds every defect. It reports the condition of the system as reviewed, on the date reviewed, against the checklist; it is not a guarantee that the system will never fail.
- Checks that need a real device, a real inbox, your live site or an outside account are listed for your team with exact steps; they are not performed by us unless agreed.
- We are not responsible for changes made to the system by others, before or after the review, or for how the documents are used once delivered.
- Our total liability under this engagement is limited to the fees paid for it. Neither party is liable to the other for indirect or consequential loss.

## 9. Ending the engagement

Either of us may end the engagement in writing at any time. You pay for the work done up to that point, and we deliver the documents completed up to that point. Sections 3, 4 and 8 continue to apply afterwards.

## 10. Agreement

| | |
|---|---|
| **Client – name, role, signature, date** | |
| **Reviewer – name, signature, date** | |

*These terms are governed by the laws of <country or state>.*
