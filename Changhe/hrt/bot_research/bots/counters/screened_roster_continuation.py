"""Follow the selected C02 opening, change one roster order, then continue."""
from copy import deepcopy

from bot_research.bots.counters.archetypes import Archetype, Profile
from bot_research.bots.defense.frozen.v38.fortress import make as make_fortress
from bot_research.bots.economy.frozen.v20.econ20 import make as make_economy


ORDERS = {
    'screen': ('tier2', 'tier2', 'tier3'),
    'middle': ('tier2', 'tier3', 'tier2'),
    'front': ('tier3', 'tier2', 'tier2'),
}


class ScreenedRosterContinuation:
    def __init__(self, order='screen', continuation='original'):
        if order not in ORDERS or continuation not in ('original', 'fortress38', 'economy20'):
            raise ValueError('Unknown order or continuation.')
        self.order = ORDERS[order]
        self.opening = Archetype(Profile(growth_rounds=9, roster=('tier5', 'tier2'),
            defense='splash', defense_count=4, pulse_period=5, pulse_phase=1))
        self.continuation = continuation
        if continuation == 'fortress38':
            self.delegate = make_fortress()
        elif continuation == 'economy20':
            self.delegate = make_economy(free_fallback='zero', foreign_attack_from=11,
                doom='next', fac_cap=400, sat_reach=True, replan=True, foreign_sat_from=11)
        else:
            self.delegate = self.opening.decide

    def decide(self, observation):
        rnd = observation['round']
        if rnd < 6:
            return self.opening.decide(deepcopy(observation))
        if rnd == 6:
            gold = observation['players'][observation['player']]['gold']
            cost = sum(observation['rules']['minions'][tier]['cost'] for tier in self.order)
            if gold < cost:
                return []
            return [{'op': 'buy_minion', 'type': tier} for tier in self.order]
        return self.delegate(deepcopy(observation))


def make(**parameters):
    return ScreenedRosterContinuation(**parameters).decide
