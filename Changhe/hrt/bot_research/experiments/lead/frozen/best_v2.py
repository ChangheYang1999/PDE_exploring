"""Lead candidate bot ("planner"), entry point ``decide``.

Decision rules (one call per round, using only the observation):

1. Maze. A fixed template of 33 wall cells (four horizontal barriers with
   alternating gaps plus a vertical snake in the bottom rows, minus 26 reserved
   splash slots) is built as soon as affordable. With every slot empty the
   route has length 46; with every slot filled it has length 78.
2. Defense. Per-copy splash damage S (sum over route indices of adjacent splash
   damage) kills every copy whose HP is at most S, for any number of copies.
   Splashes are added only on reserved slots, in greedy order of marginal S
   (route length breaks ties). The number k of new splashes this round
   minimises  cost(k) + kappa * expected_damage(S_k), where expected damage is
   the known threat (the opponent's roster entries active this round that can
   arrive, with HP > S, counted for up to ``h_known`` rounds of their remaining
   life) plus p_attack times the worst one-round damage the opponent can buy
   with its visible gold against S. kappa is scaled by max(1, income/income_ref).
3. Attack. Our purchases are simulated exactly against the opponent's current
   buildings (gamekit.simulate_defense). A type is bought only if its HP exceeds
   the opponent's current S plus the S increase its visible gold could buy this
   round on the best free cells beside its route (``response`` scales that
   allowance). Among types and counts (n_max, n_max/2, n_max/4, n_max/8) the
   one maximising damage * kappa_attack - cost is bought if positive.
4. Economy. Remaining gold buys factories (at most ``max_factories`` per round)
   until ``last_factory_round``; in the final round all gold goes to attack.

Use ``bot_research.bots.best:decide`` (keys state by player) or the factory
form ``bot_research.bots.best:@make?kappa=4`` for parameter variants.
"""
from __future__ import annotations

from bot_research.harness import gamekit as gk

TIERS = ("tier1", "tier2", "tier3", "tier4", "tier5")

_BARRIERS = [[(x, y) for x in range(12) if x != gap] for y, gap in ((1, 11), (3, 0), (5, 11), (7, 0))]
_SNAKE = []
for _i, _x in enumerate(range(1, 11, 2)):
    _SNAKE += [(_x, _y) for _y in ((9, 10, 11) if _i % 2 == 0 else (8, 9, 10))]
# Reserved splash slots: interior cells of the first two barriers and six snake cells.
SLOTS = tuple([(x, 1) for x in range(1, 11)] + [(x, 3) for x in range(1, 11)]
              + [(5, 9), (3, 10), (7, 10), (3, 9), (7, 9), (5, 10)])
_slot_set = set(SLOTS)
WALLS = tuple(c for c in [c for b in _BARRIERS for c in b] + _SNAKE if c not in _slot_set)

DEFAULTS = dict(
    kappa=4.0,             # gold per HP for defensive spending (scaled by income / income_ref)
    kappa_attack=4.0,      # gold per HP for attack spending (scaled likewise)
    income_ref=100.0,      # income at which kappa applies unscaled
    h_known=4,             # rounds of damage counted for known (already bought) threats
    p_attack_min=0.5,      # minimum assumed probability that the opponent attacks
    response=1.0,          # multiplier on the opponent's best same-round splash response
    max_factories=80,
    max_minions=200,
    last_factory_round=46,
    attack_from_round=1,
)


def _active_entries(roster, round_number):
    return [e for e in roster if e["bought_round"] <= round_number
            and (e.get("expires_after_round") is None or round_number <= e["expires_after_round"])]


class Planner:
    def __init__(self, **params):
        unknown = set(params) - set(DEFAULTS)
        if unknown:
            raise ValueError(f"unknown parameters {sorted(unknown)}")
        self.p = {**DEFAULTS, **params}

    # ----- helpers -------------------------------------------------------
    def _splash_sequence(self, buildings, blocked, rules, gold):
        """Greedy order of slot splashes from the current state: list of (cell, S, L)."""
        cost = rules.turrets["splash"]["cost"]
        seq = []
        b = list(buildings)
        bl = set(blocked)
        free = [c for c in SLOTS if c not in bl]
        while free and (len(seq) + 1) * cost <= gold:
            best = None
            for c in free:
                if not gk.legal_build(bl, c):
                    continue
                trial = b + [{"x": c[0], "y": c[1], "type": "splash"}]
                path = gk.route_cached(bl | {c})
                s = gk.splash_total(path, trial, rules)
                key = (s, len(path))
                if best is None or key > best[0]:
                    best = (key, c, s, len(path) - 1)
            if best is None:
                break
            _, c, s, L = best
            seq.append((c, s, L))
            b.append({"x": c[0], "y": c[1], "type": "splash"})
            bl.add(c)
            free.remove(c)
        return seq

    @staticmethod
    def _window_damage(entries, L, S, rules, r, horizon):
        """Damage over ``horizon`` rounds of known active entries (dense order) with HP > S that can arrive."""
        ticks = rules.ticks
        dmg = 0
        for k, e in enumerate(entries):
            t = e["type"]
            if k % ticks + L <= ticks - 1 and rules.minions[t]["hp"] > S:
                exp = e.get("expires_after_round")
                rounds = horizon if exp is None else max(1, min(horizon, exp - r + 1))
                dmg += rules.minions[t]["damage"] * rounds
        return dmg

    def _potential_damage(self, n_known, gold, L, S, rules):
        best = 0
        ticks = rules.ticks
        for t in TIERS:
            m = rules.minions[t]
            if m["hp"] <= S or m["cost"] > gold:
                continue
            n = gold // m["cost"]
            # count copies whose dense index lands in the arrival window
            hits = sum(1 for j in range(min(n, 2 * ticks)) if (n_known + j) % ticks + L <= ticks - 1)
            best = max(best, hits * m["damage"])
        return best

    # ----- main ----------------------------------------------------------
    def __call__(self, obs):
        p = self.p
        rules = gk.Rules.from_observation(obs)
        r = obs["round"]
        me = obs["players"][obs["player"]]
        opp = obs["players"][1 - obs["player"]]
        gold = me["gold"]
        buildings = list(me["buildings"])
        blocked = gk.cells_of(buildings)
        actions = []

        # 1. template walls
        for c in WALLS:
            if gold < rules.wall_cost:
                break
            if gk.legal_build(blocked, c):
                actions.append({"op": "build_wall", "x": c[0], "y": c[1]})
                buildings.append({"x": c[0], "y": c[1], "type": "wall"})
                blocked.add(c)
                gold -= rules.wall_cost

        # 2. defense
        path = gk.route_cached(blocked)
        L = len(path) - 1
        S = gk.splash_total(path, buildings, rules)
        known = _active_entries(opp["roster"], r)
        opp_new_attack = sum(1 for e in opp["roster"] if e["bought_round"] == r - 1)
        p_attack = max(p["p_attack_min"], 1.0 if opp_new_attack else 0.0)
        cost = rules.turrets["splash"]["cost"]
        income = L + rules.factory_income * me["n_factories"]
        scale = max(1.0, income / p["income_ref"])
        kappa = p["kappa"] * scale
        max_hp = max(m["hp"] for m in rules.minions.values())
        seq = self._splash_sequence(buildings, blocked, rules, gold) if S < max_hp else []
        options = [(0, S, L)] + [(i + 1, s, l) for i, (_, s, l) in enumerate(seq)]
        best = None
        for k, s, l in options:
            exp = self._window_damage(known, l, s, rules, r, p["h_known"]) + p_attack * self._potential_damage(
                len(known), opp["gold"], l, s, rules)
            score = k * cost + kappa * exp
            if best is None or score < best[0] - 1e-9:
                best = (score, k)
        k = best[1]
        for c, _, _ in seq[:k]:
            actions.append({"op": "build_turret", "type": "splash", "x": c[0], "y": c[1]})
            buildings.append({"x": c[0], "y": c[1], "type": "splash"})
            blocked.add(c)
            gold -= cost

        # 3. attack
        final_round = r >= rules.max_rounds
        if r >= p["attack_from_round"]:
            spent, more = self._attack(obs, rules, gold, final_round, p["kappa_attack"] * scale)
            actions += more
            gold -= spent

        # 4. economy
        if r <= p["last_factory_round"]:
            n = min(p["max_factories"], gold // rules.factory_cost)
            actions += [{"op": "buy_factory"}] * n
        return actions

    @staticmethod
    def _response_bound(opath, ob, gold, rules):
        """Per-copy splash increase from the opponent's best same-round splashes on free cells
        beside its current route (top adjacency counts; route changes ignored)."""
        n = gold // rules.turrets["splash"]["cost"]
        if n <= 0:
            return 0
        blocked = gk.cells_of(ob)
        on_route = set(opath[:-1])
        full = set(opath)
        counts = []
        for x in range(gk.W):
            for y in range(gk.H):
                c = (x, y)
                if c in blocked or c in full or c in (gk.SPAWN, gk.BASE):
                    continue
                a = sum(1 for nb in gk.neighbors8(c) if nb in on_route)
                if a:
                    counts.append(a)
        counts.sort(reverse=True)
        return rules.turrets["splash"]["damage"] * sum(counts[:n])

    def _attack(self, obs, rules, gold, final_round, kappa):
        p = self.p
        me = obs["players"][obs["player"]]
        opp = obs["players"][1 - obs["player"]]
        r = obs["round"]
        ob = list(opp["buildings"])
        opath = gk.route_cached(gk.cells_of(ob))
        oS = gk.splash_total(opath, ob, rules)
        o_resp = 0 if final_round else p["response"] * self._response_bound(opath, ob, opp["gold"], rules)
        mine = [e["type"] for e in _active_entries(me["roster"], r)]
        profile = gk.splash_profile(opath, ob, rules)
        guns = gk.gun_coverage(opath, ob, rules)
        base = gk.simulate_defense(mine, opath, ob, rules, profile=profile, guns=guns).damage if mine else 0
        best = None
        for t in TIERS:
            m = rules.minions[t]
            if m["cost"] > gold or m["hp"] <= oS + o_resp:
                continue
            n_max = min(p["max_minions"], gold // m["cost"])
            for n in sorted({n_max, max(1, n_max // 2), max(1, n_max // 4), max(1, n_max // 8)}):
                res = gk.simulate_defense(mine + [t] * n, opath, ob, rules, profile=profile, guns=guns)
                gain = res.damage - base
                if gain <= 0:
                    continue
                value = gain * kappa - n * m["cost"]
                if final_round:
                    value = gain
                if best is None or value > best[0]:
                    best = (value, t, n, gain)
        if best is None or best[0] <= 0:
            return 0, []
        value, t, n, gain = best
        return n * rules.minions[t]["cost"], [{"op": "buy_minion", "type": t}] * n


def make(**params):
    """Factory: a fresh planner (separate state per side)."""
    return Planner(**params)


_instances: dict = {}


def decide(observation):
    """Entry point required by the runner; one planner per player index."""
    key = observation["player"]
    if key not in _instances:
        _instances[key] = Planner()
    return _instances[key](observation)
