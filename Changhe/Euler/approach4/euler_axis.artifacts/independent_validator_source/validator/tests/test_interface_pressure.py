#!/usr/bin/env python3
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,time
import numpy as np
from scipy.special import eval_legendre
from piecewise_adapter import PiecewiseField
from piecewise_pressure import InterfaceStressPressure,InterfaceGreenPoisson,DirectInterfaceNewton
ROOT=Path(__file__).resolve().parents[1];ROWS=[]
def check(name,error,tolerance,detail=None):
    row=dict(name=name,error=float(error),tolerance=float(tolerance),passed=bool(np.isfinite(error) and error<=tolerance))
    if detail is not None:row['detail']=detail
    ROWS.append(row);print(json.dumps(row),flush=True)
def main():
    start=time.monotonic();exception=None
    try:
        template=PiecewiseField.load(ROOT/'external_exports/S1_pilot_L0_20261028T2003Z/coeffs.npz')
        for kind in ['axial','rotation']:
            coefficients={k:np.zeros_like(v) for k,v in template.coefficients.items()};A=.7;a=2.
            coefficients['phi_el0' if kind=='axial' else 'q_el0'][0]=A/2 if kind=='axial' else A
            field=PiecewiseField(template.metadata,coefficients)
            pressure=InterfaceStressPressure(field,decay_power=1.,lmax=8,nangle=24,nradial=20,scale=2.)
            R=np.array([0.,.3,1.1,1.9,2.1,3.7,8.,11.]);mu=np.array([-1.,-.47,0.,.21,1.]);RR=R[:,None];MM=mu[None,:]
            P,G=pressure.on_spheres(R,mu)
            if kind=='axial':reference=np.where(RR<a,-A*A/3,2*A*A/3*(a/np.maximum(RR,1e-9))**3*eval_legendre(2,MM))
            else:reference=np.where(RR<a,-A*A*a*a/3+A*A*RR*RR/3-2*A*A*RR*RR/15*eval_legendre(2,MM),-2*A*A*a**5/(15*np.maximum(RR,1e-9)**3)*eval_legendre(2,MM))
            check(kind+'_stress_pressure',np.max(abs(P-reference)),2e-11)
            check(kind+'_outside_monopole',abs(pressure.radial(8.)[0][0]),2e-12)
            eps=1e-7;inside=pressure.radial(a-eps)[0];outside=pressure.radial(a+eps)[0]
            J=pressure.surfaces[0]['J'];check(kind+'_pressure_jump',np.max(abs(outside-inside+J)),3e-7)
            for point in [(0.,0.),(.3,.7),(1.7,.1),(.3,2.8)]:
                r,z=point;h=1e-5
                value,grad=pressure.evaluate(r,z);fd=[]
                for j in range(2):
                    def f(t):return float(pressure.evaluate(abs(r+t) if j==0 else r,z+t if j==1 else z)[0])
                    fd.append((-f(2*h)+8*f(h)-8*f(-h)+f(-2*h))/(12*h))
                check(kind+'_gradient_'+str(point),np.max(abs(grad-fd)),2e-9)
            if kind=='rotation':
                direct=DirectInterfaceNewton(field.source,interfaces=field.interfaces,decay_power=1.,nradial=64,nangle=96,scale=2.)
                for r,z in [(0.,0.),(0.,.7),(.3,.7),(3.,1.)]:
                    Rpoint=np.hypot(r,z);expected=-A*A*(a*a-Rpoint*Rpoint/3) if Rpoint<a else -2*A*A*a**3/(3*Rpoint)
                    value=direct.evaluate(r,z)
                    check('rotation_direct_bulk_'+str((r,z)),abs(value-expected),3e-7)
    except Exception as exc:
        import traceback;traceback.print_exc();exception=repr(exc)
    files=[Path(__file__),ROOT/'src/piecewise_pressure.py',ROOT/'src/piecewise_adapter.py',ROOT.parent/'research/interface_pressure/PROOF.md']
    out=dict(recorded_utc=datetime.now(timezone.utc).isoformat(),elapsed_seconds=time.monotonic()-start,checks=ROWS,exception=exception,
             all_passed=exception is None and all(x['passed'] for x in ROWS),source_sha256={str(p.relative_to(ROOT.parent)):hashlib.sha256(p.read_bytes()).hexdigest() for p in files},
             scope='Two exactly evaluable discontinuous fields, neither an Euler profile. Tests include both a normal jump and a divergence-free vortex sheet.')
    (ROOT/'results/interface_pressure_tests.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:out[k] for k in ['all_passed','elapsed_seconds','exception']}));raise SystemExit(0 if out['all_passed'] else 1)
if __name__=='__main__':main()
