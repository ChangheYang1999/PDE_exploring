"""Search one-turret round-1 defences on prefixes of the default layout walls.

    .venv/bin/python -B -m bot_research.experiments.lead.r1_search

For wall prefixes of plan.LAYOUT (frozen hrt-w1 v7) of length 0, 5, ..., 20 and one turret
(gun1, gun2, splash) on every legal free cell, the worst leak over all 27 ordered rosters
costing at most 100 gold is computed with gamekit.simulate_defense (exact replica of the
engine's combat). Zero-leak options of interest are replayed on the engine roster by roster in
r1_certificate.py.
"""
from __future__ import annotations

from bot_research.bots.defense.frozen.v7 import plan as P
from bot_research.experiments.lead.r1_certificate import CFG, RULES, rosters
from bot_research.harness import gamekit as gk

ROSTERS = rosters()


def worst(buildings):
    blocked = gk.cells_of(buildings)
    path = gk.route_cached(blocked)
    profile = gk.splash_profile(path, buildings, RULES)
    guns = gk.gun_coverage(path, buildings, RULES)
    w = (0, ())
    for r in ROSTERS:
        d = gk.simulate_defense(list(r), path, buildings, RULES, profile=profile, guns=guns).damage
        if d > w[0]:
            w = (d, r)
    return w, len(path) - 1


def main():
    order = P.LAYOUT.wall_order
    rows = []
    for k in (0, 5, 10, 15, 20):
        walls = [{"x": c[0], "y": c[1], "type": "wall"} for c in order[:k]]
        blocked = gk.cells_of(walls)
        for kind in ("gun1", "gun2", "splash"):
            cost = k + RULES.turrets[kind]["cost"]
            if cost > 100:
                continue
            for x in range(gk.W):
                for y in range(gk.H):
                    c = (x, y)
                    if c in blocked or c in (gk.SPAWN, gk.BASE) or not gk.legal_build(blocked, c):
                        continue
                    b = walls + [{"x": x, "y": y, "type": kind}]
                    (d, r), L = worst(b)
                    rows.append((d, cost, -L, k, kind, c, r))
    rows.sort()
    best = {}
    for d, cost, negL, k, kind, c, r in rows:
        key = (k, kind)
        if key not in best:
            best[key] = (d, cost, -negL, c, r)
    print("wall prefix | turret | best cell | worst leak | cost | route | worst roster")
    for (k, kind), (d, cost, L, c, r) in sorted(best.items()):
        print(f"{k:2d} | {kind:6s} | {c} | {d:3d} | {cost:3d} | {L:2d} | {r}")
    zero = [x for x in rows if x[0] == 0]
    print(f"zero-leak options: {len(zero)}")
    for d, cost, negL, k, kind, c, r in sorted(zero, key=lambda x: (x[1], x[2]))[:15]:
        b = [{"x": cc[0], "y": cc[1], "type": "wall"} for cc in order[:k]] + [{"x": c[0], "y": c[1], "type": kind}]
        print(f"  walls {k} + {kind} at {c}: cost {cost}, route {-negL}")


if __name__ == "__main__":
    main()
