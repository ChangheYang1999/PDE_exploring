"""Delay guard00 to round four, buy one heavy, then call cold Fortress38.

The defender is constructed once with its original defaults. It consumes no
observations until round six and retains its private state afterward.
"""
from copy import deepcopy
from pathlib import Path
import json

from td_game.actions import apply_action
from td_game.config import config_from_dict
from bot_research.bots.counters.visible_search import player_from_snapshot
from bot_research.bots.defense.frozen.v38.fortress import make as make_defender


DATA = Path(__file__).with_name('data') / 'early_wall_guard_001.json'


class FourthRoundWall:
    def __init__(self):
        self.witness = deepcopy(next(
            witness for witness in json.loads(DATA.read_text())['witnesses']
            if witness['id'] == 'guard00'))
        self.defender = make_defender()
        self.trace = []
        self.filtered_proposals = []
        self.last_round = 0
        self.player = None
        self.defender_calls = 0
        self.defender_last_round = None

    def decide(self, observation):
        rnd, side = observation['round'], observation['player']
        if type(rnd) is not int or rnd != self.last_round + 1:
            raise ValueError('This counter requires consecutive rounds from round one.')
        if type(side) is not int or side not in (0, 1):
            raise ValueError('This counter requires physical player zero or one.')
        if self.player is not None and side != self.player:
            raise ValueError('This counter cannot change physical player assignments.')

        observed = deepcopy(observation)
        cfg = config_from_dict(observed['rules'])
        state = player_from_snapshot(observed['players'][side])
        proposed_actions = []
        rejected_proposals = []
        actions = []

        def submit(action):
            proposed_actions.append(deepcopy(action))
            event = apply_action(state, deepcopy(action), rnd, cfg)
            if event['accepted']:
                actions.append(deepcopy(action))
                return True
            rejection = dict(round=rnd, action=deepcopy(action), reason=event['reason'])
            rejected_proposals.append(deepcopy(rejection))
            self.filtered_proposals.append(deepcopy(rejection))
            return False

        defender_called = rnd >= 6
        if defender_called:
            phase = 'defender'
            proposals = self.defender(deepcopy(observed))
            if not isinstance(proposals, list):
                raise TypeError('The retained defender must return an ordered action list.')
            self.defender_calls += 1
            self.defender_last_round = rnd
            for action in proposals:
                submit(action)
        else:
            phase = 'factory_opening'
            if rnd == 4:
                phase = 'wall_opening'
                for x, y in self.witness['walls']:
                    submit(dict(op='build_wall', x=x, y=y))
                for turret in self.witness['turrets']:
                    submit(dict(op='build_turret', **deepcopy(turret)))
            if rnd == 5:
                phase = 'heavy_opening'
                if state.gold >= cfg.minions['tier4'].cost:
                    submit(dict(op='buy_minion', type='tier4'))
            while state.gold >= cfg.globals.factory_cost:
                if not submit(dict(op='buy_factory')):
                    break

        self.trace.append(dict(
            round=rnd, player=side, phase=phase, witness=self.witness['id'],
            defender_called=defender_called, defender_calls=self.defender_calls,
            defender_last_round=self.defender_last_round,
            proposed_actions=deepcopy(proposed_actions),
            rejected_proposals=deepcopy(rejected_proposals),
            submitted_actions=deepcopy(actions)))
        self.last_round, self.player = rnd, side
        return deepcopy(actions)


def make():
    return FourthRoundWall().decide
