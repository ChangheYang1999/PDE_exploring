#!/usr/bin/env python3
"""Constraint, chain-rule and exponent-step checks of the moving affine chart."""
from pathlib import Path
import sys,time
import numpy as np
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT/'exploration'))
from s1_free_c import FreeExponentProblem
from independent_artifacts import atomic_json

def main():
    start=time.perf_counter();rows=[];rng=np.random.default_rng(748124)
    def check(name,error,tol):
        v=float(np.max(abs(error)))
        if not np.isfinite(v) or v>tol:raise AssertionError((name,v,tol))
        rows.append(dict(name=name,error=v,tolerance=tol))
    p=FreeExponentProblem(.6,2.,nradial=13,nangle=10);x=p.seed();x[:-1]=rng.normal(size=p.nfree)*.05
    for c_l in [.501,.55,.6,2/3,.749]:
        x[-1]=c_l;s=p.state(c_l);coeff=p.coefficients(x);f=p.field(x)
        check('affine constraints '+str(c_l),s['A']@coeff-s['target'],2e-11)
        check('source strain '+str(c_l),f.phi.evaluate(0.,0.,0,1)-.5,2e-11)
        check('source swirl '+str(c_l),f.q.evaluate(0.,0.)-2.,2e-11)
        projector=np.eye(s['A'].shape[1])-np.linalg.pinv(s['A'])@s['A']
        check('chart spans constrained space '+str(c_l),s['Z']@np.linalg.pinv(s['Z'])-projector,2e-11)
        J=p.jacobian(x);J2=p.jacobian(x,h=4e-6)
        check('c_l derivative step '+str(c_l),np.linalg.norm(J[:,-1]-J2[:,-1])/(1+np.linalg.norm(J2[:,-1])),1e-6)
        v=rng.normal(size=len(x));v/=np.linalg.norm(v);h=8e-6
        fd=(p.residual(x+h*v)-p.residual(x-h*v))/(2*h)
        check('full JVP '+str(c_l),np.linalg.norm(fd-J@v)/(1+np.linalg.norm(fd)),2e-6)
    x[-1]=.6;f=p.field(x);recovered=p.seed(f)
    check('field roundtrip',p.coefficients(recovered)-p.coefficients(x),1e-11)
    atomic_json(ROOT/'results/s1_free_c_tests.json',dict(all_passed=True,case_count=len(rows),elapsed_seconds=time.perf_counter()-start,rows=rows))
    print('PASS',len(rows),time.perf_counter()-start)
if __name__=='__main__':main()
