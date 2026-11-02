"""Timing and schedule controls assuming no new opponent purchases.

The spending code is inherited unchanged from the exact-model counter.
Only the public-action prediction is replaced by an empty submission.
"""
from bot_research.bots.counters.stateful_public import StatefulPublicTiming
from bot_research.bots.counters.stateful_schedule import StatefulSchedule

EMPTY_MODEL = 'bot_research.bots.counters.visible_forecast_v2:@no_new_purchases'


def checked(parameters):
    if {'model_spec', 'model_parameters'} & set(parameters):
        raise ValueError('Visible-roster controls do not accept an opponent model.')
    return parameters


class VisibleTiming(StatefulPublicTiming):
    def __init__(self, **parameters):
        super().__init__(model_spec=EMPTY_MODEL, **checked(parameters))


class VisibleSchedule(StatefulSchedule):
    def __init__(self, **parameters):
        super().__init__(model_spec=EMPTY_MODEL, **checked(parameters))


def timing(**parameters):
    return VisibleTiming(**parameters).decide


def schedule(**parameters):
    return VisibleSchedule(**parameters).decide


def no_new_purchases():
    return lambda observation: []
