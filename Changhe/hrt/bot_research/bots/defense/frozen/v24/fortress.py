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
attack_share (0.7), attack_tier ("tier5"), min_leak_per_gold (0.1), walls (True),
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
history_factor (1.0), history_share (1.0), history_min_spend (100: a past round counts only if the opponent spent at
least this much on minions in it; below that the poke-insurance fallback is the relevant cover).
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


def make(spec_share=0.6, attack="opportunistic", attack_from=3, attack_share=0.7, attack_tier="tier5",
         min_leak_per_gold=0.1, walls=True, layout="default", poke_insurance=True, round1=None, lethal_share=0.4,
         round1_poke=2, big_threat=None, robust_attack=False, survive_kill=False, growth_gap=None,
         insure_levels=(70,), history_insurance=True, history_factor=1.0, history_share=1.0, history_min_spend=100):
    layout = P.layout_by_name(layout) if isinstance(layout, str) or layout is None else layout
    hist = {"max_spend": 0}      # per side per match (make() is called once per side); own observations only

    def decide(obs):
        me = obs["players"][obs["player"]]
        rules = gk.Rules.from_observation(obs)
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
            kill = None
            for t in TIER_ORDER:
                c = rules.minions[t]["cost"]
                n = min(MAX_MINIONS_PER_ROUND, left // c)
                if n <= 0:
                    continue
                h, d = P.opponent_leak(obs, [t] * n)
                if d >= opp_hp and (kill is None or n * c < kill[0]):
                    kill = (n * c, t, n)
            if kill is not None:
                safe = (not comps) or P.threat_damage(o2, comps) < me["hp"]
                if not safe and comps:
                    # would the best affordable defence save me anyway? if not, the kill is still the
                    # better move (draw at worst instead of a loss)
                    d_acts = P.plan_defense(o2, left, threat_types=comps, layout=layout, partial="best")
                    o3 = _with_buildings(obs, actions + d_acts, 0)
                    safe = P.threat_damage(o3, comps) >= me["hp"]
                if safe:
                    actions += [{"op": "buy_minion", "type": kill[1]}] * kill[2]
                    left -= kill[0]
                    n_f = min(MAX_FACTORIES_PER_ROUND, left // rules.factory_cost)
                    actions += [{"op": "buy_factory"}] * max(0, n_f)
                    return actions
        # 1. mandatory defence against the visible roster
        if visible:
            d = P.plan_defense(o2, left, threat_types=[visible], layout=layout, partial="best")
            actions += d
            left -= _cost_of(d, rules)
            o2 = _with_buildings(obs, actions, left)
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
        if comps and (lethal_share is not None or big_threat is not None):
            worst = P.threat_damage(o2, comps)
            if (lethal_share is not None and worst >= lethal_share * me["hp"]) or (big_threat is not None and worst >= big_threat):
                share, mode = 1.0, "best"
        if final_round and comps:
            share, mode = 1.0, "best"      # gold has no value after round 50: defend the HP lead first
        covered_full = not comps
        if comps and left > 0:
            spec = P.plan_defense(o2, int(left * share), threat_types=comps, layout=layout, partial=mode)
            covered_full = bool(spec) or mode == "best"
            if not spec and poke_insurance:
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
        if attack != "none" and rnd >= attack_from and left > 0 and not dying:
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
                finish = None
                for t in TIER_ORDER:
                    c = rules.minions[t]["cost"]
                    n = min(MAX_MINIONS_PER_ROUND, left // c)
                    if n <= 0:
                        continue
                    h, d = P.opponent_leak(obs, [t] * n)
                    if d >= opp_hp and (finish is None or n * c < finish[0]):
                        finish = (n * c, t, n)
                if finish is not None:
                    bought = [finish[1]] * finish[2]
                else:
                    for t in TIER_ORDER:
                        c = rules.minions[t]["cost"]
                        n = min(MAX_MINIONS_PER_ROUND, budget // c)
                        if n <= 0:
                            continue
                        h, d = P.opponent_leak(obs, [t] * n)
                        gain = (d - base_dmg) / (n * c)
                        if gain >= min_leak_per_gold and (best is None or gain > best[0]):
                            best = (gain, t, n)
                    opp_turrets = sum(1 for b in obs["players"][1 - obs["player"]]["buildings"] if b["type"] != "wall")
                    frac = 1.0
                    if isinstance(robust_attack, (int, float)) and not isinstance(robust_attack, bool):
                        frac = float(robust_attack)
                    use_robust = robust_attack is True or (robust_attack == "adaptive" and opp_turrets > 0) or (0 < frac < 1.0 and not isinstance(robust_attack, (bool, str)))
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
                            if gain >= min_leak_per_gold and (best is None or gain > best[0]):
                                best = (gain, t, n)
                    if best is not None:
                        _, t, n = best
                        bought = [t] * n
            actions += [{"op": "buy_minion", "type": t} for t in bought]
            left -= _cost_of([{"op": "buy_minion", "type": t} for t in bought], rules)
        # 5. factories
        n_f = min(MAX_FACTORIES_PER_ROUND, left // rules.factory_cost)
        actions += [{"op": "buy_factory"}] * max(0, n_f)
        return actions

    return decide


def decide(obs):
    """Module-level default (stateless) for the plain module:function form."""
    return make()(obs)
