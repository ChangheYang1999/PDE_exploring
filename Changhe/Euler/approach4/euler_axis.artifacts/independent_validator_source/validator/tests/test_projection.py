#!/usr/bin/env python3
from pathlib import Path
import datetime,hashlib,json,time
import numpy as np
from independent_fields import manufactured_power,ScalarExpansion
from independent_projection import ShellProjection,project_shell
from independent_geometry import shell_quadrature
from independent_pressure import GreenPoisson
from independent_registered_metrics import evaluate_set
ROOT=Path(__file__).resolve().parents[1];checks=[]
def check(name,error,tolerance,detail=None):
    row={'name':name,'error':float(error),'tolerance':float(tolerance),'passed':bool(np.isfinite(error) and error<=tolerance)}
    if detail is not None:row['detail']=detail
    checks.append(row);print(json.dumps(row),flush=True)

def main():
    start=time.time();exception=None
    try:
        # Chain operators checked on a polynomial in s,z, independently of
        # the envelope recurrence and including both rotation-axis poles.
        f=ScalarExpansion([(1.,2,1,0.),(.4,1,2,0.),(-.7,0,3,0.)])
        projection=ShellProjection(lambda s,z:f.evaluate(s,z),.4,.8,radial_degree=14,angular_degree=12,trim_relative=2e-15)
        R=np.array([.42,.57,.79])[:,None];mu=np.array([-1.,-.4,0.,.23,1.])[None,:]
        s=R*R*(1-mu*mu);z=R*mu
        for ds in range(4):
            for dz in range(4-ds):
                exact=f.evaluate(s,z,ds,dz);value=projection.evaluate(s,z,ds,dz)
                check(f'polynomial_chain_{ds}_{dz}',np.max(np.abs(exact-value))/(1+np.max(np.abs(exact))),2e-9)
        field=manufactured_power();pressure=GreenPoisson(field.source,decay_power=2*field.alpha,lmax=12,nangle=32,nradial=24)
        for k in [-2,0,4,10]:
            lo,hi=2.**k,2.**(k+1);grid=shell_quadrature(lo,hi,nradial=8,nangle=64)
            P,G=pressure.on_spheres(grid['radii'],grid['mu'])
            reference,arr=evaluate_set(field,grid['r'],grid['z'],grid['weights'],P,G)
            history=[]
            for nr,na in [(12,12),(20,18),(32,24)]:
                projected=project_shell(field,lo,hi,radial_degree=nr,angular_degree=na,trim_relative=2e-18,extended=True)
                measured,other=evaluate_set(projected,grid['r'],grid['z'],grid['weights'],P,G)
                errors={name:float(np.max(np.abs(other[name]-arr[name]))/(np.max(np.abs(arr[name]))+1e-300))
                        for name in ['U','M','q_residual','eta_residual']}
                history.append({'degrees':[nr,na],'errors':errors,'phi_projection':projected.phi.metadata,'q_projection':projected.q.metadata})
            check(f'shell_projected_values_{k}',history[-1]['errors']['U'],2e-10,history)
            check(f'shell_projected_residuals_{k}',max(history[-1]['errors'][name] for name in ['M','q_residual','eta_residual']),2e-6)
    except Exception as exc:
        import traceback;traceback.print_exc();exception=repr(exc)
    paths=[Path(__file__),ROOT/'src/independent_projection.py',ROOT/'src/independent_registered_metrics.py']
    record={'recorded_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'elapsed_seconds':time.time()-start,
            'checks':checks,'exception':exception,'source_sha256':{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths},
            'all_passed':exception is None and all(c['passed'] for c in checks)}
    (ROOT/'results/projection_tests.json').write_text(json.dumps(record,indent=2,allow_nan=False)+'\n')
    print(json.dumps({'all_passed':record['all_passed'],'checks':len(checks),'elapsed_seconds':record['elapsed_seconds']}))
    raise SystemExit(0 if record['all_passed'] else 1)
if __name__=='__main__':main()
