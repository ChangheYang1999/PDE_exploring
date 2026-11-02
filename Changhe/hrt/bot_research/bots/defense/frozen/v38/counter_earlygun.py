"""Reproduction of astra's non-forecasting counter to fortress v21 (lane hrt-w1 test bot, not a candidate).

Round 1: gun1 at (3,1) + 3 factories. Rounds 2..growth: maximum factories, then tier5 waves, both via hrt-w3's
feature_bluff continuation (turret_round=0, growth_rounds=growth). From round lock_from on: saturate with the
defense planner (required_hp 1500, splash only) and buy factories with the rest.
Spec: bot_research.bots.defense.counter_earlygun:@make?growth=6&lock_from=10
Options added 2026-10-31 (defaults reproduce the original schedule exactly): tier (the wave tier of the continuation,
"tier5"; "tier4" gives a round-5 striker with growth=4), guard_round (None; a round in which one splash is built at
guard_cell (10,1), killing tier1/tier2 pokes), gun_cell ((3,1); the round-1 gun1 cell).
"""
from bot_research.bots.counters.feature_bluff import make as _bluff
from bot_research.harness import gamekit as gk

from . import plan as P
from .fortress import _cost_of


def make(growth=6, lock_from=10, tier="tier5", guard_round=None, guard_cell=(10, 1), gun_cell=(3, 1)):
    continuation = _bluff(turret_round=0, growth_rounds=growth, tier=tier)

    def decide(obs):
        me = obs["players"][obs["player"]]
        if lock_from is not None and obs["round"] >= lock_from:
            rules = gk.Rules.from_observation(obs)
            acts = P.plan_defense(obs, me["gold"], required_hp=1500, allow_guns=False, partial="best")
            left = me["gold"] - _cost_of(acts, rules)
            return acts + [{"op": "buy_factory"}] * max(0, min(80, left // rules.factory_cost))
        if obs["round"] != 1:
            acts = continuation(obs)
            if guard_round is not None and obs["round"] == int(guard_round):
                # one splash guard first (60 gold), then the continuation's purchases with the gold that remains
                acts = [{"op": "build_turret", "type": "splash", "x": guard_cell[0], "y": guard_cell[1]}] + list(acts)
                rules = gk.Rules.from_observation(obs)
                budget = me["gold"] - rules.turrets["splash"]["cost"]
                kept = []
                for a in acts[1:]:
                    c = rules.factory_cost if a["op"] == "buy_factory" else rules.minions[a["type"]]["cost"] if a["op"] == "buy_minion" else 0
                    if c <= budget:
                        kept.append(a)
                        budget -= c
                acts = acts[:1] + kept
            return acts
        return [{"op": "build_turret", "type": "gun1", "x": gun_cell[0], "y": gun_cell[1]}] + [{"op": "buy_factory"}] * 3

    return decide
