from __future__ import annotations

import unittest
from dataclasses import asdict
from pathlib import Path

from td_game.combat import Minion, combat_tick
from td_game.config import ConfigError, GlobalRules, balanced_config, config_from_dict, load_config
from td_game.engine import Engine
from td_game.state import Building, RosterEntry

ROOT = Path(__file__).resolve().parents[1]


class FinalRulesTests(unittest.TestCase):
    def test_final_catalogs_and_packaged_configs_match(self):
        cfg = balanced_config()
        self.assertEqual(cfg, load_config(ROOT / "configs/balanced.json"))
        self.assertEqual(cfg.globals, GlobalRules())
        self.assertFalse(cfg.demo)
        self.assertEqual((cfg.wall_cost, cfg.wall_damage, cfg.wall_range, cfg.wall_cooldown),
                         (1, 0, 0.0, 1))
        self.assertEqual({name: asdict(item) for name, item in cfg.minions.items()}, {
            "tier1": {"cost": 15, "hp": 20, "speed": 1.0, "damage": 5},
            "tier2": {"cost": 40, "hp": 70, "speed": 1.0, "damage": 12},
            "tier3": {"cost": 100, "hp": 180, "speed": 1.0, "damage": 26},
            "tier4": {"cost": 260, "hp": 560, "speed": 1.0, "damage": 60},
            "tier5": {"cost": 650, "hp": 1500, "speed": 1.0, "damage": 140},
        })
        self.assertEqual({name: asdict(item) for name, item in cfg.turrets.items()}, {
            "gun1": {"symbol": "1", "cost": 30, "damage": 8, "range": 2.5, "cooldown": 1, "aoe": 0},
            "gun2": {"symbol": "2", "cost": 80, "damage": 22, "range": 3.0, "cooldown": 1, "aoe": 0},
            "gun3": {"symbol": "3", "cost": 200, "damage": 55, "range": 3.5, "cooldown": 1, "aoe": 0},
            "splash": {"symbol": "X", "cost": 60, "damage": 10, "range": 0.0, "cooldown": 1, "aoe": 8},
        })

    def test_exact_global_defaults(self):
        self.assertEqual(asdict(GlobalRules()), {
            "width": 12, "height": 12, "spawn": (0, 0), "base": (11, 11),
            "initial_hp": 800, "initial_gold": 100, "max_rounds": 50,
            "ticks_per_round": 250, "roster_lifespan": 12,
            "factory_cost": 20, "factory_income": 15,
            "path_income_per_step": 1, "base_hit_bounty": 5,
        })

    def test_implicit_mechanic_defaults_match_explicit_config(self):
        cfg = balanced_config()
        data = cfg.to_dict()
        for name in ("wall_damage", "wall_range", "wall_cooldown"):
            del data[name]
        for item in data["minions"].values():
            del item["speed"]
        for item in data["turrets"].values():
            del item["cooldown"]
            if item["aoe"] == 0:
                del item["aoe"]
        self.assertEqual(config_from_dict(data), cfg)

    def test_unsupported_mechanic_values_are_not_silently_ignored(self):
        cases = [
            ("minions", "tier1", "speed", 0.5),
            ("minions", "tier1", "speed", True),
            ("turrets", "gun1", "cooldown", 2),
            ("turrets", "gun1", "cooldown", True),
            ("turrets", "splash", "aoe", 3),
            ("turrets", "splash", "aoe", True),
            ("turrets", "splash", "range", 1.0),
        ]
        for catalog, name, parameter, value in cases:
            data = balanced_config().to_dict()
            data[catalog][name][parameter] = value
            with self.subTest(parameter=parameter, value=value), self.assertRaises(ConfigError):
                config_from_dict(data)
        for parameter, value in (("wall_damage", 1), ("wall_range", 1.0), ("wall_cooldown", 2)):
            data = balanced_config().to_dict()
            data[parameter] = value
            with self.subTest(parameter=parameter), self.assertRaises(ConfigError):
                config_from_dict(data)

    def test_turret_tiers_strictly_increase_cost_damage_and_range(self):
        cfg = balanced_config()
        tiers = [cfg.turrets[name] for name in ("gun1", "gun2", "gun3")]
        for lower, higher in zip(tiers, tiers[1:]):
            self.assertLess(lower.cost, higher.cost)
            self.assertLess(lower.damage, higher.damage)
            self.assertLess(lower.range, higher.range)

    def test_premium_turret_reaches_targets_beyond_lower_tiers(self):
        cfg = balanced_config()
        for name in ("gun1", "gun2", "gun3"):
            with self.subTest(turret=name):
                engine = Engine(cfg, ("A", "B"))
                defender = engine.players[0]
                defender.buildings.append(Building(1, 3, name))
                copies = [Minion(i, 100, 5, 0) for i in (0, 1)]
                alive, totals = combat_tick(0, copies, [], engine.path(0), defender, cfg)
                loss = cfg.turrets[name].damage if name == "gun3" else 0
                self.assertEqual([copy.hp for copy in alive], [100 - loss, 100])
                self.assertEqual(totals.killed, 0)

    def test_all_final_minions_participate_in_purchase_round(self):
        engine = Engine(balanced_config(), ("A", "B"))
        engine.players[0].gold = 1065  # Fund all five tiers without changing the default starting gold.
        records = engine.play_round([[{"op": "buy_minion", "type": t} for t in engine.config.minions], []])
        combat = next(e for e in records[0]["event"] if e["kind"] == "combat")
        self.assertEqual(combat["outgoing_hits"], 5)
        self.assertEqual(combat["damage_dealt"], 243)
        self.assertEqual(records[1]["snapshot"]["hp"], 557)
        self.assertEqual(records[0]["snapshot"]["gold"], 47)
        self.assertEqual([e["type"] for e in records[0]["snapshot"]["roster"]], list(engine.config.minions))

    def test_splash_hits_exactly_the_eight_neighboring_cells_and_all_copies(self):
        cfg = balanced_config()
        defender = Engine(cfg, ("A", "B")).players[0]
        defender.buildings.append(Building(5, 5, "splash"))
        neighbors = {(-1, -1), (0, -1), (1, -1), (-1, 0),
                     (1, 0), (-1, 1), (0, 1), (1, 1)}
        for dx in range(-2, 3):
            for dy in range(-2, 3):
                with self.subTest(offset=(dx, dy)):
                    copies = [Minion(i, 100, 5, 0) for i in range(3)]
                    alive, totals = combat_tick(0, copies, [], [(5 + dx, 5 + dy)], defender, cfg)
                    expected_hp = 90 if (dx, dy) in neighbors else 100
                    self.assertEqual([copy.hp for copy in alive], [expected_hp] * 3)
                    self.assertEqual(totals.killed, 0)

    def test_splash_attacks_each_tick_including_spawn_and_stacks_with_guns(self):
        cfg = balanced_config()
        defender = Engine(cfg, ("A", "B")).players[0]
        defender.buildings = [Building(5, 5, "splash"), Building(4, 5, "gun1")]
        path = [(4, 4), (5, 4), (6, 4), (7, 4)]
        entries = [RosterEntry(0, "tier3", 1, 12)]
        alive, _ = combat_tick(0, [], entries, path, defender, cfg)
        self.assertEqual(alive[0].hp, 162)
        alive, _ = combat_tick(1, alive, [], path, defender, cfg)
        self.assertEqual(alive[0].hp, 144)


if __name__ == "__main__":
    unittest.main()
