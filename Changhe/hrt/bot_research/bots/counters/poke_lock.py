"""Small first-round attack followed by defense, growth and splash immunity.

This policy does not model the opponent's decision function. It is an ablation
of forecast_lock: decisions use only visible roster, gold and own resources.
The defensive component is the economy lane's explicitly frozen v2 planner.
"""
from __future__ import annotations
from bot_research.bots.economy.frozen.v2.defense_plan import defend, saturate
from bot_research.bots.economy.frozen.v2.fastsim import MapModel
from bot_research.bots.economy.frozen.v2.threat import active_types


class PokeLock:
    def __init__(self, opening_units=2, reserve=180, saturate_round=20, phi=0.0,
                 late_round=51, max_factories=80):
        self.opening_units = int(opening_units)
        self.reserve = int(reserve)
        self.saturate_round = int(saturate_round)
        self.phi = float(phi)
        self.late_round = int(late_round)
        self.max_factories = int(max_factories)

    def decide(self, observation):
        r = observation['round']
        me = observation['players'][observation['player']]
        enemy = observation['players'][1-observation['player']]
        rules = observation['rules']
        gold = me['gold']
        actions = []
        buildings = [(b['x'], b['y'], b['type']) for b in me['buildings']]
        if r == 1:
            n = min(self.opening_units, gold // rules['minions']['tier1']['cost'])
            actions += [{'op': 'buy_minion', 'type': 'tier1'}] * n
            gold -= n * rules['minions']['tier1']['cost']
        else:
            factor = self.phi if r < self.late_round else 1.0
            more, buildings, gold, _ = defend(buildings, gold,
                active_types(enemy['roster'], r), int(factor * enemy['gold']), rules,
                cap=600, reserve=1600)
            actions += more
        if r >= self.saturate_round:
            more, buildings, gold, _ = saturate(buildings, gold, 1500, rules)
            actions += more
        if r < 48:
            cost = rules['globals']['factory_cost']
            n = min(self.max_factories, gold // cost)
            if self.reserve and r >= 2:
                model = MapModel(buildings, rules)
                income = model.L + me['n_factories'] * rules['globals']['factory_income']
                marginal_cost = cost-rules['globals']['factory_income']
                n = min(n, max(0, (gold+income-self.reserve)//marginal_cost))
            actions += [{'op': 'buy_factory'}] * n
        return actions


def make(opening_units=2, reserve=180, saturate_round=20, phi=0.0,
         late_round=51, max_factories=80):
    return PokeLock(opening_units, reserve, saturate_round, phi, late_round, max_factories).decide
