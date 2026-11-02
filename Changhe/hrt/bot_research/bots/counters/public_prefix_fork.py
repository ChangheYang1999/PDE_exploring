"""Two fixed continuations sharing exactly the same public three-round opening."""
from bot_research.experiments.lead.v30 import make as make_passive
from bot_research.bots.counters.maze_grower import MazeGrower


class PublicPrefixFork:
    def __init__(self, continuation='baseline'):
        if continuation not in ('baseline', 'flood'):
            raise ValueError('Unknown fixed continuation.')
        self.continuation = continuation
        self.baseline = make_passive(poke_reactive='turret_only', fail_limit=2,
            passive_turret=False, robust_k=None, behind_mode='current',
            passive_until=5, passive_mid_from=5, r1_poke=0)
        self.flood = MazeGrower(layout='lead_opening', growth_rounds=3,
                               tier='tier1', bait=[])

    def decide(self, observation):
        if observation['round'] <= 3 or self.continuation == 'baseline':
            return self.baseline(observation)
        return self.flood.decide(observation)


def make(**parameters):
    return PublicPrefixFork(**parameters).decide
