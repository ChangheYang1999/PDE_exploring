from __future__ import annotations

import copy
import importlib.util
import json
import tempfile
import unittest
from dataclasses import replace
from pathlib import Path

from td_game.config import balanced_config
from td_game.engine import Engine

ANALYSIS_AVAILABLE = importlib.util.find_spec("pandas") is not None
if ANALYSIS_AVAILABLE:
    import pandas as pd
    from data_analysis.features import build_feature_df


@unittest.skipUnless(ANALYSIS_AVAILABLE, "install .[analysis] for feature-extraction tests")
class FeatureTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.directory = Path(self.temp.name)
        config = balanced_config()
        config = replace(config, globals=replace(config.globals, max_rounds=3, roster_lifespan=2))
        engine = Engine(config, ("bot1", "bot2"))
        self.records = engine.initial_records(("bot1", "bot2"))
        for record in self.records:
            record["match"]["tournament"] = {"game_index": 7}
        self.records += engine.play_round([
            [{"op": "buy_minion", "type": "tier1"}],
            [{"op": "buy_minion", "type": "tier2"}],
        ])
        self.records += engine.play_round([[], []])
        self.records += engine.play_round([
            [{"op": "buy_minion", "type": "tier1"}, {"op": "buy_factory"},
             {"op": "build_turret", "type": "gun1", "x": 2, "y": 1}],
            [{"op": "buy_factory"}, {"op": "buy_factory"}],
        ])

    def write(self, filename="misleading-bot-name.jsonl", records=None):
        path = self.directory / filename
        path.write_text("".join(json.dumps(r) + "\n" for r in
                                (self.records if records is None else records)), encoding="utf-8")
        return path

    def test_two_rows_index_columns_and_targets(self):
        self.write()
        df = build_feature_df(self.directory)
        self.assertEqual(df.shape, (2, 6))
        self.assertIsInstance(df.index, pd.MultiIndex)
        self.assertEqual(df.index.names, ["game_id", "player"])
        self.assertEqual(df.index.tolist(), [("game_000007", 0), ("game_000007", 1)])
        self.assertEqual(df.columns.tolist(),
                         ["n_factories", "n_turrets", "length_path", "n_minions", "result", "target"])
        self.assertEqual(df["target"].tolist(), ["bot1", "bot2"])

    def test_final_settled_values_and_total_minion_purchases(self):
        self.write()
        df = build_feature_df(self.directory)
        for player, record in enumerate(self.records[-2:]):
            snap = record["snapshot"]
            row = df.loc[("game_000007", player)]
            for field in ("n_factories", "n_turrets", "length_path"):
                self.assertEqual(row[field], snap[field])
        self.assertEqual([len(r["snapshot"]["roster"]) for r in self.records[-2:]], [1, 0])
        self.assertEqual(df["n_minions"].tolist(), [2, 1])  # expired purchases still count
        self.assertEqual(df["n_factories"].tolist(), [1, 2])
        self.assertEqual(df["n_turrets"].tolist(), [1, 0])

    def test_rejected_purchases_and_other_actions_do_not_count(self):
        config = balanced_config()
        config = replace(config, globals=replace(config.globals, max_rounds=1))
        engine = Engine(config, ("bot1", "bot2"))
        records = engine.initial_records(("bot1", "bot2"))
        records += engine.play_round([
            [{"op": "buy_minion", "type": "unknown"}, {"op": "buy_factory"},
             {"op": "build_turret", "type": "gun1", "x": 2, "y": 1}],
            [{"op": "buy_minion", "type": "tier3"}] * 3,
        ])
        self.write(records=records)
        self.assertEqual(build_feature_df(self.directory)["n_minions"].tolist(), [0, 1])

    def test_result_uses_metadata_for_wins_losses_and_draws(self):
        for winner, expected in ((0, [1, -1]), (1, [-1, 1]), (None, [0, 0])):
            records = copy.deepcopy(self.records)
            for record in records[-2:]:
                record["result"] = {"winner": winner, "reason": "round_limit"}
                record["snapshot"]["hp"] = 800  # equal HP cannot identify the supplied winner
            self.write(records=records)
            self.assertEqual(build_feature_df(self.directory)["result"].tolist(), expected)

    def test_metadata_ids_order_and_non_jsonl_files(self):
        self.write("a.jsonl")
        records = copy.deepcopy(self.records)
        for record in records[:2]:
            record["match"]["tournament"]["game_index"] = 2
        self.write("z.jsonl", records)
        (self.directory / "manifest.json").write_text("ignored", encoding="utf-8")
        (self.directory / "summary.csv").write_text("ignored", encoding="utf-8")
        first = build_feature_df(self.directory)
        second = build_feature_df(self.directory)
        self.assertTrue(first.index.is_unique)
        self.assertEqual(first.index.tolist(),
                         [("game_000002", 0), ("game_000002", 1), ("game_000007", 0), ("game_000007", 1)])
        pd.testing.assert_frame_equal(first, second)

    def test_explicit_game_id_and_filename_fallback(self):
        records = copy.deepcopy(self.records)
        for record in records[:2]:
            record["match"]["tournament"]["game_id"] = "explicit-id"
        self.write("fallback.jsonl", records)
        self.assertEqual(build_feature_df(self.directory).index[0], ("explicit-id", 0))
        for record in records[:2]:
            record["match"].pop("tournament", None)
            record["match"].pop("bots", None)  # snapshot identities also work without match.bots
        self.write("fallback.jsonl", records)
        df = build_feature_df(self.directory)
        self.assertEqual(df.index[0], ("fallback", 0))
        self.assertEqual(df["target"].tolist(), ["bot1", "bot2"])

    def test_duplicate_game_ids_are_rejected(self):
        self.write("one.jsonl")
        self.write("two.jsonl")
        with self.assertRaisesRegex(ValueError, "two.jsonl: duplicate game_id"):
            build_feature_df(self.directory)

    def test_invalid_logs_report_path_and_problem(self):
        cases = []
        missing_player = copy.deepcopy(self.records[:-1])
        cases.append((missing_player, "round 3 missing partner"))
        missing_field = copy.deepcopy(self.records)
        del missing_field[-1]["snapshot"]["length_path"]
        cases.append((missing_field, "snapshot missing length_path"))
        unfinished = copy.deepcopy(self.records)
        for record in unfinished[-2:]:
            del record["result"]
        cases.append((unfinished, "unfinished game"))
        unknown_target = copy.deepcopy(self.records)
        for record in unknown_target[:2]:
            record["match"]["bots"][0] = ""
        cases.append((unknown_target, "no identifiable bot target"))
        wrong_target = copy.deepcopy(self.records)
        for record in wrong_target[:2]:
            record["match"]["bots"][0] = "bot30"
        cases.append((wrong_target, "disagrees with snapshot.name"))
        invalid_index = copy.deepcopy(self.records)
        for record in invalid_index[:2]:
            record["match"]["tournament"]["game_index"] = True
        cases.append((invalid_index, "game_index must be a nonnegative integer"))
        for records, phrase in cases:
            with self.subTest(phrase=phrase):
                self.write("bad.jsonl", records)
                with self.assertRaisesRegex(ValueError, f"bad.jsonl:.*{phrase}"):
                    build_feature_df(self.directory)
        (self.directory / "bad.jsonl").write_text("{broken\n", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "bad.jsonl: line 1: malformed JSON"):
            build_feature_df(self.directory)

    def test_empty_and_missing_directories_are_rejected(self):
        with self.assertRaisesRegex(ValueError, "no game JSONL files"):
            build_feature_df(self.directory)
        with self.assertRaisesRegex(ValueError, "expected a game-log directory"):
            build_feature_df(self.directory / "missing")


if __name__ == "__main__":
    unittest.main()
