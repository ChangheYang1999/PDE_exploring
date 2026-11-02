"""Growth and repeated floods defended against the current visible roster.

No opponent implementation is loaded. The empty-action model means only
"assume no new purchases this round". Its full-action prediction is usually
wrong; it is used to reuse ForecastGrower's identical spending controller.
"""
from __future__ import annotations
from bot_research.bots.counters.forecast_grower import ForecastGrower


def no_new_purchases():
    return lambda observation: []


class VisibleGrower(ForecastGrower):
    def __init__(self, **parameters):
        if 'model_spec' in parameters or 'model_parameters' in parameters:
            raise ValueError('VisibleGrower does not accept an opponent model.')
        super().__init__(
            model_spec='bot_research.bots.counters.visible_grower:@no_new_purchases',
            **parameters)

    def decide(self, observation):
        actions = super().decide(observation)
        self.trace[-1]['defensive_information'] = 'visible roster; assumes no new purchases'
        return actions


def make(**parameters):
    return VisibleGrower(**parameters).decide
