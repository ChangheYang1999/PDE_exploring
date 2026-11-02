"""Timed legal splash upgrades, with a fixed economy and tier5-wave policy."""
import hashlib
import json
from pathlib import Path
from td_game.actions import apply_action
from td_game.config import config_from_dict
from bot_research.bots.counters.maze_grower import MazeGrower
from bot_research.bots.counters.visible_search import player_from_snapshot

DATA = Path(__file__).with_name('data') / 'guard_ladder_001.json'
DATA_SHA256 = '47b8155c77ed465e1e636f87e5ad40c6a12b109ae3dea9e11675d9126bd34541'


class GuardLadder(MazeGrower):
    def __init__(self, upgrades=((4, 1), (6, 2), (9, 5)), **parameters):
        if parameters.get('layout', 'empty') != 'empty':
            raise ValueError('This guard certificate uses the empty wall layout.')
        parameters['layout'] = 'empty'
        super().__init__(**parameters)
        self.upgrades = tuple(tuple(map(int, pair)) for pair in upgrades)
        if not self.upgrades or any(len(pair) != 2 for pair in self.upgrades):
            raise ValueError('Each upgrade is a round and cumulative guard count.')
        rounds, counts = zip(*self.upgrades)
        if (list(rounds) != sorted(set(rounds)) or min(rounds) < 2 or max(rounds) > 50
                or list(counts) != sorted(counts) or min(counts) < 1 or max(counts) > 5):
            raise ValueError('Require increasing rounds 2..50 and nondecreasing counts 1..5.')
        raw = DATA.read_bytes()
        if hashlib.sha256(raw).hexdigest() != DATA_SHA256:
            raise ValueError('Guard-ladder certificate differs.')
        self.guards = tuple(tuple(cell) for cell in json.loads(raw)['guards'])

    def decide(self, observation):
        parent = super().decide(observation)
        rnd = observation['round']
        target = dict(self.upgrades).get(rnd)
        if target is None:
            return parent
        state = player_from_snapshot(observation['players'][observation['player']])
        cfg = config_from_dict(observation['rules'])
        actions = []
        occupied = {(b.x, b.y): b.type for b in state.buildings}
        for x, y in self.guards[:target]:
            if occupied.get((x, y)) == 'splash':
                continue
            action = dict(op='build_turret', type='splash', x=x, y=y)
            if not apply_action(state, action, rnd, cfg)['accepted']:
                break
            actions.append(action)
            occupied[(x, y)] = 'splash'
        for action in parent:
            if apply_action(state, action, rnd, cfg)['accepted']:
                actions.append(action)
        return actions


def make(**parameters):
    return GuardLadder(**parameters).decide
