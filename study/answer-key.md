# DataAnnotation practice answer key

Open this after attempting the corresponding exercise in **DataAnnotation_Practice_Workbook.md**. Equivalent answers earn full credit if they preserve the facts, satisfy the prompt, and work on edge cases.

## How to score yourself

- For a short drill, give yourself one point for each of five checks. **Decision or result**, **evidence or reasoning**, **every required output**, **format or implementation**, and **independent verification**. Skip an inapplicable check and adjust the denominator. For verification, recalculate, run tests or explicitly check the answer against the source packet.
- For a mock, use its point breakdown. Score observable work in the submitted draft. Give partial credit for correct reasoning even if a later calculation went wrong, while recording any critical error separately. Mark your first attempt before revising.
- Treat material unsupported claims, wrong authorization or a broken release plan, materially wrong numbers, and instructions missed in a way that changes the result as critical. A polished explanation can still fail one of these checks.
- A practice score of 80/100 or better, zero critical errors, and a clean attempt on a fresh drill is the suggested readiness bar. Treat it as a way to decide what to work on. It is independent of DataAnnotation’s assessment and hiring decisions.

## Generalist drills

### G01 — Compare replies

**B.** R2 confirms Monday at 9 a.m., and R3 supports the items to bring. R1 describes Friday as tentative. A’s error could cause the customer to arrive before the shop is ready. The material difference is confirmation status.

### G02 — Rewrite a policy response

> Please contact support with your order details and a description of the damage. You reported it within seven days, so support can review it. Final-sale items are ineligible for change-of-mind returns, and the outcome depends on the review.

This uses P2 and P3 without treating P1 as a promise. A response can earn full credit with the damage-review route and no guarantee even if it omits the change-of-mind detail.

### G03 — Source conflict

| Line | Bill now | Evidence |
| --- | --- | --- |
| $120 inspection | Yes | D1 approval and D4 billing rule |
| $60 cleaning | No | D1 decline and D4 billing rule |

D3 establishes that the shop recorded the cleaning as performed. It supplies no customer authorization. D2 is a draft and does not change D1.

### G04 — Format and arithmetic

- Shipped 2 kits
- Subtotal $48
- Total $57

Two times $24, plus $9. Check that the response itself has three bullets, begins each bullet correctly, and has no work or greeting.

### G05 — Materiality and both-bad judgment

**Both bad.** A asserts public approval despite N2. B claims that external testing passed despite N3.

> The four-person internal demo passed. No public launch date has been approved, and external load testing has yet to begin.

### G06 — Weak causal claim

> Visits rose 30%, from 2,000 to 2,600, during the week the homepage changed and the paid campaign began. Their individual effects are unknown.

One useful comparison is a randomized old-versus-new homepage test with otherwise comparable traffic acquisition. The denominator is 2,000. The time coincidence does not isolate the cause.

### G07 — Latest record and scope

> Unit 14’s Friday booking was canceled and it is first on the waitlist, so a Friday arrival is still unconfirmed (R2, R4).

R3 confirms a different unit. Being first on a waitlist is distinct from a reservation.

### G08 — Ask a focused question

> Which delivery would you like to move, A17 or B43? Once I know which one, I can check whether next Tuesday is available.

Asking for both the ID and unrelated details adds friction. A specific booking needs the delivery ID first.

### G09 — Percent versus percentage points

The change is **15 percentage points** and **25% relative to the previous rate**, because `(75% − 60%) / 60% = 25%`.

> At the measured site, completion rose from 60% to 75%, an increase of 15 percentage points.

The measurement does not generalize to all sites.

### G10 — Confident claims from incomplete evidence

> Of 60 inspected records, 12 (20%) lacked a signed approval copy in the packet. The separate approval system was not reviewed.

The sample measures missing documents in one packet. The authorization itself remains unverified for those 12. S1–S3 do not establish that work proceeded without approval.

## Coding drills

### C01 — Stable deduplication

```python
def unique_ids(ids):
    seen = set()
    result = []
    for item_id in ids:
        if item_id not in seen:
            seen.add(item_id)
            result.append(item_id)
    return result

assert unique_ids([]) == []
source = ["b", "a", "b", "A"]
assert unique_ids(source) == ["b", "a", "A"]
assert source == ["b", "a", "b", "A"]
```

Expected O(n) time and O(u) auxiliary space for u unique IDs, excluding the returned list. A set alone loses the required order.

### C02 — Half-open intervals

```python
def merge_bookings(intervals):
    merged = []
    for start, end in sorted(intervals):
        if merged and start < merged[-1][1]:
            left, right = merged[-1]
            merged[-1] = (left, max(right, end))
        else:
            merged.append((start, end))
    return merged

assert merge_bookings([(1, 3), (3, 5)]) == [(1, 3), (3, 5)]
assert merge_bookings([(1, 3), (3, 5), (2, 4)]) == [(1, 5)]
source = [(2, 3), (1, 8), (9, 10)]
assert merge_bookings(source) == [(1, 8), (9, 10)]
assert source == [(2, 3), (1, 8), (9, 10)]
assert merge_bookings([]) == []
```

O(n log n) time and O(n) auxiliary space for the sorted copy. The strict comparison preserves touching intervals. Taking the maximum end preserves nested intervals.

### C03 — Top customer

```python
def top_customer(sales):
    totals = {}
    for customer_id, cents in sales:
        totals[customer_id] = totals.get(customer_id, 0) + cents
    if not totals:
        return None
    best = min(totals, key=lambda customer_id: (-totals[customer_id], customer_id))
    return best, totals[best]

assert top_customer([]) is None
assert top_customer([("b", 3), ("a", 7), ("a", -4)]) == ("a", 3)
assert top_customer([("a", -5), ("b", -2)]) == ("b", -2)
```

Expected O(n) time, O(u) auxiliary space. Setting the initial best total to zero would fail the all-negative case.

### C04 — Find the boundary bug

For `start=10` and `end=20`, `[10]` should count 1 but returns 0. With `[20]`, it should count 0 but returns 1. Use `start <= stamp < end`. On a sorted list, subtract the first index at or above the start from the first index at or above the end.

```python
from bisect import bisect_left

def count_events(events, start, end):
    return bisect_left(events, end) - bisect_left(events, start)

assert count_events([10, 10, 19, 20, 20], 10, 20) == 3
assert count_events([10], 10, 10) == 0
```

O(log n) time per query. Use the left insertion point for both bounds so duplicate boundary values are handled correctly.

### C05 — Longest run without repeats

```python
def longest_unique(values):
    last_seen = {}
    left = 0
    best = 0
    for right, value in enumerate(values):
        left = max(left, last_seen.get(value, -1) + 1)
        last_seen[value] = right
        best = max(best, right - left + 1)
    return best

assert longest_unique(["a", "b", "b", "a"]) == 2
assert longest_unique([]) == 0
assert longest_unique([1, 2, 3, 1, 4]) == 4
```

The max prevents a repeat from before the current window from moving the left boundary backward. Expected O(n) time and O(u) space.

### C06 — Incorrect mutable default

Call `attach_tag("a")`, then `attach_tag("b")`. The second call returns both tags in the original implementation. Python evaluates the default when defining the function, so the list is shared. Use an explicit identity check for the default.

```python
def attach_tag(tag, tags=None):
    if tags is None:
        tags = []
    tags.append(tag)
    return tags

assert attach_tag("a") == ["a"]
assert attach_tag("b") == ["b"]
supplied = []
assert attach_tag("c", supplied) is supplied
assert supplied == ["c"]
```

A fallback of `tags or []` silently replaces a caller-supplied empty list.

### C07 — SQL grain and zero rows

```sql
SELECT c.id,
       COUNT(DISTINCT o.id) AS paid_orders,
       COALESCE(SUM(i.cents), 0) AS paid_item_cents
FROM customers AS c
LEFT JOIN orders AS o
  ON o.customer_id = c.id AND o.status = 'paid'
LEFT JOIN order_items AS i
  ON i.order_id = o.id
GROUP BY c.id
ORDER BY c.id;
```

An order with two item rows appears twice after the join, inflating plain `COUNT(o.id)`. Distinct counts a paid order once even if the item join has no match. The paid-status filter in the join preserves the customer without a qualifying order. Moving it to the outer `WHERE` filters those customers out.

### C08 — HTTP retry semantics

Scope the key to the customer or other authorized caller. Enforce uniqueness on `(caller_id, idempotency_key)` in PostgreSQL and store a stable representation or hash of the request. Commit a pending reservation or equivalent durable record before issuing the external call. Use a stable provider key for that operation, so worker retries and reconciliation refer to the same charge. If the provider succeeded before the worker crashed, reconcile or retry with the same provider key and store its existing result before finalizing. A repeated request with the same payload returns its existing result or pending status. A different payload using the same key returns a conflict such as HTTP 409. A database constraint alone does not prevent duplicate calls to an external provider.

### C09 — Grouping and tests

```python
def first_duplicate(values):
    seen = set()
    for value in values:
        if value in seen:
            return value
        seen.add(value)
    return None

assert first_duplicate(["b", "a", "a", "b"]) == "a"
assert first_duplicate([]) is None
stream = iter(["b", "a", "a", "b"])
assert first_duplicate(stream) == "a"
assert next(stream) == "b"
```

The relevant order is each value’s second appearance. The generator is consumed through the matching item and remains positioned at the next item. If there is no match it is exhausted. Expected O(n) time and O(u) auxiliary space for the consumed prefix.

### C10 — Validate a proposed fix

For `[1000, -250]`, the required subtotal is 750 cents. The patch returns 1,000 because it discards the refund. If the final total must floor at zero, use `max(0, sum(cart))`. With `[100, -200]`, that returns zero. The original specification allows a negative subtotal, so applying even a final floor is a product change.

## DevOps drills

### D01 — Image identity and rollback

A mutable tag can point at a different image on the rollback run. Record the deployed image digest, previous known-good digest, source revision, effective configuration version and migration state for each environment. Redeploy the previously verified digest with compatible configuration and schema. Confirm the running revision or digest, then run a request through the production traffic path and compare error rate and latency against the release baseline.

### D02 — Database compatibility

Add a nullable `display_name` while leaving `name` in place. Put synchronization in the write path across the mixed-version window, for example with a database mechanism covering writes by both versions. Backfill and reconcile. Deploy new code that can tolerate the transition and keep both fields consistent. Verify that reads and writes work through both versions and that a rollback still sees fresh data. After old writers are removed, data has been reconciled, and the rollback window has ended or rollback is independently made safe, enforce new constraints and remove the old field. An initial backfill alone misses updates arriving during the rollout.

### D03 — Readiness and traffic

Readiness should check whether the instance can serve the traffic it will receive. In this scenario, include a lightweight check of the necessary DB path with bounded timeout and avoid an expensive query. Liveness should test whether the process is responsive and should be restarted when it is genuinely stuck. Making a shared DB outage a liveness failure can restart every otherwise healthy instance. In staging, delay DB availability, send representative requests through the load balancer, and verify that the new instance receives no traffic until ready and then serves the DB-backed request.

### D04 — Secret exposure

1. Disable the offending step, restrict log access, and preserve relevant access evidence with the secret redacted.
2. Revoke or rotate the exposed credential promptly and update the approved runtime secret. Verify the old credential fails and the application still connects.
3. Review log access and database authentication from the exposure window onward. Assess whether the credential was used and what it could access.
4. Remove credential printing, use least-privilege secret injection, and verify fresh logs contain no credential. Masking is a backup, since transformed values can escape it.

### D05 — State and concurrent changes

Each local state copy can disagree about resources and ownership. Put the workspace on a shared remote backend that supports state locking, scope state access, and serialize applies for the same environment in CI. Use the same workspace and backend for planning and applying. Reject a stale plan or replan after a concurrent change. Start two controlled runs in staging and verify that one waits or fails safely without writing state or modifying resources concurrently.

### D06 — Separate signal from hypothesis

1. Compare latency by revision, endpoint and traffic volume. Confirm the timing and compare a canary or old revision serving similar traffic.
2. Inspect DB query time, execution plans, wait events and connection counts. Check that the new query appears in the slow workload.
3. Check infrastructure changes and unrelated DB load during the same window. Identify whether the symptom persists under comparable load.

Use an agreed performance threshold and observation window, for example abort if p95 remains above 2× baseline for five minutes at comparable traffic. Timing and DB CPU support investigation. The query is a hypothesis. Recovery after rollback strengthens that hypothesis but can also reflect traffic or load changes.

### D07 — Permission scope

Use a dedicated worker identity and grant only the permissions required to start and stop the named VM, plus narrowly scoped read permissions if its implementation needs them. Use the organization’s supported resource-scoped IAM mechanism. Authenticate through an attached identity or short-lived federation, depending on where the worker runs. Remove the broad role and revoke a key if one was created. Verify the identity can start or stop the intended VM in a safe environment, and that another VM or an unrelated admin action is denied. This answer assumes the supported IAM setup stipulated in the exercise.

### D08 — Queue backlog and safe recovery

Early acknowledgement risks permanent loss if the worker crashes before storing the result. Redelivery after the provider succeeds risks a duplicate external action. Persist or reconcile the result durably, then acknowledge. Use a stable operation key for a provider that supports it. Keep a unique local record to coordinate workers and reconcile uncertain outcomes before another send. If the provider lacks idempotency or a way to check results, preserve an uncertain state and define the manual recovery policy. Track age of the oldest unprocessed item and redelivery rate, and compare accepted and completed throughput if available.

## Finance and FP&A drills

### F01 — Operating-profit bridge

Budget profit = `1,000 × (80 − 50) − 20,000 = $10,000`. Actual = `900 × (85 − 52) − 21,000 = $8,700`.

| Effect | Calculation | Favorable/(unfavorable) |
| --- | --- | ---: |
| Volume | (900 − 1,000) × (80 − 50) | ($3,000) |
| Price | (85 − 80) × 900 | $4,500 |
| Variable cost | (50 − 52) × 900 | ($1,800) |
| Fixed cost | 20,000 − 21,000 | ($1,000) |
| Total | 8,700 − 10,000 | **($1,300)** |

### F02 — Working capital and cash

CFO = `120 + 15 − 20 − 12 + 8 = $111k`. Debt principal repayment is a **$25k financing outflow**. Net movement before investing = **+$86k**. The increases in receivables and inventory are operating uses of cash.

### F03 — DCF and terminal value

Year-3 cash flow = `121 × 1.02 = $123.42k`. Year-2 terminal value = `123.42 / (0.10 − 0.02) = $1,542.75k`. Discount year 1 once and year 2 plus the terminal value twice. Enterprise value = `110 / 1.10 + (121 + 1,542.75) / 1.10² = $1,475k`. Equity value = `1,475 − 300 + 40 = $1,215k`. Adding the undiscounted terminal value mixes valuation dates and overstates today's value.

### F04 — Rent roll, NOI and cash

Effective annual rent = `10 × 1,100 × 12 = $132,000`. NOI = `132,000 − 4,400 × 12 = $79,200`. Cash after debt and reserve = `79,200 − 54,000 − 8,000 = $17,200`.

### F05 — Credit headroom

Current DSCR = `260 / 200 = 1.30×`. Minimum compliant NOI is `1.25 × 200 = $250k`. The allowable decline is `$10k / $260k = 3.85%`. A 7% decline gives `260 × 0.93 = $241.8k` and DSCR = `241.8 / 200 = 1.209×`, below the covenant.

### F06 — Reconcile two reports

March GL revenue stays **$232k**. Normalized March revenue is `232 + 10 = $242k`. The comparison is **$2k favorable, or 0.83% above budget**, using $240k as the denominator. The add-back removes the defined February-sale credit memo from the March management comparison and leaves the booked March total as recorded.

### F07 — Run-rate forecast

Base Q4 is `3 × 110 × $1,000 = $330k`. Downside Q4 is `330 × 0.85 = $280.5k`. Full-year base is **$1,230k** and downside is **$1,180.5k**. The downside is **$49.5k lower**, or **4.02% below base**. The scenario changes only the remaining three months. The first nine months are already actual.

### F08 — Cash timing and liquidity

October before financing = `30 + 80 − 92 − 25 = −$7k`. November before financing on the no-draw path = `−7 + 105 − 90 = $8k`. To end October at $10k, draw **$17k**. With no repayment, November cash becomes `10 + 105 − 90 = $25k`.

### F09 — Cohort mix and weighting

Blended conversion = `(80 + 60) / (100 + 300) = 35%`. The segment rates are 80% and 20%. Their 50% simple average is useful as an equal-weight segment statistic, for example for a report intentionally giving each segment equal influence. It does not describe overall conversion per lead here.

### F10 — Three-statement effects

| Year-one change | Amount |
| --- | ---: |
| Net income | ($24k) |
| Cash flow from operations | $0 |
| Cash flow from investing | ($120k) |
| Cash | ($120k) |
| Net PP&E | $96k |
| Retained earnings | ($24k) |

Net income falls by annual depreciation of `120 / 5 = $24k`. The indirect CFO add-back reverses that noncash expense. Assets change by `−120 + 96 = −$24k`, matching equity, with liabilities unchanged.

## Mock scoring

### MG1 — Evidence and verdict · 35 points

- **8** for **both bad**.
- **8** for finding A’s incorrect date with R2.
- **8** for finding B’s unauthorized polishing charge with R3 and R4.
- **8** for confirming Thursday at 11 a.m. and a $170 balance. Approved work is $220 less $50 already paid.
- **3** for a replacement of at most 35 words.

> Unit 31 is confirmed for Thursday at 11 a.m. Your balance is $170 after the $50 deposit. The declined polishing is excluded.

### MG2 — Audit a summary · 35 points

- **8** for scope correction and S3.
- **8** for `72 / 90 = 80%` versus `60 / 90 = 66.67%`, a change of about 13.33 percentage points, and S1–S2.
- **8** for removing the unsupported cause with S4.
- **8** for preserving 12 pending, six failed, and cause under investigation.
- **3** for exactly two update bullets, in the requested order.

Sample corrections. Only the east site reported (S3). Completion rose about 13.33 percentage points (S1, S2). Failure causes are still under investigation (S4).

- East site completion rose from 66.7% to 80%, about 13.3 percentage points (S1–S3).
- Twelve checks are pending and six failed. The failure causes are under investigation (S1, S4).

### MG3 — Follow constrained instructions · 30 points

- **7** for identifying May 18 as a valid day under P1.
- **7** for asking the customer for a preferred date for the inspection.
- **8** for distinguishing separate approval of the $300 line and unverified parts availability.
- **8** for three sentences in order, no guarantee, and at most 65 words.

> Quote Q7 is still valid today, May 18. What date would you prefer for the $120 inspection? The optional $300 item requires separate approval, and parts availability has yet to be confirmed.

### MC1 — Adjacent log events · 35 points

- **12** for using the immediately previous event for each account and updating after every event.
- **6** for inclusive comparison, including equal timestamps.
- **5** for correct output and input order.
- **8** for three meaningful tests with the requested edges.
- **4** for complexity and explanation.

```python
def adjacent_alerts(events, window):
    previous = {}
    alerts = []
    for timestamp, account in events:
        if account in previous and timestamp - previous[account] <= window:
            alerts.append((account, timestamp))
        previous[account] = timestamp
    return alerts

assert adjacent_alerts([], 5) == []
assert adjacent_alerts([(5, "x"), (5, "x")], 0) == [("x", 5)]
assert adjacent_alerts([(1, "a"), (2, "b"), (4, "a"), (6, "b"),
                        (7, "a"), (9, "b")], 3) == [
    ("a", 4), ("a", 7), ("b", 9)
]
```

The last example tests that a nonalert still updates the prior timestamp for `b`. Expected O(n) time and O(u) auxiliary space for u accounts, excluding the output.

### MC2 — Inventory consumption · 35 points

- **10** for accepting only full quantities and decrementing exactly once.
- **7** for rejection with no mutation to available stock.
- **6** for treating missing stock as zero and preserving the inputs.
- **4** for the requested return types and input order.
- **5** for the two required tests.
- **3** for complexity.

```python
def fulfill(stock, requests):
    remaining = stock.copy()
    accepted = []
    for sku, quantity in requests:
        available = remaining.get(sku, 0)
        can_fulfill = quantity <= available
        accepted.append(can_fulfill)
        if can_fulfill:
            remaining[sku] = available - quantity
    return accepted, remaining

source = {"pump": 2}
requests = [("pump", 3), ("pump", 2), ("pump", 1), ("seal", 1)]
assert fulfill(source, requests) == ([False, True, False, False], {"pump": 0})
assert source == {"pump": 2}
assert requests == [("pump", 3), ("pump", 2), ("pump", 1), ("seal", 1)]
assert fulfill({"oil": 1}, [("oil", 1)]) == ([True], {"oil": 0})
assert fulfill({}, []) == ([], {})
```

With s stock keys and r requests, expected time is O(s + r). The returned stock copy and decisions use O(s + r) space, with O(1) additional working space.

### MC3 — Debug and test · 30 points

- **7** for explaining that the strict comparison drops exact-cutoff events.
- **7** for explaining why set iteration does not establish first-seen order.
- **8** for an implementation preserving inclusivity and order.
- **5** for edge tests and a meaningful order check.
- **3** for complexity.

```python
def recent_ids(events, cutoff):
    seen = set()
    result = []
    for timestamp, item_id in events:
        if timestamp >= cutoff and item_id not in seen:
            seen.add(item_id)
            result.append(item_id)
    return result

assert recent_ids([(10, "x")], 10) == ["x"]
assert recent_ids([(11, "b"), (12, "a"), (13, "b")], 10) == ["b", "a"]
assert recent_ids([(11, "a"), (12, "b"), (13, "a")], 10) == ["a", "b"]
```

A single case can accidentally align with the set’s iteration order. Use several permutations and duplicates, and inspect the code to confirm that output order is constructed directly. Expected O(n) time and O(u) space excluding returned values.

### MD1 — Production release · 40 points

- **8** for immutable artifact selection and recording the prior known-good digest, its config version and compatible migration state.
- **14** for an additive field, a backfill and compatible writes across mixed versions, and delaying required-field enforcement or removal until safe.
- **8** for a traffic readiness check that exercises the DB-backed path.
- **10** for a canary or controlled rollout with an observable threshold, a safe rollback step and a verification check.

Example. Build once and deploy by digest. Add `status_code` with a compatible transition, keep `status`, and make writes from both revisions preserve the two representations. Backfill and validate. Canary against staging and production traffic gates, and verify both old and new revisions with a DB-backed request. Pause or revert to the previous digest if the error rate or latency crosses the agreed threshold. Keep the compatible schema and run a smoke test through the load balancer. Store the old digest, deployment config version and migration status. Remove the old column only after retiring old writers and closing or independently securing the rollback window.

### MD2 — Delayed incident · 35 points

- **7** for pausing affected sends or another containment that preserves pending work.
- **7** for correlating rollout, message attempts and provider request IDs to verify duplicate sends.
- **13** for a durable send record, stable idempotency key, reconciliation and acknowledgement after a durable outcome.
- **8** for a test that stops the worker after the provider succeeds but before the local record is finalized, then verifies redelivery causes no second send.

Example. Pause the affected queue consumers or disable the send path without discarding messages. Group the same logical event by queue ID and provider request ID. Confirm whether there were two provider sends. Introduce a unique durable operation record and stable per-event provider key. On retry, reconcile or issue the same keyed call and store its result before acknowledging. In staging, kill the worker in the uncertain window and verify a single provider send and one completed local record after recovery. A code rollback alone may leave messages eligible for redelivery.

### MD3 — Permission and secret review · 25 points

- **5** for identifying broad privileges and token disclosure as separate failures.
- **7** for distinct source-read and destination-write permissions, scoped to the resources and operations actually needed.
- **4** for short-lived CI authentication and no log echo.
- **5** for at least one useful allow and deny test.
- **4** for containing an existing disclosure, revoking or invalidating the credential where possible, and reviewing access.

Example. Use a dedicated federated CI identity. Allow read of the approved artifact and write of the status object. Grant overwrite or listing only if necessary for the workflow. Authenticate with short-lived credentials without printing them. Verify the allowed read and write, and confirm a source write or unrelated object read is denied. If the token was exposed, restrict access to the logs, invalidate the credential where supported, verify expiration or revocation and review use during the exposure window.

### MF1 — FP&A bridge · 40 points

- **8** for the two profits.
- **16** for the four effects, four points each.
- **6** for consistent signs and a bridge tied to the profit change.
- **10** for a two-sentence takeaway using the numbers and leaving the cause of volume decline open.

Budget = `1,200 × (220 − 130) − 70,000 = $38,000`. Actual = `1,050 × (235 − 136) − 72,000 = $31,950`.

| Effect | Calculation | Favorable/(unfavorable) |
| --- | --- | ---: |
| Volume | (1,050 − 1,200) × 90 | ($13,500) |
| Price | (235 − 220) × 1,050 | $15,750 |
| Variable cost | (130 − 136) × 1,050 | ($6,300) |
| Fixed cost | 70,000 − 72,000 | ($2,000) |
| Total | 31,950 − 38,000 | **($6,050)** |

> Operating profit fell $6,050, as lower volume and higher costs outweighed a $15,750 pricing benefit. The records do not establish why volume fell.

### MF2 — Cash and credit · 35 points

- **10** for subtracting all three uses from EBITDA to get **$315k**.
- **8** for `315 / 260 = 1.2115×`, above the 1.20× threshold.
- **8** for required cash of `1.20 × 260 = $312k` and **$3k** headroom.
- **9** for distinguishing the stated cash coverage measure from the model’s EBITDA ratio and describing the cushion accurately.

The draft used `440 / 260 ≈ 1.69×`. That ratio omits cash taxes, maintenance capex, and working-capital absorption. The required measure passes by only $3k.

### MF3 — Valuation review · 25 points

- **6** for using year-3 cash flow of 112.2 and a year-2 terminal value of 1,402.5.
- **6** for discounting terminal value two years.
- **8** for enterprise value and equity value.
- **5** for explaining why net debt is deducted once from enterprise value.

Year-3 cash flow = `110 × 1.02 = 112.2`. Terminal value at year 2 = `112.2 / (0.10 − 0.02) = 1,402.5`. Enterprise value today = `100 / 1.10 + (110 + 1,402.5) / 1.10² = 1,340.91`. Equity value today is **1,120.91**. The unlevered cash flows value the business for all capital providers. Subtract the supplied net debt once to estimate the value attributable to equity holders.

## How to study your results

| If you missed | Do next |
| --- | --- |
| A claim that the source did not establish | Redo G07 and G10. Mark the subject, date, action, authority and what each source can establish. |
| Formatting or requested deliverables | Redo G04 and MG3 with a checklist of exact instructions. Count before submitting. |
| Edge cases or wrong output order | Redo C02 or MC3 from a blank page. Write tests before implementing. |
| A crash or rollback gap | Redo C08, D02 and MD2. Draw the sequence and insert a crash after each durable and external step. |
| Variance signs or a bridge that did not tie | Redo F01 and MF1. Calculate both endpoint profits first. Compare the sum of effects to the full change. |
| Debt, cash or DCF timing | Redo F02, F03 and MF2. Mark each amount’s period, sign, unit, and classification before calculating. |

After the review, answer a fresh exercise in your own words with the key closed. Record the mistake you caught independently and the check that caught it.

## Rapid recall answers

| ID | Recall answer |
| --- | --- |
| R01 | A tentative slot is a possibility that needs confirmation. A confirmed slot may be communicated as booked if no later record changes it. |
| R02 | Unsupported means the available record cannot establish the claim. Contradicted means evidence in the record conflicts with it. |
| R03 | Give the comparative verdict, the decisive evidence, the remaining error and its practical consequence. Use a both-bad option if the rubric allows and both answers fail materially. |
| R04 | You need evidence that distinguishes the proposed cause from credible alternatives, such as a controlled comparison or a design that addresses confounding. |
| R05 | Ask when the missing fact changes the answer or could cause an unauthorized, costly or irreversible action. Make the question as specific as possible. |
| R06 | A later or more authoritative source can still describe a different customer, location or period. Check all three before treating it as decisive. |
| R07 | Use a set to track membership and append each first occurrence to a list. In modern Python a dictionary can also preserve insertion order. |
| R08 | Integer cents preserve exact currency amounts and subtraction in these exercises. Negative rows reduce the total without floating-point representation error. |
| R09 | Put an event exactly at the start and one exactly at the end. The first must count, and the second must be excluded. |
| R10 | Hash lookups avoid a sorting pass under ordinary hash behavior. Sorting can be useful when ordering is required, and the complexity claim should state its assumptions. |
| R11 | Create two candidates with the same primary score but different secondary keys. Arrange input order so a naive first-seen choice gives the wrong result. |
| R12 | An outer WHERE condition on the right-side columns can reject the NULL-extended rows. Use a suitable join condition or preserve those rows explicitly. |
| R13 | Use the previously verified image digest, together with the compatible configuration and schema state. A tag can move. |
| R14 | During a rolling deploy, both revisions can touch the same data. A schema change that breaks one revision can also make rollback ineffective. |
| R15 | Readiness controls whether to route requests to the instance. Liveness helps decide whether to restart a stuck process. |
| R16 | Acknowledge after persisting the outcome or recording a durable resolution that can safely recover the side effect. |
| R17 | Reconcile with the provider using the original operation key or retry under that same idempotency key. Persist the result before treating the job as complete. |
| R18 | Show that it can perform the exact required operation and that an adjacent unauthorized operation is denied. |
| R19 | Budget contribution per unit. Apply price and variable-cost changes to actual units to avoid double-counting with this bridge convention. |
| R20 | An increase uses cash. Under the indirect method, subtract the change. |
| R21 | Use year 3 cash flow in the year-2 terminal value formula and discount that year-2 value two years to today. |
| R22 | Quantify its size against a relevant base or threshold and state how it affects the decision. Some small amounts are material when they cross a covenant or change an action. |
| R23 | It weights segments by the number of eligible observations. Equal weighting answers a different question about the average segment. |
| R24 | Use the definition supplied by the covenant, show the reconciliation, and explain what the model’s alternative ratio leaves out. |

## Second-pass drill solutions

Use the same five-check drill rubric as before. Mark the first assumption or decision that sent your answer in the wrong direction. Then try a fresh problem that shares that underlying rule.

### More Generalist solutions

#### G11 — Effective date

The fee is **$12**. P3 fixes the charge on the order date, August 30. P1 supplies the fee in effect then. Delivery date is irrelevant to this rule.

#### G12 — Valid tie

**Tie.** Each is one sentence, correctly states Tuesday at 2 p.m., and tells the customer to bring a photo ID. Both meet the stated requirements. A stylistic preference has no bearing on the rubric.

#### G13 — Separate extraction from inference

```json
{"caller":"Jordan Lee","time":"14:15","invoice":107,"payment_reported":true,"payment_verified":false}
```

The caller reported payment, and the packet provides no bank confirmation. In this schema, false for verified says verification is absent. It does not determine whether funds were sent. The answer body should contain only the JSON object.

#### G14 — Check a citation’s claim

S1 reports a median, not a universal repair duration, and covers an eight-shop pilot, not the network. S2 is limited to 40 respondents and concerns communication, not repair quality or all customers.

> Across the eight pilot shops, median repair time was four days (S1), and 65% of the 40 survey respondents reported satisfaction with communication (S2).

#### G15 — Write a discriminating prompt

Example original prompt:

> A customer approved a $90 inspection only (R1). The technician later proposed a $240 repair (R2), and the customer has yet to respond (R3). State what the shop may do now and what approval it needs next. Cite the relevant records.

Grading condition. Inspection may proceed. Repair requires approval. The answer must cite the actual authorization or pending record. Plausible failure. “The shop can complete both tasks because the inspection found that repair is necessary.” Necessity is different from authorization.

#### G16 — Unsupported precision

> Delivery is expected two to four business days after shipment. Once the package ships, we can estimate the arrival window from its ship date.

This preserves the service estimate without asserting a date or time. A statement that the package must ship Tuesday adds a fact absent from the packet.

#### G17 — Conflicting sources and escalation

> Hold the order. The signed approval covers up to $400 (S1), and revised parts quotes require written approval (S4). Please confirm in writing whether you authorize the $475 part shown in S2.

S3 reflects an employee impression, which does not meet the written approval rule. No ordering or commitment should occur from this record.

#### G18 — Compare rubric weights

A’s raw total is **9/10** and B’s is **8/10**. **B wins** because A’s fabricated approval triggers the disqualification gate. The rubric specifies that gate regardless of raw total.

### More coding and backend solutions

#### C11 — Rolling sums

```python
def window_totals(values, k):
    if k < 1:
        raise ValueError("k must be positive")
    if k > len(values):
        return []
    total = sum(values[i] for i in range(k))
    result = [total]
    for i in range(k, len(values)):
        total += values[i] - values[i - k]
        result.append(total)
    return result

assert window_totals([-2, 3, -1], 1) == [-2, 3, -1]
assert window_totals([-2, 3, -1], 2) == [1, 2]
assert window_totals([1], 2) == []
try:
    window_totals([], 0)
except ValueError:
    pass
else:
    raise AssertionError("missing validation")
```

O(n) time and O(1) auxiliary space excluding output. Each slide adds the entering value and removes the value k positions back. Re-summing every window would cost O(nk) in the worst case.

#### C12 — Find first occurrence by binary search

```python
def first_index(sorted_ids, target):
    left, right = 0, len(sorted_ids)
    while left < right:
        middle = (left + right) // 2
        if sorted_ids[middle] < target:
            left = middle + 1
        else:
            right = middle
    if left < len(sorted_ids) and sorted_ids[left] == target:
        return left
    return -1

assert first_index([1, 2, 2, 2, 4], 2) == 1
assert first_index([1, 2, 4], 3) == -1
assert first_index([1, 2, 4], 8) == -1
assert first_index([], 1) == -1
```

Find the insertion point before equal values, then check for a match. O(log n) time and O(1) extra space.

#### C13 — Shortest route through dependencies

```python
from collections import deque

def shortest_hops(graph, start, goal):
    pending = deque([(start, 0)])
    seen = {start}
    while pending:
        node, hops = pending.popleft()
        if node == goal:
            return hops
        for neighbor in graph.get(node, ()):
            if neighbor not in seen:
                seen.add(neighbor)
                pending.append((neighbor, hops + 1))
    return -1

graph = {"s": ["a", "b"], "a": ["c"], "c": ["s", "g"], "b": ["g"]}
assert shortest_hops(graph, "s", "g") == 2
assert shortest_hops(graph, "s", "missing") == -1
assert shortest_hops({}, "s", "s") == 0
```

Breadth-first search expands by distance, so it finds a minimum-hop path even when the first listed neighbor is on a longer path. Marking nodes when queued prevents repeated queue entries. O(V + E) time and O(V) extra space for the traversed graph.

#### C14 — Deterministic top-k selection

```python
def ranked_ids(scores, k):
    return sorted(scores, key=lambda item_id: (-scores[item_id], item_id))[:k]

scores = {"c": 3, "b": 3, "a": 3, "d": 5}
assert ranked_ids(scores, 2) == ["d", "a"]
assert ranked_ids(scores, 0) == []
assert ranked_ids(scores, 9) == ["d", "a", "b", "c"]
```

Sorting is O(n log n) time and O(n) space. The negative score makes larger scores come first, and the secondary key resolves the boundary tie.

#### C15 — SQL latest record

```sql
WITH ranked AS (
    SELECT unit_id, event_id, state,
           ROW_NUMBER() OVER (
               PARTITION BY unit_id
               ORDER BY event_at DESC, event_id DESC
           ) AS position
    FROM events
)
SELECT unit_id, event_id, state
FROM ranked
WHERE position = 1
ORDER BY unit_id;
```

If unit U1 has IDs 4 and 5 at the same latest timestamp, both match a join using that timestamp alone. Include an older event and a second unit in the fixture. Only event 5 should win for U1.

#### C16 — Lost update

Both requests read 100 before either writes. Each computes 110 and the second write overwrites the first. Use an atomic relative update:

```sql
UPDATE accounts
SET balance = balance + 10
WHERE id = $1
RETURNING balance;
```

That handles concurrent distinct increments. For retries of the same logical credit, add a unique operation ID and make recording the credit and applying the increment atomic in the same transaction. On retry, return the original result or recorded outcome instead of issuing another credit.

#### C17 — Parse and classify

```python
import re

def parse_counts(lines):
    totals = {}
    invalid = 0
    for line in lines:
        fields = line.split(",")
        if len(fields) != 2:
            invalid += 1
            continue
        label, count = (field.strip() for field in fields)
        if not label or re.fullmatch(r"[+-]?[0-9]{1,9}", count) is None:
            invalid += 1
            continue
        totals[label] = totals.get(label, 0) + int(count)
    return totals, invalid

assert parse_counts([" x , +5 ", "x,-2", "y,3", "z,1,2",
                     "", "x,1.5", "n,1_000", "a,١"]) == ({"x": 3, "y": 3}, 5)
assert parse_counts([" ,3", "x,+", "y,0"]) == ({"y": 0}, 2)
```

ASCII digits are explicit. A bare call to `int` can accept formats beyond this contract. A leading sign without digits is invalid. The nine-digit limit applies to each input amount. Aggregated totals can be larger.

#### C18 — Validate before changing state

With stock `{"a": 2}` and request `("a", -3)`, the draft increases stock to 5. With requests `[("a", 1), ("a", 5)]`, it subtracts one before failing. Validate exact positive integer counts, simulate each request in order on a working copy, and commit the staged stock only after every line is valid and affordable. For a multi-worker database, use one transaction with concurrency control, such as row locks in a consistent order plus conditional updates, or a serializable transaction with retry. Roll back the whole batch on failure. Test a repeated SKU, a late failure and concurrent overlapping batches.

### More DevOps solutions

#### D09 — Unexpected cache behavior

Stop caching authenticated account responses immediately and purge the affected entries. Restrict access to affected logs, preserve evidence needed to determine exposure and review the origin’s authorization. Configure the route to bypass shared caching, including appropriate cache-control headers, and verify at the CDN rather than relying on headers alone. In a controlled test, request the same path as two distinct users and then unauthenticated. Each user sees only authorized data, and the anonymous request is denied. Latency does not identify whose response was served.

#### D10 — Health of a worker

Track live subscription or recent successful poll status, plus completed jobs and oldest queue age when work exists. A heartbeat proves the process can run its heartbeat code. In staging, sever the subscription, enqueue a synthetic job, and verify that the failure alerts and that reconnection or a supervised restart restores consumption. Repeated loss, authorization errors, or lack of progress after reconnect need investigation beyond restarts.

#### D11 — Restore test

The recovery point objective is **at most one hour of data loss**. The recovery time objective is **service restored within two hours**. A nightly backup can be much more than one hour old and a success report does not prove that a backup can be restored. In an isolated environment, simulate loss, start the timer, provision recovery dependencies, restore the backup plus any supported logs to a verified timestamp, and run a representative application transaction. Compare the newest recovered committed data with the incident point. Stop the timer when the service passes its defined recovery check, then report both results.

#### D12 — Change blast radius

Stop or isolate staging consumers without discarding messages. Revoke access to the production queue from the staging identity, preserve evidence of what was consumed and reconcile any in-flight work before replay. Enforce distinct environment configurations and identities, and deny production queue access to staging at the permission boundary. Use synthetic queues or sandbox permission checks to verify staging can reach its test queue and is denied access to a production-scoped test target.

#### D13 — Artifact trust

Build once from a reviewed commit in a dedicated build environment. Pin dependencies and build tools by trusted versions and checksums or digests. Record the immutable artifact digest and provenance, and promote that same artifact after verification. Use a narrowly scoped production deployment identity distinct from the build identity. Verify the deployment references the approved digest and, where configured, trusted provenance or signature. A mutable branch or unverified download breaks the link between review and deployment.

#### D14 — Safe infrastructure change

Create the new endpoint alongside the old one. Test correct HTTPS with the real hostname or equivalent SNI and certificate verification, routes, backend readiness and representative requests before changing DNS. Shift traffic under an observation plan and keep the old endpoint serving. Monitor error rate, latency and traffic by endpoint and DNS behavior. Restore the prior DNS target if the new endpoint misses agreed criteria, then verify service while both endpoints remain available. One TTL is a cache setting. Existing connections, different resolver behavior and earlier higher TTLs can extend the overlap needed.

#### D15 — Capacity versus correctness

Additional workers may raise outbound concurrency, trigger more 429s and increase retry pressure. Start with a bounded canary that reduces provider concurrency or applies rate-aware backoff, leaving the comparison group or baseline clear. Measure successful completions per minute, provider 429 rate and queue age. Improvement means more successful work or lower queue age with fewer rejections, rather than merely fewer attempts.

#### D16 — Secrets across revisions

If allowed, create a second valid credential, publish it through the secret store and deploy or restart a canary that uses it. Verify both versions can connect during overlap, finish rollout, confirm old-credential use has ended, then revoke the old value and test the final path. With one active credential, coordinate a controlled cutover with drained traffic or an agreed maintenance window, preload configuration where possible, and plan recovery. A restart-based app may need a brief service interruption under that constraint.

### More Finance and FP&A solutions

#### F11 — Price sensitivity with mix

A contributes **$45/unit**, B **$60/unit**. Base profit = `100 × 45 + 60 × 60 − 5,000 = $3,100`. Scenario profit = `80 × 45 + 80 × 60 − 5,000 = $3,400`. Mix improves profit by **$300**, or 20 units times the $15 contribution difference. Unit volume is unchanged.

#### F12 — Break-even and operating leverage

Contribution is **$30/unit** and break-even is `24,000 / 30 = 800 units`. At 1,000 units profit is **$6,000**. At 900 units profit is **$3,000**, down **50%**. Fixed cost stays constant, so a 10% volume reduction takes away $3,000 of contribution from a much smaller starting profit.

#### F13 — AR and accruals

Ending gross AR is `50 + 120 − 100 − 5 = $65k`. A write-off against an existing allowance removes an uncollectible balance without receiving cash. Gross AR increased $15k, but `120 − 15 = $105k` would overstate collections by the $5k write-off.

#### F14 — Gross margin denominator

Gross profit is **$180k**. Gross margin is `180 / 480 = 37.5%`. Markup on cost is `180 / 300 = 60%`.

> Gross margin was 37.5% of net sales. The model’s 60% is markup on cost, which uses cost of goods sold as its denominator.

#### F15 — Credit and concentration

Base ratio is `360 / 250 = 1.44×`. The cash floor is `1.25 × 250 = $312.5k`, so base headroom is **$47.5k**. Tenant loss reduces cash to **$270k**, giving **1.08×** coverage and a **$42.5k** shortfall to the floor.

#### F16 — Capital project payback versus NPV

Conventional interpolated payback is `2 + (100 − 90) / 45 ≈ 2.22 years`. NPV in thousands is `−100 + 45 / 1.10 + 45 / 1.10² + 45 / 1.10³ ≈ 11.91`. Actual cumulative cash first exceeds $100k at the **end of year 3**, because the problem places cash at year-end. Interpolation provides a convention, while the actual timing governs liquidity.

#### F17 — Forecast audit and sensitivity

At 5% churn, billed customers = `1,000 + 120 − 50 = 1,070`, giving **$32,100**. At 7% churn, billed customers = `1,000 + 120 − 70 = 1,050`, giving **$31,500**. Revenue falls **$600**. The draft includes new additions in the churn base even though the model defines churn on beginning customers only.

#### F18 — Capex, maintenance and free cash flow

After-tax operating profit = `150 × 0.75 = $112.5k`. Unlevered FCF = `112.5 + 20 − 45 − 12 = $75.5k`. Deducting maintenance capex only gives **$95.5k**, overstating total forecast free cash flow by **$20k**. A maintenance-only measure can be shown separately if labeled.

### Data and ML sampler solutions

#### ML01 — Leakage by time

Eventual follow-up calls occur after the prediction point and can reveal what happened. Exclude that feature. Compute historical features from records available as of each quote’s send time, and use a forward-in-time split so a later period tests an earlier-trained system. Choose a label maturity window so quotes still awaiting outcomes are handled consistently.

#### ML02 — Grouped evaluation

A model or prompt tuned on one paraphrase can benefit from essentially seeing the test scenario during development. Assign every paraphrase of a base scenario to the same split. Audit scenario IDs across splits and search for near-duplicate inputs or common source bundles before publishing scores.

#### ML03 — Confusion matrix

TP = **40**, FP = **40**, FN = **10**, TN = **910**. Precision = `40 / 80 = 50%`, recall = `40 / 50 = 80%`, and accuracy = `(40 + 910) / 1,000 = 95%`. A system that flags nothing also gets 95% accuracy here, while catching zero unauthorized charges.

#### ML04 — Threshold and business costs

A costs `5 × 8 + 40 = 80`. B costs `9 × 8 + 18 = 90`. Select **A** under the stated costs and validation counts, then report performance on a separate test set that did not inform threshold choice. The cost assumption is part of the decision.

#### ML05 — Compare systems fairly

The two sets may differ in difficulty, and using test failures to revise a prompt makes that set part of development. Freeze both prompts, run them on the same fresh held-out cases under the same model and settings, and record paired wins and losses. Predefine a metric such as the proportion of fully correct evidence-supported responses. Keep the final test results out of revision decisions, or use another untouched set for the next final evaluation.

#### ML06 — Model performance by slice

Overall = `182 / 200 = 91%`. Routine = `171 / 180 = 95%`. Safety-critical = `11 / 20 = 55%`.

> The system passed 91% overall, with 95% on routine cases and 55% on the 20 safety-critical cases. The critical failures warrant review, and the small sample leaves production performance uncertain.

## Second mock scoring

### Generalist Mock G2

#### MG21 — Apply a rule hierarchy · 35 points

- **7** for **both bad**.
- **8** for explaining that the operator canceled for weather, so P2 and R1 govern rather than P1.
- **8** for identifying the premature “issued” claim and the excluded fee under P3 and R2.
- **9** for giving $140 as eligible for review and excluding the $12 fee.
- **3** for a response of at most 45 words.

> The operator canceled because of weather, so your $140 rental fee is eligible for refund review. The $12 third-party booking fee is excluded. A refund can be issued after review.

#### MG22 — Edit a claim with multiple denominators · 35 points

- **7** for respondent rate `66 / 88 = 75%`.
- **7** for confirmed reports as a share of starters `66 / 110 = 60%`.
- **7** for confirmed reports as a share of enrollees `66 / 120 = 55%`.
- **8** for explaining that outcomes are missing for nonrespondents and that the design supplies no comparison that supports the causal claim.
- **6** for a two-sentence replacement that conveys the correct scope and leaves causation open.

> At week six, 66 of 88 respondents reported improvement, representing 60% of the 110 starters and 55% of the 120 enrollees. Outcomes for nonrespondents are unknown, and the trial design does not establish that treatment caused the reported changes.

#### MG23 — Preserve structured constraints · 30 points

- **9** for current T2 status, the exact ETA phrase and revised quote approval.
- **7** for treating T1 as closed, with no balance and no further customer action.
- **7** for exact headers, two rows and the correct row order.
- **7** for one sentence of at most 20 words identifying the customer's action.

| Ticket | Current status | Next action |
| --- | --- | --- |
| T2 | Open, ETA unavailable | Approve the revised quote before repairs start |
| T1 | Closed, no balance due | None |

Please approve the revised quote for T2 before repairs begin.

### Coding Mock C2

#### MC21 — Count contiguous totals · 40 points

- **15** for a prefix-sum frequency map, including initialization for sublists starting at index zero.
- **7** for counting previous prefixes before inserting the current prefix and preserving all repeated prefixes.
- **7** for expected O(n) time, O(n) worst-case extra space and explaining why negative values break the usual monotone window rule.
- **8** for the three requested tests.
- **3** for a clear return and solution explanation.

```python
def count_target_ranges(values, target):
    frequencies = {0: 1}
    total = 0
    result = 0
    for value in values:
        total += value
        result += frequencies.get(total - target, 0)
        frequencies[total] = frequencies.get(total, 0) + 1
    return result

assert count_target_ranges([0, 0], 0) == 3
assert count_target_ranges([1, -1, 1], 1) == 3
assert count_target_ranges([], 0) == 0
```

If two prefixes differ by target, their intervening nonempty sublist sums to target. Count earlier occurrences before recording the current prefix. Negatives can shrink a sum when expanding and increase it when shrinking, so window size does not give a reliable decision rule.

#### MC22 — Reachability with layered output · 35 points

- **13** for correct breadth-first traversal and level boundaries.
- **9** for marking on discovery and preserving discovery order.
- **5** for handling the start and missing adjacency lists.
- **5** for a test with a cycle and repeated neighbors.
- **3** for complexity.

```python
from collections import deque

def reachable_by_level(graph, start):
    pending = deque([start])
    seen = {start}
    levels = []
    while pending:
        level = []
        for _ in range(len(pending)):
            node = pending.popleft()
            level.append(node)
            for neighbor in graph.get(node, ()):
                if neighbor not in seen:
                    seen.add(neighbor)
                    pending.append(neighbor)
        levels.append(level)
    return levels

graph = {"s": ["b", "a", "b"], "b": ["s", "d"], "a": ["d", "c"]}
assert reachable_by_level(graph, "s") == [["s"], ["b", "a"], ["d", "c"]]
assert reachable_by_level({}, "isolated") == [["isolated"]]
```

Capture the queue length before iterating a level. Newly queued nodes stay for the next level. Expected O(V + E) time and O(V) additional space in the reachable graph.

#### MC23 — Reviewer’s counterexample · 25 points

- **9** for identifying absolute-value selection, ascending output and input mutation.
- **6** for separate counterexamples to wrong membership and order.
- **7** for a correct implementation supporting short inputs.
- **3** for a nonmutation check.

The draft picks by absolute value and mutates its caller’s list. It returns the slice in ascending absolute-value order. For `[-9, 6, 5, 4]`, the required members are 6, 5 and 4, while the draft includes −9. For `[1, 2, 3, 4]`, the draft returns `[2, 3, 4]` in the wrong order.

```python
def top_three(scores):
    return sorted(scores, reverse=True)[:3]

scores = [-9, 6, 5, 4]
assert top_three(scores) == [6, 5, 4]
assert scores == [-9, 6, 5, 4]
assert top_three([1, 2, 3, 4]) == [4, 3, 2]
assert top_three([-1, -3]) == [-1, -3]
assert top_three([]) == []
```

### DevOps Mock D2

#### MD21 — State safety before a live change · 35 points

- **7** for holding the destructive apply.
- **9** for checking old and new addresses, provider resource ID, workspace, state and plan reasons.
- **10** for a reviewed state move or equivalent declarative address mapping after confirming the same physical database.
- **9** for safe state handling and verifying a fresh plan has no unintended replacement before allowing apply.

Example. Block the apply. Confirm project, environment and database identifier. Compare the old state address with the refactored resource and check which attributes, if any, the plan says force replacement. If only the address changed, use a reviewed declarative move or a controlled state migration with the same backend, normal state locking and a recovery path for state. Replan and check that the physical ID is preserved and no database destroy or create remains. Verify the recovery evidence and obtain normal change approval before a live apply. A backup does not make unnecessary replacement safe.

#### MD22 — Cache and authorization incident · 35 points

- **8** for immediate bypass or disablement of affected caching and purge without unnecessary exposure of records.
- **8** for correlating request and cache metadata, assessing scope and preserving restricted evidence.
- **10** for authenticated cache policy plus per-invoice authorization at the origin.
- **9** for two-user and anonymous tests, with protected diagnostic handling.

Example. Bypass cache for authenticated invoice requests, purge affected entries and restrict access to evidence. Correlate request IDs, times, cache-hit indicators and invoice owner identifiers in the restricted system. Avoid reproducing with real invoice contents or putting them in tickets. At origin, authorize every request against the invoice’s owner or authorized role. In staging, use two synthetic accounts, warm the cache with one, and verify the other and an anonymous request cannot receive its invoice. Check both CDN behavior and direct origin authorization. The incident evidence identifies a likely route, while an origin bug remains possible until tested.

#### MD23 — Queue and provider rate limits · 30 points

- **8** for honoring retry-after with bounded delays, jitter where appropriate, and limiting concurrency.
- **7** for deferring work durably, preserving it across redelivery and using explicit retry or age limits.
- **7** for a stable operation key, reconciliation and a manual-review rule for unresolved or exhausted items.
- **8** for a canary with measured success and a stop criterion.

Example. Respect the provider’s minimum retry-after delay. Schedule retries through a durable mechanism with capped backoff and bounded jitter above the minimum. If the provider’s minimum exceeds the retry budget, defer or escalate without retrying early. Restrict outbound concurrency and acknowledge a queue item only when its outcome or safe deferral is durable. Use the same key for the same operation and reconcile ambiguous results. Send unresolved, exhausted or nonretryable items to the designated review path. Compare successful completions, 429 rate, oldest job age and duplicate effects during a controlled canary. Stop if duplicates appear, the queue age breaches its threshold, or errors materially worsen.

### Finance Mock F2

#### MF21 — Rolling forecast and pricing tradeoff · 35 points

- **8** for both full-year revenues.
- **9** for both Q4 profits and the incremental change.
- **9** for the correct whole-unit threshold and formula.
- **9** for comparing profit and revenue with a clear explanation of the volume and contribution assumptions.

| Measure | Base | Proposed price |
| --- | ---: | ---: |
| Q4 units | 2,000 | 1,760 |
| Q4 revenue | $120,000 | $116,160 |
| Full-year revenue | $1,200,000 | $1,196,160 |
| Q4 operating profit | $20,000 | $24,560 |

Incremental profit is **+$4,560**. New unit contribution is `66 − 35 = $31`. To reach $20,000 after $30,000 fixed cost requires `50,000 / 31 ≈ 1,612.90`, so the minimum is **1,613 units**. The modeled price increase reduces total sales dollars as volume falls, while higher contribution per unit increases profit. The result depends on how customers respond to the price increase.

#### MF22 — Tie accrual profit to cash · 35 points

- **12** for the working-capital signs and CFO.
- **6** for CFI and net CFF.
- **7** for tying to ending cash.
- **10** for recalculating the AP-sign-only case and showing why it does not explain 142.

CFO = `90 + 15 − 35 + 8 − 12 = 66`. CFI = **−40**. CFF = `25 − 18 = 7`. Ending cash = `50 + 66 − 40 + 7 = 83`. Flipping AP from −12 to +12 adds 24. That produces CFO **90** and ending cash **107**, leaving **35** of the reported 142 unexplained by that sign error alone. A second mistake is possible, but its cause is not established.

#### MF23 — Audit a debt metric and communicate it · 30 points

- **8** for calculating base and downside coverage.
- **8** for the correct coverage floor and downside shortfall.
- **6** for minimum EBITDA.
- **8** for a two-sentence recommendation tied to the thin baseline margin and evidence needed to validate the forecast.

Base cash available = `240 − 30 − 20 = 190`, so coverage is **1.267×**. Downside EBITDA is `240 × 0.88 = 211.2`. Downside cash is **161.2**, or **1.075×**. The cash floor is `150 × 1.25 = 187.5`. Downside shortfall is **26.3** and minimum EBITDA is `187.5 + 30 + 20 = 237.5`.

> The base case clears the 1.25× floor by only $2.5k of available cash, and the downside misses it by $26.3k. Before relying on the forecast, confirm the debt-service schedule and test the EBITDA downside using current revenue, margin and customer concentration data.

## Diagnose the second-round misses

| Pattern | Underlying skill | Fresh test to make for yourself |
| --- | --- | --- |
| You used the right fact from the wrong record | Match time, scope and authority before using a fact. | Create two dated notes for different units, then ask for the latest status of only one. |
| Your code solved the usual case and failed a boundary | Put the contract into a counterexample before coding. | Generate lists with duplicates, zeros and one item. Compare your result against a slow, simple reference on small inputs. |
| Your deployment plan ignored what happens in the middle | Review transitions and partial failures. | Put old and new versions side by side and simulate a crash after every write, external action and acknowledgement. |
| Your model tied, but answered the wrong question | Identify the specific decision and metric before calculating. | Compare two scenarios where revenue and profit point in opposite directions. State what assumption drives the gap. |
| Your average score hid a critical failure | Look at slices and hard requirements. | Create a small high-risk slice and report its numerator and denominator beside the aggregate. |
