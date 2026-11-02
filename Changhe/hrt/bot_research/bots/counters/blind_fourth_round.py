"""Submit G through round three, then continue the already advanced L4.

L4 is a fresh WallSignalRepair with only attack_round changed to four.
Both members consume actual observations through round three in G then L4
order. Opponent presence is recorded but never changes the fixed commitment.
"""
from copy import deepcopy
from bot_research.bots.counters.early_wall_guard import EarlyWallGuard
from bot_research.bots.counters.wall_signal_repair import WallSignalRepair


class BlindFourthRound:
    def __init__(self):
        self.g = EarlyWallGuard(witness='guard00')
        self.l4 = WallSignalRepair()
        self.l4.attack_round = 4
        self.selected = None
        self.selection_round = None
        self.last_round = 0
        self.player = None
        self.trace = []

    def decide(self, observation):
        rnd, side = observation['round'], observation['player']
        if type(rnd) is not int or rnd != self.last_round + 1:
            raise ValueError('This control requires consecutive rounds from round one.')
        if type(side) is not int or side not in (0, 1):
            raise ValueError('This control requires physical player zero or one.')
        if self.player is not None and side != self.player:
            raise ValueError('This control cannot change physical player assignments.')

        enemy = observation['players'][1-side]
        selected_before = self.selected
        if self.selected is None and rnd == 4:
            self.selected = 'L4'
            self.selection_round = rnd

        member_calls = ['G', 'L4'] if self.selected is None else ['L4']
        proposals = {}
        for name in member_calls:
            member = self.g if name == 'G' else self.l4
            proposed = member.decide(deepcopy(observation))
            if not isinstance(proposed, list):
                raise TypeError('A member must return an ordered action list.')
            proposals[name] = deepcopy(proposed)

        returned_member = self.selected or 'G'
        actions = deepcopy(proposals[returned_member])
        discarded = {name: deepcopy(proposal) for name, proposal in proposals.items()
                     if name != returned_member}
        self.trace.append(dict(
            round=rnd, player=side, selected_before=selected_before,
            selected=self.selected, selection_round=self.selection_round,
            opponent_buildings=len(enemy['buildings']),
            opponent_roster=len(enemy['roster']),
            presence=bool(enemy['buildings'] or enemy['roster']),
            member_calls=list(member_calls), returned_member=returned_member,
            proposed_actions=deepcopy(proposals),
            discarded_proposals=deepcopy(discarded),
            submitted_actions=deepcopy(actions)))
        self.last_round, self.player = rnd, side
        return actions


def make():
    return BlindFourthRound().decide
