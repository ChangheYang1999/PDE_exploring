"""Pure exact center-certificate functions extracted from our audited result70 test.
No top-level candidate evaluation and no fitting-code imports.
"""
from fractions import Fraction as F
from math import factorial
from datetime import datetime,timezone
from core_generating_mp import endpoint_data
now=lambda:datetime.now(timezone.utc).isoformat()
def scale(v,c):return tuple(sorted(x*c for x in v))
def plus(v,w):return (v[0]+w[0],v[1]+w[1])
def absolute(v):return (F(0) if v[0]<=0<=v[1] else min(map(abs,v)),max(map(abs,v)))
def serial(v):return {'lo':str(v[0]),'hi':str(v[1]),'display':[float(x) for x in v]}
def certify(data):
    d=endpoint_data(data);H,Pt,Pw,s,a=[F(d[k]) for k in ('H','Pt','Pw','s','a')]
    if F(d['alpha'])!=3:raise ValueError('exp3 certificate only')
    h=H;pbase=F(0);q=Pw/s**2
    for r in d['patches']:
        q0,qu,qv,R,L=[F(r[k]) for k in ('q0','qu','qv','R','L')]
        h+=q0;pbase+=qu/R**2-q0/L**2;q+=qv/R**2-q0/L**2
    if h<=0:raise ArithmeticError('positive local chart failed')
    pbase+=h/3
    n=100;exlo=sum((F(3**k,factorial(k)) for k in range(n+1)),F(0));exhi=exlo+F(3**(n+1),factorial(n+1))/(1-F(3,n+2))
    ell=scale((exlo-1,exhi-1),-F(1,18));p=plus((pbase,pbase),scale(ell,Pt))
    g=plus(scale(p,-60/h),(-12*q/h**3,)*2);th=scale(p,-6*a/h**2)
    D=plus(scale(p,6*a/h**2-420/h),(-84*q/h**3,)*2)
    redundant=plus(scale(g,7),scale(th,-1))
    if not redundant[0]<=D[0]<=D[1]<=redundant[1]:raise ArithmeticError('independent assembly containment')
    N=plus(scale(absolute(g),7),absolute(th));N2=plus(scale(absolute(g),11),absolute(th))
    ratios={}
    for name,den in [('prompt',N),('grouped',N2)]:
        if den[0]<=0:ratios[name]=None
        else:
            num=absolute(D);ratios[name]=serial((num[0]/den[1],num[1]/den[0]))
    ac=None
    if not p[0]<=0<=p[1]:
        correction=scale(tuple(sorted(1/v for v in p)),14*q/h)
        ac=serial(plus((70*h,70*h),correction))
    return {'utc':now(),'source_sha256':data.get('source_sha256'),'endpoint_data':d,'h':str(h),'q':str(q),'p':serial(p),'Omega_xy':serial(g),'Theta_xxy':serial(th),'D':serial(D),'N':serial(N),'N2':serial(N2),'ratios':ratios,'a_center':ac,'exp3':serial((exlo,exhi)),'nonzero_D':D[1]<0 or D[0]>0,'scope':'Exact local test. No global chart, canonical inverse, rounding bound or residual supremum claimed.'}

