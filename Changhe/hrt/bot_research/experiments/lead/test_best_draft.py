"""Legality, determinism and basic strength checks for bot_research.bots.best on the unchanged engine."""
from __future__ import annotations

import copy
import hashlib
import unittest
from pathlib import Path

from td_bots.protocol import collect_actions
from td_game.config import balanced_config
from td_game.engine import Engine

from bot_research.bots import best
from bot_research.experiments.lead.frozen import best_v3b
from bot_research.harness import gamekit
from bot_research.harness.match import resolve_spec

ROOT = Path(__file__).resolve().parents[1]

# hrt-w1's frozen planner as imported by best.py (bots/defense/frozen/v7/SHA256SUMS).
PLANNER_SHA256 = {
    "__init__.py": "a3c320f4c74a2282c83308b83ccbb7b7e339f6b390ef98b6c914374b96ffe190",
    "geometry.py": "e995ed072b4d5a206b8d4b8970d65dfc65a498dbd3716afbe751856fd9317b5f",
    "plan.py": "19a9096fbe27a9ffcc4cc3b233b0efa187932a32d3ce5d7d8b28cf71c055428a",
    "simulate.py": "2a0f5d1452f40870302535f38172176934b7c730a2e5d9aef904147b0ce896cc",
    "templates.py": "68d37b840e40866d8ae9c086e6f29fb67344541fb557b6d17cbd106409167824",
}
# The development setting best.py reproduces (checked on full trajectories by
# experiments/lead/same_actions.py; here on a short prefix).
V7_SPEC = 'bot_research.experiments.lead.v7:@make?big_threat=100&attack_mode="robust"&poke_insurance=false'


def play(spec_a, spec_b, max_rounds=None):
    """Play on the engine; return (engine, rejected counts, error counts, per-round actions of A)."""
    engine = Engine(balanced_config(), ("A", "B"))
    bots = [type("B", (), {"decide": staticmethod(resolve_spec(s))})() for s in (spec_a, spec_b)]
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
                specs = ("bot_research.bots.best:@make", opp) if side == 0 else (opp, "bot_research.bots.best:@make")
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
        runs = [play("bot_research.bots.best:@make", "bot_research.harness.baselines:@rush?tier=\"tier1\"",
                     max_rounds=12)[3] for _ in range(2)]
        self.assertEqual(runs[0], runs[1])

    def test_reproduces_development_setting(self):
        opp = "bot_research.harness.baselines:@eco_then_flood?switch=8"
        a = play("bot_research.bots.best:@make", opp, max_rounds=10)[3]
        b = play(V7_SPEC, opp, max_rounds=10)[3]
        self.assertEqual(a, b)

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
