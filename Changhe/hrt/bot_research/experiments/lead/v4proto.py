"""Prototype wrappers for cycle 3 (development only, not the entry point).

``bot_research.experiments.lead.v4proto:@fortress_poke?r1_poke=1&attack_from=6&attack_share=0.5``:
the frozen hrt-w1 fortress v4 policy, with ``r1_poke`` tier1 bought in round 1 in place of
factories (one factory per 20 gold given up, as needed).
"""
from __future__ import annotations

from bot_research.bots.defense.frozen.v4 import fortress as F


def fortress_poke(r1_poke=1, **params):
    core = F.make(**params)

    def decide(obs):
        actions = core(obs)
        if obs["round"] == 1 and r1_poke:
            me = obs["players"][obs["player"]]
            rules = obs["rules"]
            cost = rules["minions"]["tier1"]["cost"]
            fcost = rules["globals"]["factory_cost"]
            spent = 0
            for a in actions:
                if a["op"] == "build_wall":
                    spent += rules["wall_cost"]
                elif a["op"] == "build_turret":
                    spent += rules["turrets"][a["type"]]["cost"]
                elif a["op"] == "buy_factory":
                    spent += fcost
                elif a["op"] == "buy_minion":
                    spent += rules["minions"][a["type"]]["cost"]
            left = me["gold"] - spent
            need = r1_poke * cost
            while left < need and any(a["op"] == "buy_factory" for a in actions):
                i = max(i for i, a in enumerate(actions) if a["op"] == "buy_factory")
                del actions[i]
                left += fcost
            n = min(r1_poke, left // cost)
            actions = [{"op": "buy_minion", "type": "tier1"}] * n + actions
        return actions

    return decide
