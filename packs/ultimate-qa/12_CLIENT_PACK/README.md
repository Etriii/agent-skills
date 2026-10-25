# 12 – Client pack: what to send someone who wants their system reviewed

Four optional client-facing Markdown sources live in `md/`; generate Word copies in `docs/` when needed. They explain the review in the client's language, collect intake information, and help the client read the result. Core QA does not create or require these files. Nothing in them mentions the template, the `requirements/` folder, the run settings or the agent – keep it that way when you edit them.

| # | File (in `docs/`) | What it is | When to send it |
|---|---|---|---|
| 01 | `01_About_The_QA_Review.docx` | What a QA review is, the sixteen areas in plain words, every document they will receive, how the work runs, what we never do, and the questions clients ask | First contact – with your quote or proposal |
| 02 | `02_What_We_Need_From_You.docx` | The intake form: contacts, the system, what matters most, access, one test account per role, documents, connected services, what we may and may not do, practical details | When they say yes. It must come back before you start |
| 03 | `03_How_To_Read_Your_QA_Report.docx` | Reading order, what the statuses and severities mean, the reference numbers, how to fill in the approval checklist, a short glossary | With the finished Phase 1 documents |
| 04 | `04_Terms_Of_The_Review.docx` | The engagement terms: scope, access and confidentiality, ownership of the documents, decisions, fees, timeline, limits, signature block | With your quote, or when they say yes – signed before you start. Fill in the angle-bracket blanks; have the wording checked against your local law before you rely on it |

## What to send, step by step

1. **First contact.** Send `01_About_The_QA_Review.docx` with your quote or proposal. Describe the expected audit, gap report, and approval checklist without sending invented project examples.
2. **When they agree.** Send `04_Terms_Of_The_Review.docx` with the blanks filled in (fees, dates, the system's name) for signature, and `02_What_We_Need_From_You.docx`. Point at section 5 (test accounts) and say plainly how you want passwords handed over – never by email.
3. **When the form comes back.** Keep it with the project, for example in `docs/qa/` or straight into `qa-findings/requirements/07_client_pack_returned.docx` if the folder already exists. Then run the review as usual and mention the path in the prompt:

   ```
   Read <template folder>/README.md and follow it for this project. The client's returned form is at docs/qa/client_pack.docx.
   ```

   The agent reads the form first, takes the intake answers from it, fills in `requirements/02_PROJECT_CONTEXT.md` and the permission settings, and asks only about what the client left blank.
4. **Preparing the client report.** After QA audit and plan are complete, run `$ultimate-qa-client prepare`. It reads `qa-findings/v<N>/recommendations/` and writes a plain-language QA report and approval checklist to `qa-findings/v<N>/client/md/` and `docs/`. Send those client files and `03_How_To_Read_Your_QA_Report.docx`. Put returned decisions in `client/decisions/` and preserve their wording.
5. **After separately authorized implementation.** Run `$ultimate-qa-client report` to write `client/after_implementation/` from actual change and test evidence. Send its summary and change log for re-test and sign-off.

## Before sending: personalise the cover

The first lines of each `.md` are the cover block: `project`, `date` and `reviewer` are placeholders in angle brackets. If the four introductory client documents are needed, copy their Markdown sources into the project's current `qa-findings/v<N>/client/intro/md/`, fill in the cover, then generate Word files there:

```
python tools/md_to_docx.py --all <project>/qa-findings/v1/client/intro/md --outdir <project>/qa-findings/v1/client/intro/docs
```

Or ask the agent, from any folder outside the template:

```
Read <template folder>/12_CLIENT_PACK/README.md and prepare the client pack for <client name>, reviewer <your name>, into <a folder you name>.
```

It writes personalised copies (markdown and Word) into the folder you name. It never writes into the template folder.

## Where the client's answers go

For you and for the agent: each section of the returned form lands in one place inside `qa-findings/requirements/`.

| Form section | Lands in |
|---|---|
| 1. Who to talk to | `02_PROJECT_CONTEXT.md` §1 (client / company) – decision maker's name goes on the approval checklist sign-off line |
| 2. About the system | `02_PROJECT_CONTEXT.md` §1 Basics (name, what it does, users, URLs, type) |
| 3. What matters most | `02_PROJECT_CONTEXT.md` §4 Core user journeys; complaints and worries into §10 |
| 4. Access | `02_PROJECT_CONTEXT.md` §1 (repository / branch), §5 (how to run it locally), §8 (design references) |
| 5. Test accounts | `02_PROJECT_CONTEXT.md` §3 Roles and test accounts – logins only, never the passwords; a permission matrix becomes `04_permission_matrix.md` |
| 6. Documents | `02_PROJECT_CONTEXT.md` §8a Source documents, and `REQUIREMENTS_PATH` / `PLANS_PATH` / `PROGRESS_PATH` in `01_RUN_SETTINGS.md`; a done-list also goes into `06_PROGRESS_SOURCES.md` |
| 7. Connected services | `02_PROJECT_CONTEXT.md` §6 Integrations |
| 8. What we may and may not do | `01_RUN_SETTINGS.md`: `CAN_RUN_APP`, `DESTRUCTIVE_TESTING` + `DESTRUCTIVE_TARGET`, `SCOPE`; off-limits items into `ASK_BEFORE` and `02_PROJECT_CONTEXT.md` §1 Out of scope |
| 9. Practical details | `01_RUN_SETTINGS.md`: `CLIENT_LANGUAGE`, `REVIEWER_NAME`; `02_PROJECT_CONTEXT.md` §1 (deadline), §8 (browsers and devices), §9 (data-protection laws) |
| 10. Anything else | `02_PROJECT_CONTEXT.md` §10 |

The client never sees `requirements/`. During the optional client workflow, later questions go in the version's `client/questions/` folder.

## Do not send

The template itself, `01_QA_AGENT_PROMPT.md`, `04_REQUIREMENTS_TEMPLATE/`, or any file from a project's `qa-findings/requirements/`.
