"""Defensive planning component for research bots (lane hrt-w1).

Public API
----------
plan_defense(observation, budget, required_hp=None, threat_types=None, *, allow_guns=True, layout=LAYOUT)
    -> list[action]   build actions (cost <= min(budget, own gold)) that stop the given threat as cheaply
                      as the planner can find, or the strongest affordable partial plan.
plan_walls(observation, budget, layout=LAYOUT, stage=None) -> list[action]   layout walls in build order.
threat_compositions(observation, extra_gold=None) -> list[list[str]]   sampled rosters the opponent can
                      field this round (visible active roster + up to ~9 alternative purchase bundles with
                      its visible gold, in several orders). A heuristic cover, not every affordable order:
                      a zero-leak plan is guaranteed only for the listed compositions (order matters for
                      guns, not for splash).
splash_damage(buildings, rules) -> int   exact per-copy splash damage on the current route.
LAYOUT: MasterLayout   the default target layout (see below).

Exact model (bundled rules, see bot_research/notes/defense.md)
  * A copy that reaches the base has occupied every route cell 0..L-1 for exactly one tick, so its
    full-route splash exposure is 10 * A with A = number of (route cell, adjacent splash) pairs;
    independent of the stream (copies that die earlier receive only a prefix). If 10 * A >= HP of
    every type fielded, no copy reaches the base (zero leaks, proved; see notes/defense.md).
  * Guns hit one copy per tick (frontmost in range); their effect depends on the stream, so gun plans
    are verified by exact simulation (bot_research.harness.gamekit.simulate_defense == engine).

Master layout (MasterLayout.default()): horizontal serpentine with wall rows 1, 3, 5, 7 (gaps at
x = 11, 0, 11, 0) plus a square wave of 3-cell pillars at columns 1, 3, 5, 7, 9 in rows 8-11. Full
layout: 59 cells, route length 78, 41 cells with splash adjacency >= 6 (seven with 7). Cells with
final adjacency >= 5 are reserved for splashes (never built as walls); stage A (rows 1, 3) is built
as walls except its two U-turn pillars. Buildings are permanent, so reserved cells stay open until
bought; an open cell next to a gap shortens the intermediate route by about 2 steps.

Cost of planning: a few milliseconds for splash plans (adjacency counting), up to ~1 s for gun plans
(exact simulations on a restricted candidate set).
"""
from __future__ import annotations

from dataclasses import dataclass, field

from bot_research.harness import gamekit as gk

from .geometry import N8, W, H, SPAWN, BASE, attackable_cells, route, splash_adjacency

TIERS = ("tier1", "tier2", "tier3", "tier4", "tier5")


def _rows(gaps: dict) -> list[tuple[int, int]]:
    return [(x, y) for y, gap in gaps.items() for x in range(W) if x != gap]


@dataclass
class MasterLayout:
    cells: list[tuple[int, int]]
    wall_order: list[tuple[int, int]]        # cells to build as walls, in build order
    splash_cells: list[tuple[int, int]]      # reserved for splashes, in purchase preference order
    stages: list[int]                        # wall_order prefix lengths completing stage A, B, wave
    final_adj: dict = field(default_factory=dict)
    final_route: set = field(default_factory=set)
    final_len: int = 0

    @staticmethod
    def default(reserve_stage_a=((10, 1), (1, 3)), reserve_min_adj: int = 5) -> "MasterLayout":
        stage_a = _rows({1: 11, 3: 0})
        stage_b = _rows({5: 11, 7: 0})
        wave = []
        for c in (1, 3, 5, 7, 9):
            rows = (8, 9, 10) if (c - 1) in (0, 4, 8) else (9, 10, 11)
            wave += [(c, y) for y in rows]
        cells = stage_a + stage_b + wave
        full = route(set(cells))
        att = attackable_cells(full)
        final_adj = {c: splash_adjacency(c, att) for c in cells}
        reserved = list(reserve_stage_a)
        for c in stage_b + wave:
            if final_adj[c] >= reserve_min_adj:
                reserved.append(c)
        reserved.sort(key=lambda c: (-final_adj[c], -(c[0] == 10), c[1], -c[0]))
        wall_a = [c for c in stage_a if c not in reserved]
        wall_a.sort(key=lambda c: (c[1], c[0] if c[1] == 1 else -c[0]))
        wall_b = [c for c in stage_b if c not in reserved]
        wall_w = [c for c in wave if c not in reserved]
        wall_order = wall_a + wall_b + wall_w
        stages = [len(wall_a), len(wall_a) + len(wall_b), len(wall_order)]
        return MasterLayout(cells, wall_order, reserved, stages, final_adj, set(full), len(full) - 1)


    @staticmethod
    def from_template(walls, slots, stage_rows=((1, 3), (5, 7))) -> "MasterLayout":
        """Layout from a WALLS/SLOTS pair (see templates.py). Walls are ordered by stage: rows in
        stage_rows[0] first (row 1 left to right, row 3 right to left), then stage_rows[1], then the
        rest (bottom snake). Slots are ordered by final adjacency (ties: nearer the pillar end)."""
        walls = [tuple(c) for c in walls]
        slots = [tuple(c) for c in slots]
        cells = walls + slots
        full = route(set(cells))
        att = attackable_cells(full)
        final_adj = {c: splash_adjacency(c, att) for c in cells}

        def stage_key(c):
            x, y = c
            for i, rows in enumerate(stage_rows):
                if y in rows:
                    return (i, y, x if y % 4 == 1 else -x)
            return (len(stage_rows), y, x)
        wall_order = sorted(walls, key=stage_key)
        stages = []
        for i in range(len(stage_rows)):
            stages.append(sum(1 for c in wall_order if stage_key(c)[0] <= i))
        stages.append(len(wall_order))
        slots.sort(key=lambda c: (-final_adj[c], -(c[0] in (10, 1)), c[1], -c[0]))
        return MasterLayout(cells, wall_order, slots, stages, final_adj, set(full), len(full) - 1)


LAYOUT = MasterLayout.default()


def layout_by_name(name: str) -> MasterLayout:
    """'default' (serpentine + wave, reserved adjacency >= 5), 'annealed25', 'annealed26', 'pillars774', 'lead_v3'."""
    if name in (None, "default"):
        return LAYOUT
    from . import templates as T
    pairs = {"annealed25": (T.ANNEALED_25_WALLS, T.ANNEALED_25_SLOTS),
             "annealed26": (T.ANNEALED_26_WALLS, T.ANNEALED_26_SLOTS),
             "pillars774": (T.PILLARS_7_7_4_WALLS, T.PILLARS_7_7_4_SLOTS),
             "lead_v3": (T.LEAD_V3_WALLS, T.LEAD_V3_SLOTS)}
    walls, slots = pairs[name]
    return MasterLayout.from_template(walls, slots)


# ----------------------------------------------------------------------------- observation helpers
def observe(observation: dict):
    me = observation["players"][observation["player"]]
    rules = gk.Rules.from_observation(observation)
    buildings = [dict(b) for b in me["buildings"]]
    blocked = {(b["x"], b["y"]) for b in buildings}
    return me, rules, buildings, blocked


def splash_name_of(rules) -> str:
    return next(k for k, v in rules.turrets.items() if v["aoe"] == 8)


def adjacency_total(buildings, blocked, rules) -> int:
    path = gk.route_cached(blocked)
    if path is None:
        return -1
    att = set(path[:-1])
    return sum(splash_adjacency((b["x"], b["y"]), att) for b in buildings
               if b["type"] != "wall" and rules.turrets[b["type"]]["aoe"] == 8)


def splash_damage(buildings, rules, blocked=None) -> int:
    blocked = blocked if blocked is not None else {(b["x"], b["y"]) for b in buildings}
    a = adjacency_total(buildings, blocked, rules)
    return a * rules.turrets[splash_name_of(rules)]["damage"] if a >= 0 else -1


def active_opponent_types(observation: dict) -> list[str]:
    """Opponent entries that fight this round (dense order), from the visible roster."""
    opp = observation["players"][1 - observation["player"]]
    return gk.active_types(opp["roster"], observation["round"])


MAX_BUNDLE_GOLD = 10 ** 6    # gold above this is treated as this much when generating purchase bundles
MAX_BUNDLE_COPIES = 2000     # copies per sampled bundle (memory bound; the leak check short-cuts huge ones)
HUGE_COMPOSITION = 400       # compositions above this size are judged by the exact splash bound, not simulated


def affordable_bundles(gold: int, rules, max_bundles: int = 12) -> list[list[str]]:
    """Alternative purchase lists with at most `gold`: for each tier, as many as affordable of that
    tier first, then fill greedily with the most expensive affordable types (heavy-first order), and
    the same multiset in ascending-cost order (heavy-last: cheap copies screen the heavy ones against
    frontmost-first guns); plus a tier1 screen ahead of big copies and interleaved orders of the two
    most expensive affordable tiers. A heuristic cover of the attacker's options, not all of them."""
    costs = {t: rules.minions[t]["cost"] for t in TIERS if t in rules.minions}
    gold = min(gold, MAX_BUNDLE_GOLD)
    out = []

    def add(b):
        if b and b not in out:
            out.append(b[:MAX_BUNDLE_COPIES])

    for lead in reversed(TIERS):
        if lead not in costs:
            continue
        g = gold
        bundle = []
        n = g // costs[lead]
        bundle += [lead] * n
        g -= n * costs[lead]
        for t in reversed(TIERS):
            if t in costs and t != lead:
                k = g // costs[t]
                bundle += [t] * k
                g -= k * costs[t]
        add(bundle)
        if len(set(bundle)) > 1:
            add(sorted(bundle, key=lambda t: costs[t]))          # heavy last
    if "tier1" in costs and gold >= costs["tier1"]:
        big = next((t for t in reversed(TIERS) if t in costs and costs[t] <= gold - costs["tier1"]), None)
        if big:
            n_big = (gold - 3 * costs["tier1"]) // costs[big] if gold >= 3 * costs["tier1"] + costs[big] else 0
            if n_big > 0:
                rest = gold - n_big * costs[big]
                add(["tier1"] * (rest // costs["tier1"]) + [big] * n_big)
    aff = [t for t in reversed(TIERS) if t in costs and costs[t] <= gold]
    if len(aff) >= 2:
        a, b = aff[0], aff[1]
        g, mix = gold, []
        while g >= costs[a] + costs[b]:
            mix += [b, a]
            g -= costs[a] + costs[b]
        for t in aff:
            while g >= costs[t]:
                mix.append(t)
                g -= costs[t]
        add(mix)
        add([x for x in reversed(mix)])
    return out[:max_bundles]


def wrap_bundles(gold: int, n_visible: int, rules, ticks: int = 250, max_pad: int = 300) -> list[list[str]]:
    """Purchases that pad the roster with the cheapest copies so that a heavy copy becomes entry
    ticks*m (spawn tick 0, arriving even on long routes), for each heavy tier affordable after the padding.
    Entry k (zero-based) spawns at tick k % ticks, so with n_visible active entries the first new copy is
    entry n_visible and pad = ticks*m - n_visible cheap copies make the heavy one entry ticks*m (tick 0)."""
    costs = {t: rules.minions[t]["cost"] for t in TIERS if t in rules.minions}
    if "tier1" not in costs:
        return []
    out = []
    m = n_visible // ticks + 1
    pad = ticks * m - n_visible          # the heavy copy becomes entry index ticks*m -> spawn tick 0
    if pad < 0 or pad > max_pad:
        return []
    pad_cost = pad * costs["tier1"]
    gold = min(gold, MAX_BUNDLE_GOLD)
    for h in ("tier5", "tier4", "tier3"):
        if h in costs and pad_cost + costs[h] <= gold:
            n_h = min((gold - pad_cost) // costs[h], MAX_BUNDLE_COPIES - pad)
            out.append(["tier1"] * pad + [h] * max(1, n_h))
    return out


EXHAUSTIVE_MAX = 400   # enumerate every ordered purchase list when there are at most this many


def exhaustive_bundles(gold: int, rules, max_count: int = EXHAUSTIVE_MAX) -> list[list[str]] | None:
    """Every ordered purchase list (sequence of types) with total cost <= gold, if there are at most
    max_count of them (else None). Order matters for gun targeting, so this is the exact threat set
    for a small budget (e.g. 26 lists for 100 gold, excluding the empty one)."""
    costs = [(t, rules.minions[t]["cost"]) for t in TIERS if t in rules.minions]
    out = []
    stack = [([], gold)]
    while stack:
        seq, g = stack.pop()
        for t, c in costs:
            if c <= g:
                nxt = seq + [t]
                out.append(nxt)
                if len(out) > max_count:
                    return None
                stack.append((nxt, g - c))
    return out


def threat_compositions(observation: dict, extra_gold: int | None = None) -> list[list[str]]:
    """Rosters the opponent may field this round: visible active entries followed by each alternative
    purchase bundle its visible gold allows (new purchases spawn after older entries). When the gold
    allows at most EXHAUSTIVE_MAX ordered purchase lists, all of them are used (exact); otherwise the
    sampled bundles (affordable_bundles) plus roster-wrap bundles (padding to 250 entries so a heavy
    copy spawns at tick 0)."""
    rules = gk.Rules.from_observation(observation)
    opp = observation["players"][1 - observation["player"]]
    base = active_opponent_types(observation)
    gold = opp["gold"] if extra_gold is None else extra_gold
    exhaustive = exhaustive_bundles(gold, rules)
    if exhaustive is not None:
        bundles = exhaustive or [[]]
    else:
        bundles = affordable_bundles(gold, rules) or [[]]
    bundles = bundles + wrap_bundles(gold, len(base), rules, rules.ticks)
    comps = []
    for b in bundles:
        comp = base + b
        if comp and comp not in comps:
            comps.append(comp)
    return comps


def max_hp(types, rules) -> int:
    return max((rules.minions[t]["hp"] for t in types), default=0)


# ----------------------------------------------------------------------------- building blocks
def _action(cell, kind):
    if kind == "wall":
        return {"op": "build_wall", "x": cell[0], "y": cell[1]}
    return {"op": "build_turret", "type": kind, "x": cell[0], "y": cell[1]}


def _apply(buildings, blocked, cell, kind):
    buildings.append({"x": cell[0], "y": cell[1], "type": kind})
    blocked.add(cell)


def _pop(buildings, blocked, cell):
    buildings.pop()
    blocked.discard(cell)


def plan_walls(observation: dict, budget: int, layout: MasterLayout = LAYOUT, stage: int | None = None) -> list[dict]:
    """Layout walls in build order (optionally only through stage index 0, 1 or 2), within budget."""
    me, rules, buildings, blocked = observe(observation)
    budget = min(budget, me["gold"])
    limit = layout.stages[stage] if stage is not None else len(layout.wall_order)
    actions, spent = [], 0
    for c in layout.wall_order[:limit]:
        if c in blocked:
            continue
        if spent + rules.wall_cost > budget:
            break
        if gk.legal_build(blocked, c):
            actions.append(_action(c, "wall"))
            _apply(buildings, blocked, c, "wall")
            spent += rules.wall_cost
    return actions


FOREIGN_LIMIT = 8   # own buildings outside the layout above which the layout's exclusions are dropped


def is_foreign(blocked, layout) -> bool:
    """True when the own map has more than FOREIGN_LIMIT buildings outside the master layout (e.g. after a
    scripted opening); the planner then searches every legal cell next to the route."""
    return sum(1 for c in blocked if c not in layout.final_adj) > FOREIGN_LIMIT


def _splash_candidates(blocked, layout, path):
    """Reserved cells plus off-layout cells next to the current route that are not on the final route
    (on a foreign map: every legal cell next to the route)."""
    att = set(path[:-1])
    cands = {c for c in layout.splash_cells if c not in blocked}
    foreign = is_foreign(blocked, layout)
    for (x, y) in att:
        for dx, dy in N8:
            c = (x + dx, y + dy)
            if (0 <= c[0] < W and 0 <= c[1] < H and c not in blocked and c not in (SPAWN, BASE)
                    and (foreign or (c not in layout.final_route and c not in layout.wall_order))):
                cands.add(c)
    return cands


def _greedy_splashes(buildings, blocked, rules, layout, budget, target_adj, splash_name):
    cost = rules.turrets[splash_name]["cost"]
    actions, spent = [], 0
    cur = adjacency_total(buildings, blocked, rules)
    while cur < target_adj and spent + cost <= budget:
        path = gk.route_cached(blocked)
        best = None
        for c in _splash_candidates(blocked, layout, path):
            if not gk.legal_build(blocked, c):
                continue
            _apply(buildings, blocked, c, splash_name)
            a = adjacency_total(buildings, blocked, rules)
            _pop(buildings, blocked, c)
            key = (a - cur, c in layout.splash_cells, layout.final_adj.get(c, 0))
            if best is None or key > best[0]:
                best = (key, c, a)
        if best is None or best[0][0] <= 0:
            break
        _, c, a = best
        _apply(buildings, blocked, c, splash_name)
        actions.append(_action(c, splash_name))
        spent += cost
        cur = a
    return actions, spent, cur


def _wall_prefix_plans(buildings0, blocked0, rules, layout, budget):
    """Yield (actions, spent, buildings, blocked) for wall prefixes: none, through each stage."""
    unbuilt = [c for c in layout.wall_order if c not in blocked0]
    prefixes = [0]
    for s in layout.stages:
        n = len([c for c in layout.wall_order[:s] if c not in blocked0])
        if n and n not in prefixes:
            prefixes.append(n)
    for n in prefixes:
        if n * rules.wall_cost > budget:
            continue
        buildings, blocked = [dict(b) for b in buildings0], set(blocked0)
        actions, spent = [], 0
        for c in unbuilt[:n]:
            if gk.legal_build(blocked, c):
                actions.append(_action(c, "wall"))
                _apply(buildings, blocked, c, "wall")
                spent += rules.wall_cost
        yield actions, spent, buildings, blocked


def _leak(buildings, blocked, rules, comps):
    """(leak score, total hits) over threat compositions.

    score = sum over compositions of (10 * leaked base damage + remaining HP of leaked copies); it is
    0 exactly when nothing leaks and decreases when a copy is wounded further, which lets the greedy
    gun pass make progress on big copies that need several turrets.
    Shortcuts (exact): a composition whose every type has HP <= the per-copy splash exposure cannot leak
    (proved bound); a composition with more than HUGE_COMPOSITION copies and some type above the exposure
    is counted as leaking its copies above the exposure, since guns kill at most one copy per tick each
    and such floods exceed that (conservative for the planner: it then buys splash saturation).
    """
    from .simulate import simulate_leak
    path = gk.route_cached(blocked)
    profile = gk.splash_profile(path, buildings, rules)
    guns = gk.gun_coverage(path, buildings, rules)
    exposure = sum(profile)
    score = hits = 0
    for types in comps:
        hp_max = max(rules.minions[t]["hp"] for t in types)
        if hp_max <= exposure:
            continue
        if len(types) > HUGE_COMPOSITION:
            big = [t for t in types if rules.minions[t]["hp"] > exposure]
            n_gun_kills = 250 * len(guns)
            leaking = big[n_gun_kills:] if n_gun_kills < len(big) else []
            if not leaking:
                leaking = big[-1:]       # conservative: assume at least one heavy copy gets through
            score += sum(10 * rules.minions[t]["damage"] + rules.minions[t]["hp"] - exposure for t in leaking)
            hits += len(leaking)
            continue
        h, d, lhp = simulate_leak(types, path, buildings, rules, profile=profile, guns=guns)
        score += 10 * d + lhp
        hits += h
    return score, hits


SATURATION_ADJ = 155   # adjacency to keep reachable with splashes (tier5 needs 150)


def reserved_capacity(buildings, blocked, layout):
    """Final-route adjacency still reachable with splashes: splashes already placed plus every
    unbuilt reserved cell (both measured on the layout's final route)."""
    total = 0
    for b in buildings:
        if b["type"] == "splash":
            total += layout.final_adj.get((b["x"], b["y"]), 0)
    for c in layout.splash_cells:
        if c not in blocked:
            total += layout.final_adj[c]
    return total


def _gun_candidates(blocked, layout, path, rules, kind, top=8, buildings=None):
    """Legal cells with the most route cells in range of `kind` (not on the final route).

    Reserved splash cells are offered only while the reserved capacity minus that cell stays
    >= SATURATION_ADJ, so guns never remove the option of full splash immunity."""
    att = set(path[:-1])
    cap = reserved_capacity(buildings, blocked, layout) if buildings is not None else None
    foreign = is_foreign(blocked, layout)
    rng2 = rules.turrets[kind]["range"] ** 2
    scored = []
    seen = set()
    for (x, y) in att:
        for dx in range(-3, 4):
            for dy in range(-3, 4):
                c = (x + dx, y + dy)
                if c in seen or not (0 <= c[0] < W and 0 <= c[1] < H) or c in blocked or c in (SPAWN, BASE):
                    continue
                seen.add(c)
                if not foreign and (c in layout.final_route or c in layout.wall_order):
                    continue
                if not foreign and cap is not None and c in layout.final_adj and cap - layout.final_adj[c] < SATURATION_ADJ:
                    continue
                cov = sum((px - c[0]) ** 2 + (py - c[1]) ** 2 <= rng2 for (px, py) in att)
                if cov:
                    scored.append((cov, c))
    scored.sort(reverse=True)
    return [c for _, c in scored[:top]]


def _gun_pass(buildings, blocked, rules, actions, spent, budget, comps, layout, max_steps=12, deadline=None):
    """Greedy additions (gun3/gun2/gun1/splash) judged by simulated leak score per gold.

    Candidates are scored on the composition with the largest current leak score (one simulation
    per candidate); the chosen addition is then re-scored on all compositions."""
    from .simulate import simulate_leak

    def leak_one(types):
        path = gk.route_cached(blocked)
        profile = gk.splash_profile(path, buildings, rules)
        guns = gk.gun_coverage(path, buildings, rules)
        h, d, lhp = simulate_leak(types, path, buildings, rules, profile=profile, guns=guns)
        return 10 * d + lhp, h

    cur_dmg, cur_hits = _leak(buildings, blocked, rules, comps)
    kinds = sorted(rules.turrets, key=lambda k: -rules.turrets[k]["cost"])
    splash = splash_name_of(rules)
    import time as _time
    steps = 0
    while cur_hits > 0 and steps < max_steps:
        if deadline is not None and _time.time() > deadline:
            break
        path = gk.route_cached(blocked)
        worst = max(comps, key=lambda t: leak_one(t)[0])
        w_score, _ = leak_one(worst)
        best = None
        for kind in kinds:
            k_cost = rules.turrets[kind]["cost"]
            if spent + k_cost > budget:
                continue
            if kind == splash:
                pool = sorted(_splash_candidates(blocked, layout, path),
                              key=lambda c: -layout.final_adj.get(c, 0))[:6]
            else:
                pool = _gun_candidates(blocked, layout, path, rules, kind, buildings=buildings)
            for c in pool:
                if not gk.legal_build(blocked, c):
                    continue
                _apply(buildings, blocked, c, kind)
                sc, h = leak_one(worst)
                level = 0
                if h == 0:
                    # clears the worst composition: check all of them (cheapest full clear wins)
                    _, h_all = _leak(buildings, blocked, rules, comps)
                    level = 2 if h_all == 0 else 1
                _pop(buildings, blocked, c)
                gain = (w_score - sc) / k_cost
                key = (level, -k_cost if level == 2 else gain, gain)
                if best is None or key > best[0]:
                    best = (key, c, kind)
        if best is None:
            break
        _, c, kind = best
        _apply(buildings, blocked, c, kind)
        d, h = _leak(buildings, blocked, rules, comps)
        if d >= cur_dmg:
            _pop(buildings, blocked, c)
            break
        actions.append(_action(c, kind))
        spent += rules.turrets[kind]["cost"]
        cur_dmg, cur_hits = d, h
        steps += 1
    return actions, spent, cur_dmg, cur_hits


# ----------------------------------------------------------------------------- main entry point
GUN_PASS_MAX_ENTITIES = 120   # gun plans are not tried against compositions larger than this (splash is the answer)
TIME_BUDGET = 3.0             # seconds; the gun pass stops adding candidates once exceeded (plans so far are kept)


def plan_defense(observation: dict, budget: int, required_hp: int | None = None, threat_types=None, *,
                 allow_guns: bool = True, layout: MasterLayout = LAYOUT, partial: str = "best",
                 time_budget: float | None = None) -> list[dict]:
    """Build actions (cost <= min(budget, own gold)) stopping the threat as cheaply as found.

    threat_types: list of type lists (compositions) or one list of types the opponent may field
    this round; required_hp: alternatively a per-copy HP to beat with splash alone. With a threat
    and allow_guns, both the splash-bound plan and a gun plan (exact simulation, zero leaks on all
    compositions) are built and the cheaper zero-leak plan is returned; if neither achieves zero
    leaks within budget, the plan with the least simulated leaked damage (then most adjacency).
    partial="best" returns the strongest affordable plan when zero leaks are unaffordable;
    partial="none" returns [] in that case (do not spend on a defence that still leaks).
    Plans always start from the current buildings in the observation. Gun plans are skipped when a
    composition has more than GUN_PASS_MAX_ENTITIES copies, and the gun pass stops after time_budget
    seconds (default TIME_BUDGET); the result is then the best plan found so far (still exact).
    """
    import time as _time
    t0 = _time.time()
    deadline = t0 + (TIME_BUDGET if time_budget is None else time_budget)
    me, rules, buildings0, blocked0 = observe(observation)
    budget = max(0, min(budget, me["gold"]))
    splash = splash_name_of(rules)
    sdmg = rules.turrets[splash]["damage"]
    comps = None
    if threat_types:
        comps = [list(t) for t in threat_types] if isinstance(threat_types[0], (list, tuple)) else [list(threat_types)]
        comps = [c for c in comps if c]
        if required_hp is None:
            required_hp = max(max_hp(c, rules) for c in comps) if comps else 0
    if not required_hp:
        return []
    target_adj = -(-required_hp // sdmg)

    a0 = adjacency_total(buildings0, blocked0, rules)
    if a0 >= target_adj:
        return []
    if comps and allow_guns and _leak(buildings0, blocked0, rules, comps)[1] == 0:
        return []

    candidates = []   # (zero_leak, -cost, -leaked_damage, adjacency, actions)
    for w_actions, w_spent, buildings, blocked in _wall_prefix_plans(buildings0, blocked0, rules, layout, budget):
        s_actions, s_spent, adj = _greedy_splashes(buildings, blocked, rules, layout, budget - w_spent, target_adj, splash)
        actions, spent = w_actions + s_actions, w_spent + s_spent
        if comps:
            d, h = _leak(buildings, blocked, rules, comps)
            candidates.append((h == 0, -spent, -d, adj, actions))
        else:
            candidates.append((adj >= target_adj, -spent, 0, adj, actions))
    if comps and allow_guns and max(len(c) for c in comps) <= GUN_PASS_MAX_ENTITIES:
        for i, (w_actions, w_spent, buildings, blocked) in enumerate(_wall_prefix_plans(buildings0, blocked0, rules, layout, budget)):
            if i >= 2 or _time.time() > deadline:
                break
            actions, spent, d, h = _gun_pass(buildings, blocked, rules, list(w_actions), w_spent, budget, comps, layout, deadline=deadline)
            candidates.append((h == 0, -spent, -d, adjacency_total(buildings, blocked, rules), actions))
    if not candidates:
        return []
    zero = [c for c in candidates if c[0]]
    if zero:
        zero.sort(key=lambda c: (c[1], c[3]), reverse=True)   # cheapest, then most adjacency
        return zero[0][4]
    if partial == "none":
        return []
    candidates.sort(key=lambda c: (c[2], c[3], c[1]), reverse=True)   # least leak, most adjacency, cheapest
    return candidates[0][4]


def defense_cost(observation: dict, threat_types, *, allow_guns: bool = True, layout: MasterLayout = LAYOUT) -> int | None:
    """Cost of the cheapest zero-leak plan the planner finds with unlimited budget (None if none)."""
    me, rules, buildings, blocked = observe(observation)
    o2 = dict(observation)
    players = list(o2["players"])
    m2 = dict(me)
    m2["gold"] = 10 ** 9
    players[o2["player"]] = m2
    o2["players"] = players
    acts = plan_defense(o2, 10 ** 9, threat_types=threat_types, allow_guns=allow_guns, layout=layout, partial="none")
    if not acts:
        comps = [list(t) for t in threat_types] if threat_types and isinstance(threat_types[0], (list, tuple)) else [list(threat_types or [])]
        comps = [c for c in comps if c]
        if not comps or _leak(buildings, blocked, rules, comps)[1] == 0:
            return 0
        return None
    total = 0
    for a in acts:
        total += rules.wall_cost if a["op"] == "build_wall" else rules.turrets[a["type"]]["cost"]
    return total


def opponent_leak(observation: dict, extra_types: list[str]) -> tuple[int, int]:
    """(hits, base damage) my active roster plus `extra_types` would score on the opponent's CURRENT
    map this round (exact simulation; ignores anything the opponent builds this round)."""
    from .simulate import simulate_leak
    me = observation["players"][observation["player"]]
    opp = observation["players"][1 - observation["player"]]
    rules = gk.Rules.from_observation(observation)
    types = gk.active_types(me["roster"], observation["round"]) + list(extra_types)
    if not types:
        return 0, 0
    blocked = {(b["x"], b["y"]) for b in opp["buildings"]}
    path = gk.route_cached(blocked)
    h, d, _ = simulate_leak(types, path, [dict(b) for b in opp["buildings"]], rules)
    return h, d


def threat_damage(observation: dict, comps=None) -> int:
    """Largest simulated base damage over the threat compositions against the current own map
    (exact; compositions default to threat_compositions(observation))."""
    from .simulate import simulate_leak
    me, rules, buildings, blocked = observe(observation)
    comps = comps if comps is not None else threat_compositions(observation)
    if not comps:
        return 0
    path = gk.route_cached(blocked)
    profile = gk.splash_profile(path, buildings, rules)
    guns = gk.gun_coverage(path, buildings, rules)
    worst = 0
    for types in comps:
        h, d, lhp = simulate_leak(types, path, buildings, rules, profile=profile, guns=guns)
        worst = max(worst, d)
    return worst


def opponent_view(observation: dict) -> dict:
    """The observation as the opponent sees it this round (same public state, player index swapped)."""
    o = dict(observation)
    o["player"] = 1 - observation["player"]
    return o


def robust_leak(observation: dict, extra_types: list[str], *, layout=None, fraction: float = 1.0) -> tuple[int, int]:
    """(hits, damage) my roster plus `extra_types` would score this round if the opponent answers with the
    best zero-leak-or-partial plan plan_defense finds for it using `fraction` of its visible gold (1.0 = all;
    a proxy for its best same-round response; exact for the simulated map, heuristic as a bound)."""
    from .simulate import simulate_leak
    me = observation["players"][observation["player"]]
    opp = observation["players"][1 - observation["player"]]
    rules = gk.Rules.from_observation(observation)
    types = gk.active_types(me["roster"], observation["round"]) + list(extra_types)
    if not types:
        return 0, 0
    ov = opponent_view(observation)
    acts = plan_defense(ov, int(opp["gold"] * fraction), threat_types=[types], layout=layout or LAYOUT, partial="best")
    buildings = [dict(b) for b in opp["buildings"]] + [
        {"x": a["x"], "y": a["y"], "type": "wall" if a["op"] == "build_wall" else a["type"]} for a in acts]
    blocked = {(b["x"], b["y"]) for b in buildings}
    path = gk.route_cached(blocked)
    if path is None:
        return 0, 0
    h, d, _ = simulate_leak(types, path, buildings, rules)
    return h, d
