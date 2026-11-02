"""Twenty-wall signal with one of four predeclared later/heavier purchases."""
from bot_research.bots.counters.wall_signal_timing import WallSignalTiming

SETTINGS = {(3, 'tier3'), (4, 'tier3'), (4, 'tier4'), (5, 'tier4')}


class DelayedWallSignal(WallSignalTiming):
    def __init__(self, attack_round=4, tier='tier4'):
        if (attack_round, tier) not in SETTINGS:
            raise ValueError('Undeclared delayed wall-signal setting.')
        super().__init__(wall_count=20)
        self.attack_round = attack_round
        self.tier = tier


def make(**parameters):
    return DelayedWallSignal(**parameters).decide
