"""Timing-attack probe: pure economy, one all-in attack, then saturation.

Spec: ``bot_research.bots.economy.timing:@make?attack_round=5``.

Rounds before ``attack_round``: all gold on factories (at most ``fac_cap``).
Round ``attack_round``: the package with the largest simulated damage on the
opponent's current map (offense.search, optimistic: the opponent builds
nothing) among packages costing at most ``attack_frac`` of the gold.
With ``pre_defend`` the rounds up to the attack also defend against the
opponent's visible roster plus packages of at most ``pre_gold`` gold.
Later rounds: defence.defend against the opponent's visible roster and full
gold, then splash saturation with the rest up to per-copy splash
``sat_target``, then factories until ``factory_stop``. With ``repeat`` it
also attacks in every later round in which the opponent's per-copy splash on
its route is below the HP of tier5.
Written to probe the early-round windows of the economy bot; it reads only
its observation.
"""
from __future__ import annotations

from .defense_plan import defend, saturate
from .fastsim import MapModel
from .offense import search
from .threat import active_types


def _tuples(buildings):
    return [(b["x"], b["y"], b["type"]) for b in buildings]


def make(attack_round=5, fac_cap=40, attack_frac=1.0, sat_target=1600, factory_stop=47,
         repeat=False, pre_defend=False, pre_gold=0):
    def decide(obs):
        rnd = obs["round"]
        me_i = obs["player"]
        me = obs["players"][me_i]
        op = obs["players"][1 - me_i]
        rules = obs["rules"]
        g = rules["globals"]
        gold = me["gold"]
        fcost = g["factory_cost"]
        actions = []
        my_b = _tuples(me["buildings"])
        if rnd <= attack_round and pre_defend:
            # before the attack: defend the visible roster (plus packages of pre_gold)
            d, my_b, gold, _ = defend(my_b, gold, active_types(op["roster"], rnd),
                                      min(op["gold"], pre_gold), rules, cap=600)
            actions += d
        if rnd > attack_round:
            d, my_b, gold, _ = defend(my_b, gold, active_types(op["roster"], rnd), op["gold"], rules,
                                      cap=600)
            actions += d
            s, my_b, gold, _ = saturate(my_b, gold, sat_target, rules)
            actions += s
        attack_now = rnd == attack_round
        if repeat and rnd > attack_round:
            opp_S = MapModel(_tuples(op["buildings"]), rules).splash_total
            attack_now = opp_S < rules["minions"]["tier5"]["hp"]
        if attack_now and gold >= rules["minions"]["tier1"]["cost"]:
            my_active = active_types(me["roster"], rnd)
            res, _ = search(_tuples(op["buildings"]), my_active, int(gold * attack_frac), rules,
                            cap=400, responded=False, active_cap=len(my_active) + 400)
            best = max(res, key=lambda r: (r[2], -r[1]), default=None)
            if best is not None and best[2] > 0:
                actions += [{"op": "buy_minion", "type": t} for t in best[0]]
                gold -= best[1]
        if rnd <= factory_stop and rnd < g["max_rounds"] - 1:
            n = max(0, min(fac_cap, gold // fcost))
            actions += [{"op": "buy_factory"}] * n
        return actions

    return decide
