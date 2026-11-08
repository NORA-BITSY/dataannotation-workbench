"""Deliberately flawed implementation supplied to learners."""


def evaluate(observation):
    if observation["tcp_healthy"] and observation["error_pct"] <= 2:
        return "promote", []
    return "hold", ["not_ready"]
