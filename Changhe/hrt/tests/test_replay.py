from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from td_game.config import balanced_config
from td_game.logs import LogError, load_log
from td_game.runner import run_match
from td_stats.main import summarize
from td_view.control import ACTION, SPEEDS, advance, handle_key
from td_view.draw import CELL_WIDTH, EVENT_X, MAP_Y, PLAYER_1_X, PLAYER_2_X, Canvas, draw
from td_view.scene import ViewScene, buildscene, visible_events
from td_view.utils import cell_width, truncate, visible_lines


class Noop:
    def decide(self, observation):
        return []


class FakeScreen:
    def __init__(self, height=24, width=100):
        self.height, self.width = height, width
        self.buffer = {}
        self.erases = 0

    def getmaxyx(self):
        return self.height, self.width

    def erase(self):
        self.erases += 1
        self.buffer.clear()

    def refresh(self):
        pass

    def addstr(self, y, x, text, attr=0):
        assert 0 <= y < self.height and x >= 0
        assert x + sum(map(cell_width, text)) <= self.width
        for ch in text:
            self.buffer[y, x] = ch
            x += cell_width(ch)

    def line(self, y):
        return "".join(self.buffer.get((y, x), " ") for x in range(self.width)).rstrip()

    def text(self):
        return "\n".join(self.line(y) for y in range(self.height))


class LogReplayTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.path = Path(self.temp.name) / "match.jsonl"
        run_match(balanced_config(), [Noop(), Noop()], ("A", "B"), self.path)
        self.log = load_log(self.path)

    def rewrite(self, records):
        damaged = Path(self.temp.name) / "damaged.jsonl"
        damaged.write_text("".join(json.dumps(r) + "\n" for r in records), encoding="utf-8")
        return damaged

    def records(self):
        return [json.loads(line) for line in self.path.read_text(encoding="utf-8").splitlines()]

    def test_full_fifty_round_recording_and_required_sparse_schema(self):
        records = self.records()
        self.assertEqual(len(records), 102)
        self.assertEqual(len(self.log.frames), 51)
        for record in records:
            self.assertIn("event", record)
            self.assertIn("snapshot", record)
            self.assertIn(record["player"], (0, 1))
            snap = record["snapshot"]
            self.assertEqual(set(snap), {"name", "hp", "gold", "n_factories", "n_turrets", "n_walls", "length_path", "buildings", "roster"})
            self.assertEqual(snap["length_path"], 22)
            self.assertNotIn("tick", record)
            self.assertNotIn("path", snap)
            self.assertNotIn("grid", snap)
        for p in (0, 1):
            initial = self.log.frames[0].records[p]["snapshot"]
            self.assertEqual((initial["hp"], initial["gold"]), (800, 100))
            self.assertEqual(self.log.frames[-1].records[p]["result"], {"winner": None, "reason": "round_limit"})

    def test_reader_pairs_by_explicit_identity_even_if_records_reordered(self):
        log = load_log(self.rewrite(list(reversed(self.records()))))
        self.assertEqual([f.round for f in log.frames], list(range(51)))
        self.assertEqual(log.frames[0].records[0]["snapshot"]["name"], "A")

    def test_bad_logs_report_locations(self):
        original = self.records()
        duplicate = original[:2] + [original[0]] + original[2:]
        missing_partner = original[:-1]
        missing_field = self.records()
        del missing_field[4]["snapshot"]["gold"]
        unsupported = self.records()
        unsupported[0]["schema_version"] = 100
        for records, phrase in ((duplicate, "line 3: duplicate"), (missing_partner, "line 101: round 50 missing partner"),
                                (missing_field, "line 5: snapshot missing gold"), (unsupported, "line 1: unsupported schema_version")):
            with self.subTest(phrase=phrase), self.assertRaisesRegex(LogError, phrase):
                load_log(self.rewrite(records))
        damaged = Path(self.temp.name) / "bad.jsonl"
        damaged.write_text("{broken\n", encoding="utf-8")
        with self.assertRaisesRegex(LogError, "line 1: malformed JSON"):
            load_log(damaged)

    def test_bad_snapshot_and_missing_metadata_are_clear_errors(self):
        for field, value in (("buildings", [{"x": 12, "y": 0, "type": "wall"}]), ("roster", [{}]), ("gold", "100")):
            records = self.records()
            records[2]["snapshot"][field] = value
            with self.subTest(field=field), self.assertRaisesRegex(LogError, "line 3:"):
                load_log(self.rewrite(records))
        records = self.records()
        del records[0]["match"]
        with self.assertRaisesRegex(LogError, "line 1: round 0 requires"):
            load_log(self.rewrite(records))

    def test_independent_reader_scenes_and_stats_with_engine_and_bots_disabled(self):
        script = '''
import sys
class ForbiddenImports:
    def find_spec(self, fullname, path=None, target=None):
        if fullname in ("td_game.engine", "td_game.combat", "td_game.pathfinding", "td_game.config") or fullname.startswith("td_bots"):
            raise AssertionError("replay imported " + fullname)
sys.meta_path.insert(0, ForbiddenImports())
from td_game.logs import load_log
from td_stats.main import summarize
from td_view.scene import buildscene
log = load_log(sys.argv[1])
assert len(log.frames) == 51
assert summarize(log)["rounds"] == 50
for frame in log.frames:
    assert len(buildscene(frame, log.match)) == 2
'''
        completed = subprocess.run([sys.executable, "-c", script, str(self.path)], capture_output=True, text=True)
        self.assertEqual(completed.returncode, 0, completed.stderr)

    def test_summary_uses_events_and_outcomes(self):
        summary = summarize(self.log)
        self.assertEqual(summary["rounds"], 50)
        self.assertEqual(summary["players"][0]["outcome"], "draw")
        self.assertEqual(summary["players"][0]["income_path"], 50 * 22)
        self.assertEqual(summary["players"][0]["gold"], 100 + 50 * 22)

    def test_manual_playback_events_have_no_future_or_duplicates(self):
        vs = ViewScene(self.log)
        self.assertEqual(handle_key(vs, "j", 0), ACTION.REDRAW)
        self.assertTrue(vs.paused)
        first = visible_events(vs)
        self.assertTrue(all(r <= 1 for r, p, e in first))
        handle_key(vs, "k", 0)
        self.assertTrue(all(r == 0 for r, p, e in visible_events(vs)))
        handle_key(vs, "j", 0)
        self.assertEqual(visible_events(vs), first)
        handle_key(vs, "G", 0)
        self.assertEqual(vs.index, 50)
        handle_key(vs, "0", 0)
        self.assertEqual(vs.index, 0)
        self.assertEqual(handle_key(vs, "q", 0), ACTION.QUIT)

    def test_verbose_pause_speed_and_automatic_end(self):
        vs = ViewScene(self.log, paused=True)
        self.assertFalse(vs.verbose)
        self.assertEqual(handle_key(vs, "v", 0), ACTION.REDRAW)
        self.assertTrue(vs.verbose)
        self.assertEqual(handle_key(vs, " ", 10), ACTION.REDRAW)
        self.assertFalse(vs.paused)
        self.assertEqual(advance(vs, 10.99), ACTION.NONE)
        self.assertEqual(advance(vs, 11), ACTION.REDRAW)
        self.assertEqual(vs.index, 1)
        handle_key(vs, "+", 11)
        self.assertEqual(SPEEDS[vs.speed_index], 2.0)
        self.assertEqual(advance(vs, 11.5), ACTION.REDRAW)
        self.assertEqual(vs.index, 2)
        for _ in range(10):
            handle_key(vs, "-", 12)
        self.assertEqual(SPEEDS[vs.speed_index], 0.25)
        handle_key(vs, "END", 13)
        self.assertTrue(vs.paused)
        handle_key(vs, "k", 13)
        handle_key(vs, " ", 13)
        self.assertEqual(advance(vs, 17), ACTION.REDRAW)
        self.assertEqual(vs.index, 50)
        self.assertTrue(vs.paused)

    def test_fixed_drawing_layout_cell_width_and_no_path_display(self):
        snap = self.log.frames[0].records[0]["snapshot"]
        snap.update(buildings=[{"x": 3, "y": 4, "type": "wall"}, {"x": 2, "y": 1, "type": "gun1"},
                               {"x": 7, "y": 4, "type": "gun2"}, {"x": 8, "y": 7, "type": "gun3"},
                               {"x": 5, "y": 6, "type": "splash"}],
                    n_turrets=4, n_factories=2, length_path=987654)
        players = buildscene(self.log.frames[0], self.log.match)
        self.assertEqual(players[0].grid[4][3], "#")
        self.assertEqual(players[0].grid[1][2], "1")
        self.assertEqual(players[0].grid[4][7], "2")
        self.assertEqual(players[0].grid[7][8], "3")
        self.assertEqual(players[0].grid[6][5], "X")
        self.assertFalse(hasattr(players[0], "path"))
        screen = FakeScreen()
        vs = ViewScene(self.log)
        draw(screen, {"vs": vs})
        self.assertEqual(CELL_WIDTH, 2)
        self.assertEqual(screen.buffer[MAP_Y, PLAYER_1_X], "┌")
        self.assertEqual(screen.buffer[MAP_Y, PLAYER_2_X], "┌")
        self.assertEqual(screen.buffer[MAP_Y + 1 + 4, PLAYER_1_X + 1 + 3 * 2], "#")
        self.assertEqual(screen.buffer[MAP_Y + 1 + 1, PLAYER_1_X + 1 + 2 * 2], "1")
        self.assertEqual(screen.buffer[2, EVENT_X], "E")
        self.assertEqual(screen.buffer[MAP_Y + 1 + 4, PLAYER_1_X + 1 + 7 * 2], "2")
        self.assertEqual(screen.buffer[MAP_Y + 1 + 7, PLAYER_1_X + 1 + 8 * 2], "3")
        self.assertEqual(screen.buffer[MAP_Y + 1 + 6, PLAYER_1_X + 1 + 5 * 2], "X")
        self.assertIn("T: 4  F: 2", screen.text())
        self.assertNotIn("987654", screen.text())
        self.assertNotIn("length_path", screen.text())
        for ps, x in zip(players, (PLAYER_1_X, PLAYER_2_X)):
            self.assertEqual(ps.grid[0][0], "S")
            self.assertEqual(ps.grid[11][11], "B")
            self.assertEqual(screen.buffer[MAP_Y + 1, x + 1], "S")
            self.assertEqual(screen.buffer[MAP_Y + 12, x + 1 + 11 * CELL_WIDTH], "B")

    def test_overflow_ellipsis_and_redraw_erases_stale_text(self):
        screen = FakeScreen()
        vs = ViewScene(self.log, index=49, verbose=True)
        draw(screen, {"vs": vs})
        self.assertIn("...", screen.text())
        vs.index = 0
        vs.verbose = False
        self.log.frames[0].records[0]["snapshot"]["name"] = "X"
        draw(screen, {"vs": vs})
        self.assertEqual(screen.erases, 2)
        self.assertEqual(screen.line(2)[:PLAYER_2_X].rstrip(), "player0")
        self.assertNotIn("R49", screen.text())
        roster = [{"id": i, "type": "tier1", "expires_after_round": None, "remaining_rounds": None} for i in range(100)]
        self.log.frames[0].records[0]["snapshot"]["roster"] = roster
        draw(screen, {"vs": vs})
        self.assertIn("Roster(100):", screen.text())
        self.assertIn("...", screen.line(screen.height - 3)[:PLAYER_2_X])

    def test_narrow_terminal_and_absolute_coordinate_overwrite(self):
        screen = FakeScreen(height=5, width=15)
        vs = ViewScene(self.log)
        draw(screen, {"vs": vs})
        self.assertIn("...", screen.text())
        screen = FakeScreen()
        canvas = Canvas(screen)
        canvas._add_str(8, 7, "abcd")
        canvas._add_str(8, 7, "XY")
        self.assertEqual(screen.line(7)[8:12], "XYcd")
        canvas._add_str(1000, 1000, "ignored")
        self.assertEqual(truncate("abcdef", 5), "ab...")
        self.assertEqual(truncate("塔塔塔", 5), "塔...")
        self.assertEqual(visible_lines(["a", "b", "c"], 2), ["...", "c"])

    def test_match_runner_records_all_actions_and_prevents_overwrite(self):
        class ActionFixture:
            def decide(self, observation):
                if observation["round"] != 1:
                    return []
                # Fixed inputs exercise each action's recording contract.
                return [{"op": "buy_factory"}, {"op": "build_wall", "x": 5, "y": 5},
                        {"op": "build_turret", "type": "gun1", "x": 2, "y": 1},
                        {"op": "buy_minion", "type": "tier1"}]

        first_path = Path(self.temp.name) / "match1.jsonl"
        second_path = Path(self.temp.name) / "match2.jsonl"
        names = ("bot1", "bot2")
        for path in (first_path, second_path):
            run_match(balanced_config(), [Noop(), ActionFixture()], names, path)
        self.assertEqual(first_path.read_bytes(), second_path.read_bytes())
        log = load_log(first_path)
        self.assertIsNotNone(log.result)
        ops = {event["action"]["op"] for frame in log.frames for record in frame.records
               for event in record["event"] if event["kind"] == "action" and event["accepted"]}
        self.assertEqual(ops, {"buy_factory", "buy_minion", "build_wall", "build_turret"})
        for frame in log.frames:
            buildscene(frame, log.match)
        summary = summarize(log)
        self.assertGreater(summary["players"][1]["outgoing_hits"], 0)
        with self.assertRaises(FileExistsError):
            run_match(balanced_config(), [Noop(), Noop()], names, first_path)


if __name__ == "__main__":
    unittest.main()
