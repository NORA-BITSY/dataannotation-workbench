# DataAnnotation execution package

Start with the [findings report](../../docs/research/contributor-and-pipeline-findings.md) for the company, selection map, fourteen family profiles, five work sessions, public case traces, and Product Pat’s role decision. The files here support verification and reuse.

| File | Contents |
| --- | --- |
| [Role register](../../data/roles/role_register.jsonl) | 133 roles with posting and signup URLs, advertised rate, requirements, location, named tool or standard matches, illustrated inputs and outputs, and unknown account-level fields |
| [Role register summary](../../data/roles/role_register_summary.json) | Role counts, rates, public signup campaign values, and reconciliation with the prior snapshot |
| [Source ledger](../../docs/research/source-ledger.md) | Source provenance, evidence strength, and limits |
| `build_and_score.py` | Reproducible generator, record validator and deterministic scorer |
| `synthetic/cases.jsonl` | Canonical case manifest and source bundle |
| `synthetic/demonstrations.jsonl` | Six development-only input and reference pairs |
| `synthetic/preferences.jsonl` | Six development-only input, chosen, rejected and judgment records |
| `synthetic/heldout_inputs.jsonl` | Six model-facing holdout items, with prompts and documents |
| `synthetic/evaluator_only.jsonl` | Private-to-evaluator criteria, references and planted controls |
| `synthetic/responses_evaluator_only.jsonl` | Linked response IDs, response producers and structured outputs |
| `synthetic/reviews_evaluator_only.jsonl` | Linked review IDs, pilot flags, provenance, preference rationale and adjudication state |
| `synthetic/score_report.json` | Run ID, aggregate checks and per-criterion results for every case |

Each role row is keyed by `role_id`, the official posting slug. `posting_status` records public visibility and a resolvable signup link, not proof of individual admission or current paid work. `public_signup_projects_parameter` is read from the public link. An absent parameter and unknown account-level facts are represented by null. Stated duties and prerequisites are human-readable summaries. The tools field captures selected explicit matches and is non-exhaustive. Illustrative inputs, outputs, checks and downstream use are hypotheses informed by the posting. An earlier canonical snapshot is retained separately. [Company and Role Dataset](https://chatgpt.com/library?file_id=libfile_bfdbe860b5b881919502b5b4438a5a6a&account_id=personal)

## Run and audit the scorer

Run this from the Boatable example directory using Python 3.8 or later. The generator uses only the standard library.

```sh
python3 build_and_score.py --out /tmp/boatable-score-check
diff -r synthetic /tmp/boatable-score-check
```

Expected summary is 12 passing reference answers, 12 caught planted errors, four answer regressions and three invalid-record checks. An empty diff confirms the regenerated outputs match. Call `invalid_reason(case)` before scoring any input of uncertain validity. For a valid case, call `evaluate(case, parsed_answer)` and store each returned Boolean with the case, version, run, response producer and evaluator version. A malformed response on a valid task fails format. An invalid input bundle raises an `invalid_record` error and stays out of model-performance denominators.

## Annotator guide

1. Match the case and source versions. Read the brief and policy, then the quote lines, approval states and supplied slot record. Check each source ID and confirm the source bundle supports the assignment. A missing approval record is invalid evidence, while a present approval record marked pending is valid evidence to hold a required item.
2. Extract approved lines with integer cents from the quote. Cite the quote and approval records per line. Reconcile amounts and confirm each approved line appears once.
3. Use the stated decision precedence. An unresolved required line triggers an approval hold. Otherwise an unavailable slot triggers a scheduling hold. Otherwise the quote is ready. Cite the policy, relevant approval and supplied slot evidence.
4. Score format, arithmetic, evidence traceability, authorization, coverage and decision independently. Preserve the first review, record criterion disagreements and cite the deciding evidence in any adjudication. Flag a missing or inconsistent input as `invalid_record`, with a reason. When ranking two valid responses, use `tie` for equivalent quality and `both_bad` where neither satisfies a material requirement. Prefer a winner only with a defensible difference.
5. Export a reference as a demonstration only after verification. For a preference record, preserve the inputs and both responses, with the rationale stored for audit. Keep held-out questions and sources separate from answers and evaluation code. Quarantine ambiguous cases before release or resolve them under a new task version.

## Dataset card

**Dataset** Boatable Marine Service Desk, version 1.0. English-language fictional tasks for testing structured quote reconciliation and release decisions. Every source document is original project material, generated from a written scenario. The files include no public benchmark rows or customer records. The original cases are provided for Product Pat’s project evaluation and practice.

**Composition and splits** 12 unique scenario groups, six development and six held-out. Each split has two quote, two scope-change and two scheduling cases. A common service-desk policy is shared deliberately. Cases do not share a quote, approval or scheduling bundle across splits. The holdout was assigned in the scenario specification before scoring and export. The held-out file is the only holdout artifact intended for the tested model. A frozen runner should receive its prompt and documents without opening the rest of this archive.

**Record links** `case_id` plus `version` identifies a task. Its source manifest includes the record ID, origin, rights descriptor and SHA-256 of the UTF-8 representation from `json.dumps(doc, sort_keys=True, ensure_ascii=False)`. `response_id` identifies a reference or seeded control. Review and run records point to those response IDs. A blank adjudication means none was recorded. Model and model version are unset for authored and seeded responses.

**Quality and provenance** The same reviewer authored and verified the records. Q01, C01 and S01 served as the pilot. The reference line IDs and decision are set in the scenario independently of the grader’s calculations. Reference amounts derive from the original quote data. Controls are programmatically mutated from the references. There was no second review, so the records have no independent agreement estimate. The score report records controls and regressions rather than model accuracy.

**Intended use and limits** Exercise a model’s structured output, evidence handling and policy adherence. The cases are small, share a common policy and use clean source records. They cannot estimate field accuracy, transfer to other domains, or benefits from model training. If a frozen model becomes available, compare a baseline prompt with a prompt containing development examples. Preserve the same model version, task inputs, decoding settings and scorer. Record output artifacts, criterion counts, invalid inputs and paired per-case results. The comparison tests inference-time examples.
