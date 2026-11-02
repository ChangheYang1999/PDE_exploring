"""Lead v4b development bot: v4 plus poke-insurance budget and response-aware attack options.

Spec: ``bot_research.experiments.lead.v4b:@make?attack_mode="adaptive"``

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
     least min_leak_per_gold. attack_mode "current" uses that rule as is; "robust" also requires
     a leak after the opponent's estimated best same-round response (plan_defense from the
     opponent's side with resp_share of its visible gold against exactly the attacking roster);
     "adaptive" uses "current" until fail_limit attacks have dealt less than half of their
     predicted damage, then "robust". Attack outcomes are judged from the opponent's HP in the
     next observation (own state only).
  5. Factories with the rest (at most max_factories per round, none after last_factory_round).
"""
from __future__ import annotations

from bot_research.bots.defense.frozen.v7 import plan as P
from bot_research.harness import gamekit as gk

TIER_ORDER = ["tier5", "tier4", "tier3", "tier2", "tier1"]
GUARD_CELL = (1, 3)

DEFAULTS = dict(
    r1="poke", r1_poke=2,
    spec_share=0.6, poke_insurance=True, poke_share=None, grades=(1.0,),
    attack_from=6, attack_share=0.5, min_leak_per_gold=0.1,
    attack_mode="current", resp_share=1.0, fail_limit=1,
    max_factories=40, max_minions=60, last_factory_round=46,
    layout="default", walls_first=True,
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


class Lead4b:
    def __init__(self, **params):
        unknown = set(params) - set(DEFAULTS)
        if unknown:
            raise ValueError(f"unknown parameters {sorted(unknown)}")
        self.p = {**DEFAULTS, **params}
        lay = self.p["layout"]
        self.layout = P.layout_by_name(lay) if isinstance(lay, str) else lay
        self.pending = None   # (round, opponent HP before, predicted damage) of our last attack
        self.failed = 0

    def __call__(self, obs):
        p, layout = self.p, self.layout
        me = obs["players"][obs["player"]]
        rules = gk.Rules.from_observation(obs)
        rnd = obs["round"]
        left = me["gold"]
        actions = []
        opp_hp = obs["players"][1 - obs["player"]]["hp"]
        if self.pending is not None and self.pending[0] == rnd - 1:
            _, hp_before, predicted = self.pending
            if hp_before - opp_hp < predicted / 2:
                self.failed += 1
        self.pending = None

        def add(acts):
            nonlocal left
            actions.extend(acts)
            left -= _cost_of(acts, rules)

        # 0. layout walls (walls_first=False builds them after the defence, as fortress v4 does)
        if p["walls_first"] or rnd == 1:
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
                        ps = p["spec_share"] if p["poke_share"] is None else p["poke_share"]
                        spec = P.plan_defense(o2, int(left * ps), threat_types=cheap, layout=layout, partial="none")
                if spec:
                    add(spec)
                    o2 = _with_buildings(obs, actions, left)
            if not p["walls_first"] and left > 0:
                add(P.plan_walls(o2, left, layout=layout, stage=0))
            # 3. attack
            if rnd >= p["attack_from"] and left > 0:
                bought, predicted = self._attack(obs, rules, int(left * p["attack_share"]))
                if bought:
                    add(bought)
                    self.pending = (rnd, opp_hp, predicted)
        # 4. factories
        if rnd <= p["last_factory_round"]:
            n_f = min(p["max_factories"], left // rules.factory_cost)
            add([{"op": "buy_factory"}] * max(0, n_f))
        return actions

    def _attack(self, obs, rules, budget):
        """(actions, predicted extra damage) of the chosen attack, or ([], 0)."""
        p = self.p
        mode = p["attack_mode"]
        if mode == "adaptive":
            mode = "current" if self.failed < p["fail_limit"] else "robust"
        _, base = P.opponent_leak(obs, [])
        cands = []
        for t in TIER_ORDER:
            c = rules.minions[t]["cost"]
            n = min(p["max_minions"], budget // c)
            if n <= 0:
                continue
            _, d = P.opponent_leak(obs, [t] * n)
            gain = (d - base) / (n * c)
            if gain >= p["min_leak_per_gold"]:
                cands.append((gain, t, n, d - base))
        cands.sort(reverse=True)
        if mode == "robust":
            out = []
            for gain, t, n, _ in cands[:2]:
                d = self._leak_after_response(obs, rules, [t] * n)
                g = d / (n * rules.minions[t]["cost"])
                if g >= p["min_leak_per_gold"]:
                    out.append((g, t, n, d))
            cands = sorted(out, reverse=True)
        if not cands:
            return [], 0
        _, t, n, d = cands[0]
        return [{"op": "buy_minion", "type": t}] * n, d

    def _leak_after_response(self, obs, rules, extra):
        """Damage of our active roster plus ``extra`` after the opponent's estimated best response
        (hrt-w1 plan_defense from the opponent's side against exactly this roster)."""
        me = obs["players"][obs["player"]]
        opp = obs["players"][1 - obs["player"]]
        types = gk.active_types(me["roster"], obs["round"]) + list(extra)
        o = dict(obs)
        o["player"] = 1 - obs["player"]
        acts = P.plan_defense(o, int(opp["gold"] * self.p["resp_share"]), threat_types=[types], partial="best")
        b = [dict(x) for x in opp["buildings"]] + [
            {"x": a["x"], "y": a["y"], "type": "wall" if a["op"] == "build_wall" else a["type"]}
            for a in acts if a["op"] in ("build_wall", "build_turret")]
        path = gk.route_cached(gk.cells_of(b))
        return gk.simulate_defense(types, path, b, rules).damage


def make(**params):
    return Lead4b(**params)
