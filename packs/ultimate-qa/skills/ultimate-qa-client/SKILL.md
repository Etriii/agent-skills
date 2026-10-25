---
name: ultimate-qa-client
description: Optionally turn completed QA recommendations into client documents and track client decisions. Use only when client-facing output is requested.
---

# Ultimate QA Client

This skill runs only when invoked directly or by `ultimate-qa run --client` after the QA plan is complete. Use `$ultimate-qa-client prepare` in Codex or `/ultimate-qa-client prepare` in Claude Code. Locate the Ultimate QA kit through `ULTIMATE_QA_KIT`, an adjacent `qa-template/`, or `kit-location.txt` in this skill folder (fall back to the core skill's marker for older installations); ask for its path only if needed. Read `12_CLIENT_PACK/README.md`, `03_OUTPUT_TEMPLATES.md`, and `06_INTAKE_AND_CONDITIONS.md` for the current task. Use the same verified application Git root and QA version as the core workflow. QA audit and plan never depend on this skill.

- `prepare`: Read the current `qa-findings/v<N>/recommendations/md/03_QA_Audit_Report.md` and `04_Improvement_Plan.md`, plus available gaps and evidence. If the audit or plan is missing, identify the missing QA step and stop; never invent findings. Create only `qa-findings/v<N>/client/` with `md/`, `docs/`, and `decisions/`. Use the client templates to write a plain-language QA report and approval checklist, retaining the QA version and stable finding and plan IDs. Fill only proposal columns; leave client decision, reason, and recommendation fields blank. Generate matching Word files with `tools/md_to_docx.py` and visually inspect them before delivery. Do not change the source recommendations or start implementation. On a rerun, archive generated files before replacing them and carry returned decisions verbatim.
- `intake`: Read a returned client form and ask only unanswered questions about goals, requirements, user roles, existing plan, existing progress, test accounts, environment, and approval authority. Record decisions in the project's internal requirements and conditions; keep credentials out of files.
- `decisions`: Read returned approvals from `client/decisions/` or a direct client reply. Preserve each choice, rejection or deferral reason, and alternative recommendation verbatim. Mark missing decisions pending; never infer consent from silence.
- `report`: After separately authorized implementation, write the plain-language client summary and change log in `client/after_implementation/md/` and `client/after_implementation/docs/`, using actual changes and test evidence. Never report a proposed fix as completed.
- `next-version`: Carry unresolved client decisions and accepted unfinished work with their original IDs. Show closed work in the historical summary, not as new action items. Revisit a rejected item only with changed evidence and an explicit explanation.

Client-facing files must not expose internal paths, secrets, run settings, or test credentials. Report scope and evidence limits plainly. A client approval authorizes only the recorded item; code implementation, data migration, deployment, and external messages follow the user's actual instructions and local policy.
