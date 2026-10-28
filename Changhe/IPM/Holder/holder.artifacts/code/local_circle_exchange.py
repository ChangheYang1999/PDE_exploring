"""Feasible integer transport improvement by exact 2-by-2 exchanges.
Float costs select exchanges only. Every mass and marginal remains exact.
"""
import numpy as np
from local_circle_greedy import transport_greedy

def transport_exchange(masses,points,alpha,steps=80):
 plan,info=transport_greedy(masses,points,alpha)
 z=np.asarray(points);cost=abs(z[:,None]-z[None,:])**alpha
 for _ in range(steps):
  edges=list(plan);src=np.array([e[0] for e in edges]);dst=np.array([e[1] for e in edges]);flow=np.array([plan[e] for e in edges],dtype=np.float64)
  unit=cost[src,dst];gain=unit[:,None]+unit[None,:]-cost[src[:,None],dst[None,:]]-cost[src[None,:],dst[:,None]]
  improvement=gain*np.minimum(flow[:,None],flow[None,:]);np.fill_diagonal(improvement,0)
  k=int(np.argmax(improvement));i,j=np.unravel_index(k,improvement.shape)
  if gain[i,j]<=1e-12 or improvement[i,j]<=1e-10:break
  a,b=edges[i];c,d=edges[j];amount=min(plan[(a,b)],plan[(c,d)])
  assert a!=c and b!=d and amount>0
  for e in [(a,b),(c,d)]:
   plan[e]-=amount
   if plan[e]==0:del plan[e]
  for e in [(a,d),(c,b)]:plan[e]=plan.get(e,0)+amount
 actual=[0]*len(masses)
 for (i,j),v in plan.items():
  assert isinstance(v,int) and v>0 and masses[i]>0 and masses[j]<0
  actual[i]+=v;actual[j]-=v
 assert actual==masses
 return plan,dict(status='greedy exchanges',repairs=0,exchanges=_+1)
