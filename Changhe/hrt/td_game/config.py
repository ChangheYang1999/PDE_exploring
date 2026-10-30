"""Validated JSON rules and the bundled game configuration."""
from __future__ import annotations

import json
import math
from dataclasses import asdict, dataclass, field
from importlib.resources import files
from pathlib import Path
from typing import Any


class ConfigError(ValueError):
    pass


@dataclass(frozen=True)
class GlobalRules:
    width: int = 12
    height: int = 12
    spawn: tuple[int, int] = (0, 0)
    base: tuple[int, int] = (11, 11)
    initial_hp: int = 800
    initial_gold: int = 100
    max_rounds: int = 50
    ticks_per_round: int = 250
    roster_lifespan: int = 12
    factory_cost: int = 20
    factory_income: int = 15
    path_income_per_step: int = 1
    base_hit_bounty: int = 5


@dataclass(frozen=True)
class MinionType:
    cost: int
    hp: int
    damage: int
    speed: float = 1.0


@dataclass(frozen=True)
class TurretType:
    symbol: str
    cost: int
    damage: int
    range: float
    cooldown: int = 1
    aoe: int = 0


@dataclass(frozen=True)
class GameConfig:
    label: str
    demo: bool
    wall_cost: int
    minions: dict[str, MinionType]
    turrets: dict[str, TurretType]
    globals: GlobalRules = field(default_factory=GlobalRules)
    wall_damage: int = 0
    wall_range: float = 0.0
    wall_cooldown: int = 1

    def to_dict(self) -> dict[str, Any]:
        # JSON normalization makes metadata and observations portable.
        return json.loads(json.dumps(asdict(self)))


def _integer(value: Any, name: str, minimum: int = 0) -> None:
    if type(value) is not int or value < minimum:
        raise ConfigError(f"{name} must be an integer >= {minimum}")


def config_from_dict(data: dict[str, Any]) -> GameConfig:
    if not isinstance(data, dict):
        raise ConfigError("configuration must be a JSON object")
    for key in ("minions", "turrets", "wall_cost"):
        if key not in data:
            raise ConfigError(f"missing required rule parameter: {key}; select --balanced for bundled rules")
    raw_globals = data.get("globals", {})
    if not isinstance(raw_globals, dict):
        raise ConfigError("globals must be an object")
    try:
        converted = dict(raw_globals)
        for key in ("spawn", "base"):
            if key in converted:
                converted[key] = tuple(converted[key])
        rules = GlobalRules(**converted)
    except (TypeError, ValueError) as exc:
        raise ConfigError(f"invalid globals: {exc}") from exc
    for key, value in asdict(rules).items():
        if key not in ("spawn", "base"):
            _integer(value, key, 1 if key in ("width", "height", "initial_hp", "max_rounds", "ticks_per_round") else 0)
    for key in ("spawn", "base"):
        point = getattr(rules, key)
        if len(point) != 2 or any(type(value) is not int for value in point):
            raise ConfigError(f"{key} must contain two integer coordinates")
    if (rules.width, rules.height, rules.spawn, rules.base) != (12, 12, (0, 0), (11, 11)):
        raise ConfigError("version 1 supports a 12x12 map, spawn (0,0), base (11,11)")
    _integer(data["wall_cost"], "wall_cost")
    wall_parameters = {}
    for key, expected in (("wall_damage", 0), ("wall_range", 0.0), ("wall_cooldown", 1)):
        value = data.get(key, expected)
        allowed_types = (int, float) if key == "wall_range" else (int,)
        if type(value) not in allowed_types or value != expected:
            raise ConfigError(f"{key} must be {expected}; walls do not attack")
        wall_parameters[key] = value
    minions, turrets = {}, {}
    for catalog, cls, target in (("minions", MinionType, minions), ("turrets", TurretType, turrets)):
        entries = data[catalog]
        if not isinstance(entries, dict) or not entries:
            raise ConfigError(f"{catalog} must be a nonempty object")
        for name, definition in entries.items():
            if not isinstance(name, str) or not name or name == "wall":
                raise ConfigError(f"invalid {catalog} type name: {name!r}")
            try:
                item = cls(**definition)
            except (TypeError, ValueError) as exc:
                raise ConfigError(f"invalid {catalog}.{name}: {exc}") from exc
            _integer(item.cost, f"{catalog}.{name}.cost")
            _integer(item.damage, f"{catalog}.{name}.damage")
            if catalog == "minions":
                _integer(item.hp, f"{catalog}.{name}.hp", 1)
                if type(item.speed) not in (int, float) or item.speed != 1.0:
                    raise ConfigError(f"minions.{name}.speed must be 1.0 (one cell per tick)")
            else:
                if type(item.range) not in (int, float) or not math.isfinite(item.range) or item.range < 0:
                    raise ConfigError(f"turrets.{name}.range must be finite and nonnegative")
                if not isinstance(item.symbol, str) or len(item.symbol) != 1 or not item.symbol.isascii() or not item.symbol.isalnum():
                    raise ConfigError(f"turrets.{name}.symbol must be one ASCII letter or digit")
                if type(item.cooldown) is not int or item.cooldown != 1:
                    raise ConfigError(f"turrets.{name}.cooldown must be 1 (attacks every tick)")
                if type(item.aoe) is not int or item.aoe not in (0, 8):
                    raise ConfigError(f"turrets.{name}.aoe must be 0 or 8")
                if item.aoe == 8 and item.range != 0.0:
                    raise ConfigError(f"turrets.{name}.range must be 0.0 for the eight-neighbor AOE")
            target[name] = item
    if type(data.get("demo", False)) is not bool:
        raise ConfigError("demo must be a boolean")
    label = data.get("label", "custom rules")
    if not isinstance(label, str):
        raise ConfigError("label must be a string")
    return GameConfig(label, data.get("demo", False), data["wall_cost"], minions, turrets, rules, **wall_parameters)


def load_config(path: str | Path) -> GameConfig:
    try:
        return config_from_dict(json.loads(Path(path).read_text(encoding="utf-8")))
    except (OSError, json.JSONDecodeError) as exc:
        raise ConfigError(f"cannot load configuration {path}: {exc}") from exc


def balanced_config() -> GameConfig:
    return config_from_dict(json.loads(files("td_game").joinpath("balanced.json").read_text(encoding="utf-8")))
