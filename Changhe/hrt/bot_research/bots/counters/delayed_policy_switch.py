"""Follow a public policy, substitute one wave, then use a fresh continuation."""
from copy import deepcopy
from td_game.actions import apply_action
from td_game.config import config_from_dict
from bot_research.bots.economy.frozen.v17.econ17 import make as economy17
from bot_research.bots.counters.catalogue_continuation import economy20, CONTINUATION_PARAMETERS
from bot_research.bots.counters.visible_search import player_from_snapshot

PREFIX_PARAMETERS = dict(free_fallback='zero', foreign_attack_from=11)


class DelayedPolicySwitch:
    def __init__(self, switch_round=9, tier='tier5', count_cap=1000):
        self.switch_round = None if switch_round is None else int(switch_round)
        self.tier, self.count_cap = str(tier), int(count_cap)
        if self.switch_round is not None and not 2 <= self.switch_round <= 50:
            raise ValueError('Switch round must be null or 2 through 50.')
        if self.tier not in ('tier1', 'tier2', 'tier3', 'tier4', 'tier5') or not 1 <= self.count_cap <= 1000:
            raise ValueError('Invalid tier or count cap.')
        self._reset()

    def _reset(self):
        self.prefix = economy17(**PREFIX_PARAMETERS)
        self.continuation = None
        self.prefix_calls = self.continuation_calls = self.last_round = 0
        self.player = None
        self.trace = []

    def decide(self, observation):
        rnd, side = observation['round'], observation['player']
        if rnd == 1:
            self._reset()
        if rnd != self.last_round+1 or self.player not in (None, side):
            raise ValueError('Require one call per round and a fixed player assignment.')
        detail = dict(round=rnd, branch='prefix', prefix_proposal=None, wave_count=0)
        if self.switch_round is None or rnd <= self.switch_round:
            proposal = self.prefix(deepcopy(observation))
            self.prefix_calls += 1
            detail['prefix_proposal'] = deepcopy(proposal)
            actions = proposal
            if rnd == self.switch_round:
                detail['branch'] = 'switch'
                actions = [a for a in proposal if a['op'] not in ('buy_factory', 'buy_minion')]
                projected = player_from_snapshot(observation['players'][side])
                config = config_from_dict(observation['rules'])
                for action in actions:
                    if not apply_action(projected, action, rnd, config)['accepted']:
                        raise ValueError('Prefix construction was illegal.')
                count = min(self.count_cap, projected.gold // observation['rules']['minions'][self.tier]['cost'])
                detail['wave_count'] = count
                detail['wave_budget'] = projected.gold
                actions += [dict(op='buy_minion', type=self.tier) for _ in range(count)]
        else:
            detail['branch'] = 'continuation'
            if self.continuation is None:
                self.continuation = economy20(**CONTINUATION_PARAMETERS)
            actions = self.continuation(deepcopy(observation))
            self.continuation_calls += 1
        detail.update(prefix_calls=self.prefix_calls, continuation_calls=self.continuation_calls)
        self.trace.append(detail)
        self.last_round, self.player = rnd, side
        return actions


def make(**parameters):
    return DelayedPolicySwitch(**parameters).decide
