"""Use an exact early-wall witness, one heavy purchase and frozen defense."""
from copy import deepcopy
from pathlib import Path
import json
from td_game.actions import apply_action
from td_game.config import config_from_dict
from bot_research.bots.counters.visible_search import player_from_snapshot
from bot_research.bots.defense.frozen.v38.fortress import make as make_defender

DATA = Path(__file__).with_name('data')/'early_wall_guard_001.json'


class EarlyWallGuard:
    def __init__(self, witness='guard00'):
        self.witness = next(w for w in json.loads(DATA.read_text())['witnesses'] if w['id']==witness)
        self.defender = make_defender()
        self.trace = []
        self.filtered_proposals = []

    def decide(self, observation):
        rnd, side = observation['round'], observation['player']
        cfg = config_from_dict(observation['rules'])
        state = player_from_snapshot(observation['players'][side])
        actions = []
        def submit(action):
            event = apply_action(state,action,rnd,cfg)
            if event['accepted']:
                actions.append(action)
                return True
            self.filtered_proposals.append(dict(round=rnd,action=action,reason=event['reason']))
            return False
        if rnd >= 5:
            for action in self.defender(deepcopy(observation)):
                submit(action)
        else:
            if rnd == self.witness['wall_round']:
                for x,y in self.witness['walls']:
                    submit(dict(op='build_wall',x=x,y=y))
            if rnd == 3:
                for turret in self.witness['turrets']:
                    submit(dict(op='build_turret',**turret))
            if rnd == 4 and state.gold >= cfg.minions['tier4'].cost:
                submit(dict(op='buy_minion',type='tier4'))
            while state.gold >= cfg.globals.factory_cost:
                if not submit(dict(op='buy_factory')):
                    break
        self.trace.append(dict(round=rnd,witness=self.witness['id'],defender_active=rnd>=5,
            filtered_proposals=sum(p['round']==rnd for p in self.filtered_proposals)))
        return actions


def make(**parameters):
    return EarlyWallGuard(**parameters).decide
