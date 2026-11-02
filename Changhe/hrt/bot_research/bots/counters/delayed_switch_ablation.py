"""Output-only controls for the declared delayed policy switch."""
from copy import deepcopy
from bot_research.bots.counters.delayed_policy_switch import DelayedPolicySwitch


class DelayedSwitchAblation(DelayedPolicySwitch):
    def __init__(self, mode='wave', **parameters):
        if mode not in ('wave', 'save', 'prefix'):
            raise ValueError('Unknown ablation mode.')
        self.mode = mode
        super().__init__(**parameters)

    def decide(self, observation):
        actions = super().decide(observation)
        detail = self.trace[-1]
        detail['mode'] = self.mode
        if detail['branch'] == 'switch':
            detail['proposed_wave_count'] = detail['wave_count']
            if self.mode == 'save':
                actions = [a for a in actions if a['op'] != 'buy_minion']
                detail['wave_count'] = 0
            elif self.mode == 'prefix':
                actions = deepcopy(detail['prefix_proposal'])
                detail['wave_count'] = None
                detail['branch'] = 'prefix_at_switch'
        return actions


def make(**parameters):
    return DelayedSwitchAblation(**parameters).decide
