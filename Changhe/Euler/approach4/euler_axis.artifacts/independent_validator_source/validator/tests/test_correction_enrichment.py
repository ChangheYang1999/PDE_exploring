#!/usr/bin/env python3
"""A richer correction sector preserves old columns and exact source constraints."""
from pathlib import Path
from datetime import datetime,timezone
import sys,time,json
import numpy as np
from numpy.polynomial import Polynomial as Poly
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'exploration'))
from s1_green_pilot import source_basis,GreenS1Problem
from independent_fields import ScalarExpansion
from independent_farfield import angular_data
from eta_green_basis import EtaGreenField
from coefficient_tail import saved_powers,at_power
from independent_artifacts import atomic_json,sha256

def main():
    start=time.perf_counter();rows=[];rng=np.random.default_rng(529827)
    def check(name,error,tol):
        e=float(np.max(abs(error)))
        if not np.isfinite(e) or e>tol:raise AssertionError((name,e,tol))
        rows.append(dict(name=name,error=e,tolerance=tol))
    for c_l in [.56,2/3,.74]:
        alpha=(1-c_l)/c_l;m=3
        ee,qq=source_basis(c_l,m,3,2)
        ee2,qq2=source_basis(c_l,m,3,2,2*m)
        if ee!=ee2[:len(ee)] or qq!=qq2[:len(qq)]:raise AssertionError('old column order changed')
        check(f'basis inclusion {c_l}',0,0)
        check(f'enriched dimension {c_l}',len(ee2)-(m*3+2*m*2),0)
        A=np.zeros(2*m);A[1::2]=rng.normal(size=m);B=np.zeros(2*m-1);B[::2]=rng.normal(size=m)
        data=angular_data(alpha,A,B);p=2*alpha+1;A1=data['A1'];B1=data['B1'];mu=Poly([0.,1.]);s2=Poly([1.,0.,-1.])
        E1=-(p*(p-3)*A1+s2*A1.deriv(2)-4*mu*A1.deriv())
        e=np.array([E1.coef[j] if j<len(E1.coef) and abs(2*beta-j-(p+2))<1e-10 else 0. for i,j,beta in ee2])
        q=np.array([B1.coef[j] if j<len(B1.coef) and abs(2*beta-j-(p+1))<1e-10 else 0. for i,j,beta in qq2])
        field=EtaGreenField(ScalarExpansion([(v,*t) for v,t in zip(e,ee2)]),ScalarExpansion([(v,*t) for v,t in zip(q,qq2)]),c_l)
        pp,qp,_=saved_powers(field,p,p+1);nodes=np.linspace(-1,1,37)
        check(f'correction stream span {c_l}',at_power(pp,p)(nodes)-A1(nodes),2e-10)
        check(f'correction swirl span {c_l}',at_power(qp,p+1)(nodes)-B1(nodes),2e-10)
    for pole in [False,True]:
        p=GreenS1Problem(.74,2.,angular=3,radial=3,correction=1,correction_angular=6,nradial=13,nangle=12,pole=pole)
        x,_=p.seed();x=x+.02*rng.normal(size=len(x));e,q=p.unpack(x);field=p.field(x)
        check(f'source constraints {pole}',p.C@np.r_[e,q],2e-10)
        check(f'source strain {pole}',field.phi.evaluate(0.,0.,0,1)-.5,2e-11)
        check(f'source amplitude {pole}',field.q.evaluate(0.,0.)-2,2e-11)
        rq,re=p.raw(x);d=field.reduced(p.r,p.z)
        check(f'assembled q {pole}',(rq-d['q'])/(1+np.max(abs(rq))),2e-11)
        check(f'assembled eta {pole}',(re-d['eta'])/(1+np.max(abs(re))),2e-11)
        v=rng.normal(size=len(x));v/=np.linalg.norm(v);h=2e-5;J=p.evaluate(x)[1]
        fd=(p.evaluate(x+h*v)[0]-p.evaluate(x-h*v)[0])/(2*h)
        check(f'JVP {pole}',np.linalg.norm(fd-J@v)/(1+np.linalg.norm(J@v)),2e-8)
    files=[Path(__file__),ROOT/'exploration/s1_green_pilot.py',ROOT/'src/eta_green_basis.py',ROOT/'src/coefficient_tail.py']
    record=dict(completed_utc=datetime.now(timezone.utc).isoformat(),all_passed=True,case_count=len(rows),rows=rows,elapsed_seconds=time.perf_counter()-start,source_sha256={str(p.relative_to(ROOT)):sha256(p) for p in files})
    atomic_json(ROOT/'results/correction_enrichment_tests.json',record);print(json.dumps(dict(all_passed=True,case_count=len(rows),elapsed_seconds=record['elapsed_seconds'])))
if __name__=='__main__':main()
