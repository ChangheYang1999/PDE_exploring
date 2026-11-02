"""Per-pairing comparison of two candidates from tournament results files (hrt-w2).

Usage: python3 pair_diff.py RES_A SUBSTR_A RES_B SUBSTR_B
RES_A and RES_B may be comma lists of results files (a later file overrides an earlier one on the same pairing).
A candidate is selected by the spec ending with SUBSTR (exact suffix match). For every (opponent, scenario, seat)
present in both, prints the HP differences where they differ, then W-D-L and the mean clipped difference ([-800, 800])
of each candidate over the common matches.
Outcomes (W/D/L) are the engine's (results field "winner": the candidate's seat, the other seat, or null for a
draw); since 2026-10-31T09:21Z. Before, these tools counted by the sign of the HP difference, which differs from
the engine only for both_bases_destroyed (a draw with a nonzero HP difference).
"""
from __future__ import annotations

import json
import sys


def outcome(r):
    """1 win, 0 draw, -1 loss for the candidate, by the engine's winner field."""
    w = r.get("winner")
    return 0 if w is None else (1 if w == r["candidate_side"] else -1)


def load(path, suffix):
    out = {}
    for line in (ln for p in path.split(",") for ln in open(p)):
        r = json.loads(line)
        s = r["candidate_side"]
        c = r["spec_a"] if s == 0 else r["spec_b"]
        if not c.endswith(suffix):
            continue
        o = r["spec_b"] if s == 0 else r["spec_a"]
        out[(o, r.get("scenario"), s)] = (r["hp_diff_a"] if s == 0 else -r["hp_diff_a"], outcome(r))
    return out


def main():
    a, b = load(sys.argv[1], sys.argv[2]), load(sys.argv[3], sys.argv[4])
    keys = sorted((k for k in a if k in b), key=lambda k: (k[0], str(k[1]), k[2]))
    for k in keys:
        if a[k] != b[k]:
            print(f"{k[0].split('.')[-1][:60]} | {k[1]} | {k[2]} | A {a[k][0]}{'' if a[k][1] or not a[k][0] else ' (draw)'} "
                  f"| B {b[k][0]}{'' if b[k][1] or not b[k][0] else ' (draw)'}")
    for name, d in (("A", a), ("B", b)):
        v = [d[k][0] for k in keys]
        o = [d[k][1] for k in keys]
        if v:
            w = sum(x > 0 for x in o); dr = sum(x == 0 for x in o); lo = sum(x < 0 for x in o)
            clip = sum(max(-800, min(800, x)) for x in v) / len(v)
            print(f"{name}: n={len(v)} {w}-{dr}-{lo} clip {clip:+.0f}")


if __name__ == "__main__":
    main()
