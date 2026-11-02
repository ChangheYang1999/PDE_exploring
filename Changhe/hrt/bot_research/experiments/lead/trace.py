"""Per-round trace of a match log (both players).

    .venv/bin/python -B -m bot_research.experiments.lead.trace LOG [--rounds 1-20]

Columns per player: HP after the round, gold after, factories, splash/gun counts,
per-copy splash S and route length L after construction, purchases this round
(f = factories, s = splashes, g = guns, w = walls, minions by tier digit), and
base damage taken this round.
"""
from __future__ import annotations

import argparse
import json
from collections import Counter

from bot_research.harness import gamekit as gk


def load(path):
    rounds = {}
    rules = None
    with open(path, encoding="utf-8") as stream:
        for line in stream:
            rec = json.loads(line)
            if rec.get("round") == 0 and rules is None and "match" in rec:
                rules = rec["match"]["rules"]
            rounds.setdefault(rec["round"], {})[rec["player"]] = rec
    return rules, rounds


def summary(rec, rules_obj):
    snap = rec["snapshot"]
    buys = Counter()
    for e in rec["event"]:
        if e["kind"] != "action" or not e["accepted"]:
            continue
        a = e["action"]
        if a["op"] == "buy_factory":
            buys["f"] += 1
        elif a["op"] == "build_wall":
            buys["w"] += 1
        elif a["op"] == "build_turret":
            buys["s" if a["type"] == "splash" else "g" + a["type"][-1]] += 1
        elif a["op"] == "buy_minion":
            buys["t" + a["type"][-1]] += 1
    combat = next((e for e in rec["event"] if e["kind"] == "combat"), {})
    b = snap["buildings"]
    path = gk.route_cached(gk.cells_of(b))
    S = gk.splash_total(path, b, rules_obj)
    n_s = sum(1 for x in b if x["type"] == "splash")
    n_g = sum(1 for x in b if x["type"].startswith("gun"))
    buy = " ".join(f"{k}{v}" for k, v in sorted(buys.items()) if k not in ("w",)) or "-"
    return (f"hp {snap['hp']:4d} g {snap['gold']:6d} F {snap['n_factories']:4d} s{n_s:2d} g{n_g:2d} "
            f"S {S:4d} L {len(path) - 1:3d} dmg {combat.get('base_damage', 0):4d} | {buy}")


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("log")
    ap.add_argument("--rounds", default="1-20")
    args = ap.parse_args(argv)
    lo, hi = (int(x) for x in args.rounds.split("-"))
    rules, rounds = load(args.log)
    obs_like = {"rules": rules}
    rules_obj = gk.Rules.from_observation(obs_like)
    names = [rounds[0][p]["snapshot"]["name"] for p in (0, 1)]
    print("A:", names[0])
    print("B:", names[1])
    for r in range(lo, hi + 1):
        if r not in rounds:
            break
        print(f"r{r:2d} A {summary(rounds[r][0], rules_obj)}")
        print(f"    B {summary(rounds[r][1], rules_obj)}")


if __name__ == "__main__":
    main()
