"""The fast local simulator must agree exactly with the engine's simulate_map."""
from __future__ import annotations

import random
import unittest

from td_game.config import balanced_config
from td_game.pathfinding import shortest_path

from bot_research.harness import gamekit


def random_map(rng: random.Random, n_buildings: int) -> list[dict]:
    blocked: set = set()
    buildings = []
    kinds = ["wall", "wall", "gun1", "gun2", "gun3", "splash", "splash"]
    attempts = 0
    while len(buildings) < n_buildings and attempts < 2000:
        attempts += 1
        cell = (rng.randrange(12), rng.randrange(12))
        if not gamekit.legal_build(blocked, cell):
            continue
        blocked.add(cell)
        buildings.append({"x": cell[0], "y": cell[1], "type": rng.choice(kinds)})
    return buildings


class FastSimulatorAgreement(unittest.TestCase):
    def test_random_maps_and_rosters(self):
        cfg = balanced_config()
        rules = gamekit.Rules.from_observation({"rules": cfg.to_dict()})
        rng = random.Random(12345)
        types = list(cfg.minions)
        for case in range(60):
            buildings = random_map(rng, rng.randrange(0, 60))
            n = rng.choice([1, 3, 10, 40, 120, 260, 520])
            roster = [rng.choice(types) for _ in range(n)]
            path = shortest_path(12, 12, gamekit.cells_of(buildings), (0, 0), (11, 11))
            fast = gamekit.simulate_defense(roster, path, buildings, rules)
            ref = gamekit.engine_simulate_defense(roster, buildings, cfg)
            with self.subTest(case=case, n=n, buildings=len(buildings)):
                self.assertEqual((fast.hits, fast.damage, fast.killed, fast.spawned, fast.cleared),
                                 (ref.hits, ref.damage, ref.killed, ref.spawned, ref.cleared))

    def test_route_matches_engine_path(self):
        rng = random.Random(7)
        for _ in range(50):
            buildings = random_map(rng, rng.randrange(0, 70))
            self.assertEqual(gamekit.route(gamekit.cells_of(buildings)),
                             shortest_path(12, 12, gamekit.cells_of(buildings), (0, 0), (11, 11)))


if __name__ == "__main__":
    unittest.main()
