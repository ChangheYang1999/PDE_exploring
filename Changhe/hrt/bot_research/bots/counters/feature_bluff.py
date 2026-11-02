"""A declared turret purchase followed by fixed economic growth and waves.

This policy probes the opponent's public ``ever owned a turret`` feature.
The off-route turret can reveal whether that coarse feature is exploitable;
it does not pretend that a full-game comparison isolates every consequence
of the purchase. All actions are checked on a reconstructed own-state copy.
"""
from __future__ import annotations

from td_game.actions import apply_action
from td_game.config import config_from_dict
from bot_research.bots.counters.visible_search import player_from_snapshot


class FeatureBluff:
    def __init__(self, turret_round=1, turret_x=0, turret_y=11, turret_kind='gun1',
                 growth_rounds=6, tier='tier5', factory_cap=2000, purchase_cap=1000):
        self.turret_round = int(turret_round)
        self.turret_x = int(turret_x)
        self.turret_y = int(turret_y)
        self.turret_kind = str(turret_kind)
        self.growth_rounds = int(growth_rounds)
        self.tier = str(tier)
        self.factory_cap = int(factory_cap)
        self.purchase_cap = int(purchase_cap)
        if self.turret_round < 0 or self.growth_rounds < 0:
            raise ValueError('Rounds must be nonnegative.')
        if self.factory_cap < 0 or self.purchase_cap < 0:
            raise ValueError('Purchase caps must be nonnegative.')

    def decide(self, observation):
        rnd = observation['round']
        state = player_from_snapshot(observation['players'][observation['player']])
        config = config_from_dict(observation['rules'])
        actions = []

        def add(action):
            accepted = apply_action(state, action, rnd, config)['accepted']
            if accepted:
                actions.append(action)
            return accepted

        if rnd == self.turret_round:
            add({'op': 'build_turret', 'type': self.turret_kind,
                 'x': self.turret_x, 'y': self.turret_y})
        if rnd <= self.growth_rounds:
            count = min(max(0, self.factory_cap - state.n_factories),
                        state.gold // config.globals.factory_cost)
            for _ in range(count):
                if not add({'op': 'buy_factory'}):
                    break
        else:
            count = min(self.purchase_cap, state.gold // config.minions[self.tier].cost)
            for _ in range(count):
                if not add({'op': 'buy_minion', 'type': self.tier}):
                    break
        return actions


def make(**parameters):
    return FeatureBluff(**parameters).decide
