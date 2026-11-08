# DataAnnotation Workbench

A private research and practice workspace for understanding DataAnnotation.tech, choosing a contributor track, and studying how expert work becomes training data or evaluation evidence.

## Start here

| If you want to | Open |
| --- | --- |
| Choose what to apply for and what to study first | [Apply-first decision](docs/roles/application-decision-2026-11-07.md) · [Study start](study/) |
| Rehearse the assessment setup and allowed-tool checks | [Assessment-day toolkit](study/toolkit/assessment-day.md) |
| Compare time to paid work and cleared cash | [Earnings model](docs/research/earnings-model.md) · [First paid week](docs/research/first-paid-week.md) |
| Understand the company, selection process and day-to-day work | [Contributor and pipeline findings](docs/research/contributor-and-pipeline-findings.md) |
| Compare all 133 roles and 14 families in the captured snapshot | [Role register](docs/roles/role-register.md) · [Spreadsheet](data/roles/company-and-role-dataset.xlsx) · [Machine-readable role data](data/roles/role_register.jsonl) |
| Decide which track fits your experience | [Role fit and assessment preparation](docs/roles/role-fit-and-assessment-prep.md) |
| Take an original practice assessment | [Practice workbook](study/workbook.md) |
| Grade a completed practice run | [Separate answer key](study/answer-key.md) |
| See how reference answers and rubrics become an executable evaluation | [Boatable synthetic example](examples/boatable/) |
| See the next research and study build | [Earnings and specialist readiness work order](docs/work-orders/earnings-and-specialist-readiness.md) |
| Audit a claim or revisit the research design | [Source ledger](docs/research/source-ledger.md) · [Work orders](docs/work-orders/) |

The study pack has **76 standalone drills, eight timed mocks, and 24 recall cards**. The mocks contain another 24 scored tasks. Generalist, Coding, DevOps and Finance/FP&A each have two mocks. Six additional drills sample Data Science and ML evaluation. The next work order added eight fresh diagnostic forms and two applied labs. Open the answer key after attempting the exercise.

## Repository structure

- `docs/research/` covers Surge Labs and DataAnnotation, onboarding, project work, downstream training and evaluation, and the evidence behind the findings.
- `docs/roles/` documents role requirements and application fit. `data/roles/` contains a dated machine-readable snapshot, its summary and the spreadsheet.
- `study/` keeps learner-facing questions separate from solutions and scoring rubrics.
- `examples/boatable/` includes twelve original fictional service-desk cases, clean held-out inputs, evaluator-only records, and a deterministic Python scorer.
- `docs/work-orders/` preserves the scope and completion criteria for completed and planned research passes.
- `examples/finance-forecast/` and `examples/technical-release/` supply original work samples.
- `scripts/verify.py` checks the cross-file counts, exercise IDs and score totals, runs the practice Python examples, and regenerates the scorer outputs for byte comparison.

## Verify locally

From the repository root, run this with Python 3.8 or later. No external packages or credentials are needed.

```sh
python3 scripts/verify.py
```

For a standalone scoring run:

```sh
python3 examples/boatable/build_and_score.py --out /tmp/boatable-score-check
```

The checked-in score report measures 12 reference answers and 12 planted errors. It contains no model performance results. For a model evaluation, give the model only the held-out inputs. Keep the evaluator answers and code in a separate scoring process.

## Maintain the evidence

The initial role and company research is a **November 7, 2026 snapshot**. Public listing maxima and signup links are not individual offers. Keep a source URL and checked date with changes, mark first-party claims separately from contributor accounts, and record unknown account-specific details as unknown. Update the role rows and summary together. Preserve the original workbook as a dated reference if a later snapshot changes.

Keep live assessment questions, candidate answers, real customer records and credentials outside this repository. The practice material and synthetic examples are original. The research files link to public examples and describe their provenance and limits.
