"""Replay a match on the unchanged engine and return the observation of a given round.

    from bot_research.experiments.lead.obs_at import observation_at
    obs = observation_at(spec_a, spec_b, round_number, player)

Both bots are fresh instances from the harness spec resolver; the engine is the
bundled one with balanced rules. Used for loss review only.
"""
from __future__ import annotations

from td_bots.protocol import collect_actions
from td_game.config import balanced_config
from td_game.engine import Engine

from bot_research.harness.match import resolve_spec


def observation_at(spec_a, spec_b, round_number, player=0):
    engine = Engine(balanced_config(), ("A", "B"))
    bots = [type("B", (), {"decide": staticmethod(resolve_spec(s))})() for s in (spec_a, spec_b)]
    while engine.result is None:
        obs = [engine.observation(p) for p in (0, 1)]
        if obs[0]["round"] == round_number:
            return obs[player]
        actions, errors = collect_actions(bots, obs)
        engine.play_round(actions, errors)
    return None
