"""Select a feasible integer plan by batched two-edge exchanges.

Floating costs select moves only. Cycle cancellation preserves every exact
integer marginal and bounds support size. No optimality claim is used.
"""
import numpy as np
from local_circle_greedy import transport_greedy

def _remove_cycles(plan,cost,n):
    removed=0
    while True:
        parent=list(range(n));adj=[[] for _ in range(n)];cycle=None
        def root(x):
            while parent[x]!=x:
                parent[x]=parent[parent[x]];x=parent[x]
            return x
        for e in plan:
            u,v=e;ru,rv=root(u),root(v)
            if ru!=rv:
                parent[ru]=rv;adj[u].append((v,e));adj[v].append((u,e))
                continue
            stack=[u];previous={u:(None,None)}
            while stack and v not in previous:
                node=stack.pop()
                for nxt,edge in adj[node]:
                    if nxt not in previous:previous[nxt]=(node,edge);stack.append(nxt)
            assert v in previous
            path=[];node=v
            while node!=u:
                node,edge=previous[node];path.append(edge)
            cycle=[e]+path;assert len(cycle)%2==0
            break
        if cycle is None:return removed
        signs=[1 if k%2==0 else -1 for k in range(len(cycle))]
        change=sum(sign*cost[e] for sign,e in zip(signs,cycle))
        if change>0:signs=[-s for s in signs]
        amount=min(plan[e] for sign,e in zip(signs,cycle) if sign<0)
        for sign,e in zip(signs,cycle):
            plan[e]+=sign*amount
            if plan[e]==0:del plan[e]
        removed+=1

def transport_batch_exchange(masses,points,alpha,rounds=8):
    plan,info=transport_greedy(masses,points,alpha)
    z=np.asarray(points);cost=abs(z[:,None]-z[None,:])**alpha
    moves=cycles=0
    for step in range(rounds):
        if len(plan)<2:break
        edges=list(plan);src=np.array([e[0] for e in edges]);dst=np.array([e[1] for e in edges]);flow=np.array([plan[e] for e in edges],dtype=float)
        unit=cost[src,dst]
        gain=unit[:,None]+unit[None,:]-cost[src[:,None],dst[None,:]]-cost[src[None,:],dst[:,None]]
        value=gain*np.minimum(flow[:,None],flow[None,:]);np.fill_diagonal(value,0)
        best=np.argmax(value,axis=1)
        choices=sorted(((float(value[i,j]),i,int(j)) for i,j in enumerate(best)),reverse=True)
        used=set();ops=[]
        for score,i,j in choices:
            if score<=1e-10 or gain[i,j]<=1e-12:break
            if i in used or j in used:continue
            a,b=edges[i];c,d=edges[j]
            if a==c or b==d:continue
            used.add(i);used.add(j);amount=min(plan[(a,b)],plan[(c,d)])
            ops.append((a,b,c,d,amount))
        if not ops:break
        # All subtracted edges are distinct. Incoming additions cannot harm
        # nonnegativity, even if a new edge is another operation's old edge.
        for a,b,c,d,amount in ops:
            for e in [(a,b),(c,d)]:plan[e]-=amount
            for e in [(a,d),(c,b)]:plan[e]=plan.get(e,0)+amount
        plan={e:v for e,v in plan.items() if v};moves+=len(ops)
        cycles+=_remove_cycles(plan,cost,len(masses))
    actual=[0]*len(masses)
    for (i,j),v in plan.items():
        assert isinstance(v,int) and v>0 and masses[i]>0 and masses[j]<0
        actual[i]+=v;actual[j]-=v
    assert actual==masses
    return plan,dict(status='batch exchanges',repairs=0,rounds=step+1,moves=moves,cycles=cycles)
