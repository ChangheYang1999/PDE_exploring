"""Add a selected five-wall guard to the public C02 screened-order counter."""
from pathlib import Path
import json

from td_game.actions import apply_action
from td_game.config import config_from_dict
from bot_research.bots.counters.screened_roster_continuation import ScreenedRosterContinuation
from bot_research.bots.counters.visible_search import player_from_snapshot

DATA = Path(__file__).parent/'data/screened_roster_guard_001.json'


class ScreenedRosterGuarded(ScreenedRosterContinuation):
    def __init__(self, continuation='fortress38'):
        super().__init__(order='screen', continuation=continuation)
        self.walls = json.loads(DATA.read_text())['walls']

    def decide(self, observation):
        original = super().decide(observation)
        if observation['round'] != 6 or not original:
            return original
        proposed = original + [dict(op='build_wall', x=x, y=y) for x, y in self.walls]
        own = player_from_snapshot(observation['players'][observation['player']])
        cfg = config_from_dict(observation['rules'])
        if all(apply_action(own, action, 6, cfg)['accepted'] for action in proposed):
            return proposed
        return original


def make(**parameters):
    return ScreenedRosterGuarded(**parameters).decide
