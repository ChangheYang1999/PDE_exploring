"""Harness checks: spec resolution, version digests, scenario isolation."""
from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from bot_research.harness import match


class Harness(unittest.TestCase):
    def test_factory_spec_gives_fresh_instances(self):
        a = match.resolve_spec("bot_research.bots.best:@make?mid_until=5")
        b = match.resolve_spec("bot_research.bots.best:@make?mid_until=5")
        self.assertIsNot(a, b)

    def test_import_closure_follows_imports(self):
        files = {p.as_posix().split("bot_research/", 1)[1] for p in match.import_closure("bot_research.bots.best")}
        self.assertIn("bots/best.py", files)
        self.assertIn("harness/gamekit.py", files)
        self.assertIn("__init__.py", files)

    def test_play_match_records_both_sides_and_versions(self):
        with tempfile.TemporaryDirectory(dir=str(match.ROOT / "bot_research" / "tmp")) as d:
            row = match.play_match("bot_research.bots.best:@make", "td_bots.protocol:idle", Path(d) / "m.jsonl")
        self.assertEqual(row["winner"], 0)
        self.assertEqual(len(row["version_a"]), 64)
        self.assertFalse(row["source_changed"])
        self.assertEqual(row["players"][0]["n_rejected"], 0)

    def test_scenario_rounds_use_pristine_observation(self):
        calls = []

        def mutating_bot(obs):
            calls.append(obs["round"])
            obs["players"][obs["player"]]["gold"] = -1
            raise RuntimeError("bot failure during scripted round")

        def override(obs):
            return [{"op": "buy_factory"}] * (obs["players"][obs["player"]]["gold"] // 20) if obs["round"] == 1 else None

        bot = match.TimedBot(mutating_bot, override)
        out = bot.decide({"round": 1, "player": 0, "players": [{"gold": 100}, {"gold": 100}]})
        self.assertEqual(len(out), 5)
        self.assertEqual(len(bot.scenario_errors), 1)


if __name__ == "__main__":
    unittest.main()
