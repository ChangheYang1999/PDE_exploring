"""Lead v13 development bot: v12 plus splash-only insurance options.

With the defaults (``fortress_n=None``, ``splash_insurance=False``) it plays exactly as v12 with the
same parameters.
splash_insurance: every speculative-insurance plan (step 2) is made with allow_guns=False (splashes
and walls only); the mandatory defence against the visible roster may still use guns.
fortress_n (int or None), fortress_k: from the first round in which the opponent's visible gold plus
fortress_k rounds of its visible income (factories x factory_income + its route length x
path_income_per_step) would buy at least fortress_n tier5, splash_insurance holds for the rest of
the match. Splash-only plans that cannot reach zero leaks buy, with big_partial, the most
adjacency within the budget, so the big-threat rule then spends on progress towards S >= 1500.
poke_reactive "relevant": as "turret", but only turrets that cover the opponent's current route
(a splash next to a route cell or a gun with a route cell in range) count.
open_attack_from (round or None): in rounds open_attack_from .. attack_from - 1 the attack step also
runs (same attack_mode and attack_share) while no opponent turret covers the opponent's route.
lead_guard_from (round or None): from that round on, when the big-threat rule does not fire, the
full zero-leak plan is also bought with up to all remaining gold (no partial plan) if the worst
sampled composition would deal at least max(lead_guard_min, lead + 1) damage this round, where
lead = own HP - opponent HP in the observation (a leak that would remove our current lead).
With lead_guard_turret, only while the opponent owns a turret.

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
     leaks against the tier1/tier2 compositions only (poke insurance; only up to round poke_until
     if set; with poke_reactive true only while the opponent's visible roster holds a tier1/tier2
     entry bought in round 2 or later, entries leaving the roster when they expire; with
     poke_reactive "turret" also while the opponent owns a turret). With big_threat set, the
     full zero-leak plan is bought with up to all remaining gold instead whenever the worst sampled
     composition would deal at least big_threat damage this round on our map without it; with
     big_partial, the least-leak partial plan within all remaining gold if zero leaks are unaffordable.
  4. Attack from attack_from: the tier with the most extra leaked damage per gold on the opponent's
     current map (exact simulation), using attack_share of the remaining gold, if that ratio is at
     least min_leak_per_gold. attack_mode "current" uses that rule as is; "robust" also requires
     a leak after the opponent's estimated best same-round response (plan_defense from the
     opponent's side with resp_share of its visible gold against exactly the attacking roster);
     "adaptive" uses "current" until fail_limit attacks have dealt less than half of their
     predicted damage, then "robust". Attack outcomes are judged from the opponent's HP in the
     next observation (own state only).
  gun_cap: plan calls whose compositions include one with more than gun_cap copies are made
  with allow_guns=False (splash plans only; bounds the decision time, as hrt-w1's v11 does).
  planner selects hrt-w1's frozen planning module ("v7", "v11" or "v22", see PLANNERS).
  foreign_planner ("v22" or None): every plan_defense call whose own map is "foreign" in the sense
  of hrt-w1's v22 planner (more than 8 own buildings outside the master layout, e.g. after a scripted
  opening) goes to that planner, which then searches every legal cell next to the route instead of
  the layout's cells only; all other calls, the threat compositions and the walls stay with planner.
  5. Factories with the rest (at most max_factories per round, none after last_factory_round).
"""
from __future__ import annotations

from bot_research.bots.defense.frozen.v7 import plan as P7
from bot_research.bots.defense.frozen.v11 import plan as P11
from bot_research.bots.defense.frozen.v22 import plan as P22
from bot_research.harness import gamekit as gk

# hrt-w1's frozen planners. v11 adds heavy-last and roster-wrap compositions, exhaustive ordered
# purchase lists up to 400 lists and a gun-pass skip for compositions over 120 copies; its
# wall-clock cutoff is disabled here (time_budget=PLAN_TIME) so actions depend on the observation only.
PLANNERS = {"v7": P7, "v11": P11, "v22": P22}
PLAN_TIME = 1e6

TIER_ORDER = ["tier5", "tier4", "tier3", "tier2", "tier1"]
GUARD_CELL = (1, 3)

DEFAULTS = dict(
    r1="poke", r1_poke=2,
    spec_share=0.6, poke_insurance=True, poke_share=None, grades=(1.0,),
    attack_from=6, attack_share=0.5, min_leak_per_gold=0.1,
    attack_mode="current", resp_share=1.0, fail_limit=1,
    max_factories=40, max_minions=60, last_factory_round=46,
    layout="default", walls_first=True, big_threat=None, big_partial=False, planner="v7", gun_cap=None,
    poke_until=None, poke_reactive=False, foreign_planner=None,
    lead_guard_from=None, lead_guard_min=1, lead_guard_turret=False,
    open_attack_from=None,
    splash_insurance=False, fortress_n=None, fortress_k=3,
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


def _worst_leak(obs, rules, comps):
    """Largest base damage over compositions on our current map (exact simulation)."""
    b = obs["players"][obs["player"]]["buildings"]
    path = gk.route_cached(gk.cells_of(b))
    return max(gk.simulate_defense(c, path, b, rules).damage for c in comps)


def _covering_turret(buildings, rules):
    """True if some turret covers the route of this map (splash next to a route cell, gun in range)."""
    path = gk.route_cached(gk.cells_of(buildings))
    return gk.splash_total(path, buildings, rules) > 0 or bool(gk.gun_coverage(path, buildings, rules))


class Lead13:
    def __init__(self, **params):
        unknown = set(params) - set(DEFAULTS)
        if unknown:
            raise ValueError(f"unknown parameters {sorted(unknown)}")
        self.p = {**DEFAULTS, **params}
        self.P = PLANNERS[self.p["planner"]]
        lay = self.p["layout"]
        self.layout = self.P.layout_by_name(lay) if isinstance(lay, str) else lay
        fp = self.p["foreign_planner"]
        self.FP = PLANNERS[fp] if fp else None
        self.foreign_layout = self.FP.layout_by_name(lay) if fp else None
        self.foreign_calls = 0
        self.pending = None   # (round, opponent HP before, predicted damage) of our last attack
        self.failed = 0
        self.fortress = False   # splash-only insurance is on (sticky once fortress_n triggers)

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
            add(self.P.plan_walls(obs, left, layout=layout, stage=0))
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
            visible = self.P.active_opponent_types(obs)
            if visible:
                add(self._plan(o2, left, threat_types=[visible], layout=layout, partial="best"))
                o2 = _with_buildings(obs, actions, left)
            # 2. speculative insurance
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
                        spec = self._plan(o2, left, threat_types=comps, layout=layout,
                                          partial="best" if p["big_partial"] else "none", **ins)
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
            # 3. attack
            open_attack = (p["open_attack_from"] is not None and p["open_attack_from"] <= rnd < p["attack_from"]
                           and not _covering_turret(obs["players"][1 - obs["player"]]["buildings"], rules))
            if (rnd >= p["attack_from"] or open_attack) and left > 0:
                bought, predicted = self._attack(obs, rules, int(left * p["attack_share"]))
                if bought:
                    add(bought)
                    self.pending = (rnd, opp_hp, predicted)
        # 4. factories
        if rnd <= p["last_factory_round"]:
            n_f = min(p["max_factories"], left // rules.factory_cost)
            add([{"op": "buy_factory"}] * max(0, n_f))
        return actions

    def _fortress(self, obs, rules):
        """True from the first round in which the opponent's projected gold buys fortress_n tier5."""
        p = self.p
        if not self.fortress and p["fortress_n"] is not None:
            opp = obs["players"][1 - obs["player"]]
            income = opp["n_factories"] * rules.factory_income + opp["length_path"] * rules.path_income
            projected = opp["gold"] + p["fortress_k"] * income
            self.fortress = projected // rules.minions["tier5"]["cost"] >= p["fortress_n"]
        return self.fortress

    def _lead_guard(self, obs, rules):
        """Damage threshold of the lead guard this round, or None when it is off."""
        p = self.p
        if p["lead_guard_from"] is None or obs["round"] < p["lead_guard_from"]:
            return None
        me, opp = obs["players"][obs["player"]], obs["players"][1 - obs["player"]]
        if p["lead_guard_turret"] and not any(b["type"] in rules.turrets for b in opp["buildings"]):
            return None
        return max(p["lead_guard_min"], me["hp"] - opp["hp"] + 1)

    def _plan(self, *args, **kwargs):
        P = self.P
        if self.FP is not None:
            obs = args[0]
            blocked = {(b["x"], b["y"]) for b in obs["players"][obs["player"]]["buildings"]}
            if self.FP.is_foreign(blocked, self.foreign_layout):
                P = self.FP
                self.foreign_calls += 1
                if "layout" in kwargs:
                    kwargs["layout"] = self.foreign_layout
        if P is not P7:
            kwargs["time_budget"] = PLAN_TIME
        cap, tt = self.p["gun_cap"], kwargs.get("threat_types")
        if cap is not None and tt:
            comps = tt if isinstance(tt[0], (list, tuple)) else [tt]
            if max(len(c) for c in comps) > cap:
                kwargs["allow_guns"] = False
        return P.plan_defense(*args, **kwargs)

    def _attack(self, obs, rules, budget):
        """(actions, predicted extra damage) of the chosen attack, or ([], 0)."""
        p = self.p
        mode = p["attack_mode"]
        if mode == "adaptive":
            mode = "current" if self.failed < p["fail_limit"] else "robust"
        _, base = self.P.opponent_leak(obs, [])
        cands = []
        for t in TIER_ORDER:
            c = rules.minions[t]["cost"]
            n = min(p["max_minions"], budget // c)
            if n <= 0:
                continue
            _, d = self.P.opponent_leak(obs, [t] * n)
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
        acts = self._plan(o, int(opp["gold"] * self.p["resp_share"]), threat_types=[types], partial="best")
        b = [dict(x) for x in opp["buildings"]] + [
            {"x": a["x"], "y": a["y"], "type": "wall" if a["op"] == "build_wall" else a["type"]}
            for a in acts if a["op"] in ("build_wall", "build_turret")]
        path = gk.route_cached(gk.cells_of(b))
        return gk.simulate_defense(types, path, b, rules).damage


def make(**params):
    return Lead13(**params)
