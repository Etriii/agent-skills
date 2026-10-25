---
name: ultimate-qa-architecture
description: Assess code architecture, ownership, coupling, maintainability, and change risk during a QA review. Use for clean architecture or code quality analysis.
---

# Ultimate QA Architecture

Read `references/checks.md` for the review dimensions and evidence scale. Inspect the project architecture, then trace representative user journeys from UI/API through domain logic to persistence. Use project-native tests, static analysis, import graphs, and churn/history where available. Report concrete path:line examples and the effect on a real change or defect.

Distinguish confirmed defects from maintainability risks. A large file alone is not proof of poor architecture. Score each dimension 0–3 only when the evidence supports it; leave unassessed dimensions blank. Give a short repair sequence ordered by risk and dependency, and link architecture findings to functional findings when the same root cause appears. Avoid prescribing a framework or layer pattern where simpler ownership fits.
