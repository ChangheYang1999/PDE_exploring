"""Economy bot v17: econ16 (v16) with attacks held back on maps it did not build itself.

Spec: ``bot_research.bots.economy.econ17:@make?k=v``. All parameters are optional;
the defaults are those of v16, so ``econ17:@make`` plays as ``econ16:@make``.
New parameter ``foreign_attack_from`` (default None: off). The bot records every
cell at which it asked to build a wall or a turret. Once its observed map contains
a building at a cell it never asked for (this happens when the scripted rounds of
a scenario discard its actions and place other buildings), the map is marked
foreign for the rest of the match, and from then on the attack step (step 6 and
the open-case attack) buys nothing before round ``foreign_attack_from``. The
finishing attack (a package that destroys the opponent's base this round) and the
round-1 poke are unchanged. The bot still reads only its observation and its own
state (the opponent-turret flag, the set of requested cells, the foreign flag).
Reason (empirical, 2026-10-31T06:45-06:56Z, notes/economy.md entries 7 and 8): on
scripted openings the template cannot be completed, so the map never reaches the
lock (lock_check: final S 330-1080) and every gold spent on early attacks is
missing from the growth race; v16 free_fallback="zero" with attack_from=11 won
107 of 108 scenario matches (scen17; v16 zero: 89 in scen16), but on the standard
start the same setting lost many matches by 5 to 85 HP (sweep17), because there
early pokes decide close matches.

Description of v16, which v17 keeps:
Spec: ``bot_research.bots.economy.econ16:@make?k=v``. All parameters are optional;
the defaults are those of v15, so ``econ16:@make`` plays as ``econ15:@make``.
Change from v15 (econ15.py, frozen as frozen/v15): with ``free_fallback="zero"``
the fallback plans are computed exactly as with ``"leak"``, but a non-empty
primary plan (hrt-w1's plan_defense with ``layout``) is replaced only by a
fallback plan that answers the threat completely (no simulated roster leaks,
or for the saturation step the per-copy splash reaches the target). When the
primary plan is empty the rule is that of ``"empty"``. Reason (w3dev1, finished
2026-10-31T06:08Z): against hrt-w3's ``feature_bluff:@make?turret_round=3`` (one off-route
gun1 in round 3, factories through round 6, then tier5 waves), v15 with
``free_fallback="leak"`` lost -260 (base destroyed in round 10) in both seats,
while v13 won +705. Replay of round 6 (``experiments/economy/diag_bluff.py``):
the primary plan cost 592 (22 template walls, 2 gun3, 3 gun1, 1 gun2) and the
free plan 600 (splash, gun2, 2 gun3, 2 gun1, no walls); both leak against 5 of
8 threat rosters (worst damage 140), the free plan has the lower leak score
(6623 against 7194) and was bought, so the route stayed at 22 instead of being
lengthened, and the same happened in round 7. The leak score measures only the
current round and does not value the walls.

Description of v15, which v16 keeps:
Change from v14 (econ14.py, frozen as frozen/v14): every defence purchase goes
through ``defend``. It first calls hrt-w1's plan_defense with ``layout`` as
before. With ``free_fallback="empty"`` (default), if that plan is empty while
the threat is not answered (some simulated roster of the threat list still
leaks on the current map, or for the saturation step the per-copy splash is
below the target), a layout-free plan is computed and bought if it improves
the answer: for a threat list, ``freeplan.free_plan`` (greedy turrets on any
legal cell off the current route, exact simulation, this lane); for the
saturation target, hrt-w1's plan_defense with an empty layout (no walls, no
reserved cells, every legal cell next to the route a splash candidate). With
``free_fallback="leak"`` the fallback is also tried when the primary plan is not
empty but still leaks, both alone and appended to the primary plan, and the
best plan is bought (zero leaks at least cost first, otherwise the lower hrt-w1
leak score, then the cheaper).
``free_fallback=null`` restores v14. Reason (scen13, finished 2026-10-31T05:07Z): under
the harness opening mirror:1:2, v13 lost -800 to lead v4/v5/v6 and fortress v9
(attack variant). Replay of v13 vs lead v4 (round 11): exactly 8 own buildings
lay outside the lead_v3 template, so v15's foreign-map rule (more than 8) did
not apply; no template cell was left, plan_defense returned [] even with
partial="best", a visible tier5 leaked and v13 bought 40 factories with 1773
gold. On that map one gun3 at (4, 6) (200 gold) stops the visible roster;
v15's gun candidates were 8 illegal route cells (the top 8 by coverage are cut
before the legality test). econ12's fallback to the named "default" layout (a
second template with its own walls) did not fix this and is not used.

Description of v14, which v15 keeps:
New parameters
``early_threat`` (default null: off, then v14 plays as v13), ``early_from``
(2), ``early_share`` (1.0) and ``early_partial`` ("none"). In rounds
``early_from <= round < late_round``, after the visible defence, the bot
simulates every roster of threat_compositions (the opponent's active roster
followed by each purchase list its full visible gold allows; hrt-w1's frozen
v15 planner) on its own current map. If the largest base damage of these
rosters is at least ``early_threat``, it buys plan_defense against all of them
with ``early_share`` of its remaining gold (``early_partial`` as in
plan_defense: "none" buys only a zero-leak plan). Reason (known13,
2026-10-31T05:05Z): v13 lost 14 to 60 HP against hrt-w3's exact-forecast
timing counter attacking with all its gold in rounds 3 to 5 (tier3 at round
3/4/5, tier4 at round 5), because before ``late_round`` (6) v13 insures
only against the visible roster. The lead's screen (NOTES_FOR_TEAM
04:57Z, ``big_threat``) suggests the same remedy for its bot.

Description of v13, which v14 keeps:
Change from v11 (econ11.py, frozen as frozen/v11): the default of ``r1_units``
is 1 instead of 0 (one tier1 bought in round 1, after the layout walls).
Reason (sweep10, 2026-10-31 04:53Z, 34 opponents of opp_key4.txt, both
seats, standard start): econ10 with r1_units 0/1/2/3/4 scored 60-0-8, 66-2-0,
52-8-8, 62-2-4 and 52-0-16 (W-D-L). With 0 it lost by 5 to poke_lock
(opening 1) and the lead's v4/v5/v6, whose round-1 tier1 poke lands
unanswered; with 1 those matches are wins or draws and no match is lost.
econ12's alternative-layout fallback (alt_layouts) is not included: it did
not improve the scripted openings (scen12s) and lost -800 to fortress v14
under mirror:1:2.

Description of v11, which v13 keeps:
Change from v10 (econ10.py, frozen as frozen/v10): the defence component is
``bots/defense/frozen/v15/plan.py`` instead of v11. v15 adds a foreign-map
fallback: when the own map holds more than 8 buildings outside the master
layout (for example after a scripted opening), the splash and gun candidate
cells include every legal cell next to the route. Reason (scen10, 2026-10-31
04:25Z): under the harness openings mirror:1:2 and asym:3:2, v10 lost -267 to
-942 (base destroyed in rounds 10-13) against lead_best_a/b and econ v2/v3,
whose single tier4/tier5 pokes leaked every round because the template
planner found no zero-leak plan on the scripted map.

Description of v10, which v11 keeps:
Every plan_defense call passes ``time_budget=plan_time`` (default 1e6 seconds,
i.e. no cutoff). hrt-w1's planner stops its gun pass after 3 s by default, so
with the default the purchases could depend on the machine's speed and load
rather than on the observation alone; v9 reached 2.8-3.1 s per decision
against the lead's v4/v5 in sweep9. With the cutoff disabled the actions are a
function of the observation and the bot's state only. Values in a spec are
parsed as JSON by the harness: write ``none_frac=null`` and ``finish=null``,
not ``None``.

Description of v9, which v10 keeps:
Changes from v8 (econ8.py, frozen as frozen/v8): the defence component is
``bots/defense/frozen/v11/plan.py`` (same API as v9; v10 added exhaustive
enumeration of every ordered purchase list when the opponent's gold allows at
most 400 of them, v11 a helper). Finishing attack (``finish``, after the
visible defence): if some attack package bought with all remaining gold
removes the opponent's whole HP this round on its current map together
with the own active roster (``finish="opt"``), or by itself under the crude
same-round response (``finish="resp"``), the cheapest such package is bought
before the other purchases (``finish=null`` in a spec: off). Nothing is bought
when the active roster alone already deals the opponent's HP on its current
map. The idea is hrt-w1's finish rule (defense.md 03:44Z). Default changed
from v8: ``layout="lead_v3"`` (sweep8: v8 with lead_v3 was 52-0-2 against
opp_key2, v8 default 48-0-6).

Description of v8, which v9 keeps:
Changes from v7 (econ7.py, frozen as frozen/v7): from round ``none_from`` on,
while the opponent has never owned a turret (the "open" case; by then it has
seen our early pokes and not answered them), the attack runs before steps 4-5
(``none_first``) with the fraction ``none_frac`` of the gold (``none_frac=None``
turns the open case off), copies are assumed to keep hitting for the
rest of their lifetime (``none_persist``), and the value of a package is
capped at the opponent's HP (``cap_hp``). ``spec_splash``: when no zero-leak
plan against the unseen purchases is affordable, the partial plan is
splash-only (permanent progress to the lock) instead of the planner's least-leak
plan. Reason (sweep7): v7 lost -450 to eco6_t5, which never builds a turret,
because it poked with 30 % of its gold in rounds 2-5 and then spent rounds 6-8
on gun3/gun2 partial plans against a tier5 flood it could not stop. Default
changed from v7: ``r1_guard=0`` (no round-1 guard; sweep7: v7 with
``r1_guard=0`` was 48-0-6 against opp_key2, v7 default 40-4-10).

Description of v7, which v8 keeps:
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

from bot_research.bots.defense.frozen.v15 import plan as P
from bot_research.bots.defense.frozen.v15.simulate import simulate_leak
from bot_research.harness import gamekit as gk

from .fastsim import MapModel
from .freeplan import free_plan
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


def _worst_damage(obs, comps):
    """Largest base damage of the rosters ``comps`` on the own map of ``obs`` (exact simulation)."""
    _, rl, buildings, blocked = P.observe(obs)
    path = gk.route_cached(blocked)
    profile = gk.splash_profile(path, buildings, rl)
    guns = gk.gun_coverage(path, buildings, rl)
    return max(simulate_leak(t, path, buildings, rl, profile=profile, guns=guns)[1] for t in comps)


def make(layout="lead_v3", walls=True, late_round=6, spec_share=1.0, spec_partial="best", spec_splash=False,
         guard_gold=0, guard_share=0.5, r1_guard=0, sat_from=None, sat_frac=0.5, sat_target=1600,
         lock=True, r1_units=1, r1_tier="tier1", attack_from=2, theta=0.2, theta_end=0.0, alpha=1.0,
         attack_frac=1.0, early_attack_frac=0.3, min_cap=300, active_cap=500, response="crude",
         persist_w=1.0, block_k=0.5, factory_stop=47, fac_cap=40,
         none_from=4, none_frac=1.0, none_persist=True, none_first=True, cap_hp=True,
         finish="opt", plan_time=1e6, early_threat=None, early_from=2, early_share=1.0,
         early_partial="none", free_fallback="empty", foreign_attack_from=None):
    lay = P.layout_by_name(layout)
    free = P.MasterLayout([], [], [], [0, 0, 0], {}, set(), 0)
    state = {"opp_turrets": {0: False, 1: False}, "req": {0: set(), 1: set()},
             "foreign": {0: False, 1: False}}

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
        if foreign_attack_from is not None and not state["foreign"][me_i]:
            req = state["req"][me_i]
            if any((b["x"], b["y"]) not in req for b in me["buildings"]):
                state["foreign"][me_i] = True
        hold = (foreign_attack_from is not None and state["foreign"][me_i]
                and rnd < foreign_attack_from)
        open_case = not state["opp_turrets"][me_i] and rnd >= none_from

        def add(acts):
            nonlocal left
            actions.extend(acts)
            left -= _cost(acts, rules)

        def defend(o2, budget, partial, threat_types=None, required_hp=None):
            """plan_defense with ``layout``, then with the empty layout if needed (docstring)."""
            kw = dict(threat_types=threat_types, required_hp=required_hp, time_budget=plan_time,
                      partial=partial)
            first = P.plan_defense(o2, budget, layout=lay, **kw)
            if not free_fallback or (first and free_fallback not in ("leak", "zero")):
                return first

            def key(acts):
                cost = _cost(acts, rules)
                _, rl, b, bl = P.observe(_with(o2, acts, o2["players"][me_i]["gold"] - cost))
                if threat_types:
                    score, hits = P._leak(b, bl, rl, threat_types)
                    return (1, -cost, 0) if hits == 0 else (0, -score, -cost)
                sd = P.splash_damage(b, rl, bl)
                return (1, -cost, 0) if sd >= required_hp else (0, sd, -cost)

            k_first = key(first)
            if k_first[0] == 1:
                return first
            if not threat_types:
                other = P.plan_defense(o2, budget, layout=free, **kw)
                if free_fallback == "zero" and first and not (other and key(other)[0] == 1):
                    return first
                return other if other and key(other) > k_first else first
            plans = [free_plan(o2, budget, threat_types, partial=partial)]
            if first:
                c1 = _cost(first, rules)
                plans.append(first + free_plan(_with(o2, first, o2["players"][me_i]["gold"] - c1),
                                               budget - c1, threat_types, partial=partial))
            best = max(plans, key=key)
            if free_fallback == "zero" and first and not (best and key(best)[0] == 1):
                return first
            return best if best and key(best) > k_first else first

        def attack(frac):
            if hold:
                return
            my_active = active_types(me["roster"], rnd)
            endgame = rnd > factory_stop
            th = theta_end if endgame else theta
            budget = int(left * (1.0 if endgame else frac))
            room = min(min_cap, active_cap - len(my_active))
            if not (rnd >= attack_from and budget >= rules["minions"]["tier1"]["cost"] and room > 0):
                return
            res, _ = search(_tuples(op["buildings"]), my_active, budget, rules,
                            opp_gold=op["gold"], cap=room, responded=response,
                            active_cap=len(my_active) + room, my_gold=me["gold"])
            a = 1.0 if not state["opp_turrets"][me_i] else alpha
            bounty = g["base_hit_bounty"]
            minions = rules["minions"]
            horizon = min(g["roster_lifespan"] - 1, max_rounds - rnd)
            later = {}
            if open_case and none_persist:
                later = {t: horizon for t in minions}
            elif persist_w > 0:
                # rounds k >= 1 in which the opponent cannot yet afford to stop a copy
                om = MapModel(_tuples(op["buildings"]), rules)
                lone = om.splash_total + sum(d * len(c) for d, c in om.guns)
                inc = (g["factory_income"] * op["n_factories"]
                       + g["path_income_per_step"] * op["length_path"])
                for t, m in minions.items():
                    need = block_k * (m["hp"] - lone)
                    later[t] = sum(1 for k in range(1, horizon + 1)
                                   if op["gold"] + k * inc < need)
            pw = 1.0 if open_case and none_persist else persist_w
            best = None
            for pkg, cost, md_opt, md_resp in res:
                val = a * md_opt + (1 - a) * md_resp
                if later and val > 0:
                    dmg = sum(minions[t]["damage"] for t in pkg)
                    val += pw * md_opt * sum(minions[t]["damage"] * later[t] for t in pkg) / dmg
                if cap_hp:
                    val = min(val, op["hp"])
                if val <= 0:
                    continue
                # expected hits: value divided by the package's mean damage per copy
                mean_dmg = sum(minions[t]["damage"] for t in pkg) / len(pkg)
                net = max(1.0, cost - bounty * val / mean_dmg)
                surplus = val - th * net
                key = (surplus, val, -cost)
                if surplus > 0 and (best is None or key > best[0]):
                    best = (key, pkg)
            if best is not None:
                add([{"op": "buy_minion", "type": t} for t in best[1]])

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
                add(defend(o2, left, "best", threat_types=[visible]))
                o2 = _with(obs, actions, left)
        # finishing attack (v9)
        attacked = False
        if finish and rnd >= attack_from and left >= rules["minions"]["tier1"]["cost"]:
            my_active = active_types(me["roster"], rnd)
            room = min(min_cap, active_cap - len(my_active))
            if room > 0:
                res, base0 = search(_tuples(op["buildings"]), my_active, left, rules,
                                    opp_gold=op["gold"], cap=room, responded=response,
                                    active_cap=len(my_active) + room, my_gold=me["gold"])
                # opt: the active roster's damage plus the package's; resp: the package alone
                kill = [] if base0 >= op["hp"] else [
                    (cost, pkg) for pkg, cost, md_opt, md_resp in res
                    if (md_resp if finish == "resp" else base0 + md_opt) >= op["hp"]]
                if kill:
                    add([{"op": "buy_minion", "type": t} for t in min(kill)[1]])
                    attacked = True
                    o2 = _with(obs, actions, left)
        # 6 (open case, v8): attack before the unseen-purchase defence
        if not attacked and open_case and none_first and none_frac is not None:
            attack(none_frac)
            attacked = True
            o2 = _with(obs, actions, left)
        if not immune:
            # 4. unseen purchases
            if not early and left > 0:
                comps = P.threat_compositions(obs)
                if comps:
                    budget = int(left * spec_share)
                    if spec_splash:
                        acts = defend(o2, budget, "none", threat_types=comps)
                        if not acts:
                            _, rl, b0, bl0 = P.observe(o2)
                            if P._leak(b0, bl0, rl, comps)[1] > 0:
                                acts = defend(o2, budget, "best", required_hp=P.max_hp(
                                    [t for c in comps for t in c], rl))
                    else:
                        acts = defend(o2, budget, spec_partial, threat_types=comps)
                    add(acts)
                    o2 = _with(obs, actions, left)
            elif early and left > 0:
                gg = r1_guard if rnd == 1 else guard_gold
                gg = min(op["gold"], gg)
                if gg > 0:
                    comps = P.threat_compositions(obs, extra_gold=gg)
                    if comps:
                        share = 1.0 if rnd == 1 else guard_share
                        add(defend(o2, int(left * share), "none", threat_types=comps))
                        o2 = _with(obs, actions, left)
                # threat-triggered early insurance (v14)
                if early_threat is not None and rnd >= early_from and left > 0:
                    comps = P.threat_compositions(obs)
                    if comps and _worst_damage(o2, comps) >= early_threat:
                        add(defend(o2, int(left * early_share), early_partial, threat_types=comps))
                        o2 = _with(obs, actions, left)
            # 5. saturation
            if rnd >= (late_round if sat_from is None else sat_from) and left > 0:
                add(defend(o2, int(left * sat_frac), "best", required_hp=sat_target))
                o2 = _with(obs, actions, left)

        # 6. attack
        if not attacked:
            frac = none_frac if (open_case and none_frac is not None) else (
                early_attack_frac if early else attack_frac)
            attack(frac)

        # 7. factories
        if rnd <= factory_stop and rnd < max_rounds - 1:
            n = max(0, min(fac_cap, left // fcost))
            add([{"op": "buy_factory"}] * n)
        if foreign_attack_from is not None:
            state["req"][me_i].update((a["x"], a["y"]) for a in actions
                                      if a["op"] in ("build_wall", "build_turret"))
        return actions

    return decide
