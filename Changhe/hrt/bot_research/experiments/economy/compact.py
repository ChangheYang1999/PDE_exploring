"""One line per candidate of a tournament: W-D-L and every non-won pairing with its mean HP difference.

Usage: python3 compact.py RESULTS.jsonl
Standard starts and each scenario are reported separately (label suffix " @scenario").
Opponent names are shortened as in summarize.py. "errs" counts matches in which the
candidate's decide raised (the harness records bot_errors per player); such rows are invalid.
Outcomes (W/D/L) are the engine's (results field "winner": the candidate's seat, the other seat, or null for a
draw); since 2026-10-31T09:21Z. Before, these tools counted by the sign of the HP difference, which differs from
the engine only for both_bases_destroyed (a draw with a nonzero HP difference).
"clip" is the mean over matches of the HP difference clipped to [-800, 800] (one HP total; a
destroyed base can end far below 0, which would dominate a plain mean).
"""
from __future__ import annotations

import json
import sys
from collections import defaultdict

from summarize import short


def outcome(r):
    """1 win, 0 draw, -1 loss for the candidate, by the engine's winner field."""
    w = r.get("winner")
    return 0 if w is None else (1 if w == r["candidate_side"] else -1)


def main():
    rows = defaultdict(lambda: defaultdict(list))
    errs = defaultdict(int)
    for line in open(sys.argv[1]):
        r = json.loads(line)
        if r.get("error"):
            continue
        side = r["candidate_side"]
        cand = r["spec_a"] if side == 0 else r["spec_b"]
        opp = r["spec_b"] if side == 0 else r["spec_a"]
        scen = r.get("scenario") or "std"
        diff = r["hp_diff_a"] if side == 0 else -r["hp_diff_a"]
        rows[(cand, scen)][opp].append((diff, outcome(r)))
        if (r.get("players") or [{}, {}])[side].get("bot_errors"):
            errs[(cand, scen)] += 1
    for (cand, scen), opps in rows.items():
        w = d = l = 0
        bad = []
        clip = [max(-800, min(800, x)) for diffs in opps.values() for x, _ in diffs]
        for opp, diffs in opps.items():
            for _, o in diffs:
                w += o > 0
                d += o == 0
                l += o < 0
            m = sum(x for x, _ in diffs) / len(diffs)
            if any(o <= 0 for _, o in diffs):
                bad.append(f"{short(opp)} {m:+.0f}")
        label = short(cand) + ("" if scen == "std" else f" @{scen}")
        print(f"{label} | {w}-{d}-{l} | clip {sum(clip) / len(clip):+.0f} | errs {errs[(cand, scen)]} | "
              + "; ".join(bad))


if __name__ == "__main__":
    main()
