"""Fast exact replica of one map's combat for local planning.

Semantics follow td_game/combat.py (read, not modified):
- the k-th active roster entry (purchase order, expired entries skipped)
  spawns at tick k % ticks;
- each tick: spawn, move copies born earlier one cell, resolve arrivals at
  path index L (removed before turrets fire), every turret selects, then
  damage is applied and copies with hp <= 0 are removed;
- a gun hits the single in-range copy with the largest path index; ties go to
  the earliest copy in list order (spawn tick order, then roster order);
- a splash (aoe 8, range 0) hits every copy in the eight neighbouring cells.

All copies move in lockstep, so copies born at the same tick share a cell for
the whole round. The simulator groups them by spawn tick.
"""
from __future__ import annotations

from td_game.pathfinding import shortest_path

W = H = 12
SPAWN = (0, 0)
BASE = (11, 11)


def route(blocked):
    """Engine route for a set of blocked cells (identical BFS and tie-breaks)."""
    return shortest_path(W, H, blocked, SPAWN, BASE)


class MapModel:
    """Precomputed per-path-index turret coverage for a defender map."""

    def __init__(self, buildings, rules, path=None):
        # buildings: iterable of (x, y, type)
        self.buildings = [(b[0], b[1], b[2]) for b in buildings]
        blocked = {(x, y) for x, y, _ in self.buildings}
        self.path = path if path is not None else route(blocked)
        if self.path is None:
            raise ValueError("no path")
        self.L = len(self.path) - 1
        turrets = rules["turrets"]
        L = self.L
        splash = [0] * L
        guns = []  # (damage, sorted list of in-range path indices)
        for x, y, t in self.buildings:
            if t == "wall":
                continue
            spec = turrets[t]
            if spec["aoe"] == 8:
                for i in range(L):
                    px, py = self.path[i]
                    if max(abs(px - x), abs(py - y)) == 1:
                        splash[i] += spec["damage"]
            else:
                r2 = spec["range"] ** 2
                cover = [i for i in range(L)
                         if (self.path[i][0] - x) ** 2 + (self.path[i][1] - y) ** 2 <= r2]
                if cover:
                    guns.append((spec["damage"], cover))
        self.splash = splash
        self.guns = guns
        # in_range[g][i] boolean for quick tests
        self.gun_mask = []
        for dmg, cover in guns:
            m = [False] * L
            for i in cover:
                m[i] = True
            self.gun_mask.append((dmg, m, max(cover), min(cover)))
        self.splash_total = sum(splash)


def schedule_from_types(types, ticks=250):
    """types: list of minion type names in active-roster order."""
    groups = {}
    for k, t in enumerate(types):
        groups.setdefault(k % ticks, []).append(t)
    return groups


def simulate(model, types, rules, ticks=250, detail=False, slack=False):
    """Simulate a wave of active entries (types in roster order) on model.

    Returns (hits, damage). With detail=True also returns a dict mapping
    entry k to its arrival tick (arrived entries only). With slack=True
    returns (hits, damage, slack) where slack is the sum over arrived copies
    of damage * remaining_hp / full_hp (a continuous measure of how far the
    defence is from killing them; used as a planning surrogate).
    """
    minions = rules["minions"]
    L = model.L
    splash = model.splash
    guns = model.gun_mask
    # groups: spawn tick -> list of [hp, dmg, k]
    groups = {}
    for k, t in enumerate(types):
        s = k % ticks
        groups.setdefault(s, []).append([minions[t]["hp"], minions[t]["damage"], k, minions[t]["hp"]])
    spawn_ticks = sorted(groups)
    hits = 0
    damage = 0
    slk = 0.0
    arrived = {} if detail else None
    active = []  # spawn ticks currently on map, ascending (front first)
    si = 0
    nspawn = len(spawn_ticks)
    for tick in range(ticks):
        while si < nspawn and spawn_ticks[si] == tick:
            active.append(tick)
            si += 1
        if not active:
            if si >= nspawn:
                break
            continue
        # arrivals: front groups with tick - s == L
        while active and tick - active[0] == L:
            s = active.pop(0)
            for m in groups[s]:
                hits += 1
                damage += m[1]
                if slack:
                    slk += m[1] * m[0] / m[3]
                if detail:
                    arrived[m[2]] = tick
        if not active:
            continue
        # gun targeting: frontmost alive group in range
        gun_hits = {}
        for dmg, mask, hi, lo in guns:
            for s in active:  # front first
                idx = tick - s
                if idx < lo:
                    break
                if idx <= hi and mask[idx]:
                    gun_hits[s] = gun_hits.get(s, 0) + dmg
                    break
        new_active = []
        for s in active:
            g = groups[s]
            sd = splash[tick - s]
            gd = gun_hits.get(s, 0)
            if sd or gd:
                first = True
                for m in g:
                    m[0] -= sd + (gd if first else 0)
                    first = False
                g[:] = [m for m in g if m[0] > 0]
            if g:
                new_active.append(s)
        active = new_active
    if detail:
        return hits, damage, arrived
    if slack:
        return hits, damage, slk
    return hits, damage
