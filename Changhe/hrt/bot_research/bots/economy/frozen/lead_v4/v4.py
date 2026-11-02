"""Lead v4 development bot: insurance core from hrt-w1's frozen planner (v7) plus a lead policy layer.

Spec: ``bot_research.experiments.lead.v4:@make?r1="poke"&r1_poke=2``

Policy each round (observation only):
  0. Layout walls (stage A of the default master layout) first, so every defence plan is made on
     the route that will exist after this round's construction.
  1. Round 1 (r1): "poke" buys r1_poke tier1 and factories; "guard" buys a gun2 at (1, 3) on the
     20-wall stage-A map (zero simulated leaks against every ordered roster costing at most 100,
     see experiments/lead/r1_search.py); "none" buys factories only.
  2. Mandatory defence: plan_defense against the opponent's visible active roster (partial plans
     allowed when zero leaks are unaffordable).
  3. Speculative insurance: zero leaks against the sampled affordable threat compositions if the
     plan costs at most spec_share of the remaining gold; otherwise the same for the compositions
     affordable with fractions ``grades[1:]`` of the opponent's gold, in order; otherwise zero
     leaks against the tier1/tier2 compositions only (poke insurance).
  4. Attack from attack_from: the tier with the most extra leaked damage per gold on the opponent's
     current map (exact simulation), using attack_share of the remaining gold, if that ratio is at
     least min_leak_per_gold.
  5. Factories with the rest (at most max_factories per round, none after last_factory_round).
"""
from __future__ import annotations

from bot_research.bots.defense.frozen.v7 import plan as P
from bot_research.harness import gamekit as gk

TIER_ORDER = ["tier5", "tier4", "tier3", "tier2", "tier1"]
GUARD_CELL = (1, 3)

DEFAULTS = dict(
    r1="poke", r1_poke=2,
    spec_share=0.6, poke_insurance=True, grades=(1.0,),
    attack_from=6, attack_share=0.5, min_leak_per_gold=0.1,
    max_factories=40, max_minions=60, last_factory_round=46,
    layout="default",
)


def _cost_of(actions, rules):
    total = 0
    for a in actions:
        op = a["op"]
        if op == "build_wall":
            total += rules.wall_cost
        elif op == "build_turret":
            total += rules.turrets[a["type"]]["cost"]
        elif op == "buy_factory":
            total += rules.factory_cost
        elif op == "buy_minion":
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


class Lead4:
    def __init__(self, **params):
        unknown = set(params) - set(DEFAULTS)
        if unknown:
            raise ValueError(f"unknown parameters {sorted(unknown)}")
        self.p = {**DEFAULTS, **params}
        lay = self.p["layout"]
        self.layout = P.layout_by_name(lay) if isinstance(lay, str) else lay

    def __call__(self, obs):
        p, layout = self.p, self.layout
        me = obs["players"][obs["player"]]
        rules = gk.Rules.from_observation(obs)
        rnd = obs["round"]
        left = me["gold"]
        actions = []

        def add(acts):
            nonlocal left
            actions.extend(acts)
            left -= _cost_of(acts, rules)

        # 0. layout walls
        add(P.plan_walls(obs, left, layout=layout, stage=0))
        o2 = _with_buildings(obs, actions, left)
        attack = []
        if rnd == 1:
            if p["r1"] == "guard":
                cell = GUARD_CELL
                blocked = gk.cells_of(o2["players"][obs["player"]]["buildings"])
                cost = rules.turrets["gun2"]["cost"]
                if left >= cost and cell not in blocked and gk.legal_build(blocked, cell):
                    add([{"op": "build_turret", "type": "gun2", "x": cell[0], "y": cell[1]}])
            elif p["r1"] == "poke":
                c = rules.minions["tier1"]["cost"]
                n = min(p["r1_poke"], left // c)
                attack = [{"op": "buy_minion", "type": "tier1"}] * n
                add(attack)
        else:
            # 1. mandatory defence against the visible roster
            visible = P.active_opponent_types(obs)
            if visible:
                add(P.plan_defense(o2, left, threat_types=[visible], layout=layout, partial="best"))
                o2 = _with_buildings(obs, actions, left)
            # 2. speculative insurance
            comps = P.threat_compositions(obs)
            if comps and left > 0:
                budget = int(left * p["spec_share"])
                spec = []
                opp_gold = obs["players"][1 - obs["player"]]["gold"]
                for i, f in enumerate(p["grades"]):
                    cf = comps if i == 0 else P.threat_compositions(obs, extra_gold=int(opp_gold * f))
                    spec = P.plan_defense(o2, budget, threat_types=cf, layout=layout, partial="none") if cf else []
                    if spec:
                        break
                if not spec and p["poke_insurance"]:
                    cheap = [c for c in comps if all(rules.minions[t]["hp"] <= 70 for t in c)]
                    if cheap:
                        spec = P.plan_defense(o2, budget, threat_types=cheap, layout=layout, partial="none")
                if spec:
                    add(spec)
                    o2 = _with_buildings(obs, actions, left)
            # 3. attack
            if rnd >= p["attack_from"] and left > 0:
                add(self._attack(obs, rules, int(left * p["attack_share"])))
        # 4. factories
        if rnd <= p["last_factory_round"]:
            n_f = min(p["max_factories"], left // rules.factory_cost)
            add([{"op": "buy_factory"}] * max(0, n_f))
        return actions

    def _attack(self, obs, rules, budget):
        p = self.p
        best = None
        _, base = P.opponent_leak(obs, [])
        for t in TIER_ORDER:
            c = rules.minions[t]["cost"]
            n = min(p["max_minions"], budget // c)
            if n <= 0:
                continue
            _, d = P.opponent_leak(obs, [t] * n)
            gain = (d - base) / (n * c)
            if gain >= p["min_leak_per_gold"] and (best is None or gain > best[0]):
                best = (gain, t, n)
        if best is None:
            return []
        _, t, n = best
        return [{"op": "buy_minion", "type": t}] * n


def make(**params):
    return Lead4(**params)
