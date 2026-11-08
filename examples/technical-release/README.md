# Applied lab · Release admission and rollback · v1

**Practice time** 70 minutes. Use Python 3, a local editor, and the fictional [incident record](incident.md). There is no remote deployment and no third-party dependency.

## Assignment

1. Run the tests against the supplied implementation. Record which failures establish the largest safety problem.
2. Repair `release_gate.py` and add one boundary test of your own. Preserve the given interface and reason order. This exercise models a decision only.
3. Write a release decision with the evidence from the incident, a safe rollback or hold decision, and a verification step through the real traffic path. Separate what the log proves from a hypothesis. Explain what should happen if the database cannot support the previous image.
4. Submit the patch, the before and after test result, and a decision note of at most 200 words.

Run from this directory:

```sh
python3 -m unittest -v
```

## Contract

`evaluate(observation)` returns a tuple of a decision string and a list of blocking reasons, in the order below. All documented fields are present and have the types shown in the tests. Promote only if every condition passes.

| Check | Blocking reason |
| --- | --- |
| Candidate artifact is an immutable lowercase digest matching `sha256:` plus 64 hex characters. | `mutable_artifact` |
| The old application can still read and write the current schema. | `rollback_incompatible` |
| The representative DB-backed request returns exactly HTTP 200. | `not_ready` |
| Error rate is at most 2% and p95 is at most 400 ms. Rates in code are percentages, so 2 means 2%. | `canary_regression` |

Use `promote` with an empty reason list if all checks pass. Otherwise return `hold` and every applicable reason. A TCP probe is useful evidence that the port opens. The contract deliberately uses a DB-backed request for traffic readiness.
