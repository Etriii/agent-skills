# PDF and Excel design

## Shared design and filter disclosure

Reuse the target's branding, typography, palette, labels, status/type mappings, and renderers. Keep one owned definition for metric meaning and color decisions, with format-specific rendering. Use restrained headings, whitespace, subtle rules, readable contrast, and consistent numeric alignment.

Show the validated effective filters in both formats, including applied defaults. Never print raw request parameters as if they determined the query. Include the period, date field/time zone, relevant organization/store/branch/self scope, supported status/type/search filters, selected content, generation time, and applicable limits. Use readable values such as All statuses for unrestricted fields. Show section-specific filters beside their section or in a clearly named filter block. Disclose unsupported list filters that were not carried into the report; do not imply exact list equivalence.

Only include scope and preparer metadata permitted for that audience. Do not print secrets or private query tokens. Keep the displayed filter description aligned with the actual authorized queries and renderers.

## Full-report PDF

1. Cover on page one: system and organization name, available logo, report title, reporting period, audience/scope, permitted preparer identity/role, generated date/time/time zone, report reference, section count and accurately labelled record count. Omit unavailable optional contact details rather than inventing them.
2. Contents starting on page two: matching numbered section titles, subsection hierarchy where useful, and accurate rendered page numbers. Allow contents to span pages; do not promise that the summary is always page three.
3. Summary starting on a separate page after contents: headline figures, totals by section, meaningful status/type counts and shares, filters, and short interpretation notes.
4. Selected report sections with purpose/counting basis, figures, breakdowns, records, and totals. Begin major sections on new pages.
5. Reading notes covering definitions, columns, filters, exclusions, denominators, and known limitations. Detailed mode expands this material without removing essential notes from mid mode.

Use the renderer's own pagination facilities or a verified multi-pass layout. Recalculate contents after layout changes. Add useful running headers and Page N of M footers with report identity/generation time; a quiet cover may omit them.

Records must remain visually distinct: readable tables with repeated headings and subtle separators/banding, or cards with identity, primary status, and a labelled field grid. Use existing application patterns. Choose cards, selected columns, or landscape pages for wide records instead of shrinking all text. Keep labels with their values, avoid clipped content and accidental blank pages, and preserve Unicode/currency glyphs.

Use colored pills for status/type fields and restrained indicators for figures; keep other text readable. Meaning must survive grayscale printing and color-vision differences through explicit labels. Do not paint an entire record with competing category colors.

Any PDF row cap must say Showing X of Y and explain how to obtain the remaining records. Full-population summaries remain uncapped. Only claim Excel contains every matching row when the workbook actually does.

The full-report structure applies to both detail levels. Do not silently convert unrelated receipts, tickets, or certificates into multi-page reports.

## Actual Excel workbook

Create a genuine `.xlsx` file rather than renamed CSV, HTML, or an image of a PDF.

Use sheets in this order:

- **Cover:** report/system identity, permitted preparer, period, generation time, reference, scope, and effective filters.
- **Contents:** useful internal links to Summary, Breakdowns, record sheets, and Reading Notes.
- **Summary:** headline figures, accurately labelled totals, categorical counts/shares, and filter context.
- **Breakdowns:** clearly separated grouped figures for selected sections.
- **Record sheets:** one coherent dataset per sheet, with a stable identity and permitted columns.
- **Reading Notes:** metric/column definitions, filter meanings, units, exclusions, limits, and color legend where useful.

Respect an explicit alternate layout requirement; do not duplicate blocks merely to fill an empty sheet. Keep absence of applicable breakdowns clear. Reuse suitable existing workbook planning/writing primitives.

Record sheets need frozen headings, autofilters or native tables, useful widths, wrapped long labels, readable fills, number/date formats, right-aligned numeric data, and clear totals. Keep record tables rectangular; avoid merged cells inside filterable data. Decorative cover merges must not damage record usability. Use existing sensible print setup, repeating headings and page orientation where supported.

Write money/counts/percentages as numeric values, dates as dates with a documented time zone, and identifiers/barcodes as text preserving leading zeros and long digits. Keep source text as literal text even when it begins with a formula marker. Trusted generated formulas may be used for totals with appropriate cached values and read-back checks; never turn untrusted values into formulas or external links.

Fill status/type cells using the same owned mappings as PDF and screen. Freeze the actual heading row, not a guessed row number. Keep sheet names unique, valid, and within Excel limits. Export all authorized matching rows unless an explicit limit applies; partition oversized datasets using the existing pattern and disclose counts rather than silently losing rows.

## Reference patterns and adaptation

BALE illustrates shared report definitions, a server-scoped catalog, grouped counts/colors, full-row workbook exports, and queued retained files. Its PDF combines contents and summary and its workbook starts with Summary; adapt those renderers to the separate front matter specified above.

LMS illustrates a separate cover/contents/summary, record cards, shared palettes, summary counts by kind, workbook section links, Breakdowns, and Reading Notes. Neither example requires adopting its backend framework, branding, retention values, or creator-only sharing policy.

These are portable design patterns, not runtime dependencies or copied implementations. Verify the target's present behavior instead of assuming either reference is available.
