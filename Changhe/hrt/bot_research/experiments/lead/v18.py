"""Lead v18 development bot: v17 plus two options of the speculative-insurance step.

With the defaults (``mid_joint=None, fortress_guns=False``) it plays exactly as v17 with the same
parameters (v15, v16 and v17 are imported unmodified; the v15 instance is the original class). With
either option set, the v15 instance is replaced by ``Base18``, a copy of ``v15.Lead15.__call__`` that
differs in two marked places, one per option.
mid_joint (share or None): in rounds 2 .. mid_until (v17's parameter, which
must be set), when the speculative step reaches the poke fallback (the zero-leak plan against all
sampled compositions costs more than spec_share of the gold and the big-threat rule bought nothing)
and the poke condition holds (which includes round <= poke_until, so with poke_until=3 only rounds 2
and 3 are affected), the zero-leak plan against the sampled compositions whose types all have
HP <= mid_hp is tried first, with up to mid_joint of the gold left after the mandatory defence. If
that plan is empty (unaffordable, or no such composition leaks), v15's poke plan follows as before.
v17's mid-tier insurance step still runs afterwards.
With mid_joint=0.0 the first attempt has budget 0 and returns no plan, so v18 plays as v17: this
setting checks that the copied method is faithful (experiments/lead/same_actions.py).
Reason (hrt-w3, notes/validation.md 2026-10-31T09:21Z): against budget_timing (tier3, attack_round 3,
budget_fraction 0.5), Lead17 has 110 gold in round 3; v15's poke fallback buys a splash for 60, and the
50 left cannot stop the tier3 (26 damage, 774:800 at round 50). One gun2 at (9,5) for 80 gold stops
all four sampled mid-tier compositions and the actual roster, but only a plan made before the poke
purchase, with more than 0.6 of the gold, finds it.
fortress_guns (default False): when the big-threat plan is splash-only (fortress trigger, splash_insurance
or big_splash) and still leaves a leak against the sampled compositions, the zero-leak plan with guns
allowed and up to all the gold is bought instead, if the planner finds one.
Reason (c8m log 00019, 2026-10-31T09:28Z): against forecast_timing (tier5, attack_round 8) the fortress
trigger fires in round 7; the splash-only plan (8 splashes, 480 gold) still lets one tier5 through,
while one gun3 (200 gold) stops every sampled composition of that round. In round 8 two tier5 arrive
and no plan within our 532 gold stops them; the C2 settings without the trigger buy guns and win +15.
foreign_target (a key of FOREIGN or None): with v16's foreign_policy set, the policy played from the
switch round is this frozen teammate bot (a fresh instance created in that round) instead of econ17.
Reason (hrt-w1 notes/defense.md 2026-10-31T09:24Z): frozen fortress v25 beats econ17 under mirror:1:2
(+1300) and mirror:22:3 (+1410) in both seats, so best_v9b, which plays econ17 on such maps, may lose to
it there; hrt-w2's econ19 (frozen 09:31Z) changes the lock and late-flood logic of econ17.
catch_up (default False), catch_up_share (None: attack_share): in rounds 2 .. attack_from - 1, while our
HP is below the opponent's and the foreign policy has not taken over, after v17 has chosen its actions the
gold it put into factories is taken back, v15's attack rule is run with the "current" mode (exact
simulation against the opponent's current map, no response assumption) on catch_up_share of that gold,
and the rest goes back into factories. These attacks do not count towards the adaptive mode's failure
limit. With attack_from=6 and mid_until=5 this is the order mandatory defence, insurance, mid-tier
insurance, attack, factories, the same as in best_v9b's rounds 6 and later.
Reason (hrt-w3 notes/validation.md 2026-10-31T09:53Z, runs/validation/best-v9b-counter-model-free-001,
case0010): guard_geometry with a gun1 at (10,1) and one tier1 in round 1 kills our three round-1 tier1
and deals 5; it then buys only factories in rounds 2-5 (two gun1 on its map) and becomes immune by about
round 9, so the -5 is frozen and best_v9b loses 795:800 in both seats. Our first attack (round 6) meets
its round-6 construction.
"""
from __future__ import annotations

from bot_research.experiments.lead import v15, v17
from bot_research.experiments.lead.v15 import _cost_of, _covering_turret, _immune, _with_buildings, _worst_leak
from bot_research.harness import gamekit as gk
from bot_research.harness.match import resolve_spec

FOREIGN = {
    "econ19": 'bot_research.bots.economy.frozen.v19.econ19:@make?free_fallback="zero"&foreign_attack_from=11'
              '&doom="next"&fac_cap=400&sat_reach=true',
    "fortress25": "bot_research.bots.defense.frozen.v25.fortress:@make",
    "fortress26": "bot_research.bots.defense.frozen.v26.fortress:@make",
}


class Base18(v15.Lead15):
    """v15.Lead15 with the joint early plan and fortress_guns (see the module docstring)."""

    def __init__(self, mid_joint=None, mid_until=None, mid_hp=180, fortress_guns=False, **params):
        super().__init__(**params)
        self.mid_joint, self.mid_until, self.mid_hp = mid_joint, mid_until, mid_hp
        self.fortress_guns = fortress_guns
        self.joint_rounds, self.gun_rounds = [], []

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

        if p["walls_first"] or rnd == 1:
            add(self.P.plan_walls(obs, left, layout=layout, stage=0))
        o2 = _with_buildings(obs, actions, left)
        attack = []
        if rnd == 1:
            if p["r1"] == "guard":
                cell = v15.GUARD_CELL
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
            visible = self.P.active_opponent_types(obs)
            if visible:
                add(self._plan(o2, left, threat_types=[visible], layout=layout, partial="best"))
                o2 = _with_buildings(obs, actions, left)
            comps = self.P.threat_compositions(obs)
            splash_only = p["splash_insurance"] or self._fortress(obs, rules)
            ins = {"allow_guns": False} if splash_only else {}
            if comps and left > 0:
                budget = int(left * p["spec_share"])
                spec = []
                opp_gold = obs["players"][1 - obs["player"]]["gold"]
                for i, f in enumerate(p["grades"]):
                    cf = comps if i == 0 else self.P.threat_compositions(obs, extra_gold=int(opp_gold * f))
                    spec = self._plan(o2, budget, threat_types=cf, layout=layout, partial="none", **ins) if cf else []
                    if spec:
                        break
                if not spec and p["big_threat"] is not None:
                    worst = _worst_leak(o2, rules, comps)
                    if worst >= p["big_threat"]:
                        big = {"allow_guns": False} if p["big_splash"] else ins
                        spec = self._plan(o2, left, threat_types=comps, layout=layout,
                                          partial="best" if p["big_partial"] else "none", **big)
                        # Second change from v15: fortress_guns (see the module docstring).
                        if self.fortress_guns and big:
                            rest = left - _cost_of(spec, rules)
                            if _worst_leak(_with_buildings(obs, actions + spec, rest), rules, comps) > 0:
                                alt = self._plan(o2, left, threat_types=comps, layout=layout, partial="none")
                                if alt:
                                    spec = alt
                                    self.gun_rounds.append(rnd)
                    elif self._lead_guard(obs, rules) is not None and worst >= self._lead_guard(obs, rules):
                        spec = self._plan(o2, left, threat_types=comps, layout=layout, partial="none", **ins)
                poke_now = p["poke_insurance"] and (p["poke_until"] is None or rnd <= p["poke_until"])
                if poke_now and p["poke_reactive"]:
                    opp_roster = obs["players"][1 - obs["player"]]["roster"]
                    poke_now = any(e["bought_round"] >= 2 and rules.minions[e["type"]]["hp"] <= 70
                                   for e in opp_roster)
                    if p["poke_reactive"] == "turret":
                        poke_now = poke_now or any(
                            b["type"] in rules.turrets for b in obs["players"][1 - obs["player"]]["buildings"])
                    elif p["poke_reactive"] == "relevant":
                        poke_now = poke_now or _covering_turret(obs["players"][1 - obs["player"]]["buildings"], rules)
                # First change from v15: the joint plan against cheap and mid-tier compositions.
                if not spec and poke_now and self.mid_joint is not None and rnd <= self.mid_until:
                    mid = [c for c in comps if all(rules.minions[t]["hp"] <= self.mid_hp for t in c)]
                    if mid:
                        spec = self._plan(o2, int(left * self.mid_joint), threat_types=mid, layout=layout,
                                          partial="none", **ins)
                        if spec:
                            self.joint_rounds.append(rnd)
                if not spec and poke_now:
                    cheap = [c for c in comps if all(rules.minions[t]["hp"] <= 70 for t in c)]
                    if cheap:
                        ps = p["spec_share"] if p["poke_share"] is None else p["poke_share"]
                        spec = self._plan(o2, int(left * ps), threat_types=cheap, layout=layout, partial="none", **ins)
                if spec:
                    add(spec)
                    o2 = _with_buildings(obs, actions, left)
            if not p["walls_first"] and left > 0:
                add(self.P.plan_walls(o2, left, layout=layout, stage=0))
            open_attack = (p["open_attack_from"] is not None and p["open_attack_from"] <= rnd < p["attack_from"]
                           and not _covering_turret(obs["players"][1 - obs["player"]]["buildings"], rules))
            immune = p["immune_attack"] and _immune(o2, rules)
            if (rnd >= p["attack_from"] or open_attack) and left > 0:
                share = p["attack_share"] if not immune or p["immune_share"] is None else p["immune_share"]
                bought, predicted = self._attack(obs, rules, int(left * share), "current" if immune else None)
                if bought:
                    add(bought)
                    self.pending = (rnd, opp_hp, predicted)
        if rnd <= p["last_factory_round"]:
            n_f = min(p["max_factories"], left // rules.factory_cost)
            add([{"op": "buy_factory"}] * max(0, n_f))
        return actions


class Lead18(v17.Lead17):
    def __init__(self, mid_joint=None, fortress_guns=False, foreign_target=None, catch_up=False,
                 catch_up_share=None, **params):
        super().__init__(**params)
        self.mid_joint, self.fortress_guns = mid_joint, fortress_guns
        self.catch_up, self.catch_up_share = catch_up, catch_up_share
        self.catch_rounds = []
        if mid_joint is not None and self.mid_until is None:
            raise ValueError("mid_joint needs mid_until")
        if foreign_target is not None and (self.foreign_policy is None or foreign_target not in FOREIGN):
            raise ValueError(f"foreign_target {foreign_target!r} needs foreign_policy and a key of FOREIGN")
        self.foreign_target = foreign_target
        if mid_joint is not None or fortress_guns:
            self.base = Base18(mid_joint=mid_joint, mid_until=self.mid_until, mid_hp=self.mid_hp,
                               fortress_guns=fortress_guns, **self.base.p)

    def __call__(self, obs):
        # v16 switches to econ17 when self.alt is None; setting self.alt first selects the other target.
        if self.foreign_target is not None and self.alt is None and self._foreign(obs):
            self.alt = resolve_spec(FOREIGN[self.foreign_target])
            self.switch_round = obs["round"]
        actions = super().__call__(obs)
        rnd, p = obs["round"], self.base.p
        me, opp = obs["players"][obs["player"]], obs["players"][1 - obs["player"]]
        if self.alt is not None or not self.catch_up or not 2 <= rnd < p["attack_from"] or me["hp"] >= opp["hp"]:
            return actions
        rules = gk.Rules.from_observation(obs)
        kept = [a for a in actions if a["op"] != "buy_factory"]
        left = me["gold"] - _cost_of(kept, rules)
        share = p["attack_share"] if self.catch_up_share is None else self.catch_up_share
        bought, _ = self.base._attack(obs, rules, int(left * share), "current") if left > 0 else ([], 0)
        if not bought:
            return actions
        left -= _cost_of(bought, rules)
        self.catch_rounds.append(rnd)
        out = kept + bought
        if rnd <= p["last_factory_round"]:
            out += [{"op": "buy_factory"}] * max(0, min(p["max_factories"], left // rules.factory_cost))
        return out


def make(**params):
    return Lead18(**params)
