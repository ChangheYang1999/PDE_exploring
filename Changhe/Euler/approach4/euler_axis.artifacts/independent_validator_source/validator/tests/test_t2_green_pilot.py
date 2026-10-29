#!/usr/bin/env python3
"""Formulation-A assembly, elliptic inverse, constraints and derivative checks."""
from pathlib import Path
import sys,time
import numpy as np
from scipy.special import roots_legendre
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'exploration'))
from t2_green_pilot import GreenRingProblem
from eta_green_basis import EtaGreenField
from independent_pressure import GreenPoisson
from independent_artifacts import atomic_json

def main():
    start=time.perf_counter();rows=[];rng=np.random.default_rng(49123)
    def check(name,value,tol):
        error=float(np.max(abs(value)))
        if not np.isfinite(error) or error>tol:raise AssertionError((name,error,tol))
        rows.append(dict(name=name,error=error,tolerance=tol))
    for c_l,K in [(.56,.5),(.6,1.),(.68,2.),(.74,2.)]:
        problem=GreenRingProblem(c_l,K,angular=3,radial=3,correction=1,nradial=17,nangle=12)
        x,_=problem.seed();x+=.03*rng.normal(size=len(x));field=problem.field(x);e,q=problem.unpack(x)
        check(f'local phi/eta rows {c_l}',problem.Cp@e-problem.tp,3e-11)
        check(f'local q row {c_l}',problem.Cq@q-problem.tq,3e-12)
        rq,re=problem.raw(x);direct=field.reduced(problem.r,problem.z)
        check(f'q assembly {c_l}',(rq-direct['q'])/(1+np.max(abs(rq))),3e-11)
        check(f'eta assembly {c_l}',(re-direct['eta'])/(1+np.max(abs(re))),3e-11)
        check(f'elliptic {c_l}',direct['elliptic']/(1+np.max(abs(problem.E@e))),3e-11)
        direction=rng.normal(size=len(x));direction/=np.linalg.norm(direction);f,J=problem.evaluate(x);h=3e-5
        fd=(problem.evaluate(x+h*direction)[0]-problem.evaluate(x-h*direction)[0])/(2*h)
        check(f'JVP {c_l}',np.linalg.norm(fd-J@direction)/(1+np.linalg.norm(J@direction)),3e-8)
        zz=np.array([0.,.03,.7,2.,31.]);ss=np.zeros_like(zz)
        check(f'axis q zero {c_l}',field.q.evaluate(ss,zz),0.)
        check(f'axis eta zero {c_l}',field.eta_expansion.evaluate(ss,zz),0.)
        check(f'axis eta_s zero {c_l}',field.eta_expansion.evaluate(ss,zz,1,0),0.)
        rr=np.array([0.,.2,1.,2.,11.]);check(f'phi odd {c_l}',field.phi.evaluate(rr*rr,zz)+field.phi.evaluate(rr*rr,-zz),3e-12)
        check(f'q odd {c_l}',field.q.evaluate(rr*rr,zz)+field.q.evaluate(rr*rr,-zz),3e-12)
        rec=ROOT/'results'/f'green_roundtrip_c{c_l}.json';atomic_json(rec,field.as_dict());loaded=EtaGreenField.load(rec)
        check(f'serialization {c_l}',field.cartesian(np.c_[rr,np.zeros_like(rr),zz])-loaded.cartesian(np.c_[rr,np.zeros_like(rr),zz]),0.)
        scaled,gauge=field.reporting_gauge();A,B,_=field.leading_polynomials();As,Bs,_=scaled.leading_polynomials();L=gauge['dilation_L']
        check(f'leading A dilation {c_l}',As.coef-L**(1+field.alpha)*A.coef,2e-11)
        check(f'leading B dilation {c_l}',Bs.coef-L**(1+field.alpha)*B.coef,2e-11)
        if c_l==.6:
            inverse=GreenPoisson(lambda r,z:field.eta_expansion.evaluate(r*r,z),dimension=5,decay_power=field.alpha,lmax=12,nangle=24,nradial=48)
            points=np.array([[0.,0.],[0.,.3],[.4,-.7],[1.,0.],[3.,4.],[20.,-9.]])
            phi,grad=inverse.evaluate(points[:,0],points[:,1]);ss=points[:,0]**2;zz=points[:,1]
            expected=field.phi.jet(ss,zz,1)
            check('separate numerical Green inverse phi',phi-expected[0,0],3e-9)
            eg=np.c_[2*points[:,0]*expected[1,0],expected[0,1]]
            check('separate numerical Green inverse gradient',grad-eg,3e-9)
            mu,_=roots_legendre(31);R=1e5
            error=R**field.alpha*field.phi.evaluate(R*R*(1-mu*mu),R*mu)-A(mu)
            check('leading tail from source inverse',error,1e-4)
    atomic_json(ROOT/'results/t2_green_pilot_tests.json',dict(all_passed=True,case_count=len(rows),rows=rows,elapsed_seconds=time.perf_counter()-start))
    print('PASS',len(rows),time.perf_counter()-start)
if __name__=='__main__':main()
