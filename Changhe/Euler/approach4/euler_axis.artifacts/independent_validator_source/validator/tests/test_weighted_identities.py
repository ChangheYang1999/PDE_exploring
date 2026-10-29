#!/usr/bin/env python3
from pathlib import Path
import datetime,hashlib,json,time
import numpy as np
from independent_fields import manufactured_power,manufactured_gaussian,ScalarExpansion,PotentialField
from independent_weighted_identities import weighted_circulation_suite,weighted_circulation,axial_identity
ROOT=Path(__file__).resolve().parents[1];checks=[]
def check(name,error,tolerance,detail=None):
    row={'name':name,'error':float(error),'tolerance':float(tolerance),'passed':bool(np.isfinite(error) and error<=tolerance)}
    if detail is not None:row['detail']=detail
    checks.append(row);print(json.dumps(row),flush=True)

def main():
    start=time.time();exception=None
    try:
        fields=[manufactured_power(.51),manufactured_power(.74),manufactured_gaussian()]
        for index,field in enumerate(fields):
            records=weighted_circulation_suite(field,nradial=64,nangle=64)
            for k,row in enumerate(records):
                check(f'infinite_domain_residual_identity_{index}_{k}',row['quadrature_consistency_relative'],2e-10,row)
                other=weighted_circulation(field,row['p'],row['beta'],nradial=96,nangle=80,split_radius=2*field.phi.length)
                error=max(abs(row[key]-other[key])/(1+abs(other[key])) for key in ['I','J','K_residual_integral'])
                check(f'quadrature_and_split_refinement_{index}_{k}',error,2e-10)
            diluted=field.dilate(1.71)
            row=records[2];other=weighted_circulation(diluted,row['p'],row['beta'],nradial=64,nangle=64)
            factor=1.71**(2*row['p']+3-row['beta'])
            check(f'weighted_dilation_{index}',max(abs(other[key]-factor*row[key])/(1+abs(other[key])) for key in ['I','J','K_residual_integral']),3e-12)
            line=axial_identity(field,np.linspace(-4,4,61),q0=.37)
            check(f'axis_differential_identity_{index}',np.max(np.abs(line['differential_identity_error'])),5e-13)
        c=.63;q0=.7;z0=.4
        linear=PotentialField(ScalarExpansion([(.5,0,1,0.),(-(1+c)*z0/2,0,0,0.)]),ScalarExpansion([(q0,0,0,0.)]),c)
        line=axial_identity(linear,np.linspace(-3,3,41),q0)
        check('exact_shifted_axis_branch',np.max(np.abs(line['H'])),1e-15)
    except Exception as exc:
        import traceback;traceback.print_exc();exception=repr(exc)
    paths=[Path(__file__),ROOT/'src/independent_fields.py',ROOT/'src/independent_weighted_identities.py']
    record={'recorded_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'elapsed_seconds':time.time()-start,
            'checks':checks,'exception':exception,'source_sha256':{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths},
            'all_passed':exception is None and all(c['passed'] for c in checks)}
    (ROOT/'results/weighted_identity_tests.json').write_text(json.dumps(record,indent=2,allow_nan=False)+'\n')
    print(json.dumps({'all_passed':record['all_passed'],'checks':len(checks),'elapsed_seconds':record['elapsed_seconds']}))
    raise SystemExit(0 if record['all_passed'] else 1)
if __name__=='__main__':main()
