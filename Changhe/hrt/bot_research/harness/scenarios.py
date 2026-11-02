"""Scripted opening scenarios.

A scenario fixes both players' submissions for the first ``k`` rounds, which
produces a different (legal, engine-generated) starting position for the
bots, who take over from round ``k + 1``. The rules are never changed.

Scenario names
--------------
``mirror:SEED:K``  both players receive the same pseudo-random opening
                   (generated from SEED); the position stays symmetric.
``asym:SEED:K``    each player receives an independent opening
                   (seeds SEED*2+player); positions differ.
``eco:K``          both players buy only factories for K rounds.

The opening generator reads only the public observation (own gold and own
map) so every scripted action is legal or is rejected by the engine with a
recorded reason, exactly as for any bot.
"""
from __future__ import annotations

import random
from typing import Callable

from td_game.pathfinding import shortest_path


def _path(buildings):
    return shortest_path(12, 12, {(b["x"], b["y"]) for b in buildings}, (0, 0), (11, 11))


def random_opening_actions(observation: dict, seed: int) -> list[dict]:
    me = observation["players"][observation["player"]]
    rng = random.Random(seed * 1000003 + observation["round"])
    gold = me["gold"]
    actions: list[dict] = []
    blocked = {(b["x"], b["y"]) for b in me["buildings"]}
    weights = {"factory": rng.random(), "walls": rng.random() * 0.5, "turret": rng.random() * 0.7,
               "minion": rng.random() * 0.6}
    total = sum(weights.values())
    budget = {k: gold * w / total for k, w in weights.items()}
    # Walls on random free cells that keep a route open.
    for _ in range(int(budget["walls"])):
        x, y = rng.randrange(12), rng.randrange(12)
        if (x, y) in blocked or (x, y) in ((0, 0), (11, 11)):
            continue
        if shortest_path(12, 12, blocked | {(x, y)}, (0, 0), (11, 11)) is None:
            continue
        blocked.add((x, y))
        actions.append({"op": "build_wall", "x": x, "y": y})
        gold -= 1
    # One turret adjacent to the current route.
    turret_cost = {"gun1": 30, "gun2": 80, "splash": 60}
    kind = rng.choice(list(turret_cost))
    if budget["turret"] >= turret_cost[kind] and gold >= turret_cost[kind]:
        route = shortest_path(12, 12, blocked, (0, 0), (11, 11)) or []
        candidates = sorted({(x + dx, y + dy) for x, y in route for dx in (-1, 0, 1) for dy in (-1, 0, 1)
                             if 0 <= x + dx < 12 and 0 <= y + dy < 12} - blocked - {(0, 0), (11, 11)})
        rng.shuffle(candidates)
        for x, y in candidates:
            if shortest_path(12, 12, blocked | {(x, y)}, (0, 0), (11, 11)) is not None:
                actions.append({"op": "build_turret", "type": kind, "x": x, "y": y})
                blocked.add((x, y))
                gold -= turret_cost[kind]
                break
    # Minions.
    minion_budget = min(budget["minion"], gold)
    while minion_budget >= 15:
        kind = "tier2" if minion_budget >= 40 and rng.random() < 0.4 else "tier1"
        cost = 40 if kind == "tier2" else 15
        actions.append({"op": "buy_minion", "type": kind})
        minion_budget -= cost
        gold -= cost
    while gold >= 20:
        actions.append({"op": "buy_factory"})
        gold -= 20
    return actions


def make_overrides(name: str) -> tuple[Callable[[dict], list | None], Callable[[dict], list | None]]:
    parts = name.split(":")
    kind = parts[0]
    if kind == "eco":
        k = int(parts[1])

        def eco(observation):
            if observation["round"] > k:
                return None
            gold = observation["players"][observation["player"]]["gold"]
            return [{"op": "buy_factory"}] * (gold // 20)

        return eco, eco
    if kind in ("mirror", "asym"):
        seed, k = int(parts[1]), int(parts[2])

        def make(player):
            def override(observation):
                if observation["round"] > k:
                    return None
                s = seed if kind == "mirror" else seed * 2 + player
                return random_opening_actions(observation, s)
            return override

        return make(0), make(1)
    raise ValueError(f"unknown scenario {name!r}")
