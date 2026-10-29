#!/usr/bin/env python3
"""Compare the fast rejection path with all relevant frozen metric outputs."""
import datetime,json,time
from pathlib import Path
import numpy as np
from independent_fields import PotentialField,ScalarExpansion,manufactured_power
from eta_green_basis import EtaGreenField
from independent_geometry import shell_quadrature
from independent_registered_metrics import evaluate_set,registered_shells
from reduced_screen import evaluate_reduced_set,reduced_shells,aggregate_reduced
from independent_artifacts import atomic_json,sha256
ROOT=Path(__file__).resolve().parents[1]
checks=[]

def check(name,error,tolerance):
    checks.append({'name':name,'error':float(error),'tolerance':tolerance,'passed':bool(np.isfinite(error) and error<=tolerance)})
    if not checks[-1]['passed']:raise AssertionError(checks[-1])

class ZeroPressure:
    def on_spheres(self,R,mu):return np.zeros((len(R),len(mu))),np.zeros((len(R),len(mu),2))
    def evaluate(self,r,z):return np.zeros_like(r),np.zeros(np.shape(r)+(2,))

def main():
    start=time.perf_counter();error=None
    try:
        field=manufactured_power()
        eta=ScalarExpansion([(1.1,0,1,2.8),(-.2,1,1,4.4)])
        green=EtaGreenField(eta,ScalarExpansion([(.9,0,0,1.5),(.15,0,1,2.7)]),.6)
        for i,f in enumerate([field,green]):
            for collar in [False,True]:
                g=shell_quadrature(.17,2.3,nradial=3,nangle=12,collar=collar)
                shape=g['r'].shape
                fast,arrays=evaluate_reduced_set(f,g['r'],g['z'],g['weights'])
                full,fa=evaluate_set(f,g['r'],g['z'],g['weights'],np.zeros(shape),np.zeros(shape+(2,)))
                for eq in ['q','eta']:
                    for name in ['rms','maximum','linear_rms','nonlinear_rms','denominator','rho','m']:
                        x=fast['equations'][eq][name];y=full['equations'][eq][name]
                        check(f'metric {i} {collar} {eq} {name}',abs(x-y)/(1+abs(y)),2e-13)
                    check(f'raw {i} {collar} {eq}',np.max(np.abs(arrays[eq+'_residual']-fa[eq+'_residual'])),2e-13)
                check(f'dtype {i} {collar}',float(any(v.dtype!=np.float64 for v in arrays.values())),0)
        a,aa=reduced_shells(field,.8,shell_indices=[-1,0],include_origin=True)
        b,bb=registered_shells(field,ZeroPressure(),.8,shell_indices=[-1,0],include_origin=True)
        for ar,br in zip(a['rows'],b['rows']):
            key=f"{ar['shell_index']}_{ar['set']}"
            for coord in ['r','z','weights','q_residual','eta_residual']:
                check(f'grids {key} {coord}',np.max(np.abs(aa[key+'_'+coord]-bb[key+'_'+coord])),1e-13)
            for eq in ['q','eta']:
                for name in ['rho','m','degenerate_linear','degenerate_nonlinear']:
                    check(f'aggregate {key} {eq} {name}',abs(float(ar['metrics']['equations'][eq][name])-float(br['metrics']['equations'][eq][name])),2e-13)
        check('reject manufactured non-solution',float(not a['aggregate']['rejected_by_reduced_measurements']),0)
        check('never assert acceptance',float(a['aggregate']['full_registered_acceptance']!='NOT_EVALUATED'),0)
        zero=PotentialField(ScalarExpansion([]),ScalarExpansion([]),.6)
        z,_=reduced_shells(zero,1.,shell_indices=[0],include_origin=False)
        check('zero denominators remain undefined',abs(len(z['aggregate']['undefined_metrics'])-6),0)
        for kwargs in [{'nradial':7},{'nangle':63},{'nrandom':255}]:
            caught=False
            try:reduced_shells(field,1.,**kwargs)
            except ValueError:caught=True
            check('frozen minimum '+str(kwargs),float(not caught),0)
        g=shell_quadrature(.3,1.8,nradial=3,nangle=12)
        base,_=evaluate_reduced_set(field,g['r'],g['z'],g['weights'])
        for L in [.23,3.7]:
            scaled,_=evaluate_reduced_set(field.dilate(L),L*g['r'],L*g['z'],L**3*g['weights'])
            for eq in ['q','eta']:
                for name in ['rho','m']:
                    check(f'dilation {L} {eq} {name}',abs(scaled['equations'][eq][name]/base['equations'][eq][name]-1),2e-13)
    except Exception as exc:
        import traceback;traceback.print_exc();error=repr(exc)
    names=['tests/test_reduced_screen.py','src/reduced_screen.py','src/independent_registered_metrics.py','src/independent_geometry.py','src/independent_fields.py','src/eta_green_basis.py']
    result={'completed_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'case_count':len(checks),'all_passed':error is None and all(c['passed'] for c in checks),
            'checks':checks,'exception':error,'wall_seconds':time.perf_counter()-start,'source_sha256':{n:sha256(ROOT/n) for n in names}}
    atomic_json(ROOT/'results/reduced_screen_tests.json',result)
    print(json.dumps({k:result[k] for k in ['completed_utc','case_count','all_passed','wall_seconds','exception']}),flush=True)
    raise SystemExit(0 if result['all_passed'] else 1)
if __name__=='__main__':main()
