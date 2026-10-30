# Discovery and metric specification

## Establish coverage

Inventory routes, navigation, pages, tabs, dialogs, background workflows, permissions, services, entities, relationships, existing reports, list exports, and document viewers. Look beyond directories named reports and trace cross-repository APIs where needed. Record shared owners and each meaningful workflow even when multiple pages reuse one component.

Prioritize workflows with a reporting audience and recurring decisions: transactions and money, stock and movements, approvals, lending, visits, membership, service delivery, compliance, and audit history. These are discovery prompts, not mandatory reports for every application. Distinguish analytics from problem/abuse reports and operational single-record documents.

Cross-check discovered candidates against existing definitions, registry entries, queries, report buttons, dashboards, and exports before declaring a gap. A missing button may be an integration gap rather than a missing report.

Use one inventory row per candidate:

| Feature/workflow and source | Audience and decision | Existing report/export | Classification and evidence | Data/query owner | Scope/permission boundary | Gap and next action |
|---|---|---|---|---|---|---|

Classify as Required, Recommended, Covered, Unknown, or Unnecessary. Required needs an explicit requirement or documented operational obligation. Recommended needs a concrete audience and decision. Covered means an existing report meets that need. Page existence is insufficient evidence of necessity; mark unknown policy instead of claiming certainty.

Include deliberate no-report decisions and unchanged coverage. State discovered and inspected areas, runtime/role coverage, exclusions, and inaccessible sources. Do not claim whole-system discovery from one folder or text search.

## Specify selected reports

Bind each report to these decisions before implementation:

- Purpose, audience, recurring decision, and evidence of need.
- Record grain and stable identity: one row per sale, loan, user, movement, or other defined unit. Identify one-to-many joins and deduplication rules.
- Authoritative tables/services, relationship ownership, known omissions, archive/deletion treatment, and source-field availability.
- Reporting date field per metric, reporting time zone, range inclusivity, and distinction between events in a period and state as of a date. Issue date, return date, payment date, and current status are not interchangeable.
- Validated effective filters, defaults, supported search, sort, scope, selected sections/columns, and which list filters have no report equivalent.
- Metric formulas, units/currency, exclusions, cancelled/reversed/refunded treatment, denominator, rounding, null semantics, and reconciliation expectations.
- Core figures, categorical groups, detail columns, visual mappings, export formats, limits, and unsupported detailed-mode analysis.
- Current permission matrix, Generated Reports audience, retained-file metadata, expiry configuration, and testable acceptance.

Reuse authoritative query helpers and money/date types. Aggregate the entire matching authorized set, never only a preview page or capped PDF. Prevent joins from multiplying records or monetary amounts. Keep different currencies and different counting units separate.

## Categorical totals and color

Identify meaningful categorical fields such as status, type, role, stage, payment method, and fulfilment mode. For each useful grouping show labels, counts, applicable monetary totals, and a share with an explicit denominator.

Example only: 100 matching accounts, Active 80 (80%), Inactive 15 (15%), Unknown 5 (5%). Also show the overall 100. Use actual domain labels; do not collapse suspended, pending, archived, and inactive into one category without a stated rule.

- Exhaustive, mutually exclusive categories must sum to their population. Preserve unknown/missing values as an explicit bucket; show declared zero-count categories where meaningful.
- An empty population has zero counts and a defined zero/undefined percentage display, never division by zero.
- Multi-valued tags can overlap. Label counts as memberships or record participation and explain totals/shares that exceed the unique-record population. Do not force them to reconcile as exclusive statuses.
- Separate breakdowns by status, type, and other fields; do not add their totals together. Combined reports may contain the same entity in multiple sections: label section-row totals rather than claiming unique people or transactions.
- Derive tones from the existing field/value mapping. Type categories need distinguishable categorical colors without implying success or failure. Retain text labels and a legend when meaning is not obvious.
- New unmapped enum values need explicit review and a regression check. Use a readable neutral fallback for genuinely open-ended or unknown values; do not silently treat a known failure state as success.

## Freeze and refresh semantics

Use shared validated definitions and aggregation for screen and exports. Sharing a builder establishes matching semantics, not identical data across separate requests. If data may change between preview and generation, state that the export refreshes it and record its generation time; use the existing snapshot mechanism when exact preview/export identity is required.

Mark a preview outdated when filters, sections, columns, report identity, or relevant scope change. Retain each successfully generated file as its own immutable artifact; repeated downloads do not silently regenerate it against current data.
