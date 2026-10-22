#!/usr/bin/env python3
"""Small independent quadrature/differentiation tests; no fitting-code import."""
import hashlib,json,time
from datetime import datetime,timezone
from pathlib import Path
import mpmath as mp
import numpy as np
from exact_inverse import compiler,radial,evaluate

ROOT=Path(__file__).resolve().parent

def direct_cheb(n,x):
    if n==0:return mp.mpf(1)
    a,b=mp.mpf(1),x
    for _ in range(1,n):a,b=b,2*x*b-a
    return b

def run():
    started=datetime.now(timezone.utc).isoformat();begin=time.monotonic()
    ca=np.array([[1,.25,-.125,.0625],[.5,-.25,.125,0],[-.25,.125,0,.0625]])
    cg=np.array([[14,-2,.25,.125],[1,-.5,0,.25],[2,0,-.125,.0625]])
    comp=compiler(ca,cg);mp.mp.dps=75
    def rows(row,t):return mp.fsum(mp.mpf(float(v))*direct_cheb(n,2*t-1) for n,v in enumerate(row))
    def source(x,y,thermal):
        r2=x*x+y*y;t=(1+r2)**(-mp.mpf(1)/4);q=r2/(1+r2);phi=mp.atan2(y,x)
        ar=ca if thermal else cg
        v=mp.fsum(q**m*rows(row,t)*mp.cos(2*m*phi) for m,row in enumerate(ar))
        return x*x*y*t**6*v if thermal else x*y*t**5*v
    def psi(x,y):
        t=(1+x*x+y*y)**(-mp.mpf(1)/4)
        return evaluate(radial(comp,t),mp.atan2(y,x))['Psi']
    # Fourier projection by a separate uniform angular trapezoidal rule, exact
    # on this finite trigonometric space in exact arithmetic.
    angles=[2*mp.pi*(j+mp.mpf('.37'))/32 for j in range(32)]
    weights={k:[mp.fsum(2*mp.sin(2*k*p)*mp.sin(p)*mp.cos(p)*mp.cos(2*m*p)/32 for p in angles) for m in range(3)] for k in range(1,4)}
    def mode_B(r,k):
        t=(1+r*r)**(-mp.mpf(1)/4);q=r*r/(1+r*r)
        return q*t*mp.fsum(w*q**m*rows(row,t) for m,(row,w) in enumerate(zip(cg,weights[k])))
    records=[]
    # One representative radial point for each angular mode.
    for k,rs in [(1,'1.3'),(2,'2.1'),(3,'4.2')]:
        r=mp.mpf(rs);t=(1+r*r)**(-mp.mpf(1)/4);rad=radial(comp,t)
        expected=(rad['X'][k-1]+rad['Y'][k-1])/(4*k*t**3)
        inn=mp.quad(lambda v:v**(2*k+1)*mode_B(v,k),[0,r])
        def outer(u):
            if u==0:
                if k>1:return mp.mpf(0)
                return 2/mp.sqrt(r)*mp.fsum(w*rows(row,mp.mpf(0)) for w,row in zip(weights[k],cg))
            return 2*r**(2-2*k)*u**(4*k-5)*mode_B(r/u**2,k)
        out=mp.quad(outer,[0,mp.mpf('.25'),1])
        value=(r**(-2*k)*inn+r**(2*k)*out)/(4*k)
        err=abs(value-expected)
        assert err<mp.mpf('1e-55'),('quadrature',k,err)
        records.append({'kind':'independent_full_radial_integrals','k':k,'r':rs,'absolute_error':mp.nstr(err,25),'h':mp.nstr(value,55)})
    for xs,ys in [('0.75','0.5'),('2','1'),('4.5','2.25')]:
        x,y=mp.mpf(xs),mp.mpf(ys);r=mp.sqrt(x*x+y*y);t=(1+r*r)**(-mp.mpf(1)/4);phi=mp.atan2(y,x)
        ev=evaluate(radial(comp,t),phi)
        ux=-mp.diff(lambda z:psi(x,z),y);uy=mp.diff(lambda z:psi(z,y),x)
        omega=source(x,y,False);theta=source(x,y,True)
        tx=mp.diff(lambda z:source(z,y,True),x);ty=mp.diff(lambda z:source(x,z,True),y)
        ox=mp.diff(lambda z:source(z,y,False),x);oy=mp.diff(lambda z:source(x,z,False),y)
        ra=((2*x+ux)*tx+(2*y+uy)*ty)/(x*x*y*t**6)
        rg=((2*x+ux)*ox+(2*y+uy)*oy+omega-tx)/(x*y*t**5)
        ell=-mp.diff(lambda z:psi(z,y),x,2)-mp.diff(lambda z:psi(x,z),y,2)-omega
        vr=t*(ux*x+uy*y)/r;vp=t*(-ux*y+uy*x)/r
        errs={'fA':abs(ra-ev['fA']),'fG':abs(rg-ev['fG']),'elliptic':abs(ell),'Vr':abs(vr-ev['Vr']),'Vp':abs(vp-ev['Vp'])}
        assert max(errs.values())<mp.mpf('1e-50'),(xs,ys,errs)
        records.append({'kind':'direct_cartesian_differences','x':xs,'y':ys,'errors':{k:mp.nstr(v,25) for k,v in errs.items()}})
    logs=[{'k':mode['k'],'resonant_integer_coefficient':str(mode['P'][4*mode['k']+3] if 4*mode['k']+3<len(mode['P']) else 0)} for mode in comp['modes']]
    assert any(int(e['resonant_integer_coefficient']) for e in logs)
    result={'timestamp_start':started,'timestamp_end':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-begin,'dps':75,'ca':ca.tolist(),'cG':cg.tolist(),'records':records,'nonzero_log_tests':logs,'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'inverse_sha256':hashlib.sha256((ROOT/'exact_inverse.py').read_bytes()).hexdigest(),'status':'PASS','scope':'Manufactured evaluator tests, not exact profiles. Numerical differences, not interval enclosures.'}
    (ROOT/'verification/manufactured.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ('ca','cG','records')},indent=2))
    for rec in records:print(json.dumps(rec))

if __name__=='__main__':run()
