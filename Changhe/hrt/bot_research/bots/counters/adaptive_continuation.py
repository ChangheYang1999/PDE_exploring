"""Adaptive catalogue actions until rejection, then a fresh economy20 policy.

The two parent methods deliberately compose in this order: the continuation
wrapper calls AdaptiveCatalogue while models remain, then stops the parent.
"""
from bot_research.bots.counters.catalogue_continuation import CatalogueContinuation
from bot_research.bots.counters.adaptive_catalogue import AdaptiveCatalogue


class AdaptiveContinuation(CatalogueContinuation, AdaptiveCatalogue):
    def decide(self, observation):
        actions = super().decide(observation)
        trace = self.trace[-1]
        if trace['fallback']:
            proposal = trace.get('adaptive_attack')
            if proposal is not None:
                trace['discarded_parent_attack'] = proposal
            trace['adaptive_attack'] = dict(enabled=False, reason='fresh_economy20_continuation')
            trace['defense'] = None
            purchases = [a['type'] for a in actions if a['op'] == 'buy_minion']
            trace['attack_count'] = len(purchases)
            trace['attack_tier'] = 'continuation_package'
            trace['attack_gains'] = []
        return actions


def make(**parameters):
    return AdaptiveContinuation(**parameters).decide
