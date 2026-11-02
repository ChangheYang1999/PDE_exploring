"""Legality, determinism and basic strength checks for bot_research.bots.best on the unchanged engine.

The environment variable BEST_MODULE (default ``bot_research.bots.best``) names the module under test, so the
same checks run on a frozen copy before it is installed as best.py.
"""
from __future__ import annotations

import copy
import hashlib
import importlib
import os
import unittest
from pathlib import Path

from td_bots.protocol import collect_actions
from td_game.config import balanced_config
from td_game.engine import Engine

from bot_research.experiments.lead.frozen import best_v3b
from bot_research.harness import gamekit
from bot_research.harness import scenarios
from bot_research.harness.match import TimedBot, resolve_spec

ROOT = Path(__file__).resolve().parents[1]
BEST_MODULE = os.environ.get("BEST_MODULE", "bot_research.bots.best")
best = importlib.import_module(BEST_MODULE)
BEST = BEST_MODULE + ":@make"

# hrt-w1's frozen planner as imported by best.py (bots/defense/frozen/v7/SHA256SUMS).
PLANNER_SHA256 = {
    "__init__.py": "a3c320f4c74a2282c83308b83ccbb7b7e339f6b390ef98b6c914374b96ffe190",
    "geometry.py": "e995ed072b4d5a206b8d4b8970d65dfc65a498dbd3716afbe751856fd9317b5f",
    "plan.py": "19a9096fbe27a9ffcc4cc3b233b0efa187932a32d3ce5d7d8b28cf71c055428a",
    "simulate.py": "2a0f5d1452f40870302535f38172176934b7c730a2e5d9aef904147b0ce896cc",
    "templates.py": "68d37b840e40866d8ae9c086e6f29fb67344541fb557b6d17cbd106409167824",
}
# The development setting best.py reproduces (checked on full trajectories by
# experiments/lead/same_actions.py and same_actions_scen.py; here on short prefixes).
DEV_PARAMS = ('big_threat=100&gun_cap=120&poke_until=3&big_partial=true'
              '&r1_poke=3&attack_mode="adaptive"&poke_reactive="turret"&fortress_n=4&immune_attack=true'
              '&foreign_policy="econ17"&mid_until=5&fortress_guns=true&catch_up=true&foreign_target="econ20"')
DEV_SPEC = 'bot_research.experiments.lead.v19:@make?' + DEV_PARAMS
# The options r1_gun and mid_joint, against their development versions (v22 and v20).
OPTION_SPECS = (
    ('r1_gun=[4,1]', 'bot_research.experiments.lead.v22:@make?' + DEV_PARAMS + '&r1_gun=[4,1]'),
    ('mid_joint=0.75&mid_level=true',
     'bot_research.experiments.lead.v20:@make?' + DEV_PARAMS + '&mid_joint=0.75&mid_level=true'),
)
# SHA-256 of the SHA256SUMS files of the frozen packages best.py imports directly or through econ20
# (economy v20 imports defense v15 and v26), with the folder each listed path is relative to.
FROZEN_SUMS = {
    "bots/economy/frozen/v20/SHA256SUMS": ("bots/economy",
                                           "1ab8d493689a95b27f0fe7c06e2d22fc8a448c116d7d1ce4ff3582506f6972e6"),
    "bots/defense/frozen/v7/SHA256SUMS": ("bots/defense/frozen/v7",
                                          "f3a682f404a3451566603bba7122dba334ad0f4bb33d99559be2fa4745302af1"),
    "bots/defense/frozen/v15/SHA256SUMS": ("bots/defense/frozen/v15",
                                           "d5eceafdb3a1ae1da1e4ad0fa6061e267696605ad90ad8517d3e56228f87ea6c"),
    "bots/defense/frozen/v26/SHA256SUMS": ("bots/defense/frozen/v26",
                                           "1abea844661e3aca97bf65422a8237e5ce036641c586c40cd755002174fadc65"),
}
# Scripted openings on which the foreign-map switch is exercised (harness/scenarios.py).
SCENARIOS = ("mirror:1:2", "asym:23:2")


def play(spec_a, spec_b, max_rounds=None, scenario=None):
    """Play on the engine; return (engine, rejected counts, error counts, per-round actions of A).
    With a scenario, both submissions of the scripted rounds are replaced as in harness.match."""
    engine = Engine(balanced_config(), ("A", "B"))
    overrides = scenarios.make_overrides(scenario) if scenario else (None, None)
    bots = [TimedBot(resolve_spec(s), o) for s, o in zip((spec_a, spec_b), overrides)]
    rejected, errors, actions_a = [0, 0], [0, 0], []
    while engine.result is None and (max_rounds is None or engine.round < max_rounds):
        obs = [engine.observation(p) for p in (0, 1)]
        actions, errs = collect_actions(bots, obs)
        actions_a.append(actions[0])
        for record in engine.play_round(actions, errs):
            for event in record["event"]:
                if event["kind"] == "action" and not event["accepted"]:
                    rejected[record["player"]] += 1
                elif event["kind"] == "bot_error":
                    errors[record["player"]] += 1
    return engine, rejected, errors, actions_a


class BestBot(unittest.TestCase):
    OPPONENTS = ("td_bots.protocol:idle", "bot_research.harness.baselines:@rush?tier=\"tier3\"",
                 "bot_research.harness.baselines:@eco_then_flood?switch=8",
                 "bot_research.harness.baselines:@random_legal?seed=3")

    def test_no_rejections_or_errors_and_wins_against_baselines(self):
        for opp in self.OPPONENTS:
            for side in (0, 1):
                specs = (BEST, opp) if side == 0 else (opp, BEST)
                engine, rejected, errors, _ = play(*specs)
                with self.subTest(opponent=opp, side=side):
                    self.assertEqual(errors[side], 0)
                    self.assertEqual(rejected[side], 0)
                    self.assertEqual(engine.result["winner"], side)

    def test_rejection_counter_works(self):
        bad = type("B", (), {"decide": staticmethod(lambda obs: [{"op": "build_wall", "x": 0, "y": 0}])})()
        engine = Engine(balanced_config(), ("A", "B"))
        actions, errs = collect_actions([bad, bad], [engine.observation(0), engine.observation(1)])
        records = engine.play_round(actions, errs)
        self.assertTrue(any(e["kind"] == "action" and not e["accepted"] for e in records[0]["event"]))

    def test_deterministic(self):
        runs = [play(BEST, "bot_research.harness.baselines:@rush?tier=\"tier1\"",
                     max_rounds=12)[3] for _ in range(2)]
        self.assertEqual(runs[0], runs[1])

    def test_reproduces_development_setting(self):
        # a turret-owning opponent (rush builds none, threat_defender does) exercises the poke fallback;
        # the corner gun with one round-1 tier1 puts us 5 HP behind in round 2 (catch_up), and the half-budget
        # tier3 of round 3 and the round-1 bluff gun would exercise the joint plan of rule 3c if it were on
        for opp in ("bot_research.harness.baselines:@eco_then_flood?switch=8",
                    "bot_research.harness.baselines:@threat_defender",
                    'bot_research.bots.counters.guard_geometry:@make?roster=["tier1"]',
                    'bot_research.bots.counters.budget_timing:@make?tier="tier3"&attack_round=3&budget_fraction=0.5',
                    "bot_research.bots.counters.feature_bluff:@make?turret_round=1&turret_x=0&turret_y=2"):
            with self.subTest(opponent=opp):
                a = play(BEST, opp, max_rounds=10)[3]
                b = play(DEV_SPEC, opp, max_rounds=10)[3]
                self.assertEqual(a, b)

    def test_options_reproduce_development_versions(self):
        for params, dev in OPTION_SPECS:
            for opp in ('bot_research.bots.counters.guard_geometry:@make?roster=["tier1","tier1"]',
                        'bot_research.bots.counters.budget_timing:@make?tier="tier3"&attack_round=3&budget_fraction=0.5',
                        "bot_research.bots.counters.feature_bluff:@make?turret_round=1"):
                with self.subTest(option=params, opponent=opp):
                    a = play(BEST + "?" + params, opp, max_rounds=8)[3]
                    b = play(dev, opp, max_rounds=8)[3]
                    self.assertEqual(a, b)

    def test_reproduces_development_setting_after_scripted_opening(self):
        # the scripted walls are cells best.py never asked for, so the econ20 branch takes over in round 2
        opp = "bot_research.bots.economy.frozen.v17.econ17:@make?free_fallback=\"zero\"&foreign_attack_from=11"
        for scen in SCENARIOS:
            with self.subTest(scenario=scen):
                a = play(BEST, opp, max_rounds=8, scenario=scen)[3]
                b = play(DEV_SPEC, opp, max_rounds=8, scenario=scen)[3]
                self.assertEqual(a, b)
        bot = best.make()
        engine = Engine(balanced_config(), ("A", "B"))
        overrides = scenarios.make_overrides(SCENARIOS[0])
        bots = [TimedBot(bot, overrides[0]), TimedBot(resolve_spec(opp), overrides[1])]
        for _ in range(4):
            actions, errs = collect_actions(bots, [engine.observation(p) for p in (0, 1)])
            engine.play_round(actions, errs)
        self.assertIsNotNone(bot.alt)
        self.assertEqual(bot.switch_round, 2)

    def test_decide_entry_point_keeps_state_per_player(self):
        engine = Engine(balanced_config(), ("A", "B"))
        best._instances.clear()
        out = [best.decide(engine.observation(p)) for p in (0, 1)]
        self.assertEqual(sorted(best._instances), [0, 1])
        self.assertEqual(out[0], out[1])
        first = best._instances[0]
        best.decide(engine.observation(0))   # a new match starts with round 1: fresh instance
        self.assertIsNot(best._instances[0], first)

    def test_does_not_mutate_observation(self):
        engine = Engine(balanced_config(), ("A", "B"))
        bots = [best.make(), resolve_spec("bot_research.harness.baselines:@eco_then_flood?switch=3")]
        for _ in range(6):
            obs = [engine.observation(p) for p in (0, 1)]
            before = copy.deepcopy(obs[0])
            actions = [bots[0](obs[0]), bots[1](obs[1])]
            self.assertEqual(obs[0], before)
            engine.play_round(actions, [None, None])

    def test_frozen_planner_unchanged(self):
        folder = ROOT / "bots" / "defense" / "frozen" / "v7"
        for name, digest in PLANNER_SHA256.items():
            with self.subTest(file=name):
                self.assertEqual(hashlib.sha256((folder / name).read_bytes()).hexdigest(), digest)
        self.assertEqual(best.P.plan_defense.__module__, "bot_research.bots.defense.frozen.v7.plan")

    def test_frozen_packages_unchanged(self):
        for sums, (base, digest) in FROZEN_SUMS.items():
            with self.subTest(sums=sums):
                self.assertEqual(hashlib.sha256((ROOT / sums).read_bytes()).hexdigest(), digest)
            for line in (ROOT / sums).read_text().splitlines():
                digest_f, name = line.split()
                with self.subTest(file=f"{base}/{name}"):
                    self.assertEqual(hashlib.sha256((ROOT / base / name).read_bytes()).hexdigest(), digest_f)
        self.assertEqual(best.E20.__name__, "bot_research.bots.economy.frozen.v20.econ20")


class FrozenV3bGeometry(unittest.TestCase):
    """Exact checks of the frozen v3b template and arrival count (experiments/lead/frozen/best_v3b.py)."""

    def test_template_geometry(self):
        blocked = set(best_v3b.WALLS)
        self.assertEqual(len(best_v3b.WALLS), 33)
        self.assertEqual(len(best_v3b.SLOTS), 26)
        self.assertTrue(blocked.isdisjoint(best_v3b.SLOTS))
        path = gamekit.route(blocked)
        self.assertEqual(len(path) - 1, 46)
        full = blocked | set(best_v3b.SLOTS)
        path = gamekit.route(full)
        self.assertEqual(len(path) - 1, 78)
        rules = gamekit.Rules.from_observation(Engine(balanced_config(), ("A", "B")).observation(0))
        buildings = [{"x": x, "y": y, "type": "wall"} for x, y in best_v3b.WALLS]
        buildings += [{"x": x, "y": y, "type": "splash"} for x, y in best_v3b.SLOTS]
        self.assertEqual(gamekit.splash_total(path, buildings, rules), 1610)

    def test_arrivals_exact(self):
        for n_before in (0, 3, 249, 251, 600):
            for n in (0, 1, 7, 250, 777):
                for L in (22, 46, 78, 249, 250):
                    expect = sum(1 for k in range(n_before, n_before + n) if k % 250 + L <= 249)
                    self.assertEqual(best_v3b.arrivals(n_before, n, L, 250), expect)


if __name__ == "__main__":
    unittest.main()
