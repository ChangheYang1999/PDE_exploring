"""Fortress: defence-first research bot built on plan_defense (lane hrt-w1).

Spec: ``bot_research.bots.defense.fortress:@make?spec_share=0.6&attack="opportunistic"``

Policy each round (all planning from the observation only):
  0. Layout walls (stage A, 1 gold each) first; all plans below are made on the resulting route.
  1. Mandatory defence: zero simulated leaks against the opponent's VISIBLE active roster (it will
     attack this round for certain). Partial plans allowed if zero leaks are unaffordable.
  2. Speculative defence: zero leaks against every purchase bundle the opponent's visible gold allows
     this round, but only if such a plan costs <= spec_share * remaining gold (never a partial plan:
     a defence that still leaks a tier5 is wasted gold better compounded).
  3. Layout walls for route income (stage A, 1 gold each; the route grows to 44).
  4. Attack (attack="opportunistic", from round attack_from): if minions of some tier would leak
     base damage on the opponent's CURRENT map (exact simulation of my roster + purchase), buy the
     tier with the best leaked damage per gold using attack_share of the remaining gold. Finish rule
     (checked before the defence steps, never in the last two rounds): if all remaining gold on one tier
     would reduce the opponent to <= 0 HP this round on its current map and either the worst affordable
     threat cannot kill me this round or no affordable defence found would prevent that anyway, buy the kill.
     The kill ignores the opponent's same-round construction, so this is a heuristic, not a guarantee.
     attack="none": pure turtle. attack="flood": from attack_from, all remaining gold on attack_tier.
  5. Factories with the rest (capped per round: unbounded factory lists make multi-GB logs).

Parameters (JSON in the spec): spec_share (0.6), attack ("opportunistic"), attack_from (3),
attack_share (0.25 since v33, 0.35 in v32, 0.7 in v3-v29: the smaller share keeps the economy against opponents that answer pokes, x99, x108), attack_tier ("tier5"), min_leak_per_gold (0.1), walls (True),
layout ("default" | "annealed25" | "pillars774" | "lead_v3", see plan.layout_by_name / templates.py),
poke_insurance (True: when the full speculative plan is unaffordable, still buy zero leaks against the
tier1/tier2 bundles the opponent can afford), round1 (None | "splash" | "gun2": blind round-1 turret at (10,1)),
lethal_share (0.4: if the worst affordable threat could deal >= this share of my HP on my current map, the
speculative step may use all remaining gold and accepts the strongest partial plan; None disables),
round1_poke (2: number of tier1 bought blind in round 1, 15 gold each; 0 disables),
big_threat (None: absolute damage threshold; if the worst affordable threat could deal >= this on my current
map, the speculative step spends all gold and accepts a partial plan; the lead's screen suggests 100),
insure_levels ((70,): HP levels for the graded insurance fallback when the full speculative plan is
unaffordable: zero leaks against all affordable bundles whose copies have HP <= level, highest level first;
e.g. (560, 180, 70) also insures against single tier4/tier3 drips),
growth_gap (None: if set, from round 5 on a turret-less opponent owning >= growth_gap x my factories switches the
speculative step to the full budget with partial plans, to prepare for its flood),
survive_kill (False: if True and my existing roster alone kills the opponent this round on its current map, buy
no attack and spend all gold on defence, partial plans allowed),
robust_attack (False default; True: an opportunistic purchase is made only if it still leaks after the opponent's
best same-round response, estimated by running plan_defense for the opponent with all its visible gold;
"adaptive": the same, but only against opponents that already own at least one turret; a number f in (0,1): the
opponent is assumed to answer with fraction f of its gold),
history_insurance (True default since v23; False disables: the bot remembers the largest attack purchase the opponent made in any
single past round, read exactly from the bought_round fields of its visible roster, and when the full speculative
plan was unaffordable it still buys zero leaks against the visible roster plus one more round of purchases of
up to history_factor x that spend, using up to history_share of the remaining gold; a learned spending model
against drips: one hidden tier4 every second round beats the visible-roster defence by one copy each time),
history_factor (2.0 since v25; 1.0 in v24: econ17 escalates its drip from one to two tier4, x65), history_share (1.0), history_min_spend (100: a past round counts only if the opponent spent at
least this much on minions in it; below that the poke-insurance fallback is the relevant cover),
response_memory (False default; True in frozen v28 only, the forecast-robust alternative: after each attack step the bot stores the damage its roster plus purchase
would deal on the opponent's current map; if the opponent's HP drop in that round was below response_ratio (0.5)
of a positive prediction, the opponent answered the attack with same-round construction, and for the next
response_rounds (8) rounds the attack uses the response-aware rule (robust_leak with the opponent's full gold);
afterwards the plain rule probes again. A learned response model against forecasters and reactive insurers that
does not veto pokes against opponents that never answer),
replan_foreign (True default since v25; at the first decision of the match, if the own map already holds buildings (a
scripted opening) with which the master layout can no longer reach S 1500 (replan.needs_replan), replan.replan_layout
designs a new layout around them (replan_iters annealing steps, about 1-4 s) and every later plan uses it; see replan.py;
replan_every (0 = off; 3 in frozen v31, no gain measured): on such maps, every replan_every rounds after a re-plan, if the own map changed and the current layout
can no longer reach S 1500, a re-plan with half the steps is adopted when it reaches at least 100 more exposure),
capacity_guns (True: when every reserved slot filled would still leave S < 1500, compute the exact kill thresholds
(smallest tier5 flood whose simulated damage reaches the HP) against my map and the opponent's and the rounds each
side needs to afford them at its current income; if the threshold against me is at least capacity_min_flood (8) copies
and the opponent would get there first (within one round of me), or the gold left after the 40-factory cap has no
use (surplus) while the opponent can already afford such a flood, buy the unbuilt slots as splashes and then gun3 on
free off-route cells by route coverage, up to max(capacity_share (0.5) of the remaining gold, the surplus) and 12
turrets per round; the capacity regime of scripted maps),
guard_insure (False default; True: from round guard_from (6), against an opponent that owns at least guard_turrets (2)
turrets, has bought no minion since round 2 and can afford a copy with more than 100 HP, buy a zero-leak plan against the
visible roster plus one copy of the heaviest tier it can afford, within guard_share (0.5) of the gold, when the full
speculative plan was not bought; aimed at the first hidden tier4 of drip opponents),
eco_match (True in frozen v35 (the anti-guard-growth alternative), False in v34 and before; True or "stopped": in rounds <= eco_match_until (7), ("stopped": only when the opponent's current map stops a 3-tier1 poke stream), while the opponent owns at least eco_match_ratio (1.5) x my
factories + 2 and has shown no heavy purchase, skip the speculative insurance (unless lethal) and the pokes and grow;
probe against the cheap-guard + growth + early-tier5 schedule, x121),
eco_match_pokes (False; True: economy matching skips only the speculative insurance and keeps the pokes, which the exact
leak-per-gold gate already removes against maps that kill them; x128 traces: the astra-33 loss is the gun spending, the
early-gun win is the pokes),
race_kill (False; True: when my map after this round's defence is zero-leak against the visible roster and survives the worst
affordable addition this round, the opponent has spent at least a tier5's cost in one round (a striker) and its current map does not stop a tier5,
and all my gold on tier5 now (hitting this round and the next) plus next round's income on tier5 kills it within two rounds
on its current map, buy the whole flood now instead of the attack share; aimed at strikers that lock one or two rounds
after their strike, x128; since the sixth review: the opponent must also have bought a copy of the heaviest tier (a flood of
44 tier1 set the flag before), the next-round estimate drops the roster entries that expire, and no race in the last two
rounds; the estimate still assumes the opponent builds nothing for two rounds and samples its affordable compositions),
poke_min_frac (None; a fraction f: an opportunistic purchase of n copies of a tier is accepted only if the exact simulation
lets at least f x n of them hit the base this round (marginal over the existing roster), in addition to the leak-per-gold
gate; with 0.7, pokes continue against bare maps and single gun1 maps (timing, early-gun grower: 7-10 of 10 tier1 arrive)
and stop against splash guards (0 of n) and against partially covered groups (2 of 5), x129/x132),
big_threat_prestrike (False; True: the big_threat test applies only while the opponent has made no heavy purchase yet
(history max_spend 0): insurance against the first strike of a passive grower at the round its gold affords it, and the normal
rules afterwards; x139: big_threat=280 alone turns the fortress into a turtle against strikers whose gold always affords two
more tier5, losing the H11 kills),
eco_match_insure_cap (0; a gold amount: while economy matching skips the speculative insurance, a FULL zero-leak plan against
the affordable compositions is still bought if it costs at most this cap (and spec_share of the gold); 200 = one gun3, which the
exact planner finds sufficient against a round-5 tier4 + two tier3 + two tier1 package on the fortress's early map; the graded
poke-insurance fallback stays off while matching),
covered_fix (False; True: when the speculative planner returns no plan, the coverage flag is computed from the exact leak of
the current map instead of being False, so a map that already covers every affordable composition is not insured again by the
history rule; bookkeeping defect found by the eighth review, no measured loss attributed to it),
factory_cap (40 = MAX_FACTORIES_PER_ROUND, the practical per-round factory limit of every research bot so far, not an engine
rule (RULES.md: no limit on the number of actions); a larger value (econ20, hrt-w2's V29: 400) lets the economy compound
longer. x182/x201 traces: on lockless scripted maps against econ20-based bots the fortress holds 430 factories and 16000
unspent gold at round 20 against the opponent's 3500 factories and is killed by a 300-tier5 flood in round 21; the only
remaining lever on a full map is the factory count).
finish_wrap (False; True: the finish rule also tries the roster-padding candidate of plan.wrap_bundles, cheap copies up to the next
multiple of 250 roster entries and then every affordable tier5, so that the new tier5 spawn at ticks 0.. alongside the respawning tier5
already on the roster; always with the opponent-response check; astra review 10 verified a round-18 kill of best_v9e on mirror:22:3
(224 tier1 + 19 tier5, 15,710 gold) that survives every legal same-round construction (3125 cases), where the plain floods of rounds 17-18
landed nothing),
finish_robust_gold (None; a gold amount: the finish rule's opponent-response check, otherwise applied only above 60 copies, also applies
to small floods while the opponent owns a turret and holds at least this much gold),
mass_finish (True: the finish rule searches flood sizes beyond 60 copies (geometric grid up to all gold) by exact
simulation; a flood above 60 copies is bought only if it still kills after the opponent's estimated full-gold response).
"""
from __future__ import annotations

from bot_research.harness import gamekit as gk

from . import plan as P

MAX_FACTORIES_PER_ROUND = 40
MAX_MINIONS_PER_ROUND = 60
TIER_ORDER = ["tier5", "tier4", "tier3", "tier2", "tier1"]


def _cost_of(actions, rules):
    total = 0
    for a in actions:
        if a["op"] == "build_wall":
            total += rules.wall_cost
        elif a["op"] == "build_turret":
            total += rules.turrets[a["type"]]["cost"]
        elif a["op"] == "buy_factory":
            total += rules.factory_cost
        elif a["op"] == "buy_minion":
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


def _heavy_tier(rules):
    return max(rules.minions, key=lambda k: rules.minions[k]["hp"])


def _race_kill(obs, left, me, rules, opp_hp):
    """All remaining gold on the heaviest tier now: does that roster, hitting this round and the next, plus next round's
    income (factories and own path length, exact rules) on the same tier, deal >= opp_hp on the opponent's CURRENT map
    (exact simulation, the opponent building nothing in two rounds)? Returns the purchase list or None."""
    heavy = _heavy_tier(rules)
    c = rules.minions[heavy]["cost"]
    n1 = min(MAX_MINIONS_PER_ROUND, left // c)
    if n1 <= 0:
        return None
    opp = obs["players"][1 - obs["player"]]
    opp_path = gk.route({(b["x"], b["y"]) for b in opp["buildings"]})
    if opp_path is None or rules.minions[heavy]["hp"] <= gk.splash_total(opp_path, opp["buildings"], rules):
        return None
    _, d1 = P.opponent_leak(obs, [heavy] * n1)
    if d1 <= 0:
        return None
    my_path = gk.route({(b["x"], b["y"]) for b in me["buildings"]})
    income = me["n_factories"] * rules.factory_income + ((len(my_path) - 1) if my_path else 0) * rules.path_income
    n2 = min(MAX_MINIONS_PER_ROUND, income // c)
    # next round: the roster entries that expire after this round are gone (astra review 6: the lifespan compacts the
    # spawn indices too, so the next-round roster is simulated from an observation advanced by one round)
    obs_next = dict(obs)
    obs_next["round"] = obs["round"] + 1
    _, d2 = P.opponent_leak(obs_next, [heavy] * (n1 + n2))
    if d1 + d2 >= opp_hp:
        return [heavy] * n1
    return None


def _find_kill(obs, left, opp_hp, rules, mass, layout, wrap=False, robust_gold=None):
    """Cheapest found (cost, ordered type list) whose exact simulation on the opponent's current map deals >= opp_hp
    (a sampled search over flood sizes, not a proof of minimality); n <= 60 unless mass is True, then n grows
    geometrically up to all the gold (the capacity regime: both maps below immunity, a flood of a few hundred copies
    is the only purchase that still changes the result), and a mass purchase must also survive the opponent's
    estimated same-round response (robust_leak with all its gold). Options: wrap (astra review 10, shift 4): the
    roster-padding candidate of plan.wrap_bundles (cheap copies up to the next multiple of 250 entries, then every
    affordable heavy copy: entry k spawns at tick k mod 250, so the new heavy wave spawns alongside the roster's
    respawning heavy copies instead of behind the padding), always with the response check; robust_gold (None, or a
    gold amount): the response check also applies to floods of at most 60 copies while the opponent owns a turret
    and holds at least that much gold (a rich defender answers a visible flood in the same round; x202a round 17)."""
    kill = None          # (cost, ordered type list)
    opp = obs["players"][1 - obs["player"]]
    opp_path = gk.route({(b["x"], b["y"]) for b in opp["buildings"]})
    s_opp = gk.splash_total(opp_path, opp["buildings"], rules) if opp_path else 0
    heavy = max(rules.minions, key=lambda k: rules.minions[k]["hp"])
    screen = sorted((k for k in rules.minions if k != heavy), key=lambda k: -rules.minions[k]["hp"])[0]
    opp_turrets = sum(1 for b in opp["buildings"] if b["type"] != "wall")
    small_robust = robust_gold is not None and opp_turrets > 0 and min(opp["gold"], 10 ** 9) >= robust_gold
    for t in TIER_ORDER:
        c = rules.minions[t]["cost"]
        n_max = left // c
        if n_max <= 0 or rules.minions[t]["hp"] <= s_opp:
            continue        # exact: a copy whose HP is at most the full-route splash exposure never arrives
        sizes = [min(MAX_MINIONS_PER_ROUND, n_max)]
        if mass and n_max > MAX_MINIONS_PER_ROUND:
            n = MAX_MINIONS_PER_ROUND
            while n < n_max:
                n = min(n_max, int(n * 1.3) + 1)
                sizes.append(n)
        for n in sizes:
            variants = [[t] * n]
            if mass and t == heavy:
                # a screen copy ahead of the flood makes the frontmost-target guns waste shots (astra reviews 4 and 5:
                # one tier4 then ten tier5 kills a map where eleven tier5 are needed, at a smaller cost); all sizes
                k = n - 1 if (n * c + rules.minions[screen]["cost"]) > left else n
                if k >= 1:
                    variants.append([screen] + [t] * k)
            for types in variants:
                cost = _cost_of([{"op": "buy_minion", "type": x} for x in types], rules)
                if cost > left or (kill is not None and cost >= kill[0]):
                    continue
                h, d = P.opponent_leak(obs, types)
                if d >= opp_hp:
                    if len(types) > MAX_MINIONS_PER_ROUND or small_robust:
                        h2, d2 = P.robust_leak(obs, types, layout=layout, fraction=1.0)
                        if d2 < opp_hp:
                            continue
                    kill = (cost, types)
            if kill is not None and kill[0] <= n * c:
                break
    if wrap and mass and rules.minions[heavy]["hp"] > s_opp:
        me = obs["players"][obs["player"]]
        base = gk.active_types(me["roster"], obs["round"])
        for types in P.wrap_bundles(left, len(base), rules, rules.ticks):
            if types[-1] != heavy:
                continue
            cost = _cost_of([{"op": "buy_minion", "type": x} for x in types], rules)
            if cost > left or (kill is not None and cost >= kill[0]):
                continue
            if P.opponent_leak(obs, types)[1] < opp_hp:
                continue
            if P.robust_leak(obs, types, layout=layout, fraction=1.0)[1] < opp_hp:
                continue
            kill = (cost, types)
    return kill


def _kill_threshold(path, buildings, rules, hp, n_max=2000):
    """Smallest n such that n tier5 copies deal >= hp on this map (exact simulation; None if n_max does not)."""
    types = rules.minions
    heavy = max(types, key=lambda t: types[t]["hp"])

    def kills(n):
        return gk.simulate_defense([heavy] * n, path, buildings, rules).damage >= hp
    if kills(1):
        return 1
    lo, hi = 1, None
    n = min(60, n_max)
    while True:
        if kills(n):
            hi = n
            break
        lo = n
        if n >= n_max:
            return None          # not even n_max copies kill
        n = min(n_max, int(n * 1.5) + 1)
    while hi - lo > 1:
        mid = (lo + hi) // 2
        if gk.simulate_defense([heavy] * mid, path, buildings, rules).damage >= hp:
            hi = mid
        else:
            lo = mid
    return hi


def make(spec_share=0.6, attack="opportunistic", attack_from=3, attack_share=0.25, attack_tier="tier5",
         min_leak_per_gold=0.1, walls=True, layout="default", poke_insurance=True, round1=None, lethal_share=0.3,
         round1_poke=2, big_threat=None, robust_attack=False, survive_kill=False, growth_gap=None,
         insure_levels=(70,), history_insurance=True, history_factor=2.0, history_share=1.0, history_min_spend=100,
         response_memory=False, response_rounds=8, response_ratio=0.5, replan_foreign=True, replan_iters=5000, replan_every=0,
         capacity_guns=True, capacity_share=0.5, capacity_min_flood=8, mass_finish=True,
         guard_insure=False, guard_from=6, guard_turrets=2, guard_share=0.5,
         eco_match=True, eco_match_until=7, eco_match_ratio=1.0, eco_match_pokes=False, race_kill=True,
         poke_min_frac=None, big_threat_prestrike=False, eco_match_insure_cap=200, covered_fix=True,
         factory_cap=1200, finish_wrap=True, finish_robust_gold=400):
    layout = P.layout_by_name(layout) if isinstance(layout, str) or layout is None else layout
    hist = {"max_spend": 0, "heavy_cost": 0, "pred": None, "robust_until": 0, "layout": None, "replan_cells": None,
            "own_cells": set()}   # per side per match; own observations and own requested builds only
    layout0 = layout

    def _record(actions):
        for a in actions:
            if a["op"] in ("build_wall", "build_turret"):
                hist["own_cells"].add((a["x"], a["y"]))
        return actions

    def decide(obs):
        nonlocal layout
        me = obs["players"][obs["player"]]
        rules = gk.Rules.from_observation(obs)
        if replan_foreign:
            # foreign map (scripted opening): whenever the own map holds buildings outside the current layout
            # (only a scripted opening can add those; the bot itself builds layout cells only) and the current
            # layout can no longer reach S 1500, design a new layout around all existing buildings. Scripted
            # rounds may be observed one by one (the harness calls the bot and discards its actions), so the
            # check is repeated and the layout re-planned when more foreign buildings arrive.
            from . import replan as R
            cur_layout = hist["layout"] if hist["layout"] is not None else layout0
            own_cells = {(b["x"], b["y"]) for b in me["buildings"]}
            # foreign = on my map but never requested by me (scripted openings); layout membership is irrelevant,
            # a scripted wall on a layout cell changes the completion too (astra review 5)
            foreign_cells = sorted(c for c in own_cells if c not in hist["own_cells"])
            if foreign_cells and foreign_cells != hist.get("replan_cells") and R.needs_replan(me["buildings"], cur_layout):
                hist["layout"] = R.replan_layout(me["buildings"], iters=replan_iters, seed=obs["round"])
                hist["replan_cells"] = foreign_cells
                hist["replan_round"] = obs["round"]
            elif (hist["layout"] is not None and replan_every and obs["round"] >= hist.get("replan_round", 0) + replan_every
                  and own_cells != hist.get("replan_map") and R.needs_replan(me["buildings"], cur_layout)):
                # the map has changed since the last re-plan (guns on slots, off-layout splashes) and the current
                # layout can no longer reach S 1500: re-plan with the real map and adopt the result only if it
                # reaches clearly more exposure than the current layout still can (v27 did this by accident, through
                # its own guns counting as foreign cells, and won games that v29 lost; x89 trace)
                cand = R.replan_layout(me["buildings"], iters=max(1000, replan_iters // 2), seed=obs["round"])
                my_blocked0 = {(b["x"], b["y"]) for b in me["buildings"]}
                s_cur = 10 * P.reserved_capacity(me["buildings"], my_blocked0, cur_layout)
                s_new = 10 * P.reserved_capacity(me["buildings"], my_blocked0, cand)
                hist["replan_round"] = obs["round"]
                hist["replan_map"] = set(own_cells)
                if s_new >= s_cur + 100:
                    hist["layout"] = cand
            layout = hist["layout"] if hist["layout"] is not None else layout0
        gold = min(me["gold"], 10 ** 9)      # guard: absurd gold must not overflow float products
        rnd = obs["round"]
        actions = []
        left = gold
        # 0. layout walls first (1 gold each); every defence plan below is made on the resulting route,
        #    so walls can never silently remove splash exposure (bug found by the astra review).
        if walls and left > 0:
            w = P.plan_walls(obs, left, layout=layout, stage=0)
            actions += w
            left -= _cost_of(w, rules)
        o2 = _with_buildings(obs, actions, left)
        visible = P.active_opponent_types(obs)
        comps = P.threat_compositions(obs)
        final_round = rnd >= rules.max_rounds
        opp_gold = min(obs["players"][1 - obs["player"]]["gold"], 10 ** 9)
        opp_hp_now = obs["players"][1 - obs["player"]]["hp"]
        if response_memory and hist["pred"] is not None and hist["pred"][0] == rnd - 1:
            # did last round's attack land as predicted on the opponent's then-current map? if the opponent's
            # same-round construction removed most of it, it answers attacks: assume a full answer for a while
            _, pred_dmg, hp_before = hist["pred"]
            if pred_dmg > 0 and (hp_before - opp_hp_now) < response_ratio * pred_dmg:
                hist["robust_until"] = rnd + response_rounds
        hist["pred"] = None
        if history_insurance:
            # the opponent's past per-round attack spend, exact from the visible roster (bought_round, type)
            spend = {}
            for e in obs["players"][1 - obs["player"]]["roster"]:
                if e.get("type") in rules.minions:
                    spend[e["bought_round"]] = spend.get(e["bought_round"], 0) + rules.minions[e["type"]]["cost"]
            # only rounds with a heavy attack purchase count (>= history_min_spend gold, default the tier3 cost):
            # cheap pokes are the poke-insurance fallback's business, and reacting to a round-1 poke with guns
            # instead of factories compounds into a lost economy (v23 regression, x53: -252 against lead v4)
            hist["max_spend"] = max([hist["max_spend"]] + [v for v in spend.values() if v >= history_min_spend])
            # the most expensive single copy the opponent has bought (a flood of cheap copies is not a heavy strike)
            hist["heavy_cost"] = max([hist["heavy_cost"]] + [rules.minions[e["type"]]["cost"]
                                                             for e in obs["players"][1 - obs["player"]]["roster"]
                                                             if e.get("type") in rules.minions])
        # 0a. survive-the-kill: if my existing roster alone already kills the opponent this round on its
        #     current map, buy no attack and put the whole gold into defence (a win instead of a both-destroyed
        #     draw when the opponent's wave would otherwise kill me in the same round)
        dying = False
        if survive_kill and attack != "none":
            h0, d0 = P.opponent_leak(obs, [])
            dying = d0 >= obs["players"][1 - obs["player"]]["hp"]
        late = rnd >= rules.max_rounds - 1      # no finish-first in the last two rounds (a failed kill cannot be repaired)
        # 0b. finish first: if all remaining gold on one tier kills the opponent this round on its current
        #     map and the worst affordable threat cannot kill me this round on my current map, buy the kill
        #     before any defence (defence would otherwise consume the budget; see t13 scenario draws).
        #     Not in the final round: the kill simulation ignores the opponent's same-round construction, and
        #     in round 50 a failed kill cannot be repaired (astra review 2).
        if attack != "none" and rnd >= attack_from and left > 0 and not late and not dying:
            opp_hp = obs["players"][1 - obs["player"]]["hp"]
            kill = _find_kill(obs, left, opp_hp, rules, mass_finish, layout, wrap=finish_wrap, robust_gold=finish_robust_gold)
            if kill is not None:
                safe = (not comps) or P.threat_damage(o2, comps) < me["hp"]
                if not safe and comps:
                    # would the best affordable defence save me anyway? if not, the kill is still the
                    # better move (draw at worst instead of a loss)
                    d_acts = P.plan_defense(o2, left, threat_types=comps, layout=layout, partial="best")
                    o3 = _with_buildings(obs, actions + d_acts, 0)
                    safe = P.threat_damage(o3, comps) >= me["hp"]
                if safe:
                    actions += [{"op": "buy_minion", "type": x} for x in kill[1]]
                    left -= kill[0]
                    n_f = min(factory_cap, left // rules.factory_cost)
                    actions += [{"op": "buy_factory"}] * max(0, n_f)
                    return _record(actions)
        # 1. mandatory defence against the visible roster
        if visible:
            d = P.plan_defense(o2, left, threat_types=[visible], layout=layout, partial="best")
            actions += d
            left -= _cost_of(d, rules)
            o2 = _with_buildings(obs, actions, left)
        # 1b. economy matching (option): while the opponent out-grows me (factories >= eco_match_ratio x mine + 2) and
        #     has shown no heavy purchase, in rounds <= eco_match_until, skip the speculative insurance and the pokes and
        #     put the gold into factories (the mandatory defence stays): the cheap-guard + growth + early-tier5 schedule
        #     (counter_astra33) wins through 34 factories against 18 at round 7
        matching = False
        if eco_match and rnd <= eco_match_until and hist["max_spend"] == 0:
            opp_f = obs["players"][1 - obs["player"]]["n_factories"]
            matching = opp_f >= eco_match_ratio * me["n_factories"] + 2
            if matching and eco_match == "stopped":
                # only against an opponent whose current map already stops a tier1 poke stream (the cheap guard):
                # against a grower whose map leaks, the pokes keep paying and the rule stays off
                matching = P.opponent_leak(obs, ["tier1"] * 3)[1] == 0
        # 2. speculative defence against affordable purchases, only if cheap enough; when the worst
        #    affordable threat could take lethal_share of my HP this round, the whole remaining gold may be
        #    used and a partial plan is accepted (survival before attack; prevents mutual destruction)
        share, mode = spec_share, "none"
        if dying and comps:
            share, mode = 1.0, "best"
        if growth_gap is not None and comps and rnd >= 5:
            opp_p = obs["players"][1 - obs["player"]]
            opp_turrets = sum(1 for b in opp_p["buildings"] if b["type"] != "wall")
            if opp_turrets == 0 and opp_p["n_factories"] >= growth_gap * max(1, me["n_factories"]):
                share, mode = 1.0, "best"      # a turret-less opponent out-growing me will flood: defend now
        bt = big_threat
        if bt is not None and big_threat_prestrike and hist["max_spend"] > 0:
            bt = None       # option: the big-threat insurance applies only until the opponent's first heavy purchase is seen
        if comps and (lethal_share is not None or bt is not None):
            worst = P.threat_damage(o2, comps)
            if (lethal_share is not None and worst >= lethal_share * me["hp"]) or (bt is not None and worst >= bt):
                share, mode = 1.0, "best"
        if final_round and comps:
            share, mode = 1.0, "best"      # gold has no value after round 50: defend the HP lead first
        covered_full = not comps
        cheap_only = matching and mode == "none" and eco_match_insure_cap > 0
        if comps and left > 0 and (not (matching and mode == "none") or cheap_only):
            # while matching, a full zero-leak plan is still bought if it is cheap (eco_match_insure_cap, e.g. one gun3):
            # the exact planner stops the timing bot's round-5 tier4 + two tier3 + two tier1 with one gun3 on this map
            budget = int(left * share) if not cheap_only else min(int(left * share), int(eco_match_insure_cap))
            spec = P.plan_defense(o2, budget, threat_types=comps, layout=layout, partial=mode)
            covered_full = bool(spec)
            if spec and mode == "best":
                # a partial plan counts as cover only if it actually reaches zero leaks (astra review 4)
                covered_full = P.threat_damage(_with_buildings(obs, actions + spec, 0), comps) == 0
            elif not spec and covered_fix:
                # option (astra review 8): plan_defense returns [] both when the map already covers every composition and
                # when no plan was found; the flag must come from the actual leak, or the history insurance runs needlessly
                covered_full = P.threat_damage(o2, comps) == 0
            if not spec and poke_insurance and not cheap_only:
                # graded fallback: zero leaks against the purchase bundles whose copies all have HP <= level,
                # for the levels in insure_levels (highest first), appended to the visible roster (the roster
                # itself is already covered by step 1); default (70,) = tier1/tier2 bundles only
                opp = obs["players"][1 - obs["player"]]
                bundles = P.affordable_bundles(min(opp["gold"], 10 ** 9), rules)
                for level in sorted(insure_levels, reverse=True):
                    cheap = [visible + b for b in bundles if b and all(rules.minions[t]["hp"] <= level for t in b)]
                    if cheap:
                        spec = P.plan_defense(o2, int(left * share), threat_types=cheap, layout=layout, partial="none")
                        if spec:
                            break
            if spec:
                actions += spec
                left -= _cost_of(spec, rules)
                o2 = _with_buildings(obs, actions, left)
            # 2h. history insurance: when the full speculative plan was not bought, insure against the visible
            #     roster plus one more round of purchases of the size the opponent has already shown
            if history_insurance and not covered_full and hist["max_spend"] > 0 and left > 0:
                cap = min(opp_gold, int(hist["max_spend"] * history_factor))
                comps_h = P.threat_compositions(obs, extra_gold=cap)
                if comps_h:
                    h_plan = P.plan_defense(o2, int(left * history_share), threat_types=comps_h, layout=layout, partial="none")
                    if h_plan:
                        actions += h_plan
                        left -= _cost_of(h_plan, rules)
                        o2 = _with_buildings(obs, actions, left)
        # 2g. guard insurance: an opponent that defends (owns turrets), has not bought a minion since round 2 and can
        #     afford a heavy copy is the drip profile (guard_continuation, astra's schedule, econ's round-7 tier4): insure
        #     the visible roster plus one copy of the heaviest tier it can afford (typically one gun3), within guard_share
        #     of the gold, when the full speculative plan was not bought; the first hidden heavy copy then does not land
        if guard_insure and not covered_full and rnd >= guard_from and comps and left > 0:
            opp_p = obs["players"][1 - obs["player"]]
            opp_turrets = sum(1 for b in opp_p["buildings"] if b["type"] != "wall")
            recent = any(e.get("bought_round", 0) > 2 for e in opp_p["roster"])
            heavy_aff = [t for t in TIER_ORDER if rules.minions[t]["cost"] <= opp_gold]
            if opp_turrets >= guard_turrets and not recent and heavy_aff and rules.minions[heavy_aff[0]]["hp"] > 100:
                g_plan = P.plan_defense(o2, int(left * guard_share), threat_types=[visible + [heavy_aff[0]]], layout=layout, partial="none")
                if g_plan:
                    actions += g_plan
                    left -= _cost_of(g_plan, rules)
                    o2 = _with_buildings(obs, actions, left)
        # 2c. capacity regime: the own map can no longer reach S 1500 (every reserved slot filled would still be
        #     below immunity) and the opponent could deal lethal damage this round: zero-leak plans do not exist
        #     and the planner's partial plans stall, so buy exposure and gun capacity directly: every unbuilt
        #     slot as a splash, then gun3 on the free cells with the largest route coverage (capacity bound:
        #     a flood of n copies leaks when n x (1500 - S) exceeds 250 x total gun damage per tick)
        if capacity_guns and comps and left >= rules.turrets["splash"]["cost"]:
            my_b = o2["players"][obs["player"]]["buildings"]
            my_blocked = {(b["x"], b["y"]) for b in my_b}
            cap_adj = P.reserved_capacity(my_b, my_blocked, layout)
            danger = False
            if 10 * cap_adj < rules.minions["tier5"]["hp"]:
                # the capacity race: exact kill thresholds (smallest tier5 flood whose simulated damage reaches the
                # HP) against my map and against the opponent's, and the rounds each side needs to afford them at
                # its current income; if the opponent gets there first (or within one round of me), raise my
                # threshold now: a gun3 raises the flood the opponent needs by thousands of gold for 200
                opp_p = obs["players"][1 - obs["player"]]
                path_me = gk.route(my_blocked)
                n_kill = _kill_threshold(path_me, my_b, rules, me["hp"])
                opp_blocked = {(b["x"], b["y"]) for b in opp_p["buildings"]}
                path_opp = gk.route(opp_blocked)
                n_kill_opp = _kill_threshold(path_opp, opp_p["buildings"], rules, opp_p["hp"])
                opp_income = max(1, opp_p["n_factories"] * rules.factory_income + (len(path_opp) - 1) * rules.path_income)
                my_income = max(1, me["n_factories"] * rules.factory_income + (len(path_me) - 1) * rules.path_income)
                heavy_cost = max(rules.minions.values(), key=lambda m: m["hp"])["cost"]
                surplus = 0
                if n_kill is not None and n_kill >= capacity_min_flood:
                    # only the genuine capacity regime (floods of dozens of copies); early small floods are the
                    # ordinary insurance problem, and buying guns against them drained the economy (x68)
                    r_opp = max(0.0, (heavy_cost * n_kill - opp_gold) / opp_income)
                    r_me = float("inf") if n_kill_opp is None else max(0.0, (heavy_cost * n_kill_opp - left) / my_income)
                    danger = r_opp <= r_me + 1.0
                    # gold the factory cap cannot absorb this round has no compounding value: in a capacity race it
                    # buys gun capacity (each gun3 raises the flood the opponent needs by several copies, i.e. by
                    # thousands of its gold, for 200), as long as the opponent could already afford a real flood
                    if opp_gold >= heavy_cost * capacity_min_flood:
                        surplus = left - factory_cap * rules.factory_cost
                        danger = danger or surplus > 0
            if danger:
                budget_c = max(int(left * capacity_share), surplus)
                bought_c = []
                path_c = gk.route(my_blocked)
                for c in layout.splash_cells:
                    if budget_c < rules.turrets["splash"]["cost"] or len(bought_c) >= 12:
                        break
                    if c not in my_blocked and gk.legal_build(my_blocked, c) and c not in set(path_c):
                        bought_c.append({"op": "build_turret", "type": "splash", "x": c[0], "y": c[1]})
                        my_blocked.add(c)
                        budget_c -= rules.turrets["splash"]["cost"]
                path_c = gk.route(my_blocked)
                att_c = set(path_c[:-1])
                g3 = rules.turrets["gun3"]
                free = [(x, y) for x in range(12) for y in range(12)
                        if (x, y) not in my_blocked and (x, y) not in att_c and (x, y) not in ((0, 0), (11, 11))]
                free.sort(key=lambda c: -sum((px - c[0]) ** 2 + (py - c[1]) ** 2 <= g3["range"] ** 2 for (px, py) in att_c))
                for c in free:
                    if budget_c < g3["cost"] or len(bought_c) >= 12:
                        break
                    cov = sum((px - c[0]) ** 2 + (py - c[1]) ** 2 <= g3["range"] ** 2 for (px, py) in att_c)
                    if cov < 1 or not gk.legal_build(my_blocked, c):
                        continue
                    if gk.route(my_blocked | {c}) != path_c:
                        continue          # keep the route (and its exposure) unchanged
                    bought_c.append({"op": "build_turret", "type": "gun3", "x": c[0], "y": c[1]})
                    my_blocked.add(c)
                    budget_c -= g3["cost"]
                if bought_c:
                    actions += bought_c
                    left -= _cost_of(bought_c, rules)
                    o2 = _with_buildings(obs, actions, left)
        # 2a. blind round-1 poke: tier1 copies bought before the opponent can have a turret
        if rnd == 1 and round1_poke:
            c1 = rules.minions["tier1"]["cost"]
            n = min(int(round1_poke), left // c1)
            actions += [{"op": "buy_minion", "type": "tier1"}] * n
            left -= n * c1
        # 2b. blind round-1 option
        if rnd == 1 and round1 and not any(a["op"] == "build_turret" for a in actions):
            cell = {"splash": (10, 1), "gun2": (10, 1)}[round1]
            kind = round1
            cost = rules.turrets[kind]["cost"]
            blocked_now = {(b["x"], b["y"]) for b in o2["players"][obs["player"]]["buildings"]}
            if left >= cost and gk.legal_build(blocked_now, cell):
                actions.append({"op": "build_turret", "type": kind, "x": cell[0], "y": cell[1]})
                left -= cost
                o2 = _with_buildings(obs, actions, left)
        # 4. attack
        if attack != "none" and rnd >= attack_from and left > 0 and not dying and not (matching and not eco_match_pokes):
            budget = int(left * attack_share)
            bought = []
            if attack == "flood":
                order = [attack_tier] + [t for t in TIER_ORDER if t != attack_tier]
                for t in order:
                    c = rules.minions[t]["cost"]
                    while budget >= c and len(bought) < MAX_MINIONS_PER_ROUND:
                        bought.append(t)
                        budget -= c
            else:
                best = None
                base_hits, base_dmg = P.opponent_leak(obs, [])
                opp_hp = obs["players"][1 - obs["player"]]["hp"]
                # finish rule: if all remaining gold on one tier kills the opponent this round on its
                # current map (exact simulation), buy that (the attack share limit does not apply)
                finish = _find_kill(obs, left, opp_hp, rules, mass_finish, layout, wrap=finish_wrap, robust_gold=finish_robust_gold)
                race = None
                if finish is None and race_kill and not late and left >= rules.minions[_heavy_tier(rules)]["cost"] \
                        and hist["max_spend"] >= rules.minions[_heavy_tier(rules)]["cost"] \
                        and hist["heavy_cost"] >= rules.minions[_heavy_tier(rules)]["cost"] \
                        and (not visible or P.threat_damage(o2, [visible]) == 0) \
                        and (not comps or P.threat_damage(o2, comps) < me["hp"]):
                    # two-round race (option): my map after this round's defence is zero-leak against the visible roster
                    # and I survive its worst affordable addition this round (x129: a striker's gold always affords two
                    # more tier5, so "covered against every addition" never held), the opponent is a striker (it has spent a tier5's cost in one round)
                    # and its current map cannot stop a tier5: if all my gold on tier5 now, hitting this round and the
                    # next, plus next round's income on tier5 kills it within two rounds on its current map, buy the
                    # whole flood now (x128: the guard-handoff locks one or two rounds after its strike, and the 25
                    # percent share leaves only one tier4 on the table; the gold has no defensive use on a locked map)
                    race = _race_kill(obs, left, me, rules, opp_hp)
                if finish is not None:
                    bought = list(finish[1])
                elif race is not None:
                    bought = race
                else:
                    for t in TIER_ORDER:
                        c = rules.minions[t]["cost"]
                        n = min(MAX_MINIONS_PER_ROUND, budget // c)
                        if n <= 0:
                            continue
                        h, d = P.opponent_leak(obs, [t] * n)
                        gain = (d - base_dmg) / (n * c)
                        if poke_min_frac is not None and (d - base_dmg) < poke_min_frac * n * rules.minions[t]["damage"]:
                            continue        # most of the copies must arrive (x129: group leaks of 10-30 percent are waste)
                        if gain >= min_leak_per_gold and (best is None or gain > best[0]):
                            best = (gain, t, n)
                    opp_turrets = sum(1 for b in obs["players"][1 - obs["player"]]["buildings"] if b["type"] != "wall")
                    frac = 1.0
                    if isinstance(robust_attack, (int, float)) and not isinstance(robust_attack, bool):
                        frac = float(robust_attack)
                    use_robust = robust_attack is True or (robust_attack == "adaptive" and opp_turrets > 0) or (0 < frac < 1.0 and not isinstance(robust_attack, (bool, str)))
                    if response_memory and rnd < hist["robust_until"]:
                        use_robust = True       # learned: this opponent answered our last predicted leak
                    if best is not None and use_robust:
                        # keep a purchase only if it still leaks after the opponent's best same-round response
                        # (a fraction of its visible gold spent through plan_defense on its own map; True = all);
                        # "adaptive" assumes a response only from opponents that already own turrets. The gain
                        # is measured consistently: responded leak with the purchase minus responded leak without.
                        _, rb_base = P.robust_leak(obs, [], layout=layout, fraction=frac)
                        best = None
                        for t in TIER_ORDER:
                            c = rules.minions[t]["cost"]
                            n = min(MAX_MINIONS_PER_ROUND, budget // c)
                            if n <= 0:
                                continue
                            h2, d2 = P.robust_leak(obs, [t] * n, layout=layout, fraction=frac)
                            gain = (d2 - rb_base) / (n * c)
                            if poke_min_frac is not None and (d2 - rb_base) < poke_min_frac * n * rules.minions[t]["damage"]:
                                continue
                            if gain >= min_leak_per_gold and (best is None or gain > best[0]):
                                best = (gain, t, n)
                    if best is not None:
                        _, t, n = best
                        bought = [t] * n
            actions += [{"op": "buy_minion", "type": t} for t in bought]
            left -= _cost_of([{"op": "buy_minion", "type": t} for t in bought], rules)
            if response_memory:
                hist["pred"] = (rnd, P.opponent_leak(obs, bought)[1], opp_hp_now)
        # 5. factories
        n_f = min(factory_cap, left // rules.factory_cost)
        actions += [{"op": "buy_factory"}] * max(0, n_f)
        return _record(actions)

    return decide


_PLAYERS: dict = {}


def decide(obs):
    """Module-level entry for the plain module:function form: one make() instance per player, renewed in round 1
    (so the history, the response memory and the re-planned layout persist through a match; astra review 4)."""
    key = obs["player"]
    if obs["round"] <= 1 or key not in _PLAYERS:
        _PLAYERS[key] = make()
    return _PLAYERS[key](obs)
