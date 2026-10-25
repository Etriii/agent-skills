---
project: <Client or project name>
document: What we need from you
date: <date sent>
reviewer: <your name or company>
status: Please complete and return
---

# What we need from you – before the review starts

**About this document.** The information and access that let us review your system properly. Fill in what you can and leave blank what you do not know – we will ask. Two rules keep everything safe: **test accounts only, never real customers**, and **never send passwords by email** (section 5 explains the alternatives). Everything you give us is used only for this review, and no password, key or secret is ever copied into any document we write.

## 1. Who to talk to

| Role | Name | Email / phone |
|---|---|---|
| Decision maker – approves the work and signs off | | |
| Day-to-day contact – answers our questions | | |
| Developer or technical contact | | |
| Hosting / IT contact (server, domain, backups) | | |
| Best way to reach you (email, chat, call) and hours | | |

## 2. About the system

| Question | Your answer |
|---|---|
| Name of the system, as you call it | |
| What it does, in one or two sentences | |
| Who uses it (kinds of users) and roughly how many | |
| Is it live with real customers today? Since when? | |
| Live address (web address, if public) | |
| Test / staging address (a copy we may use freely) | |
| Type: public website / web app behind a login / API / mobile app backend / mixed | |
| Who built it, and are they still available? | |

## 3. What matters most to you

**The three to five things a user must be able to do.** Written as steps – for example: *"A new customer finds a product, adds it to the basket, pays, and receives a confirmation email."* We walk through each of these from start to finish as a new user.

| # | The task, step by step | Which kind of user |
|---|---|---|
| 1 | | |
| 2 | | |
| 3 | | |
| 4 | | |
| 5 | | |

| Question | Your answer |
|---|---|
| Which screens or features do people complain about? | |
| What are you most worried about? | |
| What would be a disaster if it went wrong? (a wrong charge, a leaked record, a lost order) | |
| Is there a date or event this must be ready for? | |

## 4. Access we need

| Access | Why we need it | How to give it to us | Done? |
|---|---|---|---|
| The source code – a **read-only** invitation to the repository (GitHub, GitLab, Bitbucket) or a zip of the project | Most checks are done by reading the code | Invite the account we give you, or share a zip through a file-sharing link | ☐ |
| Which branch or version to review | So we review the right one | Write it here: ______________ | ☐ |
| The test / staging site address | To use the system as each kind of user | Address in section 2 | ☐ |
| Instructions to run it on our own machine, if they exist | So we can test freely without touching your test site | A README or a few lines from your developer | ☐ |
| Design files or brand guidelines (Figma, PDF), if any | To check screens against the agreed design | A view-only link or the files | ☐ |
| Documents – see section 6 | To check the system against what was agreed | File-sharing link or attachments | ☐ |

We do **not** need access to your live system, your hosting control panel, your customer database or your payment provider's dashboard. If something can only be checked there, we will give your team the exact steps to do it.

## 5. Test accounts – one per kind of user

We log in as each kind of user, and every finding says which one was used. **Test accounts on the test copy only** – never a real customer, never a real administrator.

| Kind of user | What this user should be able to do | What this user must NOT be able to do | Test login (email or username) | Where (test site / our own copy) |
|---|---|---|---|---|
| e.g. Visitor (not logged in) | Browse public pages | See anything private | – | – |
| e.g. Customer | Own orders and profile only | Other customers' data, staff pages | customer1@example.test | Test site |
| e.g. Staff | All orders, customer details | Delete records, change settings, refunds | staff1@example.test | Test site |
| e.g. Administrator | Everything | – | admin@example.test | Test site |
| | | | | |
| | | | | |

**How to give us the passwords – choose one:**

- ☐ Share them through a password manager (1Password, Bitwarden, LastPass) or a one-time secret link – not by email or chat.
- ☐ Set the passwords yourself and tell us by phone.
- ☐ Tell us we may create our own test accounts on the test copy (say how: the sign-up page, an admin panel, or a command your developer gives us).

If you have a written list of who is allowed to do what (a permission matrix), please attach it – it becomes the test plan for the whole permissions area.

## 6. Documents you already have

Attach whatever exists. Nothing here is required, but each one makes the review more precise.

| Document | Have it? | How you will send it |
|---|---|---|
| Requirements, specification, or the original brief | ☐ Yes ☐ No | |
| User stories or acceptance criteria ("it is done when…") | ☐ Yes ☐ No | |
| The contract or agreed scope with the developer | ☐ Yes ☐ No | |
| Designs, mock-ups, brand guidelines | ☐ Yes ☐ No | |
| A list of known bugs, complaints or support tickets | ☐ Yes ☐ No | |
| A plan, roadmap or to-do list of what you already intend to build | ☐ Yes ☐ No | |
| A record of what has already been fixed or built (for a second review) | ☐ Yes ☐ No | |
| Anything else that explains how the business works (a price list, a process document, an example invoice) | ☐ Yes ☐ No | |

If two documents disagree, which one wins? ______________________________

## 7. Services the system connects to

| Service (payment provider, email service, SMS, maps, "sign in with Google"…) | What it is used for | Is there a test / sandbox account we may use? | Notes |
|---|---|---|---|
| | | ☐ Yes ☐ No ☐ Not sure | |
| | | ☐ Yes ☐ No ☐ Not sure | |
| | | ☐ Yes ☐ No ☐ Not sure | |
| | | ☐ Yes ☐ No ☐ Not sure | |

We never send real payments, real emails or real text messages during a review. If a service has no test mode, we check it by reading the code and give your team the steps to test it live.

## 8. What we may and may not do

Tick what applies. Where you leave something blank we assume **no**.

| Permission | Your decision |
|---|---|
| We may run a copy of the system on our own machine with made-up test data | ☐ Yes ☐ No |
| We may create test records (customers, orders, bookings…) on the test site | ☐ Yes ☐ No |
| We may deliberately try to break a **test copy** – bad input, overload, cutting off a supplier, interrupting a payment – and restore it afterwards. **Never the live system.** | ☐ Yes, on: ______________ ☐ No |
| After you approve items in the checklist, we may make the code changes | ☐ Yes ☐ No – our own developer will |
| Anything that is off limits – folders, features, the payment code, live integrations | |
| Areas you want us to skip entirely (section 2 of *About the QA review* lists the sixteen) | |

## 9. Practical details

| Question | Your answer |
|---|---|
| Deadline for the report, if any | |
| Budget or a cap on hours, if any | |
| Language for the documents (English, Filipino, Spanish…) | |
| Browsers and devices you have agreed to support, if written down anywhere | |
| Countries your users are in (decides which data-protection rules apply) | |
| Your name and role as it should appear on the documents | |
| Where to send the finished documents | |

## 10. Anything else

Known problems, things that look odd but are intentional, recent changes, dates the system must not be disturbed (a sale, an enrolment day), anything you want us to know.

-

## 11. Before you send it back

- ☐ Sections 1 to 3 filled in (contacts, the system, what matters most)
- ☐ Repository invitation sent, or a zip shared
- ☐ Test site address given
- ☐ One test account per kind of user, passwords shared safely (section 5)
- ☐ Documents attached or linked (section 6)
- ☐ Permissions ticked (section 8)

Send everything to: ______________________________

Thank you. We will confirm what we received within one working day and tell you when to expect the report.
