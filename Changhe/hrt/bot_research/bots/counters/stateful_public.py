"""Public-history clone of an explicitly named deterministic stateful policy.

A single private model is called once for each reached standard-game round.
It receives only a copied public observation via ForecastTiming.predict.
The target's real object and pending submission are never accessed.
"""
from __future__ import annotations
from bot_research.bots.counters.public_factory import PublicFactoryModel, DEFAULT_MODEL
from bot_research.bots.counters.forecast_timing import ForecastTiming


class PersistentFactoryModel(PublicFactoryModel):
    def __init__(self, spec, parameters=None):
        super().__init__(spec, parameters)
        self.policy = self.factory(**self.parameters)
        self.last_round = 0
        self.player = None

    def __call__(self, observation):
        rnd = observation['round']
        side = observation['player']
        if rnd != self.last_round + 1:
            raise ValueError('Persistent public model requires exactly one call per round from round 1.')
        if self.player is not None and side != self.player:
            raise ValueError('Persistent public model cannot switch player assignments.')
        actions = self.policy(observation) if callable(self.policy) else self.policy.decide(observation)
        self.last_round = rnd
        self.player = side
        return actions


class StatefulPublicTiming(ForecastTiming):
    def __init__(self, model_spec=DEFAULT_MODEL, model_parameters=None, **parameters):
        super().__init__(**parameters)
        self.model = PersistentFactoryModel(model_spec, model_parameters)


def timing(**parameters):
    return StatefulPublicTiming(**parameters).decide
