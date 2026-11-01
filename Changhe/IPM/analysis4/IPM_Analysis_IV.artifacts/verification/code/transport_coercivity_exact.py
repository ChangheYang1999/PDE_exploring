"""Seeded exact Laurent checks of highest-harmonic transport coercivity."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import json,random,time
from flint import fmpq
start=time.monotonic();rng=random.Random(981027)
root=Path('research/98_density_stream_equivalence/verification')

def add(a,b):
    out=dict(a)
    for key,v in b.items():out[key]=out.get(key,fmpq(0))+v
    return {key:v for key,v in out.items() if v!=0}
def scale(a,s):return {key:v*s for key,v in a.items() if v*s!=0}
def E(a):return {key:key[1]*v for key,v in a.items() if key[1]!=0}
def D(a):return {(q-1,m):q*v for (q,m),v in a.items() if q}
def multiply(a,b):
    out={}
    for (q,m),v in a.items():
        for (s,k),w in b.items():
            key=q+s,m+k;out[key]=out.get(key,fmpq(0))+v*w
    return {key:v for key,v in out.items() if v!=0}
def sine(data):
    out={}
    for (q,m),v in data.items():out[q,m]=v/2;out[q,-m]=-v/2
    return out
def norm(a,rho):return sum((abs(v)*rho**abs(m) for (q,m),v in a.items()),fmpq(0))
profiles=[('sin1',{1:fmpq(1)}),('sin1_sin3',{1:fmpq(1),3:fmpq(1)}),('mixed_sin5',{1:fmpq(1),3:fmpq(-2),5:fmpq(1,8)}),('sin7_smalltop',{1:fmpq(-3,2),3:fmpq(2),5:fmpq(-1),7:fmpq(1,17)})]
rows=[]
for delta in [fmpq(2,3),fmpq(4,9),fmpq(2,5),fmpq(3,7),fmpq(5,8)]:
    import math
    q0=int(2*delta.denominator//math.gcd(delta.numerator,2))
    i0=int((16*delta.denominator+delta.numerator-1)//delta.numerator)
    for label,lead in profiles:
        L=max(lead);rho=4
        while sum((abs(v)*rho**k for k,v in lead.items() if k<L),fmpq(0))*16>abs(lead[L])*rho**L:rho*=2
        S=sum((abs(v)*rho**k for k,v in lead.items() if k<L),fmpq(0))/(abs(lead[L])*rho**L)
        r=fmpq(1,rho*rho);c0=1-r-(1+r)*S;d0=(1+r)*(1+S)
        assert c0>=fmpq(223,256) and d0<=fmpq(289,256)
        F=sine({(0,m):v for m,v in lead.items()});EF=E(F);T=abs(lead[L])*rho**L/2
        for offset in [0,1,3,13]:
            i=i0+offset;K=i//q0;maxm=(L+1)*i
            patterns=[]
            for m in [2,2*((L+1)//2),maxm-(maxm%2)]:
                patterns.append(('basis_m%d'%m,{(K,m):fmpq(1)}))
            data={}
            for q in range(K+1):
                for m in [2,4,2*((L+1)//2),maxm-(maxm%2)]:
                    data[q,m]=fmpq(rng.randrange(-7,8),rng.randrange(1,9))
            patterns.append(('seeded_mixed',data))
            for pattern,data in patterns:
                G=sine(data);rad=add(scale(G,2-i*delta),D(G))
                out=add(multiply(rad,EF),scale(multiply(E(G),F),-(1-delta)))
                assert all(out.get((q,-m),fmpq(0))==-v for (q,m),v in out.items())
                lhs=norm(out,rho);rhs=T*L*delta*i*norm(G,rho)/8
                assert lhs>=rhs
                rows.append(dict(delta=str(delta),q0=q0,profile=label,L=L,rho=rho,i=i,log_degree=K,pattern=pattern,coercivity_margin_ratio=str(lhs/rhs),output_coefficients=len(out)))
result=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),seed=981027,arithmetic='exact rational',cases=len(rows),all_checks_pass=True,rows=rows,actual_elapsed_s=time.monotonic()-start)
(root/'exact_laurent_checks.json').write_text(json.dumps(result,indent=2)+'\n')
Path('research/98_density_stream_equivalence/sources/transport_coercivity_exact.py.txt').write_bytes(Path(__file__).read_bytes())
print(json.dumps({k:v for k,v in result.items() if k!='rows'}))
