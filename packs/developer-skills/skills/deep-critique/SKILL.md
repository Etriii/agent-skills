---
name: deep-critique
description: Give a detailed evidence-based critique with ratings challenged assumptions and prioritized improvements for an idea plan design implementation document or decision.
---

# Deep Critique

Input: A subject supplied explicitly or established in the conversation, its intended outcome, and available supporting material.

Output: A candid assessment with explained ratings, substantiated weaknesses, counterarguments, a verdict, and prioritized improvements. Full assessment is the default.

## Start without a mode menu

Treat `$deep-critique` alone as `full` on the current subject. Do not ask the user to select a mode or retype material already available. If no subject is established, ask only what they want assessed. If several subjects are plausible and the choice changes the review materially, ask which one.

Use stated goals and constraints. Infer low-impact context where reasonable, label assumptions, and continue. Ask before a missing fact would make the assessment misleading. Do not equate invoking the skill with reviewing every file or project in the workspace.

The commands below are agent chat instructions, not terminal commands. Natural-language requests can select a mode, focus, depth, or tone without exact syntax. Respect explicit requests for a shorter output or omitted ratings.

| Invocation suffix | Behavior |
|---|---|
| No suffix or `full` | Complete detailed assessment, including ratings and relevant alternatives. No interactive interview first. |
| `review` | Focus on strengths, weaknesses, risks, and recommendations, with a compact scorecard. |
| `roast` | Sharper criticism with explained ratings and actionable fixes. Tone changes; evidence standards do not. |
| `question` | Ask one decision-changing question at a time and adapt to each answer. Summarize when resolved or when the user asks to stop. |
| `rate` | Focus on category and overall scores, supporting reasons, and what would raise each score. |
| `compare` | Apply the same criteria to supplied alternatives and recommend one for the stated constraints. |
| `help` | Explain the default, list modes with copyable invocations, and stop without running a critique. |

Recognize a mode word as a command only when it clearly selects a mode; a document titled Review or a request about exchange rates is still subject material. If a command is ambiguous or unsupported, explain the supported choices instead of silently performing a different review. For `compare`, ask for a missing alternative unless the conversation already establishes it.

## Combine modes

Accept multiple explicit modes, such as `$deep-critique roast rate`, or their natural-language equivalent. Merge their requirements into one assessment without duplicate findings or scorecards. Mode order does not change the result; repeated modes count once.

- `roast rate` combines sharp criticism with a detailed scorecard. Roast alone keeps its explained ratings.
- `review compare` reviews the supplied alternatives against common criteria and recommends one.
- `full` subsumes `review` and `rate`; keep `roast` for tone, `compare` for explicit alternatives, and `question` for an interview first.
- With `question`, ask one question at a time before the final combined assessment. With question alone, summarize the interview when resolved or stopped; do not silently expand it to full mode.
- If `help` is included, show help and stop without creating files or running an assessment.

Use canonical mode order `full`, `review`, `roast`, `question`, `rate`, `compare` for storage categories. For example, `rate roast roast` and `roast rate` both use `roast+rate`; `full rate roast` uses `full+roast`. The [storage helper](scripts/report_store.py) normalizes explicit modes; do not parse arbitrary subject text with it.

## Save results in the target workspace

Persist assessments by default under `<target-root>/.deep-critique/<canonical-modes>/<UTC-timestamp>-<unique-id>/`. Bare invocation uses `full`. Resolve the root from the user's target workspace, using its Git root when applicable, never the skill installation folder. A critique of text still uses an established workspace; if none is clear or writable, complete the assessment in chat and explain why saving is unavailable. Respect an explicit chat-only request.

Read [report storage](references/report-storage.md) before creating or updating artifacts. Use the bundled Python helper for root validation, run reservation, mode normalization, Git ignore updates, transcripts, and final publication. Do not improvise a second storage implementation. Store all results in one report, with question transcripts attached automatically and extra evidence only when useful.

The helper appends `/.deep-critique/` to the target root's `.gitignore` when needed and verifies exclusion when Git is available. It preserves existing content, refuses tracked output and unrelated same-name folders, and rejects linked output paths. Do not untrack reports or force past a storage refusal. Continue the critique in chat and report the exact saving limitation.

Each assessment starts a new run. Keep a questioning session in its reserved run until finalized. Reuse the returned run reference only to continue that same unfinished assessment or retry publishing identical content. Never replace a completed report. Interrupted runs have no completion record; label them unfinished rather than passed or complete.

## Examine the subject on its own terms

1. Establish the goal, audience, constraints, maturity, and scope. Describe the strongest defensible version before judging it. An early concept and a finished deliverable need different proof.
2. Inspect supplied material and relevant accessible evidence. For an implementation, trace actual behavior and responsible boundaries. For an argument, plan, or document, trace claims, assumptions, supporting material, and consequences. Do not impose software checklists on unrelated subjects.
3. Identify weaknesses through concrete counterexamples, contradictions, failure scenarios, or tradeoffs. Separate observed flaws, plausible risks, missing information, and preferences. Cite files and lines, document sections, supplied statements, or sources as appropriate.
4. Actively try to disprove serious criticisms using counter-evidence or a stronger interpretation. Remove invalidated objections; qualify those that remain uncertain. Never manufacture faults to satisfy a roast or a target finding count.
5. Preserve strengths that survive scrutiny. Consider simpler or more suitable alternatives only when they address a real weakness. State their costs and what would change the recommendation.

Be direct about the work and reasoning without personal insults. Do not treat taste, missing polish, or hypothetical future requirements as blockers. A review is not an implementation task; apart from its report artifacts and target Git ignore entry, do not edit the subject, install dependencies, mutate data, publish, or send messages without separate authorization. Use existing tools for relevant authorized checks, and distinguish inspected material from executed verification.

## Ratings that explain the judgment

Choose applicable criteria before scoring. Start with clarity, soundness, feasibility, simplicity, risk handling, and supporting evidence. Omit irrelevant criteria and add domain-specific ones only when they change the assessment. Explain departures briefly. Compare alternatives using the same criteria and scale; disclose differences in evidence availability.

Use integer scores from 0 to 10. Scores are reasoned judgments within the reviewed scope, not probabilities or certifications.

| Range | Meaning |
|---|---|
| 9-10 | Strong for the stated purpose, with no material unresolved weakness in the assessed criterion. |
| 7-8 | Sound, with specific improvements still worthwhile. |
| 5-6 | Material weaknesses require correction. |
| 3-4 | Major changes or validation are needed. |
| 0-2 | Fundamental problems prevent the stated goal. |

For each criterion include its score, reason, evidence or explicit uncertainty, and the change that would improve it. Mark insufficiently supported judgments `Unrated`; mark genuinely irrelevant criteria `N/A`. A missing optional artifact is not automatically a defect. Judge evidence against what this stage and claim actually require.

Default overall score: arithmetic mean of rated applicable criteria, rounded to one decimal. Show the calculation and identify exclusions. If the user supplies priorities or weights, use them and disclose the formula. If an unresolved essential criterion could change the verdict, withhold the overall score rather than presenting a misleading partial average. Keep supported category scores.

State confidence separately as high, medium, or low, with the evidence limitation that explains it. Rate major parts individually when the subject contains meaningful independent parts and that breakdown helps the decision. Do not combine overlapping part and category scores into a second average. A substantiated blocker controls the verdict regardless of the numeric average.

## Full report

With no mode specified, produce a detailed report containing:

1. **Verdict and overall rating:** A direct conclusion, confidence, reviewed scope, and essential evidence limits. Choose proceed, proceed with constraints, revise before proceeding, validate first, or insufficient evidence.
2. **Strongest version and strengths:** What the subject is trying to achieve and what should be preserved.
3. **Scorecard:** Applicable criteria, reasons, improvements, and the overall calculation. Include useful ratings of major parts when relevant.
4. **Ranked critique:** For each material finding give severity, evidence, consequence or failure scenario, and the smallest sound improvement. Label blockers, major issues, and minor issues consistently with their actual impact.
5. **Assumptions and self-challenge:** Identify fragile assumptions and explain which serious objections survived counter-evidence. Merge this into findings when a separate section would repeat them.
6. **Alternatives and tradeoffs:** Include viable alternatives when they could change the decision. Do not invent alternatives merely to fill a section.
7. **Prioritized next steps:** Separate essential fixes, worthwhile improvements, and optional polish. State how to verify improvement and identify unanswered questions that could change the verdict.

Cover all applicable elements without padding or repeating findings. Put unavailable evidence and inapplicable elements in a concise limits note rather than inventing content. Full mode completes the assessment with supported assumptions; reserve a sequential interview for `question` mode.

After a completed assessment, give the saved report path or the reason saving was unavailable. Briefly mention that the default was full when applicable and that `help` lists optional modes and combinations. Do not interrupt the assessment with a menu.

Limits: Generic critique and recommendations. No fixed framework, industry, scoring outcome, external service, or specialist skill is required. Distinguish review judgments from independently verified outcomes.
