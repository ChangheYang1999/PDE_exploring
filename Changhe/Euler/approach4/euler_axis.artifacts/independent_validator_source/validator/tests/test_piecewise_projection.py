#!/usr/bin/env python3
"""Independent values and differentiated projections of the retained failed pilot."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,time
import numpy as np
from piecewise_adapter import PiecewiseField
from piecewise_projection import PiecewiseValues
ROOT=Path(__file__).resolve().parents[1]
EXPORT=ROOT/'external_exports/S1_pilot_L0_20261028T2003Z/coeffs.npz'
ROWS=[]
def check(name,error,tolerance,detail=None):
    row=dict(name=name,error=float(error),tolerance=tolerance,passed=bool(np.isfinite(error) and error<=tolerance))
    if detail is not None: row['detail']=detail
    ROWS.append(row); print(json.dumps(row),flush=True)

def main():
    start=time.monotonic();exception=None
    try:
        field=PiecewiseField.load(EXPORT);values=PiecewiseValues.load(EXPORT)
        rng=np.random.default_rng(741305)
        for element,(lo,hi) in enumerate([(0.,2.),(2.,10.),(10.,1000.)]):
            R=np.r_[lo,hi,rng.uniform(max(lo,.001),hi,61)]
            mu=np.r_[1.,-1.,rng.uniform(-1,1,61)]
            s=R**2*(1-mu**2);z=R*mu
            ref=field.jets(s,z,0,element=element)
            for key in ['phi','q']:
                got=values.evaluate(key,s,z,element=element)
                error=np.max(abs(got-ref[key][0,0]))/(1+np.max(abs(got)))
                check(f'values_element{element}_{key}',error,3e-13)
        for lo,hi,element in [(.5,1.,0),(1.,2.,0),(2.,4.,1),(8.,10.,1),(10.,20.,2),(80.,160.,2)]:
            projected=values.project(lo,hi,element=element)
            R=np.array([lo,(lo+hi)*.5,hi])[:,None]
            mu=np.array([-1.,-.999,-.43,.0,.23,.999,1.])[None,:]
            s=R**2*(1-mu**2);z=R*mu
            ref=field.jets(s,z,3,element=element)
            for key,scalar in [('phi',projected.phi),('q',projected.q)]:
                errors={}
                for ab,expected in ref[key].items():
                    got=scalar.evaluate(s,z,*ab)
                    errors[str(ab)]=float(np.max(abs(got-expected))/(1+np.max(abs(expected))))
                check(f'projected_jets_{lo}_{key}',max(errors.values()),1e-7,errors)
            # Interior points avoid selecting the adjacent piece at a shared endpoint.
            R=np.array([1.01*lo,.5*(lo+hi),.99*hi])[:,None]
            r=R*np.sqrt(1-mu**2);z=R*mu
            p=projected.reduced(r,z);q=field.reduced(r,z)
            for key in ['q','eta']:
                error=np.max(abs(p[key]-q[key]))/(np.max(abs(q[key]))+1e-300)
                check(f'projected_residual_{lo}_{key}',error,1e-6)
        scaled=PiecewiseValues.load(EXPORT,dilation=.073)
        scaled_ref=field.dilate(.073)
        r=np.array([0.,.015,.22,1.8]);z=np.array([0.,-.02,.7,-4.])
        for key in ['phi','q']:
            expected=getattr(scaled_ref,key).evaluate(r*r,z)
            check('dilated_values_'+key,np.max(abs(scaled.evaluate(key,r*r,z)-expected))/(1+np.max(abs(expected))),3e-13)
    except Exception as exc:
        import traceback;traceback.print_exc();exception=repr(exc)
    paths=[Path(__file__),ROOT/'src/piecewise_projection.py',ROOT/'src/independent_projection.py',ROOT/'src/piecewise_adapter.py',EXPORT]
    out=dict(recorded_utc=datetime.now(timezone.utc).isoformat(),elapsed_seconds=time.monotonic()-start,
        checks=ROWS,exception=exception,all_passed=exception is None and all(row['passed'] for row in ROWS),
        source_sha256={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths},
        scope='Implementation check using a failed pilot. No candidate acceptance is asserted.')
    (ROOT/'results/piecewise_projection_tests.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:out[k] for k in ['all_passed','elapsed_seconds','exception']}))
    raise SystemExit(0 if out['all_passed'] else 1)
if __name__=='__main__':main()
