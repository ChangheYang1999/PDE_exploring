"""Integrity summary of tournament results files.

    .venv/bin/python -B -m bot_research.experiments.lead.check_runs RESULTS.jsonl [...]

Per file: matches, harness errors, rejected actions, bot exceptions, matches whose loaded sources
changed during play, distinct (spec, version) labels of the candidates, slowest decide call.
"""
from __future__ import annotations

import json
import sys


def check(path):
    rows = [json.loads(line) for line in open(path, encoding="utf-8")]
    errors = sum(1 for r in rows if r.get("error"))
    rejected = sum(p.get("n_rejected", 0) for r in rows for p in r.get("players") or [])
    bot_errors = sum(len(p.get("bot_errors") or []) for r in rows for p in r.get("players") or [])
    changed = sum(1 for r in rows if r.get("source_changed"))
    specs, labels = set(), set()
    for r in rows:
        side = r["candidate_side"]
        spec = r["spec_a"] if side == 0 else r["spec_b"]
        specs.add(spec)
        labels.add((spec, r["version_a"] if side == 0 else r["version_b"]))
    slowest = max((max(r["decide_max_seconds"]) for r in rows if r.get("decide_max_seconds")), default=0.0)
    return (f"{path}: {len(rows)} matches, errors {errors}, rejected {rejected}, bot exceptions {bot_errors}, "
            f"source changed {changed}, candidate specs {len(specs)} with {len(labels)} version labels, "
            f"slowest decide {slowest:.2f} s")


def main(argv=None):
    for path in (sys.argv[1:] if argv is None else argv):
        print(check(path))


if __name__ == "__main__":
    main()
