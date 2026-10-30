# Mobile web review

Mobile is part of the main UI/UX review. `ultimate-mobile` is a direct mobile-focused entrypoint using this same playbook; it is not needed to enable mobile checks. Apply only the current discipline: UI-only covers presentation while preserving task flow; UX-only covers interaction/navigation while preserving visual identity. The mobile entrypoint covers both within mobile web scope, not a new native app.

## Establish mobile evidence

Use the application's supported phone widths and a width where content actually fails. When no supported widths are documented, start around 360-390 CSS pixels, check 320 CSS pixels for narrow reflow, and inspect landscape or an intermediate width when the journey needs it. Treat widths as useful coverage, not a substitute for testing real breakpoints, content lengths and zoom. Record exact viewport, browser, role, state and evidence type.

Inspect with touch/coarse-pointer emulation when available and keyboard access where relevant. Check long/localized labels, large text, browser zoom, safe areas, sticky/fixed layers, virtual-keyboard occlusion and content scroll. Browser emulation does not prove real-device behavior or mobile screen-reader acceptance. Report device-only gaps. Keep a wide-layout baseline to ensure responsive changes do not regress desktop; a mobile request does not authorize a desktop redesign.

## Prioritize cramped headers

Inventory the purpose and frequency evidence for every header element: navigation toggle, current page, breadcrumb ancestors, store/tenant switcher, search, messages, notifications and account control. Names that happen to match may represent different entities; trace the store and signed-in user before treating them as duplicates.

Preserve current task/location, essential navigation and meaningful active store/tenant identity. On narrow screens, shorten or collapse breadcrumb ancestors through an existing back/overflow pattern rather than ellipsizing every segment until none is useful. Keep full names reachable through an accessible menu/detail view, not a hover-only tooltip.

A reasonable profile pattern is an avatar/account trigger in the header with full name, account context and account actions inside its dropdown. Use an accessible name such as Open account menu; a photograph or initials alone is insufficient. Keep relevant current store context visible when users can act in several stores. A user avatar must not become the sole ambiguous store switcher.

Prioritize actions instead of removing them wholesale: use existing search expansion or overflow patterns when justified, keep important notification state understandable, and verify relocated actions remain reachable by the same roles. Check trigger/menu target sizes, edge clipping, logical focus, Escape/dismissal, focus return, outside-tap behavior and scrolling. Do not invent a new navigation system if an existing responsive header pattern fits.

## Align and reflow filter controls

For rows combining search, labeled selects and date inputs, inspect the control boxes separately from label/helper/error wrappers. Use intentional grid/flex alignment and consistent component sizing; do not force field labels to disappear to make borders align.

On phones, let search span a row; place related date filters side by side only if labels, dates and controls remain usable, otherwise stack them. A filter disclosure/sheet can fit many optional filters, but keep active-filter count/summary, apply/clear behavior and state discoverable. Preserve existing query parameters, pending/applied semantics, validation, pagination and results when changing the presentation. Check native date controls and input behavior rather than assuming desktop sizing will fit.

## Keep dialogs and actions distinct

Ensure dialogs fit the viewport, allow necessary content scroll, remain above fixed chrome and retain a reachable close/cancel path. Actions may wrap or stack on narrow screens with clear spacing and consistent logical order. Do not use CSS reordering that makes keyboard order contradict the visible order.

Use the target's semantic tokens and established hierarchy: Cancel usually secondary/neutral, the chosen action primary, and genuinely destructive consequences danger-styled when appropriate. Labels and explanation must communicate the distinction without color. Check default, hover, focus, pressed, disabled and loading states in supported themes. Two equally prominent filled buttons should be justified rather than accepted automatically.

For a Sign out confirmation, a possible improvement is Cancel as a quiet outline/text action and Sign out as the distinct primary or appropriate caution action. Do not assume signing out destroys saved data or requires a password; verify the actual save/authentication behavior before recommending such warnings. Keep confirmation and unsaved-change handling owned by existing code. Follow the established accessible dialog's focus policy; for irreversible consequences prefer the safe initial focus. Test that dismissal cancels and returns focus without triggering the action.

## Preview and prove

Follow [workflow](workflow.md) approval/auto rules. Show mobile before/proposed comparisons for affected pages and components, including open account menus, active filters and dialog states where relevant. Include the wide-layout preservation check. A cleaner closed header is not enough if its menu or filters become unusable.

Verify actual rendered wrapping, alignment, accessible names, touch/keyboard reachability, focus/dismissal, state preservation and unauthorized-action boundaries. Exercise long names and error/empty/loading states. Keep source-only findings, browser emulation, real-device observation and assistive-technology proof separate. Use [preview and verification](preview-and-verify.md) for the shared implementation and reporting contract.
