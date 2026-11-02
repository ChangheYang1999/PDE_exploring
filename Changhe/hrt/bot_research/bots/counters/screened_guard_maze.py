"""Growth and two timed splash guards, followed by a porous gun extension."""
import hashlib,json
from pathlib import Path
from td_game.actions import apply_action
from td_game.config import config_from_dict
from bot_research.bots.counters.staged_guard_maze import StagedGuardMaze
from bot_research.bots.counters.visible_search import player_from_snapshot

DATA=Path(__file__).with_name('data')/'screened_guard_001.json'
DATA_SHA256='c0980d0c46cf813f82d3eae5e26e18fab2d74f8135a87d4ad550eddc804ffde6'


class ScreenedGuardMaze(StagedGuardMaze):
    def __init__(self,upgrade_round=9,**parameters):
        if parameters.get('layout','empty')!='empty':raise ValueError('The screen-aware guard uses the empty layout.')
        parameters['layout']='empty';parameters['guard_rounds']=(4,6)
        super().__init__(**parameters)
        self.upgrade_round=int(upgrade_round)
        if not 7<=self.upgrade_round<=50:raise ValueError('Upgrade after both fixed splash guards.')
        raw=DATA.read_bytes()
        if hashlib.sha256(raw).hexdigest()!=DATA_SHA256:raise ValueError('Screen-aware guard data differs.')
        witness=json.loads(raw)['witnesses'][0]
        self.extra=tuple(dict(a) for a in witness['extra_actions'])

    def decide(self,observation):
        parent=super().decide(observation);rnd=observation['round']
        if rnd!=self.upgrade_round:return parent
        own=player_from_snapshot(observation['players'][observation['player']]);cfg=config_from_dict(observation['rules']);actions=[]
        for action in self.extra:
            if not apply_action(own,action,rnd,cfg)['accepted']:break
            actions.append(dict(action))
        for action in parent:
            if apply_action(own,action,rnd,cfg)['accepted']:actions.append(action)
        return actions


def make(**parameters):return ScreenedGuardMaze(**parameters).decide
