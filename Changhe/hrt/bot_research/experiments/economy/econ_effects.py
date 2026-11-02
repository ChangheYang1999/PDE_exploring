"""HP and economy effects per match, from a tournament results.jsonl with kept logs.

Usage: python3 econ_effects.py RESULTS.jsonl [round]   (default round 10)
Per match (candidate's view): seat, final HP difference, both players' HP after
rounds 1, 2, 5 and ``round``, and factories and gold in the end-of-round
snapshot of ``round``. Then means per candidate x opponent over both seats.
"""
from __future__ import annotations

import json
import os
import sys
from collections import defaultdict

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))


def short(spec):
    mod, _, rest = spec.partition(":")
    parts = mod.split(".")
    name = ".".join(parts[-2:]) if "frozen" in parts else parts[-1]
    return name + ":" + rest.replace("@", "").replace('"', "")


def snapshots(log):
    out = {}
    for line in open(os.path.join(ROOT, log)):
        d = json.loads(line)
        s = d.get("snapshot")
        if s:
            out[(d["round"], d["player"])] = s
    return out


def main():
    path = sys.argv[1]
    R = int(sys.argv[2]) if len(sys.argv) > 2 else 10
    agg = defaultdict(list)
    print("cand | opp | seat | hp_diff | hp me/opp after r1, r2, r5, rR | fac me/opp rR | gold me/opp rR")
    for line in open(path):
        r = json.loads(line)
        if r.get("error") or not r.get("log"):
            continue
        side = r["candidate_side"]
        cand = short(r["spec_a"] if side == 0 else r["spec_b"])
        opp = short(r["spec_b"] if side == 0 else r["spec_a"])
        diff = r["hp_diff_a"] if side == 0 else -r["hp_diff_a"]
        snap = snapshots(r["log"])

        def get(rnd, who, key):
            s = snap.get((rnd, who))
            return s[key] if s else None

        me, op = side, 1 - side
        hp = [(get(k, me, "hp"), get(k, op, "hp")) for k in (1, 2, 5, R)]
        fac = (get(R, me, "n_factories"), get(R, op, "n_factories"))
        gold = (get(R, me, "gold"), get(R, op, "gold"))
        print(f"{cand} | {opp} | {side} | {diff} | {hp} | {fac} | {gold}")
        agg[(cand, opp)].append((diff, fac, gold))
    print("\nmeans over seats: cand | opp | n | hp_diff | fac me/opp | gold me/opp")
    for (cand, opp), rows in agg.items():
        n = len(rows)
        m = lambda f: sum(f(x) or 0 for x in rows) / n
        print(f"{cand} | {opp} | {n} | {m(lambda x: x[0]):.1f} | "
              f"{m(lambda x: x[1][0]):.0f}/{m(lambda x: x[1][1]):.0f} | "
              f"{m(lambda x: x[2][0]):.0f}/{m(lambda x: x[2][1]):.0f}")


if __name__ == "__main__":
    main()
