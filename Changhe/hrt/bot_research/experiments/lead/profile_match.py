"""Per-round decision times of player A in one match, and a cProfile of A's slowest call.

    .venv/bin/python -B -m bot_research.experiments.lead.profile_match SPEC_A SPEC_B [--top 5]

The match runs on the unchanged engine through td_game.runner.run_match with a log in
bot_research/tmp/. The slowest call is re-run on a deep copy of its observation under cProfile
(a fresh bot instance, so this is exact only for bots that keep no state between rounds).
"""
from __future__ import annotations

import argparse
import copy
import cProfile
import io
import pstats
import time
from pathlib import Path

from td_game.config import balanced_config
from td_game.runner import run_match

from bot_research.harness.match import resolve_spec

ROOT = Path(__file__).resolve().parents[3]


class Recorder:
    def __init__(self, decide):
        self.decide, self.calls = decide, []

    def __call__(self, obs):
        saved = copy.deepcopy(obs)
        t = time.perf_counter()
        out = self.decide(obs)
        self.calls.append((time.perf_counter() - t, obs["round"], saved))
        return out


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("spec_a")
    ap.add_argument("spec_b")
    ap.add_argument("--top", type=int, default=5)
    args = ap.parse_args(argv)
    rec = Recorder(resolve_spec(args.spec_a))
    out = ROOT / "bot_research" / "tmp" / f"profile-{int(time.time() * 1000)}.jsonl"
    engine = run_match(balanced_config(), [rec, resolve_spec(args.spec_b)], (args.spec_a, args.spec_b), out)
    print("result", engine.result, "rounds", engine.round, "hp", engine.players[0].hp, engine.players[1].hp)
    slow = sorted(rec.calls, key=lambda c: c[0], reverse=True)
    print("total A seconds %.2f over %d calls" % (sum(c[0] for c in rec.calls), len(rec.calls)))
    for s, r, _ in slow[: args.top]:
        print(f"round {r:2d}: {s:.2f} s")
    if slow:
        prof = cProfile.Profile()
        bot = resolve_spec(args.spec_a)
        prof.enable()
        bot(copy.deepcopy(slow[0][2]))
        prof.disable()
        buf = io.StringIO()
        pstats.Stats(prof, stream=buf).sort_stats("cumulative").print_stats(18)
        print(buf.getvalue())
    out.unlink(missing_ok=True)


if __name__ == "__main__":
    main()
