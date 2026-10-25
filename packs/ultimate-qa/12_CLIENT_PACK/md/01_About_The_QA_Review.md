---
project: <Client or project name>
document: About the QA review
date: <date sent>
reviewer: <your name or company>
status: For information
---

# About the QA review

**About this document.** What a QA review of your website, web app or online system involves, what you receive at the end, how the work runs, and what we need from you to start. It is written for owners and managers – no technical background is needed. The companion document, *What we need from you*, is the form to fill in when you are ready to go ahead.

## 1. What a QA review is

QA stands for quality assurance: checking that a system works correctly, is safe, is fast enough, copes with growth, and matches how your business actually operates – before you rely on it, or before more is built on top of it.

Think of a building inspection before people move in. The inspector walks every room with a fixed checklist, notes what is broken, what is missing and what is risky, and hands you a report you can act on. That is what this review does for software.

The review works through **191 checks in 16 areas** (listed in section 2). For every check we record what we looked at, how we checked it, and the result. Where something is wrong or missing, we write it up so that you can understand the problem without help and your developer can fix it without asking questions.

**What it is not.** It is not a redesign or a rewrite of your system, it is not a legal audit, and it is not a full penetration test by a security specialist – where your system handles payments, health or financial data we will recommend one. It is also not a guarantee that nothing will ever go wrong; it is a thorough, documented picture of where the system stands today and a plan to make it better.

## 2. What we check – the sixteen areas

| Area | The question we ask |
|---|---|
| 1. Does everything work as intended | Do the links, buttons, forms, calculations and the main tasks your users perform actually work, end to end? |
| 2. Lists, paging and data | Do screens that show lists stay fast and correct with thousands of records, not just ten? Are dates, money and totals right everywhere? |
| 3. Look and feel | Does it work on phones and tablets, match the agreed design, and look finished? |
| 4. Ease of use and accessibility | Can a first-time user understand it? Can people who cannot use a mouse, or who use a screen reader, use it too? |
| 5. Browsers and devices | Does it behave the same in Chrome, Safari, Firefox and Edge, on Windows, Mac, iPhone and Android? |
| 6. Speed and protection against overload | Are pages fast? What happens when many people use it at once, or when one script hammers the login page? |
| 7. Security | Can someone break in, read other people's data, guess passwords, or find secrets left in the open? |
| 8. Who can see and do what | Does each kind of user – visitor, customer, staff, manager, administrator – see and do only what they should? |
| 9. Connections to other services | Payments, email, text messages, maps, sign-in with Google: do they work, and what happens when one of them is down? |
| 10. Errors and unexpected situations | Lost connection, double clicks, two people editing the same record, a refresh during payment – does the system stay correct? |
| 11. Emails and text messages | Is every message sent once, to the right person, with the right content, and does it arrive? |
| 12. Public website, search engines, analytics | For public sites: can search engines index it properly, and are the visitor numbers you rely on being recorded? |
| 13. Going live safely | Are there separate test and live environments, backups that have been restored at least once, and a way back if a release goes wrong? |
| 14. Re-testing and sign-off | Is there a repeatable way to check that a fix has not broken something else? |
| 15. Does the system match how you really work | Are there situations in your day-to-day business that the system simply has no way to record – for example counting items instead of tracking each one? These are usually the most valuable findings. |
| 16. What happens on a bad day | With your written permission and only on a test copy: what happens when we deliberately feed it bad input, overload it, cut off a supplier or interrupt it mid-payment? |

## 3. What you receive

Every document comes as a Word file. Each one starts with a short plain-English summary; the technical detail for your developer follows, clearly labelled.

| Document | What it is | Who it is for |
|---|---|---|
| **Project Map** | How the system is built and how to run it: every page, every kind of user, the data it holds, the services it connects to. Lets a new developer or manager get oriented in ten minutes. | Your developer, project manager |
| **Access Matrix** | A single table of every page against every kind of user: who can open it today, who should, and what fixes the difference. | Everyone – it is the permission picture of your system |
| **QA Audit Report** | The main report. Part 1 is a summary you can read in five minutes: the overall picture, the top risks in plain words, and the counts. Part 2 goes through all 191 checks with the result and the evidence. Part 3 lists the checks that need a real phone, a real inbox or your live site, with exact steps for your team. | Part 1 for you; the rest for your developer |
| **System Gaps Report** | The situations your system has no way to represent, each written as: what the system assumes, what is actually true in your business, what follows from the difference, and what the right design looks like. | You (the first two paragraphs of each gap), then your developer |
| **Destructive Test Report** | Only if you authorise it. What happened when we deliberately tried to break a test copy – what held, what broke, and what the data looked like afterwards. | Your developer, project manager |
| **Improvement Plan** | Everything found, merged with any plans you already had, as one prioritised list: what to do, why, how much effort, in which order. | Your developer, project manager |
| **Client QA Report** | A plain-language account of the verified findings, evidence limits and proposed changes. | You |
| **Client Approval Checklist** | One row per proposed item for you to mark **Accepted**, **Rejected** or **On hold**, with a space for your reason and for what you would like done instead. Your choices guide any later work. | **You – please fill it in and return it** |
| **Questions for you** | Only if needed: a short numbered list of decisions only you can make, each with the options and our recommendation. | You |

If you go on to have the accepted items built, you also receive:

| Document | What it is | Who it is for |
|---|---|---|
| **Client Summary** | In plain language: what was checked, what was found, what was fixed and how you can see it, what was not done and why (in your own words from the approval checklist), and what remains. Has a sign-off block. | You |
| **Change Log** | Every change made, with the exact steps for a tester to confirm it by hand. | Your tester, your developer |

## 4. How it runs

1. **You send us the information** in *What we need from you*: contacts, addresses, test accounts, documents, and what we may and may not touch. Ten to twenty minutes; leave blank what you do not know.
2. **We review.** We read the code, use the system with the test accounts as each kind of user, run automated checks, look for the situations the design cannot handle, and – only with your permission and only on a test copy – try to break it. Nothing is changed during this step.
3. **You receive the report and the approval checklist.** Read the summary, look at the top risks, and tick your decisions. Where you say no, tell us why – your reason is recorded and never overwritten.
4. **If you separately arrange development**, we build the selected items one small, tested change at a time, in the agreed order.
5. **You re-test and sign off.** The change log gives your team the exact steps for each change.
6. **Later, a second review** picks up exactly where the first left off: every item is carried forward with its history, nothing is forgotten, and nothing already fixed is reported again.

We confirm a timeline once we have seen the size of the system and your answers to the form.

## 5. What we will never do

- **Touch your live system.** Reviewing is read-only; anything that could break something happens on a test copy only, with your written permission, and the test copy is put back afterwards.
- **Use real customer data or real customer accounts.** Test accounts only.
- **Write passwords, keys or other secrets into any document**, even when we find them somewhere they should not be. We describe where; we never quote the value.
- **Change code as part of the QA review**, or change anything you have marked out of bounds. Development is arranged separately.
- **Overwrite your decisions.** Whatever you write in the approval checklist is copied into the final documents in your own words.
- **Share what you give us** with anyone outside the review.

## 6. How findings are written

Every problem is written the way a careful tester would tell you about it: which page, which kind of user we were logged in as, the exact steps, what happened, what should have happened, why it matters to the business, and then a short note for the developer. Each one carries a severity:

| Severity | Meaning |
|---|---|
| Critical | The system cannot be used, data can be lost or stolen, or money can be charged wrongly. Fix before anything else. |
| High | A main feature is broken with no reasonable workaround. Fix before release. |
| Medium | Works incorrectly or awkwardly; there is a workaround. |
| Low | Cosmetic or minor. |

Proposed work carries a priority (**Must** – needed before the system is safe to rely on; **Should** – important, next; **Nice** – valuable but optional) and an effort estimate (**S** up to a day, **M** two to five days, **L** more than five days), so you can decide with the full picture.

## 7. Questions people ask

**Will the review break anything?** No. Reviewing is read-only. The one exception – deliberately trying to break the system – only ever happens on a test copy you have named, with your written permission, and we restore it afterwards.

**Do you need our passwords?** We need test accounts for each kind of user on the test copy of your system – never real customer accounts, and never sent by email. The form explains the safe ways to hand them over.

**Do we have to fix everything you find?** No. You decide item by item. Anything you reject or put on hold is recorded with your reason, and it is not raised again as if it were new.

**What if we disagree with a finding or a recommendation?** Tell us. Your view and your reason are recorded next to ours, and if you decide to go a different way we build your version and note the remaining risk once, without arguing.

**Can you review only part of it – say, security and permissions?** Yes. The review can be limited to any of the sixteen areas.

**What if we do nothing after the report?** You still have a complete, dated picture of the system's condition that any future developer can work from, and the approval checklist stays valid whenever you are ready.

## 8. Next step

Fill in *What we need from you* – as much as you can – and send it back with the documents and access it asks for. We will confirm what we received, ask about anything missing, and tell you when to expect the report.
