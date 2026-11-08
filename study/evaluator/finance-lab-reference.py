"""Evaluator-only calculation for the original finance lab."""
import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def calculate(path):
    with path.open(encoding="utf-8", newline="") as f:
        records = {(r["period"], r["metric"]): int(r["value"])
                   for r in csv.DictReader(f) if r["status"] == "authoritative"}

    def inputs(period, fields):
        return (records[period, field] for field in fields)

    def profit(units, price, cost, fixed):
        return units * (price - cost) - fixed

    fields = ("units", "price_per_unit", "variable_per_unit", "fixed")
    bu, bp, bc, bf = inputs("oct_budget", fields)
    au, ap, ac, af = inputs("oct_actual", fields)
    budget, actual = profit(bu, bp, bc, bf), profit(au, ap, ac, af)
    bridge = {"volume": (au - bu) * (bp - bc), "price": (ap - bp) * au,
              "variable_cost": (bc - ac) * au, "fixed": bf - af}

    price, unit_cost, fixed = inputs("nov_both", fields[1:])
    start, operating, capex, floor = inputs(
        "nov_both", ("opening_cash", "cash_operating_payments", "capex", "minimum_cash")
    )
    forecast = {}
    for name in ("nov_base", "nov_downside"):
        units, collections = inputs(name, ("units", "collections"))
        net_move = collections - operating - capex
        ending = start + net_move
        forecast[name] = {
            "operating_profit": profit(units, price, unit_cost, fixed),
            "net_cash_movement": net_move, "ending_cash": ending,
            "funding_needed": max(0, floor - ending),
        }
    return {"oct_budget": budget, "oct_actual": actual, "delta": actual - budget,
            "bridge": bridge, "forecast": forecast, "minimum_cash": floor}


if __name__ == "__main__":
    print(json.dumps(calculate(ROOT / "examples/finance-forecast/source-records.csv"), indent=2))
