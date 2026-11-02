"""Forecast timing counters with an explicitly named public model factory.

Use only observation-based factories whose relevant state can be reconstructed
from the current observation. A fresh model is made per prediction. Timed or
stateful models can disagree with the target; evaluators must record that.
"""
from __future__ import annotations
import importlib
from bot_research.bots.counters.forecast_timing import ForecastTiming
from bot_research.bots.counters.mixed_timing import MixedTiming

DEFAULT_MODEL = 'bot_research.bots.defense.frozen.v15.fortress:@make'


class PublicFactoryModel:
    def __init__(self, spec, parameters=None):
        module, separator, function = spec.partition(':')
        if not separator or not function.startswith('@') or '?' in function:
            raise ValueError('Name an explicit module:@factory and pass parameters separately.')
        self.spec = spec
        self.parameters = dict(parameters or {})
        self.factory = getattr(importlib.import_module(module), function[1:])
        if not callable(self.factory):
            raise ValueError('Public model factory must be callable.')

    def __call__(self, observation):
        policy = self.factory(**self.parameters)
        return policy(observation) if callable(policy) else policy.decide(observation)


class PublicTiming(ForecastTiming):
    def __init__(self, model_spec=DEFAULT_MODEL, model_parameters=None, **parameters):
        super().__init__(**parameters)
        self.model = PublicFactoryModel(model_spec, model_parameters)


class PublicMixed(MixedTiming):
    def __init__(self, model_spec=DEFAULT_MODEL, model_parameters=None, **parameters):
        super().__init__(**parameters)
        self.model = PublicFactoryModel(model_spec, model_parameters)


def timing(**parameters):
    return PublicTiming(**parameters).decide


def mixed(**parameters):
    return PublicMixed(**parameters).decide
