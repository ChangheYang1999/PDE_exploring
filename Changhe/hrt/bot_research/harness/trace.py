"""Round-by-round trace of an authoritative match log (for loss review).

    python -B -m bot_research.harness.trace LOG [--rounds 1-12]

Per round and player: HP after the round, gold after income, factories, turrets,
walls, route length, per-copy splash damage S of the map after construction,
gold spent by category this round, base damage taken and hits scored.
"""
from __future__ import annotations

import argparse
import json
from collections import Counter

from bot_research.harness import gamekit as gk


def trace(path, lo=1, hi=10 ** 9):
    with open(path, encoding="utf-8") as stream:
        records = [json.loads(line) for line in stream]
    rules = None
    for rec in records:
        if rec.get("kind") == "match_start" or "config" in rec:
            pass
    rows = []
    by_round = {}
    for rec in records:
        if "round" in rec and "player" in rec:
            by_round.setdefault(rec["round"], {})[rec["player"]] = rec
    for r in sorted(by_round):
        if not lo <= r <= hi:
            continue
        line = [f"r{r:02d}"]
        for p in (0, 1):
            rec = by_round[r][p]
            snap = rec["snapshot"]
            spent = Counter()
            dmg = hits = 0
            for ev in rec["event"]:
                if ev["kind"] == "action" and ev["accepted"]:
                    a = ev["action"]
                    key = {"buy_factory": "F", "build_wall": "W"}.get(a["op"]) or (
                        a["type"][0] + a["type"][-1] if a["op"] == "buy_minion" else a["type"][:2] + a["type"][-1])
                    spent[key] += ev.get("cost", 0)
                elif ev["kind"] == "combat":
                    dmg, hits = ev["base_damage"], ev["outgoing_hits"]
            b = snap["buildings"]
            blocked = gk.cells_of(b)
            route = gk.route(blocked)
            splash = sum(1 for x in b if x["type"] == "splash")
            adj = 0
            idx = set(route[:-1])
            for x in b:
                if x["type"] == "splash":
                    adj += sum(1 for n in gk.neighbors8((x["x"], x["y"])) if n in idx)
            sp = " ".join(f"{k}{v}" for k, v in sorted(spent.items()))
            line.append(f"| hp {snap['hp']:>6} g {snap['gold']:>7} F {snap['n_factories']:>4} sp {splash:>2} S {adj*10:>5} "
                        f"L {snap['length_path']:>2} took {dmg:>4} hit {hits:>3} [{sp}]")
        rows.append(" ".join(line))
    return rows


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("log")
    ap.add_argument("--rounds", default="1-50")
    a = ap.parse_args(argv)
    lo, _, hi = a.rounds.partition("-")
    for row in trace(a.log, int(lo), int(hi or lo)):
        print(row)


if __name__ == "__main__":
    main()
