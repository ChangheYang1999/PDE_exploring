"""Materially different baseline opponents (lead lane).

Use with the factory spec form, e.g. ``bot_research.harness.baselines:@rush?tier="tier2"``.

greedy_eco()                      factories only, never defends or attacks.
rush(tier="tier1", eco=0.0)       every round spends (1-eco) of gold on the given minion tier,
                                  the rest on factories.
eco_then_flood(switch=8, tier="tier5")
                                  factories until round ``switch``-1, then all gold on minions of
                                  ``tier`` (falling back to the best affordable tier).
splash_turtle(eco=0.5)            greedy splash placement maximising per-copy splash damage, plus
                                  factories with the remaining share; never attacks.
gun_turtle(eco=0.5)               greedy gun2/gun1 placement maximising lone-copy gun damage, plus
                                  factories; never attacks.
maze_eco()                        walls that lengthen the route (path income), then factories.
random_legal(seed=0)              seeded random legal mixtures of all action kinds.

threat_defender(attack_after=10, margin=1.0)
                                  keeps per-copy splash damage >= margin x the highest HP the
                                  opponent fields or can afford this round, buys factories with the
                                  surplus, and floods the best affordable tier after ``attack_after``.

Practical caps: the engine has no action limit, but unbounded factory compounding
reaches millions of actions per round (a 1.1 GB log per match was observed for an
uncapped factory-only bot). Every baseline therefore buys at most
MAX_FACTORIES_PER_ROUND factories and MAX_MINIONS_PER_ROUND minions per round.
"""
from __future__ import annotations

import random

from bot_research.harness import gamekit as gk

TIER_ORDER = ["tier1", "tier2", "tier3", "tier4", "tier5"]
MAX_FACTORIES_PER_ROUND = 40
MAX_MINIONS_PER_ROUND = 60


def _me(obs):
    return obs["players"][obs["player"]]


def _opp(obs):
    return obs["players"][1 - obs["player"]]


def _factories(gold, cost=20):
    return [{"op": "buy_factory"}] * max(0, min(MAX_FACTORIES_PER_ROUND, gold // cost))


def greedy_eco():
    def decide(obs):
        return _factories(_me(obs)["gold"], obs["rules"]["globals"]["factory_cost"])
    return decide


def rush(tier="tier1", eco=0.0):
    def decide(obs):
        rules = gk.Rules.from_observation(obs)
        gold = _me(obs)["gold"]
        attack = int(gold * (1 - eco))
        n = min(MAX_MINIONS_PER_ROUND, attack // rules.minions[tier]["cost"])
        actions = [{"op": "buy_minion", "type": tier}] * n
        gold -= n * rules.minions[tier]["cost"]
        return actions + _factories(gold, rules.factory_cost)
    return decide


def _flood(gold, rules, tier=None):
    actions = []
    order = [tier] if tier else []
    order += [t for t in reversed(TIER_ORDER) if t not in order]
    for t in order:
        c = rules.minions[t]["cost"]
        while gold >= c and len(actions) < MAX_MINIONS_PER_ROUND:
            actions.append({"op": "buy_minion", "type": t})
            gold -= c
    return actions, gold


def eco_then_flood(switch=8, tier="tier5"):
    def decide(obs):
        rules = gk.Rules.from_observation(obs)
        gold = _me(obs)["gold"]
        if obs["round"] < switch:
            return _factories(gold, rules.factory_cost)
        actions, _ = _flood(gold, rules, tier)
        return actions
    return decide


def _best_splash_cell(buildings, rules):
    """Cell maximising total per-copy splash damage after placing a splash there."""
    blocked = gk.cells_of(buildings)
    best = None
    for x in range(12):
        for y in range(12):
            cell = (x, y)
            if not gk.legal_build(blocked, cell):
                continue
            new = buildings + [{"x": x, "y": y, "type": "splash"}]
            path = gk.route_cached(blocked | {cell})
            score = gk.splash_total(path, new, rules) * 1000 + len(path)
            if best is None or score > best[0]:
                best = (score, cell)
    return None if best is None else best[1]


def _best_gun_cell(buildings, rules, kind):
    blocked = gk.cells_of(buildings)
    best = None
    for x in range(12):
        for y in range(12):
            cell = (x, y)
            if not gk.legal_build(blocked, cell):
                continue
            new = buildings + [{"x": x, "y": y, "type": kind}]
            path = gk.route_cached(blocked | {cell})
            lone = sum(d * len(idx) for d, idx in gk.gun_coverage(path, new, rules))
            score = lone * 1000 + len(path)
            if best is None or score > best[0]:
                best = (score, cell)
    return None if best is None else best[1]


def splash_turtle(eco=0.5):
    def decide(obs):
        rules = gk.Rules.from_observation(obs)
        me = _me(obs)
        gold = me["gold"]
        buildings = list(me["buildings"])
        actions = []
        budget = int(gold * (1 - eco))
        cost = rules.turrets["splash"]["cost"]
        while budget >= cost:
            cell = _best_splash_cell(buildings, rules)
            if cell is None:
                break
            actions.append({"op": "build_turret", "type": "splash", "x": cell[0], "y": cell[1]})
            buildings.append({"x": cell[0], "y": cell[1], "type": "splash"})
            budget -= cost
            gold -= cost
        return actions + _factories(gold, rules.factory_cost)
    return decide


def gun_turtle(eco=0.5):
    def decide(obs):
        rules = gk.Rules.from_observation(obs)
        me = _me(obs)
        gold = me["gold"]
        buildings = list(me["buildings"])
        actions = []
        budget = int(gold * (1 - eco))
        while True:
            kind = "gun2" if budget >= rules.turrets["gun2"]["cost"] else (
                "gun1" if budget >= rules.turrets["gun1"]["cost"] else None)
            if kind is None:
                break
            cell = _best_gun_cell(buildings, rules, kind)
            if cell is None:
                break
            actions.append({"op": "build_turret", "type": kind, "x": cell[0], "y": cell[1]})
            buildings.append({"x": cell[0], "y": cell[1], "type": kind})
            budget -= rules.turrets[kind]["cost"]
            gold -= rules.turrets[kind]["cost"]
        return actions + _factories(gold, rules.factory_cost)
    return decide


def _best_wall(blocked):
    base = len(gk.route_cached(blocked))
    best = None
    for x in range(12):
        for y in range(12):
            cell = (x, y)
            if not gk.legal_build(blocked, cell):
                continue
            gain = len(gk.route_cached(blocked | {cell})) - base
            if gain > 0 and (best is None or gain > best[0]):
                best = (gain, cell)
    return best


def maze_eco():
    def decide(obs):
        rules = gk.Rules.from_observation(obs)
        me = _me(obs)
        gold = me["gold"]
        blocked = gk.cells_of(me["buildings"])
        actions = []
        # Greedy: walls that lengthen the route by at least one step pay back within a round.
        while gold >= rules.wall_cost:
            best = _best_wall(blocked)
            if best is None:
                break
            blocked.add(best[1])
            actions.append({"op": "build_wall", "x": best[1][0], "y": best[1][1]})
            gold -= rules.wall_cost
        return actions + _factories(gold, rules.factory_cost)
    return decide


def random_legal(seed=0):
    def decide(obs):
        rng = random.Random(seed * 7919 + obs["round"] * 31 + obs["player"])
        rules = gk.Rules.from_observation(obs)
        me = _me(obs)
        gold = me["gold"]
        blocked = gk.cells_of(me["buildings"])
        actions = []
        for _ in range(40):
            if gold <= 0:
                break
            choice = rng.random()
            if choice < 0.35:
                if gold < rules.factory_cost:
                    continue
                actions.append({"op": "buy_factory"})
                gold -= rules.factory_cost
            elif choice < 0.6:
                t = rng.choice(TIER_ORDER[:3])
                if gold >= rules.minions[t]["cost"]:
                    actions.append({"op": "buy_minion", "type": t})
                    gold -= rules.minions[t]["cost"]
            elif choice < 0.85:
                t = rng.choice(list(rules.turrets))
                cell = (rng.randrange(12), rng.randrange(12))
                if gold >= rules.turrets[t]["cost"] and gk.legal_build(blocked, cell):
                    actions.append({"op": "build_turret", "type": t, "x": cell[0], "y": cell[1]})
                    blocked.add(cell)
                    gold -= rules.turrets[t]["cost"]
            else:
                cell = (rng.randrange(12), rng.randrange(12))
                if gk.legal_build(blocked, cell):
                    actions.append({"op": "build_wall", "x": cell[0], "y": cell[1]})
                    blocked.add(cell)
                    gold -= rules.wall_cost
        return actions
    return decide


def _max_threat_hp(obs, rules):
    opp = _opp(obs)
    hps = [rules.minions[t]["hp"] for t in gk.active_types(opp["roster"], obs["round"])]
    hps += [m["hp"] for m in rules.minions.values() if m["cost"] <= opp["gold"]]
    return max(hps, default=0)


def threat_defender(attack_after=10, margin=1.0):
    def decide(obs):
        rules = gk.Rules.from_observation(obs)
        me = _me(obs)
        gold = me["gold"]
        buildings = list(me["buildings"])
        actions = []
        need = _max_threat_hp(obs, rules) * margin
        cost = rules.turrets["splash"]["cost"]
        path = gk.route_cached(gk.cells_of(buildings))
        while gk.splash_total(path, buildings, rules) < need and gold >= cost:
            cell = _best_splash_cell(buildings, rules)
            if cell is None:
                break
            actions.append({"op": "build_turret", "type": "splash", "x": cell[0], "y": cell[1]})
            buildings.append({"x": cell[0], "y": cell[1], "type": "splash"})
            gold -= cost
            path = gk.route_cached(gk.cells_of(buildings))
        if obs["round"] > attack_after:
            more, gold = _flood(gold, rules)
            actions += more
        return actions + _factories(gold, rules.factory_cost)
    return decide
