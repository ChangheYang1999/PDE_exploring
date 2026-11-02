"""Public-feature ablation of the frozen economy13 continuation.

``normal`` is unchanged. ``open`` deliberately ignores the public enemy
``n_turrets`` count while retaining every physical building; this disables
only the permanent turret-presence signal. ``closed`` disables the special
no-turret case by moving its activation beyond the match horizon. These are
new policies for attribution, not altered executions of the original bot.
The engine and its real observations are never modified.
"""
from __future__ import annotations
from copy import deepcopy
from bot_research.bots.counters.opening_response import OpeningResponse
from bot_research.bots.economy.frozen.v13.econ13 import make as economy13


class TurretFeatureAblation:
    def __init__(self, mode='normal', guarded=True):
        if mode not in ('normal', 'open', 'closed'):
            raise ValueError('Unknown feature-ablation mode.')
        self.mode = mode
        parameters = {'none_from': 51} if mode == 'closed' else {}
        self.policy = (OpeningResponse(opening='guard_poke5', fallback='economy13',
                                      fallback_parameters=parameters).decide
                       if guarded else economy13(**parameters))

    def decide(self, observation):
        if self.mode != 'open':
            return self.policy(observation)
        shadow = deepcopy(observation)
        shadow['players'][1 - shadow['player']]['n_turrets'] = 0
        return self.policy(shadow)


def make(**parameters):
    return TurretFeatureAblation(**parameters).decide
