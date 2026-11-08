"""Reproduce the earnings, diagnostics and applied lab checks."""
from collections import Counter
import csv
import json
from pathlib import Path
import re
import runpy
import shutil
import subprocess
import sys
from tempfile import TemporaryDirectory

from earnings import load, run, summarize

ROOT = Path(__file__).resolve().parents[1]


def verify_recheck():
    roles = ROOT / "data/roles"
    baseline = {
        row["role_id"]: row
        for row in (json.loads(line) for line in
                    (roles / "role_register.jsonl").read_text(encoding="utf-8").splitlines())
    }
    delta = load(roles / "board-recheck-2026-11-07.json")
    assert delta["counts"]["baseline"] == len(baseline)
    assert delta["counts"]["public_board"] == (
        len(baseline) + len(delta["added"]) - len(delta["removed"])
    )
    routes = load(roles / "shortlist-routes-2026-11-07.json")["public_apply_links"]
    assert len(routes) == len({row["role_id"] for row in routes}) == 11
    for row in routes:
        old = baseline[row["role_id"]]
        assert row["previous_public_projects_parameter"] == old["public_signup_projects_parameter"]
        assert row["listing_url"] == old["posting_url"]
        assert row["confirmed_account_track"] is None
    assert set(delta["shortlist_route_changes"]) == {
        row["role_id"] for row in routes
        if row["previous_public_projects_parameter"] != row["public_projects_parameter"]
    }


def verify_earnings():
    folder = ROOT / "data/earnings"
    result = run(load(folder / "assumptions.json"))
    assert result == load(folder / "example-output.json")
    zero, earlier, later, delayed = [row["runs"] for row in result["scenarios"]]
    assert zero[0]["hypothetical_earned_usd"] == "0.00" and zero[0]["total_hours"] == "6.75"
    assert earlier[0]["hypothetical_earned_usd"] == "315.00"
    assert earlier[0]["projected_cash_cleared_usd"] == "0.00"
    assert earlier[1]["hypothetical_earned_usd"] == "1035.00"
    assert earlier[1]["projected_cash_cleared_usd"] == "720.00"
    assert later[1]["hypothetical_earned_usd"] == "1200.00"
    assert delayed[1]["hypothetical_earned_usd"] == "900.00"
    empty = dict(days=dict.fromkeys(("assessment", "approval", "first_available", "first_completed")),
                 time_blocks=[])
    assert summarize(empty, 30)["effective_pre_tax_usd_per_total_hour"] is None
    assert all(row["approved_earnings_usd"] is None and row["actual_cash_received_usd"] is None
               for scenario in result["scenarios"] for row in scenario["runs"])
    with (folder / "personal-tracker-template.csv").open(encoding="utf-8", newline="") as f:
        assert not list(csv.DictReader(f))


def verify_study_expansion():
    study = ROOT / "study"
    key = (study / "evaluator/diagnostic-key.md").read_text(encoding="utf-8")
    pattern = r"^## ((?:FIN|TECH|GEN)-[ABC]) ·"
    diagnostic_ids = set()
    for path in sorted((study / "diagnostics").glob("*.md")):
        body = path.read_text(encoding="utf-8")
        assert "evaluator/" not in body and "answer-key" not in body
        forms = re.findall(pattern, body, re.M)
        assert not (set(forms) & diagnostic_ids)
        diagnostic_ids.update(forms)
    assert diagnostic_ids == {
        prefix + "-" + suffix for prefix in ("FIN", "TECH", "GEN")
        for suffix in ("AB" if prefix == "GEN" else "ABC")
    }
    for form in diagnostic_ids:
        assert f"**{form}.**" in key
    tables = re.findall(r"\| Criterion \| Points \|\n(.*?)\| Total \| (\d+) \|", key, re.S)
    assert len(tables) == 3
    for table, total in tables:
        assert sum(map(int, re.findall(r"\|\s*(\d+)(?:, [^|]+)?\s*\|", table))) == int(total) == 100
    workbook = (study / "workbook.md").read_text(encoding="utf-8")
    workbook_ids = set(re.findall(r"^#{3,4} ((?:M[GCDF](?:2)?[1-3]|(?:[GCDF]|ML)\d{2})) —",
                                  workbook, re.M))
    with (study / "skill-index.csv").open(encoding="utf-8", newline="") as f:
        index = list(csv.DictReader(f))
    counts = Counter(row["exercise_id"] for row in index)
    assert set(counts) == workbook_ids | diagnostic_ids
    assert set(counts.values()) == {1} and len(index) == 108
    assert all(row["known_trap"] and (ROOT / row["packet"]).is_file() for row in index)
    runpy.run_path(str(study / "evaluator/diagnostic-reference.py"), run_name="__main__")
    for lane, minutes in (("finance", 55), ("technical", 55), ("generalist", 20)):
        proc = subprocess.run([sys.executable, str(ROOT / "scripts/practice_timer.py"), lane],
                              check=True, capture_output=True, text=True)
        assert proc.stdout.splitlines()[-1].startswith(f"{minutes:02d} min")


def verify_labs():
    evaluator = ROOT / "study/evaluator"
    finance = runpy.run_path(str(evaluator / "finance-lab-reference.py"))
    result = finance["calculate"](ROOT / "examples/finance-forecast/source-records.csv")
    assert (result["oct_budget"], result["oct_actual"], result["delta"]) == (7200, 6440, -760)
    assert sum(result["bridge"].values()) == result["oct_actual"] - result["oct_budget"]
    assert result["minimum_cash"] == 18000
    expected = [(6850, -7000, 15000, 3000), (3365, -13000, 9000, 9000)]
    for index, scenario in enumerate(("nov_base", "nov_downside")):
        output = result["forecast"][scenario]
        assert tuple(output.values()) == expected[index]
        assert output["ending_cash"] == 22000 + output["net_cash_movement"]
        assert output["ending_cash"] + output["funding_needed"] == result["minimum_cash"]
    release = ROOT / "examples/technical-release"
    command = [sys.executable, "-B", "-m", "unittest", "-q"]
    baseline = subprocess.run(command, cwd=release, capture_output=True, text=True)
    assert baseline.returncode == 1 and "FAILED (failures=5)" in baseline.stderr
    with TemporaryDirectory(prefix="release-reference-") as directory:
        scratch = Path(directory)
        shutil.copyfile(release / "test_release_gate.py", scratch / "test_release_gate.py")
        shutil.copyfile(evaluator / "technical-release-reference.py", scratch / "release_gate.py")
        fixed = subprocess.run(command, cwd=scratch, capture_output=True, text=True)
        assert fixed.returncode == 0 and "Ran 5 tests" in fixed.stderr, fixed.stderr


def verify_work_order():
    verify_recheck()
    verify_earnings()
    verify_study_expansion()
    verify_labs()
    print("Work order verified. 11 routes, 108 study index entries, 8 diagnostics, both labs and earnings scenarios.")


if __name__ == "__main__":
    verify_work_order()
