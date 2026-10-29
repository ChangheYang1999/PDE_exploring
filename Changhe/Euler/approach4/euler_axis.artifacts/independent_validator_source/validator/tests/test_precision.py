#!/usr/bin/env python3
from pathlib import Path
import datetime,hashlib,json,time
import numpy as np
from independent_fields import manufactured_gaussian,manufactured_power,ScalarExpansion,PotentialField
from independent_precision import compare_precision
from independent_pressure import DirectNewtonPressure,GreenPoisson
ROOT=Path(__file__).resolve().parents[1]
checks=[]
def check(name,error,tolerance,detail=None):
    row={'name':name,'error':float(error),'tolerance':float(tolerance),'passed':bool(np.isfinite(error) and error<=tolerance)}
    if detail is not None:row['detail']=detail
    checks.append(row);print(json.dumps(row),flush=True)

def main():
    start=time.time();exception=None
    try:
        for k,field in enumerate([manufactured_gaussian(),manufactured_power(.505),manufactured_power(.74)]):
            rows=compare_precision(field,[[0.,0.,0.],[0.,0.,.7],[.41,-.23,.17],[31.,-17.,29.]],dps=70)
            for i,row in enumerate(rows):
                err=max(v['max_abs_error']/(1+v['reference_scale']) for v in row['defects'].values())
                check(f'mpmath_field{k}_point{i}',err,3e-14,row)
        known=ScalarExpansion([(1.,0,0,.6),(.2,0,1,1.1),(-.1,1,0,1.6)])
        def source(r,z):
            s=r*r
            return -(4*known.evaluate(s,z,1,0)+4*s*known.evaluate(s,z,2,0)+known.evaluate(s,z,0,2))
        for r,z in [(0.,0.),(0.,.7),(.4,.3),(1.8,-.9)]:
            expected=np.array([2*r*known.evaluate(r*r,z,1,0),known.evaluate(r*r,z,0,1)])
            histories=[]
            for n in [32,64,96]:
                direct=DirectNewtonPressure(source,decay_power=1.2,nradial=n,nangle=n)
                rows=direct.finite_difference_gradient(r,z)
                errors=[float(np.max(np.abs(np.asarray(row['gradient'])-expected))) for row in rows]
                histories.append({'order':n,'steps':rows,'errors':errors})
            check(f'direct_gradient_{r}_{z}',histories[-1]['errors'][-1],2e-7,histories)
        # Reconstruct actual manufactured stream potentials from their eta,
        # including the slow-decay endpoint of the permitted exponent range.
        for c in [.5,.505,.6,2/3,.74]:
            field=manufactured_power(c)
            inv=GreenPoisson(field.eta,dimension=5,decay_power=field.alpha,lmax=10,nangle=26,nradial=32)
            radii=np.array([0.,.04,.5,2.,16.,128.]);mu=np.array([-1.,-.73,0.,.21,1.])
            p,g=inv.on_spheres(radii,mu)
            r=radii[:,None]*np.sqrt(1-mu[None,:]**2);z=radii[:,None]*mu[None,:]
            expected=field.phi.evaluate(r*r,z)
            eg=np.stack((2*r*field.phi.evaluate(r*r,z,1,0),field.phi.evaluate(r*r,z,0,1)),axis=-1)
            check(f'actual_stream_value_c{c}',np.max(np.abs(p-expected)),3e-11)
            check(f'actual_stream_gradient_c{c}',np.max(np.abs(g-eg)),3e-11)
    except Exception as exc:
        import traceback;traceback.print_exc();exception=repr(exc)
    paths=[Path(__file__),ROOT/'src/independent_fields.py',ROOT/'src/independent_pressure.py',ROOT/'src/independent_precision.py']
    record={'recorded_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'elapsed_seconds':time.time()-start,'checks':checks,'exception':exception,
            'source_sha256':{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths},
            'all_passed':exception is None and all(c['passed'] for c in checks)}
    (ROOT/'results/precision_tests.json').write_text(json.dumps(record,indent=2)+'\n')
    print(json.dumps({'all_passed':record['all_passed'],'checks':len(checks),'elapsed_seconds':record['elapsed_seconds']}))
    raise SystemExit(0 if record['all_passed'] else 1)
if __name__=='__main__':main()
