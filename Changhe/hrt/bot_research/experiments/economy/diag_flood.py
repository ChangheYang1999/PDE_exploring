"""Defence options on one recorded observation of a late flood (loss review, hrt-w2).

Usage (from the project root, PYTHONPATH=.):
    python -B -m bot_research.experiments.economy.diag_flood SPEC_A SPEC_B PLAYER ROUND [SCENARIO]
Replays the match (unchanged engine, harness scenario if given) up to ROUND and takes
PLAYER's observation. Prints own/opponent gold, factories, route length, per-copy splash,
the number of empty legal cells off the route, the worst simulated damage of hrt-w1's
threat_compositions (frozen v15 planner) on the current map, and for the full own gold:
hrt-w1's plan_defense with the lead_v3 layout (partial "best" and "none"), the same with the
empty layout, and this lane's free_plan (frozen v17), each with its cost and the worst
simulated damage after it.
"""
from __future__ import annotations

import sys
import time
from collections import Counter

from bot_research.bots.defense.frozen.v15 import plan as P
from bot_research.bots.economy.frozen.v17 import econ17 as E
from bot_research.bots.economy.frozen.v17.freeplan import free_plan
from bot_research.experiments.economy.obs_replay import observation_at
from bot_research.harness import gamekit as gk


def main():
    spec_a, spec_b, player, rnd = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4])
    scen = sys.argv[5] if len(sys.argv) > 5 else None
    obs = observation_at(spec_a, spec_b, rnd, player, scenario=scen)
    rules = obs["rules"]
    me, op = obs["players"][player], obs["players"][1 - player]
    grules = gk.Rules.from_observation(obs)
    _, rl, buildings, blocked = P.observe(obs)
    path = gk.route_cached(blocked)
    on_route = set(path)
    empty = 0
    for x in range(12):
        for y in range(12):
            c = (x, y)
            if c in blocked or c in on_route or c in ((0, 0), (11, 11)):
                continue
            empty += 1
    print(f"round {rnd} player {player} scenario {scen}")
    for name, p in (("own", me), ("opp", op)):
        print(f"  {name}: hp {p['hp']} gold {p['gold']} factories {p['n_factories']} turrets {p['n_turrets']} "
              f"walls {p['n_walls']} L {p['length_path']} roster {len(p['roster'])}")
    print(f"  own per-copy splash {P.splash_damage(me['buildings'], grules)}, empty legal-candidate cells off route {empty}")
    comps = P.threat_compositions(obs)
    print(f"  threat compositions {len(comps)}; largest {max(len(c) for c in comps) if comps else 0} copies")
    print(f"  worst damage now {E._worst_damage(obs, comps) if comps else 0}")
    gold = me["gold"]
    lay = P.layout_by_name("lead_v3")
    free = P.MasterLayout([], [], [], [0, 0, 0], {}, set(), 0)
    for label, fn in (
            ("plan_defense lead_v3 best", lambda: P.plan_defense(obs, gold, layout=lay, threat_types=comps,
                                                                 time_budget=1e6, partial="best")),
            ("plan_defense lead_v3 none", lambda: P.plan_defense(obs, gold, layout=lay, threat_types=comps,
                                                                 time_budget=1e6, partial="none")),
            ("plan_defense empty best", lambda: P.plan_defense(obs, gold, layout=free, threat_types=comps,
                                                               time_budget=1e6, partial="best")),
            ("free_plan best", lambda: free_plan(obs, gold, comps, partial="best"))):
        t0 = time.time()
        acts = fn()
        dt = time.time() - t0
        cost = E._cost(acts, rules)
        after = E._with(obs, acts, gold - cost)
        worst = E._worst_damage(after, comps) if comps else 0
        cnt = Counter(a["op"] + ":" + a.get("type", "") for a in acts)
        print(f"  {label}: {len(acts)} actions, cost {cost}, worst damage after {worst}, {dt:.1f} s, {dict(cnt)}")


if __name__ == "__main__":
    main()
