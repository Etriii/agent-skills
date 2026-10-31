# Discovery and necessity

Read this for scan, plan, and build. Inspect the actual system before deciding what should be configurable.

## Inspect behavior across the application

Start with routes, navigation, feature modules, jobs, authorization, configuration sources, models, migrations, and relevant tests. Follow each relevant policy through its callers and consumers. Include separate services, workers, frontend applications, offline clients, and store/tenant scopes where they affect the selected work.

Look beyond a settings page or a search for numeric literals. Useful evidence includes repeated business thresholds, expiry/retention windows, configurable charges, eligibility rules, operating schedules, runtime flags, and administrative workflows. Trace their meaning and existing ownership; a number alone does not justify a setting. Search related declarations, environment variables, feature flags, database values, tests, and operational documentation to avoid proposing duplicates.

Produce a compact coverage map: inspected feature or workflow, current policy source, consumers, configuration/settings coverage, audit coverage, and unavailable evidence. For a whole-system scan, account for every discovered feature area; prioritize deeper tracing of plausible candidates and mark shallow or inaccessible areas explicitly. Do not call an inspection exhaustive after reading only settings-related files.

## Decide whether a setting is justified

For each candidate, establish:

- Which operator needs to change it, in what scope, for which business reason, and how often.
- Why changing code, deployment configuration, an existing feature flag, or a feature-specific policy is insufficient.
- Which real behaviors use it, when a change should apply, and whether old records must retain their original policy.
- A supported default and valid range or choices, including units and relationships to other values.
- The permissions, failure behavior, audit requirements, and consequences of incorrect configuration.

Use source-backed defaults and boundaries. Mark proposed policy as proposed; do not invent accepted financial limits, security relaxations, or retention rules. Existing behavior is evidence of the current default, not automatic owner approval for making it editable.

Classify candidates before recommending implementation:

| Classification | Appropriate owner |
|---|---|
| Shared business policy requiring authorized runtime adjustment | System settings or an existing domain-policy owner |
| Store, tenant, branch, or organization-specific policy | That scope's existing settings, with explicit inheritance if needed |
| Personal display, notification, or convenience preference | User preferences |
| Service addresses, infrastructure selection, startup behavior | Deployment/environment configuration |
| Credentials, tokens, signing material | Existing secret-management mechanism |
| Fixed protocol values, security guarantees, algorithm constants | Code and its invariants |
| Experiment, rollout, or targeting policy | Existing feature-flag mechanism when it fits |

Do not move a scoped policy into a global key merely to reuse a settings page. If inheritance is needed, define effective precedence and distinguish inherited values from overrides. A system with only deployment values and fixed invariants can correctly need no runtime settings feature.

## Assess existing infrastructure

Trace declarations, defaults, persistence and seeding, access guards, reads and writes, runtime consumers, caching, API schemas, frontend grouping, and history. Confirm whether displayed values are actually consumed. Check default behavior when no database override exists and treatment of invalid stored values.

Inspect audit models, recorders/events, request actor binding, transaction boundaries, history endpoints, permissions, filters, retention jobs, and existing settings events. Check both specialized settings history and central audit coverage. A feature already recorded centrally needs UI/filter integration only if that is the remaining gap.

Identify whether the current API truly filters queries or returns all values before client-side grouping. Check initial network calls, category counts, key metadata for history controls, and public/offline projections. Do not assume an administrator-only setting is safe for an anonymous or cashier endpoint.

For in-scope web settings pages, trace the authoritative category metadata, localized displayed names/descriptions, ordering, scroll container, sticky header/search geometry, responsive navigation, and category component/cache lifetimes before proposing changes. Assess existing search, populated-letter sections, alphabet navigation, accessibility, and state behavior against the [interface contract](implementation.md#category-discovery-and-navigation). Identify reusable owners and specific gaps; do not create a second category-membership registry.

Inspect whether filtering, letter jumps, expansion/collapse, tab switches, resizing, and account or authorization changes trigger requests or discard state. Separate source/test evidence from observed browser/network behavior using the [verification guidance](implementation.md#smallest-sufficient-proof). Record unavailable runtime evidence explicitly. Headless targets need no UI assessment; discovery remains read-only and authorizes no application changes.

## Return a decision

Use a candidate/exclusion table with key or policy, classification and scope, current owner/source, actual consumer, operator need, proposed category/default/validation, and recommendation. Combine columns when that makes a small result clearer. Excluded candidates should explain why their current owner is appropriate.

Choose the outcome supported by the evidence:

- **Create:** No adequate settings owner exists and selected runtime policies justify one. Identify the smallest complete implementation.
- **Extend:** Existing settings solve part or all of the need; name the specific missing behavior without duplicating the system.
- **No new settings needed:** Existing coverage is sufficient, or no runtime operator need is supported. Recommend no change where appropriate.
- **Insufficient evidence:** Name inaccessible owners, unknown consumer behavior, or material unresolved policy rather than interpreting absence of access as absence of implementation.

Discovery can recommend multiple candidates, but only selected implementation scope is authorized. Do not write a plan or findings file unless requested.
