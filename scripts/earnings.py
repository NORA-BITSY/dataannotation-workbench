"""Model hypothetical contractor earnings without assigning admission odds."""
import argparse
from collections import defaultdict
from decimal import Decimal, ROUND_HALF_UP
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ZERO = Decimal(0)


def money(value):
    return str(value.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP))


def quantity(value):
    number = Decimal(str(value))
    if not number.is_finite() or number < 0:
        raise ValueError("Rates, hours, and direct costs must be finite and nonnegative")
    return number


def summarize(scenario, horizon):
    """Sum day-level assumptions, reporting projected cash only after its lag."""
    stages = scenario["days"]
    named_days = ("assessment", "approval", "first_available", "first_completed")
    known = [stages[key] for key in named_days if stages[key] is not None]
    if any(type(day) is not int or day < 1 for day in known) or known != sorted(known):
        raise ValueError("Known milestones must be positive and ordered")
    if any(stages[key] is None and any(stages[other] is not None for other in named_days[i + 1:])
           for i, key in enumerate(named_days)):
        raise ValueError("A later milestone requires the earlier milestones")
    paid = earned = cash = costs = ZERO
    hours = defaultdict(lambda: ZERO)
    payment_day = None
    first_paid = None
    for entry in scenario["time_blocks"]:
        first, last = entry["from_day"], entry["through_day"]
        if type(first) is not int or type(last) is not int or not 1 <= first <= last:
            raise ValueError("Invalid day range")
        duration = quantity(entry["hours_per_day"])
        rate = quantity(entry.get("rate", 0))
        lag = entry.get("cash_lag_days", 0)
        if type(lag) is not int or lag < 0:
            raise ValueError("Cash lag must be a nonnegative integer")
        category = entry["category"]
        if category not in {"study", "onboarding", "qualification", "queue", "paid_task", "unpaid_rework"}:
            raise ValueError(f"Unknown time category: {category}")
        if category != "paid_task" and rate:
            raise ValueError("Only paid_task blocks have a modeled rate")
        if category == "paid_task" and duration and (stages["first_completed"] is None or
                                                      first < stages["first_completed"]):
            raise ValueError("Paid hours precede the first completed assignment")
        for day in range(first, min(last, horizon) + 1):
            hours[category] += duration
            if category == "paid_task":
                paid += duration
                earned += duration * rate
                if duration:
                    first_paid = day if first_paid is None else min(first_paid, day)
                if duration and rate and day + lag <= horizon:
                    cash += duration * rate
                    payment_day = day + lag if payment_day is None else min(payment_day, day + lag)
    for cost in scenario.get("direct_costs", []):
        if type(cost["day"]) is not int or cost["day"] < 1:
            raise ValueError("Invalid cost date")
        amount = quantity(cost["amount"])
        if cost["day"] <= horizon:
            costs += amount
    total = sum(hours.values(), ZERO)
    return {
        "horizon_days": horizon,
        "milestones_within_horizon": {
            **{key: stages[key] if stages[key] is not None and stages[key] <= horizon else None
               for key in named_days},
            "first_modeled_paid_hours": first_paid,
            "first_projected_cleared_payment": payment_day,
        },
        "time_hours": {key: money(amount) for key, amount in sorted(hours.items())},
        "paid_hours": money(paid),
        "total_hours": money(total),
        "paid_share": money(100 * paid / total) if total else None,
        "hypothetical_earned_usd": money(earned),
        "approved_earnings_usd": None,
        "projected_cash_cleared_usd": money(cash),
        "actual_cash_received_usd": None,
        "direct_costs_usd": money(costs),
        "effective_pre_tax_usd_per_total_hour": money((earned - costs) / total) if total else None,
    }


def load(path):
    return json.loads(path.read_text(encoding="utf-8"))


def run(config):
    return {
        "kind": "hypothetical, no probabilities or projected assignment access",
        "scenarios": [
            {"name": scenario["name"], "runs": [summarize(scenario, horizon) for horizon in (14, 30)]}
            for scenario in config["scenarios"]
        ],
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("assumptions", nargs="?", type=Path,
                        default=ROOT / "data/earnings/assumptions.json")
    args = parser.parse_args()
    print(json.dumps(run(load(args.assumptions)), indent=2))
