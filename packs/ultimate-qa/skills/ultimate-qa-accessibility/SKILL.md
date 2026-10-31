---
name: ultimate-qa-accessibility
description: Audit web accessibility through automated rules, keyboard journeys, semantics, and assistive-technology evidence.
---

# Ultimate QA Accessibility

Map the essential pages and roles, including error, dialog, loading, and empty states. Use an installed browser and accessibility engine where available. Run automated rule checks after each page has settled; collect rule ID, affected element, screenshot, and DOM context. Check labels, focus order, visible focus, keyboard operation, contrast, headings, status announcements, and responsive zoom on critical journeys.

Fix automated false positives by inspecting the actual rendered state. A zero-violation scanner result is limited evidence: it does not certify usable reading order, screen-reader announcements, or content clarity. Use a screen reader when one is available; otherwise provide exact focused manual steps only for those remaining judgments. Link each issue to the page, role, state, and applicable accessibility criterion when known.

Retest confirmed defects with the same viewport, browser, account, and page state. Preserve screenshots and test output in the current QA version's evidence folder.

## Generated artifacts

Apply this section only when the workflow saves generated reports, logs, previews, or run evidence. Use a stable skill-owned root in the target workspace, never the installed skill directory. Allocate each new run with an exclusively created `YYYYMMDDTHHMMSSZ-<unique-id>/` directory (UTC); preserve earlier runs and resume the identified active run. Reject linked paths, traversal, and unrelated same-name folders.

Before saving inside Git, resolve the intended repository root, refuse already tracked output, and inspect its `.gitignore`. Preserve existing bytes and line endings; append a root-anchored rule for only the generated output root when needed, creating `.gitignore` if absent. Verify exclusion with `git check-ignore`; never untrack files automatically. Outside Git, disclose that exclusion is unverified; workflows requiring Git retain that prerequisite. If safe storage or required exclusion fails, report the exact limitation before saving and use chat only when this workflow permits it.

Preserve existing state schemas, version identifiers, historical files, and resume paths; timestamp new run evidence beneath its existing owner without an implicit migration. Application source and project documents explicitly intended for version control retain their own contracts. This section does not authorize extra output for a chat-only request or expand the workflow's scope.
