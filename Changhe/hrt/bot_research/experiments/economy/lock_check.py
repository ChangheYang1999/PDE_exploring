"""Per-copy splash damage of the candidate's map over a match (kept logs of a tournament).

Usage (from the project root): .venv/bin/python -B -m bot_research.experiments.economy.lock_check RESULTS.jsonl
For every match with a kept log: candidate, opponent, seat, HP difference, the
first round whose end-of-round map has per-copy splash damage (gamekit.splash_total
on the engine route) of at least 1500 (the tier5 HP; '-' if never), the final
per-copy splash damage, and the number of empty cells left on the final map.
"""
from __future__ import annotations

import json
import os
import sys

from bot_research.harness import gamekit as gk
from td_game.config import balanced_config
from td_game.engine import Engine

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))


def main():
    rules = gk.Rules.from_observation(Engine(balanced_config(), ("A", "B")).observation(0))
    for line in open(sys.argv[1]):
        r = json.loads(line)
        if not r.get("log"):
            continue
        side = r["candidate_side"]
        cand = r["spec_a"] if side == 0 else r["spec_b"]
        opp = r["spec_b"] if side == 0 else r["spec_a"]
        diff = r["hp_diff_a"] if side == 0 else -r["hp_diff_a"]
        first, last, empty = None, 0, None
        for ln in open(os.path.join(ROOT, r["log"])):
            d = json.loads(ln)
            s = d.get("snapshot")
            if not s or d.get("player") != side:
                continue
            b = s["buildings"]
            blocked = {(x["x"], x["y"]) for x in b}
            path = gk.route_cached(frozenset(blocked)) if False else gk.route(blocked)
            last = gk.splash_total(path, b, rules)
            empty = 144 - len(blocked) - len(path)
            if first is None and last >= 1500:
                first = d["round"]
        print(f"{cand.split(':', 1)[1][:60]} | {opp.split('.')[-1][:50]} | {side} | {diff} | "
              f"{first if first is not None else '-'} | {last} | {empty}")


if __name__ == "__main__":
    main()
