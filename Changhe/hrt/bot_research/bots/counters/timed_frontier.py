"""Forecast-based timing attacks on public policies with wall-clock budgets.

Predictions may differ from actual target calls because of timing. Match
results remain valid, but no deterministic policy-equivalence claim follows.
"""
from bot_research.bots.counters.forecast_timing import ForecastTiming
from bot_research.bots.defense.frozen.v11.fortress import make as fortress11
from bot_research.bots.defense.frozen.v12.fortress import make as fortress12
from bot_research.bots.economy.frozen.v7.econ7 import make as economy7


def policy_factory(name,parameters=None):
    factories={'fortress11':fortress11,'fortress12':fortress12,'economy7':economy7}
    return factories[name](**dict(parameters or {}))


class ObservationModel:
    def __init__(self,name,parameters):
        self.name=name
        self.parameters=dict(parameters or {})

    def __call__(self,observation):
        return policy_factory(self.name,self.parameters)(observation)


class TimedKnown(ForecastTiming):
    def __init__(self,model='fortress12',model_parameters=None,**parameters):
        super().__init__(**parameters)
        self.model=ObservationModel(model,model_parameters)


def make(**parameters):
    return TimedKnown(**parameters).decide
