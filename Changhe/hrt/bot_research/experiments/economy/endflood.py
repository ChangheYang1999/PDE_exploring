"""Development counter (hrt-w2): any bot, plus an all-gold flood in the last rounds.

Spec: ``bot_research.experiments.economy.endflood:@make?base="MODULE:@factory"&flood_round=48``
(the base spec is resolved by the lead's harness resolver; give a base with
parameters URL-encoded). Rounds before ``flood_round``: the base bot's actions
unchanged. From ``flood_round`` on: the base bot's wall and turret purchases are
kept, its other purchases dropped, and the remaining gold buys copies of
``tier`` (at most ``cap`` per round). The bot reads only its observation.
Purpose: test whether a candidate whose map ends below per-copy splash 1500 (the
tier5 HP) is exposed to a final flood by an opponent that otherwise plays like
the base bot (notes/economy.md, entry 6).
"""
from __future__ import annotations

from bot_research.harness.match import resolve_spec


def make(base="bot_research.bots.defense.frozen.v21.fortress:@make", flood_round=48, tier="tier5", cap=1000):
    inner = resolve_spec(base)

    def decide(obs):
        acts = inner(obs)
        if obs["round"] < flood_round:
            return acts
        rules = obs["rules"]
        left = obs["players"][obs["player"]]["gold"]
        kept = []
        for a in acts:
            if a["op"] == "build_wall":
                kept.append(a)
                left -= rules["wall_cost"]
            elif a["op"] == "build_turret":
                kept.append(a)
                left -= rules["turrets"][a["type"]]["cost"]
        n = max(0, min(cap, left // rules["minions"][tier]["cost"]))
        return kept + [{"op": "buy_minion", "type": tier}] * n

    return decide
