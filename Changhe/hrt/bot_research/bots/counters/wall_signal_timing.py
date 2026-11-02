"""Add a public wall signal to the matching-H round-three timing attacker."""
from copy import deepcopy
from pathlib import Path
import json
from td_game.actions import apply_action
from td_game.config import config_from_dict
from bot_research.bots.counters.shared_prefix_selector import HP_PARAMETERS
from bot_research.bots.counters.stateful_public import StatefulPublicTiming
from bot_research.bots.counters.visible_search import player_from_snapshot

DATA = Path(__file__).with_name('data') / 'early_wall_guard_001.json'


class WallSignalTiming(StatefulPublicTiming):
    def __init__(self, wall_count=20):
        super().__init__(model_spec='bot_research.bots.counters.hp_handoff:@make',
                         model_parameters=deepcopy(HP_PARAMETERS), attack_round=3,
                         tier='tier2', defense_first=False, attack_share=1, count_cap=200)
        if type(wall_count) is not int or wall_count not in (0, 19, 20):
            raise ValueError('Only the declared 0, 19 and 20 wall openings are supported.')
        witness = next(w for w in json.loads(DATA.read_text())['witnesses'] if w['id'] == 'guard00')
        if len(witness['walls']) < wall_count:
            raise ValueError('Insufficient declared wall cells.')
        self.walls = witness['walls'][:wall_count]
        self.opening_trace = []

    def decide(self, observation):
        actions = super().decide(observation)
        if observation['round'] != 1 or not self.walls:
            return actions
        if any(a != {'op': 'buy_factory'} for a in actions):
            raise ValueError('This opening requires the standard shared factory first move.')
        config = config_from_dict(observation['rules'])
        state = player_from_snapshot(observation['players'][observation['player']])
        replacement = []
        for x, y in self.walls:
            action = dict(op='build_wall', x=x, y=y)
            if not apply_action(state, action, 1, config)['accepted']:
                raise ValueError('Declared wall prefix is not legal.')
            replacement.append(action)
        while state.gold >= config.globals.factory_cost:
            action = dict(op='buy_factory')
            if not apply_action(state, action, 1, config)['accepted']:
                raise ValueError('Declared factory purchase is not legal.')
            replacement.append(action)
        self.opening_trace.append(dict(walls=len(self.walls), discarded_actions=actions,
                                       submitted_actions=deepcopy(replacement)))
        return replacement


def make(**parameters):
    return WallSignalTiming(**parameters).decide
