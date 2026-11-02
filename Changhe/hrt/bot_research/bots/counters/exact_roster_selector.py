"""Select the early branch only at one exact public opening count."""
from bot_research.bots.counters.public_roster_selector import PublicRosterSelector


class ExactRosterSelector(PublicRosterSelector):
    def __init__(self, mode='adaptive', count=3):
        self.exact_count = int(count)
        super().__init__(mode=mode, threshold=self.exact_count)

    def decide(self, observation):
        if self.selected is None and observation['round'] >= 2:
            other = observation['players'][1-observation['player']]
            count = sum(e['type'] == 'tier1' and e['bought_round'] == 1
                        for e in other['roster'])
            self.selected = 'early' if count == self.exact_count else 'growth'
        return super().decide(observation)


def make(**parameters):
    return ExactRosterSelector(**parameters).decide
