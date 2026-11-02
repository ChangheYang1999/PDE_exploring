"""Markdown table of W-D-L (engine winner) and worst HP difference per candidate and pool.
Usage: python3 tmp/pool_table.py LABEL=RUNDIR[,RUNDIR...] ... -- SUFFIX=NAME ...
Run directories are relative to bot_research/runs/lead; several directories under one label are pooled.
The first matching suffix names a candidate (list the longest first). Candidates appear in suffix order."""
import json, sys
from collections import defaultdict
from pathlib import Path

RUNS = Path(__file__).resolve().parent.parent / "runs" / "lead"
i = sys.argv.index("--")
pools = [a.split("=", 1) for a in sys.argv[1:i]]
names = [a.rsplit("=", 1) for a in sys.argv[i + 1:]]
order = []
for _, n in names:
    if n not in order:
        order.append(n)


def cname(c):
    for suf, n in names:
        if c.endswith(suf):
            return n
    return None


table = {}
for label, dirs in pools:
    agg = defaultdict(lambda: [0, 0, 0, 10**9])
    for d in dirs.split(","):
        p = RUNS / d / "results.jsonl"
        if not p.exists():
            continue
        for line in p.open():
            if not line.strip():
                continue
            r = json.loads(line)
            cs = r["candidate_side"]
            n = cname(r["spec_a"] if cs == 0 else r["spec_b"])
            if n is None:
                continue
            dd = r["hp_diff_a"] * (1 if cs == 0 else -1)
            w = r["winner"]
            k = 0 if w == cs else (2 if w == 1 - cs else 1)
            a = agg[n]
            a[k] += 1
            a[3] = min(a[3], dd)
    table[label] = agg

print("| Pool (runs) | " + " | ".join(order) + " |")
print("| --- |" + " ---: |" * len(order))
for label, dirs in pools:
    cells = []
    for n in order:
        a = table[label].get(n)
        cells.append(f"{a[0]}-{a[1]}-{a[2]} ({a[3]:+d})" if a else "")
    print(f"| {label} ({dirs}) | " + " | ".join(cells) + " |")
