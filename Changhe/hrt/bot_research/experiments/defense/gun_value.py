"""(b) Value of a gun2/gun3 while S < 1500, on a WALLS/SLOTS template.

For k in (4, 8, 12) splashes placed by the greedy order, and each candidate gun cell (open slots and free
off-route cells, ranked by route coverage), simulate n in 1..3 copies of tier4 and tier5 with the engine
replica and report the cheapest zero-leak gun addition (one gun3, one gun2, or two gun3) per threat.
Writes bot_research/runs/defense/gun_value.txt.
"""
from bot_research.experiments.defense.template_eval import greedy_sequence, lead_template
from bot_research.experiments.defense.template_pillars import pillars_template
from bot_research.bots.defense.geometry import attackable_cells, gun_cells, route
from bot_research.bots.defense.simulate import simulate_leak
from bot_research.harness import gamekit as gk
from td_game.config import balanced_config
from td_game.engine import Engine


def main():
    obs = Engine(balanced_config(), ("A", "B")).observation(0)
    rules = gk.Rules.from_observation(obs)
    out = []
    for name, (walls, slots) in (("lead template", lead_template()),
                                 ("pillars 7+7+4 template", pillars_template(n_bulk_per_row=7, extra_snake=((1, 9), (3, 10), (5, 9), (7, 10))))):
        seq = greedy_sequence(walls, slots)
        for k in (4, 8, 12):
            built = [c for c, _, _ in seq[:k]]
            S = seq[k - 1][1]
            blocked = set(walls) | set(built)
            buildings = [{"x": x, "y": y, "type": "wall"} for x, y in walls] + [{"x": x, "y": y, "type": "splash"} for x, y in built]
            path = route(blocked)
            att = attackable_cells(path)
            open_slots = [c for c in slots if c not in blocked]
            free = [(x, y) for x in range(12) for y in range(12) if (x, y) not in blocked and (x, y) not in set(path) and (x, y) not in ((0, 0), (11, 11))]
            cands = sorted(((gun_cells(c, 3.5, att), c, c in open_slots) for c in open_slots + free), reverse=True)[:12]
            out.append(f"== {name}, k={k} splashes (S={S}, route {len(path)-1}); top gun3 cells (coverage, cell, is_slot): {cands[:6]}")
            for tier in ("tier4", "tier5"):
                for n in (1, 2, 3):
                    types = [tier] * n
                    base = simulate_leak(types, path, buildings, rules)
                    best = None
                    for kind in ("gun2", "gun3"):
                        for cov, c, is_slot in cands:
                            b2 = buildings + [{"x": c[0], "y": c[1], "type": kind}]
                            p2 = route(blocked | {c})
                            if p2 is None:
                                continue
                            h, d, lhp = simulate_leak(types, p2, b2, rules)
                            cost = rules.turrets[kind]["cost"]
                            key = (h == 0, -cost if h == 0 else -(10 * d + lhp))
                            if best is None or key > best[0]:
                                best = (key, kind, c, is_slot, h, d)
                    # two gun3 at the two best coverage cells
                    two = None
                    if len(cands) >= 2:
                        c1, c2 = cands[0][1], cands[1][1]
                        b3 = buildings + [{"x": c1[0], "y": c1[1], "type": "gun3"}, {"x": c2[0], "y": c2[1], "type": "gun3"}]
                        p3 = route(blocked | {c1, c2})
                        if p3 is not None:
                            two = simulate_leak(types, p3, b3, rules)[:2]
                    out.append(f"   {tier} x{n}: no gun -> hits {base[0]} dmg {base[1]}; best single: {best[1]} at {best[2]} (slot={best[3]}) -> hits {best[4]} dmg {best[5]}; two gun3 -> {two}")
    text = "\n".join(out)
    print(text)
    open("bot_research/runs/defense/gun_value.txt", "w").write(text)


if __name__ == "__main__":
    main()
