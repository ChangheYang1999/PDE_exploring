"""Splash capacity of recorded maps (loss review, hrt-w2).

Usage (from the project root): python3 bot_research/experiments/economy/capacity.py LOG [ROUNDS] [PLAYERS]
ROUNDS and PLAYERS are comma lists (default: every round, both players).

For each recorded snapshot (the state after that round's actions and combat) prints the
route length L, the per-copy splash S of the map (10 x route adjacencies of splash turrets),
the number of empty cells, and a greedy lower bound on the largest S reachable by adding
splash turrets only: repeatedly add the splash, on any empty cell whose blocking keeps a
route (gamekit.legal_build; a splash on a route cell reroutes the copies), with the largest
increase of S on the recomputed route (gamekit.route_cached, the engine's BFS), until no
addition increases S. Reported: the greedy S, the number of splashes and their gold, and the
first count at which S >= 1500 (the tier5 HP; by Proposition 4 of notes/economy.md such a
map is immune for the rest of the match if nothing else is built). Walls are not added, so
the bound ignores rerouting by walls; it is a lower bound on capacity, not the capacity.
"""
from __future__ import annotations

import json
import sys

sys.path.insert(0, ".")
from bot_research.harness import gamekit as gk  # noqa: E402

SPAWN, BASE = (0, 0), (11, 11)


def splash_s(path, splash_cells):
    att = path[:-1]
    return 10 * sum(1 for c in att for s in splash_cells if max(abs(c[0] - s[0]), abs(c[1] - s[1])) == 1)


def greedy(buildings, target=1500):
    blocked = {(b["x"], b["y"]) for b in buildings}
    splash = [(b["x"], b["y"]) for b in buildings if b["type"] == "splash"]
    path = gk.route_cached(blocked)
    s = splash_s(path, splash)
    n, first = 0, (0 if s >= target else None)
    while True:
        best = None
        for x in range(12):
            for y in range(12):
                c = (x, y)
                if c in blocked or c in (SPAWN, BASE) or not gk.legal_build(blocked, c):
                    continue
                p2 = gk.route_cached(blocked | {c})
                s2 = splash_s(p2, splash + [c])
                if s2 > s and (best is None or s2 > best[0]):
                    best = (s2, c, p2)
        if best is None:
            return s, n, first
        s, c, path = best
        blocked.add(c)
        splash.append(c)
        n += 1
        if first is None and s >= target:
            first = n


def main():
    log = sys.argv[1]
    rounds = set(int(r) for r in sys.argv[2].split(",")) if len(sys.argv) > 2 and sys.argv[2] else None
    players = set(int(p) for p in sys.argv[3].split(",")) if len(sys.argv) > 3 else {0, 1}
    for line in open(log):
        d = json.loads(line)
        snap = d.get("snapshot")
        if not snap or (rounds and d["round"] not in rounds) or d["player"] not in players:
            continue
        b = snap["buildings"]
        blocked = {(q["x"], q["y"]) for q in b}
        path = gk.route_cached(blocked)
        s = splash_s(path, [(q["x"], q["y"]) for q in b if q["type"] == "splash"])
        empty = sum(1 for x in range(12) for y in range(12)
                    if (x, y) not in blocked and (x, y) not in path)
        gs, n, first = greedy(b)
        print(f"r{d['round']:2d} p{d['player']} L {len(path) - 1:2d} S {s:5d} empty {empty:3d} gold {snap['gold']:7d} "
              f"greedy S {gs:5d} with {n:2d} splash ({60 * n} gold); S>=1500 after {first}")


if __name__ == "__main__":
    main()
