# 11 – Browser-assisted checks: doing the "needs a browser" items yourself

Half of the `NEEDS-MANUAL` rows in a typical audit exist for one reason: the reviewer had no browser. When the agent can drive a real browser – open pages, log in with the test accounts, resize to a phone width, read the console, take screenshots – most of those rows become real `PASS` / `FAIL` results with evidence, and Part 3 of the audit report shrinks to the things that genuinely need a person: a real phone, a real inbox, the live site, a designer's eye.

This guide says which browser tools count, the safety gate, which checklist items the browser can settle, how to work through them, and how to write them up. It changes nothing about the rules in `01_QA_AGENT_PROMPT.md`; it only turns "not checked" into "checked" where that is honest.

---

## 1. What counts as a browser tool

| Tool | How it is set up | What it can do | Notes |
|---|---|---|---|
| **Claude in Chrome** (Claude Code) | Start Claude Code with `claude --chrome`, or type `/chrome` inside a session to connect, check status or reconnect. Needs the *Claude in Chrome* extension (version 1.0.36 or later) from the Chrome Web Store. Works with Chrome, Edge, Brave, Arc, Vivaldi and Opera; not inside WSL. Available on direct Anthropic plans (Pro, Max, Team, Enterprise) – not through Bedrock, Vertex, Foundry or an API key. | Navigate, click, type, take screenshots and save them to disk, record GIFs, read console errors, inspect the page, upload files (up to 10 MB), open several tabs, work against `localhost`. | Uses the **user's own logged-in browser profile**, so it shares whatever that profile is signed in to – see the gate below. It pauses and hands back to the user at login pages and CAPTCHAs. |
| **Playwright MCP server** | `claude mcp add playwright -- npx -y @playwright/mcp@latest` (needs Node.js 18 or newer). Works with any agent that speaks MCP – Cursor, Windsurf and others register it the same way. | The same navigate / click / type / screenshot abilities, plus a fresh browser context per session, viewport sizing, and a choice of browser (`--browser firefox`, and so on). | Opens a visible browser window by default; a headless option exists. Nothing is shared with the user's own profile, which makes it the safer default on a machine that is logged in to real systems. |
| **Any other agent browser** (Cursor, Copilot, Windsurf, a project's own Playwright or Cypress setup) | As documented by that tool. | Varies. | The gate and the write-up rules below apply regardless of the tool. |

Turn it on with `BROWSER_TOOL: auto` (the default) in `requirements/01_RUN_SETTINGS.md`: the agent uses a browser if it has one and says so in `01_Project_Map` §3. `BROWSER_TOOL: no` switches it off, and those checks go back to `NEEDS-MANUAL`.

**Also useful without a browser tool:** `npx lighthouse <url> --output html --output-path evidence/6-1_lighthouse.html` (needs Chrome installed) covers QA 6.1, 6.2 and part of 4.2 / 4.4 / 12.1 from the command line; `curl -I <url>` answers QA 7.1 and 7.11.

---

## 2. The gate

- **Target.** Only the address in `BROWSER_TARGET`, or, if that is blank, the local dev URL from `02_PROJECT_CONTEXT.md` §1, or the staging URL. **Never production.** If the address, the data or the branding looks live, stop and ask.
- **Accounts.** Only the test accounts from `02_PROJECT_CONTEXT.md` §3. Never type a real customer's or a real administrator's credentials, and never take screenshots of real people's data. If the browser profile is already signed in to the client's live system, do not use that profile – use the Playwright server or a separate profile.
- **Observe and use, do not break.** The browser is for normal use and for the checks below. Anything that could damage data – bulk deletes, floods of requests, corrupting state – belongs to `08_DESTRUCTIVE_TESTING.md` and its own gate.
- **Payments and messages.** Only sandbox payment pages and only a local mail catcher or the provider's test mode. If a step would send a real email, SMS or charge, stop before it and write the manual steps instead.
- **Evidence.** Screenshots and console logs go in the version's `evidence/` folder, named `<ID>_<what>.png` or `<checklist item>_<what>.txt` (`F-003_invoice_1002.png`, `3-1_book_375px.png`). Never paste a token, a session cookie or anything from DevTools storage into a document.

---

## 3. Which checks a browser tool can settle

`Do this` is the browser work; `Still needs a person` is what stays in Part 3 even with a browser.

| Checks | Do this in the browser | Evidence to save | Still needs a person |
|---|---|---|---|
| 1.1 Links | Open every page in the Project Map; follow every header, footer and in-page link; note any 404 or wrong destination; confirm external links open in a new tab | `1-1_links.txt` – page, link, result | Nothing, for the pages reachable on the target |
| 1.2, 10.4 Buttons, double submission | Double-click every create / pay / send button; press Enter twice on forms | Screenshot of the duplicate record or the disabled button | – |
| 1.3, 1.4, 1.5 Forms | Submit each form empty, half-filled, with wrong formats, with 1,000+ characters, emoji and `<script>`; then correctly | Screenshot of each message; the saved record | – |
| 1.6 Navigation | Open every menu on desktop and at 375 px; test breadcrumbs, the logo, Back | Screenshots at two widths | – |
| 1.7 Search | Common, rare, misspelled, empty and special-character searches | Screenshot of the empty-result state | – |
| 1.8 Core journeys | Walk each journey from `02_PROJECT_CONTEXT.md` §4 end to end as a new user, one screenshot per step | `1-8_journey1_step3.png` … | Anything that needs a real payment or a real device |
| 1.12, 1.13, 1.14 Errors, confirmations, wizards | Trigger errors deliberately; try to delete without confirming; go back, refresh and close mid-wizard | Screenshots | – |
| 2.1–2.8 Lists | Page through; note the last row of page 1 and the first of page 2; sort each column both ways; combine filters; open `?page=999`, `?page=0`, `?page=abc`; find every empty state | Screenshots of edge cases | – |
| 2.10 Data formats | Read dates, money and phone numbers on every screen | Notes | Formats in exports and emails, unless a mail catcher is available (see 11) |
| 3.1 Responsive layout | Set the viewport to 1920, 1366, 768, 375 and 360 px (Playwright: viewport size; Chrome: DevTools device toolbar or a resized window) and open every page | One screenshot per page per width | A real phone for touch behaviour (3.2) |
| 3.4–3.8, 3.10 Readability, images, loading states, text, tab titles, dark mode | Read every page; watch for broken images (console 404s), missing loading states, placeholder text, missing titles or favicon; toggle dark mode if it exists | Screenshots, console log | A designer's judgement on consistency with the mock-ups (3.3) |
| 4.1 Keyboard-only | Tab through each page; confirm the focus ring is visible, the order is sensible, Esc closes dialogs, nothing traps focus | Screenshots with the focus visible | – |
| 4.3 Headings | Inspect the page structure: one H1, ordered H2 / H3 | Notes | – |
| 4.2, 4.4 Screen reader, contrast | Run Lighthouse or an axe scan on the main pages and read the report | `4-x_lighthouse_<page>.html` | A real screen reader, and judgement on whether labels and alt text make sense |
| 4.5 Zoom | Zoom the page to 200 % (or set a 640 px viewport as a proxy) | Screenshot | – |
| 4.9 Session warning | Leave a page open past the timeout, then act | Screenshot | – |
| 5.1–5.4 Browsers and devices | Only the browser you are driving counts as checked; say which | – | Every other browser, every real device |
| 5.6 Restricted browsers | A private / incognito window; blocked third-party cookies where the tool allows it | Screenshot | Ad blocker on a real machine |
| 5.7 Slow connection | Throttle to Slow 3G (Chrome DevTools, or Playwright's network conditions) and use a form | Screenshot of the loading state | Switching Wi-Fi to mobile data mid-task |
| 6.1–6.5, 6.14 Speed | Lighthouse on the home page and 3–5 key pages; Network panel for page weight and caching on a repeat visit; time common actions; disable third-party scripts and compare | Lighthouse reports, timings | Load and stress tests (6.6, 6.7) |
| 7.1 HTTPS | Open the `http://` address on staging and confirm the redirect and the padlock | Screenshot | The live certificate and its renewal |
| 7.3 Login protection | Wrong password 10–20 times; note when (or whether) it slows or locks | Screenshot of the message | – |
| 7.6 Session handling | Log out, press Back; change the password, check the other session | Screenshots | – |
| 7.7 Injection strings | The three test strings in every field, search box and URL parameter | Screenshot where anything runs or breaks | – |
| 7.9 Secrets in the open | View page source; open DevTools → Application → storage; read the URLs | Notes only – never the values | – |
| 7.10, 10.1, 10.2 Error pages | Open a made-up address; submit broken data; look for stack traces | Screenshots | A deliberately triggered server error on staging if there is no safe way to cause one |
| 7.11 Security headers | Network panel → response headers on any page (or `curl -I`) | `7-11_headers.txt` | – |
| 8.2–8.6, 8.9 Permissions | The heart of `02_Access_Matrix`: log in as every role; type the address of every page in the Project Map; change record IDs in the address bar; open private pages and file links in a private window | One line per page per role; screenshots of every wrong "Open" | – |
| 8.7 Role changes | Demote a user in one tab while they are logged in in another | Screenshot | – |
| 9.10 Social login | With the provider's test accounts only | Screenshot | Revoking access from the provider's side |
| 10.3 Lost connection | DevTools → Offline (or Playwright offline mode) in the middle of a form | Screenshot | A real phone losing signal |
| 10.6, 10.9 Refresh mid-process, expired links | Refresh, Back and Forward during checkout or sign-up; reuse an old reset link | Screenshots | – |
| 11.1–11.3, 11.5 Emails | If a mail catcher runs locally (Mailpit, Mailhog at `localhost:8025`, or the framework's log driver), trigger each message and open it in the catcher: content, placeholders, links, duplicates | Screenshots of each email | Real inboxes and spam placement (9.9, 11.4), SMS delivery (11.9) |
| 12.1–12.5, 12.8–12.10 SEO and legal pages | Read titles and meta tags from the page; open `/sitemap.xml` and `/robots.txt`; check Open Graph tags; use the cookie banner; open the legal pages; confirm staging is `noindex` | Notes, screenshots | Analytics real-time view in the client's account (12.7), sharing previews on the real platforms |
| 13.10 Smoke test | The core journeys on staging after a deployment | Screenshots | The live site |

Sections 15 and 16 are not browser sections: 15 works from the data model, 16 from its own gate.

---

## 4. How to work through it

1. **Confirm the target and the accounts.** Write both in `01_Project_Map` §3 ("Browser checks were done with <tool> against <address>, logged in as <accounts>"). Open the home page and save `evidence/00_home.png` – it proves what was reviewed.
2. **Core journeys first** (1.8), as each role that performs them, one screenshot per step. If a journey cannot be completed, that is usually the most important finding of the run.
3. **Then the permissions pass** (8.x). Take the page list from the Project Map and, for every role plus logged-out, open every page and change every ID you can. This pass produces most of the Critical findings and the whole of the Access Matrix.
4. **Then forms and input** (1.x, 7.7), **lists** (2.x), **widths** (3.1), **keyboard** (4.1), **error pages** (10.x), **emails through the catcher** (11.x), **SEO and legal pages** (12.x).
5. **Read the console and the network panel after every page.** Errors, failed requests and 404s go into `evidence/console_<page>.txt` and usually point at a finding.
6. **Look at your own screenshots before marking PASS.** The agent can open a PNG it has saved and see it; use that to double-check anything you are about to mark as working.
7. **Stop at the first sign of production.** Real names in the data, a live domain, a live payment page: close the tab, note it in the chat message, and continue with code review.

---

## 5. What stays with a person, even with a browser

Real devices (touch targets, iPhone Safari quirks, on-screen keyboards, rotation); every browser you are not driving; real inboxes and spam placement; real SMS delivery times; the live site's certificate and headers; the client's analytics account; a designer's judgement on visual consistency; whether alt text and labels actually make sense to a screen-reader user; real payments on the live gateway; load and stress tests. Write the steps for each, specific to this app, exactly as before.

---

## 6. Writing it up

- **Method.** In the results table, `How checked` reads *Used the app* with the tool, browser and width: "Used the app – Playwright (Chromium), 1366 px and 375 px". In the finding block, `How checked` says the same.
- **Evidence.** Every browser-checked row names its file in `evidence/`. A `PASS` still needs the one-line "where it is enforced" plus the screenshot name. The one screenshot that proves a finding can be embedded in the finding block with `![caption](../evidence/<file>.png)`; the converter scales it to the page.
- **Voice.** A browser result is written exactly like a tester's note – page, account, steps, what happened – never "verified by automation" or "the browser tool confirmed".
- **Part 3 shrinks, it does not vanish.** Keep every row that genuinely needs a person, with its steps.
- **If no browser tool was available**, say so in one line in `01_Project_Map` §3, mark the rows `NEEDS-MANUAL` as before, and end the run's chat message with the one-line setup from §1 so the next run can do more.
