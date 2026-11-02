"""Cheap guard with a bounded first-round wall investment.

A fixed prefix of a two-barrier layout spends only the gold remaining after
one gun1, one tier1, and the usual factory purchases. The continuation is
frozen economy13. Every intended opening action is checked on a reconstructed
own-state copy; opponent state is not simulated or read outside the observation.
"""
from __future__ import annotations
from td_game.actions import apply_action
from td_game.config import config_from_dict
from bot_research.bots.counters.visible_search import player_from_snapshot
from bot_research.bots.counters.opening_response import OpeningResponse


class GuardWalls:
    def __init__(self, wall_cap=15):
        self.wall_cap = int(wall_cap)
        if not 0 <= self.wall_cap <= 20:
            raise ValueError('wall_cap must be between zero and twenty.')
        self.policy = OpeningResponse(opening='guard_poke5', fallback='economy13')

    def decide(self, observation):
        actions = self.policy.decide(observation)
        if observation['round'] != 1 or not self.wall_cap:
            return actions
        config = config_from_dict(observation['rules'])
        state = player_from_snapshot(observation['players'][observation['player']])
        for action in actions:
            if not apply_action(state, action, 1, config)['accepted']:
                raise RuntimeError('The base opening produced an invalid action.')
        walls = [(x, 1) for x in range(10)] + [(x, 3) for x in range(11, 1, -1)]
        built = 0
        for x, y in walls:
            if built >= self.wall_cap:
                break
            action = {'op': 'build_wall', 'x': x, 'y': y}
            if apply_action(state, action, 1, config)['accepted']:
                actions.append(action)
                built += 1
        return actions


def make(**parameters):
    return GuardWalls(**parameters).decide
