---
name: ultimate-qa-performance
description: Measure application latency, throughput, resource use, and slow data paths in a controlled QA environment.
---

# Ultimate QA Performance

Confirm a disposable test stack, representative seeded data, workload, and baseline before measuring. Use the project's existing benchmark or load tool when possible, preferably inside Docker. Warm the app consistently, measure multiple runs, and record latency distributions, error rate, throughput, CPU/memory, DB query count, and environment limits. Wait until the load run and service metrics collection finish before interpreting results.

Compare the same scenario and data volume across versions. Investigate slow paths with traces, query plans, and profiles before proposing a fix. Keep overload tests behind the kit's destructive-testing gate; avoid production and shared third-party services. A single slow response or a saturated laptop is a lead, not proof of a product regression. State confidence and reproducibility with each finding.
