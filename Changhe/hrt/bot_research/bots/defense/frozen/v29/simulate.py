"""Exact local combat simulation for planning, on freshly constructed state copies.

Uses td_game.combat.simulate_map (the engine's own code) with a PlayerState built from
the observation, so predicted hits/damage equal what the engine will compute for the same
buildings, roster and round. Nothing here touches a live engine object.
"""
from __future__ import annotations

from td_game.combat import simulate_map
from td_game.config import GameConfig, config_from_dict
from td_game.state import Building, PlayerState, RosterEntry

from .geometry import route

_CFG_CACHE: dict[int, GameConfig] = {}


def config_from_observation(obs: dict) -> GameConfig:
    """Validated GameConfig from the rules embedded in the observation (cached by identity)."""
    key = id(obs["rules"])
    cfg = _CFG_CACHE.get(key)
    if cfg is None:
        cfg = config_from_dict(obs["rules"])
        _CFG_CACHE.clear()
        _CFG_CACHE[key] = cfg
    return cfg


def buildings_from_list(items) -> list[Building]:
    return [Building(b["x"], b["y"], b["type"]) for b in items]


def roster_from_list(items, round_number: int) -> list[RosterEntry]:
    """RosterEntry list from snapshot roster dicts (keeps order, hence spawn order)."""
    out = []
    for e in items:
        out.append(RosterEntry(e["id"], e["type"], e["bought_round"], e.get("expires_after_round")))
    return out


def hypothetical_entries(types: list[str], round_number: int, lifespan: int, start_id: int = 10_000) -> list[RosterEntry]:
    """Entries the opponent might buy this round (appended after the visible roster)."""
    exp = round_number + lifespan - 1 if lifespan else None
    return [RosterEntry(start_id + i, t, round_number, exp) for i, t in enumerate(types)]


def simulate_defense(cfg: GameConfig, buildings: list[Building], roster: list[RosterEntry], round_number: int):
    """Return (hits, base_damage, killed, cleared, path_length) for this defense vs roster."""
    blocked = [(b.x, b.y) for b in buildings]
    path = route(blocked)
    if path is None:
        raise ValueError("no route")
    defender = PlayerState("D", 10**9, 0, buildings=list(buildings))
    attacker = PlayerState("A", 10**9, 0, roster=list(roster))
    totals = simulate_map(attacker, defender, path, round_number, cfg)
    return totals.hits, totals.damage, totals.killed, totals.cleared, len(path) - 1


def damage_profile(cfg: GameConfig, buildings: list[Building], path, minion_type: str) -> int:
    """Splash-only damage a single copy takes along `path` (closed form, no simulation).

    Guns are ignored here because their effect depends on the whole stream.
    """
    attackable = set(path[:-1])
    total = 0
    for b in buildings:
        if b.type == "wall":
            continue
        t = cfg.turrets[b.type]
        if t.aoe == 8:
            total += t.damage * sum((b.x + dx, b.y + dy) in attackable for dx in (-1, 0, 1) for dy in (-1, 0, 1) if (dx, dy) != (0, 0))
    return total


def simulate_leak(types, path, buildings, rules, *, profile=None, guns=None):
    """Exact one-map combat replay (same rules as gamekit.simulate_defense / the engine) that also
    returns the remaining HP of every copy that reached the base.

    Returns (hits, base_damage, leaked_hp_sum). Used as a smooth progress metric for gun planning:
    a turret that wounds a copy without killing it still lowers leaked_hp_sum.
    """
    from bot_research.harness import gamekit as gk
    ticks = rules.ticks
    L = len(path) - 1
    if profile is None:
        profile = gk.splash_profile(path, buildings, rules)
    if guns is None:
        guns = gk.gun_coverage(path, buildings, rules)
    schedule = [[] for _ in range(ticks)]
    for k, t in enumerate(types):
        schedule[k % ticks].append(t)
    minions = rules.minions
    entities = []
    hits = damage = leaked_hp = 0
    for tick in range(ticks):
        for t in schedule[tick]:
            m = minions[t]
            entities.append([m["hp"], m["damage"], tick])
        if not entities:
            continue
        survivors = []
        for e in entities:
            if e[2] < tick and tick - e[2] == L:
                hits += 1
                damage += e[1]
                leaked_hp += e[0]
                continue
            survivors.append(e)
        if not survivors:
            entities = survivors
            continue
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
        entities = alive
    return hits, damage, leaked_hp
