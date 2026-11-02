"""One timed purchase followed by defense against a public frozen policy.

The private opponent model receives only a copy of the public observation.
An imagined PlayerState is reconstructed from that observation; no live game
state, opponent instance, pending submission, or external data is accessed.
"""
from __future__ import annotations
from copy import deepcopy
from td_game.actions import apply_action
from td_game.config import config_from_dict
from bot_research.bots.counters.snapshots.lead_planner_003 import Planner
from bot_research.bots.counters.visible_search import player_from_snapshot
from bot_research.bots.economy.frozen.v2.defense_plan import defend, saturate
from bot_research.bots.economy.frozen.v2.fastsim import MapModel, simulate
from bot_research.bots.economy.frozen.v2.threat import active_types


def predict(observation, model):
    enemy = 1 - observation['player']
    copied = deepcopy(observation)
    copied['player'] = enemy
    actions = model(copied)
    state = player_from_snapshot(observation['players'][enemy])
    config = config_from_dict(observation['rules'])
    for action in actions:
        event = apply_action(state, action, observation['round'], config)
        if not event['accepted']:
            raise ValueError('Private model predicted a rejected action.')
    return actions, state


class ForecastTiming:
    def __init__(self, attack_round=6, tier='tier5', attack_share=0.5, count_cap=200,
                 model_lam=1.0, model_kappa=4.0, saturate_round=20,
                 max_factories=80, defense_first=False):
        self.attack_round = int(attack_round)
        self.tier = tier
        self.attack_share = float(attack_share)
        self.count_cap = int(count_cap)
        self.model = Planner(lam=float(model_lam), kappa=float(model_kappa))
        self.saturate_round = int(saturate_round)
        self.max_factories = int(max_factories)
        self.defense_first = bool(defense_first)
        self.trace = []

    def decide(self, obs):
        rnd = obs['round']
        me = obs['players'][obs['player']]
        rules = obs['rules']
        predicted, enemy = predict(obs, self.model)
        threat = [e.type for e in enemy.roster if e.active(rnd)]
        buildings = [(b['x'], b['y'], b['type']) for b in me['buildings']]
        gold = me['gold']
        actions = []
        residual = 0
        if self.defense_first:
            more, buildings, gold, residual = defend(buildings, gold, threat, 0, rules, reserve=1600)
            actions += more
        count, gain = 0, 0
        if rnd == self.attack_round:
            cost = rules['minions'][self.tier]['cost']
            count = min(self.count_cap, int(gold * self.attack_share) // cost)
            if count:
                model = MapModel([(b.x, b.y, b.type) for b in enemy.buildings], rules)
                own_types = active_types(me['roster'], rnd)
                baseline = simulate(model, own_types, rules)[1]
                gain = simulate(model, own_types + [self.tier] * count, rules)[1] - baseline
                if gain <= 0:
                    count = 0
            actions += [{'op': 'buy_minion', 'type': self.tier}] * count
            gold -= count * cost
        if not self.defense_first:
            more, buildings, gold, residual = defend(buildings, gold, threat, 0, rules, reserve=1600)
            actions += more
        if rnd >= self.saturate_round:
            more, buildings, gold, _ = saturate(buildings, gold, 1500, rules)
            actions += more
        if rnd < 48:
            count_factories = min(self.max_factories, gold // rules['globals']['factory_cost'])
            actions += [{'op': 'buy_factory'}] * count_factories
        self.trace.append({'round': rnd, 'predicted_actions': predicted,
                           'attack_count': count, 'attack_tier': self.tier,
                           'forecast_attack_gain': gain, 'forecast_residual_damage': residual})
        return actions


def make(**parameters):
    return ForecastTiming(**parameters).decide
