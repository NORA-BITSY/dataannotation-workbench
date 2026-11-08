"""Original reference functions for TECH-A, TECH-B and TECH-C."""


def net_by_customer(events):
    totals = {}
    seen = set()
    for event_id, customer_id, cents in events:
        if event_id not in seen:
            seen.add(event_id)
            totals[customer_id] = totals.get(customer_id, 0) + cents
    return totals


def streak_alerts(events, threshold):
    result = []
    failures = {}
    for timestamp, account, succeeded in events:
        if succeeded:
            failures.pop(account, None)
        else:
            failures[account] = failures.get(account, 0) + 1
            if failures[account] == threshold:
                result.append((timestamp, account))
    return result


def latest_state(events):
    latest = {}
    for entity, timestamp, event_id, state in events:
        marker = (timestamp, event_id)
        if entity not in latest or marker > latest[entity][0]:
            latest[entity] = (marker, state)
    return {entity: record[1] for entity, record in latest.items()}


if __name__ == "__main__":
    events = [(1, "a", 100), (1, "a", 100), (2, "a", -100), (3, "b", 20)]
    assert net_by_customer(events) == {"a": 0, "b": 20}
    assert len(events) == 4
    assert net_by_customer([]) == {}
    events = [(1, "a", False), (2, "b", False), (3, "a", False),
              (4, "a", False), (5, "b", True), (6, "a", True),
              (7, "a", False), (8, "b", False), (9, "a", False)]
    assert streak_alerts(events, 2) == [(3, "a"), (9, "a")]
    assert streak_alerts([(1, "a", False), (2, "a", False)], 1) == [(1, "a")]
    assert streak_alerts([], 2) == []
    states = [("a", 3, 3, "hold"), ("a", 2, 9, "wait"), ("b", 1, 1, "open"),
              ("a", 3, 1, "closed"), ("a", 3, 3, "hold")]
    assert latest_state(states) == {"a": "hold", "b": "open"}
    assert latest_state([]) == {}
