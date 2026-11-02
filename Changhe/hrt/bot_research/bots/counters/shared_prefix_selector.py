"""Select a response from a shared first move using public round-two geometry."""
from copy import deepcopy
from bot_research.bots.counters.hp_handoff import HPHandoff
from bot_research.bots.counters.stateful_public import StatefulPublicTiming

HP_PARAMETERS = dict(layout='empty', growth_rounds=6, bait=[], bait_round=2,
                     tier='tier5', factory_cap=2000, purchase_cap=1000,
                     replan_iters=5000, deadline=12, lead_from=8)


def make_h():
    return HPHandoff(**deepcopy(HP_PARAMETERS))


def make_i():
    return StatefulPublicTiming(model_spec='bot_research.bots.counters.hp_handoff:@make',
                                model_parameters=deepcopy(HP_PARAMETERS), attack_round=3,
                                tier='tier2', defense_first=False, attack_share=1, count_cap=200)


class SharedPrefixSelector:
    def __init__(self):
        self.h = make_h()
        self.i = make_i()
        self.selected = None
        self.last_round = 0
        self.player = None
        self.trace = []

    def decide(self, observation):
        rnd, side = observation['round'], observation['player']
        if rnd != self.last_round + 1 or (self.player is not None and side != self.player):
            raise ValueError('This selector requires consecutive standard-start observations.')
        if rnd == 1:
            h_actions = self.h.decide(deepcopy(observation))
            i_actions = self.i.decide(deepcopy(observation))
            if h_actions != i_actions:
                raise ValueError('The declared first move is not shared.')
            actions = h_actions
        else:
            if rnd == 2:
                enemy = observation['players'][1-side]
                self.selected = 'H' if enemy['n_walls'] >= 20 and not enemy['roster'] else 'I'
            chosen = self.h if self.selected == 'H' else self.i
            actions = chosen.decide(deepcopy(observation))
        enemy = observation['players'][1-side]
        self.trace.append(dict(round=rnd, selected=self.selected,
                               opponent_walls=enemy['n_walls'], opponent_roster=len(enemy['roster'])))
        self.last_round, self.player = rnd, side
        return actions


def make():
    return SharedPrefixSelector().decide
