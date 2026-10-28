"""Exact greedy transport candidates, used only as feasible upper plans."""
import numpy as np

def transport_greedy(masses,points,alpha):
    positive=[i for i,m in enumerate(masses) if m>0]
    negative=[i for i,m in enumerate(masses) if m<0]
    assert sum(masses)==0
    if not positive:return {},dict(status='greedy',repairs=0)
    S=[masses[i] for i in positive];D=[-masses[j] for j in negative]
    P=np.asarray(points)[positive];Q=np.asarray(points)[negative]
    costs=abs(P[:,None]-Q[None,:])
    order=np.argsort(costs,axis=None,kind='stable');plan={};remaining=sum(S);n=len(D)
    for edge in order:
        i,j=divmod(int(edge),n)
        amount=min(S[i],D[j])
        if amount:
            plan[(positive[i],negative[j])]=amount
            S[i]-=amount;D[j]-=amount;remaining-=amount
            if not remaining:break
    assert not any(S) and not any(D)
    actual=[0]*len(masses)
    for (i,j),v in plan.items():actual[i]+=v;actual[j]-=v
    assert actual==masses
    return plan,dict(status='greedy',repairs=0)
