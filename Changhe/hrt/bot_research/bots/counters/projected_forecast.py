"""Controlled projections of a persistent public opponent forecast.

The minion-only and non-minion projections still advance the complete private
model once per round. Its complete prediction is retained for validation but
only the selected actions reach the controller's planning simulation. The
opening-only control never evaluates an opponent model.
"""
from copy import deepcopy
from bot_research.bots.counters.forecast_timing import ForecastTiming
from bot_research.bots.counters.stateful_public import PersistentFactoryModel


class ProjectedModel:
    def __init__(self, model, projection):
        if projection not in ('minions', 'nonminions'):
            raise ValueError('Unknown action projection.')
        self.model = model
        self.projection = projection
        self.full_prediction = None

    def __call__(self, observation):
        self.full_prediction = deepcopy(self.model(observation))
        wanted = self.projection == 'minions'
        return [deepcopy(a) for a in self.full_prediction
                if (a['op'] == 'buy_minion') == wanted]


class OpeningModel:
    def __init__(self):
        self.last_round = 0
        self.player = None
        self.full_prediction = None

    def __call__(self, observation):
        rnd, side = observation['round'], observation['player']
        if rnd != self.last_round + 1 or self.player not in (None, side):
            raise ValueError('Opening model requires one ordered call per round.')
        self.last_round, self.player = rnd, side
        return [{'op': 'buy_minion', 'type': 'tier1'} for _ in range(3)] if rnd == 1 else []


class ProjectedTiming(ForecastTiming):
    def __init__(self, projection, model_spec=None, model_parameters=None, **parameters):
        super().__init__(**parameters)
        self.projection = projection
        if projection == 'opening':
            self.model = OpeningModel()
        else:
            if model_spec is None:
                raise ValueError('A public model specification is required.')
            self.model = ProjectedModel(PersistentFactoryModel(model_spec, model_parameters), projection)

    def decide(self, observation):
        actions = super().decide(observation)
        self.trace[-1].update(projection=self.projection,
                             full_predicted_actions=deepcopy(self.model.full_prediction))
        return actions


def timing(**parameters):
    return ProjectedTiming(**parameters).decide
