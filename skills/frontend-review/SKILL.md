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
