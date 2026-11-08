# Coding and DevOps diagnostic · v1

Take one form in 55 minutes. Allow 25 minutes to implement and test, 25 for the release or incident review, and five to check the instructions. For practice, use Python 3, a plain editor and your own local tests. Submit the function, test cases, time and space complexity, and an operations note with decision, evidence, safe action and verification. The systems and records are fictional.

## TECH-A · Retry-safe payment reconciliation

Implement `net_by_customer(events)`. Events are ordered triples of unique-event ID, customer ID and signed integer cents. An event can recur identically after a retry. Count the first occurrence of each event ID once. Return a dictionary of net cents by customer, including zero totals. Leave input unchanged. Test retry, refund and a zero balance.

**Operations packet.** At 10:00 the new worker starts sending booking confirmations. At 10:08 customers report duplicates. A log shows that an external provider returned success before the worker crashed and the queue redelivered. The provider supports a stable idempotency key. The new image tag is mutable. Give a containment step that preserves queued work, the safe recovery design, and a test for the crash window. Explain how you would identify the previous artifact before reverting.

## TECH-B · Incident streaks and readiness

Implement `streak_alerts(events, threshold)`. Events are sorted by timestamp and contain `(time, account, succeeded)`, where `succeeded` is Boolean and `threshold` is a positive integer. Emit `(time, account)` at exactly the first event where an account reaches the threshold of consecutive failures. Later failures in the same streak emit nothing. A success resets only that account. Preserve input order. Test interleaving, a long streak and a reset that allows a second alert.

**Operations packet.** TCP probes turn green after four seconds. A representative database-backed request returns 503 for 30 seconds. The proposed change makes the database query a liveness check. The prior image digest is recorded. Decide whether to continue rollout. Give a readiness and liveness design, a smoke test through the traffic path, and a rollback trigger with observable evidence.

## TECH-C · Latest event and migration

Implement `latest_state(events)`. Events contain `(entity, event_time, event_id, state)`; time and ID are integers. Return a mapping of entity to state from the maximum `(event_time, event_id)` per entity. If those two fields both tie, duplicate rows are identical. Input order is arbitrary. Preserve the input. Test stale events, a tied timestamp and two independent entities.

**Operations packet.** In a rolling release the new application needs `display_name`. The old revision still reads and writes `name`. The draft migration renames the column before deploying the first new instance. The production policy requires keeping rollback available throughout the rollout. State whether to proceed, give a safe sequence with compatibility writes, and describe an old/new read-write test and a criterion for removing the old column.
