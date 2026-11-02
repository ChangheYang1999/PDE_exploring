"""Round-by-round decisions of econ15 settings on one recorded observation (loss review, hrt-w2).

Usage (from the project root, PYTHONPATH=.):
    python -B -m bot_research.experiments.economy.diag_bluff SPEC_A SPEC_B PLAYER ROUND [SETTINGS_JSON ...]
Replays the match of SPEC_A vs SPEC_B (standard start) up to ROUND, takes PLAYER's
observation and prints, for each econ15 parameter dict, the returned actions
counted by op:type and their cost, plus the opponent's gold and the worst
simulated damage of hrt-w1's threat_compositions on the resulting own map.
"""
from __future__ import annotations

import json
import sys
from collections import Counter

from bot_research.bots.defense.frozen.v15 import plan as P
from bot_research.bots.economy.frozen.v15 import econ15
from bot_research.experiments.economy.obs_replay import observation_at
from bot_research.harness import gamekit as gk


def _cost(actions, rules):
    return econ15._cost(actions, rules)


def main():
    spec_a, spec_b, player, rnd = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4])
    settings = [json.loads(s) for s in sys.argv[5:]] or [{}]
    obs = observation_at(spec_a, spec_b, rnd, player)
    me = obs["players"][player]
    op = obs["players"][1 - player]
    rules = obs["rules"]
    print(f"round {rnd} player {player}: gold {me['gold']} factories {me['n_factories']} "
          f"route {me['length_path']}; opponent gold {op['gold']} factories {op['n_factories']} "
          f"turrets {op['n_turrets']}")
    comps = P.threat_compositions(obs)
    for kw in settings:
        acts = econ15.make(**kw)(obs)
        cnt = Counter(a["op"] + (":" + a["type"] if a.get("type") else "") for a in acts)
        left = me["gold"] - _cost(acts, rules)
        o2 = econ15._with(obs, acts, left)
        _, rl, b, bl = P.observe(o2)
        score, hits = P._leak(b, bl, rl, comps)
        path = gk.route_cached(bl)
        worst = 0
        from bot_research.bots.defense.frozen.v15.simulate import simulate_leak
        for types in comps:
            h, d, _ = simulate_leak(types, path, b, rl)
            worst = max(worst, d)
        print(json.dumps(kw), dict(cnt), "cost", _cost(acts, rules), "leak score", score,
              "leaking rosters", hits, "of", len(comps), "worst damage", worst)


if __name__ == "__main__":
    main()
