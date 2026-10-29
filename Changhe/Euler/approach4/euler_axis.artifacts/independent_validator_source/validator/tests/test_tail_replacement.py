#!/usr/bin/env python3
"""Degree bounds, exterior cancellation, dilation and untouched interior checks."""
from pathlib import Path
from datetime import datetime,timezone
import time,json
import numpy as np
from numpy.polynomial import Polynomial as Poly,Legendre
from scipy.special import roots_legendre
from independent_farfield import angular_data,evaluate_vector
from independent_artifacts import atomic_json,sha256
from coefficient_tail import coefficient_audit,velocity_coefficients
from piecewise_loading import load_piecewise
from tail_replacement import first_correction_polynomials,replace_first_correction
ROOT=Path(__file__).resolve().parents[1]

def main():
    start=time.perf_counter();rows=[]
    def check(name,error,tol):
        error=float(np.max(abs(error)))
        if not np.isfinite(error) or error>tol:raise AssertionError((name,error,tol))
        rows.append(dict(name=name,error=error,tolerance=tol))
    rng=np.random.default_rng(284391);mu,w=roots_legendre(96)
    for alpha in [.38,.5,.8,.99]:
        for a,b in [(2,3),(5,4),(7,6)]:
            A=Poly(rng.normal(size=a+1)/np.arange(1,a+2)**2);B=Poly(rng.normal(size=b+1)/np.arange(1,b+2)**2)
            A1,B1,info=first_correction_polynomials(alpha,A,B)
            check(f'A degree {alpha} {a} {b}',max(0,A1.degree()-(2*max(a,b)+1)),0)
            check(f'B degree {alpha} {a} {b}',max(0,B1.degree()-(a+b+1)),0)
            d=angular_data(alpha,A,B)
            check(f'velocity reconstruction {alpha} {a} {b}',velocity_coefficients(2*alpha+1,A1,B1,mu)-evaluate_vector(d,mu,'G'),3e-11)
            Ap,Bp,proj=first_correction_polynomials(alpha,A,B,2*max(a,b)+1)
            check(f'full projection {alpha} {a} {b}',velocity_coefficients(2*alpha+1,Ap,Bp,mu)-evaluate_vector(d,mu,'G'),1e-9)
    for m in [2,3,4]:
        A=np.zeros(2*m);A[1::2]=rng.normal(size=m);B=np.zeros(2*m-1);B[::2]=rng.normal(size=m)
        Ap,Bp,info=first_correction_polynomials(.5,A,B)
        check(f'odd A1 m{m}',Ap.coef[::2],1e-13)
        check(f'even B1 m{m}',Bp.coef[1::2],1e-13)
        check(f'A parity degree m{m}',max(0,Ap.degree()-(4*m-1)),0)
        check(f'B parity degree m{m}',max(0,Bp.degree()-(4*m-2)),0)
    paths=['S1_pilot_L0_20261028T2003Z','S1_pilot2_L0_20261028T2100Z']
    for name in paths:
        old=load_piecewise(ROOT/'external_exports'/name/'coeffs.npz')
        new,info=replace_first_correction(old)
        for key in ['phi_el0','q_el0','phi_el1','q_el1']:check(name+' untouched '+key,new.coefficients[key]-old.coefficients[key],0)
        x=np.array([[0.,0.,0.],[.2,.3,-.4],[3.,2.,1.]])
        check(name+' exact inner values',new.cartesian(x)-old.cartesian(x),0)
        A,B=old.leading_polynomials();C,D=new.leading_polynomials()
        check(name+' unchanged leading A',A(mu)-C(mu),1e-12);check(name+' unchanged leading B',B(mu)-D(mu),1e-12)
        scaled,info2=replace_first_correction(old.dilate(.17))
        check(name+' dilation covariance',scaled.cartesian(np.array([[30.,20.,5.]]))-.17*new.cartesian(np.array([[30.,20.,5.]])/.17),1e-10)
        gauged,_=new.reporting_gauge();result=coefficient_audit(gauged,np.array([4.,16.]),mu,w)
        check(name+' corrected coefficient identity',result['correction_mismatch_sphere_norm'],3e-10)
        low,info3=replace_first_correction(old,12)
        gl,_=low.reporting_gauge();d=coefficient_audit(gl,np.array([4.,16.]),mu,w)
        check(name+' projected defect ratio',d['correction_relative_to_Euler']-info3['projection']['omitted_relative_norm'],2e-9)
    record=dict(completed_utc=datetime.now(timezone.utc).isoformat(),all_passed=True,case_count=len(rows),rows=rows,elapsed_seconds=time.perf_counter()-start,
        source_sha256={str(p.relative_to(ROOT)):sha256(p) for p in [Path(__file__),ROOT/'src/tail_replacement.py',ROOT/'src/coefficient_tail.py',ROOT/'src/independent_farfield.py',ROOT/'src/piecewise_adapter.py',ROOT/'src/piecewise_jacobi.py']})
    atomic_json(ROOT/'results/tail_replacement_tests.json',record);print(json.dumps(dict(all_passed=True,case_count=len(rows),elapsed_seconds=record['elapsed_seconds'])))
if __name__=='__main__':main()
