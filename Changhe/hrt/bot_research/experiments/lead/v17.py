"""Lead v17 development bot: v16 plus mid-tier insurance in the early rounds.

With the defaults (``mid_until=None``) it plays exactly as v16 with the same parameters (v15 and v16
are imported unmodified).
mid_until (round or None), mid_hp (default 180, the tier3 HP), mid_share (None: spec_share): in rounds
2 .. mid_until, while v16 has not switched to its foreign policy, after v15 has chosen its actions, the
gold v15 put into factories is taken back and the zero-leak plan (no partial plan) against the sampled
threat compositions whose types all have HP <= mid_hp is bought with up to mid_share of that gold, if
some such composition would leak on our map after v15's construction; the rest goes back into factories
(at most max_factories). Only under v15's poke condition (poke_reactive: the opponent owns a turret or
has a tier1/tier2 entry bought in round 2 or later) and with splashes only while v15's fortress
trigger holds. With mid_until <= attack_from - 1 the rounds affected contain no attack step, so taking
back factory gold is the same as inserting the plan before v15's factory step.
Reason (t7 logs 00017 and 00039, 2026-10-31T08:20Z): every C2-family setting loses 769:785 to econ13,
econ15 and econ17 because one tier3 bought in round 5 deals 26 on a map with S = 70 (below the tier3
HP 180); the worst sampled composition deals less than big_threat=100 and the full insurance plan costs
more than spec_share of the gold, so nothing is bought. Both maps then reach a lock and the
difference is frozen.
"""
from __future__ import annotations

from bot_research.experiments.lead import v15, v16
from bot_research.harness import gamekit as gk


class Lead17(v16.Lead16):
    def __init__(self, mid_until=None, mid_hp=180, mid_share=None, **params):
        super().__init__(**params)
        self.mid_until, self.mid_hp, self.mid_share = mid_until, mid_hp, mid_share
        self.mid_rounds = []

    def __call__(self, obs):
        actions = super().__call__(obs)
        rnd = obs["round"]
        if self.alt is not None or self.mid_until is None or not 2 <= rnd <= self.mid_until:
            return actions
        base, p = self.base, self.base.p
        rules = gk.Rules.from_observation(obs)
        if not self._poke_condition(obs, rules):
            return actions
        kept = [a for a in actions if a["op"] != "buy_factory"]
        left = obs["players"][obs["player"]]["gold"] - v15._cost_of(kept, rules)
        o2 = v15._with_buildings(obs, kept, left)
        comps = [c for c in base.P.threat_compositions(obs)
                 if all(rules.minions[t]["hp"] <= self.mid_hp for t in c)]
        if not comps or left <= 0 or v15._worst_leak(o2, rules, comps) == 0:
            return actions
        share = p["spec_share"] if self.mid_share is None else self.mid_share
        ins = {"allow_guns": False} if (p["splash_insurance"] or base.fortress) else {}
        plan = base._plan(o2, int(left * share), threat_types=comps, layout=base.layout, partial="none", **ins)
        if not plan:
            return actions
        left -= v15._cost_of(plan, rules)
        for a in plan:
            if a["op"] in ("build_wall", "build_turret"):
                self.requested.add((a["x"], a["y"]))
        self.mid_rounds.append(rnd)
        out = kept + plan
        if rnd <= p["last_factory_round"]:
            out += [{"op": "buy_factory"}] * max(0, min(p["max_factories"], left // rules.factory_cost))
        return out

    def _poke_condition(self, obs, rules):
        """v15's poke_reactive condition for this observation (True when poke_reactive is off)."""
        pr = self.base.p["poke_reactive"]
        if not pr:
            return True
        opp = obs["players"][1 - obs["player"]]
        ok = any(e["bought_round"] >= 2 and rules.minions[e["type"]]["hp"] <= 70 for e in opp["roster"])
        if pr == "turret":
            ok = ok or any(b["type"] in rules.turrets for b in opp["buildings"])
        elif pr == "relevant":
            ok = ok or v15._covering_turret(opp["buildings"], rules)
        return ok


def make(**params):
    return Lead17(**params)
