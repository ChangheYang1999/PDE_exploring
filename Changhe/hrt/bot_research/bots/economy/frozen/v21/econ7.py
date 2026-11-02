"""Economy bot v7: hrt-w1's planner for defence, this lane's economy and attack.

Spec: ``bot_research.bots.economy.econ7:@make?k=v``. All parameters are optional.
Defence uses the frozen copy ``bots/defense/frozen/v9/plan.py`` (lane hrt-w1,
imported, not modified): its layout walls give a long route from round 1
(path income: the default layout's 20 stage-A walls make the route 40 instead
of 22) and its plans are checked by exact simulation. The economy and attack
rules are those of econ6 (v6) with the defaults found in sweep5/sweep6.

Per round, in this order:
0. Layout walls (``walls``): stage-A walls of ``layout`` while affordable
   (1 gold each); every plan below is made on the resulting route.
1. Round 1: ``r1_units`` copies of ``r1_tier`` (a round-1 poke).
2. Lock (``lock``): if the own per-copy splash is at least the largest minion
   HP, no copy can arrive while the route is unchanged (notes/economy.md,
   Propositions 4 and 5) and steps 3-5 are skipped.
3. Visible defence: zero simulated leaks against the opponent's active roster
   (plan_defense, partial plans allowed).
4. Unseen purchases. From round ``late_round`` on: plan_defense against
   ``threat_compositions`` of the opponent's full visible gold with at most
   ``spec_share`` of the gold (``spec_partial``: "best" keeps the strongest
   partial plan, "none" spends only on a zero-leak plan). Before
   ``late_round``: only the guard, zero leaks against compositions of
   ``min(opponent gold, guard_gold)`` gold with at most ``guard_share`` of the
   gold, and never a partial plan (``guard_gold=0``: no guard). In round 1
   the guard gold is ``r1_guard``.
5. Saturation: from round ``sat_from`` (default ``late_round``) up to
   ``sat_frac`` of the gold buys splash towards per-copy splash ``sat_target``.
6. Attack (from round ``attack_from``): offense.search on the opponent's
   observed map. Value of a package = a*opt + (1-a)*resp HP (opt: no same-round
   response; resp: the crude response with the opponent's visible gold; a = 1
   while the opponent never owned a turret, else ``alpha``) plus the
   persistence term of v6 (``persist_w``, ``block_k``). Bought if value -
   theta * net gold > 0 (``theta_end`` after ``factory_stop``). Budget: the
   fraction ``attack_frac`` of the gold (``early_attack_frac`` before
   ``late_round``), at most ``min_cap`` copies, own active roster at most
   ``active_cap``.
7. Factories: while round <= ``factory_stop``, up to ``fac_cap`` per round.

The bot reads only its observation and keeps one flag across rounds (whether
the opponent ever owned a turret).
"""
from __future__ import annotations

from bot_research.bots.defense.frozen.v9 import plan as P
from bot_research.harness import gamekit as gk

from .fastsim import MapModel
from .offense import search
from .threat import active_types


def _tuples(buildings):
    return [(b["x"], b["y"], b["type"]) for b in buildings]


def _cost(actions, rules):
    total = 0
    for a in actions:
        op = a["op"]
        if op == "build_wall":
            total += rules["wall_cost"]
        elif op == "build_turret":
            total += rules["turrets"][a["type"]]["cost"]
        elif op == "buy_factory":
            total += rules["globals"]["factory_cost"]
        elif op == "buy_minion":
            total += rules["minions"][a["type"]]["cost"]
    return total


def _with(obs, actions, gold):
    """Copy of the observation with the planned own buildings added and own gold set."""
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


def make(layout="default", walls=True, late_round=6, spec_share=1.0, spec_partial="best",
         guard_gold=0, guard_share=0.5, r1_guard=30, sat_from=None, sat_frac=0.5, sat_target=1600,
         lock=True, r1_units=0, r1_tier="tier1", attack_from=2, theta=0.2, theta_end=0.0, alpha=1.0,
         attack_frac=1.0, early_attack_frac=0.3, min_cap=300, active_cap=500, response="crude",
         persist_w=1.0, block_k=0.5, factory_stop=47, fac_cap=40):
    lay = P.layout_by_name(layout)
    state = {"opp_turrets": {0: False, 1: False}}

    def decide(obs):
        rnd = obs["round"]
        me_i = obs["player"]
        me = obs["players"][me_i]
        op = obs["players"][1 - me_i]
        rules = obs["rules"]
        grules = gk.Rules.from_observation(obs)
        g = rules["globals"]
        max_rounds = g["max_rounds"]
        fcost = g["factory_cost"]
        max_hp = max(m["hp"] for m in rules["minions"].values())
        left = me["gold"]
        actions = []
        if op["n_turrets"] > 0:
            state["opp_turrets"][me_i] = True

        def add(acts):
            nonlocal left
            actions.extend(acts)
            left -= _cost(acts, rules)

        # 0. layout walls
        if walls and left > 0:
            add(P.plan_walls(obs, left, layout=lay, stage=0))
        # 1. round-1 poke
        if rnd == 1 and r1_units:
            c = rules["minions"][r1_tier]["cost"]
            n = min(r1_units, left // c)
            add([{"op": "buy_minion", "type": r1_tier}] * n)

        o2 = _with(obs, actions, left)
        mine = o2["players"][me_i]["buildings"]
        immune = lock and P.splash_damage(mine, grules) >= max_hp
        early = rnd < late_round
        if not immune:
            # 3. visible defence
            visible = P.active_opponent_types(obs)
            if visible and left > 0:
                add(P.plan_defense(o2, left, threat_types=[visible], layout=lay, partial="best"))
                o2 = _with(obs, actions, left)
            # 4. unseen purchases
            if not early and left > 0:
                comps = P.threat_compositions(obs)
                if comps:
                    add(P.plan_defense(o2, int(left * spec_share), threat_types=comps, layout=lay,
                                       partial=spec_partial))
                    o2 = _with(obs, actions, left)
            elif early and left > 0:
                gg = r1_guard if rnd == 1 else guard_gold
                gg = min(op["gold"], gg)
                if gg > 0:
                    comps = P.threat_compositions(obs, extra_gold=gg)
                    if comps:
                        share = 1.0 if rnd == 1 else guard_share
                        add(P.plan_defense(o2, int(left * share), threat_types=comps, layout=lay,
                                           partial="none"))
                        o2 = _with(obs, actions, left)
            # 5. saturation
            if rnd >= (late_round if sat_from is None else sat_from) and left > 0:
                add(P.plan_defense(o2, int(left * sat_frac), required_hp=sat_target, layout=lay,
                                   partial="best"))
                o2 = _with(obs, actions, left)

        # 6. attack
        my_active = active_types(me["roster"], rnd)
        endgame = rnd > factory_stop
        th = theta_end if endgame else theta
        frac = 1.0 if endgame else (early_attack_frac if early else attack_frac)
        budget = int(left * frac)
        room = min(min_cap, active_cap - len(my_active))
        if (rnd >= attack_from and budget >= rules["minions"]["tier1"]["cost"] and room > 0):
            res, _ = search(_tuples(op["buildings"]), my_active, budget, rules,
                            opp_gold=op["gold"], cap=room, responded=response,
                            active_cap=len(my_active) + room, my_gold=me["gold"])
            a = 1.0 if not state["opp_turrets"][me_i] else alpha
            bounty = g["base_hit_bounty"]
            minions = rules["minions"]
            later = {}
            if persist_w > 0:
                # rounds k >= 1 in which the opponent cannot yet afford to stop a copy
                om = MapModel(_tuples(op["buildings"]), rules)
                lone = om.splash_total + sum(d * len(c) for d, c in om.guns)
                inc = (g["factory_income"] * op["n_factories"]
                       + g["path_income_per_step"] * op["length_path"])
                horizon = min(g["roster_lifespan"] - 1, max_rounds - rnd)
                for t, m in minions.items():
                    need = block_k * (m["hp"] - lone)
                    later[t] = sum(1 for k in range(1, horizon + 1)
                                   if op["gold"] + k * inc < need)
            best = None
            for pkg, cost, md_opt, md_resp in res:
                val = a * md_opt + (1 - a) * md_resp
                if later and val > 0:
                    dmg = sum(minions[t]["damage"] for t in pkg)
                    val += persist_w * md_opt * sum(
                        minions[t]["damage"] * later[t] for t in pkg) / dmg
                if val <= 0:
                    continue
                # expected hits: value divided by the package's mean damage per copy
                mean_dmg = sum(minions[t]["damage"] for t in pkg) / len(pkg)
                net = max(1.0, cost - bounty * val / mean_dmg)
                surplus = val - th * net
                key = (surplus, val)
                if surplus > 0 and (best is None or key > best[0]):
                    best = (key, pkg, cost)
            if best is not None:
                _, pkg, cost = best
                add([{"op": "buy_minion", "type": t} for t in pkg])

        # 7. factories
        if rnd <= factory_stop and rnd < max_rounds - 1:
            n = max(0, min(fac_cap, left // fcost))
            add([{"op": "buy_factory"}] * n)
        return actions

    return decide
