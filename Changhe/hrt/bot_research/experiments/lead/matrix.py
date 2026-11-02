"""Compact candidate x opponent table of mean HP difference (candidate view) from results.jsonl files.

The W-D-L footer counts the engine's winner field (a simultaneous destruction of both bases is a draw
whatever the residual HP); the HP table is a separate metric. A second footer line counts the
matches whose HP sign disagrees with the engine outcome.

    .venv/bin/python -B -m bot_research.experiments.lead.matrix RESULTS.jsonl [...]
"""
from __future__ import annotations

import json
import sys
from collections import defaultdict


def short(spec):
    for a, b in (("bot_research.", ""), ("experiments.lead.frozen.", "L."), ("experiments.lead.", "X."),
                 ("bots.economy.frozen.", "E."), ("bots.defense.frozen.", "D."), ("bots.counters.", "K."),
                 ("bots.economy.", "E."), ("bots.defense.", "D."), ("harness.baselines:", "B:"), (":@make", "")):
        spec = spec.replace(a, b)
    return spec


def main(paths):
    rows = [json.loads(l) for p in paths for l in open(p) if l.strip()]
    cell = defaultdict(list)
    for r in rows:
        if r.get("error"):
            continue
        side = r["candidate_side"]
        cand, opp = (r["spec_a"], r["spec_b"]) if side == 0 else (r["spec_b"], r["spec_a"])
        hp = r["hp_diff_a"] if side == 0 else -r["hp_diff_a"]
        w = r["winner"]
        outcome = 0 if w is None else (1 if w == side else -1)
        cell[(cand, opp)].append((hp, outcome))
    cands = sorted({c for c, _ in cell})
    opps = sorted({o for _, o in cell})
    for i, c in enumerate(cands):
        print(f"C{i}: {short(c)}")
    print(f"{'opponent':58s}" + "".join(f"{'C' + str(i):>8s}" for i in range(len(cands))))
    for o in opps:
        vals = []
        for c in cands:
            v = cell.get((c, o))
            vals.append(f"{sum(h for h, _ in v) / len(v):8.0f}" if v else f"{'':8s}")
        print(f"{short(o)[:58]:58s}" + "".join(vals))
    def count(c, k):
        return sum(1 for o in opps for _, x in cell.get((c, o), []) if x == k)

    print(f"{'W-D-L (engine winner)':58s}" + "".join(f" {count(c, 1)}-{count(c, 0)}-{count(c, -1)}".rjust(8) for c in cands))
    print(f"{'HP sign differs from outcome':58s}" + "".join(
        f"{sum(1 for o in opps for h, x in cell.get((c, o), []) if (h > 0) - (h < 0) != x):8d}" for c in cands))


if __name__ == "__main__":
    main(sys.argv[1:])
