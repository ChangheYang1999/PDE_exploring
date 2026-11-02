"""Default best_v9e with a proved native-path shortcut after splash immunity.

This is a research variant. It never modifies the frozen or installed candidate.
See experiments/validation/analysis/immune_runtime_shortcut/PROOF.md.
"""
from bot_research.experiments.lead.frozen import best_v9e as parent


class ImmuneShortcut(parent.Insurer):
    def __init__(self):
        super().__init__()

    def eligible(self, obs):
        """Pure predicate; the inherited caller handles foreign maps first."""
        if obs['round'] <= 5:
            return False
        rules = parent.gk.Rules.from_observation(obs)
        if not parent._immune(obs, rules):
            return False
        me = obs['players'][obs['player']]
        return not parent.P.plan_walls(obs, me['gold'], layout=self.layout, stage=0)

    def _decide(self, obs):
        if not self.eligible(obs):
            return super()._decide(obs)
        p = self.p
        rules = parent.gk.Rules.from_observation(obs)
        rnd = obs['round']
        me = obs['players'][obs['player']]
        left = me['gold']
        opp_hp = obs['players'][1-obs['player']]['hp']
        if self.pending is not None and self.pending[0] == rnd-1:
            _, hp_before, predicted = self.pending
            if hp_before-opp_hp < predicted/2:
                self.failed += 1
        self.pending = None
        self._fortress(obs, rules)
        actions = []
        if left > 0:
            bought, predicted = self._attack(obs, rules, int(left*p['attack_share']), 'current')
            if bought:
                actions.extend(bought)
                left -= parent._cost_of(bought, rules)
                self.pending = (rnd, opp_hp, predicted)
        if rnd <= p['last_factory_round']:
            actions.extend([{'op': 'buy_factory'}] * max(0, min(p['max_factories'], left//rules.factory_cost)))
        return actions


def make():
    return ImmuneShortcut()


_instances = {}


def decide(observation):
    key = observation['player']
    if key not in _instances or observation['round'] == 1:
        _instances[key] = make()
    return _instances[key](observation)
