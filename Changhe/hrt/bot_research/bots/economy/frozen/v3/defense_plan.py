"""Slot-serpentine defensive plan with a greedy, simulation-checked builder.

Layout (final): wall rows y=1,3,5,7,9 with crossing gaps at x=0,11,0,11,0;
corridors y=0(spawn only),2,4,6,8,10; final route length 66. Each wall row
y in {3,5,7,9} has 4 permanent walls at the far end and 7 turret slots at
the gap end. A slot left empty is a shortcut through the row; filling the
slots from the far end outward lengthens the route by 2 per slot and every
filled slot is adjacent to the route cells above and below it (6 cells).
Row y=11 (x=1..10) holds optional extra turrets next to corridor y=10.

The builder adds the candidate (next slot of a row with its walls, or an
extra cell) that most reduces the worst-case leak against the attack
families in threat.py, per gold, until the worst case leaks nothing.
This is the economy lane's working defence; a better plan from the defence
lane can replace it through the same `defend` interface.
"""
from __future__ import annotations

from .fastsim import MapModel, route, simulate
from .threat import packages

ROWS = {
    9: {"walls": [8, 9, 10, 11], "slots": [7, 6, 5, 4, 3, 2, 1]},
    7: {"walls": [0, 1, 2, 3], "slots": [4, 5, 6, 7, 8, 9, 10]},
    5: {"walls": [8, 9, 10, 11], "slots": [7, 6, 5, 4, 3, 2, 1]},
    3: {"walls": [0, 1, 2, 3], "slots": [4, 5, 6, 7, 8, 9, 10]},
}
R1_WALLS = [(x, 1) for x in range(1, 12)]
EXTRA = [(x, 11) for x in range(1, 11)]
TURRETS = ("splash", "gun1", "gun2", "gun3")


def _occupied(buildings):
    return {(b[0], b[1]) for b in buildings}


def template_cells():
    """All cells of the final template: (x, y) -> 'wall' | 'slot' | 'extra'."""
    cells = {c: "wall" for c in R1_WALLS}
    for y, spec in ROWS.items():
        for x in spec["walls"]:
            cells[(x, y)] = "wall"
        for x in spec["slots"]:
            cells[(x, y)] = "slot"
    for c in EXTRA:
        cells[c] = "extra"
    return cells


def potential_splash(buildings, rules):
    """Per-copy splash on the completed template if every free template cell
    became a wall (wall cells) or a splash (slot and extra cells)."""
    occ = _occupied(buildings)
    full = list(buildings)
    for c, kind in template_cells().items():
        if c not in occ:
            full.append((c[0], c[1], "wall" if kind == "wall" else "splash"))
    try:
        return MapModel(full, rules).splash_total
    except ValueError:
        return 0


def candidates(buildings, turret_names=TURRETS, rules=None, reserve=0):
    """Candidate bundles (walls, (x, y, turret)).

    A gun is offered only if, after placing it, the completed template could
    still reach per-copy splash >= reserve (keeps the saturation option open).
    """
    occ = _occupied(buildings)
    out = []

    def gun_ok(cell, t):
        if t == "splash" or reserve <= 0 or rules is None:
            return True
        return potential_splash(buildings + [(cell[0], cell[1], t)], rules) >= reserve

    for y, spec in ROWS.items():
        nxt = next((x for x in spec["slots"] if (x, y) not in occ), None)
        if nxt is None:
            continue
        walls = [(x, y) for x in spec["walls"] if (x, y) not in occ]
        if y == 3:
            walls += [c for c in R1_WALLS if c not in occ]
        for t in turret_names:
            if gun_ok((nxt, y), t):
                out.append((walls, (nxt, y, t)))
    for c in EXTRA:
        if c not in occ:
            for t in turret_names:
                if gun_ok(c, t):
                    out.append(([], (c[0], c[1], t)))
            break  # extra cells are interchangeable up to position; take the first free one
    return out


def bundle_cost(bundle, rules):
    walls, (x, y, t) = bundle
    return len(walls) * rules["wall_cost"] + rules["turrets"][t]["cost"]


def bundle_actions(bundle):
    walls, (x, y, t) = bundle
    acts = [{"op": "build_wall", "x": wx, "y": wy} for wx, wy in walls]
    acts.append({"op": "build_turret", "type": t, "x": x, "y": y})
    return acts


def bundle_buildings(bundle):
    walls, (x, y, t) = bundle
    return [(wx, wy, "wall") for wx, wy in walls] + [(x, y, t)]


def _score(model, types, rules):
    hits, dmg, slk = simulate(model, types, rules, slack=True)
    return dmg + slk, dmg


def _worst(model, existing, pk, rules, k=3):
    """Top-k packages by surrogate score; returns (list of (score, dmg, pkg)), true worst dmg."""
    rows = []
    for p in pk:
        sc, d = _score(model, existing + p, rules)
        rows.append((sc, d, p))
    rows.sort(key=lambda r: -r[0])
    return rows[:k], max(r[1] for r in rows)


def defend(buildings, gold, threat_types, threat_gold, rules, *, cap=400, margin_gold=0,
           max_steps=60, turret_names=TURRETS, tolerate=0, reserve=1600):
    """Greedy safety builder.

    buildings: own buildings as (x, y, type); threat_types: opponent's active
    roster for this round (types in order); threat_gold: opponent's gold.
    Repeatedly adds the candidate bundle with the largest reduction of the
    surrogate threat (damage plus damage-weighted remaining HP of arriving
    copies, maximised over the three currently worst packages) per gold,
    until the worst true damage over all packages is <= tolerate.
    Returns (actions, new_buildings, gold_left, worst_damage_after).
    """
    buildings = list(buildings)
    actions = []
    pk = packages(threat_gold + margin_gold, rules["minions"], cap)
    model = MapModel(buildings, rules)
    top, worst = _worst(model, threat_types, pk, rules)
    steps = 0
    while worst > tolerate and steps < max_steps:
        steps += 1
        cur = max(r[0] for r in top)
        best = None
        for b in candidates(buildings, turret_names, rules, reserve):
            cost = bundle_cost(b, rules)
            if cost > gold:
                continue
            nb = buildings + bundle_buildings(b)
            if route({(x, y) for x, y, _ in nb}) is None:
                continue
            m = MapModel(nb, rules)
            sc = max(_score(m, threat_types + r[2], rules)[0] for r in top)
            key = ((cur - sc) / cost, m.L, -cost)
            if best is None or key > best[0]:
                best = (key, b, m)
        if best is None or best[0][0] <= 0:
            break
        _, b, m = best
        actions += bundle_actions(b)
        buildings += bundle_buildings(b)
        gold -= bundle_cost(b, rules)
        model = m
        top, worst = _worst(model, threat_types, pk, rules)
    return actions, buildings, gold, worst


def saturate(buildings, gold, target, rules, max_steps=60):
    """Add splash bundles (largest per-copy splash gain per gold first) until the
    per-copy splash on the current route reaches target or gold runs out.
    Returns (actions, new_buildings, gold_left, splash_total)."""
    buildings = list(buildings)
    actions = []
    cur = MapModel(buildings, rules).splash_total
    steps = 0
    while cur < target and steps < max_steps:
        steps += 1
        best = None
        for b in candidates(buildings, ("splash",)):
            cost = bundle_cost(b, rules)
            if cost > gold:
                continue
            nb = buildings + bundle_buildings(b)
            if route({(x, y) for x, y, _ in nb}) is None:
                continue
            m = MapModel(nb, rules)
            key = ((m.splash_total - cur) / cost, m.L)
            if best is None or key > best[0]:
                best = (key, b, m)
        if best is None or best[0][0] <= 0:
            break
        _, b, m = best
        actions += bundle_actions(b)
        buildings += bundle_buildings(b)
        gold -= bundle_cost(b, rules)
        cur = m.splash_total
    return actions, buildings, gold, cur
