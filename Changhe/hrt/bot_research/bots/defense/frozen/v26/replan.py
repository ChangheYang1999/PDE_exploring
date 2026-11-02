"""Layout re-planner for foreign maps (lane hrt-w1).

A scripted opening (harness/scenarios.py) leaves random buildings on the own map that cut the corridors of the
master layout (e.g. walls at (3,0) and (9,0) make row 1 impossible to close), so plan_walls builds a broken
serpentine with route 26-46 and the reserved splash slots lose most of their adjacency. This module designs a
new MasterLayout around the existing buildings:

    replan_layout(buildings, *, n_slots=25, iters=5000, seed=0, time_budget=None, objective="best") -> MasterLayout
    layout_for(observation, **kw) -> MasterLayout          (own buildings taken from the observation)
    needs_replan(buildings, layout=LAYOUT) -> bool          (the layout, built as far as legal, cannot reach S 1500)
    layout_cached(buildings, **kw) -> MasterLayout          (memoised replan_layout)
    plan_walls_foreign(observation, budget, objective="route") -> actions   (the lead's 08:34Z request: walls only,
                                                            legal order, route length first)

Method. Fixed cells F = all existing own buildings (walls, turrets, splashes). A candidate is a set C of new
cells (future walls and splashes) with route(F | C) not None. Since any subset of a set with a route also has a
route, every build order of C is legal (engine construction rule: a route must remain). The score of C is
computed on the final route (all of F | C built): adjacency a(c) = number of final-route cells (base excluded)
among the eight neighbours of c; the n_slots cells of C with the largest a(c), plus existing splashes in F,
give S_final = 10 * sum a (the per-copy splash exposure when every slot is a splash); score =
2 * min(S_final, 1500) + 0.3 * max(0, S_final - 1500) + 10 * sum of the ten largest a(c) + 3 * route length
- 2 * |C|. Seeds: the four built-in templates and their transposes (x <-> y; spawn and base lie on the
diagonal), each reduced to the cells that keep a route next to F, then simulated annealing (moves: add a straight
segment of 3-9 cells as a barrier or remove one, add a cell on or next to the current route, remove a chosen cell,
or both) for exactly `iters` steps (deterministic for a given seed; a wall-clock cutoff applies only when time_budget is
given, and then the result depends on the machine load, as hrt-w3's review noted). Output: splash_cells = the best n_slots cells by final adjacency (a >= 2),
wall_order = the remaining cells in greedy order of marginal route gain (each next wall is the one that
lengthens the route most given F and the walls before it), stages = [all, all, all] (one stage),
final_adj over C and F (so plan.is_foreign is False for the new layout and the planner keeps its route
exclusions), final_route and final_len from the full set.

Limits. The search is a heuristic: its layouts are constructive lower bounds on the reachable route length and
exposure, never upper bounds (nothing here shows that S 1500 is unreachable on a given map). The score uses the final route; the greedy S(k) while the structure is incomplete is lower (reported by
experiments/defense/replan_eval.py). Existing guns are kept as blockers only. Cost: about 0.3 ms per
annealing step; the default settings take 1-4 s once per match (fortress caches the result per match).
"""
from __future__ import annotations

import random
import time

from .geometry import W, H, SPAWN, BASE, N8, route, attackable_cells, splash_adjacency
from .plan import MasterLayout, LAYOUT

_TEMPLATE_NAMES = ("default", "annealed25", "annealed26", "pillars774", "lead_v3")


def _template_cells(name):
    from .plan import layout_by_name
    lay = layout_by_name(name)
    return list(lay.wall_order) + list(lay.splash_cells)


def _transpose(cells):
    return [(y, x) for (x, y) in cells]


def _score(fixed, fixed_splash, chosen, n_slots, objective="exposure"):
    """(score, S_final, route length, path) for the full set fixed | chosen; None if no route.
    objective "exposure": 2 min(S,1500) + 0.3 max(0, S-1500) + 10 sum(top-10 adjacency) + 3 L - 2 |C|;
    objective "route": 20 L + 0.5 S - 2 |C| (the lead's route-lengthening request; S is the tie-breaker)."""
    full = fixed | chosen
    path = route(full)
    if path is None:
        return None
    att = attackable_cells(path)
    adj = sorted((splash_adjacency(c, att) for c in chosen), reverse=True)
    s_fixed = sum(splash_adjacency(c, att) for c in fixed_splash)
    s_final = 10 * (sum(adj[:n_slots]) + s_fixed)
    top10 = 10 * sum(adj[:10])
    L = len(path) - 1
    if objective == "route":
        score = 20 * L + 0.5 * s_final - 2 * len(chosen)
    else:
        score = 2 * min(s_final, 1500) + 0.3 * max(0, s_final - 1500) + top10 + 3 * L - 2 * len(chosen)
    return score, s_final, L, path


def _legal_subset(fixed, cells):
    """Add the template cells one by one, keeping only those that leave a route (deterministic order)."""
    chosen = set()
    cur = set(fixed)
    for c in cells:
        if c in cur or c in (SPAWN, BASE) or not (0 <= c[0] < W and 0 <= c[1] < H):
            continue
        if route(cur | {c}) is not None:
            chosen.add(c)
            cur.add(c)
    return chosen


def replan_layout(buildings, *, n_slots: int = 25, iters: int = 5000, seed: int = 0,
                  time_budget: float | None = None, objective: str = "best") -> MasterLayout:
    """objective "exposure" or "route" (see _score), or "best" (default): run both with half the budget each and
    keep the layout with the larger S_final (then the longer route). The two objectives find different local
    optima: on the asym:23:2 seat-0 opening "exposure" reached S 800 and "route" S 1280 (replan_eval, 09:01Z)."""
    if objective == "best":
        cands = []
        for obj in ("exposure", "route"):
            lay = replan_layout(buildings, n_slots=n_slots, iters=iters // 2, seed=seed,
                                time_budget=None if time_budget is None else time_budget / 2, objective=obj)
            s_final = 10 * sum(lay.final_adj[c] for c in lay.splash_cells)
            cands.append(((s_final, lay.final_len), lay))
        return max(cands, key=lambda t: t[0])[1]
    fixed = {(b["x"], b["y"]) for b in buildings}
    fixed_splash = {(b["x"], b["y"]) for b in buildings if b.get("type") == "splash"}
    t0 = time.time()
    rnd = random.Random(seed)
    # seeds: templates and transposes, reduced to a legal subset next to the fixed cells
    best = None
    for name in _TEMPLATE_NAMES:
        cells = _template_cells(name)
        for cand in (cells, _transpose(cells)):
            chosen = _legal_subset(fixed, cand)
            sc = _score(fixed, fixed_splash, chosen, n_slots, objective)
            if sc is not None and (best is None or sc[0] > best[0][0]):
                best = (sc, chosen)
    if best is None:            # no route even with nothing added (cannot happen for a legal own map)
        return LAYOUT
    cur_sc, cur = best
    best_sc, best_set = cur_sc, set(cur)
    T0, T1 = 60.0, 2.0
    for it in range(iters):
        if time_budget is not None and time.time() - t0 > time_budget:
            break       # only with an explicit budget; the default (None) is a fixed step count, reproducible from the seed
        T = T0 * (T1 / T0) ** (it / max(1, iters - 1))
        path = cur_sc[3]
        move = rnd.random()
        new = set(cur)
        if move < 0.2:
            # barrier move: add (or, if mostly present, remove) a straight segment of 3-9 cells in a row or
            # column; single cells rarely lengthen a route, a segment next to the route does
            horizontal = rnd.random() < 0.5
            line = rnd.randrange(1, H - 1) if horizontal else rnd.randrange(1, W - 1)
            a = rnd.randrange(0, W - 2)
            b = min(W, a + rnd.randrange(3, 10))
            seg = [((x, line) if horizontal else (line, x)) for x in range(a, b)]
            seg = [c for c in seg if c not in fixed and c not in (SPAWN, BASE)]
            if not seg:
                continue
            present = sum(1 for c in seg if c in new)
            if present > len(seg) // 2:
                for c in seg:
                    new.discard(c)
            else:
                new.update(seg)
        elif move < 0.6 or not new:
            # add a cell on or next to the current route (only those change the route or the exposure)
            near = []
            for (x, y) in path[:-1]:
                if (x, y) not in fixed and (x, y) not in new and (x, y) != SPAWN:
                    near.append((x, y))
                for dx, dy in N8:
                    c = (x + dx, y + dy)
                    if 0 <= c[0] < W and 0 <= c[1] < H and c not in fixed and c not in new and c not in (SPAWN, BASE):
                        near.append(c)
            if not near:
                continue
            new.add(rnd.choice(near))
        elif move < 0.82:
            new.remove(rnd.choice(sorted(new)))
        else:
            new.remove(rnd.choice(sorted(new)))
            free = [(x, y) for x in range(W) for y in range(H)
                    if (x, y) not in fixed and (x, y) not in new and (x, y) not in (SPAWN, BASE)]
            new.add(rnd.choice(free))
        sc = _score(fixed, fixed_splash, new, n_slots, objective)
        if sc is None:
            continue
        d = sc[0] - cur_sc[0]
        if d >= 0 or rnd.random() < pow(2.718281828, d / T):
            cur, cur_sc = new, sc
            if sc[0] > best_sc[0]:
                best_sc, best_set = sc, set(new)
    return build_layout(fixed, fixed_splash, best_set, n_slots)


def build_layout(fixed, fixed_splash, chosen, n_slots) -> MasterLayout:
    """MasterLayout from a chosen cell set: slots = best final adjacency, walls in greedy route-gain order."""
    full = fixed | chosen
    path = route(full)
    att = attackable_cells(path)
    final_adj = {c: splash_adjacency(c, att) for c in chosen | fixed}
    ranked = sorted(chosen, key=lambda c: (-final_adj[c], c[1], -c[0]))
    slots = [c for c in ranked[:n_slots] if final_adj[c] >= 2]
    walls = [c for c in chosen if c not in slots]
    # greedy wall order by marginal route gain given the fixed cells and the walls already ordered
    order, gains = [], []
    cur = set(fixed)
    cur_len = len(route(cur)) - 1
    remaining = set(walls)
    while remaining:
        best_c, best_len = None, None
        for c in sorted(remaining):
            p = route(cur | {c})
            if p is None:
                continue
            if best_len is None or len(p) - 1 > best_len:
                best_c, best_len = c, len(p) - 1
        if best_c is None:
            break
        order.append(best_c)
        gains.append(best_len - cur_len)
        cur.add(best_c)
        cur_len = best_len
        remaining.remove(best_c)
    # one stage: a single wall rarely lengthens the route (a barrier needs several), and the whole set costs
    # one gold per wall, so fortress builds all re-planned walls as its stage A
    stages = [len(order), len(order), len(order)]
    return MasterLayout(list(order) + slots, order, slots, stages, final_adj, set(path), len(path) - 1)


def needs_replan(buildings, layout: MasterLayout = LAYOUT, target_s: int = 1500, n_slots: int = 25) -> bool:
    """True when the given layout, built as far as the existing buildings allow (legal subset of its walls and
    slots), can no longer reach S >= target_s with its best n_slots slots on the resulting final route."""
    fixed = {(b["x"], b["y"]) for b in buildings}
    fixed_splash = {(b["x"], b["y"]) for b in buildings if b.get("type") == "splash"}
    chosen = _legal_subset(fixed, list(layout.wall_order) + list(layout.splash_cells))
    sc = _score(fixed, fixed_splash, chosen, n_slots)
    return sc is None or sc[1] < target_s


def layout_for(observation: dict, **kw) -> MasterLayout:
    me = observation["players"][observation["player"]]
    return replan_layout(me["buildings"], **kw)


_CACHE: dict = {}


def layout_cached(buildings, **kw) -> MasterLayout:
    """replan_layout memoised on the set of existing cells (a bot that only adds layout cells afterwards keeps
    the same layout; a new foreign cell gives a new key). Module-level cache, bounded to 64 entries."""
    key = (frozenset((b["x"], b["y"], b.get("type")) for b in buildings), tuple(sorted(kw.items())))
    lay = _CACHE.get(key)
    if lay is None:
        if len(_CACHE) >= 64:
            _CACHE.clear()
        lay = replan_layout(buildings, **kw)
        _CACHE[key] = lay
    return lay


def plan_walls_foreign(observation: dict, budget: int, *, objective: str = "best", **kw) -> list[dict]:
    """The lead's request (2026-10-31T08:34Z): legal walls, in a legal build order, that lengthen the shortest
    route as much as the re-planner finds on a map with buildings the bot did not choose. Re-plans (cached) with
    objective "best" (both objectives, larger S_final kept) by default, "route" (route length first) or "exposure"
    (S first), then returns plan.plan_walls for
    the whole wall set within budget. Only the layout's wall cells are returned; its splash_cells are reserved
    for splashes (use the layout from layout_cached(...) with plan_defense to fill them)."""
    from .plan import plan_walls
    me = observation["players"][observation["player"]]
    lay = layout_cached(me["buildings"], objective=objective, **kw)
    return plan_walls(observation, budget, layout=lay)
