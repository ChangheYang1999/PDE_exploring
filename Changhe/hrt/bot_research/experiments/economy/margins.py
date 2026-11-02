"""Mean HP difference per candidate and opponent (both seats), as a table.

Usage: python3 margins.py RESULTS.jsonl [SUBSTRING ...]
Rows: opponents whose spec contains one of the substrings (all if none given);
columns: candidates in order of first appearance. Cell: mean candidate HP
minus opponent HP over the matches of that pairing (both seats), clipped to
+-800 per match, with the number of matches if it is not 2.
"""
from __future__ import annotations

import json
import sys
from collections import defaultdict

from summarize import short


def main():
    path, subs = sys.argv[1], sys.argv[2:]
    cells = defaultdict(list)
    cands, opps = [], []
    for line in open(path):
        r = json.loads(line)
        if r.get("error"):
            continue
        side = r["candidate_side"]
        c = short(r["spec_a"] if side == 0 else r["spec_b"])
        o = short(r["spec_b"] if side == 0 else r["spec_a"])
        if r.get("scenario"):
            c += " [" + r["scenario"] + "]"
        d = r["hp_diff_a"] if side == 0 else -r["hp_diff_a"]
        cells[(c, o)].append(max(-800, min(800, d)))
        if c not in cands:
            cands.append(c)
        if o not in opps and (not subs or any(s in o for s in subs)):
            opps.append(o)
    print("| opponent | " + " | ".join(f"c{i}" for i in range(len(cands))) + " |")
    print("| --- |" + " ---: |" * len(cands))
    for o in opps:
        row = []
        for c in cands:
            v = cells.get((c, o), [])
            row.append("" if not v else f"{sum(v) / len(v):+.0f}" + ("" if len(v) == 2 else f" ({len(v)})"))
        print(f"| {o} | " + " | ".join(row) + " |")
    for i, c in enumerate(cands):
        print(f"c{i} = {c}")


if __name__ == "__main__":
    main()
