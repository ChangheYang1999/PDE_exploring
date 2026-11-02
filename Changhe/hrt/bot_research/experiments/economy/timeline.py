"""Per-round timeline of a match log (jsonl written by the lead's harness).

Usage: python3 timeline.py LOG [max_round]
Prints round, player, HP, gold, factories, turrets, walls, route length,
roster size and the accepted actions of that round (counted by op:type).
"""
from __future__ import annotations

import json
import sys


def main():
    path = sys.argv[1]
    max_round = int(sys.argv[2]) if len(sys.argv) > 2 else 99
    for line in open(path):
        d = json.loads(line)
        if d.get("round", 0) > max_round:
            break
        s = d.get("snapshot")
        if not s:
            continue
        acts = {}
        for e in d.get("event") or []:
            if e.get("kind") == "action":
                a = e.get("action") or e
                key = a.get("op", "?").replace("build_", "").replace("buy_", "") + (
                    ":" + a["type"] if a.get("type") else "")
                acts[key] = acts.get(key, 0) + 1
        print(f"r{d['round']:2d} p{d['player']} hp {s['hp']:5d} gold {s['gold']:7d} fac {s['n_factories']:4d} "
              f"tur {s['n_turrets']:2d} wal {s['n_walls']:2d} L {s['length_path']:3d} ros {len(s['roster']):4d} {acts}")


if __name__ == "__main__":
    main()
