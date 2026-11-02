"""Check that two bot specs submit identical actions, round by round, against the same opponents.

    .venv/bin/python -B -m bot_research.experiments.lead.same_actions SPEC1 SPEC2 OPPONENT [...]

For every opponent and seat, plays SPEC1 against it on the unchanged engine, then SPEC2, and
compares the full per-round action lists of the candidate and of the opponent (so the comparison
covers the whole trajectory, not just the result). Prints one line per pairing and exits 1 on
any difference.
"""
from __future__ import annotations

import sys

from td_bots.protocol import collect_actions
from td_game.config import balanced_config
from td_game.engine import Engine

from bot_research.harness.match import resolve_spec


def trajectory(spec_a, spec_b):
    engine = Engine(balanced_config(), ("A", "B"))
    bots = [type("B", (), {"decide": staticmethod(resolve_spec(s))})() for s in (spec_a, spec_b)]
    out = []
    while engine.result is None:
        obs = [engine.observation(p) for p in (0, 1)]
        actions, errs = collect_actions(bots, obs)
        out.append(actions)
        engine.play_round(actions, errs)
    return out, engine.result


def main(argv=None):
    argv = list(sys.argv[1:] if argv is None else argv)
    s1, s2, opps = argv[0], argv[1], argv[2:]
    bad = 0
    for opp in opps:
        for side in (0, 1):
            pair = (lambda s: (s, opp) if side == 0 else (opp, s))
            t1, r1 = trajectory(*pair(s1))
            t2, r2 = trajectory(*pair(s2))
            same = t1 == t2 and r1 == r2
            bad += not same
            print(f"{'same' if same else 'DIFFERENT'} side {side} rounds {len(t1)}/{len(t2)} vs {opp}", flush=True)
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
