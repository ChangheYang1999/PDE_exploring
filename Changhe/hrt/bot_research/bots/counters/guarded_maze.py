"""A fixed-round splash guard added to the pinned maze grower."""
import hashlib
import json
from pathlib import Path
from td_game.actions import apply_action
from td_game.config import config_from_dict
from bot_research.bots.counters.maze_grower import MazeGrower
from bot_research.bots.counters.visible_search import player_from_snapshot

GUARD_DATA=Path(__file__).with_name('data')/'maze_guards_001.json'
GUARD_SHA256='3c3f2c8dbaf063f76ec5c55cacf7fa534f51dde68bce4cd8eeed6f2aa029cd1b'


class GuardedMaze(MazeGrower):
    def __init__(self, guard_round=3, **parameters):
        super().__init__(**parameters)
        self.guard_round=int(guard_round)
        if not 2<=self.guard_round<=self.growth_rounds:raise ValueError('Guard must follow opening and precede the flood.')
        raw=GUARD_DATA.read_bytes()
        if hashlib.sha256(raw).hexdigest()!=GUARD_SHA256:raise ValueError('Guard data checksum differs.')
        layout=parameters.get('layout','cash_rank_1')
        matches=[r for r in json.loads(raw)['layouts'] if r['layout']==layout]
        if len(matches)!=1:raise ValueError('No unique guard for this layout.')
        self.guard=tuple(matches[0]['selected']['cell'])

    def decide(self, observation):
        parent=super().decide(observation)
        if observation['round']!=self.guard_round:return parent
        state=player_from_snapshot(observation['players'][observation['player']])
        config=config_from_dict(observation['rules']);x,y=self.guard
        guard=dict(op='build_turret',type='splash',x=x,y=y)
        if not apply_action(state,guard,self.guard_round,config)['accepted']:return parent
        actions=[guard]
        for action in parent:
            if apply_action(state,action,self.guard_round,config)['accepted']:actions.append(action)
        return actions


def make(**parameters):return GuardedMaze(**parameters).decide
