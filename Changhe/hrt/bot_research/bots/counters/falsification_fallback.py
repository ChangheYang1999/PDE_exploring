"""Stop catalogue evaluation permanently after its first observed falsification."""
from __future__ import annotations
from bot_research.bots.counters.identifying_opening import OpeningIdentifier
from bot_research.bots.counters.identifying_counter import purchase_signature
from bot_research.bots.defense.frozen.v13.fortress import make as fortress13
from bot_research.bots.economy.frozen.v9.econ9 import make as economy9


class FalsificationFallback:
    def __init__(self, fallback='economy9', fallback_parameters=None, **parameters):
        factories = {'fortress13': fortress13, 'economy9': economy9}
        if fallback not in factories:
            raise ValueError('Unknown fallback policy.')
        self.fallback_name = fallback
        self.fallback_factory = factories[fallback]
        self.fallback_parameters = dict(fallback_parameters or {})
        self.inner = OpeningIdentifier(**parameters)
        self.fallback = self.fallback_factory(**self.fallback_parameters)
        self.switched = False
        self.switch_round = None
        self.trace = []

    def decide(self, observation):
        rnd = observation['round']
        model = self.inner.inner
        if rnd == 1:
            self.switched = False
            self.switch_round = None
            self.fallback = self.fallback_factory(**self.fallback_parameters)
            self.trace = []
        if not self.switched and rnd > 1:
            actual = purchase_signature(observation['players'][1 - observation['player']], rnd - 1)
            contradicted = bool(model.pending) and not any(
                signature == actual for signature in model.pending.values())
            if contradicted or not model.active:
                self.switched = True
                self.switch_round = rnd
        if self.switched:
            actions = self.fallback(observation)
            self.trace.append({'round': rnd, 'active': [], 'eliminated': [],
                               'catalogue_reset': False, 'forecast_errors': [],
                               'predicted_actions': {}, 'forecast_residual_damage': None,
                               'attack': None, 'fallback_policy': self.fallback_name,
                               'fallback_switch_round': self.switch_round,
                               'catalogue_policy_calls': 0, 'fallback_policy_calls': 1})
            return actions
        actions = self.inner.decide(observation)
        self.trace.append({**self.inner.trace[-1], 'fallback_policy': None,
                           'fallback_switch_round': None,
                           'catalogue_policy_calls': len(self.inner.trace[-1]['predicted_actions']) + len(self.inner.trace[-1]['forecast_errors']),
                           'fallback_policy_calls': 0})
        return actions


def make(**parameters):
    return FalsificationFallback(**parameters).decide
