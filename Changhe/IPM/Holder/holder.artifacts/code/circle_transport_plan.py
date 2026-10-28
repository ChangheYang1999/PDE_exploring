"""Exact integer-mass circle transports. Plan selection may be heuristic;
every returned plan has its row and column sums checked exactly.
"""
import math

def check_plan(masses,edges):
    outgoing=[0]*len(masses);incoming=[0]*len(masses)
    for (i,j),q in edges.items():
        assert isinstance(q,int) and q>0 and masses[i]>0 and masses[j]<0
        outgoing[i]+=q;incoming[j]+=q
    assert outgoing==[max(v,0) for v in masses]
    assert incoming==[max(-v,0) for v in masses]

def antipodal(masses):
    n=len(masses);h=n//2;assert n%2==0
    assert all(masses[j+h]==-masses[j] for j in range(h))
    edges={}
    for j in range(h):
        q=masses[j]
        if q>0:edges[j,j+h]=q
        elif q<0:edges[j+h,j]=-q
    check_plan(masses,edges)
    return edges

def split_mass(run,left_mass):
    assert 0<=left_mass<=sum(q for i,q in run)
    left=[];right=[];remain=left_mass
    for i,q in run:
        part=min(remain,q)
        if part:left.append((i,part))
        if q>part:right.append((i,q-part))
        remain-=part
    assert remain==0
    return left,right

def merge_parts(source,target,edges):
    assert sum(q for i,q in source)==sum(q for i,q in target)
    if not source:return
    a=b=0;ra=source[0][1];rb=target[0][1]
    while a<len(source) and b<len(target):
        q=min(ra,rb);key=(source[a][0],target[b][0]);edges[key]=edges.get(key,0)+q
        ra-=q;rb-=q
        if ra==0:
            a+=1
            if a<len(source):ra=source[a][1]
        if rb==0:
            b+=1
            if b<len(target):rb=target[b][1]
    assert a==len(source) and b==len(target)

def run_data(masses):
    nonzero=[(j,q) for j,q in enumerate(masses) if q]
    if not nonzero:return [],[],[],[],[]
    start=next(k for k,(j,q) in enumerate(nonzero) if q>0 and nonzero[k-1][1]<0)
    nonzero=nonzero[start:]+nonzero[:start];runs=[]
    for j,q in nonzero:
        if not runs or (q>0)!=(masses[runs[-1][0][0]]>0):runs.append([])
        runs[-1].append((j,abs(q)))
    assert len(runs)%2==0
    positive=runs[::2];negative=runs[1::2]
    p=[sum(q for j,q in row) for row in positive];z=[sum(q for j,q in row) for row in negative]
    assert sum(p)==sum(z)
    offsets=[0]
    for pi,ni in zip(p[:-1],z[:-1]):offsets.append(offsets[-1]+ni-pi)
    return positive,negative,p,z,offsets

def plan_at(data,t):
    positive,negative,p,z,offsets=data
    cuts=[t+d for d in offsets];k=len(p)
    pp=[split_mass(row,x) for row,x in zip(positive,cuts)]
    nn=[split_mass(row,pi-x) for row,pi,x in zip(negative,p,cuts)]
    edges={}
    for i in range(k):
        merge_parts(pp[i][1][::-1],nn[i][0],edges)
        merge_parts(pp[i][0],nn[(i-1)%k][1][::-1],edges)
    return edges

def plan_cost(edges,costs,n):
    return sum(q*costs[min(abs(i-j),n-abs(i-j))] for (i,j),q in edges.items())

def best_plan(masses,costs,tries=9):
    n=len(masses);fallback=antipodal(masses);data=run_data(masses)
    if not data[0]:return fallback,dict(kind='zero')
    p=data[2];offsets=data[4]
    lo=max(-d for d in offsets);hi=min(pi-d for pi,d in zip(p,offsets))
    best=fallback;value=plan_cost(best,costs,n);info=dict(kind='antipodal')
    if lo<=hi:
        for j in range(tries):
            t=lo+(hi-lo)*j//max(1,tries-1)
            edges=plan_at(data,t);v=plan_cost(edges,costs,n)
            if v<value:best=edges;value=v;info=dict(kind='adjacent',t=t,lo=lo,hi=hi)
    check_plan(masses,best)
    return best,info

if __name__=='__main__':
    import numpy as np
    from scipy.optimize import linprog
    from scipy.sparse import kron,eye,vstack
    from datetime import datetime,timezone
    from pathlib import Path
    import json
    n=384;unit=2**42;theta=(np.arange(n)+.5)*2*np.pi/n;alpha=.5
    point_cost=(2*np.sin(np.pi*np.arange(n//2+1)/n))**alpha
    cell_cost=(2*np.sin(np.minimum(np.pi/2,np.pi*(np.arange(n//2+1)+1)/n)))**alpha
    rows=[]
    for r in [1,1.25,1.5,2,3,5,10]:
        q=1/(4*r*r);g=(np.exp(-3j*theta)/(np.pi*(1-q*np.exp(-2j*theta))**2)*1j).real
        half=[int(round(float(v)*2*np.pi/n*unit)) for v in g[:n//2]];m=half+[-v for v in half]
        edges,info=best_plan(m,point_cost)
        exact=plan_cost(edges,point_cost,n)/unit*r**(alpha-2)
        worst=plan_cost(edges,cell_cost,n)/unit*r**(alpha-2)
        rows.append(dict(radius=r,point_cost=exact,cell_cost=worst,plan=info))
    # Exact conservation has already been checked. Compare with small independent LPs.
    comparisons=[]
    for n in [24,48]:
      theta=(np.arange(n)+.5)*2*np.pi/n
      for phi in [0,.37,1.1,np.pi/2]:
        q=.25;g=(np.exp(1j*phi-3j*theta)/(np.pi*(1-q*np.exp(-2j*theta))**2)).real
        half=[int(round(float(v)*unit)) for v in g[:n//2]];m=half+[-v for v in half]
        costs=(2*np.sin(np.pi*np.arange(n//2+1)/n))**alpha
        edges,info=best_plan(m,costs)
        pos=[i for i,v in enumerate(m) if v>0];neg=[i for i,v in enumerate(m) if v<0]
        c=np.array([[costs[min(abs(i-j),n-abs(i-j))] for j in neg] for i in pos])
        matrix=vstack([kron(eye(len(pos)),np.ones((1,len(neg)))),kron(np.ones((1,len(pos))),eye(len(neg)))],format='csr')
        rhs=np.array([m[i]/unit for i in pos]+[-m[j]/unit for j in neg])
        lp=linprog(c.ravel(),A_eq=matrix,b_eq=rhs,bounds=(0,None),method='highs')
        value=plan_cost(edges,costs,n)/unit
        assert lp.success and value>=lp.fun-1e-8
        comparisons.append(dict(n=n,phase=phi,plan=value,lp=lp.fun,ratio=value/lp.fun))
    out=dict(time_utc=datetime.now(timezone.utc).isoformat(),status='Diagnostic only, no continuous certificate',rows=rows,lp_comparisons=comparisons)
    Path('data/circle_integer_plan_diagnostic.json').write_text(json.dumps(out,indent=2)+'\n')
    for row in rows:print(row)
    print('max LP ratio',max(v['ratio'] for v in comparisons))
