"""Keep catalogue actions until rejection, then use a fresh foreign-map policy."""
from copy import deepcopy

from bot_research.bots.counters.stateful_catalogue import StatefulCatalogue
from bot_research.bots.economy.frozen.v20.econ20 import make as economy20

CONTINUATION_PARAMETERS = dict(
    free_fallback='zero', foreign_attack_from=11, doom='next', fac_cap=400,
    sat_reach=True, replan=True, foreign_sat_from=11,
)


class CatalogueContinuation(StatefulCatalogue):
    def _reset(self):
        super()._reset()
        self.continuation = None
        self.continuation_started = None
        self.continuation_calls = 0

    def decide(self, observation):
        rnd, side = observation['round'], observation['player']
        if rnd == 1 or self.active:
            original = super().decide(observation)
        else:
            if rnd != self.last_round + 1 or side != self.player:
                raise ValueError('Require one call per round and a fixed player assignment.')
            if self.pending:
                raise ValueError('An empty catalogue cannot have a pending prediction.')
            self.trace.append(dict(
                round=rnd, before_active=[], active=[], eliminated=[],
                observed_previous_signature=None, predictions={},
                call_counts=dict(self.calls), fallback=True, attack_count=0,
                attack_tier=self.tier, attack_gains=[], defense=None,
            ))
            self.last_round, self.player = rnd, side
            original = None
        trace = self.trace[-1]
        if not trace['fallback']:
            trace['continuation'] = dict(active=False, calls=0, started_round=None)
            return original
        if self.continuation is None:
            self.continuation = economy20(**CONTINUATION_PARAMETERS)
            self.continuation_started = rnd
        actions = self.continuation(deepcopy(observation))
        self.continuation_calls += 1
        trace['continuation'] = dict(
            active=True, calls=self.continuation_calls,
            started_round=self.continuation_started,
            policy='bot_research.bots.economy.frozen.v20.econ20:@make',
            parameters=dict(CONTINUATION_PARAMETERS),
        )
        return actions


def make(**parameters):
    return CatalogueContinuation(**parameters).decide
