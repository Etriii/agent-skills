---
name: frontend-review
description: Review web interface behavior accessibility and responsive states with explicit visual evidence limits.
---

# Frontend Review

Input: Affected routes, components, user journeys, available design references and browser evidence.

Output: Prioritized UI findings with route or source locations, reproduction and required acceptance checks.

1. Trace component responsibilities, state ownership and API boundaries before recommending changes.

2. Inspect loading, empty, error, disabled and permission states; check form validation and focus recovery.

3. Check semantic controls, labels, keyboard order, visible focus, contrast and announced errors. Use actual browser evidence when available.

4. Assess narrow and wide layouts, zoom, overflow and print only where the feature needs them.

5. Separate source inspection, automated accessibility checks, rendered screenshots and manual assistive-technology proof. Give precise capture steps for missing visual evidence.

Limits: Review by default. Do not claim visual acceptance from source or a successful build; do not redesign unrelated screens.

## Generated artifacts

Apply this section only when the workflow saves generated reports, logs, previews, or run evidence. Use a stable skill-owned root in the target workspace, never the installed skill directory. Allocate each new run with an exclusively created `YYYYMMDDTHHMMSSZ-<unique-id>/` directory (UTC); preserve earlier runs and resume the identified active run. Reject linked paths, traversal, and unrelated same-name folders.

Before saving inside Git, resolve the intended repository root, refuse already tracked output, and inspect its `.gitignore`. Preserve existing bytes and line endings; append a root-anchored rule for only the generated output root when needed, creating `.gitignore` if absent. Verify exclusion with `git check-ignore`; never untrack files automatically. Outside Git, disclose that exclusion is unverified; workflows requiring Git retain that prerequisite. If safe storage or required exclusion fails, report the exact limitation before saving and use chat only when this workflow permits it.

Preserve existing state schemas, version identifiers, historical files, and resume paths; timestamp new run evidence beneath its existing owner without an implicit migration. Application source and project documents explicitly intended for version control retain their own contracts. This section does not authorize extra output for a chat-only request or expand the workflow's scope.
