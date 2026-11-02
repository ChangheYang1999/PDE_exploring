"""A two-arm counter selected once from the public first-round roster.

The rule is fitted to a known development pool. It neither reads candidate
identity nor forecasts or inspects the opponent's pending action list.
"""
from bot_research.bots.counters.maze_grower import MazeGrower
from bot_research.bots.counters.staged_guard_maze import StagedGuardMaze


class PublicOpeningSelector:
    def __init__(self):
        parameters=dict(layout='empty',growth_rounds=6,bait_round=2,
                        tier='tier5',factory_cap=2000,purchase_cap=1000)
        self.bait=MazeGrower(bait=['tier1'],**parameters)
        self.guards=StagedGuardMaze(bait=[],guard_rounds=[4,6],**parameters)
        self.selected=None

    @staticmethod
    def choose(observation):
        roster=observation['players'][1-observation['player']]['roster']
        return ('bait' if len(roster)==3 and
                all(entry['type']=='tier1' and entry['bought_round']==1
                    for entry in roster) else 'guards')

    def decide(self,observation):
        if observation['round']==1:
            self.selected=None
            return self.guards.decide(observation)
        if self.selected is None:
            self.selected=self.choose(observation)
        return getattr(self,self.selected).decide(observation)


def make():return PublicOpeningSelector().decide
