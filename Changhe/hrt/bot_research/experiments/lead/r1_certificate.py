"""Check round-1 zero-leak defences against every ordered roster costing at most 100 gold.

    .venv/bin/python -B -m bot_research.experiments.lead.r1_certificate

A defence is a list of buildings on the empty map. Every multiset of tier1..tier3
with total cost <= 100 is tried in every distinct order (guns depend on order),
with the exact combat replay (harness/gamekit.simulate_defense, which matches the
engine), and every roster is also replayed on the engine (column "engine": worst engine leak).
"""
from __future__ import annotations

import itertools

from bot_research.harness import gamekit as gk
from td_game.config import balanced_config

CFG = balanced_config()
RULES = gk.Rules.from_observation({"rules": CFG.to_dict()})

CANDIDATES = {
    # astra "opening" answer: gun2 at (3,2), walls (x,1) for x<=4 and (6,y) for y<=3, 89 gold
    "astra_gun2_3_2": [{"x": 3, "y": 2, "type": "gun2"}] + [{"x": x, "y": 1, "type": "wall"} for x in range(5)]
                      + [{"x": 6, "y": y, "type": "wall"} for y in range(4)],
}


def _layout_option(n_walls, kind, cell):
    from bot_research.bots.defense.frozen.v7 import plan as P
    return [{"x": c[0], "y": c[1], "type": "wall"} for c in P.LAYOUT.wall_order[:n_walls]] + \
        [{"x": cell[0], "y": cell[1], "type": kind}]


# layout-compatible options found by r1_search.py (default master layout of hrt-w1, frozen v7)
CANDIDATES["layout20_gun2_1_3"] = _layout_option(20, "gun2", (1, 3))
CANDIDATES["layout15_gun2_10_1"] = _layout_option(15, "gun2", (10, 1))


def rosters(budget=100):
    out = set()
    for n3 in range(budget // 100 + 1):
        for n2 in range((budget - 100 * n3) // 40 + 1):
            for n1 in range((budget - 100 * n3 - 40 * n2) // 15 + 1):
                base = ["tier3"] * n3 + ["tier2"] * n2 + ["tier1"] * n1
                for perm in set(itertools.permutations(base)):
                    out.add(perm)
    return sorted(out)


def check(buildings):
    blocked = gk.cells_of(buildings)
    path = gk.route_cached(blocked)
    cost = sum(RULES.wall_cost if b["type"] == "wall" else RULES.turrets[b["type"]]["cost"] for b in buildings)
    worst = (0, ())
    for r in rosters():
        res = gk.simulate_defense(list(r), path, buildings, RULES)
        if res.damage > worst[0]:
            worst = (res.damage, r)
    # engine replay of every roster (not only the worst simulated one)
    eng = max(gk.engine_simulate_defense(list(r), buildings, CFG).damage for r in rosters())
    return cost, len(path) - 1, worst, eng


def main():
    print(f"{len(rosters())} ordered rosters with cost <= 100")
    for name, b in CANDIDATES.items():
        cost, L, worst, eng = check(b)
        print(f"{name}: cost {cost}, route {L}, worst leak {worst[0]} by {worst[1]} (engine {eng})")


if __name__ == "__main__":
    main()
