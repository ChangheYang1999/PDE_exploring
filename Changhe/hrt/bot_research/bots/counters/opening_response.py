"""Fixed opening purchases followed by a frozen general policy.

These policies do not forecast the opponent. Opening labels describe only
fixed legal intentions; all returned actions are checked on an own-state
copy reconstructed from the public observation.
"""
from __future__ import annotations
from td_game.actions import apply_action
from td_game.config import config_from_dict
from bot_research.bots.counters.visible_search import player_from_snapshot
from bot_research.bots.defense.frozen.v18.fortress import make as fortress18
from bot_research.bots.economy.frozen.v13.econ13 import make as economy13


class OpeningResponse:
    def __init__(self, opening='mixed32', fallback='economy13', fallback_parameters=None):
        if opening not in ('mixed32', 'guard22', 'guard_poke5', 'factories'):
            raise ValueError('Unknown fixed opening.')
        factories = {'fortress18': fortress18, 'economy13': economy13}
        if fallback not in factories:
            raise ValueError('Unknown frozen continuation.')
        self.opening = opening
        self.fallback_factory = factories[fallback]
        self.parameters = dict(fallback_parameters or {})
        self.continuation = self.fallback_factory(**self.parameters)

    def decide(self, observation):
        if observation['round'] != 1:
            return self.continuation(observation)
        self.continuation = self.fallback_factory(**self.parameters)
        state = player_from_snapshot(observation['players'][observation['player']])
        config = config_from_dict(observation['rules'])
        intended = []
        if self.opening in ('guard22', 'guard_poke5'):
            intended.append({'op': 'build_turret', 'type': 'gun1', 'x': 3, 'y': 1})
        if self.opening == 'mixed32':
            kinds = ['tier1'] * 4 + ['tier2']
        elif self.opening == 'guard22':
            kinds = ['tier1'] * 2 + ['tier2']
        elif self.opening == 'guard_poke5':
            kinds = ['tier1']
        else:
            kinds = []
        intended.extend({'op': 'buy_minion', 'type': k} for k in kinds)
        actions = []
        for action in intended:
            if apply_action(state, action, 1, config)['accepted']:
                actions.append(action)
        while state.gold >= config.globals.factory_cost:
            action = {'op': 'buy_factory'}
            if not apply_action(state, action, 1, config)['accepted']:
                break
            actions.append(action)
        return actions


def make(**parameters):
    return OpeningResponse(**parameters).decide
