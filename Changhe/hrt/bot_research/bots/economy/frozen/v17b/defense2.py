"""Defence builder with an explicit list of threat packages.

Same greedy as ``defense_plan.defend`` (slot-serpentine bundles, surrogate
score, stop when the worst true leak is at most ``tolerate``), but the threat
packages are given by the caller instead of ``threat.packages(gold)``.
``defense_plan`` itself is left unchanged because other lanes import it.

``early_packages`` builds the threat list used by econ v5 before its
``late_round``: the cheap families of ``threat.packages(guard_gold)`` plus
``singles`` copies of each tier the opponent can afford, up to tier
``single_max`` (unseen single heavy copies are the cheapest pokes against a
defender that answers only the visible roster).
"""
from __future__ import annotations

from .defense_plan import (TURRETS, _worst, _score, bundle_actions, bundle_buildings,
                           bundle_cost, candidates)
from .fastsim import MapModel, route
from .threat import TIERS, packages


def defend_pk(buildings, gold, threat_types, pk, rules, *, max_steps=60,
              turret_names=TURRETS, tolerate=0, reserve=1600):
    """Greedy safety builder against the packages ``pk`` (lists of types, in
    purchase order, appended after ``threat_types``).
    Returns (actions, new_buildings, gold_left, worst_damage_after)."""
    buildings = list(buildings)
    actions = []
    if not pk:
        pk = [[]]
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


def early_packages(op_gold, guard_gold, singles, single_max, minions, cap=400):
    """Threat packages: cheap families for min(op_gold, guard_gold) gold plus
    up to ``singles`` copies of each affordable tier up to ``single_max``."""
    g = min(op_gold, guard_gold)
    pk = packages(g, minions, cap) if g > 0 else [[]]
    seen = {tuple(p) for p in pk}
    top = TIERS.index(single_max) if single_max in TIERS else -1
    for t in TIERS[:top + 1]:
        n = min(singles, op_gold // minions[t]["cost"])
        for k in range(1, n + 1):
            p = [t] * k
            if tuple(p) not in seen:
                seen.add(tuple(p))
                pk.append(p)
    return pk
