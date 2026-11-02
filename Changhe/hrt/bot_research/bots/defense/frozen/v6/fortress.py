"""Fortress: defence-first research bot built on plan_defense (lane hrt-w1).

Spec: ``bot_research.bots.defense.fortress:@make?spec_share=0.6&attack="opportunistic"``

Policy each round (all planning from the observation only):
  1. Mandatory defence: zero simulated leaks against the opponent's VISIBLE active roster (it will
     attack this round for certain). Partial plans allowed if zero leaks are unaffordable.
  2. Speculative defence: zero leaks against every purchase bundle the opponent's visible gold allows
     this round, but only if such a plan costs <= spec_share * remaining gold (never a partial plan:
     a defence that still leaks a tier5 is wasted gold better compounded).
  3. Layout walls for route income (stage A, 1 gold each; the route grows to 44).
  4. Attack (attack="opportunistic", from round attack_from): if minions of some tier would leak
     base damage on the opponent's CURRENT map (exact simulation of my roster + purchase), buy the
     tier with the best leaked damage per gold using attack_share of the remaining gold.
     attack="none": pure turtle. attack="flood": from attack_from, all remaining gold on attack_tier.
  5. Factories with the rest (capped per round: unbounded factory lists make multi-GB logs).

Parameters (JSON in the spec): spec_share (0.6), attack ("opportunistic"), attack_from (3),
attack_share (0.7), attack_tier ("tier5"), min_leak_per_gold (0.1), walls (True),
layout ("default" | "annealed25" | "pillars774" | "lead_v3", see plan.layout_by_name / templates.py),
poke_insurance (True: when the full speculative plan is unaffordable, still buy zero leaks against the
tier1/tier2 bundles the opponent can afford), round1 (None | "splash" | "gun2": blind round-1 turret at (10,1)).
"""
from __future__ import annotations

from bot_research.harness import gamekit as gk

from . import plan as P

MAX_FACTORIES_PER_ROUND = 40
MAX_MINIONS_PER_ROUND = 60
TIER_ORDER = ["tier5", "tier4", "tier3", "tier2", "tier1"]


def _cost_of(actions, rules):
    total = 0
    for a in actions:
        if a["op"] == "build_wall":
            total += rules.wall_cost
        elif a["op"] == "build_turret":
            total += rules.turrets[a["type"]]["cost"]
        elif a["op"] == "buy_factory":
            total += rules.factory_cost
        elif a["op"] == "buy_minion":
            total += rules.minions[a["type"]]["cost"]
    return total


def _with_buildings(obs, actions, gold):
    """Copy of the observation with planned buildings added and gold set (own side only)."""
    me = obs["players"][obs["player"]]
    new_me = dict(me)
    new_me["buildings"] = list(me["buildings"]) + [
        {"x": a["x"], "y": a["y"], "type": "wall" if a["op"] == "build_wall" else a["type"]}
        for a in actions if a["op"] in ("build_wall", "build_turret")]
    new_me["gold"] = gold
    players = list(obs["players"])
    players[obs["player"]] = new_me
    o2 = dict(obs)
    o2["players"] = players
    return o2


def make(spec_share=0.6, attack="opportunistic", attack_from=3, attack_share=0.7, attack_tier="tier5",
         min_leak_per_gold=0.1, walls=True, layout="default", poke_insurance=True, round1=None):
    layout = P.layout_by_name(layout) if isinstance(layout, str) or layout is None else layout

    def decide(obs):
        me = obs["players"][obs["player"]]
        rules = gk.Rules.from_observation(obs)
        gold = me["gold"]
        rnd = obs["round"]
        actions = []
        # 1. mandatory defence against the visible roster
        visible = P.active_opponent_types(obs)
        if visible:
            actions += P.plan_defense(obs, gold, threat_types=[visible], layout=layout, partial="best")
        left = gold - _cost_of(actions, rules)
        o2 = _with_buildings(obs, actions, left)
        # 2. speculative defence against affordable purchases, only if cheap enough
        comps = P.threat_compositions(obs)
        if comps and left > 0:
            spec = P.plan_defense(o2, int(left * spec_share), threat_types=comps, layout=layout, partial="none")
            if not spec and poke_insurance:
                # fall back to zero leaks against the cheap pokes only (tier1/tier2 bundles)
                cheap = [c for c in comps if all(rules.minions[t]["hp"] <= 70 for t in c)]
                if cheap:
                    spec = P.plan_defense(o2, int(left * spec_share), threat_types=cheap, layout=layout, partial="none")
            if spec:
                actions += spec
                left -= _cost_of(spec, rules)
                o2 = _with_buildings(obs, actions, left)
        # 2b. blind round-1 option
        if rnd == 1 and round1 and left >= 60 and not any(a["op"] == "build_turret" for a in actions):
            cell = {"splash": (10, 1), "gun2": (10, 1)}[round1]
            kind = round1
            cost = rules.turrets[kind]["cost"]
            if left >= cost:
                actions.append({"op": "build_turret", "type": kind, "x": cell[0], "y": cell[1]})
                left -= cost
                o2 = _with_buildings(obs, actions, left)
        # 3. route-income walls
        if walls and left > 0:
            w = P.plan_walls(o2, left, layout=layout, stage=0)
            actions += w
            left -= _cost_of(w, rules)
        # 4. attack
        if attack != "none" and rnd >= attack_from and left > 0:
            budget = int(left * attack_share)
            bought = []
            if attack == "flood":
                order = [attack_tier] + [t for t in TIER_ORDER if t != attack_tier]
                for t in order:
                    c = rules.minions[t]["cost"]
                    while budget >= c and len(bought) < MAX_MINIONS_PER_ROUND:
                        bought.append(t)
                        budget -= c
            else:
                best = None
                base_hits, base_dmg = P.opponent_leak(obs, [])
                for t in TIER_ORDER:
                    c = rules.minions[t]["cost"]
                    n = min(MAX_MINIONS_PER_ROUND, budget // c)
                    if n <= 0:
                        continue
                    h, d = P.opponent_leak(obs, [t] * n)
                    gain = (d - base_dmg) / (n * c)
                    if gain >= min_leak_per_gold and (best is None or gain > best[0]):
                        best = (gain, t, n)
                if best is not None:
                    _, t, n = best
                    bought = [t] * n
            actions += [{"op": "buy_minion", "type": t} for t in bought]
            left -= _cost_of([{"op": "buy_minion", "type": t} for t in bought], rules)
        # 5. factories
        n_f = min(MAX_FACTORIES_PER_ROUND, left // rules.factory_cost)
        actions += [{"op": "buy_factory"}] * max(0, n_f)
        return actions

    return decide


def decide(obs):
    """Module-level default (stateless) for the plain module:function form."""
    return make()(obs)
