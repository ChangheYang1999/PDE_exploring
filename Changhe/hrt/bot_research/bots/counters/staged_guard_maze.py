"""A grower with a pinned, legally checked sequence of timed splash guards."""
import hashlib,json
from pathlib import Path
from td_game.actions import apply_action
from td_game.config import config_from_dict
from bot_research.bots.counters.maze_grower import MazeGrower
from bot_research.bots.counters.visible_search import player_from_snapshot

DATA=Path(__file__).with_name('data')/'staged_guards_001.json'
DATA_SHA256='fdc86066da88290d4d0c82f1c53895174f0ee38250ee18fb29fd425eba8c8398'


class StagedGuardMaze(MazeGrower):
    def __init__(self,guard_rounds=(4,6),**parameters):
        super().__init__(**parameters)
        self.guard_rounds=tuple(map(int,guard_rounds))
        if not self.guard_rounds or len(self.guard_rounds)>3 or sorted(set(self.guard_rounds))!=list(self.guard_rounds) or min(self.guard_rounds)<2 or max(self.guard_rounds)>50:
            raise ValueError('Require one to three increasing guard rounds in 2..50.')
        raw=DATA.read_bytes()
        if hashlib.sha256(raw).hexdigest()!=DATA_SHA256:raise ValueError('Staged-guard certificate differs.')
        rows=[r for r in json.loads(raw)['layouts'] if r['layout']==parameters.get('layout','cash_rank_1')]
        if len(rows)!=1:raise ValueError('Unknown staged-guard wall layout.')
        self.guards=tuple(tuple(c) for c in rows[0]['guards'])

    def decide(self,observation):
        parent=super().decide(observation);rnd=observation['round']
        if rnd not in self.guard_rounds:return parent
        limit=self.guard_rounds.index(rnd)+1
        state=player_from_snapshot(observation['players'][observation['player']]);cfg=config_from_dict(observation['rules']);actions=[]
        occupied={(b.x,b.y):b.type for b in state.buildings}
        for x,y in self.guards[:limit]:
            if occupied.get((x,y))=='splash':continue
            action=dict(op='build_turret',type='splash',x=x,y=y)
            if not apply_action(state,action,rnd,cfg)['accepted']:break
            actions.append(action);occupied[(x,y)]='splash'
        for action in parent:
            if apply_action(state,action,rnd,cfg)['accepted']:actions.append(action)
        return actions


def make(**parameters):return StagedGuardMaze(**parameters).decide
