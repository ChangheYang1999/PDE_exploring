"""Forecast-free single-wave opening followed by the frozen safety builder.

This generalizes PokeLock to a chosen minion tier. Once our map is immune and
our only purchased roster has expired, both HP values are fixed under this
policy: we buy no further attackers and leave the immune map unchanged.
"""
from __future__ import annotations
from bot_research.bots.counters.poke_lock import PokeLock
from bot_research.bots.economy.frozen.v2.fastsim import MapModel
from bot_research.bots.economy.frozen.v2.threat import active_types


class OpeningLock(PokeLock):
    def __init__(self, opening_tier='tier2', opening_units=1, **parameters):
        super().__init__(opening_units=opening_units, **parameters)
        self.opening_tier = opening_tier

    def decide(self, observation):
        me = observation['players'][observation['player']]
        rules = observation['rules']
        if observation['round'] == 1:
            cost = rules['minions'][self.opening_tier]['cost']
            count = min(self.opening_units, me['gold'] // cost)
            gold = me['gold'] - count * cost
            factories = min(self.max_factories, gold // rules['globals']['factory_cost'])
            return ([{'op': 'buy_minion', 'type': self.opening_tier}] * count
                    + [{'op': 'buy_factory'}] * factories)
        if not active_types(me['roster'], observation['round']):
            model = MapModel([(b['x'], b['y'], b['type']) for b in me['buildings']], rules)
            if model.splash_total >= max(m['hp'] for m in rules['minions'].values()):
                return []
        return super().decide(observation)


def make(**parameters):
    return OpeningLock(**parameters).decide
