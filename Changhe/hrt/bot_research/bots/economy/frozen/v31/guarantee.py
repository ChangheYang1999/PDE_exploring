"""Provable lower bound on the base damage of an attack package (Theorem B).

Setting: the attacker observes the defender's buildings and gold G at
decision time and appends a package P to its own active roster (after its e
active entries, so the j-th copy of P spawns at tick (e + j) % 250). The
defender may then build anything with cost at most G before combat (it cannot
see P). The bound holds for every such response; see notes/economy.md, Entry 2,
for the statement and proof. Ingredients (all read from td_game/combat.py):

* the route is a BFS shortest path, so two route cells that are 4-neighbours
  are consecutive on it (otherwise it could be shortened): the route cells in
  any region induce a linear forest of the 4-neighbour grid graph. In
  particular a 2x2 block holds at most 3 route cells, so after any response
  the route has length L' <= L_max = sum over the 36 disjoint 2x2 blocks of
  min(3, cells of the block not built now) - 1 (107 on the empty map); with
  no gold to build, L' = L;
* a copy spawned at tick s can arrive only at tick s + L' <= 249, so copies
  with s <= 249 - L_max are never cut off by the clock ("eligible");
* a splash turret adds its damage to every copy on one of its eight
  neighbouring cells once per tick; a copy visits each route cell once, so a
  splash turret gives a copy at most damage * (number of its neighbours that
  are route cells) over the whole trip. The eight neighbours form an 8-cycle
  of the 4-neighbour graph, so by the linear forest property at most 7 of
  them are route cells (and at most the in-grid neighbours not built now);
* a gun deals its damage to at most one copy per tick, and only while some
  copy is on a route cell within its range. Copies with the same spawn tick
  share their cell at every tick. A gun's range holds at most c route cells,
  where c is the maximum induced linear forest of the in-range cells: 15, 20
  and 27 for ranges 2.5, 3.0 and 3.5 (exact search,
  experiments/economy/induced_forest.py), and for an existing gun also at
  most its in-range cells not built now. With m distinct eligible spawn
  ticks, such a gun deals at most
  damage * min(span, m * c) to the package in one round, where span is the
  number of ticks in which an eligible package copy can be on the map;
* a copy of HP h that dies received splash at most S (the per-copy splash
  bound), hence gun damage at least h - S.

With g gold on new guns, Gamma is at most the existing guns' bound plus the
best integer combination of new guns costing at most g.
So the dead eligible copies K satisfy sum_{j in K} (h_j - S)^+ <= Gamma
(total gun damage bound), and the damage of the arriving eligible copies is at
least sum_j d_j minus the optimum of the fractional knapsack
max sum_{K} d_j subject to sum_{K} need_j <= Gamma (copies with need 0 count
as killed). The defender's split of G between splash and guns is minimised
over explicitly; gold on walls only lowers both terms and is already covered
by L_max.

Arithmetic (changed 2026-10-31T04:12Z after hrt-w3's audit, validation.md
04:00Z): the fractional kill relaxation and the gun-efficiency bound are computed with exact
fractions, and the returned bound is the ceiling of the exact rational bound,
an int (base damage is an integer, so the ceiling is still a lower bound). The
float version (the copies under frozen/, which no bot imports) could exceed
the exact rational value by about 1e-15.
"""
from __future__ import annotations

from fractions import Fraction
from math import ceil

GRID = 12
TICKS = 250
# maximum induced linear forest of the cells within Euclidean range r of a
# cell (centre excluded), from experiments/economy/induced_forest.py
INDUCED = {2.5: 15, 3.0: 20, 3.5: 27}
RING = 7  # route cells among the 8 neighbours of a cell: an induced subgraph of an 8-cycle


def _offsets(radius):
    r2 = radius * radius
    k = int(radius) + 1
    return [(dx, dy) for dx in range(-k, k + 1) for dy in range(-k, k + 1)
            if (dx, dy) != (0, 0) and dx * dx + dy * dy <= r2]


NEIGH8 = [(dx, dy) for dx in (-1, 0, 1) for dy in (-1, 0, 1) if (dx, dy) != (0, 0)]


def _free_count(x, y, offs, blocked):
    n = 0
    for dx, dy in offs:
        cx, cy = x + dx, y + dy
        if 0 <= cx < GRID and 0 <= cy < GRID and (cx, cy) not in blocked:
            n += 1
    return n


def route_cells_cap(c_range, n_free):
    return min(INDUCED.get(float(c_range), n_free), n_free)


def block_bound(blocked, grid=GRID):
    """Upper bound on the number of route cells: at most 3 per 2x2 block."""
    tot = 0
    for bx in range(0, grid, 2):
        for by in range(0, grid, 2):
            free = sum((x, y) not in blocked for x in (bx, bx + 1) for y in (by, by + 1))
            tot += min(3, free)
    return tot


def _gun_knapsack(guns, gold, eff, exact_upto=20000):
    """Function g -> maximum total damage bound of new guns costing at most g
    (unbounded integer knapsack; above ``exact_upto`` gold the linear
    relaxation g * eff, which is an upper bound)."""
    if gold > exact_upto or not guns:
        return lambda g: g * eff
    unit = 0
    for c, _ in guns:
        unit = c if unit == 0 else _gcd(unit, c)
    n = gold // unit
    best = [0] * (n + 1)
    items = [(c // unit, v) for c, v in guns]
    for i in range(1, n + 1):
        b = best[i - 1]
        for cu, v in items:
            if cu <= i and best[i - cu] + v > b:
                b = best[i - cu] + v
        best[i] = b
    return lambda g: best[min(n, g // unit)] if g >= 0 else 0


def _gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def spawn_ticks(e, n, ticks=TICKS):
    return [(e + j) % ticks for j in range(n)]


def bound(def_buildings, def_gold, n_existing, pkg_types, rules, L_max=None, ticks=TICKS,
          detail=False, existing_types=None):
    """Theorem B lower bound on the damage the copies of ``pkg_types`` deal this round.

    def_buildings: iterable of (x, y, type) on the defender's map.
    def_gold: the defender's gold at decision time (its maximal same-round spend).
    n_existing: number of the attacker's active entries before the package.
    existing_types: optionally those entries' types; when given and the
        defender cannot afford any building, the exact simulated damage is
        returned (no response is possible).
    L_max: any proven upper bound on the defender's route length after its
        response; default the 2x2-block bound (or the current length when the
        defender cannot afford a wall or turret).
    Returns the bound (an int, the ceiling of the exact rational bound); with
    detail=True also a dict with the minimising split.
    """
    minions = rules["minions"]
    turrets = rules["turrets"]
    blocked = {(b[0], b[1]) for b in def_buildings}
    cheapest = min([rules.get("wall_cost", 1)] + [t["cost"] for t in turrets.values()])
    if def_gold < cheapest and existing_types is not None:
        # no response is possible: the guaranteed damage is the simulated one
        from .fastsim import MapModel, simulate
        _, _, arrived = simulate(MapModel(def_buildings, rules), list(existing_types) + list(pkg_types),
                                 rules, detail=True)
        e = len(existing_types)
        val = sum(minions[pkg_types[k - e]]["damage"] for k in arrived if k >= e)
        return (val, {"eligible": len(pkg_types), "exact": True}) if detail else val
    if L_max is None:
        if def_gold < cheapest:
            from .fastsim import route
            L_max = len(route(blocked)) - 1
        else:
            L_max = block_bound(blocked) - 1
    cut = ticks - 1 - L_max
    ticks_of = spawn_ticks(n_existing, len(pkg_types), ticks)
    elig = [(s, t) for s, t in zip(ticks_of, pkg_types) if s <= cut]
    if not elig:
        return (0, {"eligible": 0}) if detail else 0
    groups = sorted({s for s, _ in elig})
    m = len(groups)
    span = min(ticks, groups[-1] + L_max - groups[0])

    splash_name = None
    S_exist = 0
    gamma_exist = 0
    for x, y, t in def_buildings:
        if t == "wall":
            continue
        spec = turrets[t]
        if spec["aoe"] == 8:
            S_exist += spec["damage"] * min(RING, _free_count(x, y, NEIGH8, blocked))
        else:
            c = route_cells_cap(spec["range"], _free_count(x, y, _offsets(spec["range"]), blocked))
            gamma_exist += spec["damage"] * min(span, m * c)
    eff = Fraction(0)  # best gun damage bound per gold for new guns
    s_cost = None
    s_dmg = 0
    guns = []  # (cost, damage bound per gun)
    for name, spec in turrets.items():
        if spec["aoe"] == 8:
            if s_cost is None or spec["cost"] < s_cost:
                splash_name, s_cost, s_dmg = name, spec["cost"], spec["damage"]
            continue
        c = route_cells_cap(spec["range"], len(_offsets(spec["range"])))
        guns.append((spec["cost"], spec["damage"] * min(span, m * c)))
        eff = max(eff, Fraction(guns[-1][1], spec["cost"]))
    gun_best = _gun_knapsack(guns, def_gold, eff)

    counts = {}
    for _, t in elig:
        counts[t] = counts.get(t, 0) + 1
    best = None
    kmax = def_gold // s_cost if s_cost else 0
    for k in range(kmax + 1):
        S = S_exist + RING * s_dmg * k
        gamma = gamma_exist + gun_best(def_gold - k * s_cost)
        items = []
        total = 0
        for t, n in counts.items():
            h, d = minions[t]["hp"], minions[t]["damage"]
            need = h - S
            if need <= 0:
                continue
            total += n * d
            items.append((Fraction(d, need), need, d, n))
        items.sort(reverse=True)
        cap = gamma
        killed = Fraction(0)
        for _, need, d, n in items:
            if cap <= 0:
                break
            x = min(Fraction(n), Fraction(cap) / need)
            killed += x * d
            cap -= x * need
        val = total - killed
        if best is None or val < best[0]:
            best = (val, k, S, gamma)
        if best[0] <= 0:
            break
    val = max(0, ceil(best[0]))
    if detail:
        return val, {"eligible": len(elig), "groups": m, "span": span, "L_max": L_max,
                     "splash_k": best[1], "S": best[2],
                     "gamma": best[3] if isinstance(best[3], int) else float(best[3]),
                     "S_exist": S_exist, "gamma_exist": gamma_exist}
    return val


def best_guaranteed(def_buildings, def_gold, n_existing, budget, rules, packages, L_max=None):
    """Among ``packages`` (lists of types) with cost <= budget, the one with the
    largest Theorem B bound. Returns (bound, pkg, cost) or (0, None, 0)."""
    minions = rules["minions"]
    best = (0, None, 0)
    for p in packages:
        c = sum(minions[t]["cost"] for t in p)
        if c > budget:
            continue
        b = bound(def_buildings, def_gold, n_existing, p, rules, L_max=L_max)
        if b > best[0] or (b == best[0] and b > 0 and c < best[2]):
            best = (b, p, c)
    return best
