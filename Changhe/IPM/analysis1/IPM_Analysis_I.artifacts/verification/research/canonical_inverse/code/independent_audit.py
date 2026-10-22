"""Cox basis in mpmath.iv vs de Boor in Arb, data and root audits.
Auxiliary checks, not an independent replacement for the Cauchy remainder proof.
"""
import os
for v in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[v]='1'
import json, bisect, hashlib, math
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
from mpmath import iv,mp
from flint import arb,ctx
from strain_arb import Data,aa,jsball,cn
BASE=Path(__file__).resolve().parents[3]
ctx.prec=192;ctx.cap=8;ctx.threads=1;iv.dps=65;mp.dps=70
raw=json.loads((BASE/'data_exact/x3.json').read_text());d=Data()
fr=lambda s:F.from_float(float.fromhex(s))
z=list(map(fr,raw['z_hex']));tt=list(map(fr,raw['spline_knots_hex']))
assert z[0]==fr(raw['scalars_hex']['k']) and 0<z[0]<1
assert len(z)==1+201*375+6 and len(tt)==376+7+1
assert tt==sorted(tt) and tt[:8]==[0]*8 and tt[-8:]==[1]*8
assert all(tt[i]<tt[i+1] for i in range(7,len(tt)-8))
assert len(d.co)==376 and len(d.co[0])==201
assert d.r0>0 and d.L>0 and d.p>6 and d.p<7
coef=[[F(0)]+z[1+m*375:1+(m+1)*375] for m in range(201)]
assert all(d.cm[m].contains(aa(max(map(abs,coef[m])))) for m in range(201))
def vi(x):
    if isinstance(x,F):return iv.mpf(x.numerator)/x.denominator
    return iv.mpf(x)
def vint(a,b):return iv.mpf([str(mp.mpf(a.numerator)/a.denominator),str(mp.mpf(b.numerator)/b.denominator)])
def exact_vint(a,b):
    # Hull of exact rational enclosures, endpoints rounded out by interval arithmetic.
    va,vb=vi(a),vi(b)
    return iv.mpf([va.a,vb.b])
def endpoints(v):
    return mp.mpf(v.a._mpi_[0]),mp.mpf(v.b._mpi_[1])
def overlaps(a,v):
    # Decimal display is itself rounded, so parse a deliberately widened Arb ball.
    b=arb(a.str(55));lo,hi=endpoints(v)
    vv=arb(str((lo+hi)/2),str((hi-lo)/2+mp.mpf('1e-60')))
    return b.overlaps(vv)
def iv_eval(qa,qb,ta,tb):
    q=exact_vint(qa,qb);theta=exact_vint(ta,tb);span=bisect.bisect_right(tt,(qa+qb)/2)-1
    basis={span:iv.mpf(1)}
    for degree in range(1,8):
        new={}
        for i in range(span-degree,span+1):
            a=iv.mpf(0);b=iv.mpf(0)
            if tt[i+degree]!=tt[i]:a=(q-vi(tt[i]))/vi(tt[i+degree]-tt[i])*basis.get(i,iv.mpf(0))
            if tt[i+degree+1]!=tt[i+1]:b=(vi(tt[i+degree+1])-q)/vi(tt[i+degree+1]-tt[i+1])*basis.get(i+1,iv.mpf(0))
            new[i]=a+b
        basis=new
    k=vi(z[0]);r0=vi(fr(raw['scalars_hex']['origin_radius']));p=6+2*k/(2-k)
    s=1-(1-q)**(2/(1-k));chi=s/(s+r0*r0*(1-s));S=iv.mpf(0)
    for m in range(201):
        bm=sum((vi(coef[m][j])*basis[j] for j in basis),iv.mpf(0))
        S+=bm*chi**max(0,m-1)*iv.cos(2*m*theta)
    # Independent forward Chebyshev recurrence.
    zz=2*q-1;pol=[iv.mpf(1),zz]
    for n in range(2,6):pol.append(2*zz*pol[-1]-pol[-2])
    T=sum((vi(z[-6+n])*pol[n] for n in range(6)),iv.mpf(0))
    S+=s**(p/2)*iv.cos(theta)**(p-2)*iv.sin(theta)**2*T
    return S,iv.cos(theta)**2*iv.sin(theta)*iv.sin(3*theta)*iv.exp(S)
def arb_eval(qa,qb,ta,tb):
    mid,rows=d.poly(qa,qb)
    q=arb(aa((qa+qb)/2),aa((qb-qa)/2).upper());theta=arb(aa((ta+tb)/2),aa((tb-ta)/2).upper())
    vals=d.radial(q,mid,rows)
    S=sum((vals[m]*(2*m*theta).cos() for m in range(201)),arb(0))+vals[-1]*theta.cos()**(d.p-2)*theta.sin()**2
    return S,theta.cos()**2*theta.sin()*(3*theta).sin()*S.exp()
checks=[]
for index,qa in enumerate([F(1,1000000),F(1,1000),F(1,10),F(1,3),F(9,10),1-F(1,1000000)]):
    qb=qa+F(1,2**45);ta=F(index+1,10);tb=ta+F(1,2**45)
    mvals=iv_eval(qa,qb,ta,tb);avals=arb_eval(qa,qb,ta,tb)
    assert all(overlaps(a,m) for a,m in zip(avals,mvals)),index
    checks.append({'q':[str(qa),str(qb)],'theta':[str(ta),str(tb)],'iv_S':str(mvals[0]),'arb_S':jsball(avals[0]),'iv_integrand':str(mvals[1]),'arb_integrand':jsball(avals[1]),'overlap':True})
roots=[]
for n in (20,32):
    pairs=[arb.legendre_p_root(n,i,weight=True) for i in range(n)]
    assert all(x>-1 and x<1 and w>0 for x,w in pairs)
    assert all(pairs[i][0]>pairs[i+1][0] for i in range(n-1))
    for degree in range(2*n):
        target=arb(0) if degree%2 else arb(2)/(degree+1)
        val=sum((w*x**degree for x,w in pairs),arb(0))
        assert val.overlaps(target),(n,degree)
    roots.append({'n':n,'moments_through':2*n-1,'all_positive_disjoint':True})
# Symbolic derivations independent of handwritten expansions.
import sympy as sp
r,m=sp.symbols('r m',positive=True);a,b=sp.Function('a')(r),sp.Function('b')(r);I,J=sp.Function('I')(r),sp.Function('J')(r)
psi=(r**m*J-r**(-m)*I)/2
repl={sp.diff(I,r,2):sp.diff(r**m*a,r),sp.diff(J,r,2):-sp.diff(r**(-m)*b,r),sp.diff(I,r):r**m*a,sp.diff(J,r):-r**(-m)*b}
forced=-(sp.diff(psi,r,2)+sp.diff(psi,r)/r-m*m*psi/r**2)
target=(sp.diff(a,r)-(m-1)*a/r+sp.diff(b,r)+(m+1)*b/r)/2
assert sp.simplify(forced.subs(repl)-target)==0
x,y=sp.symbols('x y',real=True);rr=x*x+y*y
assert sp.simplify(-sp.diff(x*y/rr**2,x)-y*(3*x*x-y*y)/rr**3)==0
th=sp.symbols('th',real=True);K=sp.cos(th)**2*sp.sin(th)*sp.sin(3*th)
JJ=sp.integrate(K,(th,0,sp.pi/3))-sp.integrate(K,(th,sp.pi/3,sp.pi/2))
assert sp.simplify(JJ-(sp.pi/48+3*sp.sqrt(3)/32))==0
result={'utc':datetime.now(timezone.utc).isoformat(),'input_checks':'PASS','iv_method':'Cox basis recurrence + forward Chebyshev, 65 decimal interval digits','point_box_checks':checks,'Gauss_audit':roots,'symbolic_checks':['density-mode Green ODE','central-strain kernel derivative','absolute angular factor integral'],'scope':'Auxiliary independent audit, not a second certified whole integral. Gaussian library guarantees and Cauchy proof remain explicit dependencies.'}
(BASE/'research/canonical_inverse/evidence/independent_audit.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='point_box_checks'}))
