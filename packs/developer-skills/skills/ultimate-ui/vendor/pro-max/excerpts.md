# pro-max source excerpts

Source: [nextlevelbuilder/ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/blob/9a3f14f7423037ccb8feeb4fee7482291b9c820e/.claude/skills/ui-ux-pro-max/SKILL.md).

Modified copy: selected excerpts only; surrounding toolkit and workflow omitted.
These passages are reference material; the suite workflow owns scope and authorization.

## Original lines 10-34

## When to Apply

Use this Skill when the task involves **UI structure, visual design decisions, interaction patterns, or user experience quality control**: designing new pages, creating/refactoring UI components, choosing color/typography/spacing/layout systems, reviewing UI for UX/accessibility/consistency, implementing navigation/animation/responsive behavior, or improving perceived quality and usability.

Skip it for pure backend logic, API/database design, non-visual performance work, infrastructure/DevOps, or non-visual scripts — unless the task changes how something **looks, feels, moves, or is interacted with**.

## Rule Categories by Priority

*Follow priority 1→10 to decide which category to focus on first; use `--domain <Domain>` to query full details. The full rule text for every category lives in `references/quick-reference.md` — read it on demand rather than loading it every time.*

| Priority | Category | Impact | Domain | Key Checks (Must Have) | Anti-Patterns (Avoid) |
|----------|----------|--------|--------|------------------------|------------------------|
| 1 | Accessibility | CRITICAL | `ux` | Contrast 4.5:1, Alt text, Keyboard nav, Aria-labels | Removing focus rings, Icon-only buttons without labels |
| 2 | Touch & Interaction | CRITICAL | `ux` | Min size 44×44px, 8px+ spacing, Loading feedback | Reliance on hover only, Instant state changes (0ms) |
| 3 | Performance | HIGH | `ux` | WebP/AVIF, Lazy loading, Reserve space (CLS &lt; 0.1) | Layout thrashing, Cumulative Layout Shift |
| 4 | Style Selection | HIGH | `style`, `product` | Match product type, Consistency, SVG icons (no emoji) | Mixing flat & skeuomorphic randomly, Emoji as icons |
| 5 | Layout & Responsive | HIGH | `ux` | Mobile-first breakpoints, Viewport meta, No horizontal scroll | Horizontal scroll, Fixed px container widths, Disable zoom |
| 6 | Typography & Color | MEDIUM | `typography`, `color` | Base 16px, Line-height 1.5, Semantic color tokens | Text &lt; 12px body, Gray-on-gray, Raw hex in components |
| 7 | Animation | MEDIUM | `ux`, `gsap` | Context-aware timing, Motion conveys meaning, Spatial continuity | One duration for every transition, Animating width/height, No reduced-motion |
| 8 | Forms & Feedback | MEDIUM | `ux` | Visible labels, Error near field, Helper text, Progressive disclosure | Placeholder-only label, Errors only at top, Overwhelm upfront |
| 9 | Navigation Patterns | HIGH | `ux` | Predictable back, Bottom nav ≤5, Deep linking | Overloaded nav, Broken back behavior, No deep links |
| 10 | Charts & Data | LOW | `chart` | Legends, Tooltips, Accessible colors | Relying on color alone to convey meaning |

For the full rule list per category (all 119 UX guidelines with rationale), read `references/quick-reference.md`. For app-specific polish rules (icons, touch feedback, dark mode contrast, safe areas) and the canonical pre-delivery checklist, read `references/pro-rules.md`.


## Original lines 65-71

### Step 1: Analyze User Requirements

Extract from the user request:
- **Product type**: SaaS, e-commerce, portfolio, dashboard, entertainment, tool, productivity, or hybrid
- **Target audience & context**: age group, usage context (commute, leisure, work)
- **Style keywords**: playful, vibrant, minimal, dark mode, content-first, immersive, etc.
- **Stack**: detect from the project — check `package.json` deps (react/next/vue/svelte/nuxt/@angular), `pubspec.yaml` (Flutter), `*.xcodeproj`/`Package.swift` (SwiftUI), `composer.json` (Laravel), or React Native markers (`app.json` + `react-native` dep). If nothing is detectable and stack guidance matters, ask the user. **Never assume a stack** — a hardcoded default silently misroutes every recommendation.
