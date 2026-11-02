"""Lead bot ("insurer"), entry point ``decide``.

Decision rules (one call per round, using only the observation and the bot's own state):

0. Walls. The stage-A walls of hrt-w1's default master layout are bought first, as far as gold
   allows, so every later plan is made on the route that will exist after this round's construction.
1. Round 1. Two tier1 (``r1_poke``) and factories with the rest.
2. Mandatory defence (round 2 on). hrt-w1's planner (``plan_defense``) buys the cheapest plan with
   zero simulated leaks against the opponent's visible active roster, or the least-leak plan within
   all gold when zero leaks are unaffordable.
3. Insurance. ``threat_compositions`` lists the rosters the opponent can field this round (visible
   active entries followed by each sampled purchase its visible gold allows). If a plan with zero
   simulated leaks against all of them costs at most ``spec_share`` of the remaining gold it is
   bought. Otherwise, if the worst listed roster would deal at least ``big_threat`` damage this round
   on our map, the zero-leak plan is bought with up to all remaining gold (nothing if it is
   unaffordable). With ``poke_insurance``, a remaining fallback insures against the tier1/tier2
   rosters only, within ``poke_share`` (default ``spec_share``) of the remaining gold, through round
   ``poke_until`` (every round if None); with ``poke_reactive`` only while the opponent's visible
   roster holds a tier1/tier2 entry bought in round 2 or later, and with ``poke_reactive="turret"``
   also while the opponent owns a turret.
4. Attack (from ``attack_from``). For each tier, ``attack_share`` of the remaining gold (at most
   ``max_minions`` copies) is simulated exactly against the opponent's current map. The best two
   tiers by extra damage per gold are then replayed after the opponent's estimated best same-round
   response (hrt-w1's planner run from the opponent's side with all of its visible gold against
   exactly the attacking roster). The best of them is bought if it still deals at least
   ``min_leak_per_gold`` damage per gold.
5. Factories with the rest (at most ``max_factories`` per round, none after ``last_factory_round``).

Every simulation uses the exact combat model (bot_research/harness/gamekit.py, tested against the
engine). The planner is hrt-w1's frozen v7 planning module, imported unmodified; its SHA-256 sums
are checked by bot_research/tests/test_best.py. The planner has no wall-clock cutoff, so the
actions are a function of the observation sequence only.

Use ``bot_research.bots.best:decide`` (one instance per player index, renewed in round 1) or the
factory form ``bot_research.bots.best:@make?big_threat=50`` for parameter variants.
"""
from __future__ import annotations

from bot_research.bots.defense.frozen.v7 import plan as P
from bot_research.harness import gamekit as gk

TIER_ORDER = ["tier5", "tier4", "tier3", "tier2", "tier1"]

DEFAULTS = dict(
    r1_poke=2,             # tier1 bought in round 1
    spec_share=0.6,        # insurance within this share of the remaining gold
    big_threat=100,        # insure with all gold if the worst affordable roster deals at least this
    poke_insurance=False,  # fallback insurance against tier1/tier2 rosters only
    poke_until=None,       # last round of the fallback insurance (None: every round)
    poke_reactive=False,   # fallback only while the opponent's roster shows a tier1/tier2 bought in round >= 2
                           # ("turret": or while the opponent owns a turret)
    poke_share=None,       # budget share of the fallback (None: spec_share)
    attack_from=6,         # first attacking round
    attack_share=0.5,      # share of the remaining gold an attack may use
    min_leak_per_gold=0.1,  # minimum damage per gold after the opponent's response
    max_factories=40, max_minions=60, last_factory_round=46,
    gun_cap=None,          # plans against rosters longer than this use splashes only
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


class Insurer:
    def __init__(self, **params):
        unknown = set(params) - set(DEFAULTS)
        if unknown:
            raise ValueError(f"unknown parameters {sorted(unknown)}")
        self.p = {**DEFAULTS, **params}
        self.layout = P.layout_by_name("default")

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
            if comps and left > 0:
                spec = self._plan(o2, int(left * p["spec_share"]), threat_types=comps, layout=layout,
                                  partial="none")
                if not spec and p["big_threat"] is not None and _worst_leak(o2, rules, comps) >= p["big_threat"]:
                    spec = self._plan(o2, left, threat_types=comps, layout=layout, partial="none")
                poke_now = p["poke_insurance"] and (p["poke_until"] is None or rnd <= p["poke_until"])
                if poke_now and p["poke_reactive"]:
                    opp = obs["players"][1 - obs["player"]]
                    poke_now = any(e["bought_round"] >= 2 and rules.minions[e["type"]]["hp"] <= 70
                                   for e in opp["roster"])
                    if p["poke_reactive"] == "turret":
                        poke_now = poke_now or any(b["type"] in rules.turrets for b in opp["buildings"])
                if not spec and poke_now:
                    cheap = [c for c in comps if all(rules.minions[t]["hp"] <= 70 for t in c)]
                    if cheap:
                        ps = p["spec_share"] if p["poke_share"] is None else p["poke_share"]
                        spec = self._plan(o2, int(left * ps), threat_types=cheap, layout=layout, partial="none")
                if spec:
                    add(spec)
                    o2 = _with_buildings(obs, actions, left)
            # 4. attack
            if rnd >= p["attack_from"] and left > 0:
                add(self._attack(obs, rules, int(left * p["attack_share"])))
        # 5. factories
        if rnd <= p["last_factory_round"]:
            add([{"op": "buy_factory"}] * max(0, min(p["max_factories"], left // rules.factory_cost)))
        return actions

    def _plan(self, *args, **kwargs):
        cap, tt = self.p["gun_cap"], kwargs.get("threat_types")
        if cap is not None and tt and max(len(c) for c in tt) > cap:
            kwargs["allow_guns"] = False
        return P.plan_defense(*args, **kwargs)

    def _attack(self, obs, rules, budget):
        """Purchase list of the chosen attack, or []."""
        p = self.p
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
                cands.append((gain, t, n))
        cands.sort(reverse=True)
        out = []
        for _, t, n in cands[:2]:
            g = self._leak_after_response(obs, rules, [t] * n) / (n * rules.minions[t]["cost"])
            if g >= p["min_leak_per_gold"]:
                out.append((g, t, n))
        if not out:
            return []
        _, t, n = max(out)
        return [{"op": "buy_minion", "type": t}] * n

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
