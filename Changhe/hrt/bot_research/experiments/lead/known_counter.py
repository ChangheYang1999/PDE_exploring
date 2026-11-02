"""Known-policy timing counter for lead exploitability screens (development only).

Wraps hrt-w3's ForecastTiming (bots/counters/forecast_timing.py, used unmodified): every round
the counter predicts the target's exact actions from a copy of the public observation, defends
against the target's resulting roster, and in round attack_round buys as many copies of `tier`
as attack_share of its gold allows, if they leak on the target's predicted post-action map.

    bot_research.experiments.lead.known_counter:@timing?model="v4b"&model_parameters={"spec_share":1.0}&attack_round=9&tier="tier5"&attack_share=1.0

The target is rebuilt from scratch for each prediction, so the forecast is exact only for
targets whose actions depend on the current observation alone (all lead v4/v4b/v5/v6 settings except
attack_mode="adaptive", which keeps state between rounds).
"""
from __future__ import annotations

from bot_research.bots.counters.forecast_timing import ForecastTiming
from bot_research.experiments.lead import v4, v4b, v5, v6

MODELS = {"v4": v4.make, "v4b": v4b.make, "v5": v5.make, "v6": v6.make}


class _Model:
    def __init__(self, name, parameters):
        if name not in MODELS:
            raise ValueError(f"unknown model {name}")
        self.name, self.parameters = name, dict(parameters or {})
        MODELS[name](**self.parameters)

    def __call__(self, observation):
        return MODELS[self.name](**self.parameters)(observation)


class SpecTiming(ForecastTiming):
    def __init__(self, model="v4", model_parameters=None, **parameters):
        super().__init__(**parameters)
        self.model = _Model(model, model_parameters)


def timing(**parameters):
    return SpecTiming(**parameters).decide
