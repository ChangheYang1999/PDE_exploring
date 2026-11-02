"""Target a public deterministic policy with an early hit and forecast defense.

The model is an archived copy of a published research policy, instantiated
privately. It receives only the same public observation with player reversed.
No live engine, opponent object, submitted actions, or call stack is inspected.
This is a deliberately narrow counter, not a general opponent model.
"""
from __future__ import annotations
from copy import deepcopy

from td_game.actions import apply_action
from td_game.config import config_from_dict
from bot_research.bots.counters.snapshots.lead_planner_001 import Planner
from bot_research.bots.counters.visible_search import player_from_snapshot
from bot_research.bots.economy.defense_plan import defend, saturate
from bot_research.bots.economy.fastsim import MapModel
from bot_research.bots.economy.threat import active_types


class ForecastLock:
    def __init__(self, opening_units=6, reserve=0, saturate_round=40, max_factories=80):
        self.opening_units = int(opening_units)
        self.reserve = int(reserve)
        self.saturate_round = int(saturate_round)
        self.max_factories = int(max_factories)
        self.model = Planner()
        self.trace = []

    def decide(self, observation):
        r = observation['round']
        if r == 1:
            self.trace = []
        own_index = observation['player']
        enemy_index = 1 - own_index
        me = observation['players'][own_index]
        rules = observation['rules']
        gold = me['gold']
        enemy_obs = deepcopy(observation)
        enemy_obs['player'] = enemy_index
        predicted = self.model(enemy_obs)
        enemy_state = player_from_snapshot(observation['players'][enemy_index])
        config = config_from_dict(rules)
        for action in predicted:
            apply_action(enemy_state, action, r, config)
        threat = [e.type for e in enemy_state.roster if e.bought_round <= r and
                  (e.expires_after_round is None or r <= e.expires_after_round)]
        buildings = [(b['x'], b['y'], b['type']) for b in me['buildings']]
        actions = []
        if r == 1:
            n = min(self.opening_units, gold // rules['minions']['tier1']['cost'])
            actions += [{'op': 'buy_minion', 'type': 'tier1'}] * n
            gold -= n * rules['minions']['tier1']['cost']
        more, buildings, gold, residual = defend(buildings, gold, threat, 0, rules, reserve=1600)
        actions += more
        if r >= self.saturate_round:
            more, buildings, gold, _ = saturate(buildings, gold, 1500, rules)
            actions += more
        if r < 48:
            cost = rules['globals']['factory_cost']
            n = min(self.max_factories, gold // cost)
            # Keep the next visible gold above a specified threshold when
            # feasible. Every new factory spends 20 now and returns 15 now.
            if self.reserve and r >= 2:
                model = MapModel(buildings, rules)
                next_without_spend = gold + model.L + me['n_factories'] * rules['globals']['factory_income']
                margin = cost - rules['globals']['factory_income']
                n = min(n, max(0, (next_without_spend-self.reserve)//margin))
            actions += [{'op': 'buy_factory'}] * n
        self.trace.append({'round': r, 'predicted_actions': predicted,
                           'forecast_incoming_types': threat, 'forecast_residual_damage': residual})
        return actions


def make(opening_units=6, reserve=0, saturate_round=40, max_factories=80):
    return ForecastLock(opening_units, reserve, saturate_round, max_factories).decide
