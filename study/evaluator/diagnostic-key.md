# Diagnostic keys and scoring · evaluator only

Finish an unaided attempt before opening this page. Each form uses a 100-point practice rubric. Record points and critical errors separately. A score of at least 80 with zero critical errors and a clean fresh retest is the provisional readiness gate. For a technical entry, also require at least 36/50 in **each** half so one strength cannot hide the other. A reviewer can use the same points after the attempt. These are local practice standards.

## Finance forms

Each FIN form uses this rubric.

| Criterion | Points |
| --- | ---: |
| Budget and actual operating profit | 12, six each |
| Four bridge effects | 24, six each |
| Correct signs and proof of tie to the actual-minus-budget delta | 9 |
| Cash endpoint and minimum funding calculation | 22, 11 each |
| Identifies invalid cash assumption and cites the decisive record | 13 |
| Two-sentence management note with quantified driver, cash action and appropriately scoped uncertainty | 20 |
| Total | 100 |

A **critical error** is a reversed management decision from material arithmetic, counting the invalid receipt as cash, hiding an untied bridge, or inventing a business cause. A wrong effect that is explicitly flagged and reconciled loses the relevant points. Score cash and operating profit separately.

| Form | Budget → actual profit | Bridge in dollars, volume / price / variable / fixed | Cash before financing / funding |
| --- | --- | --- | --- |
| FIN-A | $15,000 → $11,200, −$3,800 | −4,500 / +4,500 / −1,800 / −2,000 | $23k / $7k |
| FIN-B | $20,000 → $16,680, −$3,320 | +2,800 / −3,200 / −1,920 / −1,000 | $19k / $6k |
| FIN-C | $14,000 → $13,680, −$320 | −1,600 / +4,560 / −2,280 / −1,000 | $8k / $4k |

**FIN-A.** Budget = 1,000 × (100 − 55) − 30,000. Actual = 900 × (105 − 57) − 32,000. Cash = 42 + 70 − 64 − 25. Exclude the deposit expected on day 31. Example note: “Operating profit declined $3,800 as higher prices offset the lost volume but did not cover higher costs. Arrange $7k of funding to reach the floor and investigate the unit decline.”

**FIN-B.** Budget = 600 × (180 − 110) − 22,000. Actual = 640 × (175 − 113) − 23,000. Cash = 28 + 54 − 51 − 12. The $9k invoice has yet to turn into cash. Example note: “Volume added $2,800 but lower unit price took away $3,200 before cost increases. Arrange $6k of funding and examine invoice-level prices and product mix before attributing the decline to discounts.”

**FIN-C.** Budget = 800 × (90 − 50) − 18,000. Actual = 760 × (96 − 53) − 19,000. The $4,560 price benefit offsets $4,880 in adverse effects. Cash = 15 + 49 − 36 − 20. A credit against a later vendor invoice is not cash received. Example note: “Higher prices offset $4,560 of adverse volume and cost effects, leaving profit down $320. Arrange $4k of funding, and verify the cause of the unit decline before changing the sales forecast.”

## Technical forms

Each TECH form uses the same structure. The [reference functions](diagnostic-reference.py) run on Python 3.

| Criterion | Points |
| --- | ---: |
| Implements all required output semantics and preserves input | 24 |
| Three meaningful tests covering required boundary cases | 16 |
| Correct complexity explanation | 10 |
| Release or incident decision tied to the supplied evidence | 12 |
| Recovery design handles the explicit safety constraint | 18 |
| Observable verification, including a failure-path test | 14 |
| Concise note separating evidence, assumption and action | 6 |
| Total | 100 |

A **critical error** is a materially wrong code result that would count the wrong event or state, losing pending work, promoting with a failing representative check, or ordering a rollback to an incompatible or unidentified artifact. A working normal case alone does not earn boundary-test points.

**TECH-A.** Store seen event IDs and aggregate signed cents on first occurrence. Keep zero totals. Expected time O(n), memory O(u + c) including the result, with u unique events and c customers. Pause or isolate the send path while preserving the queue. Keep a durable operation record and stable provider key, reconcile ambiguous success, and acknowledge only when safe. Test a crash after provider success before local completion and verify one provider send after retry. Identify the prior verified digest and compatible configuration/schema from deployment records before any rollback. A mutable tag is insufficient evidence of identity.

**TECH-B.** Maintain a separate streak count per account. Reset on success and alert only at the threshold event, so later failures in that streak cannot alert again. Expected O(n) time and O(a) auxiliary space excluding output. Hold or stop the rollout. Test the DB-backed traffic path for readiness and keep liveness tied to the process rather than dependency health. Induce the DB delay and verify the traffic path excludes the new instance until ready. Define a threshold such as a sustained representative 503 rate above the agreed baseline and verify the known-good digest, its schema compatibility, and healthy smoke tests before and after rollback.

**TECH-C.** Compare the two-field marker lexicographically within each entity and return its state. Expected O(n) time, O(e) space for e entities. Hold the destructive rename. Add the new column while keeping the old one, backfill and maintain compatible writes across versions, and move reads after proving consistency. Test old-write/new-read and new-write/old-read, including rollback. Remove the old column only after old writers retire and rollback compatibility is no longer required or has an independent verified path.

## Generalist forms

| Criterion | Points |
| --- | ---: |
| Correct comparative verdict | 25 |
| Material errors with decisive evidence IDs | 30 |
| Complete and factually correct rewrite | 35 |
| Fits the 40-word limit and required deliverables | 10 |
| Total | 100 |

**GEN-A.** B is better. A makes an unsupported claim that the refund has been issued and includes the excluded $9 fee. R2 establishes pending review. P1 and R1 establish eligibility, and P2 excludes the fee. Rewrite: “Your $80 rental fee is eligible for refund review. The $9 third-party booking fee is excluded. The decision is still pending.”

**GEN-B.** Both bad. A presents an unavailable slot as booked, contrary to P1 and R2. B gets the date right and contradicts P2 on photo ID. Rewrite: “You’re confirmed for Wednesday at 11 a.m. Bring a photo ID to check in.”

A **critical error** here is inventing approval, promising an unavailable slot or removing a stated condition. A stylistic preference alone does not change the verdict.

## Applied labs

**Finance.** Grade source selection and correction (25), October profit and tie-out (25), forecast and independent cash tie-out (35), and a concise management note with a bounded assumption (15). October closes at $6,440 versus $7,200 budget. The bridge is −$2,280 + $4,200 − $1,680 − $1,000 = −$760. The draft used $47 rather than A03's $49 variable cost. November base and downside operating profits are $6,850 and $3,365. End cash before financing is $15,000 and $9,000, requiring $3,000 and $9,000. Use approved $14,000 capex C05, discard superseded C07, and exclude C08 until December. Independent cash movement is −$7,000 base and −$13,000 downside. Adding each funding requirement brings ending cash to $18,000. The [reference calculator](finance-lab-reference.py) rebuilds this from the input rows. A critical error is funding the wrong amount by counting outside-period or superseded amounts, or a materially untied bridge presented as correct.

**Release.** Grade reproducible before/after evidence (20), correct gate and reason order (35), added boundary test (10), and safe evidence-based decision with observable verification (35). The learner code should fail four of five test methods (five failures counting the regression subtests) and the [reference implementation](technical-release-reference.py) passes all five. Hold. The mutable tag, incompatible prior schema, 503 and p95 of 460 ms violate separate gates. Preserve the verified old digest but restore compatible schema through a tested path before attempting that image. Gate on immutable candidate and actual DB-backed success, then confirm both latency and error rate. A critical error is authorizing promotion or a rollback that can still write incompatible data.

## Retest and coaching

Log the exact failed criterion and one preventative check. Repair it with a targeted workbook drill, then use the next unopened variant. A reviewer should give criterion-level feedback, cite one mistake from the completed practice response, distinguish actual from possible errors, and name the fresh retest. For finance, use A → B → C. For technical, use A → B → C. For Generalist, use A → B and then one unseen workbook mock if needed.
