# Earnings and time scenarios

From the repository root:

```sh
python3 scripts/earnings.py
python3 scripts/earnings.py /path/to/your-local-assumptions.json
```

See the [editable assumptions](../../data/earnings/assumptions.json) and [reproduced output](../../data/earnings/example-output.json). A day range is inclusive. Enter hours per day for each category, and ensure blocks represent separate hours. Day 1 is the decision to begin preparation. A projected payment lag is a modeling choice. Project terms and actual payout status determine cash in practice.

| Illustrative path | Day 14 earned / projected cash | Day 30 earned / projected cash | Day 30 effective rate |
| --- | ---: | ---: | ---: |
| No work available | $0 / $0 | $0 / $0 | $0.00 per total hour |
| Earlier start | $315 / $0 | $1,035 / $720 | $32.70 per total hour |
| Later specialist start | $0 / $0 | $1,200 / $675 | $39.47 per total hour |
| Later specialist delayed four more days | $0 / $0 | $900 / $375 | $34.09 per total hour |

These values use fictional rates and one paid hour per eligible day. The specialist case earns $165 more by day 30 but has $45 less projected cash cleared. An additional three-day delay at one $75 paid hour per day reduces earned dollars to $975, below the earlier path's $1,035. With the four-day delay, effective rate is still slightly higher because fewer paid hours were worked, while both earnings and cleared cash are lower. Set the decision criterion explicitly when comparing paths.

For the same eventual number of paid hours, a hypothetical $180 in displaced earnings at a $30 per-hour rate spread would take six paid hours at the higher rate to recover. This shortcut assumes comparable hours and costs. Use the cumulative runs when start dates, paid hours or cash timing differ.

Approved earnings and actual cash are unknown in scenario mode. Use a local copy of the [empty tracker](../../data/earnings/personal-tracker-template.csv) once you have real data. Enter each time block once. Record approved amounts and deposits in separate events, avoid counting the same payout twice, and keep project/customer details out of the tracker. Calculate realized approved effective rate as approved earnings less attributable direct costs divided by total invested hours for the matching work period. Use cleared cash separately for spending decisions. Leave a zero denominator blank. [Contractor terms](https://app.dataannotation.tech/contract/280)
