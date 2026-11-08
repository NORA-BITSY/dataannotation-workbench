# Work order 03 · Earnings and specialist readiness

**Owner** Product Pat  
**Prepared** November 7, 2026  
**Status** Executed · readiness and account choices await Patrick  
**Repository** [NORA-BITSY/dataannotation-workbench](https://github.com/NORA-BITSY/dataannotation-workbench)  
**Starting commit** `5544eee024dc959a6001e6790e36c56374786a81`

## Execution results

[Apply-first decision](../roles/application-decision-2026-11-07.md) · [Source and route recheck](../research/route-and-pay-recheck-2026-11-07.md) · [Earnings model](../research/earnings-model.md) · [Diagnostics and labs](../../study/README.md) · [Assessment-day toolkit](../../study/toolkit/assessment-day.md)

The board comparison matched 133 roles and the 11 selected Apply routes. Eight original diagnostic forms, two work-sample labs, an offline practice timer and 14/30-day earnings scenarios were added. The live account choices required sign-in, so the routing recommendation is conditional. Unaided scores and actual assignment economics await Patrick's observations.

## Decision this work order must produce

Choose the highest-paying track Patrick can credibly pursue now, the next track worth preparing for, and the exact evidence that should change that order. Produce a study system that measures independent readiness, catches material mistakes, and adapts to the work Patrick actually sees after qualification.

The previous passes already mapped 133 roles, traced how contributor work is used, and built 76 drills, eight timed mocks, 24 recall cards, and a synthetic scorer. Begin from those assets. This pass prioritizes **route selection, ability demonstrated unaided, and income that can actually be earned**. Maintain the role inventory while concentrating new work on the shortlist. [Contributor findings](../research/contributor-and-pipeline-findings.md) · [Role fit](../roles/role-fit-and-assessment-prep.md) · [Practice workbook](../../study/workbook.md) · [Existing verifier](../../scripts/verify.py)

| Track | Starting hypothesis | Evidence that changes the recommendation |
| --- | --- | --- |
| FP&A Analyst | Best near-term specialist fit if Patrick can independently build and reconcile a driver forecast and explain management reporting work he owned. | Put Finance Expert or the technical lane first if its displayed entry route, experience evidence and unaided results are stronger. |
| Finance Expert | Strong finance-adjacent option. The corporate finance degree and prior work support the profile, while modeling fluency and role-specific experience still need direct evidence. | Move ahead of FP&A if Patrick can defend the linked statements, DCF and assumptions unaided and map actual work to the stated experience requirement. |
| DevOps with coding preflight | Highest advertised tier among the strongest practical leads. Test the shared technical fundamentals and the ability to review a deployment, diagnose failure and demonstrate rollback. | Put it first if the relevant entry appears, the coding and DevOps gates clear, and Patrick can substantiate hands-on contributions. |
| Backend and Software Engineering | Adjacent technical opportunities if the same preparation transfers and Patrick can show a shipped service, fix or substantial contribution. | Promote only after an unaided code review or patch exercise and concrete evidence of personally performed work. |
| Data Scientist and ML Engineer | Secondary high-rate route. Check whether independently reproducible modeling or evaluation work satisfies the listing before allocating substantial prep time. | Promote if a complete independent project and fresh diagnostic meet the actual role requirements. |
| Generalist | Faster fallback if it is the available entry and Patrick clears the independent readiness checks. | Compare the implications of starting it against waiting for an available specialist route. The public FAQ does not resolve the consequences of track choice in Patrick's account. |

The official FP&A and DevOps pages were checked while scoping this work order. They list different hands-on experience requirements and advertised top ends of $125+ and $150+, respectively. The FAQ describes qualification tracks and says project availability depends on demand and past performance. It does not establish Patrick's admission, hours or assignment rate. [FP&A posting](https://www.dataannotation.tech/job-board/fpa-analyst) · [DevOps posting](https://www.dataannotation.tech/job-board/devops-engineer) · [FAQ](https://www.dataannotation.tech/faqs)

## 1. Verify routes, requirements and evidence

1. Inspect the current default-branch head, role snapshot, source ledger, previous work orders and verifier. Run the verifier and record its baseline. Reuse the established directories and avoid duplicating the workbook.
2. Reconcile the public board against the 133-role snapshot at the level needed to spot additions, withdrawals and material changes. Deep-check FP&A, Finance Expert, DevOps, Backend, Software Engineer, Data Scientist, ML Engineer and Generalist. Add Treasury, Credit or Accounting to the comparison only where role-specific evidence suggests an advantage. Capture posting status, advertised pay label, geography, experience and credentials, stated work, official Apply URL and date. Never promote a public route parameter into a confirmed assessment assignment.
3. Separate **the role listing**, **the signup route**, **the Starter track**, **a later qualification**, **project access**, and **paid work**. Verify each transition from the source that actually supports it. For conflicts between a general FAQ and a role page, retain both and identify the unresolved application question. Document exact retake and tool rules only where directly supported.
4. Establish which options Patrick's existing account actually displays, if it can be inspected without starting an assessment or changing state. A user-provided redacted list of track labels is enough. Record unavailable evidence as unknown and prepare a conditional first-track decision. Avoid duplicate accounts, profile changes, taking a test or accepting a contract in this work order.
5. Map each shortlisted role to evidence of Patrick's experience, with columns for task, personal contribution, independently verifiable result, credentials where relevant, unresolved gap and next proof. Start with corporate finance education, cash-flow analysis, management reporting and reconciliation. For technical work, start with GCP, Docker, APIs and database work that Patrick can explain and verify. Distinguish former registrations, prior roles and verified current credentials. Distinguish AI-assisted project delivery from independent assessment ability. Use sanitized descriptions and links to existing authorized evidence.
6. Compare official terms with recent dated independent reporting and public first-person accounts where useful. Capture the role or track, date, whether the number is an actual assignment or a stated ceiling, whether an hour was paid, and what the source can support. Try to corroborate any material pattern with independent accounts and record discrepancies. Leave queue frequency, typical rates, approval odds and time to first payment unknown when evidence is weak. Exclude leaked assessment questions, unauthorized screenshots and unverifiable claims of insider access.

**Deliverables**  
A shortlist and route matrix under `docs/roles/`, plus a dated change log under `docs/research/`. Update the role dataset or add a compact date-stamped delta when material changes are found. Preserve the original snapshot. Add a prioritized source ledger with one row per material claim and an evidence label of **official policy**, **official listing**, **independent reporting**, **contributor account**, **user-observed**, **scenario**, or **unknown**.

## 2. Model the path to paid hours

Build a dependency-free scenario sheet or local calculator and a short interpretation. Evaluate the next 14 and 30 days, with an optional 90-day comparison when useful. Compare starting a credible lower-variance track now, spending additional time to prepare for a higher tier, and using a staged plan contingent on the route actually offered.

- Track the time from preparation to assessment, approval, first available task, first completed paid hour and first cleared payment. These are distinct states. Show a **zero-work case** and one or more explicitly hypothetical task-rate and hours cases. Never populate unknown probabilities or hours with listing marketing figures.
- Capture study, onboarding, time checking the queue, qualifying and working. Tag preparation as paid only when the actual project terms establish it. Separate paid task hours from time spent preparing, looking for work or fixing work without pay. Keep projected earnings, approved earnings and cash received in separate fields. Record direct expenses and leave tax treatment out of the default model.
- Calculate gross earnings as the sum of **paid hours × actual or assumed task rate** by category. Calculate effective pre-tax return as **(gross earnings − direct costs) ÷ total time invested**. Show zero earnings with real prep time and label a zero time denominator undefined. For a same-hours comparison, divide the explicit cost of additional preparation or displaced earnings by the incremental dollars per paid hour. If schedules or availability differ, compare cumulative scenario returns instead. Do not value the same study hours twice.
- Show a decision sensitivity, such as how much additional study or queue delay would erase the higher-rate advantage. Where task supply is unknown, compare scenarios and rank robustness rather than reporting a predicted income. Once Patrick has work, replace assumptions with logged observations. Track the rolling realized rate and paid share of total time. Use short, intentional queue checks.
- Build a seven-day and fourteen-day action sequence with stop points. Use one short diagnostic block for the finance lane and one for the technical lane before recommending a longer study commitment. Use Generalist when it is the viable entry and its access implications are understood. If no track is available after preparation, switch effort to transferable skills or portfolio work while waiting. Do not allocate money to courses, cloud resources or services without separate approval.

**Deliverables**  
An assumptions file, example scenario output, tests for zero-work and zero-time cases, and an empty personal earnings tracker template. Include a brief decision memo giving the primary route, fallback, what Patrick must verify himself, and the trigger for changing course. Keep actual applicant and earnings records local to Patrick unless he explicitly asks to commit them.

## 3. Build an evidence-based study map

Review the existing exercises and map each to a concrete skill, difficulty, time, known trap and role. Compare against public job descriptions and reputable learning materials. Identify gaps in practicing a complete deliverable, finding subtle errors, and explaining evidence under time pressure. Add original exercises only where they address a measured gap, create a fresh equivalent for retesting, or reproduce a representative type of paid work.

| Lane | Highest-value competencies | Representative work product to build |
| --- | --- | --- |
| FP&A and Finance | Reconcile conflicting records, linked statements and cash timing, driver forecasts, sensitivities, pricing and mix, DCF, and clear management commentary. | Original fictional financial packet, blank spreadsheet or CSV inputs, clean model and answer commentary, plus a model with seeded errors to audit. |
| Coding and Backend | Parse requirements, work within a codebase, Python or JavaScript fundamentals, SQL data grain, retries and concurrency, unit tests, reproducible defect evidence, and concise patch review. | Small local service or repository task with a bug, relevant tests, and an evaluator-only reference patch. |
| DevOps | Reproducible artifacts, deployment and rollback, schema compatibility, CI/CD and infrastructure changes, queue recovery, observability, and permissions. | A local release or incident lab with synthetic logs, a known-good version, a broken change and a rollback or hold decision. Use fixtures where running infrastructure adds no value. |
| Generalist | Evidence hierarchy, fact-checking, structured outputs, competing good answers, material error versus stylistic preference, and explanation quality. | Short source-packet comparisons and rewrites with exact instructions, scope and source citations. |
| Data and ML | Leakage, split design, metric interpretation, failure slicing and reproducibility. | A small frozen-baseline evaluation with grouped holdout and a documented failure taxonomy, only if the diagnostic justifies the extra lane. |

Use official technical references for current tooling and free authoritative coursework for fundamentals. Inspect public benchmarks for representative task structure and rubric design. Record reuse rights for any imported material and prefer original examples that exercise the same skills. These resources inform practice design. They do not reveal DataAnnotation's actual assessment content. [DAYJOB Finance](https://huggingface.co/datasets/surgeai/DAYJOB-finance) · [GDPval](https://openai.com/index/gdpval/) · [SWE-bench](https://www.swebench.com/) · [MIT Finance Theory](https://ocw.mit.edu/courses/15-401-finance-theory-i-fall-2008/) · [Google SRE books](https://sre.google/books/)

**Deliverables**  
A skill-to-exercise index and an ordered prep roadmap with study blocks for 20 minutes, one hour and a weekend. For each study resource, state the target skill, estimated time, a hands-on exercise, and how to verify proficiency. Put the most useful paths in `study/README.md` or the existing workbook index.

## 4. Produce diagnostics, two applied labs and fresh retests

1. Produce one cold **Finance/FP&A diagnostic** and one cold **technical diagnostic** with a coding preflight and a DevOps review. Target 45–60 minutes per diagnostic. Reuse existing mocks as baseline options if Patrick has yet to see them. Provide two fresh equivalent variants per diagnostic, testing the same skills with different facts, failure modes and expected outputs.
2. Build two self-contained applied labs, one finance and one technical, that can run locally or be completed from source packets. For each, include a user prompt, evidence packet, constraints, expected output shape, one deliberate critical trap, evaluator-only answers and a worked review. The technical lab includes a failing-before and passing-after test or a reproducible simulated incident. The finance lab includes at least two independent tie-outs and documented rounding. Add a brief Generalist readiness check with a fresh alternate.
3. Score only observable criteria. Give each assessment a 100-point rubric with partial credit, an explicit critical-error list and an independent retest requirement. Use a practice benchmark of **80/100 or higher, zero critical errors, and a clean fresh retest**. Tighten it where a critical skill is underrepresented. A passing practice score is a recommendation input rather than an official threshold or selection guarantee.
4. Keep the prompt and required records in learner-facing files. Keep worked answers, reference patches and scoring fixtures in separate paths. Label tasks, expected duration, track, version, allowed practice tools and what constitutes a completed response. Ask Patrick to do readiness attempts without AI or answer access. Feedback and instruction can follow each completed practice run.
5. Provide two paths for grading. The practice answer key supports self-scoring. A reviewer can also score completed practice responses with the same rubric and return a breakdown, error log, targeted exercises and a fresh retest. Use deterministic checks where appropriate and leave subjective scoring explicit. The Boatable scorer demonstrates the architecture and remains scoped to its own cases.

**Deliverables**  
Diagnostic packets, alternate forms, two labs, evaluator-only materials, a score log template and a one-page readiness checklist. If Patrick has yet to take the diagnostics, publish a provisional decision with clear branching and an exact next session. Record no fabricated scores or eligibility outcomes.

## 5. Keep the workbench useful after qualification

Add a one-page work-session checklist based on documented platform behavior and transferable quality habits. Cover reading project-specific instructions, checking the current rate and pay basis, verifying a submission before sending it, logging eligible time according to project rules, and recording outcomes when feedback is visible. Add a short first-week review using aggregate time, rates and task categories. Keep assessment questions, confidential project instructions, outputs, customer information and credentials outside Git. Use only original or permitted public material in shared notes. Apply the live assessment's tool rules, including any restriction on AI assistance.

## Publish and verify

- Work in the existing private repository. Extend `docs/roles/`, `docs/research/`, `study/`, `data/`, `examples/` and `scripts/` as warranted. Preserve existing material and repository history. Add a README entry for the recommended path, source dates, diagnostics and how to run any lab.
- Extend `scripts/verify.py` only for newly introduced reproducibility checks. Verify unique exercise IDs, answer-key coverage, rubric totals, fixture math, fail/pass controls, scenario calculator tests, runnable code and local links. Confirm cold forms can be used without accidentally opening the answer key. Check that public links support the claims and that all new tracked data is permitted.
- Publish the verified changes and confirm the target is still private. Record the commit and link to the revised start page. Keep study and application decisions human-controlled. Any live application or assessment is a separate step for Patrick.

## Completion criteria

1. A dated comparison ranks the primary, secondary and fallback paths using verified role requirements, Patrick's evidenced experience, study time, route uncertainty and effective earnings scenarios.
2. The workbench offers a concrete first session, fresh diagnostic variants, two verified work-sample labs and a scoring-to-retest workflow. Existing materials remain easy to find.
3. The earnings tool separates advertised caps, assumptions, observed work, effective return and cash received. Unknown queue access and zero-work outcomes are visible.
4. Any public posting or source change has traceable provenance. Role title, assessment access, task access and actual compensation stay distinct throughout.
5. The repository verifier passes and the committed result is reviewable in the private repository. Any account-specific decision still awaiting Patrick's input is listed with the exact evidence needed.
