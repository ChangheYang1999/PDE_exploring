#!/usr/bin/env python3
"""Exact rational manufactured potentials versus the beta-integral inverse."""
from pathlib import Path
import datetime,time
import mpmath as mp
from independent_fields import ScalarExpansion
from eta_green_basis import EtaGreenField
from green_precision import reference_potential_jet,compare_green_point
from independent_artifacts import atomic_json,sha256
ROOT=Path(__file__).resolve().parents[1]

def main():
    start=time.perf_counter();rows=[];exception=None
    def check(name,error,tolerance):
        error=float(error);row={'name':name,'error':error,'tolerance':tolerance,'passed':error<=tolerance};rows.append(row)
        if not row['passed']:raise AssertionError(row)
    try:
        with mp.workdps(70):
            for ell,beta,solid in [(0,1,[(0,0,1)]),(1,2,[(0,1,1)]),(3,3,[(0,3,10),(1,1,-7.5)])]:
                terms=[]
                for i,j,a in solid:
                    terms.extend([(2*beta*(2*ell+5)*a,i,j,beta+1),(-4*beta*(beta+1)*a,i+1,j,beta+2),(-4*beta*(beta+1)*a,i,j+2,beta+2)])
                source=ScalarExpansion(terms);field=EtaGreenField(source,ScalarExpansion([(1.,0,0,2.)]),.74)
                exact=lambda s,z:sum(mp.mpf(str(a))*s**i*z**j for i,j,a in solid)/(1+s+z*z)**beta
                for rr,zz in [(.03,.08),(.5,.7),(4.,-2.),(30.,20.)]:
                    r,z=mp.mpf(str(rr)),mp.mpf(str(zz));s=r*r;p=reference_potential_jet(source,s,z)
                    for key,value in p.items():
                        expected=mp.diff(exact,(s,z),key)
                        check(f'exact potential ell{ell} r{rr} z{zz} jet{key}',abs(value-expected),1e-56)
                    result=compare_green_point(field,rr,zz,70)
                    for key,errors in result['errors'].items():
                        check(f'float comparison ell{ell} r{rr} z{zz} {key}',errors['absolute_error']/(1+errors['reference_scale']),2e-11)
    except Exception as error:
        import traceback;traceback.print_exc();exception=repr(error)
    result={'all_passed':exception is None,'case_count':len(rows),'rows':rows,'exception':exception,
            'completed_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'wall_seconds':time.perf_counter()-start,
            'source_sha256':{name:sha256(ROOT/name) for name in ['src/green_precision.py','tests/test_green_precision.py']}}
    atomic_json(ROOT/'results/green_precision_tests.json',result);print(result['all_passed'],len(rows),result['wall_seconds'],flush=True)
    raise SystemExit(0 if result['all_passed'] else 1)
if __name__=='__main__':main()
