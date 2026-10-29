#!/usr/bin/env python3
from pathlib import Path
import datetime,hashlib,json,time
import numpy as np
from independent_fields import ScalarExpansion,PotentialField,manufactured_power
from independent_geometry import core_scale,reporting_gauge,shell_quadrature,random_shell
from independent_registered_metrics import metric,evaluate_set,annotate_and_aggregate
ROOT=Path(__file__).resolve().parents[1];checks=[]
def check(name,error,tolerance,detail=None):
    row={'name':name,'error':float(error),'tolerance':float(tolerance),'passed':bool(np.isfinite(error) and error<=tolerance)}
    if detail is not None:row['detail']=detail
    checks.append(row);print(json.dumps(row),flush=True)

def main():
    start=time.time();exception=None
    try:
        # Pure Gaussian swirl has max |Omega|=2 at the origin and outermost
        # half-maximum sphere R=sqrt(log 2), as proved in evaluation_geometry.
        zero=ScalarExpansion([],kernel='gaussian');q=ScalarExpansion([(1.,0,0,1.)],kernel='gaussian')
        field=PotentialField(zero,q,.6);core=core_scale(field)
        check('analytic_gaussian_swirl_core',abs(core['a_eff']-np.sqrt(np.log(2.))),2e-10,core)
        check('analytic_gaussian_swirl_maximum',abs(core['max_vorticity']-2),2e-13)
        for L in [.17,3.1]:
            other=core_scale(field.dilate(L))
            check(f'core_scale_covariance_{L}',abs(other['a_eff']/L-core['a_eff']),3e-10)
            check(f'vorticity_dilation_invariance_{L}',abs(other['max_vorticity']-core['max_vorticity']),3e-13)
        for lo,hi in [(0.,.125),(.5,1.),(32.,64.)]:
            grid=shell_quadrature(lo,hi);volume=4*np.pi*(hi**3-lo**3)/3
            check(f'shell_volume_{lo}_{hi}',abs(np.sum(grid['weights'])/volume-1),2e-14)
            collar=shell_quadrature(lo,hi,collar=True);measure=2*np.arcsin(.05)*(hi**3-lo**3)/3
            check(f'collar_measure_{lo}_{hi}',abs(np.sum(collar['weights'])/measure-1),2e-14)
            points=random_shell(lo,hi,np.random.default_rng(371));R=np.hypot(points['r'],points['z'])
            check(f'random_domain_{lo}_{hi}',float(np.any(R<lo) or np.any(R>hi)),0)
        m=metric(np.ones(8),2*np.ones(8),100*np.ones(8),[2*np.ones(8),100*np.ones(8)],np.ones(8))
        check('minimum_term_metric',abs(m['rho']-.5)+abs(m['classical_per_term_ratio']-.01),1e-15,m)
        undefined=metric(np.zeros(8),np.zeros(8),np.zeros(8),[np.zeros(8)],np.ones(8))
        check('zero_denominator_not_silent_success',float(undefined['rho'] is not None or not undefined['undefined_denominator']),0,undefined)
        original=manufactured_power();field,gauge=reporting_gauge(original)
        _,again=reporting_gauge(field)
        check('reporting_gauge_is_normalized',abs(again['input_leading_squared_norm']-1),2e-14,gauge)
        grid=shell_quadrature(.3,1.7)
        r,z=grid['r'],grid['z'];P=(1+r*r+z*z)**-.8
        gp=np.stack((-1.6*r*(1+r*r+z*z)**-1.8,-1.6*z*(1+r*r+z*z)**-1.8),axis=-1)
        base,_=evaluate_set(field,r,z,grid['weights'],P,gp)
        check('primitive_two_implementations',base['cartesian_cylindrical_residual_difference'],4e-15)
        check('reduced_term_decomposition',max(base['q_term_sum_difference'],base['eta_term_sum_difference']),4e-14)
        for L in [.21,2.3]:
            scaled,_=evaluate_set(field.dilate(L),L*r,L*z,L**3*grid['weights'],L**2*P,L*gp)
            errors=[abs(scaled['equations'][e]['rho']/base['equations'][e]['rho']-1) for e in ['M_r','M_theta','M_z','q','eta']]
            check(f'registered_ratio_covariance_{L}',max(errors),3e-13)
        rows=[{'shell_index':0,'set':'shell_gauss','metrics':base}]
        result=annotate_and_aggregate(rows)
        check('manufactured_non_solution_fails_A1',float(result['A1_measured_pass']),0,result)
    except Exception as exc:
        import traceback;traceback.print_exc();exception=repr(exc)
    paths=[Path(__file__)]+[ROOT/'src'/n for n in ['independent_fields.py','independent_geometry.py','independent_registered_metrics.py']]
    record={'recorded_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'elapsed_seconds':time.time()-start,
            'checks':checks,'exception':exception,'source_sha256':{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths},
            'all_passed':exception is None and all(c['passed'] for c in checks)}
    (ROOT/'results/registered_metric_tests.json').write_text(json.dumps(record,indent=2,allow_nan=False)+'\n')
    print(json.dumps({'all_passed':record['all_passed'],'checks':len(checks),'elapsed_seconds':record['elapsed_seconds']}))
    raise SystemExit(0 if record['all_passed'] else 1)
if __name__=='__main__':main()
