"""Splash capacity of a re-planned layout beyond its 25 slots (hrt-w2 analysis).

Usage (project root): python -B -m bot_research.experiments.economy.replan_fill SCEN [SCEN ...]
For each scenario and seat, at the first free decision round (scripted rounds played as in
replan_reach.py): build hrt-w1's frozen v26 re-plan (iters 5000, seed = round) in full (its wall
cells as walls, its slots as splashes; cells already occupied or illegal at that point are skipped),
report the route L and per-copy splash S, then add splashes greedily on any legal empty cell
(capacity.greedy: largest S increase on the recomputed route) and report the S reached and the
number of extra splashes. Also the same greedy from the map itself (no layout) for comparison, and whether
hrt-w1's frozen v15 plan_defense (econ25's lock_reachable test) finds S 1500 with 10**7 gold with that
layout or with the empty layout.
"""
from __future__ import annotations

import sys

from bot_research.bots.defense.frozen.v15 import plan as P
from bot_research.bots.defense.frozen.v26 import replan as R26
from bot_research.bots.economy.frozen.v25 import econ25 as E25
from bot_research.experiments.economy.capacity import greedy, splash_s
from bot_research.experiments.economy.replan_reach import own_map
from bot_research.harness import gamekit as gk


def build_full(buildings, lay):
    b = [dict(x) for x in buildings]
    blocked = {(x["x"], x["y"]) for x in b}
    for kind, cells in (("wall", lay.wall_order), ("splash", lay.splash_cells)):
        for c in cells:
            c = tuple(c)
            if c in blocked or not gk.legal_build(blocked, c):
                continue
            blocked.add(c)
            b.append({"x": c[0], "y": c[1], "type": kind})
    return b


def main(argv):
    print("scenario seat round S_map greedy_map(S,n) L_full S_full greedy_full(S,n)", flush=True)
    for scen in argv:
        obs = own_map(scen)
        seats = (0,) if scen.startswith("mirror") else (0, 1)
        for p in seats:
            b = obs[p]["players"][p]["buildings"]
            rnd = obs[p]["round"]
            path0 = gk.route_cached({(x["x"], x["y"]) for x in b})
            s0 = splash_s(path0, [(x["x"], x["y"]) for x in b if x["type"] == "splash"])
            g0 = greedy(b)
            lay = R26.replan_layout(b, iters=5000, seed=rnd)
            full = build_full(b, lay)
            path = gk.route_cached({(x["x"], x["y"]) for x in full})
            s_full = splash_s(path, [(x["x"], x["y"]) for x in full if x["type"] == "splash"])
            g1 = greedy(full)
            o = E25._with(obs[p], [], 10 ** 7)
            v15 = [bool(P.plan_defense(o, 10 ** 7, required_hp=1500, layout=L, partial="none", time_budget=1e6))
                   for L in (lay, P.MasterLayout([], [], [], [0, 0, 0], {}, set(), 0))]
            print(scen, p, rnd, s0, g0[:2], len(path) - 1, s_full, g1[:2], "v15_reach(lay,free)", v15, flush=True)


if __name__ == "__main__":
    main(sys.argv[1:])
