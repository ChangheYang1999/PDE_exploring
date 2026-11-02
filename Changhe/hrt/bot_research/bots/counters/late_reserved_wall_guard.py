"""Keep two empty public rounds, then reserve the round-four heavy purchase."""
from bot_research.bots.counters.reserved_wall_guard import ReservedWallGuard


class LateReservedWallGuard(ReservedWallGuard):
    def __init__(self):
        super().__init__()
        self.witness['wall_round'] = 3

    def decide(self, observation):
        actions = super().decide(observation)
        self.trace[-1]['wall_round'] = 3
        return actions


def make():
    return LateReservedWallGuard().decide
