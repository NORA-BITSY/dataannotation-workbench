"""Offline elapsed-time cues for original practice sessions."""
import argparse
import time

PLANS = {
    "finance": (("Profit and bridge", 25), ("Cash and sources", 15),
                ("Management note", 10), ("Final audit", 5)),
    "technical": (("Implementation and tests", 25), ("Operations decision", 25),
                  ("Final audit", 5)),
    "generalist": (("Read and compare", 8), ("Rationale and rewrite", 9), ("Final audit", 3)),
}


def checkpoints(plan):
    elapsed = 0
    for label, minutes in plan:
        yield elapsed, label
        elapsed += minutes
    yield elapsed, "Stop and save your practice draft"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("track", choices=PLANS)
    parser.add_argument("--run", action="store_true", help="wait and print the cues in real time")
    args = parser.parse_args()
    start = time.monotonic()
    for minute, label in checkpoints(PLANS[args.track]):
        if args.run:
            time.sleep(max(0, start + 60 * minute - time.monotonic()))
        print(f"{minute:02d} min · {label}", flush=True)


if __name__ == "__main__":
    main()
