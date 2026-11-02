"""Randomized equivalence check: bots/economy/fastsim.py vs td_game.combat.simulate_map.

Usage (from project root):
  PYTHONDONTWRITEBYTECODE=1 TMPDIR=$PWD/bot_research/tmp .venv/bin/python -B \
      -m bot_research.experiments.economy.check_fastsim [n_cases] [seed]
"""
from __future__ import annotations

import random
import sys
from copy import deepcopy

from td_game.combat import simulate_map
from td_game.config import balanced_config
from td_game.pathfinding import shortest_path
from td_game.state import Building, PlayerState, RosterEntry

from bot_research.bots.economy.fastsim import MapModel, simulate


def random_map(rng, n_build, turret_names):
    buildings = []
    blocked = set()
    tries = 0
    while len(buildings) < n_build and tries < 2000:
        tries += 1
        x, y = rng.randrange(12), rng.randrange(12)
        if (x, y) in ((0, 0), (11, 11)) or (x, y) in blocked:
            continue
        if shortest_path(12, 12, blocked | {(x, y)}, (0, 0), (11, 11)) is None:
            continue
        t = rng.choice(turret_names + ["wall"] * 2)
        buildings.append(Building(x, y, t))
        blocked.add((x, y))
    return buildings


def main():
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 300
    seed = int(sys.argv[2]) if len(sys.argv) > 2 else 1
    rng = random.Random(seed)
    config = balanced_config()
    rules = config.to_dict()
    tnames = list(config.turrets)
    mnames = list(config.minions)
    mismatches = 0
    for case in range(n):
        buildings = random_map(rng, rng.randrange(0, 70), tnames)
        defender = PlayerState("d", 800, 0, buildings=list(buildings))
        n_roster = rng.choice([1, 5, 30, 120, 260, 520, 700])
        roster = []
        for i in range(n_roster):
            bought = rng.randrange(1, 14)
            roster.append(RosterEntry(i, rng.choice(mnames), bought, bought + 11))
        attacker = PlayerState("a", 800, 0, roster=roster)
        rnd = rng.randrange(1, 14)
        path = shortest_path(12, 12, {(b.x, b.y) for b in buildings}, (0, 0), (11, 11))
        hp_before = defender.hp
        totals = simulate_map(attacker, defender, path, rnd, config)
        active_types = [e.type for e in roster if e.active(rnd)]
        model = MapModel([(b.x, b.y, b.type) for b in buildings], rules, path=path)
        hits, dmg = simulate(model, active_types, rules)
        if (hits, dmg) != (totals.hits, totals.damage) or hp_before - defender.hp != dmg:
            mismatches += 1
            print("MISMATCH case", case, (hits, dmg), (totals.hits, totals.damage))
    print(f"cases={n} seed={seed} mismatches={mismatches}")
    return 1 if mismatches else 0


if __name__ == "__main__":
    raise SystemExit(main())
