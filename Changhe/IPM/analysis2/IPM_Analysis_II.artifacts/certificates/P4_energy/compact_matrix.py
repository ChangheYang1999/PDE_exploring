"""Exact compactified representation of fourth derivatives of the source potential.
Independent of all Cartesian-jet and numerical-lane evaluators.
"""
from pathlib import Path
from fractions import Fraction as Q
from math import comb
import json,sys,time
from datetime import datetime,timezone
from flint import arb,ctx
BASE=Path(__file__).resolve().parents[2]

def A(v):
    v=Q(v);return arb(v.numerator)/arb(v.denominator)

def add(T,kind,n,l,value):
    if n<0:
        n=-n
        if kind=='s':value=-value
    if not value or (kind=='s' and n==0):return
    key=kind,n,l
    T[key]=T.get(key,Q(0))+value
    if T[key]==0:del T[key]

def derivative(T,p,k,d,axis):
    out={}
    for (kind,n,l),v in T.items():
        s=2*k-d+2*l;u=p-k-l
        if axis=='x':
            add(out,kind,n+1,l,v*(s-n)/2)
            add(out,kind,n-1,l,v*(s+n)/2)
            add(out,kind,n+1,l+1,v*u)
            add(out,kind,n-1,l+1,v*u)
        elif kind=='c':
            add(out,'s',n+1,l,v*(s-n)/2)
            add(out,'s',n-1,l,-v*(s+n)/2)
            add(out,'s',n+1,l+1,v*u)
            add(out,'s',n-1,l+1,-v*u)
        else:
            add(out,'c',n-1,l,v*(s+n)/2)
            add(out,'c',n+1,l,-v*(s-n)/2)
            add(out,'c',n-1,l+1,v*u)
            add(out,'c',n+1,l+1,-v*u)
    return out

def chebyshev(n,kind='T'):
    seq=[[Q(1)],[Q(0),Q(1 if kind=='T' else 2)]]
    while len(seq)<=n:
        nxt=[Q(0)]*(len(seq[-1])+1)
        for k,v in enumerate(seq[-1]):nxt[k+1]+=2*v
        for k,v in enumerate(seq[-2]):nxt[k]-=v
        seq.append(nxt)
    return seq[n]

def construct(state):
    d=json.loads((BASE/'source_audit'/f'state{state:03d}_exact.json').read_text())
    gamma=1/Q(d['exact_parameters']['cl']);delta=1-gamma
    polys={}
    for label,axes in [('chi22','xxyy'),('chi04','yyyy'),('chi31','xxxy')]:
        for branch in range(4):
            trig={};p=(3+gamma-branch*delta)/2
            for (j,m,k),a in zip(d['canonical_order'],d['canonical_coefficients']):
                if j!=branch:continue
                T={('c',2*m,0):Q(a)}
                for di,axis in enumerate(axes):T=derivative(T,p,k,di,axis)
                for (kind,n,l),v in T.items():add(trig,kind,n,k-2+l,v)
            assert all(l>=0 for kind,n,l in trig)
            P={}
            for (kind,n,l),v in trig.items():
                assert n%2==0
                assert kind==('s' if label=='chi31' else 'c')
                C=chebyshev(n//2-1,'U') if kind=='s' else chebyshev(n//2)
                for zdeg,c in enumerate(C):P[l,zdeg]=P.get((l,zdeg),Q(0))+v*c
            P={key:v for key,v in P.items() if v}
            polys[label,branch]=P
    return d,delta,polys

def encode(P):return [[i,j,str(v)] for (i,j),v in sorted(P.items())]

def evaluate(polys,delta,t,z):
    fields={}
    w=(1-t)**(A(delta)/2)
    for label in ('chi22','chi04','chi31'):
        v=arb(0)
        for j in range(4):
            value=sum((A(a)*t**k*z**n for (k,n),a in polys[label,j].items()),arb(0))
            v+=w**(j+1)*value
        if label=='chi31':v*= (1-z*z).sqrt()
        fields[label]=v
    return fields

if __name__=='__main__':
    state=int(sys.argv[1]) if len(sys.argv)>1 else 131
    ctx.prec=320;start=time.monotonic()
    d,delta,P=construct(state)
    out={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'state':state,'delta':str(delta),'input_sha256':d['canonical_serialization_sha256'],'polynomials':{f'{label}_{j}':encode(p) for (label,j),p in P.items()},'crosschecks':[]}
    sys.path.insert(0,str(BASE/'source_audit'))
    from field_eval import State
    S=State(state,320)
    for xs,ys in [('0','0.1'),('0.5','0.5'),('1','2'),('3','1'),('0','10'),('15','20')]:
        x=A(xs);y=A(ys);q=x*x+y*y;t=q/(1+q);z=(x*x-y*y)/q
        f=evaluate(P,delta,t,z);old=S.evaluate(x,y)
        checks={'chi22':old['du22'],'chi04':-old['rho_y']-old['du22'],'chi31':old['du21']}
        record={'x':xs,'y':ys,'overlaps':{},'new_fields':{k:v.str(45) for k,v in f.items()}}
        for k,v in checks.items():
            record['overlaps'][k]=f[k].overlaps(v)
            assert record['overlaps'][k],(xs,ys,k,f[k],v)
        out['crosschecks'].append(record)
        print(state,xs,ys,'OK',flush=True)
    out['elapsed_seconds']=time.monotonic()-start
    Path(__file__).with_name(f'state{state:03d}_compact_polynomials.json').write_text(json.dumps(out,indent=2)+'\n')
    print('elapsed',out['elapsed_seconds'],flush=True)
