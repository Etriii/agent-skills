# UI specialist

Review visual presentation against the page's task and existing design system. UI-only work preserves information architecture, routes and task order. A necessary structural UX change becomes a separately identified recommendation; do not implement it through UI-only authorization. Accessibility defects inside the selected visual scope remain in scope.

## Trace and inspect

- Find existing tokens, component library, typography, layout containers, breakpoints, icon family, themes and real brand assets. Reuse these before adding CSS values or dependencies. Do not assume React, Tailwind or a particular UI kit.
- Trace shared style/component callers. Check real content, long/localized labels, large values, missing images, keyboard focus and browser zoom. Identify the responsible owner instead of stacking specificity or hiding overflow.
- Review visual hierarchy: clear page purpose, coherent headings, legible text, task-relevant primary action, visible current location and appropriate emphasis. Count competing primary actions and duplicated labels without imposing an arbitrary limit.
- Review composition: alignment, consistent gutters, grouping, grid/card density, reading width, whitespace and section rhythm. Dense operational tables can be correct; removing every card or making every screen sparse is not a quality rule.
- Compare related controls' baselines, top/bottom edges, heights, labels, icon placement and hit areas. A search field beside labeled date filters should share an intentional control row; use the responsible grid/flex alignment and field wrappers rather than arbitrary margin nudges. Inspect errors, helper text and wrapped labels before calling different heights a defect. Keep required labels and accessible names when aligning controls.
- Review typography and color: established type scale, meaningful weights, line height, line length, contrast, link recognition, light/dark states and semantic status colors. Keep labels available; truncation needs a practical way to recover essential content.
- Review controls and media: coherent icons, understandable affordances, distinguishable interactive states, consistent image ratios, reserved media space and useful empty states. Use authentic product content or clearly labeled fixtures. Never invent testimonials, trust badges or business metrics.
- Review action hierarchy and semantic color. Primary, secondary/cancel and destructive actions need distinguishable emphasis, clear labels, spacing, focus and state contrast. Two equally bright filled buttons in a confirmation dialog can obscure which action is safe or intended. Prefer the existing secondary/outline treatment for Cancel and the appropriate primary or danger treatment for the consequential action. Do not communicate risk through color alone or assign every Sign out action a destructive-red style; signing out is not deletion of saved data.
- Review responsive composition at the app's supported narrow and wide sizes and at a width where the actual layout breaks. Check overflow, wrap, sticky overlays, safe areas and usable targets. Reflow content; shrinking desktop until it fits is not a mobile design.
- Review motion and feedback: purposeful transitions, reduced-motion behavior, stable loading geometry and immediate feedback for actions. Do not add animation merely to appear premium.

## Accessibility floor

Use semantic links, buttons, headings, forms and tables. Check accessible names, labels, error associations, keyboard traversal, visible and unobscured focus, content reflow/zoom, contrast and non-color status cues. Aim for applicable WCAG 2.2 AA criteria; do not declare conformance from a checklist. Normal text generally needs 4.5:1 contrast, large text 3:1, and relevant UI graphics 3:1; verify actual foreground/background combinations. Target size criteria have exceptions and different thresholds by platform; use the target's standards and practical touch usability rather than labeling every sub-44px control a WCAG failure.

Keep automation, keyboard/browser checks and assistive-technology observation separate. CSS inspection cannot prove screen-reader behavior or rendered contrast across every state.

## Choose a direction deliberately

For an existing product, describe the current visual language and the few adjustments that solve confirmed issues. For a broader approved redesign, specify a compact direction covering hierarchy, density, layout, type, color, imagery and interaction states. Tie choices to audience, actual content and task. Elegance means coherent decisions and easy reading/operation; it does not mandate a new palette, huge whitespace, pills, glass effects or a marketing hero.

Consult Taste for subject-specific intent and real-content composition, frontend-design for deliberate typography and meaningful microcopy, and Pro Max for relevant interaction/accessibility checks through [source guidance](source-guidance.md). Treat upstream aesthetic prescriptions as context-dependent ideas. Preserve useful existing patterns and user preferences when they differ.

For each visual recommendation, show the concrete defect or opportunity, proposed adjustment, responsible owner, responsive/state effects and acceptance evidence. In the final comparison, preserve the same content and state so apparent improvement does not come from hiding information or using more flattering data.

For responsive web reviews, include [mobile review](mobile-review.md). Inspect header priorities, filter wrapping and dialog actions at narrow widths; do not reserve mobile checks for the standalone shortcut.
