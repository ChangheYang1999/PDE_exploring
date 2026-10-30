from __future__ import annotations

from copy import deepcopy
from dataclasses import asdict
from typing import Any

from .actions import apply_action
from .combat import simulate_map
from .config import GameConfig
from .pathfinding import shortest_path
from .state import PlayerState

SCHEMA_VERSION = 1


class Engine:
    def __init__(self, config: GameConfig, names: tuple[str, str]):
        self.config = config
        self.players = [PlayerState(name, config.globals.initial_hp, config.globals.initial_gold) for name in names]
        if len(self.players) != 2:
            raise ValueError("exactly two player names required")
        self.round = 0
        self.result: dict | None = None

    def path(self, player: int) -> list[tuple[int, int]]:
        rules = self.config.globals
        path = shortest_path(rules.width, rules.height, ((b.x, b.y) for b in self.players[player].buildings), rules.spawn, rules.base)
        if path is None:
            raise RuntimeError("engine invariant violated: map has no path")
        return path

    def snapshot(self, player: int) -> dict:
        state = self.players[player]
        return {
            "name": state.name, "hp": state.hp, "gold": state.gold,
            "n_factories": state.n_factories,
            "n_turrets": sum(b.type != "wall" for b in state.buildings),
            "n_walls": sum(b.type == "wall" for b in state.buildings),
            "length_path": len(self.path(player)) - 1,
            "buildings": [asdict(b) for b in state.buildings],
            "roster": [dict(asdict(e), remaining_rounds=None if e.expires_after_round is None else e.expires_after_round - self.round) for e in state.roster],
        }

    def observation(self, player: int) -> dict:
        return {"round": self.round + 1, "player": player,
                "players": [self.snapshot(p) for p in (0, 1)], "rules": self.config.to_dict()}

    def records(self, events: list[list[dict]], metadata: dict | None = None) -> list[dict]:
        records = []
        for player in (0, 1):
            record = {"schema_version": SCHEMA_VERSION, "round": self.round,
                      "player": player, "event": events[player], "snapshot": self.snapshot(player)}
            if metadata is not None:
                record["match"] = metadata
            if self.result is not None:
                record["result"] = self.result
            records.append(record)
        return deepcopy(records)

    def initial_records(self, bot_specs: tuple[str, str]) -> list[dict]:
        if self.round != 0:
            raise ValueError("initial records only available before round 1")
        metadata = {"rules": self.config.to_dict(), "bots": list(bot_specs),
                    "protocol": "trusted Python decide(observation) -> list of JSON actions",
                    "neighbor_order": ["right", "down", "left", "up"],
                    "action_order": "A[0], B[0], A[1], B[1], ...",
                    "tick_order": ["spawn", "move older minions", "base hits", "turrets", "remove dead"]}
        return self.records([[{"kind": "initial"}], [{"kind": "initial"}]], metadata)

    def play_round(self, submissions: list[list[Any]], bot_errors: list[str | None] | None = None) -> list[dict]:
        if self.result is not None:
            raise ValueError("match is already finished")
        if len(submissions) != 2 or any(not isinstance(a, list) for a in submissions):
            raise ValueError("two action lists required")
        self.round += 1
        events = [[], []]
        for player, error in enumerate(bot_errors or [None, None]):
            if error:
                events[player].append({"kind": "bot_error", "reason": error})
        order = 0
        for index in range(max(map(len, submissions))):
            for player in (0, 1):
                if index < len(submissions[player]):
                    event = apply_action(self.players[player], submissions[player][index], self.round, self.config)
                    event["order"] = order
                    order += 1
                    events[player].append(event)
        paths = [self.path(p) for p in (0, 1)]
        # Complete BOTH maps even if a base falls during the first simulation.
        outgoing = [simulate_map(self.players[p], self.players[1-p], paths[1-p], self.round, self.config) for p in (0, 1)]
        rules = self.config.globals
        for p, state in enumerate(self.players):
            own, incoming = outgoing[p], outgoing[1-p]
            events[p].append({"kind": "combat", "outgoing_hits": own.hits, "incoming_hits": incoming.hits,
                              "damage_dealt": own.damage, "base_damage": incoming.damage,
                              "spawned": own.spawned, "killed": own.killed, "cleared": own.cleared})
            income = {"path": (len(paths[p]) - 1) * rules.path_income_per_step,
                      "factories": state.n_factories * rules.factory_income,
                      "hits": own.hits * rules.base_hit_bounty}
            income["total"] = sum(income.values())
            state.gold += income["total"]
            events[p].append({"kind": "income", **income})
            expired = [e.id for e in state.roster if e.expires_after_round is not None and e.expires_after_round <= self.round]
            expired_ids = set(expired)
            state.roster[:] = [e for e in state.roster if e.id not in expired_ids]
            if expired:
                events[p].append({"kind": "expiration", "roster_ids": expired})
        self.result = self._outcome()
        return self.records(events)

    def _outcome(self) -> dict | None:
        hp = [state.hp for state in self.players]
        if hp[0] <= 0 and hp[1] <= 0:
            return {"winner": None, "reason": "both_bases_destroyed"}
        if any(value <= 0 for value in hp):
            return {"winner": 0 if hp[1] <= 0 else 1, "reason": "base_destroyed"}
        if self.round >= self.config.globals.max_rounds:
            return {"winner": None if hp[0] == hp[1] else (0 if hp[0] > hp[1] else 1), "reason": "round_limit"}
        return None
