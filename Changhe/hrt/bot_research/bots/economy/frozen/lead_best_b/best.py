"""Lead candidate bot ("planner"), entry point ``decide``.

Decision rules (one call per round, using only the observation):

1. Maze. A fixed template of 33 wall cells (four horizontal barriers with
   alternating gaps plus a vertical snake in the bottom rows, minus 26 reserved
   splash slots) is built as soon as affordable. With every slot empty the
   route has length 46; with every slot filled it has length 78 and per-copy
   splash damage S is 1610 (1540 with 25 slots).
2. Defense. Per-copy splash damage S (sum over route indices of adjacent splash
   damage) kills every copy whose HP is at most S, for any number of copies.
   Splashes are added only on reserved slots, in greedy order of S (route
   length breaks ties). The number k of new splashes this round minimises
       lam * 60 * k + kappa * E(k),
   where E(k) is the expected base damage with the resulting S_k: the known
   threat (the opponent's active roster entries that can arrive, with HP > S_k)
   plus p_attack times the largest damage the opponent can buy with its
   visible gold against S_k. Each threat is counted for the number of rounds it
   would keep hitting if from next round on all our gold went into the same
   splash order (at least 1, at least ``h_known`` for known entries, at most the
   entry's remaining life). kappa = kappa0 * max(1, income / income_ref).
   Splashes are never wasted (all slots are needed for immunity against tier5
   by the final round), so lam < 1 prices only the delay of the purchase.
   A modelled damage total that reaches our HP adds a prohibitive penalty
   (times p_attack when it needs the unseen attack).
3. Attack. Our purchases are simulated exactly against the opponent's current
   buildings (gamekit.simulate_defense). A type is considered only if its HP
   exceeds the opponent's current S plus a heuristic estimate of the S its
   visible gold could add this round on the free cells beside its route
   (``response`` scales it; route changes are ignored, so it is not a bound).
   For types and counts (n_max, n_max/2, n_max/4, n_max/8) the value is
   damage * rounds * kappa_attack - cost, where rounds is the estimated number
   of rounds before the opponent can reach S >= HP. Defense and attack are
   chosen jointly: an attack is bought only if its value exceeds the increase
   of the best defense score caused by the gold it uses.
4. Economy. Remaining gold buys factories (at most ``max_factories`` per round)
   until ``last_factory_round``. In the final round gold has no later use, so
   splash cost and attack cost are not charged.

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
    lam=1.0,               # fraction of a splash's cost charged to buying it now
    h_known=4,             # minimum rounds of damage counted for known (already bought) threats
    p_attack_min=0.5,      # minimum assumed probability that the opponent attacks
    response=1.0,          # multiplier on the opponent's estimated same-round splash response
    persist=True,          # count attack damage for the rounds the opponent needs to block it
    max_factories=80,
    max_minions=200,
    last_factory_round=46,
    attack_from_round=1,
)


_LETHAL = 1e9  # score penalty when the modelled damage reaches our HP


def _active_entries(roster, round_number):
    return [e for e in roster if e["bought_round"] <= round_number
            and (e.get("expires_after_round") is None or round_number <= e["expires_after_round"])]


def arrivals(n_before, n, L, ticks):
    """Exact number of dense indices k in [n_before, n_before + n) with k % ticks + L <= ticks - 1."""
    w = ticks - L
    if w <= 0 or n <= 0:
        return 0

    def upto(m):
        q, rem = divmod(m, ticks)
        return q * w + min(rem, w)
    return upto(n_before + n) - upto(n_before)


class Planner:
    def __init__(self, **params):
        unknown = set(params) - set(DEFAULTS)
        if unknown:
            raise ValueError(f"unknown parameters {sorted(unknown)}")
        self.p = {**DEFAULTS, **params}

    # ----- helpers -------------------------------------------------------
    @staticmethod
    def _splash_sequence(buildings, blocked, rules):
        """Greedy order of all free slot splashes from the current state: list of (cell, S, L)."""
        seq = []
        b = list(buildings)
        bl = set(blocked)
        free = [c for c in SLOTS if c not in bl]
        while free:
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
    def _response_estimate(opath, ob, gold, rules):
        """Heuristic S increase from the opponent spending ``gold`` on splashes on free cells
        beside its current route (largest adjacency counts first; route changes ignored)."""
        n = int(gold) // rules.turrets["splash"]["cost"]
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

    # ----- main ----------------------------------------------------------
    def __call__(self, obs):
        p = self.p
        rules = gk.Rules.from_observation(obs)
        r = obs["round"]
        me = obs["players"][obs["player"]]
        gold = me["gold"]
        buildings = list(me["buildings"])
        blocked = gk.cells_of(buildings)
        actions = []
        final_round = r >= rules.max_rounds

        # 1. template walls
        for c in WALLS:
            if gold < rules.wall_cost:
                break
            if gk.legal_build(blocked, c):
                actions.append({"op": "build_wall", "x": c[0], "y": c[1]})
                buildings.append({"x": c[0], "y": c[1], "type": "wall"})
                blocked.add(c)
                gold -= rules.wall_cost

        # 2. defense and attack, chosen jointly
        path = gk.route_cached(blocked)
        L = len(path) - 1
        S = gk.splash_total(path, buildings, rules)
        income = L + rules.factory_income * me["n_factories"]
        scale = max(1.0, income / p["income_ref"])
        seq, evaluate, kmax = self._defense_model(obs, rules, gold, buildings, blocked, S, L,
                                                  p["kappa"] * scale, final_round)
        base_score, k = min((evaluate(j, 0), j) for j in range(kmax + 1))
        attack = []
        if r >= p["attack_from_round"]:
            best = None
            for value, t, n, c in self._attack_options(obs, rules, gold, final_round, p["kappa_attack"] * scale):
                score, j = min((evaluate(j, c), j) for j in range(kmax + 1))
                net = value - (score - base_score)
                if net > 0 and (best is None or net > best[0]):
                    best = (net, j, t, n, c)
            if best is not None:
                _, k, t, n, c = best
                attack = [{"op": "buy_minion", "type": t}] * n
                gold -= c
        for c, _, _ in seq[:k]:
            actions.append({"op": "build_turret", "type": "splash", "x": c[0], "y": c[1]})
            gold -= rules.turrets["splash"]["cost"]
        actions += attack

        # 3. economy
        if r <= p["last_factory_round"]:
            n = min(p["max_factories"], gold // rules.factory_cost)
            actions += [{"op": "buy_factory"}] * n
        return actions

    def _defense_model(self, obs, rules, gold, buildings, blocked, S, L, kappa, final_round):
        """Greedy splash order, a scoring function evaluate(k, spent) for buying the first k
        splashes while ``spent`` more gold goes elsewhere this round, and the largest k."""
        p = self.p
        r = obs["round"]
        me = obs["players"][obs["player"]]
        opp = obs["players"][1 - obs["player"]]
        cost = rules.turrets["splash"]["cost"]
        max_hp = max(m["hp"] for m in rules.minions.values())
        seq = self._splash_sequence(buildings, blocked, rules) if S < max_hp else []
        levels = [S] + [s for _, s, _ in seq]
        lengths = [L] + [l for _, _, l in seq]
        known = _active_entries(opp["roster"], r)
        opp_new_attack = any(e["bought_round"] == r - 1 for e in opp["roster"])
        p_attack = max(p["p_attack_min"], 1.0 if opp_new_attack else 0.0)
        rounds_left = rules.max_rounds - r + 1
        ticks = rules.ticks
        F = me["n_factories"]
        hp_me = me["hp"]
        fcost, finc = rules.factory_cost, rules.factory_income
        lam = 0.0 if final_round else p["lam"]
        kmax = min(len(seq), gold // cost)

        # per k: known arriving threats grouped by (hp, damage, life), and the best new-attack threats
        known_k, pot_k = [], []
        for k in range(kmax + 1):
            s_k, l_k = levels[k], lengths[k]
            groups = {}
            for idx, e in enumerate(known):
                m = rules.minions[e["type"]]
                if m["hp"] <= s_k or idx % ticks + l_k > ticks - 1:
                    continue
                ex = e.get("expires_after_round")
                life = rounds_left if ex is None else min(rounds_left, ex - r + 1)
                key = (m["hp"], m["damage"], life)
                groups[key] = groups.get(key, 0) + 1
            known_k.append(groups)
            pots = []
            for t in TIERS:
                m = rules.minions[t]
                if m["hp"] <= s_k or m["cost"] > opp["gold"]:
                    continue
                hits = arrivals(len(known), opp["gold"] // m["cost"], l_k, ticks)
                if hits:
                    pots.append((m["hp"], hits * m["damage"]))
            pot_k.append(pots)

        def needed(h):
            for j, s in enumerate(levels):
                if s >= h:
                    return j
            return None

        def evaluate(k, spent):
            g = gold - cost * k - spent
            if g < 0:
                return float("inf")
            nf = min(p["max_factories"], g // fcost) if r <= p["last_factory_round"] else 0
            inc = lengths[k] + finc * (F + nf)
            g1 = inc + g - fcost * nf

            def rounds(h, life):
                j = needed(h)
                if j is None:
                    return life
                need = cost * (j - k)
                extra = 0 if need <= g1 else -(-(need - g1) // max(1, inc))
                return max(1, min(life, 1 + extra))

            known_total = sum(n * d * max(min(p["h_known"], life), rounds(h, life))
                              for (h, d, life), n in known_k[k].items())
            life = min(rules.lifespan, rounds_left)
            pot_total = max((d * rounds(h, life) for h, d in pot_k[k]), default=0)
            score = lam * cost * k + kappa * (known_total + p_attack * pot_total)
            if known_total >= hp_me:
                score += _LETHAL
            elif known_total + pot_total >= hp_me:
                score += _LETHAL * p_attack
            return score

        return seq, evaluate, kmax

    def _attack_options(self, obs, rules, gold, final_round, kappa):
        """Candidate purchases (value, type, count, cost), value = estimated damage * kappa - cost."""
        p = self.p
        me = obs["players"][obs["player"]]
        opp = obs["players"][1 - obs["player"]]
        r = obs["round"]
        ob = list(opp["buildings"])
        opath = gk.route_cached(gk.cells_of(ob))
        oS = gk.splash_total(opath, ob, rules)
        o_resp = 0 if final_round else p["response"] * self._response_estimate(opath, ob, opp["gold"], rules)
        o_inc = (len(opath) - 1) + rules.factory_income * opp["n_factories"]
        rounds_left = rules.max_rounds - r + 1
        mine = [e["type"] for e in _active_entries(me["roster"], r)]
        profile = gk.splash_profile(opath, ob, rules)
        guns = gk.gun_coverage(opath, ob, rules)
        base = gk.simulate_defense(mine, opath, ob, rules, profile=profile, guns=guns).damage if mine else 0
        out = []
        for t in TIERS:
            m = rules.minions[t]
            if m["cost"] > gold or m["hp"] <= oS + o_resp:
                continue
            # rounds the opponent needs before its S reaches this HP (estimate, capped)
            rounds = 1
            if p["persist"] and not final_round:
                g = opp["gold"] + o_inc
                cap = min(rules.lifespan, rounds_left, 4)
                while rounds < cap and oS + self._response_estimate(opath, ob, g, rules) < m["hp"]:
                    rounds += 1
                    g += o_inc
            n_max = min(p["max_minions"], gold // m["cost"])
            for n in sorted({n_max, max(1, n_max // 2), max(1, n_max // 4), max(1, n_max // 8)}):
                res = gk.simulate_defense(mine + [t] * n, opath, ob, rules, profile=profile, guns=guns)
                gain = res.damage - base
                if gain <= 0:
                    continue
                c = n * m["cost"]
                value = gain * kappa if final_round else gain * rounds * kappa - c
                out.append((value, t, n, c))
        return out


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
