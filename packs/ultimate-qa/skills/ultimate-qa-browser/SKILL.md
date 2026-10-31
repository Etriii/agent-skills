---
name: ultimate-qa-browser
description: Exercise QA user journeys, roles, accessibility, and visual states with a browser against an authorized local or staging target.
---

# Ultimate QA Browser

Read the kit's `11_BROWSER_ASSISTED_CHECKS.md` if available. Confirm the exact local or staging URL, available test roles, data reset method, and browser tool. Do not browse production by default. Map critical journeys from requirements and routes; cover success, validation, permission denial, empty state, loading, error, keyboard navigation, and narrow viewport where relevant.

Prefer installed Playwright or an available browser automation tool. Wait for navigation, network, and assertions to settle before judging results. On failure save URL, role, steps, expected and observed behavior, console/network clues, screenshots, and a trace when supported. Use automated accessibility checks as leads; keyboard flow and meaningful wording still need judgment. Mark a check manual only after available automation and equivalent evidence have been tried or a concrete limitation is documented.

Do not create brittle tests for every checklist sentence. Add repeatable regression coverage for critical paths and confirmed defects in the project's existing test framework when the user has authorized code changes.

## Generated artifacts

Apply this section only when the workflow saves generated reports, logs, previews, or run evidence. Use a stable skill-owned root in the target workspace, never the installed skill directory. Allocate each new run with an exclusively created `YYYYMMDDTHHMMSSZ-<unique-id>/` directory (UTC); preserve earlier runs and resume the identified active run. Reject linked paths, traversal, and unrelated same-name folders.

Before saving inside Git, resolve the intended repository root, refuse already tracked output, and inspect its `.gitignore`. Preserve existing bytes and line endings; append a root-anchored rule for only the generated output root when needed, creating `.gitignore` if absent. Verify exclusion with `git check-ignore`; never untrack files automatically. Outside Git, disclose that exclusion is unverified; workflows requiring Git retain that prerequisite. If safe storage or required exclusion fails, report the exact limitation before saving and use chat only when this workflow permits it.

Preserve existing state schemas, version identifiers, historical files, and resume paths; timestamp new run evidence beneath its existing owner without an implicit migration. Application source and project documents explicitly intended for version control retain their own contracts. This section does not authorize extra output for a chat-only request or expand the workflow's scope.
