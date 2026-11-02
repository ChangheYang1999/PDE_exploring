"""Delay a G/L choice through their second shared decision when possible."""
from copy import deepcopy
from bot_research.bots.counters.early_wall_guard import EarlyWallGuard
from bot_research.bots.counters.wall_signal_repair import WallSignalRepair


class TwoRoundWallSelector:
    def __init__(self):
        self.g = EarlyWallGuard(witness='guard00')
        self.l = WallSignalRepair()
        self.selected = None
        self.selection_round = None
        self.last_round = 0
        self.player = None
        self.trace = []

    def decide(self, observation):
        rnd, side = observation['round'], observation['player']
        if rnd != self.last_round + 1 or (self.player is not None and side != self.player):
            raise ValueError('This selector requires consecutive standard-start observations.')
        enemy = observation['players'][1-side]
        present = bool(enemy['buildings'] or enemy['roster'])
        if self.selected is None and ((rnd == 2 and present) or rnd == 3):
            self.selected = 'G' if present else 'L'
            self.selection_round = rnd
        if self.selected is None:
            g_actions = self.g.decide(deepcopy(observation))
            l_actions = self.l.decide(deepcopy(observation))
            if g_actions != l_actions:
                raise ValueError('The declared G/L prefix is not shared.')
            actions = g_actions
        else:
            chosen = self.g if self.selected == 'G' else self.l
            actions = chosen.decide(deepcopy(observation))
        self.trace.append(dict(round=rnd, selected=self.selected,
            selection_round=self.selection_round,
            opponent_buildings=len(enemy['buildings']), opponent_roster=len(enemy['roster'])))
        self.last_round, self.player = rnd, side
        return actions


def make():
    return TwoRoundWallSelector().decide
