"""Layout reach on scripted-opening maps: base lead_v3 layout against two re-planners (hrt-w2 analysis).

Usage (project root): python -B -m bot_research.experiments.economy.replan_reach SCEN [SCEN ...]
For each scenario and seat, plays the scripted rounds with idle bots (the scripted actions replace the
bots' actions, so the own map at the first free decision does not depend on the bots), then reports at
that round, for the own buildings:
- base: S_final of the lead_v3 layout built as far as legal (econ25._s_final, hrt-w1 v26 scorer);
- v26: hrt-w1 frozen v26 replan_layout(iters=5000, seed=round), as used by econ20-econ25;
- v34: hrt-w1 frozen v34 replan_layout(iters=5000, seed=round, objective "best"), as used by fortress v34;
each with S_final (v26 scorer, 25 slots plus existing splashes) and the final route length.
"""
from __future__ import annotations

import sys

from td_game.config import balanced_config
from td_game.engine import Engine
from td_bots.protocol import collect_actions

from bot_research.bots.defense.frozen.v15 import plan as P
from bot_research.bots.defense.frozen.v26 import replan as R26
from bot_research.bots.defense.frozen.v34 import replan as R34
from bot_research.bots.economy.frozen.v25 import econ25 as E25
from bot_research.experiments.economy.obs_replay import _Bot
from bot_research.harness import scenarios


def own_map(scen):
    k = int(scen.split(":")[-1])
    engine = Engine(balanced_config(), ("A", "B"))
    over = scenarios.make_overrides(scen)
    bots = [_Bot(lambda o: [], ov) for ov in over]
    while engine.result is None:
        obs = [engine.observation(p) for p in (0, 1)]
        if obs[0]["round"] == k + 1:
            return obs
        actions, errors = collect_actions(bots, obs)
        engine.play_round(actions, errors)
    return None


def main(argv):
    base = P.layout_by_name("lead_v3")
    print("scenario seat round n_build base v26_S v26_L v34_S v34_L", flush=True)
    for scen in argv:
        obs = own_map(scen)
        if obs is None:
            print(scen, "ended during the scripted rounds", flush=True)
            continue
        seats = (0,) if scen.startswith("mirror") else (0, 1)
        for p in seats:
            b = obs[p]["players"][p]["buildings"]
            rnd = obs[p]["round"]
            l26 = R26.replan_layout(b, iters=5000, seed=rnd)
            l34 = R34.replan_layout(b, iters=5000, seed=rnd)
            print(scen, p, rnd, len(b), E25._s_final(b, base), E25._s_final(b, l26), l26.final_len,
                  E25._s_final(b, l34), l34.final_len, flush=True)


if __name__ == "__main__":
    main(sys.argv[1:])
