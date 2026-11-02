"""Economy bot: worst-case defence first, opportunistic attack, factories with the rest.

Spec: ``bot_research.bots.economy.econ:@make?k=v``. All parameters are optional.

Per round, in this order:
1. Round 1 only: buy ``r1_factories`` factories before anything else.
2. Defence: ``defense_plan.defend`` adds slot-serpentine turrets/walls until the
   worst simulated leak over the attack families of ``threat.packages`` (for the
   opponent's visible gold plus ``margin`` times it, after its active roster) is
   at most ``tolerate`` (``tolerate_late`` from round ``late_round`` on). Before
   ``late_round`` only the fraction ``phi`` of the opponent's gold is assumed
   spendable on attack (``phi=0``: defend against the visible roster only).
3. Attack: ``offense.search`` evaluates attack packages on the opponent's
   observed map (optimistic: no new opponent building; responded: a crude
   same-round response with the opponent's visible gold). The value of a
   package is ``a*opt + (1-a)*resp`` HP, where ``a`` is 1 while the opponent has
   never owned a turret and ``alpha`` otherwise. The package maximising
   value - theta * net gold (cost minus expected bounty) is bought if that
   surplus is positive; ``theta`` is the HP price of one gold (``theta_end``
   from round ``factory_stop + 1`` on). At most ``attack_frac`` of the gold
   left after defence is used. ``response="defend"`` replaces the crude
   response by this lane's own defence builder answering our visible gold.
2b. Saturation: from round ``sat_from`` (default ``late_round``) up to
   ``sat_frac`` of the remaining gold buys splash slots until the per-copy splash
   on the route reaches ``sat_target``. ``reserve``: guns are placed only where
   the completed template can still reach that per-copy splash.
4. Factories: while round <= ``factory_stop``, buy up to ``fac_cap`` factories.
   A factory bought in round r returns 15*(50-r) usable gold, so it pays for
   r <= 48 only.

Early guard: before ``late_round`` the threat gold is at least
``min(opponent gold, guard_gold)`` (cheap early attacks are defended), with
tolerance ``guard_tol`` when given. Lock (``lock=True``): once the own route's
per-copy splash is at least the largest minion HP, no copy can arrive while
the route is unchanged (notes/economy.md, Proposition 4), so the bot stops
building turrets and walls.

Round 1 (v4 options): ``r1_units`` copies of ``r1_tier`` are bought first
(a round-1 poke); with ``r1_guard`` > 0 the round-1 defence runs before any
factory against packages of at most ``min(opponent gold, r1_guard)`` gold, no
attack search runs in round 1, and the factories are bought from what is left. Before ``late_round`` the attack
may use only ``early_attack_frac`` of the gold left after defence and at most
``early_min_cap`` copies (both default to the late values), so that pokes do
not stop factory growth.

Caps: at most ``min_cap`` minions per round, own active roster at most
``active_cap``; threat families use at most ``threat_cap`` new copies.
The bot reads only its observation and keeps no cross-round state except a
flag recording whether the opponent ever owned a turret.
"""
from __future__ import annotations

from .defense_plan import defend, saturate
from .fastsim import MapModel
from .offense import search
from .threat import active_types


def _tuples(buildings):
    return [(b["x"], b["y"], b["type"]) for b in buildings]


def make(r1_factories=5, tolerate=0, tolerate_late=0, late_round=1, margin=0.0, phi=1.0,
         factory_stop=47, fac_cap=40, min_cap=300, active_cap=500, threat_cap=600,
         theta=0.2, theta_end=0.0, alpha=0.3, attack_frac=1.0, attack_from=1,
         response="crude", reserve=1600, sat_target=1600, sat_from=None, sat_frac=0.5,
         guard_gold=0, guard_tol=None, lock=True, r1_guard=0, r1_units=0, r1_tier="tier1",
         early_attack_frac=None, early_min_cap=None):
    state = {"opp_turrets": {0: False, 1: False}}

    def decide(obs):
        rnd = obs["round"]
        me_i = obs["player"]
        me = obs["players"][me_i]
        op = obs["players"][1 - me_i]
        rules = obs["rules"]
        g = rules["globals"]
        max_rounds = g["max_rounds"]
        fcost = g["factory_cost"]
        gold = me["gold"]
        max_hp = max(m["hp"] for m in rules["minions"].values())
        actions = []
        if op["n_turrets"] > 0:
            state["opp_turrets"][me_i] = True

        # 1. round-1 opening: optional poke, then factories (skipped when r1_guard
        # asks for a round-1 defence first; the final factory step buys the rest)
        if rnd == 1 and r1_units:
            c = rules["minions"][r1_tier]["cost"]
            n = min(r1_units, gold // c)
            actions += [{"op": "buy_minion", "type": r1_tier}] * n
            gold -= n * c
        if rnd == 1 and r1_factories and not r1_guard:
            n = min(r1_factories, gold // fcost)
            actions += [{"op": "buy_factory"}] * n
            gold -= n * fcost

        # 2. defence
        opp_active = active_types(op["roster"], rnd)
        early = rnd < late_round
        tol = tolerate if early else tolerate_late
        threat_gold = int(op["gold"] * ((phi if early else 1.0) + margin))
        if early and guard_gold:
            threat_gold = max(threat_gold, min(op["gold"], guard_gold))
            if guard_tol is not None:
                tol = guard_tol
        if rnd == 1 and r1_guard:
            threat_gold = max(threat_gold, min(op["gold"], r1_guard))
        my_buildings = _tuples(me["buildings"])
        # lock: per-copy splash >= the largest minion HP means no copy can ever
        # arrive while the route is unchanged, so build nothing more
        immune = lock and MapModel(my_buildings, rules).splash_total >= max_hp
        if not immune:
            d_actions, my_buildings, gold, worst = defend(
                my_buildings, gold, opp_active, threat_gold, rules,
                cap=threat_cap, tolerate=tol, reserve=reserve)
            actions += d_actions
        # 2b. saturation: per-copy splash >= sat_target makes the map immune to
        # every copy with HP <= sat_target on this route (tier5 HP is 1500)
        if not immune and rnd >= (late_round if sat_from is None else sat_from) and gold > 0:
            s_actions, my_buildings, left, _ = saturate(
                my_buildings, int(gold * sat_frac), sat_target, rules)
            actions += s_actions
            gold -= int(gold * sat_frac) - left

        # 3. attack
        my_active = active_types(me["roster"], rnd)
        endgame = rnd > factory_stop
        th = theta_end if endgame else theta
        frac = attack_frac if (not early or early_attack_frac is None) else early_attack_frac
        budget = int(gold * (1.0 if endgame else frac))
        mcap = min_cap if (not early or early_min_cap is None) else early_min_cap
        room = min(mcap, active_cap - len(my_active))
        r1_skip = rnd == 1 and r1_guard  # a guarded round 1 keeps its gold for factories
        if (rnd >= attack_from and not r1_skip and budget >= rules["minions"]["tier1"]["cost"]
                and room > 0):
            res, _ = search(_tuples(op["buildings"]), my_active, budget, rules,
                            opp_gold=op["gold"], cap=room, responded=response,
                            active_cap=len(my_active) + room, my_gold=me["gold"])
            a = 1.0 if not state["opp_turrets"][me_i] else alpha
            bounty = g["base_hit_bounty"]
            best = None
            for pkg, cost, md_opt, md_resp in res:
                val = a * md_opt + (1 - a) * md_resp
                if val <= 0:
                    continue
                # expected hits: value divided by the package's mean damage per copy
                mean_dmg = sum(rules["minions"][t]["damage"] for t in pkg) / len(pkg)
                net = max(1.0, cost - bounty * val / mean_dmg)
                surplus = val - th * net
                key = (surplus, val)
                if surplus > 0 and (best is None or key > best[0]):
                    best = (key, pkg, cost)
            if best is not None:
                _, pkg, cost = best
                actions += [{"op": "buy_minion", "type": t} for t in pkg]
                gold -= cost

        # 4. factories
        if rnd <= factory_stop and rnd < max_rounds - 1:
            n = max(0, min(fac_cap, gold // fcost))
            actions += [{"op": "buy_factory"}] * n
            gold -= n * fcost
        return actions

    return decide
