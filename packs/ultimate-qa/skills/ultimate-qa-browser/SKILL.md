---
name: ultimate-qa-browser
description: Exercise QA user journeys, roles, accessibility, and visual states with a browser against an authorized local or staging target.
---

# Ultimate QA Browser

Read the kit's `11_BROWSER_ASSISTED_CHECKS.md` if available. Confirm the exact local or staging URL, available test roles, data reset method, and browser tool. Do not browse production by default. Map critical journeys from requirements and routes; cover success, validation, permission denial, empty state, loading, error, keyboard navigation, and narrow viewport where relevant.

Prefer installed Playwright or an available browser automation tool. Wait for navigation, network, and assertions to settle before judging results. On failure save URL, role, steps, expected and observed behavior, console/network clues, screenshots, and a trace when supported. Use automated accessibility checks as leads; keyboard flow and meaningful wording still need judgment. Mark a check manual only after available automation and equivalent evidence have been tried or a concrete limitation is documented.

Do not create brittle tests for every checklist sentence. Add repeatable regression coverage for critical paths and confirmed defects in the project's existing test framework when the user has authorized code changes.
