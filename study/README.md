# Study start

## Take a diagnostic before committing to a track

1. **Finance first.** Set aside 65 minutes. Prepare a blank sheet, take [FIN-A](diagnostics/finance.md) in 55 minutes, and mark uncertainties. Review and score it separately. Build the [finance lab](../examples/finance-forecast/) after repairing the biggest gap.
2. **Compare the technical lane.** Take [TECH-A](diagnostics/technical.md) in 55 minutes and score coding and operations separately. Use the [release lab](../examples/technical-release/) to verify a real fail/pass workflow.
3. **Generalist fallback.** Try [GEN-A](diagnostics/generalist.md) in 20 minutes if that is the viable entry. Use GEN-B as the fresh alternate.
4. **Score and retest.** Open the [evaluator key](evaluator/diagnostic-key.md) after finishing. Log your result in a local copy of the [score template](score-log-template.csv). Require 80/100, zero critical errors and a clean fresh retest. For technical, also require at least 36/50 in each half. These are practice standards. Patrick's actual scores remain open.

The finance and technical lanes each have A, B and C forms. Use unopened forms in order. Keep the key closed during attempts. Use the [workbook](workbook.md) for the underlying skill and the [skill index](skill-index.csv) to find a drill by time, difficulty or trap. [Workbook answer key](answer-key.md) · [Assessment-day toolkit](toolkit/assessment-day.md) · [Apply-first decision](../docs/roles/application-decision-2026-11-07.md)

| Time available | Work block |
| --- | --- |
| 20 minutes | Do one original Generalist form or one small drill from a weak category. Mark one check that would have caught your error. |
| One hour | Take FIN-A or TECH-A and set the key aside until you finish. Reserve a separate block for review. |
| Weekend | Take both A forms in separate sessions, review the biggest failure in each, complete one applied lab for the likely track, and reserve the B form for a fresh retest. |

## Free study material with a verification task

| Resource | Skill and suggested time | Practice and verification |
| --- | --- | --- |
| [MIT Finance Theory I](https://ocw.mit.edu/courses/15-401-finance-theory-i-fall-2008/) | Discounting and valuation · 45 min | Review time value and discounted cash flow. Redo F03, then confirm terminal and present values with an independent calculation. |
| [Surge DAYJOB Finance](https://huggingface.co/datasets/surgeai/DAYJOB-finance) and [GDPval](https://openai.com/index/gdpval/) | Representative work products and rubric design · 30 min | Inspect how a public example defines the deliverable. Complete the original finance lab and cite the exact source rows that reverse the draft conclusion. |
| [Python unittest](https://docs.python.org/3/library/unittest.html) and [PostgreSQL transaction isolation](https://www.postgresql.org/docs/current/transaction-iso.html) | Reproducible regression tests and concurrency · 45 min | Redo C16 and run the release tests. Identify the failure that demonstrates the contract breach and the test that verifies the repair. |
| [Google SRE books](https://sre.google/books/) | Release safety and incident reasoning · 35 min | Read a relevant release engineering or incident section. Produce a hold/rollback decision for MD1 and name a threshold and smoke test. |
| [SWE-bench](https://www.swebench.com/) | Patch-level evaluation · 20 min | Review how an engineering task can be judged with tests. For MC23 or the release lab, write a minimal failing reproduction and a regression test. |
| [DataAnnotation Generalist posting](https://www.dataannotation.tech/job-board/generalist) | Evidence-based comparisons and rewrites · 20 min | Complete G14 and GEN-A. Verify every corrected fact against a source ID. |

The public resources are linked for preparatory study. Exercises and lab records here are original. An applicant can do the diagnostics with no paid tools or cloud setup.
