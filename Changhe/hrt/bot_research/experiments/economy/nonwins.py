"""Per-candidate W-D-L, clipped mean and the list of non-wins from a tournament results.jsonl.

Usage: python3 nonwins.py RESULTS.jsonl
A non-win line: opponent (shortened), scenario, candidate seat, HP difference (candidate's view), end round.
Outcomes (W/D/L) are the engine's (results field "winner": the candidate's seat, the other seat, or null for a
draw); since 2026-10-31T09:21Z. Before, these tools counted by the sign of the HP difference, which differs from
the engine only for both_bases_destroyed (a draw with a nonzero HP difference).
"""
from __future__ import annotations

import json
import sys
from collections import defaultdict


def outcome(r):
    """1 win, 0 draw, -1 loss for the candidate, by the engine's winner field."""
    w = r.get("winner")
    return 0 if w is None else (1 if w == r["candidate_side"] else -1)


def short(spec):
    mod, _, rest = spec.partition(":")
    parts = mod.split(".")
    return ".".join(parts[-2:]) + ":" + rest.replace("@make", "").replace('"', "")[:70]


def main():
    rows = defaultdict(list)
    for line in open(sys.argv[1]):
        r = json.loads(line)
        side = r["candidate_side"]
        cand = r["spec_a"] if side == 0 else r["spec_b"]
        opp = r["spec_b"] if side == 0 else r["spec_a"]
        diff = r["hp_diff_a"] if side == 0 else -r["hp_diff_a"]
        rows[cand].append((short(opp), r.get("scenario"), side, diff, r.get("rounds", r.get("end_round")), outcome(r)))
    for cand, rs in rows.items():
        w = sum(1 for x in rs if x[5] > 0)
        d = sum(1 for x in rs if x[5] == 0)
        l = len(rs) - w - d
        clip = sum(max(-800, min(800, x[3])) for x in rs) / len(rs)
        print(f"{cand}\n  n={len(rs)} {w}-{d}-{l} clip {clip:+.0f}")
        for x in sorted(rs, key=lambda x: (x[0], str(x[1]), x[2])):
            if x[5] <= 0:
                print(f"    {x[0]} | {x[1]} | seat {x[2]} | {x[3]} | r{x[4]}" + (" | draw" if x[5] == 0 else ""))


if __name__ == "__main__":
    main()
