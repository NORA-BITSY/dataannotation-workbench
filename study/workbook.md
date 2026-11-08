# DataAnnotation assessment practice workbook

**Prepared for Product Pat**

All questions and source packets here are original. They cover skills named in DataAnnotation’s FAQ and role descriptions. The timing and scores in this workbook are practice settings. DataAnnotation does not publish an official scoring key or passing threshold for its Starter Assessment.

## How to use this workbook

The expanded workbook contains 76 drills, eight timed mocks with 24 scored tasks, and 24 recall cards. Start at **Second-pass practice** if you already used the first set.

1. Take **Generalist Mock G** cold if Generalist is the track you intend to enter. For a technical entry, take **Coding Mock C**, then use **DevOps Mock D** to test specialist readiness. For finance, take **Finance Mock F**. Pick the closest match to the actual Starter label shown in your account.
2. Work in a blank document without AI, AI completions, or the answer key. The source packets are self-contained. For coding practice, use a local editor, Python 3 and your own tests. For finance, you may use a calculator or a blank spreadsheet. These are practice permissions. Use the rules shown on the live assessment for any outside tools.
3. Open the separate answer key after finishing. Score each criterion, record your mistake and redo the task unaided. Then take a fresh drill on the same skill. Keep the relevant mock cold if you prefer to study first.
4. For this workbook, a reasonable readiness bar is **80% or better with zero critical errors**, followed by an unaided clean attempt on a fresh drill. Critical errors are fabricated evidence, unsafe or unauthorized actions, materially wrong numbers or a missed explicit instruction that changes the result. This is my practice bar and gives you no official pass prediction.

The public FAQ describes one Starter attempt and different qualification tracks at signup. It estimates about an hour for most Starter Assessments and one to two hours for specialized assessments. The account screen governs the track, instructions and actual timing. [DataAnnotation FAQ](https://www.dataannotation.tech/faqs)

| If you have | Work through |
| --- | --- |
| 45 minutes | G01–G03, then review. For technical entry, C01 and D01. For finance, F01 and F02. |
| Two focused hours | One relevant mock, its key, then two fresh drills on the biggest mistakes. |
| Four sessions | Take a baseline mock, work through targeted drills, repeat the weak skills without the key, then do a different relevant mock or a fresh drill set under time pressure. |
| A week | Day 1 baseline. Days 2–3 study the two weakest skills. Day 4 practice the adjacent track. Day 5 do a mixed set unaided. Day 6 repeat material misses. Day 7 use the readiness checklist and decide whether to start. |

For the work you’ve done, prioritize FP&A modeling and management reporting, or coding plus DevOps. Use a real forecast, reconciliation, or deployment you personally handled when practicing how to explain experience. [FP&A](https://www.dataannotation.tech/job-board/fpa-analyst) · [Finance Expert](https://www.dataannotation.tech/job-board/finance-expert) · [DevOps](https://www.dataannotation.tech/job-board/devops-engineer) · [Software Engineer](https://www.dataannotation.tech/job-board/software-engineer)

## Study notes

### Generalist and shared evaluation skills

- Turn the user’s request into a checklist before comparing answers. Include format, required facts, forbidden claims, and the deliverable.
- Judge against the evidence packet. Identify the exact claim, the supporting or conflicting line, and the correction. Unsupported means the packet cannot establish it. Contradicted means the packet gives evidence against it.
- Distinguish a harmless wording flaw from a mistake that changes the result. If two answers share a critical failure, state it even if one reads better.
- Write verdict, evidence and consequence. A short explanation with a concrete citation beats a long impression of tone.
- Reread the deliverable against every instruction. Count bullets or words where requested.

### Coding

- Write the input contract and tie-break before touching the implementation. Trace a normal case and a boundary case.
- Reach for a dictionary when you need lookup or aggregation by ID, a set when you need membership, and sorting when order is the core requirement.
- For intervals, decide whether touching boundaries overlap. For queues or sliding windows, state what leaves the window and when.
- Keep a few independent tests. Use empty input, a duplicate, a tie, and a value exactly at the boundary. Verify a return type and whether mutation is permitted.
- When reviewing a patch, give a minimal counterexample with expected versus observed behavior. Explain time and auxiliary space in terms of the input size.

### DevOps and backend

- Trace the path from user to load balancer, application, dependencies and database. Identify what actually proves the service is ready.
- Separate artifact identity, configuration, secrets and state. An immutable image reference makes rollback reproducible. Database compatibility determines whether rolling back the app can work.
- Think through retries, partial failure and concurrency. When a request can arrive twice, identify which system enforces the idempotency rule and what happens if the external call succeeds but your process crashes.
- Keep verification concrete. Name the test, what would make it pass and what would trigger a hold or rollback.

### Finance and FP&A

- State the period, unit, sign convention and denominator before computing. Separate revenue, operating profit and cash.
- Use `profit = units × (price − variable cost per unit) − fixed cost`. Tie the volume, price, variable-cost and fixed-cost effects to the full movement.
- For an indirect cash flow, subtract an increase in operating receivables or inventory and add an increase in operating payables. Keep debt movements separate from operating cash.
- For enterprise valuation, use unlevered cash flows with an enterprise discount rate, discount terminal value to today, then subtract debt and add cash under the problem’s assumptions.
- Review each material claim against the model. Cite a driver, quantify its effect, and describe the remaining uncertainty.

## Generalist drills

Use only the fictional material supplied for each task. Unless the task says otherwise, give a brief rationale with line labels.

### G01 — Compare replies · 8 min

Customer asks for the earliest confirmed boat pickup and what to bring. R1 says Friday 3 p.m. is held pending shop confirmation. R2 confirms Monday at 9 a.m. R3 says bring a photo ID and the work-order number.

- A: “Your pickup is confirmed for Friday at 3. Bring photo ID and your work-order number.”
- B: “Your earliest confirmed pickup is Monday at 9 a.m. Bring photo ID and your work-order number.”

Choose the better answer and explain the practical consequence of the material error in the other.

### G02 — Rewrite a policy response · 8 min

P1 says standard returns are accepted within 30 calendar days of delivery. P2 says a final-sale product is ineligible for a change-of-mind return. P3 says damage reported within seven days goes to support review, and approval is case by case. The buyer reports damage on day 5. The item was final sale. A draft says, “You qualify for a refund within 30 days.” Replace it in **at most 45 words**. Give the next action and make no guarantee.

### G03 — Source conflict · 10 min

D1, customer email dated May 3, approves a $120 inspection and declines a $60 cleaning. D2, a May 4 draft estimate, lists both lines. D3, a May 5 shop log, says cleaning was performed but contains no approval. D4 says the shop bills optional work only with recorded customer approval.

Produce a two-row table with line, bill now (yes/no), and supporting record. Add one sentence on what the newest log can establish.

### G04 — Format and arithmetic · 8 min

R1 shows three kits reserved at $24 each. R2 says one was canceled before shipment. R3 shows shipping of $9 for the remaining order. Return **exactly three bullets**, starting with **Shipped**, **Subtotal**, and **Total**, respectively. Include the currency symbol on both money lines. Do not add a greeting or show work.

### G05 — Materiality and both-bad judgment · 10 min

Q asks for the safest statement about a demo launch. N1 says a four-person internal demo passed. N2 says no public launch date was approved. N3 says external load testing has not begun.

- A: “The demo passed, and the public launch is approved for June.”
- B: “External load testing passed, and the team is awaiting a launch date.”

The rubric permits **A**, **B**, **tie**, or **both bad**. Give one label, one material defect per answer, and a corrected statement of at most 40 words.

### G06 — Weak causal claim · 10 min

N1 says a store changed its homepage on Tuesday. N2 says visits rose from 2,000 to 2,600 that week. N3 says a paid campaign started Tuesday. N4 says weather and seasonality were not studied. A draft states, “The homepage redesign caused a 30% increase.” Rewrite it for an internal report and name one comparison that would improve attribution.

### G07 — Latest record and scope · 9 min

R1, 8:00 a.m., reserves bay 2 on Friday for Unit 14. R2, 9:10 a.m., cancels that booking for a lift inspection. R3, 9:30 a.m., confirms bay 3 on Saturday for Unit 18. R4, 10:00 a.m., says Unit 14 is first on the Friday waitlist. A customer asks whether Unit 14 can arrive Friday. Give a one-sentence answer and cite the two relevant updated records.

### G08 — Ask a focused question · 8 min

A customer asks, “Can you move my delivery to next Tuesday?” The record lists two open deliveries for this customer, **A17** and **B43**. Tuesday has potential capacity; availability is only confirmed after a specific delivery is selected. Draft a response in two sentences. Ask only what you need to proceed and avoid promising a slot.

### G09 — Percent versus percentage points · 8 min

A report says completion went from 60 of 100 cases to 75 of 100. A draft calls it “a 15% improvement” and claims the change applies to all sites. The packet describes only one site. Calculate both the percentage-point and relative changes, then rewrite the claim with appropriate scope.

### G10 — Confident claims from incomplete evidence · 10 min

S1 says 48 of 60 inspected records contained a signed approval. S2 says the remaining 12 lacked a signed copy in the packet. S3 says some approvals can be stored in a separate system that was not checked. A draft says “20% of work was done without approval.” Explain the flaw and write a more defensible sentence.

## Coding drills

Use Python 3 for implementation questions. Include time and auxiliary space when requested. Code blocks under review may contain deliberate bugs.

### C01 — Stable deduplication · 12 min

Implement `unique_ids(ids)`. Input is a list of case-sensitive strings. Return each ID once in order of first occurrence. Leave the input unchanged. Target linear expected time. Provide tests for empty input, a nonadjacent duplicate and distinct casing.

### C02 — Half-open intervals · 20 min

Implement `merge_bookings(intervals)`. Each tuple is `(start, end)` with integer `start < end`. Return sorted tuples with strictly overlapping intervals merged. Touching intervals such as `(1, 3)` and `(3, 5)` stay separate unless another interval bridges them. Preserve the input. Give time and auxiliary space and test a nested interval and a bridge.

### C03 — Top customer · 15 min

Implement `top_customer(sales)`. Each row is `(customer_id, cents)`, with a string ID and integer cents. Refunds are negative. Return `(id, net_cents)` for the highest net total. Break ties by lexicographically smallest ID. Return `None` for empty input. Test a tie and a dataset in which all totals are negative.

### C04 — Find the boundary bug · 10 min

This function should count entries in a sorted list whose timestamps are within `[start, end)`.

```python
def count_events(events, start, end):
    return sum(1 for stamp in events if start < stamp <= end)
```

Give the smallest examples that show the lower and upper boundary bugs. Correct the condition. Then name a faster approach for repeated queries on a large sorted list, including which insertion point to use for each endpoint. Assume `start <= end`.

### C05 — Longest run without repeats · 20 min

Implement `longest_unique(values)` for a list of hashable values. Return the length of the longest contiguous sublist with no repeats, or zero for an empty list. Target linear expected time. Explain why your left boundary never moves backward. Test `["a","b","b","a"]` and an empty list.

### C06 — Incorrect mutable default · 10 min

The author expects every call without `tags` to use a fresh list.

```python
def attach_tag(tag, tags=[]):
    tags.append(tag)
    return tags
```

Give a two-call reproducer, a corrected implementation, and a test for an explicitly supplied empty list. Preserve the behavior of mutating a caller-supplied list.

### C07 — SQL grain and zero rows · 17 min

PostgreSQL tables are `customers(id PRIMARY KEY)`, `orders(id PRIMARY KEY, customer_id, status)`, and `order_items(id PRIMARY KEY, order_id, cents)`. For **every** customer, return the number of paid orders and total item cents on paid orders. A paid order with zero items still counts. Customers without paid orders must appear with zeros. Explain why a naive join followed by `COUNT(orders.id)` can inflate the count and why filtering `status` in the outer `WHERE` is a trap.

### C08 — HTTP retry semantics · 15 min

A service creates a reservation in PostgreSQL and calls a payment provider. A client retries on timeouts. Two API workers may receive the same request simultaneously. The provider supports idempotency keys. Sketch the backend invariant, database constraint, provider call and handling of a crash after charging but before marking the reservation paid. Specify what to return if the same key is reused with a different payload.

### C09 — Grouping and tests · 16 min

Implement `first_duplicate(values)` for an iterable of hashable values. Return the value whose **second appearance is encountered first**, or `None` if none repeats. Inputs contain no `None`. Work in one pass without converting the iterable to a list. Explain how `["b","a","a","b"]` tests the tie in interpretation and what happens to a generator after the function returns.

### C10 — Validate a proposed fix · 12 min

A function should return integer cents for a cart consisting of integer item amounts. Refund rows can be negative. An AI patch changes `sum(cart)` to `sum(max(0, cents) for cents in cart)` to prevent negative subtotals. Explain which specification it breaks. Provide a counterexample. If the product later requires **final totals** to floor at zero, give the expression that preserves refunds before applying the floor.

## DevOps drills

These are fictional review tasks. Where multiple safe designs exist, state assumptions and tell the reviewer how to verify your choice.

### D01 — Image identity and rollback · 13 min

A production pipeline pushes `registry/service:latest`. Rollback reruns the same deploy job with `latest`. An engineer says the old revision is guaranteed to return. Explain why, propose what to record per deploy, and describe a rollback check.

### D02 — Database compatibility · 15 min

Version 1 reads column `name`. Version 2 uses only `display_name`. The proposed release renames the column first, then rolls app instances gradually. Give a staged migration that preserves both app versions and a rollback window. State when the old column may be removed.

### D03 — Readiness and traffic · 12 min

A container listens on its port eight seconds after start. It cannot answer requests that need its database until 35 seconds. The load balancer checks TCP connectivity and starts sending all traffic immediately. A proposed fix uses the database as the liveness check. Explain what to use for readiness and liveness, then give one test that demonstrates the traffic problem is fixed.

### D04 — Secret exposure · 13 min

A GitHub Actions step echoes a production database URL containing a password into logs for 20 minutes. An engineer deletes the log and reruns the job. Write a response in four ordered steps, covering containment, credential rotation, investigation, and prevention.

### D05 — State and concurrent changes · 12 min

Two infrastructure jobs can apply against the same Terraform workspace. State is stored as a local file on each runner. Both jobs show a clean plan against their own files. Explain the risks and propose how state, locking and CI concurrency should work together. Name an observable test.

### D06 — Separate signal from hypothesis · 12 min

A new revision starts at 14:00. API p95 rises from 120 ms to 900 ms. Error rate stays flat. DB CPU rises from 25% to 88%. The new revision includes a query change. Give the first three checks and a criterion for aborting a rollout. Distinguish evidence, hypothesis and what a rollback can tell you.

### D07 — Permission scope · 11 min

A scheduled worker needs to start and stop exactly one GCP VM. Its deploy job gives the worker project-wide Owner and stores a long-lived service account key in a repository secret. Explain the privilege and credential issues. Propose least privilege and a verification test that checks one allowed and one forbidden action. Assume the organization can enforce resource-scoped permissions through its supported IAM setup.

### D08 — Queue backlog and safe recovery · 14 min

A worker acknowledges jobs before persisting results. It also processes an external provider action that can succeed before a worker crash. Backlog rose after a deploy. Give two distinct risks, a safe acknowledgement policy, a duplicate-protection strategy, and two metrics that distinguish throughput trouble from redelivery.

## Finance and FP&A drills

All figures and companies are fictional. Show formulas or a calculation trail. Round only the final answer unless otherwise stated.

### F01 — Operating-profit bridge · 16 min

Budget is 1,000 units at $80 price and $50 variable cost per unit, with $20,000 fixed cost. Actual is 900 units at $85 price and $52 variable cost per unit, with $21,000 fixed cost. Compute budget and actual operating profit. Bridge the difference through volume at budget contribution, price on actual units, variable cost on actual units, and fixed cost. Use positive for favorable.

### F02 — Working capital and cash · 13 min

Net income is $120k and depreciation is $15k. Accounts receivable increased $20k, inventory increased $12k, accounts payable increased $8k, and the company paid $25k of debt principal. Assume no other items. Compute cash flow from operations and the net cash movement before any investing activity. Classify the debt repayment.

### F03 — DCF and terminal value · 20 min

Unlevered free cash flow is $110k in year 1 and $121k in year 2, at year-end. It grows at 2% forever after year 2. WACC is 10%. Debt is $300k, cash is $40k, and there are no other adjustments. Compute terminal value at year 2, enterprise value today, and equity value today. Explain where the draft goes wrong if it adds the undiscounted terminal value to enterprise value today.

### F04 — Rent roll, NOI and cash · 12 min

Twelve units rent at $1,100 per month. On average two units are vacant. Monthly property operating costs are $4,400. Annual debt service is $54,000, and the roof reserve is $8,000 per year. Assume full collection on occupied units, no other income, and no additional costs. Compute annual effective rental income, NOI, and cash after debt service and reserve. The exercise defines NOI before debt and reserve.

### F05 — Credit headroom · 13 min

A lender defines DSCR as annual NOI divided by annual debt service and requires at least 1.25×. NOI is $260k and annual debt service is $200k. Compute current DSCR, minimum compliant NOI, the dollar and percentage decline from current NOI to the covenant floor, and DSCR after a 7% NOI decline.

### F06 — Reconcile two reports · 12 min

A budget report shows $240k in March revenue. The GL export shows $232k, including a $10k credit memo for a February sale issued and recorded in March. The management comparison uses a defined normalization that adds back that credit memo for the March comparison only. Keep the GL value separate. Compute normalized March revenue and its dollar and percentage variance to budget. State the reason the adjustment appears in one comparison.

### F07 — Run-rate forecast · 16 min

January–September actual revenue is $900k. For Q4, assume 110 billed units per month at $1,000 net per unit. Downside assumes 15% fewer units at the same price. Compute full-year base and downside revenue and the dollar and percentage difference from the base. Fractional units are allowed as expected values. A draft applies the 15% cut to the whole full year. Explain its error.

### F08 — Cash timing and liquidity · 15 min

Beginning October cash is $30k. Collections are $80k in October and $105k in November. Cash operating payments are $92k and $90k, respectively. A $25k equipment payment is due in October. Minimum cash is $10k at each month-end. Compute monthly ending cash before financing. Then assume the company draws just enough funding in October to hit the floor and does not repay it in November. Compute the draw and November ending cash.

### F09 — Cohort mix and weighting · 13 min

Segment A had 80 sales out of 100 leads. Segment B had 60 sales out of 300 leads. A draft reports an overall conversion rate of 50% by averaging segment rates. Calculate the correct blended rate and explain when 50% would be a useful statistic.

### F10 — Three-statement effects · 15 min

A company buys $120k of equipment for cash on January 1, uses straight-line depreciation over five years with zero salvage, and records a full year of depreciation. Ignore taxes and any other activity. Show year-one changes to net income, CFO, CFI, cash, net PP&E and retained earnings. State the year-end balance sheet check.

## Timed mock assessments

Each mock is scored separately out of 100. Save at least five minutes to check every required output. Use only the packet and the tools allowed for practice above.

### Generalist Mock G · 55 minutes

#### MG1 — Evidence and verdict · 35 points · 15 min

A customer asks, “Can I collect Unit 31 Wednesday, and what do I owe at pickup?” Records show:

| ID | Record |
| --- | --- |
| R1 | Monday, service desk suggests Wednesday afternoon. |
| R2 | Tuesday, shop confirms Thursday at 11 a.m. and marks Wednesday unavailable. |
| R3 | Signed approval covers a $180 inspection and $40 consumables. The deposit of $50 already posted. |
| R4 | Draft estimate includes a $75 polish. Customer declined it. |

Answer A says, “You’re confirmed for Wednesday. The balance is $170.” Answer B says, “You’re confirmed for Thursday at 11 a.m. The balance is $245, including polishing.”

Use **A**, **B**, **tie**, or **both bad**. Explain one material defect per answer, cite the decisive records, and give a replacement in at most 35 words. Use the amounts as supplied and assume no tax.

#### MG2 — Audit a summary · 35 points · 18 min

A fictional program manager needs a two-bullet update about field checks.

- S1, current field sheet: 72 of 90 checks are complete, with 12 pending and six failed.
- S2, earlier field sheet: 60 of 90 were complete last week.
- S3, coordinator memo: only the east site has reported.
- S4, manager note: failure causes are under investigation.

Draft: “All sites reached 80% completion, up 12 percentage points. The six failures were caused by operator error.”

List three distinct corrections with citations. Then write **exactly two bullets**, one on the completion change and one on the outstanding results and uncertainty.

#### MG3 — Follow constrained instructions · 30 points · 17 min

Policy P1 says quote Q7 is valid through May 18, inclusive. P2 says a $120 inspection may be scheduled once the customer confirms a date. P3 says parts availability is unverified. P4 says the estimate contains a $300 optional line awaiting separate approval. Today is May 18. Draft a response in **three sentences, 65 words maximum**. Sentence 1 must state the quote’s status today. Sentence 2 must ask the customer for a preferred inspection date. Sentence 3 must distinguish the optional line and parts availability. Avoid a guarantee.

### Coding Mock C · 65 minutes

#### MC1 — Adjacent log events · 35 points · 20 min

Implement `adjacent_alerts(events, window)`. Events are sorted by nondecreasing integer timestamp and each row is `(timestamp, account_id)`. Emit `(account_id, timestamp)` for every event that occurs **at most** `window` seconds after that account’s immediately previous event. Preserve input order in the returned alerts. Assume a nonnegative window. Target expected linear time. Provide three tests including simultaneous events and interleaved accounts. State time and space.

#### MC2 — Inventory consumption · 35 points · 22 min

Implement `fulfill(stock, requests)`. The stock mapping has nonnegative integer counts and requests are `(sku, positive_quantity)` in order. A request is accepted only if its full quantity is available. Missing SKUs have zero stock. A rejected request consumes nothing. Return a list of booleans and the final stock mapping. Preserve the input stock and request list. Give tests for exact depletion and a rejection followed by an acceptance. State time and auxiliary space.

#### MC3 — Debug and test · 30 points · 18 min

Review:

```python
def recent_ids(events, cutoff):
    return list({item_id for timestamp, item_id in events if timestamp > cutoff})
```

The contract says include timestamps **equal** to cutoff and return each ID once in first qualifying occurrence order. Explain both defects and provide a corrected implementation. Give a minimal edge test for each defect, explain how to test the ordering requirement when set iteration can happen to agree, and state complexity.

### DevOps Mock D · 60 minutes

#### MD1 — Production release · 40 points · 24 min

A team deploys an API through rolling replacement. Every build pushes the same `stable` tag. A predeploy migration makes `status_code` mandatory and drops `status`. The old image reads and writes `status`. TCP health checks are green even when the API returns database errors. Give a release plan, compatibility sequence, readiness check, and rollback trigger. Name the exact artifacts you would retain for rollback.

#### MD2 — Delayed incident · 35 points · 20 min

At 10:00 a rollout reaches 50%. At 10:04 users report duplicate confirmation emails. Logs show queue messages redelivered after network timeouts. The worker sends email before recording the send, and the external email API supports an idempotency key. Write a triage response with a containment step, an evidence check, the durable fix and a test that reproduces the critical crash window.

#### MD3 — Permission and secret review · 25 points · 11 min

A job reads an artifact from one private bucket and writes a deployment status file to a second. CI can authenticate with short-lived credentials. The proposed config grants broad admin to both buckets and prints the access token. Identify the two problems, propose a least-privilege setup, and state a test proving permitted and denied operations. Address the logged token if the proposed configuration already ran.

### Finance Mock F · 65 minutes

#### MF1 — FP&A bridge · 40 points · 24 min

All amounts are dollars. Budget is 1,200 services at $220 each, $130 variable cost per service, and $70,000 fixed costs. Actual is 1,050 services at $235, $136 variable cost per service, and $72,000 fixed costs. Compute both operating profits and a volume, price, variable cost and fixed cost bridge, favorable positive. Write a two-sentence management takeaway. The records give no reason for the volume decline.

#### MF2 — Cash and credit · 35 points · 21 min

Figures are in thousands. EBITDA is 440. Cash taxes are 50, maintenance capex is 45, working capital absorbed 30, and scheduled annual debt service is 260. For this exercise, coverage is `(EBITDA − cash taxes − maintenance capex − working-capital absorption) / debt service`. The requirement is 1.20×. Compute available cash for debt service, coverage, and dollar headroom versus the required cash amount. A model says there is ample headroom because EBITDA divided by debt service exceeds 1.20×. Explain the error.

#### MF3 — Valuation review · 25 points · 15 min

Figures are in thousands. Year-1 and year-2 unlevered free cash flow are 100 and 110. WACC is 10%, terminal growth is 2%, net debt is 220, and cash flows occur at year-end. A draft uses `110 / (10% − 2%)` for terminal value and adds it undiscounted to the present value of years 1 and 2. Identify both errors, compute the corrected enterprise and equity values, and state why you subtract net debt once.

## Error log

Copy a row per missed skill and redo the task before looking again at the key.

| Task | Score | What I missed | Rule to remember | New test or example | Unaided retry |
| --- | --- | --- | --- | --- | --- |
| | | | | | |

Before starting the live assessment, check the track label and rules, allow an uninterrupted block, and verify you can finish the relevant practice task with time to reread. Use the answer key’s scoring guide to decide what to review first.

## Rapid recall cards

Answer each aloud in one or two sentences. These work well for short phone-only study sessions. Check the matching card in the answer key.

| ID | Prompt |
| --- | --- |
| R01 | What is the difference between a tentative booking and a confirmed booking in a customer reply? |
| R02 | How do you distinguish an unsupported claim from a contradicted one? |
| R03 | What should your explanation contain when one answer is better but still has a material mistake? |
| R04 | What does a plausible explanation of a trend need before you describe it as causal? |
| R05 | When do you ask a clarifying question instead of making an assumption? |
| R06 | Why check source version, date and subject separately? |
| R07 | What data structure helps keep first-seen order while doing fast membership tests? |
| R08 | Why does using integer cents simplify a refund calculation? |
| R09 | How do you test both ends of a half-open interval? |
| R10 | What makes an expected O(n) dictionary solution different from an O(n log n) sorting solution? |
| R11 | How do you choose an input that demonstrates a tie-break bug? |
| R12 | When can a left join stop preserving unmatched rows? |
| R13 | Which reference should an automated rollback use to select a container image? |
| R14 | Why should an app version and its database migration be reviewed together? |
| R15 | What is the difference between readiness and liveness? |
| R16 | When should a worker acknowledge a queue message that produces an external side effect? |
| R17 | What do you do after a provider succeeds but your local process dies before recording it? |
| R18 | What pair of tests gives evidence that a service identity has the right permission scope? |
| R19 | Which contribution margin is used for volume in this workbook’s operating-profit bridge? |
| R20 | What happens to operating cash flow when operating receivables increase, all else equal? |
| R21 | In a two-year DCF, which cash flow starts the terminal-value formula and how far back is that value discounted? |
| R22 | How do you tell whether a variance is material to the user’s decision? |
| R23 | Why does the overall rate use the sum of numerators over the sum of denominators? |
| R24 | If a debt covenant states a specific definition of coverage, what should you do when the model uses a different common ratio? |

## Second-pass practice

Use this section for fresh attempts after the first round. All of the scenarios are fictional and self-contained. The new mocks are independent of the first set. To preserve a cold attempt, take the second mock before looking at its key or score breakdown. For the technical mocks, write runnable code where requested. Treat every unit, tie-break, decision threshold and output constraint as part of the task.

### Pick your next session

| Result from your first attempt | What to do next |
| --- | --- |
| You were accurate but ran out of time | Take two drills at the suggested pace. Reserve the last 15% of the time to verify explicit instructions, calculations and edge cases. |
| You made one material mistake | Redo the problem with the key closed, then take a different drill that tests the same rule. Write down what would have caught the mistake. |
| Finance or FP&A is your likely first route | Do F11, F14 and F17, then take **Finance Mock F2** cold. |
| Coding or DevOps is your likely first route | Do C11, C13 and C16, then take **Coding Mock C2**. If it goes well, do D11 and D14 before **DevOps Mock D2**. |
| Generalist is your likely first route | Do G11, G14 and G17, then take **Generalist Mock G2** cold. |
| You are exploring data and ML roles | Work through ML01–ML06 after the core track. Focus on evaluation design, leakage and interpreting results. |

### More Generalist drills

#### G11 — Effective date · 8 min

P1 is effective through August 31 and charges $12 for delivery. P2 is effective September 1 and charges $18. P3 says the charge is fixed when the order is placed. An order was placed August 30 and arrives September 4. A draft charges $18 because it arrives in September. Give the correct fee and cite the two decisive rules.

#### G12 — Valid tie · 8 min

A user asks for a one-sentence answer stating the appointment time and what to bring. R1 confirms Tuesday at 2 p.m. and requires a photo ID. A says, “Your appointment is Tuesday at 2 p.m., and please bring a photo ID.” B says, “Please bring a photo ID to your appointment on Tuesday at 2 p.m.” Choose A, B, tie or both bad. Justify your answer against the stated requirements.

#### G13 — Separate extraction from inference · 10 min

A record says “Jordan Lee called at 14:15 to ask about invoice 107. Caller said a bank transfer was sent. Bank confirmation unavailable.” Return only JSON with keys `caller`, `time`, `invoice`, `payment_reported`, `payment_verified`. Use strings for caller and time, an integer for invoice, and Booleans for the final two fields.

#### G14 — Check a citation’s claim · 12 min

S1, a memo, says an eight-shop pilot had a median repair time of four days. S2, a survey, says 65% of 40 responding customers reported satisfaction with communication. A draft says “Repairs take four days across the network and 65% of all customers approve of the repair quality (S1–S2).” Identify three separate overclaims and write a corrected sentence.

#### G15 — Write a discriminating prompt · 12 min

Write an original prompt of at most 90 words to test whether a model confuses **approval to inspect** with **approval to repair**. Include a tiny source packet, a requested output and an observable grading condition. Separately provide one plausible but materially incorrect response.

#### G16 — Unsupported precision · 9 min

A dispatch report says delivery is expected in two to four business days after shipment. The package has not shipped and no ship date is confirmed. A chatbot says “It will arrive at 10 a.m. next Tuesday.” Rewrite in two sentences, preserving the timing information and explaining what must happen before an arrival window can be estimated.

#### G17 — Conflicting sources and escalation · 12 min

S1, signed customer approval, authorizes parts up to $400. S2, work note, lists a $475 part. S3, email from an employee, says “customer sounded okay with it.” S4 says revised parts quotes need written customer authorization before ordering. Give a decision, identify two decisive records, and ask for the narrowest next action in no more than 45 words.

#### G18 — Compare rubric weights · 10 min

A rubric scores accuracy 0–4, instruction-following 0–4, style 0–2. Any fabricated refund approval disqualifies the response regardless of score. A earns 3, 4 and 2 and fabricates approval. B earns 4, 3 and 1 and has no fabricated approval. Choose the winner, state the raw totals, and explain how the gate applies.

### More coding and backend drills

#### C11 — Rolling sums · 15 min

Implement `window_totals(values, k)` for a list of integers. Return the sum of each consecutive window of exactly k elements. Return `[]` if k exceeds the input length. Raise `ValueError` for k less than 1. Preserve input, target linear time, and test k=1, negatives and an oversized window.

#### C12 — Find first occurrence by binary search · 15 min

Implement `first_index(sorted_ids, target)` for a list of nondecreasing integers. Return the index of the first matching value, or -1. Use a loop and target O(log n) time with constant extra space. Include duplicates, missing values and an empty list in your tests.

#### C13 — Shortest route through dependencies · 20 min

Implement `shortest_hops(graph, start, goal)`. The graph maps each node to its outgoing neighbors. Every edge costs one hop. Missing keys have no outgoing neighbors. Return the minimum number of hops, or -1 if unreachable. Start equals goal gives 0. Include a cycle and a case where the first neighbor leads to a longer route.

#### C14 — Deterministic top-k selection · 15 min

Implement `ranked_ids(scores, k)`. Scores maps string IDs to integers. Return up to k IDs by descending score, then ascending ID. k is a nonnegative integer. A sort is fine. Explain the cost and test a tie at the cutoff, zero k and k larger than the input.

#### C15 — SQL latest record · 18 min

Given `events(event_id PRIMARY KEY, unit_id, event_at, state)`, return the latest row for each unit. `event_at` is non-null. If times tie, higher `event_id` wins. Return `unit_id`, `event_id` and `state`. Explain why joining on `MAX(event_at)` alone can return duplicate units and give a fixture that tests the tie.

#### C16 — Lost update · 15 min

Two API requests each read a balance of 100, add 10 in application code and write the result. Expected final balance is 120, but the actual balance is 110. Explain the interleaving. Write a PostgreSQL update that increments atomically and returns the new balance. Describe how the fix differs if the same logical credit request can be retried.

#### C17 — Parse and classify · 15 min

Implement `parse_counts(lines)` for strings of the form `label,count`. A valid line contains exactly one comma, a nonempty trimmed label, and a trimmed ASCII integer of one to nine digits with an optional leading plus or minus. Empty and malformed lines are invalid. Return `(totals, invalid_count)` and sum repeated labels. Test negative amounts, extra delimiters and invalid number formats.

#### C18 — Validate before changing state · 15 min

A bulk API uses this draft. A negative or unaffordable quantity should cause the **entire** batch to fail. Quantities must be positive integers. The caller’s inventory must remain unchanged when the batch fails.

```python
def apply_batch(stock, requests):
    for sku, count in requests:
        if stock.get(sku, 0) < count:
            return False
        stock[sku] = stock.get(sku, 0) - count
    return True
```

Show two counterexamples, including one involving an earlier successful request. Sketch a fix for in-memory use under a single writer, then state what a database-backed multi-worker version needs.

### More DevOps drills

#### D09 — Unexpected cache behavior · 12 min

A reverse proxy caches `GET /account` by URL only. Two different signed-in users get the same response. Identify the immediate containment, the policy for this route, and the two-user verification test. Explain why inspecting only response time would miss the issue.

#### D10 — Health of a worker · 12 min

A worker logs “alive” every minute but processes no jobs after losing its queue subscription. Propose two signals beyond process liveness and a staging test. Distinguish what a restart can fix from what should be escalated.

#### D11 — Restore test · 14 min

A backup job reports success nightly. An outage destroyed both the application and its database. The objective is at most one hour of data loss and two hours to restore service. State the recovery point and recovery time objectives in plain English. Explain why the nightly report is insufficient and design a timed restore exercise.

#### D12 — Change blast radius · 14 min

A pipeline applies the same environment variables to staging and production. It points staging at the production queue. The staging worker started consuming live jobs. Give a safe immediate response, a prevention control and a verification step that tests both environments without consuming real jobs.

#### D13 — Artifact trust · 14 min

A production job builds on deploy from a mutable branch, downloads a build tool by an unpinned URL and uses a broad production identity. Propose a release design that binds deployment to reviewed code and an identified artifact. Specify the permission boundary and what you would verify at deploy time.

#### D14 — Safe infrastructure change · 16 min

A proposed change replaces a public load balancer. DNS TTL is five minutes. The old endpoint must remain usable until the new endpoint serves correct HTTPS traffic. Design a cutover with a preflight check, overlap period, observation criteria and rollback. Explain why waiting exactly one TTL may be insufficient.

#### D15 — Capacity versus correctness · 12 min

After a deploy, worker throughput drops from 200 to 70 jobs/min. Inflight jobs increase and provider 429 responses spike. A proposal doubles worker replicas. Explain why this might make the symptom worse and name a better first experiment with a measurable result.

#### D16 — Secrets across revisions · 13 min

A service reads a rotating credential at startup. A rolling deploy leaves two revisions alive for 15 minutes. The proposed rotation invalidates the old credential before any new instances are ready. Design a rotation sequence that accommodates overlap, verify it, and describe an alternative if the provider permits only one active credential.

### More Finance and FP&A drills

#### F11 — Price sensitivity with mix · 15 min

Product A sells 100 units at $90 with variable cost $45 each. Product B sells 60 units at $140 with variable cost $80 each. Fixed costs are $5,000. A scenario shifts 20 units from A to B while total units and per-unit prices and costs remain unchanged. Compute base and scenario operating profit and quantify the mix effect.

#### F12 — Break-even and operating leverage · 13 min

Price is $75, variable cost is $45, and monthly fixed cost is $24,000. Compute break-even units and operating profit at 1,000 units. Then lower volume by 10% and compute the percentage change in profit using initial profit as denominator. Explain why the volume and profit percentages differ.

#### F13 — AR and accruals · 12 min

Beginning accounts receivable is $50k, credit sales are $120k, collections are $100k, and write-offs against existing allowance are $5k. Assume no other movements. Compute ending gross AR. Explain why the write-off is distinct from a collection and why gross AR growth alone does not reconstruct collections in this case.

#### F14 — Gross margin denominator · 12 min

Net sales are $480k and cost of goods sold is $300k. A model says gross margin is 60% because profit is $180k. Compute gross margin and markup on cost, and give a two-sentence correction for management.

#### F15 — Credit and concentration · 15 min

Cash available for annual debt service is $360k, debt service is $250k, and the minimum coverage ratio is 1.25×. The largest tenant supplies $90k of annual cash contribution. An assumed tenant loss removes all of that contribution without cost offsets. Compute baseline and stressed ratios, dollar headroom to the covenant cash floor before stress, and stressed shortfall.

#### F16 — Capital project payback versus NPV · 16 min

A project costs $100k now and returns $45k cash at each year-end for three years. The discount rate is 10%, and terminal value is zero. Compute simple payback using conventional within-year interpolation and NPV. Then state the first year-end at which cumulative cash actually exceeds the cost under the stated timing.

#### F17 — Forecast audit and sensitivity · 16 min

A subscription starts with 1,000 paying customers. The month adds 120 and loses 5% of the beginning base. Assume all changes take effect before billing and price is $30. Compute billed customers and revenue. If churn becomes 7% with additions unchanged, calculate revenue sensitivity. A draft applies churn to the base plus new additions. Explain the discrepancy.

#### F18 — Capex, maintenance and free cash flow · 15 min

EBIT is $150k, tax rate is 25%, D&A is $20k, total capex is $45k, and operating working capital increases $12k. Compute unlevered free cash flow with taxes applied to EBIT. A draft deducts only $25k maintenance capex despite $20k of growth capex in the forecast. State the amount and direction of its error in total free cash flow.

### Data and ML sampler

#### ML01 — Leakage by time · 10 min

A model predicts whether a service quote will be accepted at the time it is sent. Features include quote amount, prior customer jobs, and the eventual number of follow-up calls about that quote. Data are split randomly across an 18-month history. Identify the strongest leakage risk and propose a split and cutoff rule that better represent future use.

#### ML02 — Grouped evaluation · 10 min

An evaluation corpus includes multiple paraphrases of the same base scenario. Versions of several scenarios appear in both development and test sets. Explain how this can inflate scores and specify the unit you would split on. Describe one audit before reporting the result.

#### ML03 — Confusion matrix · 12 min

A classifier flags unauthorized charges. Among 1,000 cases, 50 actually contain an unauthorized charge. It flags 80, of which 40 are correct. Compute true negatives, false negatives, precision, recall and overall accuracy. Explain why accuracy alone is misleading here.

#### ML04 — Threshold and business costs · 12 min

At threshold A, a validation set yields five false negatives and 40 false positives. At threshold B, it yields nine false negatives and 18 false positives. Assign cost 8 to each missed problem and 1 to each false alarm. Calculate each threshold’s cost, choose one under this objective, and identify which set to use for the final report.

#### ML05 — Compare systems fairly · 13 min

A new retrieval prompt scores 84% on 100 cases and the previous prompt scored 79% on a different 100. The new prompt was revised after viewing several of its test failures. Explain why the five-point gap is hard to interpret. Design a controlled follow-up with a primary metric, paired comparison and data-handling rule.

#### ML06 — Model performance by slice · 12 min

A benchmark contains 180 routine cases with 171 passes and 20 safety-critical cases with 11 passes. Calculate overall and slice pass rates. Write a two-sentence finding for a decision-maker. Distinguish what the sample shows from what you can claim about future production.

## Second timed mocks

Each mock is worth 100 practice points. Times include five minutes for checking. For a retake, write the entire answer in a fresh document. The second mocks deliberately introduce different constraints and edge cases.

### Generalist Mock G2 · 60 minutes

#### MG21 — Apply a rule hierarchy · 35 points · 18 min

Nora requests a refund for a canceled ferry rental. The fictional records say:

| ID | Record |
| --- | --- |
| P1 | Customer-initiated cancellation within 24 hours normally earns a credit only. |
| P2 | Operator cancellations due to weather are eligible for refund of the rental fee. |
| P3 | Refunds must be reviewed before they are issued. A $12 third-party booking fee is excluded. |
| R1 | Operator cancellation notice, weather, issued 10 hours before departure. |
| R2 | Paid rental fee $140 and third-party booking fee $12. |

A says “You canceled within 24 hours, so your only option is a credit.” B says “The operator canceled, so your full $152 refund has been issued.” Give A, B, tie or both bad. Explain the decisive defect in each answer and write a corrected response in **at most 45 words**. Cite source IDs in your rationale.

#### MG22 — Edit a claim with multiple denominators · 35 points · 18 min

A trial has 120 enrolled. Ten withdrew before treatment and 110 started. At week six, 88 starters completed the follow-up survey. Of those, 66 reported improvement. The draft states “75% of all participants improved, demonstrating the treatment works.” This packet supplies no control group or improvement records for nonrespondents. Compute the improvement rate among respondents, the confirmed count as a share of starters, and the confirmed count as a share of enrollees. Give a two-sentence replacement and identify the unsupported causal claim.

#### MG23 — Preserve structured constraints · 30 points · 19 min

A customer asks for an update on tickets T1 and T2. A 9 a.m. note marks T1 waiting on parts. A 2 p.m. note closes T1 with no balance due. A 3 p.m. note says T2 remains open, no ETA, and the customer needs to approve a revised quote before repair work starts. Return exactly two rows in a Markdown table with columns **Ticket**, **Current status**, **Next action**. Order T2 before T1. Use the phrase **ETA unavailable** in T2’s current status. Follow the table with one sentence of at most 20 words identifying the customer’s next action.

### Coding Mock C2 · 70 minutes

#### MC21 — Count contiguous totals · 40 points · 25 min

Implement `count_target_ranges(values, target)`. Return the number of nonempty contiguous sublists whose sum equals target. Values are integers and may include negatives and zeros. Target expected O(n) time. Explain why an ordinary expanding/shrinking window is insufficient, and test `[0,0]` with target zero, `[1,-1,1]` with target one, and empty input.

#### MC22 — Reachability with layered output · 35 points · 22 min

Implement `reachable_by_level(graph, start)`. The graph is directed, adjacency lists are ordered, and missing keys have no neighbors. Return a list of lists. Level zero contains start. Each later level contains nodes first reached in that many edges, in first discovery order. Include each node once. Handle cycles and repeated neighbors. Give a test with both, and state complexity.

#### MC23 — Reviewer’s counterexample · 25 points · 18 min

Review this proposal for a function that should select the three largest signed scores, descending, while preserving the input and returning fewer than three when necessary.

```python
def top_three(scores):
    scores.sort(key=abs)
    return scores[-3:]
```

Identify each independent defect. Give a small fixture where absolute-value ranking selects the wrong members, plus a fixture where the returned order is wrong even if every score is positive. Supply a corrected implementation and a check for nonmutation.

### DevOps Mock D2 · 65 minutes

#### MD21 — State safety before a live change · 35 points · 20 min

A Terraform plan says it will replace a database after a resource address was refactored. The desired database settings are unchanged. The current remote backend supports locking. A teammate proposes applying immediately, then restoring a snapshot if replacement causes trouble. Write the decision, the evidence needed to distinguish address drift from an actual replacement, a safe way to reconcile the address if that is the cause, and the final checks before allowing any apply. Treat the database as production.

#### MD22 — Cache and authorization incident · 35 points · 20 min

After a release, a customer sees another customer’s invoice. CDN logs show cache hits for an authenticated endpoint. You cannot yet tell whether the CDN was the sole cause. Write a triage sequence covering containment, evidence and impact assessment, a fix addressing both caching and origin authorization, and an observable two-user test. Include how you avoid spreading invoice data during diagnosis.

#### MD23 — Queue and provider rate limits · 30 points · 20 min

A provider returns 429 with a retry-after value. Workers ignore it and retry immediately. Queue age grows. Existing tasks can be retried and provider calls accept an idempotency key. Propose a bounded retry policy, queue behavior, duplicate protection, and a canary test with success and stop signals. State when a failed task should enter manual review.

### Finance Mock F2 · 70 minutes

#### MF21 — Rolling forecast and pricing tradeoff · 35 points · 22 min

Year-to-date revenue is $1,080k through September. In Q4, the baseline is 2,000 units at $60 per unit, $35 variable cost per unit and $30k fixed cost. A proposed Q4 price increase to $66 reduces expected units by 12%, with the same unit variable cost and fixed cost. Compute full-year revenue for both scenarios, Q4 operating profit for both, and incremental Q4 profit. Calculate the minimum whole units at the new price needed to match or beat baseline Q4 profit. Explain why the revenue and profit decisions can differ.

#### MF22 — Tie accrual profit to cash · 35 points · 22 min

Amounts are in thousands. Beginning cash is 50. Net income is 90 and D&A is 15. AR increases by 35, inventory falls by 8, and AP falls by 12. Capex is 40. The company borrows 25 and repays 18 of debt principal. Compute CFO, CFI, CFF and ending cash. A draft shows ending cash of 142 after treating the AP reduction as a source. Identify whether the reported number actually follows from that sign error under the stated assumptions.

#### MF23 — Audit a debt metric and communicate it · 30 points · 21 min

Amounts are in thousands. EBITDA is 240 and base annual cash operating costs are already reflected in EBITDA. For the specified coverage metric, deduct 30 maintenance capex and 20 cash taxes from EBITDA and divide by annual debt service of 150. Minimum is 1.25×. A downside reduces EBITDA by 12% and leaves the deductions unchanged. Compute base and downside coverage, the downside cash shortfall to the floor, and minimum EBITDA to meet the floor. Write a two-sentence recommendation that states what additional evidence you would request before relying on the forecast.

## Final prep check

- **Follow instructions:** Before each answer, identify the deliverable, constraints, allowed sources and any exact format.
- **Check the highest-risk item:** In Generalist, trace a decisive claim. In coding, run a boundary or counterexample test. In DevOps, simulate a failure or rollback. In finance, tie the result to endpoints or a second calculation.
- **Track improvement:** A fresh problem should show you can apply the rule without recalling a particular answer. Compare rubric categories across attempts. One critical miss is worth reviewing even when the total is high.
- **Before opening the actual assessment:** Confirm the track, reserve a quiet block and read the live instructions on timing and allowed tools. If AI assistance is prohibited, do the live work independently and keep AI completions disabled.
