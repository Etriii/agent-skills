---
name: ultimate-qa-accessibility
description: Audit web accessibility through automated rules, keyboard journeys, semantics, and assistive-technology evidence.
---

# Ultimate QA Accessibility

Map the essential pages and roles, including error, dialog, loading, and empty states. Use an installed browser and accessibility engine where available. Run automated rule checks after each page has settled; collect rule ID, affected element, screenshot, and DOM context. Check labels, focus order, visible focus, keyboard operation, contrast, headings, status announcements, and responsive zoom on critical journeys.

Fix automated false positives by inspecting the actual rendered state. A zero-violation scanner result is limited evidence: it does not certify usable reading order, screen-reader announcements, or content clarity. Use a screen reader when one is available; otherwise provide exact focused manual steps only for those remaining judgments. Link each issue to the page, role, state, and applicable accessibility criterion when known.

Retest confirmed defects with the same viewport, browser, account, and page state. Preserve screenshots and test output in the current QA version's evidence folder.
