"""Early attacks against the growth gap, from kept tournament logs (hrt-w2 analysis).

Usage: python3 attack_growth.py RESULTS.jsonl [CAND_SUBSTRING] [last_round]   (from the project root)
For each kept log of a candidate whose spec contains CAND_SUBSTRING: every round 2..last_round (default 10) in
which the candidate bought minions, with the factory counts and gold of both players at the end of the previous
round (the state the candidate observed), the attack's cost, and the final HP difference of the match.
"""
from __future__ import annotations

import ast
import json
import sys


def main():
    path = sys.argv[1]
    sub = sys.argv[2] if len(sys.argv) > 2 else ""
    last = int(sys.argv[3]) if len(sys.argv) > 3 else 10
    for line in open(path):
        r = json.loads(line)
        side = r["candidate_side"]
        cand = r["spec_a"] if side == 0 else r["spec_b"]
        if sub not in cand or not r.get("log"):
            continue
        opp = (r["spec_b"] if side == 0 else r["spec_a"]).split(".")[-1][:40]
        diff = r["hp_diff_a"] if side == 0 else -r["hp_diff_a"]
        snap, ev = {}, {}
        for l in open(r["log"]):
            d = json.loads(l)
            if "round" not in d or "player" not in d:
                continue
            if d.get("snapshot"):
                snap[(d["round"], d["player"])] = d["snapshot"]
            e = d.get("event")
            if isinstance(e, str):
                e = ast.literal_eval(e)
            if isinstance(e, list):
                ev[(d["round"], d["player"])] = e
        rows = []
        for rnd in range(2, last + 1):
            acts = ev.get((rnd, side), [])
            att = sum(a.get("cost", 0) for a in acts
                      if a.get("accepted") and a.get("action", {}).get("op") == "buy_minion")
            if not att:
                continue
            me, op = snap.get((rnd - 1, side)), snap.get((rnd - 1, 1 - side))
            if not me or not op:
                continue
            rows.append(f"r{rnd}:att{att} f{me['n_factories']}/{op['n_factories']} g{me['gold']}/{op['gold']}")
        print(f"{r.get('scenario') or 'std'} | {opp} | {side} | {diff} | " + "; ".join(rows))


if __name__ == "__main__":
    main()
