"""Build and score the synthetic Boatable case pack with Python 3."""
import argparse
from collections import Counter
from hashlib import sha256
import json
from pathlib import Path

VERSION = "1.0"
POLICY = {
    "id": "POL",
    "rules": [
        "Bill only explicitly approved line items. Use the quoted integer cents.",
        "Cite both the quote and the approval for every billed line.",
        "If any required item lacks approval, hold for approval.",
        "Otherwise, hold for scheduling if the requested slot is unavailable.",
        "Otherwise, mark the quote ready. Cite the policy, any required unresolved approvals, and any supplied slot record.",
    ],
}
PROMPT = (
    "Reconcile this fictional marine service quote. Follow POL. "
    "Return JSON with lines (id, cents, evidence), total_cents, decision "
    "(quote_ready, hold_for_approval, or hold_for_scheduling), and decision_evidence."
)
CRITERIA = {
    "format": "Complete, typed JSON with unique line IDs and evidence lists.",
    "arithmetic": "Total equals the sum of billed integer cents.",
    "traceability": "Every billed amount agrees with its quote. Every evidence ID exists and matches its line.",
    "authorization": "Only approved lines appear.",
    "coverage": "Every approved line appears exactly once.",
    "decision": "The release or hold status and its citations agree with the records.",
}

# Each tuple includes independently specified reference line IDs and status.
# Each scenario has its own source bundle and template group.
SPECS = [
    ("Q01", "quote", "development", "outboard-diagnostic", [
        ("diag", "Outboard diagnostic", 14500, "approved", True),
        ("plug", "Spark plug set", 4800, "approved", False),
        ("flush", "Optional flush", 8200, "pending", False)], None, ["diag", "plug"], "quote_ready"),
    ("Q02", "quote", "development", "haulout-reconciliation", [
        ("haul", "Haul out", 26000, "approved", True),
        ("rinse", "Hull rinse", 9500, "approved", False),
        ("paint", "Bottom paint", 19500, "declined", False)], None, ["haul", "rinse"], "quote_ready"),
    ("Q03", "quote", "heldout", "electrical-reconciliation", [
        ("test", "Battery load test", 7200, "approved", True),
        ("cable", "Terminal cable", 4600, "approved", False),
        ("battery", "Battery replacement", 21900, "declined", False)], None, ["test", "cable"], "quote_ready"),
    ("Q04", "quote", "heldout", "winterization-reconciliation", [
        ("winter", "Winterization", 23500, "approved", True),
        ("oil", "Oil and filter", 11200, "approved", False),
        ("wrap", "Shrink wrap", 37000, "pending", False)], None, ["winter", "oil"], "quote_ready"),
    ("C01", "scope_change", "development", "pump-change-hold", [
        ("inspect", "Bilge inspection", 6900, "approved", False),
        ("pump", "Replace failed bilge pump", 18500, "pending", True),
        ("alarm", "Optional alarm", 5300, "declined", False)], None, ["inspect"], "hold_for_approval"),
    ("C02", "scope_change", "development", "trailer-change-accepted", [
        ("service", "Trailer service", 10000, "approved", True),
        ("bearing", "Wheel bearing change order", 9400, "approved", False),
        ("jack", "Optional jack", 12800, "pending", False)], None, ["service", "bearing"], "quote_ready"),
    ("C03", "scope_change", "heldout", "seacock-revocation", [
        ("survey", "Through-hull inspection", 12500, "approved", False),
        ("valve", "Seacock change order", 29700, "revoked", True),
        ("hose", "Optional hose", 6100, "approved", False)], None, ["survey", "hose"], "hold_for_approval"),
    ("C04", "scope_change", "heldout", "canopy-alternate-approval", [
        ("patch", "Canvas patch", 11000, "approved", True),
        ("zip", "Zipper change order", 7400, "approved", False),
        ("new", "Full replacement alternative", 52000, "declined", False)], None, ["patch", "zip"], "quote_ready"),
    ("S01", "scheduling", "development", "crane-slot-blocked", [
        ("crane", "Crane reservation", 31500, "approved", True),
        ("stand", "Optional storage stand", 7200, "pending", False)], ("2026-11-18T10:00", False), ["crane"], "hold_for_scheduling"),
    ("S02", "scheduling", "development", "electronics-slot-cleared", [
        ("install", "Electronics installation", 27500, "approved", True),
        ("chart", "Optional chart update", 3800, "declined", False)], ("2026-11-19T09:00", True), ["install"], "quote_ready"),
    ("S03", "scheduling", "heldout", "engine-slot-and-approval", [
        ("inspect", "Engine inspection", 11800, "approved", False),
        ("seal", "Required seal replacement", 13200, "pending", True)], ("2026-11-20T14:30", False), ["inspect"], "hold_for_approval"),
    ("S04", "scheduling", "heldout", "survey-slot-moved", [
        ("survey", "Pre-purchase survey", 51000, "approved", True),
        ("travel", "Travel charge", 8400, "approved", False),
        ("lab", "Optional lab test", 5400, "pending", False)], ("2026-11-23T11:15", False), ["survey", "travel"], "hold_for_scheduling"),
]


def make_case(spec):
    case_id, family, split, scenario, items, slot, wanted, decision = spec
    docs = [POLICY]
    for item_id, label, cents, approval, required in items:
        docs.append({"id": f"Q-{item_id}", "kind": "quote", "line_id": item_id,
                     "description": label, "cents": cents, "required": required})
        docs.append({"id": f"A-{item_id}", "kind": "approval", "line_id": item_id, "state": approval})
    if slot is not None:
        docs.append({"id": "SLOT", "kind": "slot", "requested_local_time": slot[0], "available": slot[1]})
    manifest = [
        {"id": doc["id"], "origin": "original_synthetic",
         "rights": "original fictional project material",
         "sha256": sha256(json.dumps(doc, sort_keys=True, ensure_ascii=False).encode()).hexdigest()}
        for doc in docs
    ]
    case = {"case_id": case_id, "version": VERSION, "family": family, "split": split,
            "scenario_group": scenario, "prompt": PROMPT, "source_manifest": manifest, "documents": docs}
    amounts = {item[0]: item[2] for item in items}
    lines = [{"id": x, "cents": amounts[x], "evidence": [f"Q-{x}", f"A-{x}"]} for x in wanted]
    decision_refs = ["POL"] + [f"A-{x[0]}" for x in items if x[4] and x[3] != "approved"]
    if slot is not None:
        decision_refs.append("SLOT")
    answer = {"lines": lines, "total_cents": sum(x["cents"] for x in lines),
              "decision": decision, "decision_evidence": decision_refs}
    return case, answer


def strings(values):
    return isinstance(values, list) and all(isinstance(value, str) and value for value in values)


def valid_answer(answer):
    if not isinstance(answer, dict):
        return False
    if type(answer.get("total_cents")) is not int or answer["total_cents"] < 0:
        return False
    if not isinstance(answer.get("decision"), str) or not strings(answer.get("decision_evidence")):
        return False
    rows = answer.get("lines")
    if not isinstance(rows, list) or any(
        not isinstance(row, dict) or not isinstance(row.get("id"), str) or not row["id"]
        or type(row.get("cents")) is not int or row["cents"] < 0 or not strings(row.get("evidence"))
        for row in rows
    ):
        return False
    return len({row["id"] for row in rows}) == len(rows)


def invalid_reason(case):
    docs = case.get("documents")
    if not isinstance(case.get("prompt"), str) or case["prompt"] != PROMPT:
        return "missing or unrecognized task instructions"
    if not isinstance(docs, list) or any(
        not isinstance(doc, dict) or not isinstance(doc.get("id"), str) for doc in docs
    ):
        return "missing or malformed source records"
    if len({doc["id"] for doc in docs}) != len(docs) or POLICY not in docs:
        return "duplicate records or missing applicable policy"
    quotes = [doc for doc in docs if doc.get("kind") == "quote"]
    approvals = [doc for doc in docs if doc.get("kind") == "approval"]
    slots = [doc for doc in docs if doc.get("kind") == "slot"]
    if any(
        not isinstance(doc.get("line_id"), str)
        or type(doc.get("cents")) is not int or doc["cents"] < 0
        or type(doc.get("required")) is not bool for doc in quotes
    ) or any(
        not isinstance(doc.get("line_id"), str)
        or doc.get("state") not in ("approved", "pending", "declined", "revoked")
        for doc in approvals
    ):
        return "malformed quote or approval"
    quote_ids = {doc["line_id"] for doc in quotes}
    approval_ids = {doc["line_id"] for doc in approvals}
    if not quotes or len(quote_ids) != len(quotes) or len(approval_ids) != len(approvals) or quote_ids != approval_ids:
        return "missing or conflicting line evidence"
    if len(slots) > 1 or any(type(slot.get("available")) is not bool for slot in slots):
        return "missing or conflicting slot status"
    return None


def evaluate(case, answer):
    """Return per-criterion booleans for a valid case; reject invalid cases."""
    if reason := invalid_reason(case):
        raise ValueError(f"invalid_record: {reason}")
    if not valid_answer(answer):
        return dict.fromkeys(CRITERIA, False)
    docs = case["documents"]
    quotes = {d["line_id"]: d for d in docs if d.get("kind") == "quote"}
    approvals = {d["line_id"]: d for d in docs if d.get("kind") == "approval"}
    slot = next((d for d in docs if d.get("kind") == "slot"), None)
    expected = {x for x, record in approvals.items() if record["state"] == "approved"}
    missing_required = {x for x, q in quotes.items() if q["required"] and x not in expected}
    if missing_required:
        decision = "hold_for_approval"
    elif slot and not slot["available"]:
        decision = "hold_for_scheduling"
    else:
        decision = "quote_ready"
    decision_refs = {"POL", *(approvals[x]["id"] for x in missing_required)}
    if slot:
        decision_refs.add(slot["id"])
    lines = answer["lines"]
    listed = {row["id"] for row in lines}
    return {
        "format": True,
        "arithmetic": sum(row["cents"] for row in lines) == answer["total_cents"],
        "traceability": all(
            (i := row["id"]) in quotes and row["cents"] == quotes[i]["cents"]
            and set(row["evidence"]) == {quotes[i]["id"], approvals[i]["id"]}
            for row in lines
        ),
        "authorization": listed <= expected,
        "coverage": expected <= listed,
        "decision": answer["decision"] == decision and set(answer["decision_evidence"]) == decision_refs,
    }


def make_flawed(case, answer):
    wrong = json.loads(json.dumps(answer))
    family = case["family"]
    if family == "quote":
        wrong["total_cents"] += 199
        return wrong, "arithmetic"
    if family == "scheduling":
        wrong["decision"] = "quote_ready" if answer["decision"] != "quote_ready" else "hold_for_scheduling"
        return wrong, "decision"
    docs = case["documents"]
    unapproved = next(d for d in docs if d.get("kind") == "approval" and d["state"] != "approved")
    line_id = unapproved["line_id"]
    quoted = next(d for d in docs if d["id"] == f"Q-{line_id}")
    wrong["lines"].append({"id": line_id, "cents": quoted["cents"], "evidence": [quoted["id"], unapproved["id"]]})
    wrong["total_cents"] += quoted["cents"]
    return wrong, "authorization"


def jsonl(path, rows):
    path.write_text("".join(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n" for row in rows), encoding="utf-8")


def build(directory):
    directory.mkdir(parents=True, exist_ok=True)
    cases, evaluator, demos, pairs, tests, responses, reviews = [], [], [], [], [], [], []
    records = [make_case(spec) for spec in SPECS]
    assert len({case["case_id"] for case, _ in records}) == 12
    assert len({case["scenario_group"] for case, _ in records}) == 12
    assert Counter((case["family"], case["split"]) for case, _ in records) == {
        (family, split): 2 for family in ("quote", "scope_change", "scheduling") for split in ("development", "heldout")
    }
    # Review three development cases with different failure families before export.
    pilot_ids = {"Q01", "C01", "S01"}
    for case, reference in sorted(records, key=lambda pair: pair[0]["case_id"] not in pilot_ids):
        wrong, intended = make_flawed(case, reference)
        good_score, bad_score = evaluate(case, reference), evaluate(case, wrong)
        assert all(good_score.values()) and not bad_score[intended], case["case_id"]
        case_id = case["case_id"]
        reference_id = f"{case_id}:{VERSION}:reference"
        control_id = f"{case_id}:{VERSION}:control"
        for response_id, response, kind in (
            (reference_id, reference, "author_reference"),
            (control_id, wrong, "programmatic_seeded_control"),
        ):
            responses.append({"case_id": case_id, "version": VERSION, "response_id": response_id,
                              "producer": kind, "tool": "build_and_score.py", "model": None,
                              "answer": response})
        reviews.append({
            "case_id": case_id, "version": VERSION, "review_id": f"{case_id}:{VERSION}:review",
            "reviewer": "author_single_reviewer", "review_status": "single_reviewer_verified",
            "reference_response_id": reference_id, "control_response_id": control_id,
            "preference": "reference", "reason": CRITERIA[intended], "adjudication": None,
            "pilot_review": case_id in pilot_ids,
        })
        cases.append(case)
        evaluator.append({"case_id": case["case_id"], "version": VERSION, "reference": reference,
                          "control": wrong, "intended_failure": intended, "criteria": CRITERIA,
                          "review_status": "single_reviewer_verified",
                          "reviewer": "author_single_reviewer", "pilot_review": case["case_id"] in pilot_ids})
        tests.append({"case_id": case["case_id"], "split": case["split"], "reference": good_score,
                      "control": bad_score, "intended_failure": intended,
                      "reference_response_id": reference_id, "control_response_id": control_id})
        if case["split"] == "development":
            model_input = {"prompt": case["prompt"], "documents": case["documents"]}
            demos.append({"case_id": case["case_id"], "input": model_input, "output": reference})
            pairs.append({"case_id": case["case_id"], "input": model_input, "chosen": reference, "rejected": wrong,
                          "judgment": {"label": "chosen", "reason": CRITERIA[intended],
                                       "provenance": "author_labeled_synthetic_control"}})
    first, valid = records[0]
    forged = json.loads(json.dumps(valid))
    forged["lines"][0]["evidence"] = ["INVENTED", "ALSO-INVENTED"]
    assert not evaluate(first, forged)["traceability"]
    omitted = json.loads(json.dumps(valid))
    omitted["total_cents"] -= omitted["lines"].pop()["cents"]
    assert evaluate(first, omitted)["arithmetic"] and not evaluate(first, omitted)["coverage"]
    duplicate = json.loads(json.dumps(valid))
    duplicate["lines"].append(duplicate["lines"][0])
    assert not evaluate(first, duplicate)["format"]
    assert not evaluate(first, {"lines": [None]})["format"]
    incomplete = {**first, "documents": [doc for doc in first["documents"] if doc["id"] != "A-diag"]}
    assert invalid_reason(incomplete) == "missing or conflicting line evidence"
    assert invalid_reason({**first, "prompt": "Unclear instructions."}) == "missing or unrecognized task instructions"
    assert invalid_reason({**first, "documents": first["documents"] + [first["documents"][1]]}) == (
        "duplicate records or missing applicable policy"
    )
    holdout = [{k: c[k] for k in ("case_id", "version", "prompt", "documents")} for c in cases if c["split"] == "heldout"]
    assert not {r["case_id"] for r in holdout} & {r["case_id"] for r in demos}
    assert not any({"reference", "criteria", "control"} & set(x) for x in holdout)
    jsonl(directory / "cases.jsonl", sorted(cases, key=lambda c: c["case_id"]))
    jsonl(directory / "evaluator_only.jsonl", sorted(evaluator, key=lambda c: c["case_id"]))
    jsonl(directory / "responses_evaluator_only.jsonl", sorted(responses, key=lambda r: r["response_id"]))
    jsonl(directory / "reviews_evaluator_only.jsonl", sorted(reviews, key=lambda r: r["review_id"]))
    jsonl(directory / "demonstrations.jsonl", sorted(demos, key=lambda c: c["case_id"]))
    jsonl(directory / "preferences.jsonl", sorted(pairs, key=lambda c: c["case_id"]))
    jsonl(directory / "heldout_inputs.jsonl", sorted(holdout, key=lambda c: c["case_id"]))
    report = {
        "run_id": f"boatable-{VERSION}-deterministic-controls",
        "dataset_version": VERSION, "cases": len(cases), "development": len(demos), "heldout": len(holdout),
        "references_passing": sum(all(t["reference"].values()) for t in tests),
        "controls_caught": sum(not t["control"][t["intended_failure"]] for t in tests),
        "additional_regression_checks": ["forged evidence", "omitted approved line", "duplicate line", "malformed response"],
        "invalid_record_checks": ["missing approval source", "unrecognized instructions", "duplicate source"],
        "model_inference": "not_run", "model_weight_updates": "not_run",
        "review_mode": "single_reviewer", "pilot_ids": sorted(pilot_ids),
        "per_case": sorted(tests, key=lambda t: t["case_id"]),
    }
    (directory / "score_report.json").write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(f"{report['cases']} cases. {report['references_passing']} references passed. "
          f"{report['controls_caught']} seeded errors caught. Four answer regressions and three invalid-record checks passed.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=Path, default=Path("synthetic"))
    build(parser.parse_args().out)
