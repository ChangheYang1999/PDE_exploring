"""Is the lock still reachable? Per-round check on a replayed match (hrt-w2, loss review).

Usage (from the project root, PYTHONPATH=.):
    python -B -m bot_research.experiments.economy.reach_check SPEC_A SPEC_B PLAYER ROUNDS [SCENARIO]
ROUNDS is a comma list. Replays the match once (unchanged engine; harness scenario as in
obs_replay.py) and at each listed round takes PLAYER's observation. With the own gold set to
10**7 it asks hrt-w1's frozen v15 plan_defense for a splash plan reaching per-copy splash
TARGET (1600, econ17's sat_target; also 1500, the tier5 HP) with partial="none", once with the
lead_v3 layout and once with the empty layout (as econ17's defend does). An empty answer from
both while the map is below the target means: no plan of this planner reaches the target with
unlimited gold. Prints the own per-copy splash, empty cells, both answers (cost of the plan or
"none") and the planner time.
"""
from __future__ import annotations

import copy
import sys
import time

from td_bots.protocol import collect_actions
from td_game.config import balanced_config
from td_game.engine import Engine

from bot_research.bots.defense.frozen.v15 import plan as P
from bot_research.bots.economy.frozen.v18 import econ18 as E
from bot_research.experiments.economy.obs_replay import _Bot
from bot_research.harness import gamekit as gk
from bot_research.harness import scenarios
from bot_research.harness.match import resolve_spec

BIG = 10 ** 7


def reach(obs, target, layout):
    o = E._with(obs, [], BIG)
    t0 = time.time()
    acts = P.plan_defense(o, BIG, required_hp=target, layout=layout, partial="none", time_budget=1e6)
    return acts, time.time() - t0


def report(obs, rnd):
    rules = obs["rules"]
    grules = gk.Rules.from_observation(obs)
    me = obs["players"][obs["player"]]
    _, rl, buildings, blocked = P.observe(obs)
    path = gk.route_cached(blocked)
    empty = sum(1 for x in range(12) for y in range(12)
                if (x, y) not in blocked and (x, y) not in set(path) and (x, y) not in ((0, 0), (11, 11)))
    s = P.splash_damage(me["buildings"], grules)
    out = [f"r{rnd:2d} S {s:5d} empty {empty:3d} gold {me['gold']:6d}"]
    lay = P.layout_by_name("lead_v3")
    free = P.MasterLayout([], [], [], [0, 0, 0], {}, set(), 0)
    for target in (1600, 1500):
        for name, layout in (("lead_v3", lay), ("empty", free)):
            if s >= target:
                out.append(f"{target}/{name}: reached")
                continue
            acts, dt = reach(obs, target, layout)
            res = f"cost {E._cost(acts, rules)}" if acts else "none"
            out.append(f"{target}/{name}: {res} ({dt:.1f} s)")
    print(" | ".join(out), flush=True)


def main():
    spec_a, spec_b, player = sys.argv[1], sys.argv[2], int(sys.argv[3])
    rounds = sorted(int(r) for r in sys.argv[4].split(","))
    scen = sys.argv[5] if len(sys.argv) > 5 else None
    engine = Engine(balanced_config(), ("A", "B"))
    over = scenarios.make_overrides(scen) if scen else (None, None)
    bots = [_Bot(resolve_spec(s), o) for s, o in zip((spec_a, spec_b), over)]
    print(f"{spec_a} vs {spec_b}, player {player}, scenario {scen}")
    while engine.result is None and rounds:
        obs = [engine.observation(p) for p in (0, 1)]
        if obs[0]["round"] == rounds[0]:
            report(copy.deepcopy(obs[player]), rounds.pop(0))
        actions, errors = collect_actions(bots, obs)
        engine.play_round(actions, errors)


if __name__ == "__main__":
    main()
