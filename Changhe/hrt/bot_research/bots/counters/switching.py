"""Public-observation policies that change their economic plan at a fixed round."""
from __future__ import annotations
from bot_research.bots.counters.archetypes import make as archetype


class SwitchingArchetype:
    def __init__(self, prefix='eco5_t3', after='heavy_t4', switch_round=5):
        self.prefix = archetype(prefix)
        self.after = archetype(after)
        self.switch_round = int(switch_round)

    def decide(self, observation):
        return (self.prefix if observation['round'] < self.switch_round else self.after).decide(observation)


def make(prefix='eco5_t3', after='heavy_t4', switch_round=5):
    return SwitchingArchetype(prefix, after, switch_round).decide
