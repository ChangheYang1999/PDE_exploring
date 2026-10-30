from __future__ import annotations

import json
import unittest
from pathlib import Path

from td_bots.protocol import collect_actions
from td_game.actions import apply_action
from td_game.combat import Minion, combat_tick, simulate_map, spawn_schedule
from td_game.config import ConfigError, GlobalRules, config_from_dict, balanced_config, load_config
from td_game.engine import Engine
from td_game.pathfinding import shortest_path
from td_game.state import Building, PlayerState, RosterEntry

ROOT = Path(__file__).resolve().parents[1]


def config(**globals):
    data = balanced_config().to_dict()
    data["globals"].update(globals)
    return config_from_dict(data)


def minion(type_name="tier1"):
    return {"op": "buy_minion", "type": type_name}


def wall(x, y):
    return {"op": "build_wall", "x": x, "y": y}


def event(records, player, kind):
    return next(e for e in records[player]["event"] if e["kind"] == kind)


class ConfigTests(unittest.TestCase):
    def test_bundled_config_preserves_all_global_defaults(self):
        cfg = load_config(ROOT / "configs/balanced.json")
        self.assertEqual(cfg.globals, GlobalRules())
        self.assertEqual(cfg, balanced_config())
        self.assertFalse(cfg.demo)
        self.assertEqual(cfg.turrets["gun1"].symbol, "1")

    def test_missing_rule_parameters_are_rejected(self):
        for key in ("minions", "turrets", "wall_cost"):
            data = balanced_config().to_dict()
            del data[key]
            with self.subTest(key=key), self.assertRaisesRegex(ConfigError, key):
                config_from_dict(data)

    def test_invalid_balance_is_rejected(self):
        cases = [("wall_cost", -1), ("wall_cost", True), ("minions", {}), ("turrets", {})]
        for key, value in cases:
            data = balanced_config().to_dict()
            data[key] = value
            with self.subTest(key=key, value=value), self.assertRaises(ConfigError):
                config_from_dict(data)
        data = balanced_config().to_dict()
        data["turrets"]["gun1"]["range"] = float("nan")
        with self.assertRaises(ConfigError):
            config_from_dict(data)


class PathActionTests(unittest.TestCase):
    def setUp(self):
        self.cfg = balanced_config()
        self.player = PlayerState("A", 800, 100)

    def test_empty_path_and_stable_tie_breaking(self):
        expected = [(x, 0) for x in range(12)] + [(11, y) for y in range(1, 12)]
        self.assertEqual(shortest_path(12, 12, [], (0, 0), (11, 11)), expected)
        self.assertEqual(len(expected) - 1, 22)
        blocked = [(2, 0), (1, 1)]
        self.assertEqual(shortest_path(12, 12, blocked, (0, 0), (11, 11)),
                         shortest_path(12, 12, reversed(blocked), (0, 0), (11, 11)))

    def test_invalid_construction_has_no_side_effects(self):
        self.assertTrue(apply_action(self.player, wall(1, 0), 1, self.cfg)["accepted"])
        invalid = [wall(0, 0), wall(11, 11), wall(-1, 3), wall(12, 0), wall(1, 0), wall(0, 1),
                   wall(True, 3), wall(2.0, 3), {"op": "build_wall", "x": 4},
                   {"op": "build_turret", "type": "nope", "x": 3, "y": 3}]
        for action in invalid:
            before = (self.player.gold, list(self.player.buildings), list(self.player.roster))
            result = apply_action(self.player, action, 1, self.cfg)
            with self.subTest(action=action):
                self.assertFalse(result["accepted"])
                self.assertTrue(result["reason"])
                self.assertEqual(before, (self.player.gold, self.player.buildings, self.player.roster))
        self.assertTrue(apply_action(self.player, wall(2, 2), 1, self.cfg)["accepted"])

    def test_malformed_actions_and_later_valid_action(self):
        engine = Engine(self.cfg, ("A", "B"))
        invalid = [None, 4, [], {}, {"op": []}, {"op": "sell"},
                   {"op": "buy_minion", "type": []}, {"op": "buy_minion"}]
        records = engine.play_round([invalid + [{"op": "buy_factory"}], []])
        actions = [e for e in records[0]["event"] if e["kind"] == "action"]
        self.assertTrue(all(not e["accepted"] for e in actions[:-1]))
        self.assertTrue(actions[-1]["accepted"])
        self.assertEqual(engine.players[0].n_factories, 1)
        self.assertEqual(engine.players[0].gold, 100 - 20 + 22 + 15)

    def test_insufficient_gold_rejects_only_current_action(self):
        self.player.gold = 5
        self.assertFalse(apply_action(self.player, minion(), 1, self.cfg)["accepted"])
        self.assertEqual(self.player.gold, 5)
        self.assertTrue(apply_action(self.player, wall(3, 3), 1, self.cfg)["accepted"])
        self.assertEqual(self.player.gold, 4)

    def test_interleaved_submission_order(self):
        engine = Engine(self.cfg, ("A", "B"))
        records = engine.play_round([[wall(2, 2), minion(), minion()], [{"op": "buy_factory"}, minion()]])
        ordered = sorted((e["order"], p, e["action"]["op"]) for p in (0, 1)
                         for e in records[p]["event"] if e["kind"] == "action")
        self.assertEqual(ordered, [(0, 0, "build_wall"), (1, 1, "buy_factory"),
                                   (2, 0, "buy_minion"), (3, 1, "buy_minion"), (4, 0, "buy_minion")])


class DecisionTests(unittest.TestCase):
    def test_both_decide_from_isolated_pre_action_state(self):
        engine = Engine(balanced_config(), ("A", "B"))
        seen = []

        class Mutator:
            def decide(self, obs):
                seen.append((obs["round"], obs["players"][0]["gold"]))
                obs["players"][0]["gold"] = 999999
                obs["players"][1]["buildings"].append({"x": 0, "y": 0, "type": "wall"})
                obs["rules"]["globals"]["factory_cost"] = 0
                return [{"op": "buy_factory"}]

        class Observer:
            def decide(self, obs):
                seen.append((obs["round"], obs["players"][0]["gold"]))
                self_outer.assertEqual(obs["players"][0]["n_factories"], 0)
                self_outer.assertEqual(obs["players"][1]["buildings"], [])
                self_outer.assertEqual(obs["rules"]["globals"]["factory_cost"], 20)
                self_outer.assertNotIn("actions", obs)
                return []

        self_outer = self
        actions, errors = collect_actions([Mutator(), Observer()], [engine.observation(0), engine.observation(1)])
        self.assertEqual(errors, [None, None])
        self.assertEqual(seen, [(1, 100), (1, 100)])
        self.assertEqual(engine.players[0].gold, 100)
        self.assertEqual(engine.players[0].n_factories, 0)
        self.assertEqual(engine.players[1].buildings, [])
        records = engine.play_round(actions, errors)
        self.assertEqual(records[0]["snapshot"]["n_factories"], 1)

    def test_bot_errors_are_recorded_and_individual_invalid_actions_continue(self):
        class Bad:
            def decide(self, obs):
                raise RuntimeError("broken")

        class Valid:
            def decide(self, obs):
                return [None, {"op": "buy_factory"}]

        engine = Engine(balanced_config(), ("A", "B"))
        actions, errors = collect_actions([Bad(), Valid()], [engine.observation(p) for p in (0, 1)])
        records = engine.play_round(actions, errors)
        self.assertIn("RuntimeError: broken", event(records, 0, "bot_error")["reason"])
        self.assertEqual(records[1]["snapshot"]["n_factories"], 1)
        self.assertFalse(event(records, 1, "action")["accepted"])

    def test_entire_unparseable_return_becomes_empty(self):
        for value in ({}, [object()], [float("nan")]):
            class Bad:
                def decide(self, obs):
                    return value
            actions, errors = collect_actions([Bad(), Bad()], [{}, {}])
            with self.subTest(value=value):
                self.assertEqual(actions, [[], []])
                self.assertTrue(all(errors))


class CombatTests(unittest.TestCase):
    def setUp(self):
        self.cfg = balanced_config()
        self.defender = PlayerState("D", 800, 100)
        self.path = shortest_path(12, 12, [], (0, 0), (11, 11))
        self.entry = RosterEntry(0, "tier1", 1, 12)

    def test_spawn_stays_then_steps_and_minions_share_cells(self):
        entries = [self.entry, RosterEntry(1, "tier1", 1, 12)]
        entities, stats = combat_tick(0, [], entries, self.path, self.defender, self.cfg)
        self.assertEqual([e.path_index for e in entities], [0, 0])
        self.assertEqual(stats.hits, 0)
        entities, _ = combat_tick(1, entities, [], self.path, self.defender, self.cfg)
        self.assertEqual([e.path_index for e in entities], [1, 1])

    def test_arrival_tick_249_hits_but_250_does_not(self):
        data = self.cfg.to_dict()
        data["minions"]["dummy"] = {"cost": 0, "hp": 1, "damage": 0}
        cfg = config_from_dict(data)
        for spawn_tick, expected in ((227, 5), (228, 0), (249, 0)):
            roster = [RosterEntry(i, "dummy", 1, 12) for i in range(spawn_tick)]
            roster.append(RosterEntry(spawn_tick, "tier1", 1, 12))
            defender = PlayerState("D", 800, 100)
            totals = simulate_map(PlayerState("A", 800, 100, roster=roster), defender, self.path, 1, cfg)
            with self.subTest(spawn_tick=spawn_tick):
                self.assertEqual(defender.hp, 800 - expected)
                self.assertEqual(totals.damage, expected)
                self.assertEqual(totals.cleared, max(0, len(roster) - 228))
        entities, _ = combat_tick(249, [], [self.entry], self.path, self.defender, self.cfg)
        self.assertEqual(entities[0].path_index, 0)

    def test_modulo_schedule_and_reindex_after_filtering(self):
        roster = [RosterEntry(-1, "tier1", 1, 1)] + [RosterEntry(i, "tier1", 1, None) for i in range(251)]
        schedule = spawn_schedule(roster, 2, 250)
        self.assertEqual([e.id for e in schedule[0]], [0, 250])
        self.assertEqual([e.id for e in schedule[249]], [249])
        totals = simulate_map(PlayerState("A", 800, 100, roster=roster), self.defender, self.path, 2, self.cfg)
        self.assertEqual((totals.spawned, totals.hits, totals.cleared), (251, 229, 22))

    def test_euclidean_boundary_single_target_and_spawn_tick_attack(self):
        data = self.cfg.to_dict()
        data["turrets"]["gun1"].update(range=5.0, damage=30)
        cfg = config_from_dict(data)
        self.defender.buildings.append(Building(3, 4, "gun1"))
        entries = [self.entry, RosterEntry(1, "tier1", 1, 12)]
        entities, totals = combat_tick(0, [], entries, self.path, self.defender, cfg)
        self.assertEqual([(e.roster_id, e.hp) for e in entities], [(1, 20)])
        self.assertEqual(totals.killed, 1)
        data["turrets"]["gun1"]["range"] = 4.99
        entities, totals = combat_tick(0, [], [self.entry], self.path, self.defender, config_from_dict(data))
        self.assertEqual(entities[0].hp, 20)
        self.assertEqual(totals.killed, 0)

    def test_guns_target_furthest_progress_in_range(self):
        for name in ("gun1", "gun2", "gun3"):
            with self.subTest(turret=name):
                self.defender.buildings = [Building(9, 1, name)]
                # The rear copy is closer to the gun; the globally foremost
                # copy is outside range. Only the frontmost in range is hit.
                copies = [Minion(0, 100, 5, 5, 9),
                          Minion(1, 100, 5, 5, 18),
                          Minion(2, 100, 5, 5, 13)]
                entities, totals = combat_tick(5, copies, [], self.path, self.defender, self.cfg)
                self.assertEqual([e.hp for e in entities],
                                 [100, 100, 100 - self.cfg.turrets[name].damage])
                self.assertEqual(totals.killed, 0)

    def test_same_cell_copies_are_not_splash_targets_for_guns(self):
        self.defender.buildings = [Building(0, 1, "gun1")]
        copies = [Minion(0, 8, 5, 0), Minion(1, 100, 5, 0)]
        entities, totals = combat_tick(0, copies, [], self.path, self.defender, self.cfg)
        self.assertEqual([(e.roster_id, e.hp) for e in entities], [(1, 100)])
        self.assertEqual(totals.killed, 1)
        entities, _ = combat_tick(1, entities, [], self.path, self.defender, self.cfg)
        self.assertEqual([(e.roster_id, e.hp) for e in entities], [(1, 92)])

    def test_turrets_select_before_same_tick_damage_and_death_resolution(self):
        for buildings, rear_hp in (
            ([Building(0, 1, "gun1"), Building(1, 1, "gun2")], 100),
            ([Building(0, 1, "splash"), Building(1, 1, "gun1")], 90),
        ):
            with self.subTest(buildings=buildings):
                self.defender.buildings = buildings
                copies = [Minion(0, 1, 5, 0), Minion(1, 100, 5, 0)]
                entities, totals = combat_tick(0, copies, [], self.path, self.defender, self.cfg)
                self.assertEqual([(e.roster_id, e.hp) for e in entities], [(1, rear_hp)])
                self.assertEqual(totals.killed, 1)

    def test_arrivals_disappear_before_turrets_can_attack(self):
        self.defender.buildings.append(Building(10, 10, "gun1"))
        entity = Minion(0, 1, 5, 0, len(self.path) - 2)
        entities, totals = combat_tick(1, [entity], [], self.path, self.defender, self.cfg)
        self.assertEqual(entities, [])
        self.assertEqual((totals.hits, totals.killed, self.defender.hp), (1, 0, 795))

    def test_walls_do_not_attack_and_turret_damage_accumulates(self):
        self.defender.buildings = [Building(0, 1, "wall")]
        entities, _ = combat_tick(0, [], [self.entry], self.path, self.defender, self.cfg)
        self.assertEqual(entities[0].hp, 20)
        self.defender.buildings = [Building(0, 1, "gun1"), Building(1, 1, "gun1")]
        entities, _ = combat_tick(0, [], [self.entry], self.path, self.defender, self.cfg)
        self.assertEqual(entities[0].hp, 4)


class SettlementTests(unittest.TestCase):
    def test_factory_purchase_round_and_correct_hit_income(self):
        engine = Engine(balanced_config(), ("A", "B"))
        records = engine.play_round([[{"op": "buy_factory"}, minion()], []])
        self.assertEqual(event(records, 0, "income"), {"kind": "income", "path": 22, "factories": 15, "hits": 5, "total": 42})
        self.assertEqual((engine.players[0].gold, engine.players[1].gold), (107, 122))
        self.assertEqual((engine.players[0].hp, engine.players[1].hp), (800, 795))
        records = engine.play_round([[], []])
        self.assertEqual(engine.players[0].gold, 149)
        self.assertEqual(event(records, 0, "income")["hits"], 5)

    def test_path_income_uses_own_defensive_map(self):
        engine = Engine(config(initial_gold=1000), ("A", "B"))
        actions = [wall(3, y) for y in range(11)] + [wall(7, y) for y in range(1, 12)]
        records = engine.play_round([actions, [minion()]])
        own_length = records[0]["snapshot"]["length_path"]
        self.assertGreater(own_length, 22)
        self.assertEqual(event(records, 0, "income")["path"], own_length)
        self.assertEqual(event(records, 1, "income")["path"], 22)
        self.assertEqual(event(records, 1, "income")["hits"], 5)

    def test_roster_exactly_twelve_rounds_and_settled_remaining_lifetime(self):
        engine = Engine(config(initial_hp=100000), ("A", "B"))
        for round_number in range(1, 15):
            records = engine.play_round([[minion()] if round_number == 1 else [], []])
            self.assertEqual(event(records, 0, "combat")["outgoing_hits"], int(round_number <= 12))
            roster = records[0]["snapshot"]["roster"]
            if round_number < 12:
                self.assertEqual(roster[0]["expires_after_round"], 12)
                self.assertEqual(roster[0]["remaining_rounds"], 12 - round_number)
            else:
                self.assertEqual(roster, [])
            if round_number == 12:
                self.assertEqual(event(records, 0, "expiration")["roster_ids"], [0])

    def test_permanent_entries_and_combat_deaths_do_not_remove_roster(self):
        engine = Engine(config(roster_lifespan=0), ("A", "B"))
        data = engine.config.to_dict()
        data["turrets"]["gun1"].update(damage=30)
        engine.config = config_from_dict(data)
        for r in range(1, 16):
            records = engine.play_round([[minion()] if r == 1 else [],
                                         [{"op": "build_turret", "type": "gun1", "x": 0, "y": 1}] if r == 1 else []])
            roster = records[0]["snapshot"]["roster"]
            self.assertEqual(len(roster), 1)
            self.assertIsNone(roster[0]["expires_after_round"])
            self.assertIsNone(roster[0]["remaining_rounds"])
            self.assertEqual(event(records, 0, "combat")["killed"], 1)

    def test_new_round_generates_full_hp_copies(self):
        data = config(initial_hp=100000).to_dict()
        data["turrets"]["gun1"].update(damage=1, range=1.0)
        data["minions"]["tier1"]["hp"] = 3
        engine = Engine(config_from_dict(data), ("A", "B"))
        for r in range(1, 6):
            records = engine.play_round([[minion()] if r == 1 else [],
                                         [{"op": "build_turret", "type": "gun1", "x": 0, "y": 1}] if r == 1 else []])
            self.assertEqual(event(records, 0, "combat")["outgoing_hits"], 1)
            self.assertEqual(event(records, 0, "combat")["killed"], 0)

    def test_both_bases_fall_round_still_completes_and_hp_is_negative(self):
        data = balanced_config().to_dict()
        data["minions"]["tier1"]["damage"] = 900
        engine = Engine(config_from_dict(data), ("A", "B"))
        records = engine.play_round([[minion(), minion()], [minion(), minion()]])
        self.assertEqual([p.hp for p in engine.players], [-1000, -1000])
        self.assertEqual(engine.result, {"winner": None, "reason": "both_bases_destroyed"})
        for p in (0, 1):
            self.assertEqual(event(records, p, "combat")["outgoing_hits"], 2)
            self.assertEqual(event(records, p, "income")["hits"], 10)
            self.assertEqual(records[p]["result"], engine.result)

    def test_only_destroyed_player_loses(self):
        data = balanced_config().to_dict()
        data["minions"]["tier1"]["damage"] = 800
        engine = Engine(config_from_dict(data), ("A", "B"))
        engine.play_round([[minion()], []])
        self.assertEqual(engine.players[1].hp, 0)
        self.assertEqual(engine.result, {"winner": 0, "reason": "base_destroyed"})

    def test_round_fifty_compares_hp_or_draws(self):
        for difference, winner in ((0, None), (1, 0), (-1, 1)):
            engine = Engine(balanced_config(), ("A", "B"))
            engine.players[0].hp += difference
            for _ in range(49):
                engine.play_round([[], []])
                self.assertIsNone(engine.result)
            engine.play_round([[], []])
            self.assertEqual(engine.result, {"winner": winner, "reason": "round_limit"})
            with self.assertRaises(ValueError):
                engine.play_round([[], []])

    def test_recorded_state_does_not_change_later(self):
        engine = Engine(balanced_config(), ("A", "B"))
        initial = engine.initial_records(("A", "B"))
        first = engine.play_round([[wall(3, 3), minion()], []])
        serialized = json.dumps(first, sort_keys=True)
        engine.play_round([[wall(4, 4), minion()], []])
        self.assertEqual(json.dumps(first, sort_keys=True), serialized)
        self.assertEqual(initial[0]["snapshot"]["buildings"], [])
        self.assertEqual(initial[0]["snapshot"]["gold"], 100)
        self.assertEqual(initial[0]["snapshot"]["hp"], 800)


if __name__ == "__main__":
    unittest.main()
