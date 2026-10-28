"""Propose a transport with HiGHS, then enforce exact integer marginals.
Floating point is used only to select admissible edges. Every returned flow is
nonnegative, integral and has exactly the requested supply and demand.
"""
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import coo_matrix

def transport(masses,points,alpha):
    positive=[i for i,m in enumerate(masses) if m>0]
    negative=[i for i,m in enumerate(masses) if m<0]
    assert sum(masses)==0
    if not positive:return {},dict(status='empty',repairs=0)
    supply=[masses[i] for i in positive];demand=[-masses[j] for j in negative]
    P=np.asarray(points)[positive];Q=np.asarray(points)[negative]
    costs=abs(P[:,None]-Q[None,:])**alpha
    n,m=costs.shape;I,J=np.indices((n,m));cols=np.arange(n*m)
    mat=coo_matrix((np.ones(2*n*m),(np.concatenate([I.ravel(),n+J.ravel()]),np.concatenate([cols,cols]))),shape=(n+m,n*m)).tocsr()
    total=sum(supply)
    solution=linprog(costs.ravel(),A_eq=mat,b_eq=np.array(supply+demand,dtype=float)/total,
                     bounds=(0,None),method='highs',options={'time_limit':30})
    plan={};remaining_s=supply[:];remaining_d=demand[:]
    def send(i,j,amount):
        amount=min(int(amount),remaining_s[i],remaining_d[j])
        if amount<=0:return
        edge=(positive[i],negative[j]);plan[edge]=plan.get(edge,0)+amount
        remaining_s[i]-=amount;remaining_d[j]-=amount
    if solution.success:
        values=solution.x.reshape(n,m)
        for i,j in zip(*np.nonzero(values>0)):
            send(int(i),int(j),max(0,int(np.floor(values[i,j]*total))))
    # Exact closure. The residual may contain solver feasibility errors, so it
    # is transported explicitly rather than discarded or assumed negligible.
    repairs=sum(remaining_s)
    while sum(remaining_s):
        ii=[i for i,v in enumerate(remaining_s) if v]
        jj=[j for j,v in enumerate(remaining_d) if v]
        subset=costs[np.ix_(ii,jj)]
        a,b=np.unravel_index(np.argmin(subset),subset.shape)
        i,j=ii[a],jj[b]
        send(i,j,min(remaining_s[i],remaining_d[j]))
    actual=[0]*len(masses)
    for (i,j),v in plan.items():
        assert isinstance(v,int) and v>0 and masses[i]>0 and masses[j]<0
        actual[i]+=v;actual[j]-=v
    assert actual==masses and not any(remaining_d)
    return plan,dict(status='optimal' if solution.success else 'greedy fallback',repairs=repairs)
