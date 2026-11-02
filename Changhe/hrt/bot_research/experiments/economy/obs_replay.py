"""Replay a match (optionally under a harness scenario) and return an observation.

    from bot_research.experiments.economy.obs_replay import observation_at
    obs = observation_at(spec_a, spec_b, round_number, player, scenario="mirror:1:2")

Same loop as the lead's experiments/lead/obs_at.py (unchanged engine, balanced
rules, fresh bots from the harness spec resolver), plus the harness's scripted
openings (harness/scenarios.py make_overrides) applied the way
harness/match.py's TimedBot applies them: the bot is called and its return is
replaced by the scripted list while one exists. Used for loss review only.
"""
from __future__ import annotations

import copy

from td_bots.protocol import collect_actions
from td_game.config import balanced_config
from td_game.engine import Engine

from bot_research.harness import scenarios
from bot_research.harness.match import resolve_spec


class _Bot:
    def __init__(self, decide, override):
        self._decide, self._override = decide, override

    def decide(self, observation):
        scripted = self._override(copy.deepcopy(observation)) if self._override else None
        actions = self._decide(observation)
        return scripted if scripted is not None else actions


def observation_at(spec_a, spec_b, round_number, player=0, scenario=None):
    engine = Engine(balanced_config(), ("A", "B"))
    over = scenarios.make_overrides(scenario) if scenario else (None, None)
    bots = [_Bot(resolve_spec(s), o) for s, o in zip((spec_a, spec_b), over)]
    while engine.result is None:
        obs = [engine.observation(p) for p in (0, 1)]
        if obs[0]["round"] == round_number:
            return obs[player]
        actions, errors = collect_actions(bots, obs)
        engine.play_round(actions, errors)
    return None
