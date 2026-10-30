from __future__ import annotations

from dataclasses import dataclass, field

from td_game.logs import Frame, ReplayLog

from .utils import get


@dataclass
class PlayScene:
    name: str = ""
    hp: int = 0
    gold: int = 0
    n_factories: int = 0
    n_turrets: int = 0
    grid: list[list[str]] = field(default_factory=list)
    roster: list[dict] = field(default_factory=list)


@dataclass
class ViewScene:
    log: ReplayLog
    index: int = 0
    paused: bool = False
    verbose: bool = False
    speed_index: int = 2
    next_due: float = 0.0


def buildscene(frame: Frame, match: dict) -> list[PlayScene]:
    players = []
    symbols = {name: item["symbol"] for name, item in match["rules"]["turrets"].items()}
    symbols["wall"] = "#"
    for record in frame.records:
        snap = record["snapshot"]
        ps = PlayScene()
        ps.name = f"player{record['player']}"
        ps.hp = get(snap, "hp")
        ps.gold = get(snap, "gold")
        ps.n_factories = get(snap, "n_factories")
        ps.n_turrets = get(snap, "n_turrets")
        ps.grid = [["." for _ in range(12)] for _ in range(12)]
        for building in snap["buildings"]:
            ps.grid[building["y"]][building["x"]] = symbols[building["type"]]
        for field, symbol in (("spawn", "S"), ("base", "B")):
            x, y = match["rules"]["globals"][field]
            ps.grid[y][x] = symbol
        ps.roster = [dict(entry) for entry in snap["roster"]]
        for entry in ps.roster:
            expiry = entry["expires_after_round"]
            entry.setdefault("remaining_rounds", None if expiry is None else expiry - frame.round)
        players.append(ps)
    return players


def visible_events(vs: ViewScene) -> list[tuple[int, int, dict]]:
    # Derived from the visible prefix, never appended to a playback cache.
    return [(frame.round, p, event) for frame in vs.log.frames[:vs.index + 1]
            for p in (0, 1) for event in frame.records[p]["event"]]
