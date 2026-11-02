"""Economy bot v24: econ23 (v23) with the bot's own buildings never counted as foreign.

Spec: ``bot_research.bots.economy.econ24:@make?k=v``. Defaults are those of v23. New
parameter (written 2026-10-31T11:34Z, shift 2 of hrt-w2): ``own_in_layout`` (default False:
v23). With own_in_layout=true, every call of hrt-w1's frozen v15 planner (plan_defense in
defend and lock_reachable) gets the layout in use with its final_adj extended by the cells of
the own buildings this bot requested (value 0). v15's is_foreign then counts only cells this
bot never requested (scripted or otherwise alien) outside the layout, so the planner keeps
the layout's exclusions (final route, wall order, reserved splash capacity) while the bot
adds guns off the layout. The extension changes nothing else in the planner: the added cells
are occupied, so they are never candidates, and their value 0 adds nothing to
reserved_capacity. Reason (runs/economy/w1v29b, mirror:21:2 against hrt-w1's fortress v28,
v23 lost -2692 in both seats): v23 adopted a re-planned layout (11 walls, 25 reserved splash
cells, final route 56). Guns bought against the fortress's early attacks at rounds 4 to 8 lay
next to the current route (length 22), which is not the final route, so outside the final
layout; at round 9 the tenth such building made the map foreign for v15, guns went onto
reserved and final-route cells (rounds 9 and 11) and the round-12 splashes (18) partly onto
final-route cells, giving per-copy splash 580 at route length 24 instead of the lock.

Description of v23, which v24 keeps:
Spec: ``bot_research.bots.economy.econ23:@make?k=v``. Defaults are those of v21. New
parameter (written 2026-10-31T11:13Z, shift 2 of hrt-w2): ``replan_base`` (default False: v21).
With replan_base=true and replan_gain set, whenever the re-plan rule fires, the layout in
use becomes the re-planned one if its score (_s_final) exceeds the score of the base
layout (``layout``, lead_v3) on the current buildings by at least replan_gain, and the
base layout otherwise; a layout adopted earlier in the match is not kept. needs_replan is
asked about the base layout. So the choice depends only on the current own buildings and
the round (the seed), not on earlier re-plans. Reason (runs/economy/ho21, diag26 and
the trace of hrt-w2 scratch/replan_trace.py, mirror:36:3, pool eco6_t5): the bot also
decides during the scripted rounds (its actions are replaced), so the never-requested
cells appear one round at a time and v21 re-plans at rounds 2, 3 and 4. It adopted the
round-2 plan (1320 against lead_v3's 870) and the round-3 plan (950 against 520, the
round-2 plan on the round-3 map), then rejected the round-4 plan (390 against 170) and
kept the round-3 plan, whose score on the final map (170) is below both the round-4 plan
(390) and lead_v3 (250). v21 lost -710 in both seats where v19 (lead_v3) won +108, and
v21 with foreign_sat_from=null lost the same.

Description of v21, which v23 keeps:
Economy bot v21: econ20 (v20) with a gain test before adopting a re-planned layout.

Spec: ``bot_research.bots.economy.econ21:@make?k=v``. Defaults are those of v20. New
parameter (written 2026-10-31T10:22Z, shift 2 of hrt-w2): ``replan_gain`` (default None:
adopt every re-planned layout, as v20). When set, a layout designed by replan_layout is
adopted only if its per-copy splash on its final route (hrt-w1's frozen v26 scorer
replan._score: the best 25 cells by final adjacency plus existing splashes) exceeds the
same score of the current layout, built as far as the existing buildings allow, by at
least replan_gain; otherwise the current layout is kept (and the replan is not repeated
until the set of never-requested cells changes). Reason (runs/economy/diag24, pool
eco6_t5, asym:3:2 seat 1 and asym:24:3 seat 0): the re-planned layouts route with their
splash slots (with the re-planned walls alone the route is 22 on 16 of 18 scripted maps checked), while
the walls of lead_v3 alone give a route of 22-48 for at most 33 gold; against a tier5 flood from
round 7 v20 (and v20 without foreign_sat_from) lost -790 and -878 where v19 won +543 and
+831. On those two maps the score gain of re-planning is 310 and 210; on mirror:1:2, where
re-planning beat fortress v25 (+525), it is 410.

Description of v20, which v21 keeps:
Economy bot v20: econ19 (v19) with hrt-w1's layout re-planner on scripted-opening maps.

Spec: ``bot_research.bots.economy.econ20:@make?k=v``. Defaults are those of v19 (so of
v17). New parameters (written 2026-10-31T09:36Z, shift 2 of hrt-w2): ``replan`` (default False)
and ``replan_iters`` (default 5000). With replan=true the bot records every cell it
requested (walls and turrets). At every decision, if the own map holds a building at a
cell it never requested (only a scripted opening places such buildings), the set of those
cells differs from the set at the last re-plan, and hrt-w1's frozen v26
replan.needs_replan says that the current layout (``layout``, or the last re-planned one),
built as far as the existing buildings allow, cannot reach per-copy splash 1500, then
replan.replan_layout(own buildings, iters=replan_iters, seed=round) (deterministic: no
wall-clock cutoff) designs a new MasterLayout around all existing own buildings, and every
later layout use of the match (layout walls, plan_defense, the reachability test of
sat_reach) takes it in place of ``layout``. This is the rule of hrt-w1's fortress v25/v26
(replan_foreign), except that foreign means never requested (this bot also builds cells
outside its layout through free_plan). Reason (runs/defense/x73_v25_econ17, hrt-w1):
fortress v25 beat v17 under mirror:1:2 (round 18), mirror:22:3 (round 16) and asym:3:2
(rounds 35 and 37); under mirror:1:2 v25 had 26 splashes on a route of 70 by round 10 and
then flooded with 28 tier5, while v17, with 484 factories against 357, had no plan to the
lock with the lead_v3 layout on that map. Conjecture: with the re-planned layout the bot
reaches the lock on more scripted maps.
``foreign_sat_from`` (default None: off; written 2026-10-31T09:55Z). On a foreign map (the
flag of foreign_attack_from: a building at a cell the bot never requested; so this needs
foreign_attack_from set) step 5 (saturation) is skipped before round foreign_sat_from.
Reason (runs/economy/smoke20, asym:3:2, seat 0, against fortress v25): with replan=true
the bot bought 32 splashes in rounds 6 to 10 on the re-planned layout, had 214 factories
and 3289 gold at round 10 (v19: 329 and 4990, a 6-tier5 kill in rounds 10 and 11), found
no kill before v25's lock and lost 770 to 800 at round 50.

Description of v19, which v20 keeps:
Economy bot v19: econ18 (v18) with saturation only while the lock is reachable.

Spec: ``bot_research.bots.economy.econ19:@make?k=v``. Defaults are those of v18 (so of
v17). New parameter (written 2026-10-31T09:22Z, shift 2 of hrt-w2):
``sat_reach`` (default False). Step 5 (saturation: up to ``sat_frac`` of the remaining
gold for splash toward per-copy splash ``sat_target``) runs only if hrt-w1's frozen v15
plan_defense, given unlimited gold (10**7) and partial="none", returns a splash plan
reaching the largest minion HP (1500, the lock of Proposition 4) with ``layout`` or with
the empty layout. Reason (experiments/economy/reach_check.py, runs/economy/reach_v21.txt
and reach_std_v9a.txt): against fortress v21 under mirror:22:3 neither layout reaches 1500
from round 4 on (69 empty cells at round 4), yet v17 spent about 1020 gold on splash in
rounds 6 to 10 (this step) and about 1970 on guns in rounds 4 to 12 (steps 3 and 4,
unchanged here), ended with 33 turrets and per-copy splash 460, fell behind in factories
(154 against 184 at round 13) and lost the tier5 race; on the standard start
against best_v9a the lead_v3 layout reaches 1500 at rounds 2 to 8 and the lock holds from
round 10, so saturation is unchanged there. Conjecture: on maps where the lock is out of
reach, saturation gold is better spent on factories. Use with a larger ``fac_cap``
(fcap1, notes entry 11: fac_cap does not change play on the standard start).

Description of v18, which v19 keeps:
Spec: ``bot_research.bots.economy.econ18:@make?k=v``. All parameters are optional;
the defaults are those of v17, so ``econ18:@make`` plays as ``econ17:@make``.
New parameters (written 2026-10-31T08:01Z, shift 2 of hrt-w2):
``hold_income`` (default None: off). When set, the foreign hold of v17 (no attack
purchases before ``foreign_attack_from`` on a map with buildings the bot never
requested) applies only in rounds in which the own visible income is at least
``hold_income`` times the opponent's, income = factory_income x factories +
path_income_per_step x route length (both read from the observation; hit bounties
are not included). Reason (notes/economy.md entry 10): under asym:23:2 in seat 1,
v17 holds its attacks while the scripted rounds have left it behind in factories,
and a greedy opponent that never defends reaches tier5 first (three losses of
-719); v16, which attacks, wins the same matches. Conjecture: holding pays only
while the own economy keeps up.
``doom`` (default False; True or "next"). After the defence steps, the bot simulates every
roster of hrt-w1's threat_compositions (the opponent's active roster followed by
each purchase its full visible gold allows) on its own map with this round's
construction. If the largest base damage is at least the own HP, no affordable
defence was found that prevents a possibly lethal round, and the remaining gold
has no defensive use this round; the bot then buys, with all remaining gold, the
attack package (offense.search, no response model) with the largest damage on the
opponent's current map this round (ties: the cheaper), before factories.
With doom="next" it also fires when the same test with the opponent's gold plus its
visible income (next round's purchasing power) reaches the own HP and this lane's
layout-free free_plan, given our remaining gold plus our income, finds no
construction on the current map that brings that damage below the own HP. Reason
for firing a round early: roster entries respawn every round for 12 rounds, so a
package bought now also attacks next round, and next round's gold adds to it.
Reason (loss review, experiments/economy/capacity.py, timeline.py and diag_flood.py
on the log of frozen v17 against hrt-w1's fortress v21 under mirror:22:3, seat 0):
our map was full (2 empty cells, per-copy splash 460) from round 12; the opponent had
4062 and 6660 gold at the decisions of rounds 13 and 14; v17 bought only factories
with 2411 and 4563 gold and was destroyed by 10 tier5 in round 14 (-845). diag_flood
(2026-10-31T08:50Z): worst damage of threat_compositions 280 at round 13 and 840 at round
14 (own HP 730), and no planner finds any construction at either round. doom=True
fires only in round 14 (smoke18: 7 tier5, 700 of the opponent's 735 HP, -145, still a
loss). Both players destroyed in the same round is a draw (engine.py, RULES.md).

Description of v17, which v18 keeps:
Spec: ``bot_research.bots.economy.econ17:@make?k=v``. All parameters are optional;
the defaults are those of v16, so ``econ17:@make`` plays as ``econ16:@make``.
New parameter ``foreign_attack_from`` (default None: off). The bot records every
cell at which it asked to build a wall or a turret. Once its observed map contains
a building at a cell it never asked for (this happens when the scripted rounds of
a scenario discard its actions and place other buildings), the map is marked
foreign for the rest of the match, and from then on the attack step (step 6 and
the open-case attack) buys nothing before round ``foreign_attack_from``. The
finishing attack (a package that destroys the opponent's base this round) and the
round-1 poke are unchanged. With ``foreign_open=False`` (added at 2026-10-31T07:04Z,
after the freeze of frozen/v17; the default True keeps the frozen/v17 behaviour)
the hold applies only after the opponent has owned a turret, so attacks on an
opponent that never defended continue. Reason: scen18, frozen v17 with
foreign_attack_from=11 lost -719 to pool eco6_t5 under asym:23:2 (seat 1), a
match v16 won. The bot still reads only its observation and its own state (the
opponent-turret flag, the set of requested cells, the foreign flag).
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

import dataclasses

from bot_research.bots.defense.frozen.v15 import plan as P
from bot_research.bots.defense.frozen.v15.simulate import simulate_leak
from bot_research.bots.defense.frozen.v26 import replan as R
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


def _s_final(buildings, layout):
    """Per-copy splash of ``layout`` on its final route, built as far as the existing buildings allow
    (hrt-w1's frozen v26 scorer, 25 slots plus existing splashes; 0 if no route)."""
    fixed = {(b["x"], b["y"]) for b in buildings}
    fixed_splash = {(b["x"], b["y"]) for b in buildings if b["type"] == "splash"}
    chosen = R._legal_subset(fixed, list(layout.wall_order) + list(layout.splash_cells))
    sc = R._score(fixed, fixed_splash, chosen, 25)
    return 0 if sc is None else sc[1]


def make(layout="lead_v3", walls=True, late_round=6, spec_share=1.0, spec_partial="best", spec_splash=False,
         guard_gold=0, guard_share=0.5, r1_guard=0, sat_from=None, sat_frac=0.5, sat_target=1600,
         lock=True, r1_units=1, r1_tier="tier1", attack_from=2, theta=0.2, theta_end=0.0, alpha=1.0,
         attack_frac=1.0, early_attack_frac=0.3, min_cap=300, active_cap=500, response="crude",
         persist_w=1.0, block_k=0.5, factory_stop=47, fac_cap=40,
         none_from=4, none_frac=1.0, none_persist=True, none_first=True, cap_hp=True,
         finish="opt", plan_time=1e6, early_threat=None, early_from=2, early_share=1.0,
         early_partial="none", free_fallback="empty", foreign_attack_from=None, foreign_open=True,
         hold_income=None, doom=False, sat_reach=False, replan=False, replan_iters=5000,
         foreign_sat_from=None, replan_gain=None, replan_base=False, own_in_layout=False):
    base_lay = P.layout_by_name(layout)
    free = P.MasterLayout([], [], [], [0, 0, 0], {}, set(), 0)
    state = {"opp_turrets": {0: False, 1: False}, "req": {0: set(), 1: set()},
             "foreign": {0: False, 1: False}, "lay": {0: None, 1: None}, "replan_cells": {0: None, 1: None}}
    track = foreign_attack_from is not None or replan

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
        if replan:
            # v20: re-plan the layout around buildings this bot never requested (docstring)
            cur = state["lay"][me_i] if state["lay"][me_i] is not None else base_lay
            alien = sorted((b["x"], b["y"]) for b in me["buildings"] if (b["x"], b["y"]) not in state["req"][me_i])
            if replan_base and replan_gain is not None:
                # v23: compare with the base layout, never with an earlier re-plan (docstring)
                if alien and alien != state["replan_cells"][me_i]:
                    state["lay"][me_i] = None
                    if R.needs_replan(me["buildings"], base_lay):
                        new = R.replan_layout(me["buildings"], iters=replan_iters, seed=rnd)
                        if _s_final(me["buildings"], new) - _s_final(me["buildings"], base_lay) >= replan_gain:
                            state["lay"][me_i] = new
                    state["replan_cells"][me_i] = alien
            elif alien and alien != state["replan_cells"][me_i] and R.needs_replan(me["buildings"], cur):
                new = R.replan_layout(me["buildings"], iters=replan_iters, seed=rnd)
                # v21: adopt only with a large enough score gain (docstring)
                if replan_gain is None or _s_final(me["buildings"], new) - _s_final(me["buildings"], cur) >= replan_gain:
                    state["lay"][me_i] = new
                state["replan_cells"][me_i] = alien
        lay = state["lay"][me_i] if state["lay"][me_i] is not None else base_lay
        if own_in_layout:
            # v24: own requested buildings never make the map foreign for v15 (docstring)
            req = state["req"][me_i]
            extra = {c: 0 for c in ((b["x"], b["y"]) for b in me["buildings"])
                     if c in req and c not in lay.final_adj}
            if extra:
                lay = dataclasses.replace(lay, final_adj={**lay.final_adj, **extra})
        if foreign_attack_from is not None and not state["foreign"][me_i]:
            req = state["req"][me_i]
            if any((b["x"], b["y"]) not in req for b in me["buildings"]):
                state["foreign"][me_i] = True
        hold = (foreign_attack_from is not None and state["foreign"][me_i]
                and rnd < foreign_attack_from
                and (foreign_open or state["opp_turrets"][me_i]))
        def income(p):
            return g["factory_income"] * p["n_factories"] + g["path_income_per_step"] * p["length_path"]

        if hold and hold_income is not None:
            hold = income(me) >= hold_income * income(op)
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

        def lock_reachable(o2):
            """True if plan_defense with unlimited gold reaches per-copy splash max_hp (docstring).

            Also True if the map already has per-copy splash max_hp (the planner then has
            nothing to add and returns no actions)."""
            if P.splash_damage(o2["players"][me_i]["buildings"], grules) >= max_hp:
                return True
            big = 10 ** 7
            o = _with(o2, [], big)
            return any(P.plan_defense(o, big, required_hp=max_hp, layout=L, partial="none", time_budget=plan_time)
                       for L in (lay, free))

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
            # 5. saturation (v19: only while the lock is reachable, if sat_reach)
            if (rnd >= (late_round if sat_from is None else sat_from) and left > 0
                    and not (foreign_sat_from is not None and state["foreign"][me_i] and rnd < foreign_sat_from)
                    and (not sat_reach or lock_reachable(o2))):
                add(defend(o2, int(left * sat_frac), "best", required_hp=sat_target))
                o2 = _with(obs, actions, left)

        # doom attack (v18)
        if doom and not attacked and rnd >= attack_from and left >= rules["minions"]["tier1"]["cost"]:
            comps = P.threat_compositions(obs)
            fire = bool(comps) and _worst_damage(o2, comps) >= me["hp"]
            if not fire and doom == "next" and rnd < max_rounds:
                # next round: opponent gold plus its income; fire unless a layout-free plan with
                # our gold plus our income would then hold the base
                comps_n = P.threat_compositions(obs, extra_gold=op["gold"] + income(op))
                if comps_n and _worst_damage(o2, comps_n) >= me["hp"]:
                    g_n = left + income(me)
                    o_n = _with(o2, [], g_n)
                    acts_n = free_plan(o_n, g_n, comps_n, partial="best")
                    after = _with(o_n, acts_n, g_n - _cost(acts_n, rules))
                    fire = _worst_damage(after, comps_n) >= me["hp"]
            if fire:
                my_active = active_types(me["roster"], rnd)
                room = min(min_cap, active_cap - len(my_active))
                if room > 0:
                    res, _ = search(_tuples(op["buildings"]), my_active, left, rules,
                                    opp_gold=op["gold"], cap=room, responded=False,
                                    active_cap=len(my_active) + room, my_gold=me["gold"])
                    if res:
                        pkg = max(res, key=lambda r: (r[2], -r[1]))[0]
                        add([{"op": "buy_minion", "type": t} for t in pkg])
                        attacked = True

        # 6. attack
        if not attacked:
            frac = none_frac if (open_case and none_frac is not None) else (
                early_attack_frac if early else attack_frac)
            attack(frac)

        # 7. factories
        if rnd <= factory_stop and rnd < max_rounds - 1:
            n = max(0, min(fac_cap, left // fcost))
            add([{"op": "buy_factory"}] * n)
        if track:
            state["req"][me_i].update((a["x"], a["y"]) for a in actions
                                      if a["op"] in ("build_wall", "build_turret"))
        return actions

    return decide
