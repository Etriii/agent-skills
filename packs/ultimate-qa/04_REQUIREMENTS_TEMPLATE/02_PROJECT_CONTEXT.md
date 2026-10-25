# 02 – Project context

What the reviewer needs to know about this project before checking anything. The agent pre-fills what it can detect from the code on the first run and marks it *(detected – please confirm)*. Complete the rest – **Roles and test accounts** and **Core user journeys** are the two sections that most improve the review. Leave blank what you do not know.

Values in *Decisions* override the defaults in the QA template.

---

## 1. Basics

- **Project / app name (as the client calls it):**
- **Client / company:**
- **What the app does (1–2 sentences):**
- **Type:** public website / web app / API / mobile backend / mixed
- **Main users (who they are, roughly how many):**
- **Live URL:**
- **Staging / test URL:**
- **Local dev URL (when running locally):**
- **Repository / branch to review:**
- **Deadline / budget constraints:**
- **Out of scope – do NOT touch or review:**

## 2. Stack

- **Language(s) / framework(s):**
- **Database:**
- **Front end:**
- **Cache / queue / background jobs:**
- **Hosting / infrastructure:**
- **Package manager and versions (Node / PHP / Python / .NET …):**

## 3. Roles and test accounts

One row per role. The reviewer logs in as each of these and every finding says which one was used. **Test / staging accounts only.** Passwords may be left out if the reviewer can create local accounts from seeders or a factory – say so below the table.

| Role | What this role should be able to do | Should NOT be able to | Test account (login) | Password (test only) | Environment |
|---|---|---|---|---|---|
| e.g. Visitor (not logged in) | Browse public pages, book an appointment | See any private page | – | – | – |
| e.g. Patient | See and manage own bookings and invoices | See other patients' data, staff pages | patient1@example.test | ******** | Staging |
| e.g. Receptionist | See all bookings, create / edit bookings, see patient contact details | Delete patients, change settings, refund | reception1@example.test | ******** | Staging |
| e.g. Admin | Everything, including users, settings, exports | – | admin@example.test | ******** | Staging |

- **How to create test accounts if none are listed:** (seeder command, admin panel, factory)
- **Permission matrix:** attach as `04_permission_matrix.md` if you have one (roles × actions with Yes / No).

## 4. Core user journeys (the 3–5 things that must work)

Written as steps a person follows. The reviewer walks through each one end to end as a new user and reports on every step.

1. e.g. *New patient books an appointment:* open the site → Book → choose doctor and date → enter details → confirm → receive confirmation email → see it under My Bookings.
2.
3.
4.
5.

## 5. How to run it locally

- **Command(s):**
- **Env file / example:**
- **Seed / test data command:**
- **Services needed (database, Redis, mail catcher …):**
- **Anything that does not work locally and why:**

## 6. Integrations

| Service | Used for | Test / sandbox available? | Notes |
|---|---|---|---|
| e.g. PayMongo | Consultation fee payment | Yes – test keys in staging | |
| e.g. SendGrid | Transactional email | Yes | |
| e.g. Google Maps | Clinic location | – | |

## 7. Expected scale

- **Users / records now:**
- **Expected in 12 months:**
- **Peak concurrent users (busiest moment):**

## 8. Design and content references

- **Design mockups (Figma etc.):**
- **Brand guidelines:**
- **Supported browsers and devices agreed with the client:**
- **Languages the app must support:**

## 8a. Source documents (requirements, specs, existing plans)

Everything written down that the review should read and check the app against. The agent asks for these at intake and lists here what it read. Give paths - the files stay where they are.

| # | What it is | Path or link | Read? | Notes |
|---|---|---|---|---|
| 1 | Requirements / spec / SRS | | | |
| 2 | User stories or acceptance criteria | | | |
| 3 | Existing implementation plan / roadmap / backlog | | | |
| 4 | Client brief or contract scope | | | |
| 5 | Progress / done-list (see `06_PROGRESS_SOURCES.md`) | | | |

- **Anything the agent could not read** (scanned PDF, password-protected, binary):
- **Which document wins when two disagree:**

## 9. Decisions (override the template defaults where you have decided)

- **Default page size / maximum page size:**
- **Rate limits (login, OTP, password reset, forms, API):**
- **Session timeout (web / mobile):**
- **Password policy:**
- **Performance targets (page load, API response):**
- **Test framework / CI to use:**
- **Coding conventions to follow (link to style guide if any):**
- **Accessibility target (default WCAG 2.1 AA):**
- **Data-protection law(s) that apply (e.g. PH Data Privacy Act, GDPR):**

## 10. Anything else the reviewer should know

Known problems, areas the client complains about, recent changes, things that look odd but are intentional.

-
