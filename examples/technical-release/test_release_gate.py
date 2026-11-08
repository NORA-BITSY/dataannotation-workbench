import unittest
from release_gate import evaluate


def observation(**overrides):
    return {
        "artifact": "sha256:" + "a" * 64,
        "previous_schema_compatible": True,
        "db_status": 200,
        "tcp_healthy": True,
        "error_pct": 2,
        "p95_ms": 400,
        **overrides,
    }


class ReleaseGateTests(unittest.TestCase):
    def test_inclusive_thresholds(self):
        self.assertEqual(evaluate(observation()), ("promote", []))

    def test_block_each_regression(self):
        for kwargs in ({"error_pct": 2.01}, {"p95_ms": 401}):
            with self.subTest(kwargs=kwargs):
                self.assertEqual(evaluate(observation(**kwargs)),
                                 ("hold", ["canary_regression"]))

    def test_tcp_success_is_insufficient(self):
        self.assertEqual(evaluate(observation(db_status=503)), ("hold", ["not_ready"]))

    def test_report_all_reasons_in_order(self):
        self.assertEqual(evaluate(observation(
            artifact="registry/service:stable", previous_schema_compatible=False,
            db_status=503, p95_ms=460)), ("hold", [
                "mutable_artifact", "rollback_incompatible", "not_ready", "canary_regression"
            ]))

    def test_digest_must_be_exact(self):
        self.assertEqual(evaluate(observation(artifact="sha256:" + "Z" * 64)),
                         ("hold", ["mutable_artifact"]))
