"""Shared local-planning helpers for research bots.

Everything here works on plain data derived from a bot's observation
(``observation["rules"]``, building lists, roster lists). Nothing reads live
engine objects. ``simulate_defense`` is a re-implementation of
``td_game.combat.simulate_map`` for speed; ``bot_research/tests`` checks it
against the engine on random cases, and ``engine_simulate_defense`` calls the
engine's own pure function on fresh copies for cross-checks.
"""
from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache
from typing import Iterable, Sequence

from td_game.pathfinding import shortest_path

W = H = 12
SPAWN = (0, 0)
BASE = (11, 11)


@dataclass(frozen=True)
class Rules:
    minions: dict          # name -> {"cost","hp","damage"}
    turrets: dict          # name -> {"cost","damage","range","aoe"}
    wall_cost: int
    ticks: int
    lifespan: int
    factory_cost: int
    factory_income: int
    path_income: int
    bounty: int
    initial_hp: int
    max_rounds: int

    @staticmethod
    def from_observation(observation: dict) -> "Rules":
        r = observation["rules"]
        g = r["globals"]
        return Rules(r["minions"], r["turrets"], r["wall_cost"], g["ticks_per_round"], g["roster_lifespan"],
                     g["factory_cost"], g["factory_income"], g["path_income_per_step"], g["base_hit_bounty"],
                     g["initial_hp"], g["max_rounds"])


def route(blocked: Iterable[tuple[int, int]]) -> list[tuple[int, int]] | None:
    """The engine's route (identical function) for a set of blocked cells."""
    return shortest_path(W, H, set(blocked), SPAWN, BASE)


@lru_cache(maxsize=200000)
def _route_cached(blocked: frozenset) -> tuple | None:
    p = shortest_path(W, H, blocked, SPAWN, BASE)
    return None if p is None else tuple(p)


def route_cached(blocked: Iterable[tuple[int, int]]) -> tuple | None:
    return _route_cached(frozenset(blocked))


def cells_of(buildings: Sequence[dict]) -> set[tuple[int, int]]:
    return {(b["x"], b["y"]) for b in buildings}


def neighbors8(cell):
    x, y = cell
    for dx in (-1, 0, 1):
        for dy in (-1, 0, 1):
            if (dx or dy) and 0 <= x + dx < W and 0 <= y + dy < H:
                yield (x + dx, y + dy)


def splash_profile(path: Sequence[tuple[int, int]], buildings: Sequence[dict], rules: Rules) -> list[int]:
    """Splash damage applied to every copy at each path index (0..L-1).

    Index L (the base) is never attacked: arrival is resolved before turrets.
    """
    splash = [(b["x"], b["y"], rules.turrets[b["type"]]["damage"]) for b in buildings
              if b["type"] != "wall" and rules.turrets[b["type"]]["aoe"] == 8]
    out = []
    for i in range(len(path) - 1):
        x, y = path[i]
        out.append(sum(d for sx, sy, d in splash if max(abs(sx - x), abs(sy - y)) == 1))
    return out


def splash_total(path, buildings, rules) -> int:
    return sum(splash_profile(path, buildings, rules))


def gun_coverage(path: Sequence[tuple[int, int]], buildings: Sequence[dict], rules: Rules):
    """For each gun: (damage, indices in range sorted descending). Excludes the base index."""
    guns = []
    for b in buildings:
        if b["type"] == "wall":
            continue
        t = rules.turrets[b["type"]]
        if t["aoe"] == 8:
            continue
        r2 = t["range"] ** 2
        idx = [i for i in range(len(path) - 1)
               if (path[i][0] - b["x"]) ** 2 + (path[i][1] - b["y"]) ** 2 <= r2]
        if idx:
            guns.append((t["damage"], sorted(idx, reverse=True)))
    return guns


@dataclass
class DefenseResult:
    hits: int
    damage: int
    killed: int
    spawned: int
    cleared: int
    leaked_types: list


def active_types(roster: Sequence[dict], round_number: int) -> list[str]:
    """Types of entries active in ``round_number`` in roster order (dense indexing)."""
    out = []
    for e in roster:
        exp = e.get("expires_after_round")
        if e["bought_round"] <= round_number and (exp is None or round_number <= exp):
            out.append(e["type"])
    return out


def simulate_defense(types: Sequence[str], path: Sequence[tuple[int, int]], buildings: Sequence[dict],
                     rules: Rules, *, profile=None, guns=None) -> DefenseResult:
    """Exact replay of one map's combat for an ordered list of active entry types.

    Matches td_game.combat.simulate_map: entry k spawns at tick k % ticks; each
    tick spawns, moves older copies, resolves arrivals, applies every turret's
    selection (guns: frontmost in range, ties by list order; splash: all copies in
    the 8 neighbours), then removes copies with hp <= 0.
    """
    ticks = rules.ticks
    L = len(path) - 1
    if profile is None:
        profile = splash_profile(path, buildings, rules)
    if guns is None:
        guns = gun_coverage(path, buildings, rules)
    schedule = [[] for _ in range(ticks)]
    for k, t in enumerate(types):
        schedule[k % ticks].append(t)
    minions = rules.minions
    # entity: [hp, damage, born, type]
    entities: list[list] = []
    hits = damage = killed = spawned = 0
    leaked = []
    for tick in range(ticks):
        spawning = schedule[tick]
        spawned += len(spawning)
        for t in spawning:
            m = minions[t]
            entities.append([m["hp"], m["damage"], tick, t])
        if not entities:
            continue
        survivors = []
        for e in entities:
            if e[2] < tick and tick - e[2] == L:
                hits += 1
                damage += e[1]
                leaked.append(e[3])
                continue
            survivors.append(e)
        if not survivors:
            entities = survivors
            continue
        # survivors are in non-increasing path index order (older first)
        first_at = {}
        for pos, e in enumerate(survivors):
            idx = tick - e[2]
            if idx not in first_at:
                first_at[idx] = pos
        dmg = [profile[tick - e[2]] for e in survivors]
        for gdmg, idxs in guns:
            for i in idxs:
                pos = first_at.get(i)
                if pos is not None:
                    dmg[pos] += gdmg
                    break
        alive = []
        for e, d in zip(survivors, dmg):
            e[0] -= d
            if e[0] > 0:
                alive.append(e)
        killed += len(survivors) - len(alive)
        entities = alive
    return DefenseResult(hits, damage, killed, spawned, len(entities), leaked)


def engine_simulate_defense(types: Sequence[str], buildings: Sequence[dict], config) -> DefenseResult:
    """Cross-check: call the engine's pure simulate_map on fresh copies."""
    from td_game.combat import simulate_map
    from td_game.state import Building, PlayerState, RosterEntry

    attacker = PlayerState("A", 800, 0, roster=[RosterEntry(i, t, 1, None) for i, t in enumerate(types)])
    defender = PlayerState("D", 10 ** 9, 0, buildings=[Building(b["x"], b["y"], b["type"]) for b in buildings])
    path = shortest_path(W, H, {(b["x"], b["y"]) for b in buildings}, SPAWN, BASE)
    totals = simulate_map(attacker, defender, path, 1, config)
    return DefenseResult(totals.hits, totals.damage, totals.killed, totals.spawned, totals.cleared, [])


def legal_build(blocked: set, cell: tuple[int, int]) -> bool:
    """Engine construction legality for one cell given the current blocked set."""
    x, y = cell
    if not (0 <= x < W and 0 <= y < H) or cell in (SPAWN, BASE) or cell in blocked:
        return False
    return route_cached(blocked | {cell}) is not None
