"""Summary of a known-policy screen (results.jsonl of run_tourn.sh with known_econ counters).

Usage: python3 screen.py RESULTS.jsonl [...]
Per file: the candidate's HP difference in both seats for each (tier, attack_round)
counter, the minimum, and the number of counters with a negative result.
"""
from __future__ import annotations

import json
import re
import sys


def main():
    for path in sys.argv[1:]:
        rows = {}
        cand = None
        for line in open(path):
            r = json.loads(line)
            side = r["candidate_side"]
            cand = r["spec_a"] if side == 0 else r["spec_b"]
            opp = r["spec_b"] if side == 0 else r["spec_a"]
            d = r["hp_diff_a"] if side == 0 else -r["hp_diff_a"]
            m = re.search(r'attack_round=(\d+)&tier="(\w+)"', opp)
            rows.setdefault((m.group(2), int(m.group(1))), []).append(max(-800, min(800, d)))
        worst = min(min(v) for v in rows.values())
        neg = sum(1 for v in rows.values() if min(v) < 0)
        print(f"{cand.split(':', 1)[1]} | n={sum(map(len, rows.values()))} | min {worst} | losing counters {neg}/{len(rows)}")
        print("  " + " ".join(f"{t[-1]}@{k}:{'/'.join(map(str, v))}" for (t, k), v in sorted(rows.items())
                              if min(v) != 0 or max(v) != 0))


if __name__ == "__main__":
    main()
