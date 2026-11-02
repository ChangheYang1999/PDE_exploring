"""Frozen deterministic frontier models for development counter searches.

Both target policies are stateless functions of the public observation.
The lead snapshot preserves the source bytes captured during development;
its source hash is recorded with every experiment. Neither model uses the
wall-clock search limits of later defense versions.
"""
from __future__ import annotations
from bot_research.bots.counters.forecast_timing import ForecastTiming
from bot_research.bots.counters.snapshots.lead_four_001 import make as lead_four_001
from bot_research.bots.defense.frozen.v8.fortress import make as fortress_v8


def policy_factory(name, parameters=None):
    factories={'lead_four_001':lead_four_001,'fortress_v8':fortress_v8}
    if name not in factories:
        raise ValueError(f'Unsupported frozen frontier model: {name}')
    return factories[name](**dict(parameters or {}))


class ObservationModel:
    def __init__(self,name,parameters=None):
        self.name=name
        self.parameters=dict(parameters or {})
        policy_factory(name,self.parameters)

    def __call__(self,observation):
        return policy_factory(self.name,self.parameters)(observation)


class KnownTiming(ForecastTiming):
    def __init__(self,model='lead_four_001',model_parameters=None,**parameters):
        super().__init__(**parameters)
        self.model=ObservationModel(model,model_parameters)


def timing(**parameters):
    return KnownTiming(**parameters).decide
