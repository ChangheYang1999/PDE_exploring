"""Soundness and tightness check of the Theorem B bound (bots/economy/guarantee.py).

For defender states x defender gold x attacker existing-roster size x attack
package, compute the bound and the exact package damage (fastsim, verified
equal to td_game.combat) after several concrete same-round responses with the
defender's full gold:
  none      no building;
  omni      defense_plan.defend told the exact attack (an omniscient greedy);
  splash    all gold on splash (saturate with an unreachable target);
  gungreedy greedy over every free cell near the route and every turret type,
            by exact damage reduction per gold (any cell, rerouting allowed);
  wallcut   template walls first (route length, clock cutoff), then splash;
  wallgun   up to 30 gold of template walls, then gungreedy;
  random    random turrets/walls on free cells (3 seeds).
Every response is legal (route kept). The minimum over the responses is an
upper bound on the true guaranteed damage; the bound must never exceed it.

Usage (from project root):
  PYTHONDONTWRITEBYTECODE=1 TMPDIR=$PWD/bot_research/tmp .venv/bin/python -B \
      -m bot_research.experiments.economy.guarantee_check OUT.jsonl [quick]
"""
from __future__ import annotations

import json
import random
import sys
import time

from td_game.config import balanced_config

from bot_research.bots.economy.defense_plan import ROWS, R1_WALLS, defend, saturate
from bot_research.bots.economy.fastsim import MapModel, route, simulate
from bot_research.bots.economy.guarantee import bound
from bot_research.bots.economy.offense import attack_packages

RULES = balanced_config().to_dict()
TURRETS = [t for t in RULES["turrets"]]


def pkg_damage(buildings, existing, pkg):
    m = MapModel(buildings, RULES)
    _, _, arrived = simulate(m, existing + pkg, RULES, detail=True)
    e = len(existing)
    return sum(RULES["minions"][pkg[k - e]]["damage"] for k in arrived if k >= e)


def legal_add(buildings, cell):
    occ = {(b[0], b[1]) for b in buildings}
    if cell in occ or cell in ((0, 0), (11, 11)):
        return False
    return route(occ | {cell}) is not None


def resp_gungreedy(buildings, gold, existing, pkg, max_steps=40):
    b = list(buildings)
    cur = pkg_damage(b, existing, pkg)
    for _ in range(max_steps):
        if cur == 0:
            break
        path = MapModel(b, RULES).path
        occ = {(x, y) for x, y, _ in b}
        cells = {(x, y) for x in range(12) for y in range(12)
                 if (x, y) not in occ and min(max(abs(x - px), abs(y - py)) for px, py in path) <= 3}
        best = None
        for c in cells:
            if not legal_add(b, c):
                continue
            for t in TURRETS:
                cost = RULES["turrets"][t]["cost"]
                if cost > gold:
                    continue
                d = pkg_damage(b + [(c[0], c[1], t)], existing, pkg)
                key = ((cur - d) / cost, -cost)
                if best is None or key > best[0]:
                    best = (key, (c[0], c[1], t), d, cost)
        if best is None or best[0][0] <= 0:
            break
        b.append(best[1])
        gold -= best[3]
        cur = best[2]
    return cur


def template_walls(buildings, gold):
    """Add serpentine template walls (slots included) while gold lasts."""
    b = list(buildings)
    walls = list(R1_WALLS)
    for y, spec in ROWS.items():
        walls += [(x, y) for x in spec["walls"] + spec["slots"]]
    for c in walls:
        if gold < 1:
            break
        if legal_add(b, c):
            b.append((c[0], c[1], "wall"))
            gold -= 1
    return b, gold


def resp_wallcut(buildings, gold):
    b = list(buildings)
    walls = list(R1_WALLS)
    for y, spec in ROWS.items():
        walls += [(x, y) for x in spec["walls"] + spec["slots"]]
    for c in walls:
        if gold < 1:
            break
        if legal_add(b, c):
            b.append((c[0], c[1], "wall"))
            gold -= 1
    _, b, _, _ = saturate(b, gold, 10 ** 9, RULES)
    return b


def resp_random(buildings, gold, seed):
    rng = random.Random(seed)
    b = list(buildings)
    tries = 0
    while tries < 400:
        tries += 1
        t = rng.choice(TURRETS + ["wall"])
        cost = RULES["turrets"][t]["cost"] if t != "wall" else 1
        if cost > gold:
            continue
        c = (rng.randrange(12), rng.randrange(12))
        if legal_add(b, c):
            b.append((c[0], c[1], t))
            gold -= cost
    return b


def states():
    """Named defender maps."""
    out = {"empty": []}
    _, b, _, _ = defend([], 300, ["tier2"] * 6, 0, RULES, reserve=0)
    out["defend300"] = b
    _, b, _, _ = saturate([], 800, 10 ** 9, RULES)
    out["splash800"] = b
    walls = list(R1_WALLS)
    for y, spec in ROWS.items():
        walls += [(x, y) for x in spec["walls"]]
    b = [(x, y, "wall") for x, y in walls]
    _, b, _, _ = defend(b, 400, ["tier3"] * 8, 0, RULES, reserve=1600)
    out["template_mid"] = b
    return out


def main():
    out_path = sys.argv[1]
    quick = len(sys.argv) > 2 and sys.argv[2] == "quick"
    golds = [0, 100, 400] if quick else [0, 60, 150, 400, 1000]
    exist_sizes = [0] if quick else [0, 150]
    budgets = [300, 2000] if quick else [300, 1000, 4000]
    sts = states()
    rows = []
    t0 = time.time()
    violations = 0
    with open(out_path, "w") as fh:
        for sname, sb in sts.items():
            for G in golds:
                for e in exist_sizes:
                    existing = ["tier1"] * e
                    seen = set()
                    for budget in budgets:
                        pks = attack_packages(budget, RULES["minions"], cap=400)
                        if quick:
                            pks = pks[::4]
                        for pkg in pks:
                            key = tuple(pkg)
                            if key in seen:
                                continue
                            seen.add(key)
                            bnd, det = bound(sb, G, e, pkg, RULES, detail=True, existing_types=existing)
                            res = {"none": pkg_damage(sb, existing, pkg)}
                            if G > 0:
                                _, ob, _, _ = defend(sb, G, existing + pkg, 0, RULES, reserve=0)
                                res["omni"] = pkg_damage(ob, existing, pkg)
                                _, spb, _, _ = saturate(sb, G, 10 ** 9, RULES)
                                res["splash"] = pkg_damage(spb, existing, pkg)
                                res["wallcut"] = pkg_damage(resp_wallcut(sb, G), existing, pkg)
                                for s in range(3):
                                    res[f"random{s}"] = pkg_damage(resp_random(sb, G, s), existing, pkg)
                                if not quick or len(pkg) <= 64:
                                    res["gungreedy"] = resp_gungreedy(sb, G, existing, pkg)
                                    w = min(G, 30)
                                    wb, left = template_walls(sb, w)
                                    res["wallgun"] = resp_gungreedy(wb, G - (w - left), existing, pkg)
                            mn = min(res.values())
                            if bnd > mn + 1e-9:
                                violations += 1
                            cost = sum(RULES["minions"][t]["cost"] for t in pkg)
                            comp = {}
                            for t in pkg:
                                comp[t] = comp.get(t, 0) + 1
                            row = {"state": sname, "def_gold": G, "existing": e, "pkg": comp,
                                   "pkg_order": "screen" if pkg[0] == "tier1" and len(comp) > 1 else "plain",
                                   "cost": cost, "bound": round(bnd, 2), "min_resp": mn,
                                   "resp": res, "detail": det}
                            fh.write(json.dumps(row) + "\n")
                            rows.append(row)
            print(f"{sname} done, {len(rows)} rows, {time.time() - t0:.0f}s, violations={violations}",
                  flush=True)
    print(f"total rows {len(rows)} violations {violations}")


if __name__ == "__main__":
    main()
