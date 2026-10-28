"""Exact integer circle plans with nonuniform angular locations.
Only selection uses floats; every final plan has exact checked marginals.
"""
from circle_transport_plan import antipodal,run_data,plan_at,check_plan

def edge_kind(i,j,n):
    return (i//n == j//n),abs(i%n-j%n)

def cost_of(edges,same,opposite,n):
    total=0.0
    for (i,j),mass in edges.items():
        is_same,k=edge_kind(i,j,n)
        total+=mass*(same[k] if is_same else opposite[k])
    return total

def best_plan(masses,same,opposite,tries=17):
    n=len(masses)//2
    assert len(same)==len(opposite)==n
    best=antipodal(masses);value=cost_of(best,same,opposite,n)
    info=dict(kind='antipodal');data=run_data(masses)
    if not data[0]:return best,dict(kind='zero')
    p=data[2];offset=data[4]
    lo=max(-d for d in offset);hi=min(pi-d for pi,d in zip(p,offset))
    if lo<=hi:
        for k in range(tries):
            t=lo+(hi-lo)*k//max(1,tries-1)
            edges=plan_at(data,t);v=cost_of(edges,same,opposite,n)
            if v<value:best=edges;value=v;info=dict(kind='adjacent',t=t)
    check_plan(masses,best)
    return best,info
