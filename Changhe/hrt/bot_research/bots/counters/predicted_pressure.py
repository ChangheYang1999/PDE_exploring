"""Known-policy counter with exact current-action forecasts from public state.

Only an independently instantiated, archived policy is called. The counter
never accesses the real opponent, pending actions, or live engine state.
Its purchase search uses the frozen economy planner; the strength and risk
of the resulting whole-game strategy remain empirical questions.
"""
from __future__ import annotations
from copy import deepcopy
from td_game.actions import apply_action
from td_game.config import config_from_dict
from bot_research.bots.counters.snapshots.lead_planner_003 import Planner
from bot_research.bots.counters.visible_search import player_from_snapshot
from bot_research.bots.economy.frozen.v2.defense_plan import defend, saturate
from bot_research.bots.economy.frozen.v2.fastsim import MapModel, simulate
from bot_research.bots.economy.frozen.v2.threat import active_types, packages


class PredictedPressure:
    def __init__(self, model_params=None, attack_weight=4.0, defense_share=1.0,
                 attack_share=1.0, saturate_round=20, reserve=0, max_factories=80,
                 max_minions=500, attack_from=1, opening_units=0):
        self.model = Planner(**(model_params or {}))
        self.attack_weight = float(attack_weight)
        self.defense_share = float(defense_share)
        self.attack_share = float(attack_share)
        self.saturate_round = int(saturate_round)
        self.reserve = int(reserve)
        self.max_factories = int(max_factories)
        self.max_minions = int(max_minions)
        self.attack_from = int(attack_from)
        self.opening_units = int(opening_units)
        self.trace = []

    def decide(self, observation):
        rnd = observation['round']
        own = observation['player']
        me = observation['players'][own]
        rules = observation['rules']
        config = config_from_dict(rules)
        swapped = deepcopy(observation)
        swapped['player'] = 1-own
        prediction = self.model(swapped)
        enemy_state = player_from_snapshot(observation['players'][1-own])
        for action in prediction:
            apply_action(enemy_state, action, rnd, config)
        threat = [e.type for e in enemy_state.roster if e.bought_round <= rnd and
                  (e.expires_after_round is None or rnd <= e.expires_after_round)]
        enemy_buildings = [(b.x, b.y, b.type) for b in enemy_state.buildings]
        own_buildings = [(b['x'], b['y'], b['type']) for b in me['buildings']]
        gold = me['gold']
        actions = []
        my_types = active_types(me['roster'], rnd)
        if rnd == 1 and self.opening_units:
            n = min(self.opening_units, gold // rules['minions']['tier1']['cost'])
            actions += [{'op': 'buy_minion', 'type': 'tier1'}] * n
            gold -= n * rules['minions']['tier1']['cost']
            my_types += ['tier1'] * n
        budget = int(gold * self.defense_share)
        more, own_buildings, left, residual = defend(own_buildings, budget, threat, 0,
                                                     rules, cap=600, reserve=1600)
        actions += more
        gold -= budget-left
        if rnd >= self.saturate_round:
            more, own_buildings, gold, _ = saturate(own_buildings, gold, 1500, rules)
            actions += more
        attack_cost = 0
        attack_gain = 0
        selected = []
        if rnd >= self.attack_from:
            model = MapModel(enemy_buildings, rules)
            _, baseline = simulate(model, my_types, rules)
            budget = int(gold * self.attack_share)
            cap = min(self.max_minions, max(0, 1500-len(my_types)))
            choices = set()
            for tier, specification in rules['minions'].items():
                maximum = min(cap, budget // specification['cost'])
                for n in (1, 2, 4, 8, maximum//4, maximum//2, maximum):
                    if 0 < n <= maximum:
                        choices.add(tuple([tier] * n))
            if cap:
                choices.update(tuple(p) for p in packages(budget, rules['minions'], cap))
            best = (0, 0, 0)
            for sequence in sorted(choices):
                if not sequence:
                    continue
                cost = sum(rules['minions'][t]['cost'] for t in sequence)
                _, damage = simulate(model, my_types+list(sequence), rules)
                gain = damage-baseline
                # Damage now is certain only when the forecast is correct.
                # The finite coefficient is a tuning parameter, not a future-value proof.
                value = self.attack_weight*gain-cost if rnd < rules['globals']['max_rounds'] else gain
                key = (value, gain, -cost)
                if key > best:
                    best = key
                    selected, attack_cost, attack_gain = list(sequence), cost, gain
            actions += [{'op': 'buy_minion', 'type': t} for t in selected]
            gold -= attack_cost
        if rnd < 48:
            cost = rules['globals']['factory_cost']
            n = min(self.max_factories, gold // cost)
            if self.reserve:
                model = MapModel(own_buildings, rules)
                income = model.L + me['n_factories'] * rules['globals']['factory_income']
                n = min(n, max(0, (gold+income-self.reserve)//(cost-rules['globals']['factory_income'])))
            actions += [{'op': 'buy_factory'}] * n
        self.trace.append({'round': rnd, 'predicted_actions': prediction,
                           'forecast_defensive_damage': residual, 'attack_cost': attack_cost,
                           'forecast_attack_gain': attack_gain, 'purchased_types': selected})
        return actions


def make(**parameters):
    return PredictedPressure(**parameters).decide
