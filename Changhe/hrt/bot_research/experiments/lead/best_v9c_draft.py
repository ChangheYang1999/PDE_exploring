"""Lead bot ("insurer"), entry point ``decide``.

Decision rules (one call per round, using only the observation and the bot's own state):

0. Walls. The stage-A walls of hrt-w1's default master layout are bought first, as far as gold
   allows, so every later plan is made on the route that will exist after this round's construction.
1. Round 1. Three tier1 (``r1_poke``) and factories with the rest.
2. Mandatory defence (round 2 on). hrt-w1's planner (``plan_defense``) buys the cheapest plan it finds with
   zero simulated leaks against the opponent's visible active roster, or the least-leak plan within
   all gold when zero leaks are unaffordable.
3. Insurance. ``threat_compositions`` lists the rosters the opponent can field this round (visible
   active entries followed by each sampled purchase its visible gold allows). From the first round in
   which the opponent's visible gold plus ``fortress_k`` (3) rounds of its visible income (factories
   x 15 plus its route length x 1) would buy at least ``fortress_n`` (4) tier5, every plan of this
   step uses splashes and walls only for the rest of the match (``splash_insurance=true``: from
   round 2); a splash-only plan without zero leaks then means the plan with the most adjacency
   within the budget, i.e. progress towards S >= 1500.
   a. If a plan with zero simulated leaks against all of them costs at most ``spec_share`` (0.6) of
      the remaining gold it is bought.
   b. Otherwise, if the worst listed roster would deal at least ``big_threat`` (100) damage this
      round on our map, the zero-leak plan is bought with up to all remaining gold. If it is
      unaffordable, the least-leak plan within all remaining gold is bought (``big_partial``; with
      ``big_partial=false`` nothing is bought here). If that plan is splash-only
      (``splash_insurance``, the fortress trigger or ``big_splash``) and still leaks against some
      listed roster, the zero-leak plan with guns allowed is bought instead when the planner finds
      one within all remaining gold (``fortress_guns``). (Development reason: against a forecaster
      that buys tier5 with all its gold in round 8, the trigger fired in round 7; the splash plan
      cost 480 and still let one tier5 through, while one gun3 for 200 stopped every listed roster.)
   c. Otherwise (poke fallback, ``poke_insurance``): through round ``poke_until`` (3), and only while
      the opponent owns a turret or its visible roster holds a tier1/tier2 entry bought in round 2
      or later (``poke_reactive="turret"``), first the zero-leak plan against the listed rosters made
      only of types with at most ``mid_hp`` (180) HP is bought if it costs at most ``mid_joint`` (0.75)
      of the remaining gold (only through round ``mid_until`` and, with ``mid_level``, only while our HP
      is at least the opponent's); if there is no such plan, the zero-leak
      plan against the tier1/tier2 rosters only is bought if it costs at most ``poke_share`` (default
      ``spec_share``) of the remaining gold. ``poke_reactive=true`` drops the turret condition,
      ``false`` drops both conditions. (Development reason for the first plan, found by hrt-w3: with
      110 gold in round 3 the tier1/tier2 plan bought a splash for 60, and the 50 left could not stop
      a tier3 bought that round; one gun2 for 80 stops all the listed tier1-tier3 rosters. Reason for
      ``mid_level``: against a corner gun1 with one round-1 tier1 we were 5 HP behind in round 2; the
      joint plan bought three gun1 in rounds 2 and 3; by round 5 the opponent had 24 factories to our 9,
      it locked its map in round 10 and won by 973 with tier5 floods. While behind, the gold goes to the
      economy and to catch-up.)
   d. Mid-tier insurance: through round ``mid_until`` (5), under the same opponent condition as c
      (but not limited to ``poke_until``), if some listed roster made only of types with at most
      ``mid_hp`` (180, the tier3 HP) would still leak on our map after a-c, the zero-leak plan against
      those rosters is bought if it costs at most ``mid_share`` (default ``spec_share``) of the
      remaining gold. (Development reason: one tier3 bought in round 5 by the economy bots econ13,
      econ15 and econ17 dealt 26 on a map with S = 70, below big_threat, and decided those matches.)
4. Attack (from ``attack_from``). For each tier, ``attack_share`` of the remaining gold (at most
   ``max_minions`` copies) is simulated exactly against the opponent's current map, and the tier
   with the most extra damage per gold is bought if that ratio is at least ``min_leak_per_gold``
   (``attack_mode="current"``). After the first attack that dealt less than half of its predicted
   damage (judged from the opponent's HP in the next observation), the robust rule is used for the
   rest of the match (``attack_mode="adaptive"``): the best two tiers are replayed after the
   opponent's estimated best same-round response (hrt-w1's planner run from the opponent's side
   with all of its visible gold against exactly the attacking roster), and the better one is
   bought if it still deals at least ``min_leak_per_gold`` damage per gold
   (``attack_mode="robust"`` uses this rule from the start). In a round in which our own map, after
   this round's construction, has S >= 1500 (the largest minion HP), the first rule (no response
   assumption) is used whatever the mode (``immune_attack``): by P1 no copy can then reach our base
   while the map is unchanged, so gold has no defensive use, and the robust rule would stop every
   attack against a rich opponent that never defends.
   Catch-up (``catch_up``): before ``attack_from`` (rounds 2-5), while our HP is below the opponent's,
   the first rule is run on ``catch_up_share`` (default ``attack_share``) of the remaining gold; these
   attacks are not judged for the adaptive mode. (Development reason, found by hrt-w3: a gun1 at
   (10,1) and one tier1 in round 1 kill our round-1 tier1 and deal 5; the opponent then buys only
   factories in rounds 2-5 and both maps lock before round 6, so the 5 HP decided the match.)
5. Factories with the rest (at most ``max_factories`` per round, none after ``last_factory_round``).

Foreign maps (``foreign_policy="econ20"``). The bot records every cell at which it asked to build. From
the first round in which its own map holds a building at a cell it never asked for, the rest of the
match is played by a fresh instance of hrt-w2's frozen economy bot econ20
(``bots/economy/frozen/v20/econ20.py``, imported unmodified; ``free_fallback="zero"``,
``foreign_attack_from=11``, ``doom="next"``, ``fac_cap=400``, ``sat_reach=true``, ``replan=true``,
``foreign_sat_from=11``), which designs a new wall layout around the buildings it did not ask for with
hrt-w1's frozen re-planner (``bots/defense/frozen/v26/replan.py``). On the standard start this cannot
happen (the engine places a building only where the bot asked); after a scripted opening or another start
with buildings the bot did not choose it does. Development reason: with a foreign map the master layout
cannot be completed and our splash-only plans stalled below S = 1500. On the same 24 scripted-opening
games against fortress v25, v26 and econ19 (four openings, both seats) the previous target econ17 scored
4-0-20 (run fx1a), econ19 14-4-6, fortress v26 8-6-10, fortress v27 8-6-10 and econ20 18-0-6 (fx1b,
fx1d); on 48 games against six older opponents econ17 scored 32-6-10 (sc1), econ19 47-0-1 and econ20
46-0-2 (fx1c). econ20 runs its planner without a wall-clock cutoff (``plan_time`` 1e6 s) and the
re-planner for a fixed number of iterations with the round number as seed (``time_budget`` None), and
uses no other randomness, so the switch keeps the actions a function of the observation sequence; the
SHA-256 sums of the frozen packages it imports (economy v20, defense v15 and v26) are checked by
tests/test_best.py.

Plans against rosters of more than ``gun_cap`` (120) copies use splashes only, which bounds the
decision time (slowest call in the development runs c5a-c5c: 2.6 s with the cap, 3.96 s without it;
the cap changed no result on the c5a pool).

Every simulation uses the exact combat model (bot_research/harness/gamekit.py, tested against the
engine). The planner is hrt-w1's frozen v7 planning module, imported unmodified; its SHA-256 sums
are checked by bot_research/tests/test_best.py. The planner has no wall-clock cutoff, so the
actions are a function of the observation sequence only. The development twin of this file is
``bot_research.experiments.lead.v20:@make?big_threat=100&gun_cap=120&poke_until=3&big_partial=true&r1_poke=3&attack_mode="adaptive"&poke_reactive="turret"&fortress_n=4&immune_attack=true&foreign_policy="econ17"&mid_until=5&fortress_guns=true&catch_up=true&mid_joint=0.75&mid_level=true&foreign_target="econ20"``
(same actions; checked by tests/test_best.py and experiments/lead/same_actions.py).
"Cheapest" means the cheapest plan the planner finds (restricted wall prefixes and greedy splash and
gun additions), not a proved optimum.

Use ``bot_research.bots.best:decide`` (one instance per player index, renewed in round 1) or the
factory form ``bot_research.bots.best:@make?big_threat=50`` for parameter variants.
"""
from __future__ import annotations

from bot_research.bots.defense.frozen.v7 import plan as P
from bot_research.bots.economy.frozen.v20 import econ20 as E20
from bot_research.harness import gamekit as gk

E20_PARAMS = dict(free_fallback="zero", foreign_attack_from=11, doom="next", fac_cap=400, sat_reach=True, replan=True,
                  foreign_sat_from=11)

TIER_ORDER = ["tier5", "tier4", "tier3", "tier2", "tier1"]

DEFAULTS = dict(
    r1_poke=3,             # tier1 bought in round 1
    spec_share=0.6,        # insurance within this share of the remaining gold
    big_threat=100,        # insure with all gold if the worst affordable roster deals at least this
    big_partial=True,      # if that zero-leak plan is unaffordable, buy the least-leak plan within all gold
    poke_insurance=True,   # fallback insurance against tier1/tier2 rosters only
    poke_until=3,          # last round of the fallback insurance (None: every round)
    poke_reactive="turret",  # fallback only while the opponent owns a turret or its roster shows a
                           # tier1/tier2 bought in round >= 2 (true: roster condition only; false: always)
    poke_share=None,       # budget share of the fallback (None: spec_share)
    attack_from=6,         # first attacking round
    attack_share=0.5,      # share of the remaining gold an attack may use
    min_leak_per_gold=0.1,  # minimum damage per gold after the opponent's response
    max_factories=40, max_minions=60, last_factory_round=46,
    gun_cap=120,           # plans against rosters longer than this use splashes only
    attack_mode="adaptive",  # "current", "robust", or current until fail_limit attacks fell short
    fail_limit=1,
    splash_insurance=False,  # insurance plans with splashes and walls only from round 2
    fortress_n=4,          # ... or from the round the opponent's projected gold buys this many tier5
    fortress_k=3,          # projection horizon in rounds of the opponent's visible income
    big_splash=False,      # the big-threat plan (rule 3b) with splashes and walls only, every round
    immune_attack=True,    # current-rule attacks while our own map has S >= the largest minion HP
    immune_share=None,     # budget share of those attacks (None: attack_share)
    mid_until=5,           # last round of the mid-tier insurance (rule 3d; None: off)
    mid_hp=180,            # largest minion HP in the mid-tier rosters
    mid_share=None,        # budget share of the mid-tier insurance (None: spec_share)
    mid_joint=0.75,        # budget share of the joint tier1-tier3 plan of rule 3c (None: off)
    mid_level=True,        # ... only while our HP is at least the opponent's
    fortress_guns=True,    # rule 3b: replace a leaking splash-only plan by a zero-leak plan with guns
    catch_up=True,         # rule 4: first-rule attacks before attack_from while our HP is lower
    catch_up_share=None,   # budget share of those attacks (None: attack_share)
    foreign_policy="econ20",  # policy on maps holding buildings the bot never asked for (None: keep playing)
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
    """Largest base damage over rosters on our current map (exact simulation)."""
    b = obs["players"][obs["player"]]["buildings"]
    path = gk.route_cached(gk.cells_of(b))
    return max(gk.simulate_defense(c, path, b, rules).damage for c in comps)


def _immune(obs, rules):
    """True if our map in ``obs`` has splash exposure S at least the largest minion HP (P1)."""
    b = obs["players"][obs["player"]]["buildings"]
    path = gk.route_cached(gk.cells_of(b))
    return gk.splash_total(path, b, rules) >= max(m["hp"] for m in rules.minions.values())


class Insurer:
    def __init__(self, **params):
        unknown = set(params) - set(DEFAULTS)
        if unknown:
            raise ValueError(f"unknown parameters {sorted(unknown)}")
        self.p = {**DEFAULTS, **params}
        if self.p["foreign_policy"] not in (None, "econ20"):
            raise ValueError("foreign_policy must be \"econ20\" or None")
        self.layout = P.layout_by_name("default")
        self.pending = None   # (round, opponent HP before, predicted damage) of our last attack
        self.failed = 0       # attacks that dealt less than half of their prediction
        self.fortress = False  # splash-only insurance is on (sticky)
        self.requested = set()  # cells at which we asked to build
        self.alt = None        # the foreign-map policy, once it has taken over
        self.switch_round = None

    def __call__(self, obs):
        p, layout = self.p, self.layout
        me = obs["players"][obs["player"]]
        rnd = obs["round"]
        if self.alt is None and p["foreign_policy"] is not None and \
                {(b["x"], b["y"]) for b in me["buildings"]} - self.requested:
            self.alt = E20.make(**E20_PARAMS)
            self.switch_round = rnd
        if self.alt is not None:
            return self.alt(obs)
        actions = self._decide(obs)
        self.requested.update((a["x"], a["y"]) for a in actions if a["op"] in ("build_wall", "build_turret"))
        return actions

    def _decide(self, obs):
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

        # 0. layout walls
        add(P.plan_walls(obs, left, layout=layout, stage=0))
        o2 = _with_buildings(obs, actions, left)
        if rnd == 1:
            # 1. round-1 poke
            n = min(p["r1_poke"], left // rules.minions["tier1"]["cost"])
            add([{"op": "buy_minion", "type": "tier1"}] * n)
        else:
            # 2. mandatory defence against the visible roster
            visible = P.active_opponent_types(obs)
            if visible:
                add(self._plan(o2, left, threat_types=[visible], layout=layout, partial="best"))
                o2 = _with_buildings(obs, actions, left)
            # 3. insurance
            comps = P.threat_compositions(obs)
            ins = {"allow_guns": False} if p["splash_insurance"] or self._fortress(obs, rules) else {}
            if comps and left > 0:
                spec = self._plan(o2, int(left * p["spec_share"]), threat_types=comps, layout=layout,
                                  partial="none", **ins)
                if not spec and p["big_threat"] is not None and _worst_leak(o2, rules, comps) >= p["big_threat"]:
                    big = {"allow_guns": False} if p["big_splash"] else ins
                    spec = self._plan(o2, left, threat_types=comps, layout=layout,
                                      partial="best" if p["big_partial"] else "none", **big)
                    if p["fortress_guns"] and big and _worst_leak(
                            _with_buildings(obs, actions + spec, left - _cost_of(spec, rules)), rules, comps) > 0:
                        alt = self._plan(o2, left, threat_types=comps, layout=layout, partial="none")
                        if alt:
                            spec = alt
                poke_now = p["poke_insurance"] and (p["poke_until"] is None or rnd <= p["poke_until"])
                if poke_now:
                    poke_now = self._reactive(obs, rules)
                if not spec and poke_now and p["mid_joint"] is not None and p["mid_until"] is not None \
                        and rnd <= p["mid_until"] and (not p["mid_level"] or me["hp"] >= opp_hp):
                    mid = [c for c in comps if all(rules.minions[t]["hp"] <= p["mid_hp"] for t in c)]
                    if mid:
                        spec = self._plan(o2, int(left * p["mid_joint"]), threat_types=mid, layout=layout,
                                          partial="none", **ins)
                if not spec and poke_now:
                    cheap = [c for c in comps if all(rules.minions[t]["hp"] <= 70 for t in c)]
                    if cheap:
                        ps = p["spec_share"] if p["poke_share"] is None else p["poke_share"]
                        spec = self._plan(o2, int(left * ps), threat_types=cheap, layout=layout, partial="none",
                                          **ins)
                if spec:
                    add(spec)
                    o2 = _with_buildings(obs, actions, left)
            # 3d. mid-tier insurance
            if p["mid_until"] is not None and rnd <= p["mid_until"] and left > 0 and self._reactive(obs, rules):
                mid = [c for c in comps if all(rules.minions[t]["hp"] <= p["mid_hp"] for t in c)]
                if mid and _worst_leak(o2, rules, mid) > 0:
                    ms = p["spec_share"] if p["mid_share"] is None else p["mid_share"]
                    plan = self._plan(o2, int(left * ms), threat_types=mid, layout=layout, partial="none", **ins)
                    if plan:
                        add(plan)
                        o2 = _with_buildings(obs, actions, left)
            # 4. attack
            immune = p["immune_attack"] and _immune(o2, rules)
            if rnd >= p["attack_from"] and left > 0:
                share = p["attack_share"] if not immune or p["immune_share"] is None else p["immune_share"]
                bought, predicted = self._attack(obs, rules, int(left * share), "current" if immune else None)
                if bought:
                    add(bought)
                    self.pending = (rnd, opp_hp, predicted)
            elif p["catch_up"] and me["hp"] < opp_hp and left > 0:
                share = p["attack_share"] if p["catch_up_share"] is None else p["catch_up_share"]
                add(self._attack(obs, rules, int(left * share), "current")[0])
        # 5. factories
        if rnd <= p["last_factory_round"]:
            add([{"op": "buy_factory"}] * max(0, min(p["max_factories"], left // rules.factory_cost)))
        return actions

    def _reactive(self, obs, rules):
        """The opponent condition of rules 3c and 3d (``poke_reactive``)."""
        pr = self.p["poke_reactive"]
        if not pr:
            return True
        opp = obs["players"][1 - obs["player"]]
        ok = any(e["bought_round"] >= 2 and rules.minions[e["type"]]["hp"] <= 70 for e in opp["roster"])
        if pr == "turret":
            ok = ok or any(b["type"] in rules.turrets for b in opp["buildings"])
        return ok

    def _fortress(self, obs, rules):
        """True from the first round in which the opponent's projected gold buys fortress_n tier5."""
        p = self.p
        if not self.fortress and p["fortress_n"] is not None:
            opp = obs["players"][1 - obs["player"]]
            income = opp["n_factories"] * rules.factory_income + opp["length_path"] * rules.path_income
            projected = opp["gold"] + p["fortress_k"] * income
            self.fortress = projected // rules.minions["tier5"]["cost"] >= p["fortress_n"]
        return self.fortress

    def _plan(self, *args, **kwargs):
        cap, tt = self.p["gun_cap"], kwargs.get("threat_types")
        if cap is not None and tt and max(len(c) for c in tt) > cap:
            kwargs["allow_guns"] = False
        return P.plan_defense(*args, **kwargs)

    def _attack(self, obs, rules, budget, mode=None):
        """(purchase list, predicted damage) of the chosen attack, or ([], 0)."""
        p = self.p
        mode = mode or p["attack_mode"]
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
            for _, t, n, _ in cands[:2]:
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
        (the planner from the opponent's side with all its visible gold against exactly this roster)."""
        me = obs["players"][obs["player"]]
        opp = obs["players"][1 - obs["player"]]
        types = gk.active_types(me["roster"], obs["round"]) + list(extra)
        o = dict(obs)
        o["player"] = 1 - obs["player"]
        acts = self._plan(o, opp["gold"], threat_types=[types], partial="best")
        b = [dict(x) for x in opp["buildings"]] + [
            {"x": a["x"], "y": a["y"], "type": "wall" if a["op"] == "build_wall" else a["type"]}
            for a in acts if a["op"] in ("build_wall", "build_turret")]
        path = gk.route_cached(gk.cells_of(b))
        return gk.simulate_defense(types, path, b, rules).damage


def make(**params):
    """Factory: a fresh bot (separate state per side)."""
    return Insurer(**params)


_instances: dict = {}


def decide(observation):
    """Entry point required by the runner; one bot per player index, renewed in round 1."""
    key = observation["player"]
    if key not in _instances or observation["round"] == 1:
        _instances[key] = Insurer()
    return _instances[key](observation)
