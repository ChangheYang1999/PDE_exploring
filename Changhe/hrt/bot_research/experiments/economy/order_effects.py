"""Q2 order, screen, stacking and clock-cutoff effects, measured with the exact simulator.

All numbers are exact simulations (bots/economy/fastsim.py, verified equal to
td_game.combat.simulate_map) of one round on fixed defender maps; no response.

Usage (from project root):
  PYTHONDONTWRITEBYTECODE=1 TMPDIR=$PWD/bot_research/tmp .venv/bin/python -B \
      -m bot_research.experiments.economy.order_effects
"""
from __future__ import annotations

from td_game.config import balanced_config

from bot_research.bots.economy.defense_plan import ROWS, R1_WALLS, saturate
from bot_research.bots.economy.fastsim import MapModel, route, simulate

R = balanced_config().to_dict()
M = R["minions"]


def cost(types):
    return sum(M[t]["cost"] for t in types)


def dmg(buildings, types, e_types=()):
    model = MapModel(buildings, R)
    full = list(e_types) + list(types)
    _, _, arrived = simulate(model, full, R, detail=True)
    e = len(e_types)
    return sum(M[full[k]]["damage"] for k in arrived if k >= e), sum(1 for k in arrived if k >= e)


def greedy_guns(buildings, ref_pkg, gold, names=("gun1", "gun2", "gun3")):
    """Place guns one by one at the cell with the largest damage reduction on ref_pkg per gold."""
    b = list(buildings)
    while True:
        cur = dmg(b, ref_pkg)[0]
        occ = {(x, y) for x, y, _ in b}
        best = None
        for x in range(12):
            for y in range(12):
                if (x, y) in occ or (x, y) in ((0, 0), (11, 11)) or route(occ | {(x, y)}) is None:
                    continue
                for t in names:
                    c = R["turrets"][t]["cost"]
                    if c > gold:
                        continue
                    d = dmg(b + [(x, y, t)], ref_pkg)[0]
                    key = ((cur - d) / c, -c)
                    if best is None or key > best[0]:
                        best = (key, (x, y, t), c)
        if best is None or best[0][0] <= 0:
            return b
        b.append(best[1])
        gold -= best[2]


def template_walls_only():
    walls = list(R1_WALLS)
    for y, spec in ROWS.items():
        walls += [(x, y) for x in spec["walls"] + spec["slots"]]
    return [(x, y, "wall") for x, y in walls]


def main():
    maps = {}
    maps["guns400_empty"] = greedy_guns([], ["tier4"] * 4, 400)
    tw = template_walls_only()
    maps["template_walls_L%d" % (len(route({(x, y) for x, y, _ in tw})) - 1)] = tw
    maps["template_guns400"] = greedy_guns(tw, ["tier4"] * 4, 400)
    _, sb, _, _ = saturate([], 400, 10 ** 9, R)
    maps["splash400"] = sb
    for name, b in maps.items():
        m = MapModel(b, R)
        print(f"map {name}: L={m.L} per-copy splash={m.splash_total} "
              f"turrets={[t for _, _, t in b if t != 'wall']}")

    print("\nT1 screens (cheap copies in front of or behind heavy copies): damage, arrivals, damage per 100 gold")
    pk = {
        "tier4x4": ["tier4"] * 4,
        "screen2+tier4x4": ["tier1"] * 2 + ["tier4"] * 4,
        "screen4+tier4x4": ["tier1"] * 4 + ["tier4"] * 4,
        "screen8+tier4x4": ["tier1"] * 8 + ["tier4"] * 4,
        "screen16+tier4x4": ["tier1"] * 16 + ["tier4"] * 4,
        "interleave(t1,t4)x4": ["tier1", "tier4"] * 4,
        "tier4x4+tail8": ["tier4"] * 4 + ["tier1"] * 8,
        "tier4x5": ["tier4"] * 5,
        "tier3x10": ["tier3"] * 10,
        "screen8+tier3x10": ["tier1"] * 8 + ["tier3"] * 10,
    }
    for name, b in maps.items():
        print(f"  map {name}")
        for pn, p in pk.items():
            d, a = dmg(b, p)
            print(f"    {pn:22s} cost {cost(p):5d} dmg {d:5d} arrived {a:3d} per100 {100 * d / cost(p):6.2f}")

    print("\nT2 stacking beyond 250 entries (copies per spawn tick > 1): damage and arrivals")
    for name in ("guns400_empty", "template_guns400"):
        b = maps[name]
        for t in ("tier1", "tier2", "tier3"):
            row = []
            for n in (50, 100, 200, 250, 300, 400, 500, 750):
                d, a = dmg(b, [t] * n)
                row.append(f"{n}:{d}/{a}")
            print(f"  map {name} {t}: " + " ".join(row))

    print("\nT3 clock cutoff and roster order: e old tier1 entries active first, then 2 tier5")
    b = maps[[k for k in maps if k.startswith("template_walls")][0]]
    L = MapModel(b, R).L
    print(f"  map template walls only, L={L}, last arriving spawn tick {249 - L}")
    for e in (0, 100, 150, 182, 183, 184, 200, 248, 249, 250, 300, 433, 434):
        d, a = dmg(b, ["tier5"] * 2, ["tier1"] * e)
        print(f"    e={e:3d}: tier5 spawn ticks {e % 250},{(e + 1) % 250} -> damage {d}, arrived {a}")


if __name__ == "__main__":
    main()
