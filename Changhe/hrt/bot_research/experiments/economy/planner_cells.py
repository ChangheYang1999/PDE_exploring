"""Check of the hrt-w1 frozen v15 _gun_candidates defect (notes/economy.md, entry 5).

Usage (from the project root): PYTHONPATH=. .venv/bin/python -B bot_research/experiments/economy/planner_cells.py
For replayed observations (v13 against lead_best_b, seat 0, layout lead_v3) it prints how many cells of the
planner's gun pool pass gk.legal_build, against all legal cells with a route cell in range.
"""
from bot_research.experiments.economy.obs_replay import observation_at
from bot_research.bots.defense.frozen.v15 import plan as P
from bot_research.harness import gamekit as gk
A = "bot_research.bots.economy.frozen.v13.econ13:@make"
B = "bot_research.bots.economy.frozen.lead_best_b.best:@make"
for scen, R in (("mirror:1:2", 6), ("mirror:1:2", 9), ("mirror:22:3", 8), ("mirror:22:3", 12)):
    obs = observation_at(A, B, R, 0, scenario=scen)
    me, rl, buildings, blocked = P.observe(obs)
    path = gk.route_cached(blocked)
    att = path[:-1]
    for lname in ("lead_v3",):
        lay = P.layout_by_name(lname)
        foreign = P.is_foreign(blocked, lay)
        outside = sum(1 for c in blocked if c not in lay.final_adj)
        for kind in ("gun1", "gun2", "gun3"):
            pool = P._gun_candidates(blocked, lay, path, rl, kind, buildings=buildings)
            legal = [c for c in pool if gk.legal_build(blocked, c)]
            onroute = [c for c in pool if c in set(path)]
            r2 = rl.turrets[kind]["range"] ** 2
            alllegal = [(x, y) for x in range(12) for y in range(12) if (x, y) not in blocked and (x, y) not in ((0, 0), (11, 11))
                        and gk.legal_build(blocked, (x, y)) and any((px - x) ** 2 + (py - y) ** 2 <= r2 for px, py in att)]
            print(f"{scen} R{R} {lname} foreign={foreign} outside={outside} L={len(path)} {kind}: pool {len(pool)} legal {len(legal)} on_route {len(onroute)}; legal cells in range anywhere {len(alllegal)}")
