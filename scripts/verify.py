"""Verify the role snapshot, practice materials, and synthetic exports."""
from collections import Counter
import json
from pathlib import Path
import re
import subprocess
import sys
from tempfile import TemporaryDirectory

from verify_work_order import verify_work_order

ROOT = Path(__file__).resolve().parents[1]


def require(condition, message):
    if not condition:
        raise ValueError(message)


def read_jsonl(path):
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines()]


def verify_roles():
    folder = ROOT / "data/roles"
    rows = read_jsonl(folder / "role_register.jsonl")
    summary = json.loads((folder / "role_register_summary.json").read_text(encoding="utf-8"))
    require(len(rows) == len({row["role_id"] for row in rows}) == summary["public_role_count"],
            "Role counts or unique IDs do not match")
    require(Counter(row["role_family"] for row in rows) == summary["families"],
            "Role family counts do not match")
    require(all(row["checked_on"] == summary["checked_on"] for row in rows),
            "Role snapshot dates do not match")
    print(f"{len(rows)} unique roles across {len(summary['families'])} families.")


def verify_study():
    workbook = (ROOT / "study/workbook.md").read_text(encoding="utf-8")
    key = (ROOT / "study/answer-key.md").read_text(encoding="utf-8")
    exercise = r"^#{3,4} ((?:M[GCDF](?:2)?[1-3]|(?:[GCDF]|ML)\d{2})) —"
    questions = Counter(re.findall(exercise, workbook, re.MULTILINE))
    answers = Counter(re.findall(exercise, key, re.MULTILINE))
    require(questions == answers and questions and max(questions.values()) == 1,
            "Each exercise must have one prompt and one answer")
    recall = r"^\| (R\d{2}) \|"
    require(Counter(re.findall(recall, workbook, re.MULTILINE)) ==
            Counter(re.findall(recall, key, re.MULTILINE)), "Recall cards do not match")
    header = r"^#{3,4} (M[GCDF](?:2)?[1-3])[^\n]*? · (\d+) points[^\n]*\n"
    breakdown = header + r"(.*?)(?=^#{2,4} |\Z)"
    stated_points = dict(re.findall(header, workbook, re.MULTILINE))
    mock_points = Counter()
    graded = set()
    for exercise_id, points, body in re.findall(breakdown, key, re.MULTILINE | re.DOTALL):
        parts = re.findall(r"^- \*\*(\d+)\*\*", body, re.MULTILINE)
        require(stated_points.get(exercise_id) == points and sum(map(int, parts)) == int(points),
                f"Rubric points do not match for {exercise_id}")
        mock_points[exercise_id[:-1]] += int(points)
        graded.add(exercise_id)
    require(graded == stated_points.keys() and mock_points and set(mock_points.values()) == {100},
            "Mock score coverage or 100-point totals do not match")
    blocks = re.findall(r"```python\n(.*?)\n```", key, re.DOTALL)
    for index, block in enumerate(blocks, 1):
        exec(compile(block, f"study/answer-key.md example {index}", "exec"), {})
    print(f"{len(questions)} matched exercises, {len(mock_points)} mocks, {len(blocks)} Python examples.")


def verify_boatable():
    example = ROOT / "examples/boatable"
    original = example / "synthetic"
    with TemporaryDirectory(prefix="dataannotation-check-") as temp:
        rebuilt = Path(temp)
        subprocess.run([sys.executable, str(example / "build_and_score.py"), "--out", temp],
                       check=True)
        require({path.name for path in rebuilt.iterdir()} ==
                {path.name for path in original.iterdir()}, "Synthetic export inventory changed")
        for path in original.iterdir():
            require(path.read_bytes() == (rebuilt / path.name).read_bytes(),
                    f"Generated output differs for {path.name}")
    print("Synthetic exports are byte-identical to a fresh run.")


if __name__ == "__main__":
    verify_roles()
    verify_study()
    verify_boatable()
    verify_work_order()
