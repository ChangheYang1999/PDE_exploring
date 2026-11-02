"""Pinned wall layouts, optional early bait, then fixed growth and waves."""
import hashlib
import json
from pathlib import Path
from td_game.actions import apply_action
from td_game.config import config_from_dict
from bot_research.bots.counters.visible_search import player_from_snapshot

DATA = Path(__file__).with_name('data') / 'maze_layouts_001.json'
DATA_SHA256 = '1f290c5da4b90c151c15ddf98e54055b427678addd8441363fead6163b812dd7'


class MazeGrower:
    def __init__(self, layout='cash_rank_1', growth_rounds=6, bait=None, bait_round=2,
                 tier='tier5', factory_cap=2000, purchase_cap=1000):
        raw=DATA.read_bytes()
        if hashlib.sha256(raw).hexdigest()!=DATA_SHA256:
            raise ValueError('Wall data differs from its pinned checksum.')
        matches=[r for r in json.loads(raw)['layouts'] if r['id']==layout]
        if len(matches)!=1:raise ValueError('Unknown or duplicate wall layout.')
        self.walls=tuple(tuple(c) for c in matches[0]['walls'])
        self.growth_rounds=int(growth_rounds);self.bait=tuple(bait or ());self.bait_round=int(bait_round)
        self.tier=str(tier);self.factory_cap=int(factory_cap);self.purchase_cap=int(purchase_cap)
        if not 1<=self.bait_round<=self.growth_rounds:raise ValueError('Bait must be during growth.')
        if len(self.bait)>1000 or any(t not in ('tier1','tier2') for t in self.bait):raise ValueError('Invalid bait.')
        if min(self.factory_cap,self.purchase_cap)<0:raise ValueError('Negative cap.')

    def decide(self, observation):
        rnd=observation['round'];rules=config_from_dict(observation['rules'])
        state=player_from_snapshot(observation['players'][observation['player']]);actions=[]
        def add(action):
            if apply_action(state,action,rnd,rules)['accepted']:
                actions.append(action);return True
            return False
        if rnd==1:
            for x,y in self.walls:add(dict(op='build_wall',x=x,y=y))
        if rnd==self.bait_round:
            for tier in self.bait:
                if not add(dict(op='buy_minion',type=tier)):break
        if rnd<=self.growth_rounds:
            count=min(max(0,self.factory_cap-state.n_factories),state.gold//rules.globals.factory_cost)
            for _ in range(count):
                if not add(dict(op='buy_factory')):raise RuntimeError('Affordable factory was rejected.')
        else:
            count=min(self.purchase_cap,state.gold//rules.minions[self.tier].cost)
            for _ in range(count):
                if not add(dict(op='buy_minion',type=self.tier)):raise RuntimeError('Affordable wave was rejected.')
        return actions


def make(**parameters):return MazeGrower(**parameters).decide
