#!/usr/bin/env python3
from pathlib import Path
import datetime,hashlib,json,time
import numpy as np
from independent_fields import ScalarExpansion,PotentialField,manufactured_gaussian,manufactured_power
from independent_diagnostics import axis_audit
from independent_stagnation import stagnation_audit,evaluate_transport
ROOT=Path(__file__).resolve().parents[1]
checks=[]
def check(name,error,tolerance,detail=None):
    row={'name':name,'error':float(error),'tolerance':float(tolerance),'passed':bool(np.isfinite(error) and error<=tolerance)}
    if detail is not None:row['detail']=detail
    checks.append(row);print(json.dumps(row),flush=True)

def main():
    start=time.time();exception=None
    try:
        for k,field in enumerate([manufactured_gaussian(),manufactured_power()]):
            audit=axis_audit(field,[-1.1,-.3,0.,.7,1.3])
            for name in ['q','eta']:
                errors=[a[name+'_quadratic_remainder_max'] for a in audit['quadratic_taylor_remainders']]
                check(f'quadratic_axis_{name}_{k}',max(errors[i+1]/errors[i] for i in range(3)),.08,{'errors':errors,'radii':[a['r'] for a in audit['quadratic_taylor_remainders']]})
        # This exact linear field is unbounded. It tests local statements only.
        b=.37
        for c in [.5,.6,.74]:
            field=PotentialField(ScalarExpansion([(.5,0,1,0.)]),ScalarExpansion([(b,0,0,0.)]),c)
            r=np.array([0.,.3,1.2]);z=np.array([.7,0.,-.4]);x=np.stack((r,np.zeros_like(r),z),axis=-1)
            gp=np.stack(((.25+b*b)*r,np.zeros_like(r),-2*z),axis=-1)
            check(f'exact_linear_momentum_c{c}',np.max(np.abs(field.primitive_cartesian(x,gp))),2e-15)
            # Moving the stagnation point is not an admissible decay gauge.
            # This separate unbounded solution tests the necessary linear
            # pressure term at a nonzero axial coordinate.
            z0=.43
            shifted=PotentialField(ScalarExpansion([(.5,0,1,0.),(-(1+c)*z0/2,0,0,0.)]),
                                   ScalarExpansion([(b,0,0,0.)]),c)
            gps=np.stack(((.25+b*b)*r,np.zeros_like(r),-2*(z-z0)+c*(1-c)*z0),axis=-1)
            check(f'shifted_linear_momentum_c{c}',np.max(np.abs(shifted.primitive_cartesian(x,gps))),3e-15)
            check(f'shifted_axis_stagnation_c{c}',np.linalg.norm(evaluate_transport(shifted,0.,z0)[0]),2e-15)
            missing=gps.copy();missing[:,2]-=c*(1-c)*z0
            defect=shifted.primitive_cartesian(x,missing)[:,2]
            check(f'missing_pressure_linear_term_c{c}',np.max(np.abs(defect+c*(1-c)*z0)),3e-15)
            red=field.reduced(r,z)
            check(f'exact_linear_reduced_c{c}',max(np.max(np.abs(red['q'])),np.max(np.abs(red['eta']))),2e-15)
            W,J=evaluate_transport(field,0.,0.)
            check(f'axial_eigenvalues_c{c}',np.max(np.abs(np.sort(np.linalg.eigvals(J))-np.array([c-.5,c+1]))),2e-15)
            if c==.5:
                check('critical_stagnation_curve',max(np.linalg.norm(evaluate_transport(field,a,0.)[0]) for a in [.1,.7,2.]),2e-15)
            else:
                check(f'noncritical_radial_departure_c{c}',abs(evaluate_transport(field,1.,0.)[0][0]-(c-.5)),2e-15)
    except Exception as exc:
        import traceback;traceback.print_exc();exception=repr(exc)
    paths=[Path(__file__),ROOT/'src/independent_fields.py',ROOT/'src/independent_diagnostics.py',ROOT/'src/independent_stagnation.py']
    record={'recorded_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'elapsed_seconds':time.time()-start,'checks':checks,'exception':exception,
            'source_sha256':{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths},
            'all_passed':exception is None and all(c['passed'] for c in checks)}
    (ROOT/'results/axis_stagnation_tests.json').write_text(json.dumps(record,indent=2)+'\n')
    print(json.dumps({'all_passed':record['all_passed'],'checks':len(checks),'elapsed_seconds':record['elapsed_seconds']}))
    raise SystemExit(0 if record['all_passed'] else 1)
if __name__=='__main__':main()
