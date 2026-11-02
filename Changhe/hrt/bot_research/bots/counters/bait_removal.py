"""The A/B schedule with only the three round-two tier1 purchases removed."""
from bot_research.bots.defense.counter_astra41 import SCHEDULES


def make(variant='A'):
    if variant not in ('A','B'):
        raise ValueError('Unknown fixed schedule.')
    schedule=SCHEDULES[variant]

    def decide(observation):
        actions=[dict(a) for a in schedule.get(observation['round'], [])]
        if observation['round']==2:
            actions=[a for a in actions if a != {'op':'buy_minion','type':'tier1'}]
        return actions
    return decide
