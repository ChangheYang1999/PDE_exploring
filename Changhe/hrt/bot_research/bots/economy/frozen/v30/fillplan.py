"""Lock fill for foreign maps (hrt-w2, written 2026-10-31 shift 3).

fill_plan(buildings, layout, budget, target, rules) -> (actions, S)

Builds, in this order and within ``budget`` gold:
1. the layout's wall cells not yet occupied (wall_order), each if legal at that point;
2. the layout's splash slots not yet occupied (splash_cells), each as a splash if legal;
3. extra splashes chosen greedily: at each step the legal empty cell whose splash gives the largest
   per-copy splash S on the recomputed route (gamekit.route_cached, the engine's BFS), until S reaches
   ``target``, no cell increases S, or the gold runs out.
S is gamekit.splash_total on the final route (the damage every copy takes from splashes, base cell
excluded). Steps 1-2 stop early once S >= target. Construction legality is the engine rule (a route
from spawn to base must remain); every action returned is legal in the returned order.

Reason (notes/economy.md, shift 3): on mirror:43:3 (hs2) hrt-w1's frozen v26 re-plan has 6 walls
and 25 slots, S_final 1310 at route 56, and v15's plan_defense finds no S 1500 with 10**7 gold, so
econ25's sat_reach never saturates there; the full layout plus 20 greedy extra splashes gives 1730
(experiments/economy/replan_fill.py). Fortress v33 locked at S 1510 from the same start.
"""
from __future__ import annotations

from bot_research.harness import gamekit as gk

W = H = 12
SPAWN, BASE = (0, 0), (11, 11)


def _splash_name(rules):
    return next(n for n, t in rules.turrets.items() if t["aoe"] == 8)


def fill_plan(buildings, layout, budget, target, rules, max_extra=80):
    sname = _splash_name(rules)
    scost = rules.turrets[sname]["cost"]
    sdmg = rules.turrets[sname]["damage"]
    wcost = rules.wall_cost
    b = [dict(x) for x in buildings]
    blocked = {(x["x"], x["y"]) for x in b}
    splashes = {(x["x"], x["y"]) for x in b if x["type"] == sname}
    actions = []
    left = budget

    def s_of(path):
        return sum(sdmg for (x, y) in path[:-1] for (sx, sy) in splashes
                   if max(abs(sx - x), abs(sy - y)) == 1)

    path = gk.route_cached(blocked)
    s = s_of(path)

    def place(c, kind):
        nonlocal left, path, s
        blocked.add(c)
        if kind == "wall":
            actions.append({"op": "build_wall", "x": c[0], "y": c[1]})
            left -= wcost
        else:
            splashes.add(c)
            actions.append({"op": "build_turret", "x": c[0], "y": c[1], "type": sname})
            left -= scost
        path = gk.route_cached(blocked)
        s = s_of(path)

    for kind, cells, cost in (("wall", layout.wall_order, wcost), ("splash", layout.splash_cells, scost)):
        for c in cells:
            if s >= target:
                return actions, s
            c = tuple(c)
            if c in blocked or left < cost:
                continue
            if gk.legal_build(blocked, c):
                place(c, kind)
    for _ in range(max_extra):
        if s >= target or left < scost:
            break
        on_route = set(path)
        att = path[:-1]
        best = None
        for x in range(W):
            for y in range(H):
                c = (x, y)
                if c in blocked or c in (SPAWN, BASE):
                    continue
                if c in on_route:
                    p2 = gk.route_cached(blocked | {c})
                    if p2 is None:
                        continue
                    splashes.add(c)
                    s2 = s_of(p2)
                    splashes.discard(c)
                else:
                    s2 = s + sdmg * sum(1 for (ax, ay) in att if max(abs(ax - x), abs(ay - y)) == 1)
                if s2 > s and (best is None or s2 > best[0]):
                    best = (s2, c)
        if best is None:
            break
        place(best[1], "splash")
    return actions, s
