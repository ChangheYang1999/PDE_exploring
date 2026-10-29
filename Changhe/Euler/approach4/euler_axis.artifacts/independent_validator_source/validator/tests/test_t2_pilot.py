#!/usr/bin/env python3
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,sys,time
import numpy as np
import sympy as sp
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'exploration'))
from t2_pilot import RingProblem
ROWS=[]
def check(name,error,tolerance,detail=None):
    row=dict(name=name,error=float(error),tolerance=tolerance,passed=bool(np.isfinite(error) and error<=tolerance))
    if detail is not None:row['detail']=detail
    ROWS.append(row);print(json.dumps(row),flush=True)

def main():
    start=time.monotonic();exception=None
    try:
        s,z,c,K=sp.symbols('s z c K',real=True);nu=(1+c)/2;E=2*K*K/(3*c)
        phi=z*(c+nu*(1-s))+4*nu*z**3/3-E*s*s*z**3/6+E*s*z**5/5-4*E*z**7/105
        q=K*s*z;eta=sp.expand(-8*sp.diff(phi,s)-4*s*sp.diff(phi,s,2)-sp.diff(phi,z,2))
        ws=2*s*(c-sp.diff(phi,z));wz=c*z+2*phi+2*s*sp.diff(phi,s)
        rq=sp.expand(q+ws*sp.diff(q,s)+wz*sp.diff(q,z)-2*sp.diff(phi,z)*q)
        re=sp.expand((1+c)*eta+ws*sp.diff(eta,s)+wz*sp.diff(eta,z)-sp.diff(q*q,z))
        check('polynomial_eta_exact',int(sp.simplify(eta-E*s*s*z)!=0),0.)
        for key,expr in [('q',rq),('eta',re)]:
            for degree in range(3):check(f'polynomial_{key}_z{degree}',int(sp.simplify(expr.coeff(z,degree))!=0),0.)
        check('polynomial_axis_radial_eigenvalue',int(sp.simplify(c-sp.diff(phi,z).subs({s:0,z:0})+nu)!=0),0.)
        check('polynomial_axis_axial_eigenvalue',int(sp.simplify(sp.diff(wz,z).subs({s:0,z:0})-1-4*c)!=0),0.)
        check('polynomial_ring_radial_eigenvalue',int(sp.simplify(sp.diff(ws,s).subs({s:1,z:0})-1-c)!=0),0.)
        check('polynomial_ring_axial_eigenvalue',int(sp.simplify(sp.diff(wz,z).subs({s:1,z:0})-(2*c-1))!=0),0.)
        rng=np.random.default_rng(874100)
        for c_l,amplitude in [(.56,.5),(.6,1.),(.68,2.),(.74,4.)]:
            problem=RingProblem(c_l,amplitude,nradial=19,nangle=14)
            x,meta=problem.seed();x=x+.015*rng.normal(size=len(x));field=problem.field(x)
            p,q=problem.unpack(x)
            check(f'local_phi_rows_{c_l}',np.max(abs(problem.Cp@p-problem.tp)),3e-11)
            check(f'local_q_rows_{c_l}',np.max(abs(problem.Cq@q-problem.tq)),3e-12)
            rq,re=problem.raw(x);ref=field.reduced(problem.r,problem.z)
            check(f'q_residual_assembly_{c_l}',np.max(abs(rq-ref['q']))/(1+np.max(abs(rq))),3e-12)
            check(f'eta_residual_assembly_{c_l}',np.max(abs(re-ref['eta']))/(1+np.max(abs(re))),3e-12)
            direction=rng.normal(size=len(x));direction/=np.linalg.norm(direction)
            f,J=problem.evaluate(x);h=1e-5
            fd=(problem.evaluate(x+h*direction)[0]-problem.evaluate(x-h*direction)[0])/(2*h)
            check(f'coefficient_jacobian_{c_l}',np.linalg.norm(fd-J@direction)/(1+np.linalg.norm(J@direction)),2e-8)
            rr=np.array([0.,.17,.6,1.,2.]);zz=np.array([.13,-.27,.42,-.91,3.])
            check(f'odd_phi_{c_l}',np.max(abs(field.phi.evaluate(rr*rr,zz)+field.phi.evaluate(rr*rr,-zz))),3e-12)
            check(f'odd_q_{c_l}',np.max(abs(field.q.evaluate(rr*rr,zz)+field.q.evaluate(rr*rr,-zz))),3e-12)
            check(f'axis_q_zero_{c_l}',np.max(abs(field.q.evaluate(np.zeros(5),zz))),0.)
            d=field.cylindrical(1.,0.,3)
            check(f'ring_stagnation_{c_l}',max(abs(c_l+d['U'][0]),abs(d['U'][2])),3e-12)
            check(f'ring_eigenvalues_{c_l}',max(abs(c_l+d['ur_r']-(1+c_l)),abs(c_l+d['uz_z']-(2*c_l-1))),3e-11)
            check(f'ring_eta_slope_{c_l}',abs(d['eta_z']-2*amplitude**2/(3*c_l)),3e-11)
    except Exception as exc:
        import traceback;traceback.print_exc();exception=repr(exc)
    paths=[Path(__file__),ROOT/'exploration/t2_pilot.py',ROOT/'exploration/s1_pilot.py',ROOT/'src/independent_fields.py']
    record=dict(recorded_utc=datetime.now(timezone.utc).isoformat(),elapsed_seconds=time.monotonic()-start,
        checks=ROWS,exception=exception,all_passed=exception is None and all(row['passed'] for row in ROWS),
        source_sha256={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths})
    (ROOT/'results/t2_pilot_tests.json').write_text(json.dumps(record,indent=2)+'\n')
    print(json.dumps({k:record[k] for k in ['all_passed','elapsed_seconds','exception']}))
    raise SystemExit(0 if record['all_passed'] else 1)
if __name__=='__main__':main()
