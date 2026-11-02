"""A pinned guarded schedule, filtering unaffordable actions on private state."""
from copy import deepcopy
import hashlib,json
from pathlib import Path
from td_game.actions import apply_action
from td_game.config import config_from_dict
from bot_research.bots.counters.visible_search import player_from_snapshot

DATA=Path(__file__).with_name('data')/'heavy_drip_001.json'
DATA_SHA256='9142473c439818a6411b1734fdfff375aff417c0b37c51678ad67da09597272a'


class HeavyDrip:
    def __init__(self):
        raw=DATA.read_bytes()
        if hashlib.sha256(raw).hexdigest()!=DATA_SHA256:raise ValueError('Schedule certificate differs.')
        self.schedule={row['round']:row['actions'] for row in json.loads(raw)['schedule']}

    def decide(self,observation):
        state=player_from_snapshot(observation['players'][observation['player']]);cfg=config_from_dict(observation['rules']);out=[]
        for action in self.schedule.get(observation['round'],[]):
            action=deepcopy(action)
            if apply_action(state,action,observation['round'],cfg)['accepted']:out.append(action)
        return out


def make():return HeavyDrip().decide
