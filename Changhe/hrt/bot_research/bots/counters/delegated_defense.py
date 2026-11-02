"""Keep the four-round counter opening, then use a frozen teammate defender."""
from copy import deepcopy
from bot_research.bots.counters.emergency_route_selector import EmergencyRouteSelector, visible_incoming
from bot_research.bots.economy.frozen.v20.econ20 import make as make_economy
from bot_research.bots.defense.frozen.v38.fortress import make as make_fortress


class DelegatedRouteSelector(EmergencyRouteSelector):
    def __init__(self, mode='adaptive', delegate='econ20'):
        super().__init__(mode=mode, emergency_rule='damage', emergency_from=5)
        if delegate not in ('econ20', 'fortress38', 'template'):
            raise ValueError('Unknown defensive continuation.')
        self.delegate_name = delegate
        if delegate == 'econ20':
            self.delegate = make_economy(free_fallback='zero', foreign_attack_from=11,
                doom='next', fac_cap=400, sat_reach=True, replan=True, foreign_sat_from=11)
        elif delegate == 'fortress38':
            self.delegate = make_fortress()
        else:
            self.delegate = None
        self.delegate_started = None
        self.delegation_trace = []

    def decide(self, observation):
        rnd, side = observation['round'], observation['player']
        damage, reason = None, None
        if self.delegate_name != 'template' and self.selected == 'early' and rnd >= 5:
            if self.delegate_started is None:
                if self.early.triggered_round is not None:
                    reason = 'existing_trigger'
                elif observation['players'][side]['hp'] > observation['players'][1-side]['hp']:
                    reason = 'positive_hp_lead'
                else:
                    damage = visible_incoming(observation)
                    if damage > 0:
                        reason = 'visible_damage'
                if reason is not None:
                    self.delegate_started = rnd
            if self.delegate_started is not None:
                actions = self.delegate(deepcopy(observation))
                self.trace.append(dict(round=rnd, selected=self.selected, projection=None))
                self.delegation_trace.append(dict(round=rnd, delegate=self.delegate_name,
                    started=self.delegate_started, trigger=reason, visible_incoming=damage))
                return actions
        actions = super().decide(observation)
        self.delegation_trace.append(dict(round=rnd, delegate=None, started=None,
                                         trigger=reason, visible_incoming=damage))
        return actions


def make(**parameters):
    return DelegatedRouteSelector(**parameters).decide
