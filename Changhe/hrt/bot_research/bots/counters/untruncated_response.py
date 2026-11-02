"""Focused v24 ablation: response-test every current-map candidate tier."""
from bot_research.experiments.lead.v24 import Insurer,P,TIER_ORDER


class UntruncatedInsurer(Insurer):
    def _attack(self,obs,rules,budget,mode=None):
        p=self.p;mode=mode or p['attack_mode']
        if mode=='adaptive':mode='current' if self.failed<p['fail_limit'] else 'robust'
        if mode!='robust':return super()._attack(obs,rules,budget,mode)
        _,base=P.opponent_leak(obs,[]);candidates=[]
        for tier in TIER_ORDER:
            cost=rules.minions[tier]['cost'];n=min(p['max_minions'],budget//cost)
            if n<=0:continue
            _,damage=P.opponent_leak(obs,[tier]*n);gain=(damage-base)/(n*cost)
            if gain>=p['min_leak_per_gold']:candidates.append((gain,tier,n,damage-base))
        candidates.sort(reverse=True);passing=[]
        for _,tier,n,_ in candidates:
            damage=self._leak_after_response(obs,rules,[tier]*n)
            ratio=damage/(n*rules.minions[tier]['cost'])
            if ratio>=p['min_leak_per_gold']:passing.append((ratio,tier,n,damage))
        passing.sort(reverse=True)
        if not passing:return [],0
        _,tier,n,damage=passing[0]
        return [dict(op='buy_minion',type=tier)]*n,damage


def make(**parameters):return UntruncatedInsurer(**parameters)
