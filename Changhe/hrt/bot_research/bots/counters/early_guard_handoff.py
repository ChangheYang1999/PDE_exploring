"""A fixed early guard extension followed by the existing defensive handoff."""
from copy import deepcopy
from pathlib import Path
import hashlib
import json

from td_game.actions import apply_action
from td_game.config import config_from_dict
from bot_research.bots.counters.screened_guard_maze import ScreenedGuardMaze
from bot_research.bots.counters.visible_search import player_from_snapshot
from bot_research.bots.defense.frozen.v34.fortress import make as make_defender

DATA = Path(__file__).with_name('data') / 'early_guard_extensions_001.json'
DATA_SHA256 = '05e4e934eff12cb698a59990cf94b3c722883419104dd0228298006bf24c1e5e'


class EarlyGuardHandoff:
    def __init__(self, extension='free_t3x3', handoff_round=10, replan_iters=5000,
                 **opening_parameters):
        self.handoff_round = int(handoff_round)
        if not 10 <= self.handoff_round <= 50:
            raise ValueError('The handoff must follow the fixed round9 opening extension.')
        if int(opening_parameters.get('upgrade_round', 9)) != 9:
            raise ValueError('The original screened extension remains in round9.')
        opening_parameters['upgrade_round'] = 9
        self.opening = ScreenedGuardMaze(**opening_parameters)
        self.defender = make_defender(attack='none', round1_poke=0,
                                      replan_iters=int(replan_iters))
        raw = DATA.read_bytes()
        if hashlib.sha256(raw).hexdigest() != DATA_SHA256:
            raise ValueError('Early guard extension data differs from its checksum.')
        matches = [p for p in json.loads(raw)['plans'] if p['id'] == extension]
        if len(matches) != 1:
            raise ValueError('Unknown early guard extension.')
        self.extra = tuple(dict(a) for a in matches[0]['actions'])
        self.filtered_proposals = []
        self.trace = []

    def decide(self, observation):
        rnd = observation['round']
        if rnd < self.handoff_round:
            parent = self.opening.decide(deepcopy(observation))
            if rnd == 6:
                construction = [a for a in parent if a['op'] in ('build_wall', 'build_turret')]
                economy = [a for a in parent if a['op'] not in ('build_wall', 'build_turret')]
                proposed = [('opening', a) for a in construction]
                proposed += [('extension', a) for a in self.extra]
                proposed += [('economy', a) for a in economy]
            else:
                proposed = [('opening', a) for a in parent]
        else:
            proposed = [('defender', a) for a in self.defender(deepcopy(observation))]
        state = player_from_snapshot(observation['players'][observation['player']])
        cfg = config_from_dict(observation['rules'])
        actions, extension_count = [], 0
        for stage, action in proposed:
            event = apply_action(state, action, rnd, cfg)
            if event['accepted']:
                actions.append(action)
                extension_count += stage == 'extension'
            else:
                self.filtered_proposals.append(dict(round=rnd, stage=stage, action=action,
                                                     reason=event['reason']))
        self.trace.append(dict(round=rnd, extension_actions_accepted=extension_count,
                               extension_complete=(extension_count == len(self.extra)) if rnd == 6 else None))
        return actions


def make(**parameters):
    return EarlyGuardHandoff(**parameters).decide
