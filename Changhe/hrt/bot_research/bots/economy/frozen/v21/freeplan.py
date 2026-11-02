"""Layout-free greedy defence on an arbitrary own map (fallback planner for econ v15).

``free_plan(observation, budget, comps)`` buys turrets one at a time. Candidate
cells: every empty cell that is not on the current route, not the spawn or the
base, and legal to build on (gamekit.legal_build); a splash is offered only on
cells next to the route (attack cells), a gun only where at least one attack
cell is in its range. The planner does not assume that the route stays the
same: every evaluation recomputes it with gamekit.route_cached (the engine's
BFS), so each simulation is exact for the map it scores. (Docstring reworded at
2026-10-31T05:19Z, after the freeze of frozen/v15; the code is unchanged.)

Each step scores every (cell, turret) pair on the roster of ``comps`` with the
largest current leak score (hrt-w1's score: 10 x leaked base damage + HP of
leaked copies, frozen v15 simulate_leak, exact) and buys the pair with the
largest score reduction per gold (ties: the cheaper). It stops when no roster
of ``comps`` leaks, when nothing affordable reduces the score, or after
``max_steps`` purchases. ``partial="none"`` returns [] unless the final plan
leaks nothing on every roster of ``comps``.

Reason: hrt-w1's frozen v15 ``_gun_candidates`` keeps the 8 cells with the
largest route coverage before the legality test; on scripted maps all 8 can be
route cells where building is illegal, and with a template layout no cell may be
left at all (notes/economy.md, entry 5).
"""
from __future__ import annotations

from bot_research.bots.defense.frozen.v15.simulate import simulate_leak
from bot_research.harness import gamekit as gk

SPAWN, BASE = (0, 0), (11, 11)


def _leaks(buildings, blocked, rules, comps):
    path = gk.route_cached(blocked)
    profile = gk.splash_profile(path, buildings, rules)
    guns = gk.gun_coverage(path, buildings, rules)
    out = []
    for types in comps:
        h, d, lhp = simulate_leak(types, path, buildings, rules, profile=profile, guns=guns)
        out.append((10 * d + lhp, h))
    return out


def free_plan(observation, budget, comps, *, partial="best", max_steps=15, kinds=None):
    """Greedy turret purchases (list of build_turret actions) answering ``comps``."""
    me = observation["players"][observation["player"]]
    rules = gk.Rules.from_observation(observation)
    buildings = [dict(b) for b in me["buildings"]]
    blocked = {(b["x"], b["y"]) for b in buildings}
    budget = min(budget, me["gold"])
    kinds = list(kinds or rules.turrets)
    actions, spent = [], 0
    if not comps:
        return []
    cur = _leaks(buildings, blocked, rules, comps)
    for _ in range(max_steps):
        if all(h == 0 for _, h in cur):
            break
        wi = max(range(len(comps)), key=lambda i: cur[i][0])
        w_score = cur[wi][0]
        path = gk.route_cached(blocked)
        att = path[:-1]
        on_path = set(path)
        best = None
        for x in range(12):
            for y in range(12):
                c = (x, y)
                if c in blocked or c in on_path or c in (SPAWN, BASE):
                    continue
                if not gk.legal_build(blocked, c):
                    continue
                for kind in kinds:
                    t = rules.turrets[kind]
                    cost = t["cost"]
                    if spent + cost > budget:
                        continue
                    if t["aoe"]:
                        if not any(max(abs(px - x), abs(py - y)) == 1 for px, py in att):
                            continue
                    else:
                        r2 = t["range"] ** 2
                        if not any((px - x) ** 2 + (py - y) ** 2 <= r2 for px, py in att):
                            continue
                    nb = buildings + [{"x": x, "y": y, "type": kind}]
                    nblk = blocked | {c}
                    sc = _leaks(nb, nblk, rules, [comps[wi]])[0][0]
                    gain = w_score - sc
                    if gain <= 0:
                        continue
                    key = (gain / cost, -cost)
                    if best is None or key > best[0]:
                        best = (key, c, kind, cost)
        if best is None:
            break
        _, c, kind, cost = best
        buildings.append({"x": c[0], "y": c[1], "type": kind})
        blocked.add(c)
        actions.append({"op": "build_turret", "x": c[0], "y": c[1], "type": kind})
        spent += cost
        cur = _leaks(buildings, blocked, rules, comps)
    if partial == "none" and any(h for _, h in cur):
        return []
    return actions
