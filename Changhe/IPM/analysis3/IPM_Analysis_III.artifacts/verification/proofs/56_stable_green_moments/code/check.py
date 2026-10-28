import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'): os.environ[key]='1'
from pathlib import Path
from fractions import Fraction as Q
from math import factorial, comb
from datetime import datetime,timezone
import hashlib,json
import numpy as np
from flint import arb,ctx
TOP=Path(__file__).resolve().parents[1]
SOURCE=TOP.parents[2]/'source/analysis1/IPM_Analysis_I.artifacts/numerics/data/trial_v2_h0.008.npz'
if not SOURCE.is_file():
    SOURCE=TOP.parents[1]/'research_copy/analysis1/IPM_Analysis_I.artifacts/numerics/data/trial_v2_h0.008.npz'
def aa(x):
    return arb(x.numerator)/x.denominator if isinstance(x,Q) else arb(x)
def rec(x):
    return {'ball':x.str(60),'radius':x.rad().str(12)}
def phi(z,p,N=48):
    value=arb(0); term=arb(1)
    for j in range(N):
        value+=term/(p+j+1);term*=z/(j+1)
    M=abs(z).upper()
    error=(M.exp()*M**N/factorial(N)/(N+p+1)).upper()
    return value+arb(0,error)
def primitive(lam,p,x):
    return sum(((-1)**j*arb(factorial(p)//factorial(p-j))*x**(p-j)/lam**(j+1) for j in range(p+1)),arb(0))
def hull(x,y): return x.union(y)
sha=hashlib.sha256(SOURCE.read_bytes()).hexdigest()
assert sha=='a069d85d102e17340778042f85c003705716ba799c0f68873d10c1c582ea4874'
raw=np.load(SOURCE,allow_pickle=False)
bi=Q.from_float(float(raw['bi']));lamq=bi+4-54
assert lamq==Q(75,70368744177664)
out={'date':datetime.now(timezone.utc).isoformat(),'source':str(SOURCE),'source_sha256':sha,'lambda_exact':str(lamq)}
vals=[]
for precision in (160,384,640):
    ctx.prec=precision;lam=aa(lamq);p=6
    old=arb(-52).exp()*(primitive(lam,p,arb(0))-(-lam).exp()*primitive(lam,p,arb(-1)))
    stable=arb(-52).exp()*phi(-lam,p)
    vals.append((old,stable))
    out[str(precision)]={'primitive':rec(old),'stable':rec(stable),'overlap':old.overlaps(stable)}
    assert old.overlaps(stable)
ctx.prec=640
assert vals[0][1].contains(vals[-1][1])
beta=arb(52);c=arb(50);p=6
bound=(arb(p+1)/(arb(1).exp()*c))**(p+1)/(p+1)
out['weighted_halfline_bound_eta2']=rec(bound)
# Signed polynomial forcing F(s)=1-3s+2s^2 has exact range [-1/8,1] on [0,1].
# Check both endpoints and each interior rational point. Exact theorem supplies continuum coverage.
I=arb(Q(7,16).numerator)/16+arb(0,arb(9)/16)
checks=[]
for n in (1,2,27):
    alpha=arb(2*n+2);beta=arb(2*n-2);h=arb(1);A0=arb(3)/10;Bh=-arb(1)/5
    da=(-alpha).exp()
    Ar=hull(A0,da*A0+(1-da)*I/alpha)
    Br=hull(Bh,Bh+I) if n==1 else hull(Bh,(-beta).exp()*Bh+(1-(-beta).exp())*I/beta)
    for j in range(17):
        s=arb(j)/16
        # Integral_0^s exp(-alpha(s-u)) F(u)du.
        Av=(-alpha*s).exp()*A0
        for p,cp in enumerate((1,-3,2)):
            Av+=cp*(-alpha*s).exp()*s**(p+1)*phi(alpha*s,p,512)
        # u=s+v for the backward integral. F(s+v)=F(s)+(-3+4s)v+2v^2.
        d=1-s;Bv=(-beta*d).exp()*Bh
        for p,cp in enumerate((1-3*s+2*s*s,-3+4*s,arb(2))):
            Bv+=cp*d**(p+1)*phi(-beta*d,p,512)
        assert Ar.contains(Av) and Br.contains(Bv),(n,j,Ar,Av,Br,Bv)
    checks.append({'n':n,'A_range':rec(Ar),'B_range':rec(Br),'point_checks':17})
out['finite_hull_checks']=checks
out['verdict']='PASS: rigorous formulas; original-data resonance and numerical implementation checks'
out['finished']=datetime.now(timezone.utc).isoformat()
(TOP/'evidence/check.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2),flush=True)
