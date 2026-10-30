"""Validate before mutating. A rejection never charges or leaves an obstacle."""
from __future__ import annotations

from dataclasses import asdict
from typing import Any

from .config import GameConfig
from .pathfinding import shortest_path
from .state import Building, PlayerState, RosterEntry


def apply_action(player: PlayerState, action: Any, round_number: int, config: GameConfig) -> dict:
    def reject(reason: str) -> dict:
        return {"kind": "action", "accepted": False, "action": action, "reason": reason}

    if not isinstance(action, dict):
        return reject("action must be an object")
    op = action.get("op")
    if not isinstance(op, str) or op not in ("buy_minion", "buy_factory", "build_turret", "build_wall"):
        return reject("unknown or missing op")
    type_name = action.get("type")
    if op in ("buy_minion", "build_turret"):
        catalog = config.minions if op == "buy_minion" else config.turrets
        if not isinstance(type_name, str) or type_name not in catalog:
            return reject(f"unknown or missing {op} type")
        cost = catalog[type_name].cost
    elif op == "buy_factory":
        cost = config.globals.factory_cost
    else:
        cost = config.wall_cost
    building = None
    if op.startswith("build_"):
        x, y = action.get("x"), action.get("y")
        if type(x) is not int or type(y) is not int:
            return reject("x and y must be integers")
        rules = config.globals
        if not (0 <= x < rules.width and 0 <= y < rules.height):
            return reject("building outside map")
        if (x, y) in (rules.spawn, rules.base):
            return reject("cannot build at spawn or base")
        blocked = {(b.x, b.y) for b in player.buildings}
        if (x, y) in blocked:
            return reject("cell already occupied")
        if shortest_path(rules.width, rules.height, blocked | {(x, y)}, rules.spawn, rules.base) is None:
            return reject("building would block every path")
        building = Building(x, y, "wall" if op == "build_wall" else type_name)
    if player.gold < cost:
        return reject("insufficient gold")
    event = {"kind": "action", "accepted": True, "action": action, "cost": cost}
    if op == "buy_minion":
        lifespan = config.globals.roster_lifespan
        entry = RosterEntry(player.next_roster_id, type_name, round_number,
                            round_number + lifespan - 1 if lifespan else None)
        player.roster.append(entry)
        player.next_roster_id += 1
        event["roster_entry"] = asdict(entry)
    elif op == "buy_factory":
        player.n_factories += 1
    else:
        player.buildings.append(building)
    player.gold -= cost
    return event
