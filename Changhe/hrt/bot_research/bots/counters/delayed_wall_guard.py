"""Shift the imported guard00 walls to round two, retaining G's other rules."""
from bot_research.bots.counters.early_wall_guard import EarlyWallGuard


class DelayedWallGuard(EarlyWallGuard):
    def __init__(self):
        super().__init__(witness='guard00')
        # The parent reads a fresh JSON object per instance. No shared data edit.
        self.witness['wall_round'] = 2

    def decide(self, observation):
        actions = super().decide(observation)
        self.trace[-1]['wall_round'] = 2
        return actions


def make():
    return DelayedWallGuard().decide
