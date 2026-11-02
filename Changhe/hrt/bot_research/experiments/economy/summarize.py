"""Candidate x opponent matrix from a tournament results.jsonl.

Usage: python3 summarize.py RESULTS.jsonl [--short]
Each cell: W-D-L over both seats, then mean candidate HP diff. Rows with a
scripted-opening scenario are kept apart: the opponent label gets the suffix
" @scenario" so standard starts and scenarios are never pooled.
"""
from __future__ import annotations

import json
import sys
from collections import defaultdict


def short(spec):
    mod, _, rest = spec.partition(":")
    parts = mod.split(".")
    name = ".".join(parts[-2:]) if "frozen" in parts else parts[-1]
    return name + ":" + rest.replace("@", "").replace('"', "")


def main():
    path = sys.argv[1]
    rows = [json.loads(line) for line in open(path)]
    cell = defaultdict(lambda: [0, 0, 0, 0.0, 0, 0])
    cands, opps = [], []
    errors = 0
    for r in rows:
        if r.get("error"):
            errors += 1
            continue
        side = r["candidate_side"]
        cand = r["spec_a"] if side == 0 else r["spec_b"]
        opp = r["spec_b"] if side == 0 else r["spec_a"]
        if r.get("scenario"):
            opp += " @" + r["scenario"]
        if cand not in cands:
            cands.append(cand)
        if opp not in opps:
            opps.append(opp)
        c = cell[(cand, opp)]
        if r["winner"] is None:
            c[1] += 1
        elif r["winner"] == side:
            c[0] += 1
        else:
            c[2] += 1
        diff = r["hp_diff_a"] if side == 0 else -r["hp_diff_a"]
        c[3] += diff
        c[4] += 1
        c[5] += sum(len(p.get("bot_errors", [])) for p in r["players"][side:side + 1])
    print(f"rows={len(rows)} harness_errors={errors}")
    for ci, cand in enumerate(cands):
        tw = td = tl = 0
        print(f"\n[{ci}] {short(cand)}")
        for opp in opps:
            w, d, l, s, n, be = cell[(cand, opp)]
            tw += w
            td += d
            tl += l
            flag = "" if l == 0 else "  <-- loss"
            err = f" boterr={be}" if be else ""
            print(f"    {short(opp):55s} {w}-{d}-{l}  {s / max(1, n):8.1f}{err}{flag}")
        print(f"    TOTAL {tw}-{td}-{tl}")


if __name__ == "__main__":
    main()
