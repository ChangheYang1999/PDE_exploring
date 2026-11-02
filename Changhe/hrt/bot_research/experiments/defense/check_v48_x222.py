"""Replay check for the frozen v48 finish rule (lane hrt-w1, shift 4).

Replays the x222 game 00003 (frozen v45 against econ17 under scenario asym:23:2, fortress seat 0) from its logged observations with
frozen v48 and checks that at round 15 v48 buys the capacity-rule defence AND the padded kill (v45 bought the kill alone and drew):
5 splash + 7 gun3 + 223 tier1 + 16 tier5 + 2 factories, and that the engine resolves the round, against econ17's logged round-15
actions, as a fortress win (790 : -755). Rounds 3-14 must reproduce the logged actions (rounds 1-2 are the scenario's scripted rounds,
the harness discards the bot's actions there).

Run from the project root:
  PYTHONDONTWRITEBYTECODE=1 TMPDIR="$PWD/bot_research/tmp" .venv/bin/python -B bot_research/experiments/defense/check_v48_x222.py
Exit code 0 = all checks passed. Read-only: nothing under the project root is modified.
"""
from __future__ import annotations

import glob
import gzip
import json
import os
import sys
from collections import Counter

sys.path.insert(0, os.getcwd())
from bot_research.bots.defense.frozen.v48 import fortress as F  # noqa: E402
from td_game.config import config_from_dict  # noqa: E402
from td_game.engine import Engine  # noqa: E402
from td_game.state import Building, PlayerState, RosterEntry  # noqa: E402

LOG_GLOB = "bot_research/runs/defense/x222_r15_replay/logs/*00003--make_fortress-vs*asym-23-2.jsonl*"


def load_records(path):
    opener = gzip.open if path.endswith(".gz") else open
    with opener(path, "rt", encoding="utf-8") as fh:
        return [json.loads(line) for line in fh if line.strip()]


def main() -> int:
    paths = sorted(glob.glob(LOG_GLOB))
    if not paths:
        print("log not found:", LOG_GLOB)
        return 2
    records = load_records(paths[0])
    rules = records[0]["match"]["rules"]
    cfg = config_from_dict(rules)
    recs = {(r["round"], r["player"]): r for r in records if "round" in r and "player" in r}

    def snap(r, p):
        return recs[r, p]["snapshot"]

    def observation(r, p=0):
        return {"round": r, "player": p, "players": [snap(r - 1, q) for q in (0, 1)], "rules": rules}

    def actions(r, p):
        return [e["action"] for e in recs[r, p]["event"] if e["kind"] == "action" and e["accepted"]]

    def engine_at(r):
        engine = Engine(cfg, ("fortress", "econ17"))
        engine.round = r
        for p in (0, 1):
            s = snap(r, p)
            all_ids = [e["id"] for k in range(r + 1) for e in snap(k, p)["roster"]]
            engine.players[p] = PlayerState(
                s["name"], s["hp"], s["gold"], s["n_factories"], [Building(**b) for b in s["buildings"]],
                [RosterEntry(**{k: e[k] for k in ("id", "type", "bought_round", "expires_after_round")}) for e in s["roster"]],
                max(all_ids, default=-1) + 1)
        return engine

    bot = F.make()          # frozen v48 defaults
    failures = []
    for r in range(1, 16):
        proposed = bot(observation(r))
        if 3 <= r <= 14 and proposed != actions(r, 0):
            failures.append(f"round {r}: actions differ from the log")
        if r == 15:
            counts = Counter(a.get("type", a["op"]) for a in proposed)
            expected = {"splash": 5, "gun3": 7, "tier1": 223, "tier5": 16, "buy_factory": 2}
            print("round-15 purchase:", dict(counts))
            if dict(counts) != expected:
                failures.append(f"round 15: expected {expected}")
            engine = engine_at(14)
            result = engine.play_round([proposed, actions(15, 1)])
            accepted = all(e["accepted"] for q in result for e in q["event"] if e["kind"] == "action")
            hp = [p.hp for p in engine.players]
            print("engine after round 15: accepted", accepted, "hp", hp, engine.result)
            if not accepted or hp != [790, -755] or not engine.result or engine.result.get("winner") != 0:
                failures.append("round 15: engine outcome is not the expected fortress win 790 : -755")
    if failures:
        print("FAILED:", *failures, sep="\n  ")
        return 1
    print("OK: rounds 3-14 reproduced; round 15 = defence + padded kill; engine: fortress wins 790 : -755")
    return 0


if __name__ == "__main__":
    sys.exit(main())
