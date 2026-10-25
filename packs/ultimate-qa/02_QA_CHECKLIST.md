# 02 – QA Checklist (machine-readable)

> **Part of the QA template.** Read after `01_QA_AGENT_PROMPT.md`. This Markdown checklist is the review source. A separate printable Word checklist may be available in the full template checkout; it is optional for running the skill.
>
> **How the IDs are used in the outputs:** a checklist item is referred to as `QA 6.8`; a finding raised against it gets its own number `F-012`; a recommendation from a "Recommended to implement" list is referred to as `R-6.2` (section 6, recommendation 2). Ideas from the project's `requirements/03_IMPLEMENTATION_IDEAS.md` are `IDEA-001` and so on. Section 15 findings (design gaps) are `G-nnn`, Section 16 findings (destructive tests) are `D-nnn`, and decisions recorded in `requirements/04_CONDITIONS.md` are `CON-nnn`.
>
> Every item has two columns: **What to check** and **How to check it** (written as steps a human tester would follow). Results are never written into this file – they go into the project's `qa-findings/v<N>/recommendations/` folder.

## Status values

| Status | Meaning |
|---|---|
| PASS | Verified working as described (cite evidence). |
| FAIL | Exists but does not work correctly → bug. |
| MISSING | Not implemented at all → proposed improvement (client proposal). |
| N/A | Does not apply to this project (say why). |
| NEEDS-MANUAL | Cannot be verified from code alone; a human must check with a browser, device or external service. Give exact steps. |
| FIXED (pending re-test) | Changed in *implement* mode; a human still has to re-test it. |

## How it was checked (write one of these on every finding)

| Method | Meaning |
|---|---|
| Used the app | Opened the page in a browser / called the running app and did the steps. Say which browser, device and account. |
| Ran a command | Ran a test, linter, audit or script and read the output. Say which command. |
| Read the code | Found the answer by reading source files. Say which file and line. |
| Not checked | Could not check it here (needs a real device, an external service, production data, a human eye). Give the exact steps for a person to do it. |

## Severity (for FAIL / MISSING)

| Level | Meaning |
|---|---|
| Critical | App unusable, data loss/theft possible, or money charged wrongly. Fix before anything else. |
| High | Main feature broken, no reasonable workaround. Fix before release. |
| Medium | Works incorrectly or inconveniently; workaround exists. |
| Low | Cosmetic / minor. |

## 1. Functional Testing

**What this means:** Functional testing asks one question of every feature: does it do what it is supposed to do? It covers every link, button, form, menu and process in the website or app. It is the foundation of QA – if a feature does not work, its speed, design and security do not matter yet.

| ID | What to check | How to check it |
|---|---|---|
| 1.1 | Links (internal, external, social media) | Click every link on every page, including the header, footer and social media icons. Each must open the correct page with no 'Page not found' (404) error. External links should open in a new tab so visitors do not lose your site. For large sites use a free link checker (e.g. W3C Link Checker, Screaming Frog). |
| 1.2 | Buttons | Click every button and confirm it does exactly one thing, once. Double-click quickly – the action must not happen twice (e.g. two orders created). Buttons that should not be available yet (e.g. Submit before a form is complete) should look disabled and do nothing. |
| 1.3 | Forms – required fields and validation | For each form: submit it empty, then with only some fields filled. Every required field must be clearly marked and show a clear message when missing. Enter wrong formats (letters in a phone field, 'abc' as an email, a birth date in the future) and confirm they are rejected with a helpful message. |
| 1.4 | Forms – valid submission | Fill each form correctly and submit. Confirm a success message appears, the data is actually saved (check the admin panel or database) and any follow-up action happens (confirmation email, redirect to the next page). |
| 1.5 | Forms – unusual input | Type very long text (1,000+ characters), special characters (é, ñ, ü, emoji, quotes, < >), extra spaces before and after words, and copy-pasted text. The app should accept it or politely reject it – never crash or display garbled text. |
| 1.6 | Navigation | Open every menu and sub-menu on desktop and mobile. Confirm breadcrumbs, the logo (should go to the home page), footer links and the browser Back button all take the user where expected. The current page should be highlighted in the menu. |
| 1.7 | Site search | Search for a common word, a rare word, a misspelled word, an empty search and special characters. Results should be relevant, and 'no results' should show a friendly message with suggestions rather than a blank page. |
| 1.8 | Core user journeys (end to end) | List the 3–5 most important things a user does (e.g. sign up → verify email → log in → place order → receive confirmation → log out). Walk through each one from start to finish as a brand-new user. Every step must complete without help from a developer. |
| 1.9 | Create, view, edit and delete records | For every type of record in the system (customers, products, orders, posts, etc.): create one, find it, edit it and delete it. Confirm the change appears everywhere it should (lists, reports, dashboards, emails). |
| 1.10 | Calculations and business rules | Check every number the app calculates – totals, tax, discounts, shipping, quantities, dates and deadlines – against a calculator or spreadsheet. Test the rules at their boundaries (e.g. a discount that applies from exactly 10 items: test 9, 10 and 11). |
| 1.11 | File upload and download | Upload allowed file types and sizes and confirm they work. Then try a disallowed type (e.g. .exe), an oversized file, and a file with a very long name or special characters. Rejections must show a clear reason. Download files and confirm they open correctly and are the right file. |
| 1.12 | Error messages | Trigger errors deliberately and read the messages. Each should be in plain language, say what went wrong and what to do next, and never show technical details such as code, file paths or database text. |
| 1.13 | Confirmations for risky actions | Deleting, cancelling, paying or sending to many people should ask 'Are you sure?' (or offer an undo). Confirm that choosing No or Cancel really does nothing. |
| 1.14 | Multi-step processes (wizards, checkout) | Go forward and backward through each step. Entered data must be kept when going back. Refreshing the page or closing the browser mid-way must not create half-finished records or charge the customer. |

**Recommended to implement after this QA** (★ = strongly recommended for every system). Reference these as R-1.n:

1. ★ Write acceptance criteria before building: for each feature, a short list of 'it is done when…' statements taken straight from this checklist. This removes disagreements about what counts as a bug.
2. ★ Validate on both sides: check input in the browser for instant feedback and again on the server for safety, using one shared set of rules so both agree.
3. Add automated tests for the core user journeys (e.g. with Playwright or Cypress) so they are re-checked automatically after every change.
4. Run an automated link checker on a schedule (monthly, or after every content update).
5. Keep a 'business rules' document with worked examples (e.g. 'Orders over 2,000 get free shipping – 1,999 pays shipping, 2,000 does not'). Testers and developers then use the same examples.

## 2. Data Handling: Pagination, Sorting, Filtering & Lists

**What this means:** Almost every app has screens that show lists – orders, customers, products, messages. These work fine with ten records and break with ten thousand. Pagination means splitting a long list into pages (1, 2, 3…) instead of loading everything at once. This section checks that lists stay correct, complete and fast no matter how much data there is.

| ID | What to check | How to check it |
|---|---|---|
| 2.1 | Pagination – basic controls | On every list, click Next, Previous, First, Last and individual page numbers. The page indicator (e.g. 'Page 3 of 12') and the total count (e.g. '118 items') must be correct. The last page must show the remaining items, not a blank page. |
| 2.2 | Pagination – no duplicates or gaps | Note the last item on page 1 and the first item on page 2. Nothing should be repeated and nothing skipped. Repeat for a few pages. The sort order must stay the same across pages (if sorted by newest first, page 2 continues from where page 1 ended). |
| 2.3 | Pagination – page size | If the user can choose 10 / 25 / 50 / 100 items per page, test each option. The total number of pages should recalculate correctly and the setting should be remembered while browsing. |
| 2.4 | Pagination – edge cases | Test with 0 items (should show an empty-state message, not an error), exactly one page, and a very large number (10,000+). In the address bar, type a page that does not exist (page 999), zero, a negative number or letters (e.g. ?page=abc). The app should show page 1 or a friendly message, never an error page. |
| 2.5 | Pagination – position remembered | Go to page 4, open an item, then go back. Decide what the expected behaviour is (return to page 4, or reset to page 1) and confirm it is consistent everywhere. The same applies after editing or deleting an item. |
| 2.6 | Sorting | Click each sortable column heading up and down. Numbers must sort as numbers (1, 2, 10 – not 1, 10, 2), dates as dates and text alphabetically. The sort must stay applied when moving between pages. |
| 2.7 | Filtering and search on lists | Apply one filter, then several together (e.g. status = Paid AND date = this month). Results and the result count must be correct. 'Clear filters' must reset everything. Filters must stay applied when changing page or sort order. |
| 2.8 | Empty states | Wherever a list can be empty (new account, no results, everything filtered out) a friendly message should appear with a helpful next step (e.g. 'No orders yet – Create your first order'), not a blank space or a spinner that never ends. |
| 2.9 | Large data performance | Load a list containing thousands of records (ask the developer to generate test data). It should appear within a few seconds, and scrolling, sorting and filtering should stay smooth. Watch for the browser freezing. |
| 2.10 | Data formats | Check dates, times, time zones, currency, decimal points, percentages and phone numbers on every screen, in exports and in emails. They must use one consistent format (e.g. 01 Sep 2026, 14:30) and show the correct time zone for the user. |
| 2.11 | Data accuracy | Spot-check that what the screen shows matches what is stored: open the same record in the admin panel or an export and compare. Totals on dashboards must equal the sum of the items in the lists. |
| 2.12 | Export and import | Export a list to CSV / Excel / PDF and open it: correct columns and headers, all rows (not just the current page, unless intended), correct formats. Import a file containing one bad row and confirm the app reports which row and why, rather than failing silently or importing bad data. |
| 2.13 | Bulk actions | Select all items on a page (and 'select all across pages' if offered) and apply an action (delete, export, change status). Confirm it affects exactly the selected items and shows a summary of what changed. |
| 2.14 | Record history | Important records (orders, approvals, customer details) should show when they were created, when they were last updated and by whom. |

**Recommended to implement after this QA** (★ = strongly recommended for every system). Reference these as R-2.n:

1. ★ Use server-side pagination: the server sends only the page requested instead of sending everything and letting the browser cut it up. This is the single biggest fix for slow lists.
2. ★ Set a sensible default page size (20–50) and a hard maximum (e.g. 100) so nobody can request a million items in one go.
3. Keep the page, sort and filter settings in the web address (URL) so a user can refresh, bookmark or share a filtered view.
4. Use one shared formatting function for dates, currency and numbers across the whole app, so a fix in one place fixes every screen.
5. Add 'created at', 'updated at' and 'updated by' fields to every important record from day one – adding them later is much harder.
6. Provide a way to generate realistic test data in bulk so lists can be tested with thousands of records before launch.
7. Run large exports and imports as background jobs and notify the user when the file is ready.

## 3. User Interface (UI) & Design

**What this means:** This section checks how the app looks and feels: does it match the agreed design, does it work on small screens, and does it look professional and consistent? Visual problems rarely stop a feature from working, but they strongly affect whether users trust the product.

| ID | What to check | How to check it |
|---|---|---|
| 3.1 | Responsive layout | View every page on a large desktop (1920 px wide), a laptop (1366 px), a tablet (768 px) and phones (375 px and 360 px). Use the browser's device toolbar (press F12, then the phone icon) and at least one real phone. Nothing should be cut off, overlap or require sideways scrolling. |
| 3.2 | Touch-friendly on mobile | On a real phone, tap every button, link and form field. Targets should be large enough to hit easily (about a fingertip, roughly 44 × 44 px) with space between them. Menus should open and close with a tap. |
| 3.3 | Consistency with the design | Compare each screen with the approved design mockups (Figma, etc.). Fonts, colours, button styles, spacing and logo use should match the brand guidelines throughout. |
| 3.4 | Readability | Body text should be large enough (usually 16 px or more), have strong contrast with the background and not overlap other elements. Long words, names and titles should wrap rather than break the layout. |
| 3.5 | Images and icons | Every image should be the correct one, sharp (not stretched or pixelated) and load on all screen sizes. Missing images should show a placeholder, not a broken-image icon. |
| 3.6 | Loading and feedback states | While something is loading the user should see a spinner, progress bar or placeholder. After clicking Save, the button should show it is working (e.g. 'Saving…') and then confirm success or failure. Nothing should appear to do nothing. |
| 3.7 | Text quality | Read every screen, message and email for spelling, grammar, tone and consistent terminology (do not call the same thing 'Order' on one page and 'Purchase' on another). Confirm all placeholder text ('Lorem ipsum', 'TODO', test names) is gone. |
| 3.8 | Browser tab and favicon | Every page should have a meaningful title in the browser tab, and the site's icon (favicon) should appear in the tab and in bookmarks. |
| 3.9 | Print view (if relevant) | Print (or save as PDF) invoices, receipts, reports and tickets. They should fit the page, leave out menus and buttons, and be readable in black and white. |
| 3.10 | Themes and orientation | If the app offers dark mode, check every screen in both modes. On phones and tablets rotate the device: the layout should adapt to landscape and portrait. |
| 3.11 | Animations and motion | Animations should be short and purposeful; nothing should flash rapidly. The page should not jump around while loading (images and ads should reserve their space). |

**Recommended to implement after this QA** (★ = strongly recommended for every system). Reference these as R-3.n:

1. ★ Build a small design system (a shared set of buttons, form fields, colours and spacing rules) so every new screen automatically looks consistent.
2. Agree the list of supported screen sizes (breakpoints) in writing and design mobile-first.
3. Hold a design review comparing each finished screen with its mockup before it goes to QA.
4. Keep a short writing style guide: product terms, tone of voice, capitalisation and date formats.
5. Give every screen a standard 'loading', 'empty', 'error' and 'success' state from the start, not as an afterthought.

## 4. Usability & Accessibility

**What this means:** Usability asks whether a first-time user can understand and use the app without instructions. Accessibility asks whether people with disabilities – for example users who are blind, have low vision, cannot use a mouse or are colour-blind – can use it too. In many countries accessibility is a legal requirement for public-facing sites, and it improves the experience for everyone, including people on small screens or in bright sunlight.

| ID | What to check | How to check it |
|---|---|---|
| 4.1 | Keyboard-only use | Ignore the mouse. Press Tab to move through every link, button and field on a page. The order should be logical (top to bottom, left to right), the focused item should be clearly highlighted, Enter or Space should activate buttons and Esc should close pop-ups. You must never get stuck inside a component. |
| 4.2 | Screen reader basics | Turn on a screen reader (NVDA on Windows – free; VoiceOver on Mac / iPhone; TalkBack on Android) and move through a key page. Images should be described (alt text), every form field should announce its label, and buttons should say what they do ('Add to cart', not 'Button'). |
| 4.3 | Headings and structure | Each page should have one main heading (H1) and use sub-headings in order (H2, then H3). Screen-reader users navigate by headings, and search engines use them too. |
| 4.4 | Colour contrast | Text must stand out from its background (a contrast ratio of at least 4.5:1 for normal text – check with a free tool such as WebAIM Contrast Checker). Information must never be shown by colour alone: an error field should also have an icon or message, not just a red border. |
| 4.5 | Zoom and text size | Zoom the browser to 200% (Ctrl or Cmd and +). Everything should remain readable and usable without sideways scrolling or overlapping text. |
| 4.6 | Plain language | Show a key screen to someone who has never seen the app. Can they say what the page is for and what to do next within 10 seconds? Labels and instructions should avoid jargon and internal codes. |
| 4.7 | Predictability | The same action should look and behave the same way everywhere (e.g. the main button is always in the same place, delete is always red, saving always shows the same confirmation). |
| 4.8 | Recovery from mistakes | Users should be able to go back, cancel, edit what they entered or undo where possible. Entered data should not be lost when an error occurs. |
| 4.9 | Session and time limits | If the app logs users out after inactivity it should warn them shortly before and give a chance to stay logged in. Work in progress should not be lost without warning. |
| 4.10 | Media | Videos should have captions and audio should have a transcript. Nothing should auto-play with sound. |
| 4.11 | Multiple languages (if applicable) | Switch languages: every piece of text, including error messages and emails, should change. Longer translations should not break the layout. Dates, currency and number formats should follow the chosen language. |

**Recommended to implement after this QA** (★ = strongly recommended for every system). Reference these as R-4.n:

1. ★ Adopt WCAG 2.1 Level AA (the international accessibility standard) as the written target for the project.
2. ★ Run an automated accessibility scan (Lighthouse in Chrome, the axe browser extension or WAVE) on every major page and fix what it finds – these catch roughly a third of issues in seconds.
3. Test with at least one real screen reader before launch, because automated tools cannot judge whether alt text or labels actually make sense.
4. Do a quick usability test with 3–5 people from the target audience: give them tasks, watch silently and note where they hesitate.
5. Use proper HTML elements (real buttons, real form labels, real headings) rather than styled boxes – most accessibility comes free when this is done.

## 5. Cross-Browser & Cross-Device Compatibility

**What this means:** Users arrive on different phones, computers and browsers, each of which can display a page slightly differently. A site that works perfectly in Chrome on the developer's laptop may be broken in Safari on an iPhone. This section makes sure the experience is consistent wherever users are.

| ID | What to check | How to check it |
|---|---|---|
| 5.1 | Browsers | Test the core user journeys in the latest versions of Chrome, Firefox, Safari and Edge. On Android also test Samsung Internet if it is common among your users. Note any differences in layout or behaviour. |
| 5.2 | Older browser versions | Decide which older versions must be supported (based on your audience) and test at least the previous major version of each. Unsupported browsers should see a clear 'please update your browser' message rather than a broken page. |
| 5.3 | Operating systems | Test on Windows, macOS, iOS and Android. Fonts, date pickers, file uploads and pop-ups often behave differently on each. |
| 5.4 | Real devices | Test on at least one real iPhone, one real Android phone and one tablet – not only browser simulators. Real devices reveal keyboard, touch and performance issues that simulators miss. |
| 5.5 | Device features | Where the app uses the camera, location, microphone, notifications or clipboard, test allowing and denying permission. Denying must not break the app; it should explain what the feature needs and how to enable it. |
| 5.6 | Restricted browsers | Test with an ad blocker on, with third-party cookies blocked and in a private / incognito window. Core features should still work or show a clear explanation. |
| 5.7 | Slow and unstable connections | In Chrome DevTools (F12 → Network tab) set throttling to 'Slow 3G' and use the app. Pages should show loading indicators, stay usable and never lose entered data. Also test switching from Wi-Fi to mobile data mid-task. |
| 5.8 | Email clients (if the app sends email) | Open the app's emails in Gmail (web and mobile app), Outlook, Apple Mail and Yahoo. Layout, images and buttons should look right in each. |

**Recommended to implement after this QA** (★ = strongly recommended for every system). Reference these as R-5.n:

1. ★ Publish a written 'supported browsers and devices' list and include it in the project agreement. Anything outside the list is best-effort only.
2. Use your analytics to see which browsers and devices your real users have and prioritise those; do not guess.
3. If you cannot access real devices, use a cloud testing service such as BrowserStack or LambdaTest to test on real hardware remotely.
4. Use widely supported web features and a build tool that automatically adds compatibility code for older browsers.
5. Re-run the browser checks after every major design change, not only at launch.

## 6. Performance, Load & Throttling

**What this means:** Performance is about speed: how quickly pages appear and respond. Load is about capacity: does the app keep working when many people use it at the same time (a sale, a launch, an enrolment day)? Throttling (also called rate limiting) means deliberately limiting how many requests one user or computer can make in a given time, so that one abusive script or bug cannot overwhelm the system or attack it. Slow sites lose customers; overloaded sites go down completely.

| ID | What to check | How to check it |
|---|---|---|
| 6.1 | Page load speed | Run the home page and 3–5 key pages through Google PageSpeed Insights (free: pagespeed.web.dev). Aim for a mobile score of 90+ for content sites and at least 70 for complex apps. Key pages should be usable within about 3 seconds on a normal mobile connection. |
| 6.2 | Core Web Vitals | In the same report check Google's three main measures: LCP (how quickly the main content appears – aim under 2.5 s), INP (how quickly the page reacts to taps and clicks – aim under 200 ms) and CLS (whether things jump around while loading – aim under 0.1). These affect search ranking. |
| 6.3 | Page weight and images | Check the total size of each page (DevTools → Network → 'transferred'). Aim below 2–3 MB. Images should be compressed, served in modern formats (WebP / AVIF), sized for the screen and loaded lazily (only when scrolled into view). |
| 6.4 | Caching and repeat visits | Visit a page, then visit it again. The second visit should be noticeably faster. Static files (images, scripts, styles) should be cached; after a new release users must still receive the updated files (no stale version). |
| 6.5 | Response time of actions | Time common actions with a stopwatch or DevTools: searching, saving, loading a dashboard. Under 1 second feels instant; over 3 seconds needs a progress indicator; over 10 seconds should become a background job. |
| 6.6 | Load testing | Ask the developer to simulate the expected peak number of simultaneous users (e.g. 100, 500 and 1,000) with a tool such as k6, Apache JMeter or Locust against the staging environment. Response times should stay acceptable and there should be no errors. Record the numbers. |
| 6.7 | Stress and recovery | Push the load beyond the expected peak until the app slows or fails. Note the breaking point, and confirm the app recovers by itself when load drops (no manual restart, no corrupted data). |
| 6.8 | Throttling / rate limiting | Ask the developer to send many requests rapidly to the same feature (e.g. 100 login attempts or 200 search requests in one minute). After a defined limit, further requests should be slowed or refused with a clear 'Too many requests, please try again later' message (technically an HTTP 429 response) instead of crashing or silently accepting them. |
| 6.9 | Rate limits on sensitive features | Confirm limits exist specifically on login, password reset, one-time codes (OTP / SMS), sign-up, contact forms and any feature that sends email or SMS or costs money – these are the first targets of abuse. Legitimate users retrying a few times must not be locked out. |
| 6.10 | Rate limit documentation | The limits (per user, per IP address, per API key) should be written down, and API users should be told when they are near or over the limit (e.g. through response headers and a 'Retry-After' value). |
| 6.11 | Long-running tasks | Generating reports, sending bulk emails, imports and exports should run in the background. The user should see progress or be notified when finished; the browser should never sit on a spinning page until it times out. |
| 6.12 | Stability over time | Use the app heavily for an extended period (or run the load test for 30–60 minutes). Memory and CPU on the server should stay flat, not climb steadily – a steady climb suggests a leak that will crash the app days later. |
| 6.13 | Database efficiency | Ask the developer to confirm that fields used for searching, filtering and sorting have database indexes, and that list pages do not run one query per row (the 'N+1 problem' – asking the database 100 times when once would do). Slow-query logs should be reviewed. |
| 6.14 | Third-party scripts | Temporarily disable analytics, chat widgets, ad scripts and social embeds and compare the load time. Anything that adds more than a few hundred milliseconds should load later (deferred) or be reconsidered. |

**Recommended to implement after this QA** (★ = strongly recommended for every system). Reference these as R-6.n:

1. ★ Apply rate limiting to every public-facing endpoint by default, with stricter limits on login, password reset, OTP and messaging features. Return HTTP 429 with a Retry-After header.
2. ★ Set up monitoring and alerts for uptime, response time and error rate (e.g. UptimeRobot, Grafana, Datadog, New Relic) so the team hears about slowdowns before customers complain.
3. Set a performance budget (e.g. 'every page under 2 MB and usable within 3 seconds on mobile') and check it in every release.
4. Turn on compression (gzip or Brotli) on the web server and use a Content Delivery Network (CDN) to serve files from locations close to users.
5. Add an automatic image optimisation step so every uploaded image is resized and compressed.
6. Use a background job queue (e.g. Sidekiq, Celery, BullMQ, Laravel Queues) for anything that takes more than a few seconds.
7. Plan capacity for known peaks (campaigns, launches, deadlines): test at 2–3× the expected load and enable auto-scaling where the hosting platform supports it.

## 7. Security

**What this means:** Security testing asks whether someone with bad intentions could break in, steal or change data, impersonate another user or misuse the app (for example to send spam). Security problems are usually invisible until it is too late, so they must be tested deliberately. The checks below are the basics every system should pass; apps that handle payments, health, financial or personal data should also have a professional penetration test.

| ID | What to check | How to check it |
|---|---|---|
| 7.1 | HTTPS everywhere | Every page and resource must load over https:// with a valid certificate and a padlock icon – no 'Not secure' or 'mixed content' warnings. Typing the http:// address should redirect automatically to https://. Note the certificate expiry date and confirm renewal is automatic. |
| 7.2 | Password rules | Try to register with a weak password ('123456', 'password'). It should be rejected. A minimum length (at least 8, preferably 12 characters) should be enforced. Passwords must never be visible in plain text anywhere – not in emails, admin screens or the database (they should be stored 'hashed', a one-way scrambling). |
| 7.3 | Login protection | Enter a wrong password repeatedly (10–20 times). The account or the IP address should be temporarily locked or slowed down, and a CAPTCHA may appear. The error message should be generic ('Invalid email or password') so attackers cannot learn which emails are registered. |
| 7.4 | Password reset | Request a reset. The link should arrive only at the registered email, expire after a short time (15–60 minutes), work only once, and the old password should stop working after the reset. The user should get a notification that the password was changed. |
| 7.5 | Two-factor authentication (if offered) | Enable 2FA, log out and log in again: the code must be required. Test wrong codes, expired codes and backup codes. Confirm there is no way to skip the step (e.g. by going directly to a page after entering the password). |
| 7.6 | Session handling | Log in, then log out: pressing Back must not show private pages, and the session must be truly ended. Sessions should expire after a period of inactivity. Changing the password should log out all other devices. Session identifiers must never appear in the web address. |
| 7.7 | Injection attempts | In every text field, search box and address-bar parameter, type the test strings below and submit. The text must be treated as plain text: it must not run, break the page or show a database error. Test strings: `<script>alert(1)</script>` and `' OR 1=1 --` and `"><img src=x onerror=alert(1)>`. (These probe for 'cross-site scripting' and 'SQL injection', two of the most common attacks.) |
| 7.8 | File upload security | Try uploading a file with a dangerous extension (.exe, .php, .html, .svg containing script), a file renamed to look like an image, and a very large file. Uploads should be checked by content not just by name, size-limited, renamed on the server and stored where they cannot be executed. |
| 7.9 | No secrets in the open | Check the page source (right-click → View page source), browser storage (DevTools → Application) and the web addresses of pages: there must be no passwords, API keys, tokens, card numbers or personal data. Card and ID numbers on screen should be masked (**** 1234). |
| 7.10 | Error pages | Force errors (visit a non-existent page, submit broken data). Users should see friendly custom '404' and '500' pages. Technical details (stack traces, database queries, file paths, server version) must never appear. |
| 7.11 | Security headers | Run the site through securityheaders.com (free). It should score well; missing headers such as Content-Security-Policy, Strict-Transport-Security and X-Frame-Options should be added by the developer. |
| 7.12 | Protection against forged requests (CSRF) | Every form that changes data should include a hidden anti-forgery token, and actions that change or delete data should never happen just by visiting a link (e.g. /delete-account?id=5 opened from an email). |
| 7.13 | Up-to-date components | Ask the developer to run a dependency check (npm audit, pip-audit, composer audit, Dependabot or Snyk) and to update libraries with known vulnerabilities. Also confirm the server operating system, database and web server are patched. |
| 7.14 | Admin area | The admin login should not be linked from public pages, should require strong credentials (ideally 2FA) and, where possible, be restricted to office or VPN IP addresses. Default admin accounts and passwords must be removed. |
| 7.15 | Payments (if applicable) | Card details must be entered on, and stored by, a certified payment provider (Stripe, PayPal, Adyen or a local equivalent) – never on your own server. Confirm test / sandbox keys are replaced by live keys only in production and that refunds and failed payments are handled correctly. |
| 7.16 | Backups | Confirm backups run automatically (at least daily), are stored in a separate location, are encrypted and – most importantly – that a restore has actually been tested successfully. An untested backup is not a backup. |
| 7.17 | Privacy and data protection | Confirm the app collects only the data it needs, shows a privacy policy, asks consent for cookies / tracking where required, lets users see and delete their data, and complies with the data-protection laws that apply in your users' countries. |
| 7.18 | Logging and alerting | Important events (logins, failed logins, password changes, permission changes, payments, deletions) should be logged with time and user. Logs must not contain passwords or full card numbers. Someone should be alerted on suspicious patterns (e.g. hundreds of failed logins). |

**Recommended to implement after this QA** (★ = strongly recommended for every system). Reference these as R-7.n:

1. ★ Use the OWASP Top 10 (a free, widely used list of the most critical web security risks) as the minimum standard, and run OWASP ZAP or a similar automated scanner before each major release.
2. ★ Store passwords with a modern hashing algorithm (bcrypt, scrypt or Argon2), enforce HTTPS with HSTS, and keep all secrets (API keys, database passwords) in environment variables or a secrets manager – never in the code repository.
3. ★ Use the framework's built-in protections (parameterised database queries, output escaping, CSRF tokens) instead of writing custom security code.
4. Automate dependency updates and vulnerability alerts (Dependabot, Renovate, Snyk).
5. Commission an independent penetration test for any app that handles payments, personal, health or financial data, and repeat it after major changes.
6. Write a short incident response plan: who to call, how to take the site offline, how to restore from backup and how to notify affected users.
7. Put a Web Application Firewall (WAF) such as Cloudflare or AWS WAF in front of the site for an extra layer of protection against common attacks and bots.

## 8. Permissions, Roles & Access Control

**What this means:** Every app has different kinds of users – visitors, customers, staff, managers, administrators – and each should only be able to see and do what their role allows. A customer must not see other customers' orders; a staff member must not delete the company's data. Permission bugs are among the most common and most damaging problems found in real systems, because a developer often hides a button but forgets to block the action behind it.

| ID | What to check | How to check it |
|---|---|---|
| 8.1 | Permission matrix exists | Write a table listing every role (e.g. Visitor, Customer, Staff, Manager, Admin) against every important action (view orders, edit orders, refund, manage users, change settings, export data) with Yes / No in each cell. This matrix becomes the test plan for everything below. |
| 8.2 | Log in as each role | Create one test account per role and log in as each one. Compare the menus, pages and buttons you can see with the permission matrix. Note anything visible that should not be. |
| 8.3 | Vertical access (lower role → higher pages) | As a normal user, type the address of an admin or manager page directly into the browser (e.g. /admin, /settings, /reports). It must be refused (redirected or 'Access denied'), not just hidden from the menu. |
| 8.4 | Horizontal access (same role, other people's data) | Log in as User A and open one of your own records, e.g. /orders/1001. Change the number in the address to another record (/orders/1002) that belongs to User B. It must be refused. Repeat for invoices, profiles, messages, documents and file downloads. |
| 8.5 | Server-side enforcement | Hiding or disabling a button is not protection. Ask the developer to demonstrate (or use browser DevTools to re-enable the button) that the server itself rejects the action for an unauthorised user. Every permission must be checked on the server. |
| 8.6 | Logged-out access | Open a private page in a private / incognito window without logging in. It must redirect to the login page. Also try direct links to uploaded files, invoices, reports and images that should be private. |
| 8.7 | Role changes apply immediately | While a user is logged in on one device, demote or deactivate them from the admin panel on another. Their next action should be blocked without waiting for them to log out. |
| 8.8 | Deactivated and deleted accounts | A deactivated user cannot log in, cannot use an old password-reset link, and their API keys or tokens stop working. Their data is retained or removed according to the agreed policy. |
| 8.9 | Separation between organisations (multi-tenant) | If the app serves several companies or teams, log in as Company A and try to reach Company B's records by changing IDs, using search, exports or reports. Nothing from Company B may ever appear. |
| 8.10 | Powerful actions are restricted | Dangerous operations (delete all, change billing, change another admin's role, export all customer data) should be limited to the highest role, require confirmation, and ideally require a second person or a re-entered password. |
| 8.11 | Audit trail | Check that sensitive actions – logins, permission changes, deletions, refunds, exports, settings changes – are recorded with who, what and when, and that this log cannot be edited by normal users. |
| 8.12 | API keys and tokens | Any API key or integration token should be limited to the permissions it needs, be revocable, and stop working immediately when revoked or when the owning user is deactivated. |
| 8.13 | Shared and public links | If the app creates shareable links (documents, invoices, invitations), they must be impossible to guess (long random codes), should expire or be revocable, and should grant only the intended access. |
| 8.14 | Sign-up and invitations | New users should receive only the default (lowest) role. Invitation links should expire, work once, and not allow someone to join a different organisation than the one they were invited to. |

**Recommended to implement after this QA** (★ = strongly recommended for every system). Reference these as R-8.n:

1. ★ Check permissions in one central place in the code (a single authorisation layer or policy) and use it for every page, button, API endpoint and background job. Scattered checks are where mistakes happen.
2. ★ Record an audit log of sensitive actions from day one and keep it for an agreed period.
3. Keep the permission matrix as a living document and update it whenever a role or feature is added.
4. Write automated tests that log in as each role and attempt every restricted action – both the allowed and the forbidden cases.
5. Apply the principle of least privilege: give every user, staff member and integration the minimum access needed, and review accounts every quarter, removing unused ones.
6. Use identifiers for sensitive records that cannot be guessed (random IDs / UUIDs) instead of simple counting numbers – but never rely on that alone; still check permissions on the server.

## 9. APIs & Third-Party Integrations

**What this means:** An API (Application Programming Interface) is the way software talks to other software: the mobile app talks to the server, the website talks to the payment provider, the system sends email through an email service. Each connection can fail in its own way – wrong data, timeouts, the other service being down – and the app must handle all of them gracefully.

| ID | What to check | How to check it |
|---|---|---|
| 9.1 | Correct responses | For each API function, the developer (using Postman or automated tests) should show a normal request returning the right data and the right status code. In plain terms: 200 = OK, 201 = created, 400 = your request was invalid, 401 = please log in, 403 = not allowed, 404 = not found, 429 = too many requests, 500 = server error. |
| 9.2 | Authentication on every endpoint | Try to call each API function without a token or with an expired one. Everything that is not deliberately public must return 401. Compare the list of public endpoints with the permission matrix. |
| 9.3 | Input validation | Send requests with missing fields, wrong types (text where a number is expected), extra unexpected fields and very large payloads. The API should answer with a clear 400 error listing what is wrong, never with a 500 crash. |
| 9.4 | Rate limiting | Confirm the API applies the limits from Section 6 and returns 429 with a Retry-After header when they are exceeded. |
| 9.5 | Versioning and compatibility | If mobile apps or partners use the API, confirm that changes do not break older versions still in use (versioned URLs such as /v1/ and /v2/, or backward-compatible changes only). |
| 9.6 | Third-party service failure | Ask the developer to simulate the payment, email, SMS or map provider being down or slow (e.g. by pointing to a wrong address). The user should see a clear message, nothing should be double-charged or double-sent, and the app should recover when the service returns. |
| 9.7 | Payment flows (if applicable) | Using the provider's test cards, test: successful payment, declined card, insufficient funds, cancelled by user, expired card, 3-D Secure / OTP verification, refund (full and partial) and currency handling. Confirm the order status, receipt email and accounting records are correct in each case. |
| 9.8 | Webhooks (notifications from other services) | Confirm incoming notifications (e.g. 'payment succeeded') are verified as genuine (signature check) and that receiving the same notification twice does not apply it twice. Test what happens when a webhook arrives late or out of order. |
| 9.9 | Email deliverability | Send each type of email to Gmail, Outlook and Yahoo accounts. They should arrive in the inbox, not spam, with the correct sender name and address. Ask the developer to confirm SPF, DKIM and DMARC records are set up for the sending domain (mail-tester.com gives a free score). |
| 9.10 | Social and single sign-on login | Test 'Sign in with Google / Apple / Facebook / Microsoft': new user, returning user, a user who also has a password account (linking), and a user who revokes the app's access from their Google / Apple settings. |
| 9.11 | Timeouts and retries | Every outbound call to another service should have a timeout (e.g. 10–30 seconds) and a limited number of retries. Retries must never cause duplicate payments, orders or messages (use idempotency keys). |
| 9.12 | Test versus live credentials | Confirm that sandbox / test keys are used in development and staging, live keys only in production, and that neither is visible in the code repository. |
| 9.13 | API documentation | The API should be documented (OpenAPI / Swagger or a Postman collection) and the documentation should match what the API actually does – test a few endpoints against it. |

**Recommended to implement after this QA** (★ = strongly recommended for every system). Reference these as R-9.n:

1. ★ Use idempotency keys for payments and any action that must not happen twice, and make webhook handlers safe to re-run.
2. ★ Keep a sandbox account and test credentials for every integration so testers can exercise the full flow without real money.
3. Maintain an automated API test suite (Postman / Newman, pytest, Jest, etc.) that runs on every code change and covers success, validation error, unauthorised and rate-limited cases.
4. Monitor each integration's health (success rate, response time) and alert on failures.
5. Store third-party credentials in a secrets manager, rotate them on a schedule, and use the least-privileged API scopes each provider offers.
6. Design for failure: queue outgoing emails and notifications so they are retried automatically if the provider is temporarily down.

## 10. Error Handling, Edge Cases & Reliability

**What this means:** This section covers what happens when things go wrong or when users do unexpected things: the internet drops, two people edit the same record, someone refreshes during payment, a date is 29 February. Well-built software fails gracefully – it tells the user what happened, protects their data and lets them continue.

| ID | What to check | How to check it |
|---|---|---|
| 10.1 | Page not found (404) | Visit a made-up address (e.g. /this-page-does-not-exist). A friendly, branded page should appear with a search box or links back to useful pages. |
| 10.2 | Server error (500) | Ask the developer to trigger a server error on staging. The user should see a friendly page ('Something went wrong – we have been notified'), and the error should appear in the error-tracking tool with enough detail to diagnose. |
| 10.3 | Lost connection | Turn off Wi-Fi in the middle of filling a form or loading a page, then turn it back on. The app should show a clear 'You are offline' message, keep the entered data and allow a retry. A mobile app must not crash. |
| 10.4 | Double submission | Click Submit / Pay / Send twice quickly, or press Enter repeatedly. Only one record, order, payment or message should result. Buttons should disable after the first click. |
| 10.5 | Two people editing the same record | Open the same record in two browsers, change it in both and save. The second save should either warn that the record changed, merge sensibly, or show a clear conflict – it must never silently overwrite without anyone knowing. |
| 10.6 | Refresh, Back and Forward mid-process | During checkout, sign-up or a multi-step form: refresh the page, press Back and Forward, and close and reopen the tab. No duplicate charges, no half-created accounts, and entered data should be preserved where reasonable. |
| 10.7 | Boundary values | Test the edges of every input: zero, negative numbers, very large numbers, decimals in whole-number fields, maximum-length text, 29 February in a leap year, 31 April, midnight, end of month, the years 1900 and 2100, and times around daylight-saving changes and time-zone boundaries. |
| 10.8 | Interrupted uploads and downloads | Cancel an upload halfway or lose connection during a download. The app should clean up incomplete files and allow a retry without errors. |
| 10.9 | Expired and stale states | Use an old password-reset link, an expired invitation, a session that has timed out, or a page left open overnight, and then perform an action. Each should show a clear message about what to do rather than an error or unexpected behaviour. |
| 10.10 | Partial failures | If one part of a page (recommendations, reviews, a map, an ad) fails to load, the rest of the page should still work. One broken widget must not blank the whole screen. |
| 10.11 | Error tracking and monitoring | Confirm an error-tracking tool (e.g. Sentry, Bugsnag, Rollbar) is connected in production, that errors include the page, user role and steps but not passwords or personal data, and that the team receives alerts. |
| 10.12 | Data clean-up after failures | After a failed process (e.g. payment declined during an order), confirm no leftover 'ghost' records, reserved stock or locked items remain. |

**Recommended to implement after this QA** (★ = strongly recommended for every system). Reference these as R-10.n:

1. ★ Add a global error handler that shows a friendly message to the user and sends full details to the error-tracking tool.
2. ★ Make every submission safe to repeat (idempotent) using unique request tokens, and disable buttons while a request is in progress.
3. Use optimistic locking (a version number on each record) so simultaneous edits are detected instead of overwriting each other.
4. Provide a health-check page the monitoring tool can call every minute, and set up uptime alerts.
5. Write down an incident process: who is contacted, how status is communicated to users, and how a rollback or restore is performed.
6. Keep a list of edge cases discovered during QA and turn each one into an automated test so it can never come back.

## 11. Notifications & Communications

**What this means:** Emails, SMS messages, push notifications and in-app alerts are often the only part of the system a customer sees outside the app. A wrong name, a broken link or a message sent twice looks unprofessional and creates support work. Every message the system can send should be triggered and read during QA.

| ID | What to check | How to check it |
|---|---|---|
| 11.1 | Every message triggered | List every email, SMS, push and in-app notification the app can send (welcome, verification, password reset, order confirmation, shipping, reminders, alerts, invoices). Trigger each one and confirm it arrives. |
| 11.2 | Content and personalisation | Read each message: correct name and details, no unfilled placeholders (e.g. 'Hi {{first_name}}'), correct spelling, brand logo, and correct sender name and reply-to address. |
| 11.3 | Links and buttons in messages | Click every link and button in each message: they should open the correct page, work on mobile, and log the user in or lead to login as intended. Verification and reset links should expire and work only once. |
| 11.4 | Layout across email clients | Open emails in Gmail (web and phone app), Outlook, Apple Mail and on a small phone screen. Images, buttons and text should display correctly, with a readable plain-text fallback. |
| 11.5 | Timing and duplicates | Confirm each message is sent once and at the right moment (e.g. confirmation immediately after payment, reminder 24 hours before). Nothing should be sent to the wrong person, and nothing should be sent when an action fails. |
| 11.6 | Unsubscribe and preferences | Marketing messages must include a working unsubscribe link, and users should be able to change notification preferences. Essential messages (receipts, security alerts) should still be sent after unsubscribing from marketing. |
| 11.7 | Push notifications (mobile / web apps) | Test granting and denying permission; receiving notifications when the app is open, in the background and closed; and tapping a notification to open the correct screen. |
| 11.8 | In-app notifications | New notifications should appear with a count, mark as read when opened, and be listed in a history. Deleting or completing the related item should not break the notification. |
| 11.9 | SMS specifics | Check message length (long messages cost more and may split), the sender ID, delivery on the main mobile carriers, and that one-time codes arrive within a reasonable time (under a minute). |
| 11.10 | Message log | The admin panel or provider dashboard should show which messages were sent, to whom, when, and whether they were delivered, opened or bounced, so support staff can answer 'I never received the email'. |

**Recommended to implement after this QA** (★ = strongly recommended for every system). Reference these as R-11.n:

1. ★ Send transactional email through a dedicated service (e.g. Amazon SES, SendGrid, Postmark, Mailgun) with SPF, DKIM and DMARC configured, rather than from a shared web-hosting mailbox.
2. Keep message templates in one place with a preview tool, and review them in real inboxes (or a tool such as Litmus) whenever they change.
3. Build a notification preference centre and honour it for all non-essential messages.
4. Queue outgoing messages so they are retried on failure and never block the user's action.
5. Store a delivery log for every message and make it visible to support staff.

## 12. Content, SEO & Analytics (public websites)

**What this means:** For a public website, being found on Google and understanding how visitors behave matter as much as the features. SEO (search engine optimisation) is the basic technical hygiene that lets search engines index the site correctly. Analytics confirms that the numbers the business will rely on are actually being recorded. Mark this section N/A for internal tools that are not public.

| ID | What to check | How to check it |
|---|---|---|
| 12.1 | Page titles and descriptions | Every page should have a unique, meaningful title (what appears in the browser tab and in search results) and a meta description of roughly 150 characters. |
| 12.2 | Headings and readable addresses | One H1 per page, and web addresses that are short and readable (e.g. /products/blue-running-shoes, not /page?id=8231&cat=4). |
| 12.3 | Sitemap and robots.txt | /sitemap.xml should list all public pages and /robots.txt must not accidentally block the whole site (a common leftover from staging is 'Disallow: /'). |
| 12.4 | Redirects from an old site | If the site replaces an old one, every old address should permanently redirect (301) to its new equivalent so links and search rankings are preserved. Test a sample of the most-visited old pages. |
| 12.5 | Social sharing previews | Paste key page addresses into Facebook, LinkedIn, X or a messaging app: the preview should show the correct title, description and image (Open Graph tags). |
| 12.6 | Structured data (if applicable) | For products, articles, events or local businesses, check with Google's Rich Results Test that the structured data is valid. |
| 12.7 | Analytics events | Open the analytics tool's real-time view and perform key actions (visit, sign up, add to cart, purchase, contact form). Each should appear once, with the correct value. Confirm nothing is double-counted and that staff / test traffic is excluded. |
| 12.8 | Cookie consent | Where required, tracking scripts must not run until the visitor consents, the consent banner must work, and the choice must be remembered. |
| 12.9 | Legal and trust pages | Privacy policy, terms of service, refund / returns policy (if selling), contact details and a business address (if required) should exist, be current and be linked in the footer. The copyright year should be correct. |
| 12.10 | Staging not indexed | Confirm the staging / test site is not indexed by Google (password-protected or 'noindex'), so it never appears in search results or gets confused with the live site. |

**Recommended to implement after this QA** (★ = strongly recommended for every system). Reference these as R-12.n:

1. ★ Register the site in Google Search Console and run Lighthouse (SEO section) plus a crawler such as Screaming Frog before launch.
2. Decide the key business events (sign-up, purchase, lead) before development starts and specify exactly when each should fire.
3. Use a tag manager (e.g. Google Tag Manager) so tracking changes do not need code releases, and keep a written tracking plan.
4. Keep an inventory of old addresses and their new equivalents whenever pages are moved or renamed.
5. Review the analytics data one week after launch to confirm real traffic is being recorded correctly.

## 13. Deployment & Release Readiness

**What this means:** Deployment is the act of putting a new version of the app onto the live server where customers use it. Many serious incidents are caused not by bugs in the code but by release mistakes: test payment keys left in production, a forgotten database update, no backup before a change. This section is the pre-flight checklist for going live.

| ID | What to check | How to check it |
|---|---|---|
| 13.1 | Separate environments | There should be at least a development, a staging (test copy) and a production (live) environment, each with its own database. Staging should be as close to production as possible. Test data must never be created in production. |
| 13.2 | Production settings | Confirm production uses live keys and settings (payments, email, analytics, domain), debugging is off and 'test mode' banners are gone. Conversely, staging must not send real emails or charge real cards. |
| 13.3 | Database changes | Any database changes (migrations) have been tested on a copy of production data, including how long they take and whether they lock tables. A rollback for each migration exists. |
| 13.4 | Backup before release | A full backup is taken immediately before the release and the team knows how to restore it. |
| 13.5 | Rollback plan | It is written down how to return to the previous version quickly if something goes wrong, and this has been rehearsed at least once. |
| 13.6 | Domain, DNS and certificates | The domain points to the right server, www and non-www both work, the SSL certificate is valid and auto-renews, and email records (SPF / DKIM / DMARC) are set. |
| 13.7 | Monitoring connected | Uptime monitoring, error tracking, performance monitoring and log collection are active for production, and alerts go to a real person. |
| 13.8 | Documentation | A user guide (for customers), an admin guide (for staff) and technical notes for future developers (how to set up, deploy and restore) exist and are up to date. |
| 13.9 | Support process | Users know how to get help (contact form, email, phone), someone is assigned to respond, and there is a way to report bugs after launch. |
| 13.10 | Go-live smoke test | Immediately after deployment, run the core user journeys on the live site (with a real small payment if applicable, then refund it). Check the home page, login, one main feature and one email. |
| 13.11 | Release notes and communication | Changes are listed in release notes, and users / staff are informed of anything that affects them (new features, downtime windows, changed behaviour). |
| 13.12 | Licences and accounts | Third-party services, domains and certificates are registered to the business (not to an individual developer's personal account), with renewal dates recorded. |

**Recommended to implement after this QA** (★ = strongly recommended for every system). Reference these as R-13.n:

1. ★ Set up an automated pipeline (CI/CD) that runs the automated tests and blocks deployment if they fail, then deploys the same tested build to staging and production.
2. ★ Keep a written release checklist (this section) and have a second person confirm it before every production release.
3. Use feature flags so new functionality can be switched on gradually or turned off instantly without a new release.
4. Deploy small changes frequently rather than large changes rarely – small releases are easier to test and to roll back.
5. Schedule releases at low-traffic times, announce maintenance windows in advance, and avoid deploying right before a weekend or holiday without cover.

## 14. Regression Testing & Final Sign-off

**What this means:** Regression testing means re-checking things that already worked to make sure a fix or new feature has not accidentally broken them. It is the last step before a release and should be repeated for every release, however small – a one-line change can break an unrelated feature.

| ID | What to check | How to check it |
|---|---|---|
| 14.1 | All Critical and High issues closed | Every Critical and High bug is fixed, re-tested by the tester (not only the developer) and marked Closed. |
| 14.2 | All Fails re-tested | Every checklist item marked Fail has been re-tested after the fix and now passes. |
| 14.3 | Core user journeys re-run | The 3–5 core journeys from Section 1 are run again end to end on the release candidate, on at least one desktop browser and one real phone. |
| 14.4 | Areas near the changes re-checked | For each change in this release, the related screens and features were re-tested (e.g. changing the checkout means re-testing the cart, payment, order email and the admin order list). |
| 14.5 | Automated tests pass | All automated tests (unit, API, end-to-end) pass on the exact build being released. |
| 14.6 | Known issues documented | Remaining Medium and Low issues are listed with an owner and a target release, and the product owner has agreed to release with them. |
| 14.7 | Performance and security re-checked | A quick PageSpeed run and security-header check on the release candidate show no regression from the previous release. |
| 14.8 | Sign-off recorded | The sign-off table below is completed by the developer, the tester and the product owner or client. |

**Recommended to implement after this QA** (★ = strongly recommended for every system). Reference these as R-14.n:

1. ★ Turn the core user journeys into automated end-to-end tests so a full regression takes minutes instead of days.
2. Keep a short 'smoke test' list (10–15 checks, about 15 minutes) for urgent hot-fixes, and use the full checklist for major releases.
3. Track each release's Pass / Fail counts over time; a rising Fail rate is an early warning of technical debt.
4. Never let the person who wrote the code be the only person who tests it.

## 15. Design Gaps & Unmodelled Reality

**What this means:** Sections 1–14 find things that are wrong. This section finds things that were never thought about – where the real world contains an entity, a state or an event that the system does not represent at all, so there is no code to be wrong. These are the findings a client cannot get from a scanner, and they are usually the most valuable ones in the report. The method, the probe questions and a full worked example (a library that counts books instead of tracking copies) are in `07_SYSTEM_GAPS_GUIDE.md`. Findings from this section are numbered `G-nnn` and written up in `06_System_Gaps_Report`.

| ID | What to check | How to check it |
|---|---|---|
| 15.1 | Counters standing in for real things | List every column like `quantity`, `stock`, `available`, `slots`, `seats`. For each, ask whether the thing being counted is physically distinguishable (a book copy, a room, a device, a ticket). If it is, the system should have a row per item, not a number. Check what happens when one is returned, damaged or lost: can the system say **which one**? |
| 15.2 | Identifiers resolve to exactly one thing | For every printed or scanned identifier (barcode, QR, serial, plate, receipt number, reference code), find where it is generated and confirm it maps to one row. Two physical items sharing one code is a gap, not a bug. |
| 15.3 | The transacted thing has its own identity | For the main transaction (borrow, book, rent, assign, sell, deliver), check whether the record points at a specific item or only at a category. Read the foreign keys on the transaction table. |
| 15.4 | Lifecycle end-states are modelled | Write out every state each main record can reach, including cancelled, expired, refunded, withdrawn, lost, transferred, closed and deceased. Compare with the states the code can actually set. Ask what happens to children when a parent ends. |
| 15.5 | There is a way back | For each action that can be done by mistake (a loan, a charge, an approval, a deletion, a grade), find the correction path. Is a correction a new event that keeps the history, or an in-place edit that destroys it? Is there any way at all, or does it need database access? |
| 15.6 | Concurrent actors on the same record | Read the code for the "last one" case: two users take the last item, two approve the same refund, one user double-clicks. Is the check-and-write atomic, and is uniqueness enforced by the database or only by the form? |
| 15.7 | Reconciliation with the physical or external world | Where the data mirrors something outside it (shelf stock, cash, a payment provider, a warehouse, a calendar), find the function that compares the two. If there is none, or a discrepancy can only be fixed by silently overwriting, record it. Check whether stored aggregates can be recomputed from their rows. |
| 15.8 | Time, calendars and rules that change | Check timezone handling on due dates, expiry, overdue and grace periods; whether historical records keep the price / rate / rule that applied when they were created; and what happens on a day a scheduled job does not run. |
| 15.9 | Partial and money edge cases | Look for partial payment, partial refund, partial delivery, partial return of a multi-item transaction, and rounding. Confirm money is stored in minor units, not floats, and that the total shown and the total charged come from the same computation. |
| 15.10 | People, duplicates and merging | Check what makes two records the same person or thing (email, phone, ISBN, name+birthdate), whether duplicates can be created, and whether they can be merged afterwards. Check one person with two roles, someone who leaves and returns, and someone acting on behalf of another. |
| 15.11 | Evidence survives the record | For every disputable action (a fine, a refund, a deletion, a grade, a payment), check that the log says who, when and from where, is append-only, and still makes sense after the record it refers to is deleted. |
| 15.12 | The second customer and 10x the data | Ask what breaks with a second branch, tenant, campus, currency or language, and at ten times today's data. Look for anything keyed on a name, a title or a date, and anything hard-coded to one location or one admin account. |

**Recommended to implement after this QA** (★ = strongly recommended for every system). Reference these as R-15.n:

1. ★ Give every physically distinguishable item its own row and its own identifier, and derive availability by counting rather than storing it.
2. ★ Make every correction an event (adjustment, reversal, credit note) rather than an edit, so history survives.
3. Add a reconciliation screen or report wherever the data mirrors something physical or external, and record discrepancies as events.
4. Write the state machine for each main record into the documentation, including the end-states, and enforce the transitions in one place.
5. Enforce uniqueness and referential integrity in the database, not only in forms.

## 16. Destructive & Abuse Resilience

**What this means:** How the system behaves when it is used improperly, overloaded, interrupted or attacked. These checks are only *run* when destructive testing has been authorised (`DESTRUCTIVE_TESTING` in the run settings, plus a named non-production target – the full gate is in `08_DESTRUCTIVE_TESTING.md`); without that authorisation they are still *reviewed* from the code and marked `NEEDS-MANUAL` with steps. Findings are numbered `D-nnn` and written up in `07_Destructive_Test_Report`. Nothing in this section is ever run against production or against a third party's live service.

| ID | What to check | How to check it |
|---|---|---|
| 16.1 | Authorisation and recovery before anything else | Confirm in writing which environment may be broken, that the data is test data, that third-party credentials are sandbox ones, and how the environment is restored. Take a database dump or note the reset command, and record the app version. No gate, no destructive test. |
| 16.2 | Input abuse | In every text field, URL parameter, header and file name: 10k-character strings, wrong types, negative and zero values, impossible dates, emoji and zero-width characters, `NULL` bytes, template syntax, path traversal, script and SQL fragments. Expect rejection at the boundary with a clear message, nothing stored, nothing echoed unescaped, no stack trace. |
| 16.3 | File upload abuse | Wrong extension, double extension, 0-byte file, oversized file, archive bomb, image with an embedded payload, 300-character file name. Expect an allow-list by content type, a size cap, renaming on the server and storage outside the web root. |
| 16.4 | Limits enforced on the server | Send the maximum and maximum+1 of every limit (page size, cart items, list length, quantity) directly to the API, bypassing the form. Expect the server to enforce it and name the limit in the error. |
| 16.5 | Double submission and replay | Double-click every create or charge action; replay the same request, token, reset link or idempotency key twice; use a link after logout, after expiry and after the record was deleted. Expect one effect per intent and single-use tokens. |
| 16.6 | Resource pressure | Request an enormous page size, a search matching everything, the largest export; send a deeply nested body; fire a short burst of requests at the app's own endpoints. Stop at the first `429`. Expect server-side caps, rate limiting with `Retry-After`, and a responsive app afterwards. |
| 16.7 | Dependency failure | Locally simulate each dependency being down, slow or wrong: stop the database, cache, queue; point a third-party base URL at a dead port; return `500`, malformed JSON and unexpected payloads; make the mail or SMS provider fail after the record was created. Expect short timeouts, bounded idempotent retries, a friendly message, no half-written data, and an entry in the error tracker. |
| 16.8 | Interruption and state corruption | Kill the process mid-way through a multi-step operation (pay then create order, upload then process, transfer between records) and inspect the data afterwards. Put a record into an unusual but reachable state and open the screens that show it. Delete a parent row that has children directly in the database. Run the same background job twice. Expect transactions, idempotent jobs, foreign keys and screens that degrade rather than crash. |
| 16.9 | Restore actually works | Restore from the snapshot taken in 16.1 and confirm the app runs and a core journey passes. If the project documents a backup or restore procedure, follow it exactly as written; where the written steps are wrong or incomplete, that is a finding on its own. |
| 16.10 | Environment left clean | After the run, confirm the target environment is restored, test junk is gone, any control that was disabled for a test is back on, and say in the report how that was verified. |

**Recommended to implement after this QA** (★ = strongly recommended for every system). Reference these as R-16.n:

1. ★ Wrap every multi-step write in a transaction, and make every background job safe to run twice.
2. ★ Set an explicit timeout and a bounded retry on every outbound call, and decide per call what the user sees when it fails.
3. Add the worst inputs found here to the automated test suite so the fix cannot silently regress.
4. Run the destructive block again before every major release, on staging, as a short repeatable script.
5. Test the restore procedure on a schedule; a backup nobody has restored is not a backup.

## Appendix A – Business-impact phrasing for client-facing summaries

Use this wording (plain English) when a gap is found. Keep the checklist reference.

| Gap found | What it means for the business | What to implement |
|---|---|---|
| No server-side pagination – lists load everything at once | Screens get slower every month as data grows; eventually pages freeze or time out and staff cannot work. | Server-side pagination with page-size limits, indexed sorting and filtering (Section 2) |
| No rate limiting / throttling | Attackers can guess passwords by trying thousands of times; bots can run up your SMS and email bill; one script can take the site offline. | Rate limits on login, OTP, forms and API with clear 'try again later' responses (6.8–6.10) |
| Permissions checked only on the screen, not on the server | Any customer who edits a web address can see or change other people's records – a data breach and a legal risk. | Central server-side permission checks on every page and API, tests for each role, and an audit log (Section 8) |
| No HTTPS, or an expired certificate | Browsers show 'Not secure'; data can be read in transit; customers lose trust and leave. | Valid, auto-renewing certificate and forced HTTPS (7.1) |
| Weak password rules / no login lockout | Customer and admin accounts can be taken over. | Strong password policy, secure hashing, lockout and optional 2FA (7.2–7.5) |
| Input not validated or sanitised | Attackers can inject code, corrupt data or crash the app; bad data spreads into reports. | Validation on screen and server, safe database queries, output escaping (1.3–1.5, 7.7) |
| No backups, or backups never tested | One server failure or one mistake can erase the business's data permanently. | Automated, encrypted, off-site backups with a tested restore (7.16) |
| No error tracking or monitoring | You only learn about outages and errors from angry customers. | Uptime monitoring, error tracking and alerts to the team (10.11, 13.7) |
| No automated tests | Every change risks breaking something else; releases are slow, stressful and expensive. | Automated tests for the core user journeys and a CI pipeline (Sections 13–14) |
| No staging environment | New changes are tested on real customers and real data. | Separate development, staging and production with safe test data (13.1–13.2) |
| Slow pages / poor mobile layout | Visitors leave before the page loads; Google ranks the site lower. | Image optimisation, caching, CDN and responsive fixes (Sections 3, 6) |
| Emails land in spam / no delivery log | Customers miss receipts, password resets and confirmations; support cannot prove what was sent. | Dedicated email service with SPF / DKIM / DMARC and a delivery log (Section 11) |
| Not accessible / keyboard-unfriendly | Excludes customers with disabilities and may breach accessibility laws. | WCAG 2.1 AA fixes: labels, contrast, keyboard navigation (Section 4) |
| Double submissions / duplicate orders | Customers get charged or messaged twice; refunds and complaints follow. | Idempotent submissions and buttons disabled while processing (10.4) |
| No audit trail | Nobody can tell who changed or deleted what; disputes cannot be resolved. | Audit log of sensitive actions (8.11) |
| Test keys, debug mode or test data in production | Real payments may fail, reports are polluted, and error pages leak internal details. | Environment separation and a written release checklist (Section 13) |

_Total checks: 191 across 16 sections (169 in Sections 1-14, 12 in Section 15, 10 in Section 16). Do not renumber existing items; new items may be added at the end of a section (e.g. 7.19)._
