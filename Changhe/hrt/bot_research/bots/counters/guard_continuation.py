"""A fixed cheap opening guard followed by a selected frozen policy.

This tests whether later defense planning fixes weaknesses of the same
opening. The round-one action list is inherited unchanged from the
previously checked OpeningResponse policy. No opponent model is loaded.
"""
from __future__ import annotations
from bot_research.bots.counters.opening_response import OpeningResponse
from bot_research.bots.economy.frozen.v13.econ13 import make as economy13
from bot_research.bots.economy.frozen.v15.econ15 import make as economy15
from bot_research.bots.defense.frozen.v21.fortress import make as fortress21


class GuardContinuation:
    def __init__(self, continuation='economy15', parameters=None):
        factories = {'economy13': economy13, 'economy15': economy15,
                     'fortress21': fortress21}
        if continuation not in factories:
            raise ValueError('Unknown frozen continuation.')
        self.factory = factories[continuation]
        self.parameters = dict(parameters or {})
        self.opening = OpeningResponse(opening='guard_poke5', fallback='economy13')
        self.policy = self.factory(**self.parameters)

    def decide(self, observation):
        if observation['round'] == 1:
            self.policy = self.factory(**self.parameters)
            return self.opening.decide(observation)
        return self.policy(observation)


def make(**parameters):
    return GuardContinuation(**parameters).decide
