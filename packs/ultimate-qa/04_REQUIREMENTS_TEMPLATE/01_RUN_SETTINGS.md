# 01 – Run settings

Read by the agent at the start of every run. Paths below mean folders inside the current QA version, `qa-findings/v<N>/`. An instruction typed in chat beats a value here. Leave the defaults unless you have a reason to change them.

**By default the agent performs QA only:** audit, then write the improvement plan. Use `$ultimate-qa run` for initialization through planning, or `$ultimate-qa run --client` to also prepare client documents. `$ultimate-qa-client prepare` packages an existing review. In Claude Code, replace the `$` prefix with `/`. Implementation requires a separate instruction.

```
MODE: auto              # auto | audit | plan | implement | full
                        #   auto  = audit and plan as needed, then stop
                        #   audit = Phase 1a: map the project + check the checklist -> writes 01, 02, 03 in recommendations/,
                        #           plus 06 (design gaps) and 07 (destructive tests) when those are enabled
                        #   plan  = merge findings + ideas into a backlog → writes 04 only
                        #   implement = explicitly authorized development; records changes and evidence
                        #   full  = audit → plan only; never implies implementation

SCOPE: all              # all | section numbers from the checklist, e.g. 7,8  or  1,2,6,7,8,10

QA_VERSION: auto        # auto = use qa-findings/state.json's current version (v1 on a fresh project)
                        # v2, v3 ... = work in that version; "new" = open the next one
                        #   opening a version always asks for the progress source first (see 06_PROGRESS_SOURCES.md)

INTAKE: auto            # auto = ask the five intake questions on the first run in a project, then never again
                        # skip = do not ask; use these settings and the agent's own judgement, recorded in 04_CONDITIONS.md

REQUIREMENTS_PATH:      # path to a spec / SRS / user stories / client brief the app must be checked against
PLANS_PATH:             # path to an implementation plan, roadmap or backlog you already wrote
PROGRESS_PATH:          # path to the record of what is already built or fixed (also in 06_PROGRESS_SOURCES.md)
                        # leave blank and the agent asks at intake, or works it out from the code and the change log

GAP_HUNT: yes           # yes = also hunt for design gaps the team never considered -> 06_System_Gaps_Report
                        # no  = checklist findings only

DESTRUCTIVE_TESTING: no # no (default) | yes | staging-only
                        #   deliberately trying to break the app: abuse input, overload, kill dependencies,
                        #   interrupt writes, corrupt state -> 07_Destructive_Test_Report
                        #   never runs against production; needs DESTRUCTIVE_TARGET below

DESTRUCTIVE_TARGET:     # the exact environment destructive tests may touch, e.g. "local docker stack"
                        # or "staging.example.com (test data only)". Blank = destructive testing does not run

PHASE_SOURCE:           # path to the project's own phase / sprint / milestone document, if it has one
                        # e.g. docs/ROADMAP.md ; set PHASE_MODE and see 05_PHASE_MAP.md
PHASE_MODE: mapped      # mapped = their names, the kit's protect-first ordering underneath
                        # transformed = their structure wins completely

APPROVED_IDS:           # optional implementation scope: must | comma-separated plan refs / findings / ideas
                        #   e.g. P-01, P-02, IDEA-002      (plan refs P-nn come from 04_Improvement_Plan)
                        #   a returned client/decisions/ checklist limits client-approved scope;
                        #   a separate implementation instruction is always required

PROJECT_TYPE: auto      # auto | website | web-app | api | mobile-backend
                        #   (website → Section 12 SEO applies; api → Sections 3, 4, 12 mostly N/A)

CLIENT_LANGUAGE: English
                        # language for all documents (e.g. English, Filipino, Taglish, Spanish)

REVIEWER_NAME:          # printed on the cover of each document, e.g. "Juan Dela Cruz, QA lead"
                        # blank → "QA review"

OUTPUT_FORMAT: docx     # docx = Word file + the .md it was built from (default) | md = markdown only

CAN_RUN_APP: auto       # auto | yes | no
                        #   yes/auto = the agent may start the app locally (dev build, test data) and use it
                        #   no       = code review and commands only; runtime checks become NEEDS-MANUAL

BROWSER_TOOL: auto      # auto | yes | no
                        #   auto/yes = if the agent has a browser it can drive (Claude in Chrome, Playwright MCP server),
                        #              use it for the checks in 11_BROWSER_ASSISTED_CHECKS.md and save screenshots to evidence/
                        #   no       = never open a browser; those checks are marked NEEDS-MANUAL with steps

BROWSER_TARGET:         # the only address the browser may be pointed at, e.g. http://localhost:8000
                        # or https://staging.example.com (test accounts only) – never production.
                        # Blank = the local dev URL from 02_PROJECT_CONTEXT.md, else the staging URL there

ASK_BEFORE: adding dependencies, database migrations, deleting anything, changing public API shapes, touching payment code
                        # things the agent must ask about before doing them in implement mode
```

## Notes for this run (optional)

Anything you want the reviewer to know just for this run – for example "staging is down this week, use local", "ignore the /legacy folder", "the client cares most about the checkout".

-
