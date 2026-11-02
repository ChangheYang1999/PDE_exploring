"""Choose G or L after their checked common wall opening, using public state."""
from copy import deepcopy

from bot_research.bots.counters.early_wall_guard import EarlyWallGuard
from bot_research.bots.counters.wall_signal_repair import WallSignalRepair


class WallPrefixSelector:
    """Support consecutive standard-start calls; keep the chosen private history."""

    def __init__(self):
        self.g = EarlyWallGuard(witness='guard00')
        self.l = WallSignalRepair()
        self.selected = None
        self.last_round = 0
        self.player = None
        self.trace = []

    def decide(self, observation):
        rnd, side = observation['round'], observation['player']
        if rnd != self.last_round + 1 or (self.player is not None and side != self.player):
            raise ValueError('This selector requires consecutive standard-start observations.')

        if rnd == 1:
            g_actions = self.g.decide(deepcopy(observation))
            l_actions = self.l.decide(deepcopy(observation))
            if g_actions != l_actions:
                raise ValueError('The declared G/L first move is not shared.')
            actions = g_actions
        else:
            if rnd == 2:
                enemy = observation['players'][1 - side]
                self.selected = 'L' if not enemy['buildings'] and not enemy['roster'] else 'G'
            chosen = self.l if self.selected == 'L' else self.g
            actions = chosen.decide(deepcopy(observation))

        enemy = observation['players'][1 - side]
        self.trace.append(dict(round=rnd, selected=self.selected,
                               opponent_buildings=len(enemy['buildings']),
                               opponent_roster=len(enemy['roster'])))
        self.last_round, self.player = rnd, side
        return actions


def make():
    return WallPrefixSelector().decide
