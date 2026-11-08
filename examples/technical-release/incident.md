# Fictional release evidence

| ID | Record |
| --- | --- |
| R1 | 09:02 CI pushed `registry/service:stable`. The deploy log recorded the previous known-good digest separately. |
| R2 | 09:03 a migration removed the column the previous image needs to write. The next schema change has not been designed. |
| R3 | 09:04 TCP probe connected. The authenticated, DB-backed smoke test returned 503. |
| R4 | 09:05 canary p95 was 460 ms and error rate was 1.5%. Baseline p95 was 160 ms. |
| R5 | Policy requires a recoverable previous revision, an immutable candidate and passing representative traffic checks before promotion. |

The proposed response is to promote because TCP is healthy and the error rate is below 2%, then redeploy `stable` if necessary. Decide from the contract and evidence.
