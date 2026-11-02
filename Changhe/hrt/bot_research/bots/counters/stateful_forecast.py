"""A timing counter to the public adapting counter, using an independent clone.

The clone is called once per actual round on the reconstructed public enemy
observation. Its state is never read from the real opponent. See the informal
proof in experiments/validation/analysis/stateful_forecast/PROOF.md.
"""
from __future__ import annotations
from bot_research.bots.counters.forecast_timing import ForecastTiming
from bot_research.bots.counters.identifying_counter import IdentifyingCounter


def policy_factory(model='identifying_counter',parameters=None):
    if model!='identifying_counter':
        raise ValueError('Unknown public stateful model.')
    return IdentifyingCounter(**dict(parameters or {})).decide


class StatefulTiming(ForecastTiming):
    def __init__(self,model='identifying_counter',model_parameters=None,**parameters):
        super().__init__(**parameters)
        self.model=policy_factory(model,model_parameters)


def make(**parameters):
    return StatefulTiming(**parameters).decide
