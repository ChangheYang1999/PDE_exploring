"""Public-policy forecasting against explicitly frozen development opponents.

The model families below use observations only. Fortress v4/v6 and Planner
003 are stateless. Economy v4's sole flag says whether its opponent has ever
owned a turret. Buildings cannot be removed, so current n_turrets determines
that flag exactly on legal histories. Recreating its callable per observation
therefore preserves its decision without leaking simulated future state back
into a real decision. Saved matches check the predicted submissions directly.
"""
from __future__ import annotations

from bot_research.bots.counters.forecast_timing import ForecastTiming
from bot_research.bots.counters.forecast_schedule import ForecastSchedule
from bot_research.bots.counters.forecast_rollout import ForecastRollout
from bot_research.bots.counters.snapshots.lead_planner_003 import Planner, WALLS
from bot_research.bots.economy.frozen.v4.econ import make as economy_v4
from bot_research.bots.defense.frozen.v4.fortress import make as fortress_v4
from bot_research.bots.defense.frozen.v6.fortress import make as fortress_v6
from bot_research.bots.economy.frozen.v2.fastsim import MapModel


def policy_factory(name, parameters=None):
    parameters = dict(parameters or {})
    factories = {'planner003': Planner, 'econ_v4': economy_v4, 'fortress_v4': fortress_v4,
                 'fortress_v6': fortress_v6}
    if name not in factories:
        raise ValueError(f'Unsupported public model: {name}')
    return factories[name](**parameters)


class ObservationModel:
    def __init__(self, name, parameters=None):
        self.name = name
        self.parameters = dict(parameters or {})
        policy_factory(name, self.parameters)  # fail early on unknown parameters

    def __call__(self, observation):
        return policy_factory(self.name, self.parameters)(observation)


class KnownTiming(ForecastTiming):
    def __init__(self, model='econ_v4', model_parameters=None, **parameters):
        super().__init__(**parameters)
        self.model = ObservationModel(model, model_parameters)


class KnownSchedule(ForecastSchedule):
    def __init__(self, model='econ_v4', model_parameters=None, **parameters):
        super().__init__(**parameters)
        self.model = ObservationModel(model, model_parameters)


class KnownRollout(ForecastRollout):
    def __init__(self, model='econ_v4', model_parameters=None, **parameters):
        super().__init__(**parameters)
        self.model = ObservationModel(model, model_parameters)

    def saturated(self, game, opponent_side):
        # Only stop early for policies with a justified permanent-immunity rule.
        if self.model.name == 'planner003':
            occupied = {(b.x, b.y) for b in game.players[opponent_side].buildings}
            if not set(WALLS).issubset(occupied):
                return False
        elif self.model.name == 'econ_v4':
            if not self.model.parameters.get('lock', True):
                return False
        else:
            return False
        rules = game.config.to_dict()
        threshold = max(m['hp'] for m in rules['minions'].values())
        return all(MapModel([(b.x, b.y, b.type) for b in p.buildings], rules).splash_total >= threshold
                   for p in game.players)


def timing(**parameters):
    return KnownTiming(**parameters).decide


def schedule(**parameters):
    return KnownSchedule(**parameters).decide


def rollout(**parameters):
    return KnownRollout(**parameters).decide
