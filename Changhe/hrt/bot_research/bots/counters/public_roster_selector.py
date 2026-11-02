"""Choose a counter once, using only the visible first-round roster."""
from copy import deepcopy
from bot_research.bots.counters.guarded_round4_trigger import GuardedRound4Trigger
from bot_research.bots.counters.guard_handoff import GuardHandoff


class PublicRosterSelector:
    def __init__(self, mode='adaptive', threshold=3):
        if mode not in ('adaptive', 'early', 'growth'):
            raise ValueError('Unknown selector mode.')
        self.mode = mode
        self.threshold = int(threshold)
        if not 0 <= self.threshold <= 1000:
            raise ValueError('Invalid first-roster threshold.')
        common = dict(layout='empty', growth_rounds=6, bait=[], bait_round=2,
                      tier='tier5', factory_cap=2000, purchase_cap=1000)
        self.early = GuardedRound4Trigger(**common, upgrade_round=9,
            strike_round=4, strike_tier='tier4', strike_count=1, max_new=120,
            numerator=1, denominator=2, lead_from=5, lead_margin=0, early_gun=True)
        self.growth = GuardHandoff(**common, handoff_round=10, replan_iters=5000)
        self.selected = None if mode == 'adaptive' else mode
        self.trace = []

    def decide(self, observation):
        rnd, side = observation['round'], observation['player']
        count = sum(e['type'] == 'tier1' and e['bought_round'] == 1
                    for e in observation['players'][1-side]['roster'])
        if self.selected is None and rnd == 1:
            early = self.early.decide(deepcopy(observation))
            growth = self.growth.decide(deepcopy(observation))
            if early != growth:
                raise RuntimeError('The branch openings no longer coincide.')
            actions = early
        else:
            if self.selected is None:
                self.selected = 'early' if count >= self.threshold else 'growth'
            actions = getattr(self, self.selected).decide(deepcopy(observation))
        self.trace.append(dict(round=rnd, first_round_tier1_count=count, selected=self.selected))
        return actions


def make(**parameters):
    return PublicRosterSelector(**parameters).decide
