"""Ephemeral combat copies; no tick state is persisted in snapshots or logs."""
from __future__ import annotations

from dataclasses import dataclass

from .config import GameConfig
from .state import PlayerState, RosterEntry


@dataclass
class Minion:
    roster_id: int
    hp: int
    damage: int
    born_tick: int
    path_index: int = 0


@dataclass
class CombatTotals:
    hits: int = 0
    damage: int = 0
    spawned: int = 0
    killed: int = 0
    cleared: int = 0


def spawn_schedule(roster: list[RosterEntry], round_number: int, ticks: int) -> list[list[RosterEntry]]:
    schedule = [[] for _ in range(ticks)]
    active = [entry for entry in roster if entry.active(round_number)]
    for k, entry in enumerate(active):
        schedule[k % ticks].append(entry)
    return schedule


def combat_tick(
    tick: int, entities: list[Minion], spawning: list[RosterEntry],
    path: list[tuple[int, int]], defender: PlayerState, config: GameConfig,
) -> tuple[list[Minion], CombatTotals]:
    """Spawn, move older copies, resolve arrival, attack, then remove deaths."""
    totals = CombatTotals(spawned=len(spawning))
    entities.extend(Minion(e.id, config.minions[e.type].hp, config.minions[e.type].damage, tick) for e in spawning)
    survivors = []
    for entity in entities:
        if entity.born_tick < tick:
            entity.path_index += 1
            if entity.path_index == len(path) - 1:
                defender.hp -= entity.damage
                totals.hits += 1
                totals.damage += entity.damage
                continue
        survivors.append(entity)
    turrets = [(b, config.turrets[b.type]) for b in defender.buildings if b.type != "wall"]
    damage = [0] * len(survivors)
    for building, turret in turrets:
        target = None
        for index, entity in enumerate(survivors):
            x, y = path[entity.path_index]
            dx, dy = x - building.x, y - building.y
            if turret.aoe == 8:
                if max(abs(dx), abs(dy)) == 1:
                    damage[index] += turret.damage
            elif dx**2 + dy**2 <= turret.range**2:
                # Progress along the route determines the frontmost target.
                # Equal progress retains the stable spawn order.
                if target is None or entity.path_index > survivors[target].path_index:
                    target = index
        if target is not None:
            damage[target] += turret.damage
    # All turrets select before damage/death resolution, as in the tick order.
    for entity, amount in zip(survivors, damage):
        entity.hp -= amount
    alive = [entity for entity in survivors if entity.hp > 0]
    totals.killed = len(survivors) - len(alive)
    return alive, totals


def simulate_map(
    attacker: PlayerState, defender: PlayerState, path: list[tuple[int, int]],
    round_number: int, config: GameConfig,
) -> CombatTotals:
    schedule = spawn_schedule(attacker.roster, round_number, config.globals.ticks_per_round)
    entities = []
    totals = CombatTotals()
    for tick, spawning in enumerate(schedule):
        entities, current = combat_tick(tick, entities, spawning, path, defender, config)
        for field in ("hits", "damage", "spawned", "killed"):
            setattr(totals, field, getattr(totals, field) + getattr(current, field))
    totals.cleared = len(entities)
    # Entities go out of scope; next round creates fresh full-HP copies.
    return totals
