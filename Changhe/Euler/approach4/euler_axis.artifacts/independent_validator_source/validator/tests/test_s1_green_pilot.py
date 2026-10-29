#!/usr/bin/env python3
"""Independent checks of source-constrained eta/q Formulation A."""
from pathlib import Path
import sys,time
import numpy as np
from scipy.optimize import least_squares
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'exploration'))
from s1_green_pilot import GreenS1Problem
from independent_artifacts import atomic_json

def main():
    start=time.perf_counter();rows=[];rng=np.random.default_rng(513998)
    def check(name,value,tol):
        error=float(np.max(abs(value)))
        if not np.isfinite(error) or error>tol:raise AssertionError((name,error,tol))
        rows.append(dict(name=name,error=error,tolerance=tol))
    for c_l,K in [(.505,1.),(.6,1.),(.68,2.),(.74,2.)]:
        for pole in [False,True]:
            key=f'{c_l} {K} pole{pole}'
            p=GreenS1Problem(c_l,K,pole=pole,angular=4,radial=3,correction=1,nradial=17,nangle=12)
            b=p.base;x,_=p.seed()
            check('exact zero seed '+key,x,0.)
            old_coordinates=p.project(np.zeros(b.np+b.nq))
            check('same affine field '+key,p.lift(x)-p.lift(old_coordinates),1e-12)
            x+=.04*rng.normal(size=len(x));field=p.field(x);e,q=p.unpack(x)
            check('source strain '+key,field.phi.evaluate(0.,0.,0,1)-.5,1e-11)
            check('source swirl '+key,field.q.evaluate(0.,0.)-K,1e-11)
            check('hard equations '+key,p.C@np.r_[e,q],1e-10)
            rq,re=p.raw(x);direct=field.reduced(b.r,b.z)
            check('q assembly '+key,(rq-direct['q'])/(1+np.max(abs(rq))),2e-11)
            check('eta assembly '+key,(re-direct['eta'])/(1+np.max(abs(re))),2e-11)
            check('elliptic '+key,direct['elliptic']/(1+np.max(abs(b.E@e))),2e-11)
            v=rng.normal(size=len(x));v/=np.linalg.norm(v);h=3e-5;J=p.evaluate(x)[1]
            fd=(p.evaluate(x+h*v)[0]-p.evaluate(x-h*v)[0])/(2*h)
            check('JVP '+key,np.linalg.norm(fd-J@v)/(1+np.linalg.norm(J@v)),4e-8)
            hs=np.array([.04,.02]);small=field.reduced(.77*hs,.63*hs)
            check('source q order '+key,abs(small['q'][1])/(abs(small['q'][0])+1e-13),.075)
            check('source eta order '+key,abs(small['eta'][1])/(abs(small['eta'][0])+1e-13),.16)
            if pole:
                A,B,_=field.leading_polynomials()
                E=-(field.alpha*(field.alpha-3)*A+np.polynomial.Polynomial([1.,0.,-1.])*A.deriv(2)-4*np.polynomial.Polynomial([0.,1.])*A.deriv())
                check('independent angular pole '+key,c_l*E(1.)+2*K*B(1.),5e-10)
    p=GreenS1Problem(.6,2.)
    x,_=p.seed();initial=p.evaluate(x)[0];initial_loss=float(initial@initial)
    for method in ['trf','lm']:
        fit=least_squares(lambda x:p.evaluate(x)[0],x,jac=lambda x:p.evaluate(x)[1],method=method,x_scale='jac',max_nfev=100,ftol=1e-12,xtol=1e-12,gtol=1e-12)
        final=p.evaluate(fit.x)[0]
        check('optimizer decreases from exact zero '+method,float(final@final)/initial_loss,.01)
    atomic_json(ROOT/'results/s1_green_pilot_tests.json',dict(all_passed=True,case_count=len(rows),rows=rows,elapsed_seconds=time.perf_counter()-start))
    print('PASS',len(rows),time.perf_counter()-start)
if __name__=='__main__':main()
