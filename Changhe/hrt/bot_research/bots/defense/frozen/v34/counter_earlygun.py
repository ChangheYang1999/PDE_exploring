"""Reproduction of astra's non-forecasting counter to fortress v21 (lane hrt-w1 test bot, not a candidate).

Round 1: gun1 at (3,1) + 3 factories. Rounds 2..growth: maximum factories, then tier5 waves, both via hrt-w3's
feature_bluff continuation (turret_round=0, growth_rounds=growth). From round lock_from on: saturate with the
defense planner (required_hp 1500, splash only) and buy factories with the rest.
Spec: bot_research.bots.defense.counter_earlygun:@make?growth=6&lock_from=10
"""
from bot_research.bots.counters.feature_bluff import make as _bluff
from bot_research.harness import gamekit as gk

from . import plan as P
from .fortress import _cost_of


def make(growth=6, lock_from=10):
    continuation = _bluff(turret_round=0, growth_rounds=growth)

    def decide(obs):
        me = obs["players"][obs["player"]]
        if lock_from is not None and obs["round"] >= lock_from:
            rules = gk.Rules.from_observation(obs)
            acts = P.plan_defense(obs, me["gold"], required_hp=1500, allow_guns=False, partial="best")
            left = me["gold"] - _cost_of(acts, rules)
            return acts + [{"op": "buy_factory"}] * max(0, min(80, left // rules.factory_cost))
        if obs["round"] != 1:
            return continuation(obs)
        return [{"op": "build_turret", "type": "gun1", "x": 3, "y": 1}] + [{"op": "buy_factory"}] * 3

    return decide
