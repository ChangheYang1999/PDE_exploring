"""Standalone snapshot reader: imports no engine, BFS, configuration, or bots."""
from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any


class LogError(ValueError):
    pass


@dataclass
class Frame:
    round: int
    records: tuple[dict, dict]


@dataclass
class ReplayLog:
    frames: list[Frame]
    match: dict
    result: dict | None


def load_log(path: str | Path) -> ReplayLog:
    path = Path(path)
    grouped: dict[int, dict[int, dict]] = {}
    locations: dict[tuple[int, int], int] = {}

    def fail(line: int, message: str):
        raise LogError(f"{path}: line {line}: {message}")

    def reject_constant(value):
        raise ValueError(f"nonfinite JSON value {value}")

    def unique_object(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                raise ValueError(f"duplicate JSON field {key!r}")
            result[key] = value
        return result

    try:
        with path.open(encoding="utf-8") as stream:
            for line, text in enumerate(stream, 1):
                try:
                    record = json.loads(text, parse_constant=reject_constant, object_pairs_hook=unique_object)
                except (json.JSONDecodeError, ValueError) as exc:
                    fail(line, f"malformed JSON: {exc}")
                if not isinstance(record, dict):
                    fail(line, "record must be an object")
                for key in ("schema_version", "round", "player", "event", "snapshot"):
                    if key not in record:
                        fail(line, f"missing {key}")
                if type(record["schema_version"]) is not int or record["schema_version"] != 1:
                    fail(line, f"unsupported schema_version {record['schema_version']!r}")
                r, p = record["round"], record["player"]
                if type(r) is not int or r < 0 or type(p) is not int or p not in (0, 1):
                    fail(line, "round must be nonnegative integer and player must be 0 or 1")
                if p in grouped.setdefault(r, {}):
                    fail(line, f"duplicate (round={r}, player={p}); first seen on line {locations[r, p]}")
                if not isinstance(record["event"], list) or any(not isinstance(e, dict) or not isinstance(e.get("kind"), str) for e in record["event"]):
                    fail(line, "event must be a list of objects with a kind string")
                if not isinstance(record["snapshot"], dict):
                    fail(line, "snapshot must be an object")
                grouped[r][p] = record
                locations[r, p] = line
    except (OSError, UnicodeError) as exc:
        raise LogError(f"cannot read {path}: {exc}") from exc
    if not grouped:
        raise LogError(f"{path}: empty log")
    rounds = sorted(grouped)
    if any(r != index for index, r in enumerate(rounds)):
        raise LogError(f"{path}: missing round(s); frames must start at round 0 and be consecutive")
    for r, pair in grouped.items():
        if set(pair) != {0, 1}:
            p = next(iter(pair))
            fail(locations[r, p], f"round {r} missing partner player {1-p}")
    metadata = grouped[0][0].get("match")
    if not isinstance(metadata, dict) or grouped[0][1].get("match") != metadata:
        fail(locations[0, 0], "round 0 requires matching match metadata for both players")
    rules = metadata.get("rules")
    if not isinstance(rules, dict) or not isinstance(rules.get("globals"), dict):
        fail(locations[0, 0], "match.rules.globals missing")
    if (rules["globals"].get("width"), rules["globals"].get("height")) != (12, 12):
        fail(locations[0, 0], "version 1 replay requires 12x12 maps")
    for catalog in ("turrets", "minions"):
        if not isinstance(rules.get(catalog), dict) or not rules[catalog]:
            fail(locations[0, 0], f"match.rules.{catalog} missing or empty")
    for name, definition in rules["turrets"].items():
        symbol = definition.get("symbol") if isinstance(definition, dict) else None
        if not isinstance(symbol, str) or len(symbol) != 1 or not symbol.isascii() or not symbol.isalnum():
            fail(locations[0, 0], f"invalid display symbol for turret {name}")
    names = []
    for r in rounds:
        for p in (0, 1):
            record = grouped[r][p]
            line = locations[r, p]
            snap = record["snapshot"]
            for event in record["event"]:
                if event["kind"] in ("combat", "income"):
                    keys = ("outgoing_hits", "incoming_hits", "damage_dealt", "base_damage", "spawned", "killed", "cleared") if event["kind"] == "combat" else ("path", "factories", "hits", "total")
                    for key in keys:
                        if key in event and (type(event[key]) is not int or event[key] < 0):
                            fail(line, f"{event['kind']}.{key} must be a nonnegative integer")
                elif event["kind"] == "expiration":
                    if not isinstance(event.get("roster_ids"), list):
                        fail(line, "expiration.roster_ids must be a list")
                elif event["kind"] == "action":
                    if type(event.get("accepted")) is not bool or "action" not in event:
                        fail(line, "action event requires action and boolean accepted")
            for key in ("name", "hp", "gold", "n_factories", "n_turrets", "length_path", "buildings", "roster"):
                if key not in snap:
                    fail(line, f"snapshot missing {key}")
            if not isinstance(snap["name"], str):
                fail(line, "snapshot.name must be a string")
            if r == 0:
                names.append(snap["name"])
            elif snap["name"] != names[p]:
                fail(line, f"player {p} identity changed")
            for key in ("hp", "gold", "n_factories", "n_turrets", "length_path"):
                if type(snap[key]) is not int or (key != "hp" and snap[key] < 0):
                    fail(line, f"snapshot.{key} must be {'an' if key == 'hp' else 'a nonnegative'} integer")
            if not isinstance(snap["buildings"], list) or not isinstance(snap["roster"], list):
                fail(line, "buildings and roster must be lists")
            occupied = set()
            turret_count = 0
            for b in snap["buildings"]:
                if not isinstance(b, dict) or not all(key in b for key in ("x", "y", "type")):
                    fail(line, "building requires x, y, type")
                x, y, kind = b["x"], b["y"], b["type"]
                if type(x) is not int or type(y) is not int or not (0 <= x < 12 and 0 <= y < 12):
                    fail(line, "building coordinates outside 12x12 map")
                if (x, y) in occupied or (x, y) in ((0, 0), (11, 11)):
                    fail(line, "overlapping building or building on spawn/base")
                if not isinstance(kind, str) or (kind != "wall" and kind not in rules["turrets"]):
                    fail(line, "unknown building type")
                occupied.add((x, y))
                turret_count += kind != "wall"
            if snap["n_turrets"] != turret_count:
                fail(line, "n_turrets disagrees with sparse buildings")
            roster_ids = set()
            for e in snap["roster"]:
                if not isinstance(e, dict) or not all(key in e for key in ("id", "type", "bought_round", "expires_after_round")):
                    fail(line, "roster entry requires id, type, bought_round, expires_after_round")
                if type(e["id"]) is not int or e["id"] < 0 or e["id"] in roster_ids:
                    fail(line, "roster ID must be unique nonnegative integer per player")
                if not isinstance(e["type"], str) or e["type"] not in rules["minions"]:
                    fail(line, "unknown minion type")
                if type(e["bought_round"]) is not int or not (1 <= e["bought_round"] <= r):
                    fail(line, "invalid roster purchase round")
                expiry = e["expires_after_round"]
                if expiry is not None and (type(expiry) is not int or expiry <= r):
                    fail(line, "round-end roster contains expired entry")
                if "remaining_rounds" in e and e["remaining_rounds"] != (None if expiry is None else expiry - r):
                    fail(line, "remaining_rounds disagrees with roster expiry")
                roster_ids.add(e["id"])
            if "result" in record:
                result = record["result"]
                if r != rounds[-1] or not isinstance(result, dict) or "winner" not in result or not isinstance(result.get("reason"), str):
                    fail(line, "result must identify winner and reason on final frame only")
                if result["winner"] is not None and (type(result["winner"]) is not int or result["winner"] not in (0, 1)):
                    fail(line, "result.winner must be 0, 1, or null (draw)")
    final = grouped[rounds[-1]]
    if final[0].get("result") != final[1].get("result"):
        fail(locations[rounds[-1], 1], "final results do not agree")
    return ReplayLog([Frame(r, (grouped[r][0], grouped[r][1])) for r in rounds], metadata, final[0].get("result"))
