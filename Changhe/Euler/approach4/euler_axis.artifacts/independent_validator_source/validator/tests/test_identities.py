#!/usr/bin/env python3
from pathlib import Path
import datetime,time,json,hashlib
import numpy as np
from independent_fields import manufactured_gaussian,manufactured_power,ScalarExpansion
from independent_identities import finite_ball_balance,characteristic_balance,vorticity_and_jacobian

ROOT=Path(__file__).resolve().parents[1]
checks=[]
def check(name,error,tolerance,detail=None):
    row={'name':name,'error':float(error),'tolerance':tolerance,'passed':bool(np.isfinite(error) and error<=tolerance)}
    if detail is not None:row['detail']=detail
    checks.append(row);print(json.dumps(row),flush=True)

def main():
    start=time.time();exception=None
    try:
        scalar=ScalarExpansion([(.13,0,0,1),(-.17,0,1,1)],kernel='gaussian')
        def pressure(r,z):
            s=r*r
            return scalar.evaluate(s,z),np.stack((2*r*scalar.evaluate(s,z,1,0),scalar.evaluate(s,z,0,1)),axis=-1)
        for i,field in enumerate([manufactured_gaussian(),manufactured_power()]):
            for R in [.3,1.7,5.]:
                d=finite_ball_balance(field,pressure,R,nangle=48,nradial=28,residual_integrals=True)
                check(f'energy_balance_{i}_{R}',abs(d['energy_corrected_error']),2e-11,d)
                check(f'helicity_balance_{i}_{R}',abs(d['helicity_corrected_error']),2e-11)
            for initial in [[.4,.2],[1.3,-.7]]:
                traj=characteristic_balance(field,initial,(-2.,2.))
                check(f'characteristic_{i}_{initial}',max(d['max_corrected_error'] for d in traj),2e-9)
            xyz=np.array([[0,0,0],[0,0,.7],[.3,-.4,.2],[1.1,.4,-.8]],dtype=float)
            omega,J=vorticity_and_jacobian(field,xyz)
            U,JU=field.cartesian(xyz,True)
            curl=np.stack((JU[:,2,1]-JU[:,1,2],JU[:,0,2]-JU[:,2,0],JU[:,1,0]-JU[:,0,1]),axis=-1)
            check(f'cartesian_vorticity_{i}',np.max(np.abs(curl-omega)),4e-14)
            h=2e-4;Jfd=np.empty_like(J)
            for k in range(3):
                step=np.zeros(3);step[k]=h
                fp=vorticity_and_jacobian(field,xyz+step)[0];fm=vorticity_and_jacobian(field,xyz-step)[0]
                fpp=vorticity_and_jacobian(field,xyz+2*step)[0];fmm=vorticity_and_jacobian(field,xyz-2*step)[0]
                Jfd[...,k]=(-fpp+8*fp-8*fm+fmm)/(12*h)
            check(f'vorticity_derivative_fd_{i}',np.max(np.abs(Jfd-J)),2e-10)
            check(f'vorticity_divergence_{i}',np.max(np.abs(np.trace(J,axis1=-2,axis2=-1))),2e-14)
    except Exception as exc:
        import traceback;traceback.print_exc();exception=repr(exc)
    paths=[Path(__file__),ROOT/'src/independent_fields.py',ROOT/'src/independent_identities.py']
    record={'recorded_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'elapsed_seconds':time.time()-start,
            'checks':checks,'exception':exception,'all_passed':exception is None and all(c['passed'] for c in checks),
            'source_sha256':{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}}
    (ROOT/'results/identity_tests.json').write_text(json.dumps(record,indent=2)+'\n')
    print(json.dumps({'all_passed':record['all_passed'],'elapsed_seconds':record['elapsed_seconds']}))
    raise SystemExit(0 if record['all_passed'] else 1)
if __name__=='__main__':main()
