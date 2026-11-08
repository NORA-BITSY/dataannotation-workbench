"""Evaluator-only reference implementation for the release lab."""
import re


def evaluate(observation):
    reasons = []
    if re.fullmatch(r"sha256:[0-9a-f]{64}", observation["artifact"]) is None:
        reasons.append("mutable_artifact")
    if not observation["previous_schema_compatible"]:
        reasons.append("rollback_incompatible")
    if observation["db_status"] != 200:
        reasons.append("not_ready")
    if observation["error_pct"] > 2 or observation["p95_ms"] > 400:
        reasons.append("canary_regression")
    return ("hold" if reasons else "promote"), reasons
