"""Infer known policy families from visible purchases, then choose a response.

This is a counter-strategy experiment, not a guarantee that a static payoff
survives a mid-game policy switch. Player names are deliberately ignored.
Predictions use only fresh local player states built from public observations.
"""
from __future__ import annotations
from collections import Counter
from copy import deepcopy

from td_game.actions import apply_action
from td_game.config import config_from_dict
from bot_research.bots.counters.archetypes import Archetype, Profile, PROFILES
from bot_research.bots.counters.empirical_payoffs import NAMES, PAYOFFS
from bot_research.bots.counters.visible_search import player_from_snapshot


def signature(player, round_number):
    if isinstance(player, dict):
        return (player['n_factories'],
                tuple((b['type'], b['x'], b['y']) for b in player['buildings']),
                Counter(e['type'] for e in player['roster'] if e['bought_round'] == round_number))
    return (player.n_factories,
            tuple((b.type, b.x, b.y) for b in player.buildings),
            Counter(e.type for e in player.roster if e.bought_round == round_number))


def distance(a, b):
    return abs(a[0] - b[0]) + 3 * len(set(a[1]) ^ set(b[1])) + sum(abs(a[2][t] - b[2][t]) for t in set(a[2]) | set(b[2]))


class PosteriorResponse:
    def __init__(self, opening='growth', discount=0.9, tolerance=0.0, fixed=None):
        self.opening = opening
        self.discount = float(discount)
        self.tolerance = float(tolerance)
        self.fixed = fixed
        self.scores = {name: 0.0 for name in NAMES}
        self.pending = {}
        self.trace = []

    def decide(self, observation):
        round_number = observation['round']
        enemy_index = 1 - observation['player']
        if round_number == 1:
            self.scores = {name: 0.0 for name in NAMES}
            self.pending = {}
            self.trace = []
        if self.pending:
            actual = signature(observation['players'][enemy_index], round_number - 1)
            for name in NAMES:
                self.scores[name] = self.discount * self.scores[name] + distance(actual, self.pending[name])
        best = min(self.scores.values())
        possible = [name for name in NAMES if self.scores[name] <= best + self.tolerance]
        indices = [NAMES.index(name) for name in possible]
        def grade(name):
            values = [PAYOFFS[name][i] for i in indices]
            return min(values), sum(values) / len(values), sum(PAYOFFS[name]), name
        mode = self.fixed or max(NAMES, key=grade)
        # Build predictions from a swapped public observation. Local action
        # application does not touch the live game or invoke the real opponent.
        enemy_obs = deepcopy(observation)
        enemy_obs['player'] = enemy_index
        config = config_from_dict(enemy_obs['rules'])
        pending = {}
        for name in NAMES:
            state = player_from_snapshot(enemy_obs['players'][enemy_index])
            actions = Archetype(PROFILES[name]).decide(enemy_obs)
            for action in actions:
                apply_action(state, action, round_number, config)
            pending[name] = signature(state, round_number)
        self.pending = pending
        self.trace.append({'round': round_number, 'possible': possible, 'mode': mode,
                           'minimum_mismatch': best, 'scores': dict(self.scores)})
        if round_number == 1:
            opening_profile = Profile(growth_rounds=1, defense='splash' if self.opening == 'splash' else '',
                                      defense_count=int(self.opening == 'splash'))
            return Archetype(opening_profile).decide(observation)
        return Archetype(PROFILES[mode]).decide(observation)


def make(opening='growth', discount=0.9, tolerance=0.0, fixed=None):
    return PosteriorResponse(opening, discount, tolerance, fixed).decide


_instances = {}


def decide(observation):
    player = observation['player']
    if observation['round'] == 1 or player not in _instances:
        _instances[player] = PosteriorResponse()
    return _instances[player].decide(observation)
