"""Attack-package search against an observed defender map.

The attacker knows the defender's buildings (hence route and turret
coverage) and its gold, but not this round's hidden builds. Two estimates:

* optimistic: the defender builds nothing this round (exact via fastsim);
* responded: the defender spends its visible gold on the best splash cells
  next to its current route and on the best gun cells (a crude, fast model
  of an informed same-round response; it does not reroute the path).

New entries are appended after the attacker's active entries (dense
indexing), so their spawn ticks are fixed; entries whose spawn tick exceeds
249 - L never arrive.
"""
from __future__ import annotations

from .fastsim import MapModel, simulate
from .threat import greedy_mix

TIERS = ("tier1", "tier2", "tier3", "tier4", "tier5")
SIZES = (1, 2, 3, 4, 6, 8, 12, 16, 24, 32, 48, 64, 96, 128, 192, 256, 384)


def attack_packages(budget, minions, cap=400):
    pk = []
    for t in TIERS:
        c = minions[t]["cost"]
        nmax = min(cap, budget // c)
        sizes = [n for n in SIZES if n <= nmax]
        if nmax and nmax not in sizes:
            sizes.append(nmax)
        for n in sizes:
            pk.append([t] * n)
    c1 = minions["tier1"]["cost"]
    for t in ("tier3", "tier4", "tier5"):
        ct = minions[t]["cost"]
        for f in (2, 4, 8):
            for n in (1, 2, 4, 8):
                if f * c1 + n * ct <= budget and f + n <= cap:
                    pk.append(["tier1"] * f + [t] * n)
    pk.append(greedy_mix(budget, minions, list(reversed(TIERS)), cap))
    seen, out = set(), []
    for p in pk:
        k = tuple(p)
        if p and k not in seen:
            seen.add(k)
            out.append(p)
    return out


def cost_of(pkg, minions):
    return sum(minions[t]["cost"] for t in pkg)


def responded_model(buildings, gold, rules):
    """Defender adds splash/guns next to its current route with `gold` (no reroute)."""
    model = MapModel(buildings, rules)
    path = model.path
    on_path = set(path)
    occ = {(b[0], b[1]) for b in buildings}
    cells = []
    for x in range(12):
        for y in range(12):
            c = (x, y)
            if c in occ or c in on_path:
                continue
            adj = sum(1 for i in range(model.L) if max(abs(path[i][0] - x), abs(path[i][1] - y)) == 1)
            cov = sum(1 for i in range(model.L) if (path[i][0] - x) ** 2 + (path[i][1] - y) ** 2 <= 9.0)
            cells.append((adj, cov, c))
    turrets = rules["turrets"]
    sc, gc = turrets["splash"]["cost"], turrets["gun2"]["cost"]
    new = list(buildings)
    g = gold
    # half splash by adjacency, half gun2 by coverage (crude mixed response)
    by_adj = sorted(cells, key=lambda t: -t[0])
    by_cov = sorted(cells, key=lambda t: -t[1])
    used = set()
    half = g // 2
    for adj, cov, c in by_adj:
        if half < sc or adj == 0:
            break
        new.append((c[0], c[1], "splash"))
        used.add(c)
        half -= sc
        g -= sc
    for adj, cov, c in by_cov:
        if g < gc or cov == 0:
            break
        if c in used:
            continue
        new.append((c[0], c[1], "gun2"))
        used.add(c)
        g -= gc
    return MapModel(new, rules, path=path)


def defend_response_model(opp_buildings, opp_gold, my_active, my_gold, rules, cap=400):
    """Defender answers with this lane's own worst-case builder (defense_plan.defend)
    against the attacker's visible gold and active roster, spending at most its gold."""
    from .defense_plan import defend
    _, nb, _, _ = defend(opp_buildings, opp_gold, my_active, my_gold, rules, cap=cap)
    return MapModel(nb, rules)


def search(opp_buildings, my_active, budget, rules, opp_gold=0, cap=400, responded=False,
           active_cap=600, my_gold=None):
    """Return list of (pkg, cost, marginal_damage_opt, marginal_damage_resp) sorted by opt ratio.

    responded: False (no response estimate), True or "crude" (responded_model), or
    "defend" (defend_response_model with the attacker's visible gold my_gold).
    """
    minions = rules["minions"]
    model = MapModel(opp_buildings, rules)
    _, base = simulate(model, my_active, rules)
    rmodel = None
    if responded == "defend":
        rmodel = defend_response_model(opp_buildings, opp_gold, my_active,
                                       budget if my_gold is None else my_gold, rules)
    elif responded:
        rmodel = responded_model(opp_buildings, opp_gold, rules)
    rbase = simulate(rmodel, my_active, rules)[1] if responded else 0
    room = max(0, active_cap - len(my_active))
    res = []
    for p in attack_packages(budget, minions, min(cap, room)):
        c = cost_of(p, minions)
        _, d = simulate(model, my_active + p, rules)
        md = d - base
        if md <= 0:
            continue
        rd = 0
        if responded:
            rd = simulate(rmodel, my_active + p, rules)[1] - rbase
        res.append((p, c, md, rd))
    res.sort(key=lambda r: (-(r[2] / r[1]), r[1]))
    return res, base
