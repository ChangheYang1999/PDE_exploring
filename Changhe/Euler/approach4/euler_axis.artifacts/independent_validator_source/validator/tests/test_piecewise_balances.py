#!/usr/bin/env python3
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,time
import numpy as np
from independent_fields import manufactured_gaussian
from independent_identities import finite_ball_balance
from piecewise_adapter import PiecewiseField
from piecewise_balances import piecewise_ball_balance
ROOT=Path(__file__).resolve().parents[1];ROWS=[]
def check(name,error,tolerance):
    row=dict(name=name,error=float(error),tolerance=float(tolerance),passed=bool(np.isfinite(error) and error<=tolerance))
    ROWS.append(row);print(json.dumps(row),flush=True)
def zero_pressure(r,z):return np.zeros_like(r),np.zeros(np.shape(r)+(2,))
def smooth_pressure(r,z):
    f=.4*np.exp(-r*r-z*z);p=f*(1+.2*z)
    return p,np.stack([-2*r*p,-2*z*p+.2*f],axis=-1)
def main():
    start=time.monotonic();exception=None
    try:
        template=PiecewiseField.load(ROOT/'external_exports/S1_pilot_L0_20261028T2003Z/coeffs.npz')
        for kind in ['axial','rotation','mixed']:
            coeff={k:np.zeros_like(v) for k,v in template.coefficients.items()};A=.7;a=2.
            if kind in ['axial','mixed']:coeff['phi_el0'][0]=A/2
            if kind in ['rotation','mixed']:coeff['q_el0'][0]=A
            field=PiecewiseField(template.metadata,coeff)
            d=piecewise_ball_balance(field,zero_pressure,3.1,nangle=24,nradial=12)
            exactE=(2*np.pi*A*A*a**3/3 if kind in ['axial','mixed'] else 0)+(4*np.pi*A*A*a**5/15 if kind in ['rotation','mixed'] else 0)
            check(kind+'_energy_measure',abs(d['energy']-exactE),2e-11)
            check(kind+'_energy_identity',abs(d['energy_corrected_error']),2e-11)
            check(kind+'_helicity_identity',abs(d['helicity_corrected_error']),2e-11)
            if kind=='axial':check(kind+'_energy_jump',abs(d['energy_interface_jump']+3*field.c_l*exactE),2e-11)
            check(kind+'_jump_is_nonzero',0 if abs(d['energy_interface_jump'])>1 else 1,0)
        field=manufactured_gaussian()
        for R in [.4,1.7,4.3]:
            d=piecewise_ball_balance(field,smooth_pressure,R,nangle=40,nradial=28)
            ref=finite_ball_balance(field,smooth_pressure,R,nangle=40,nradial=28,residual_integrals=True)
            check(f'smooth_energy_{R}',abs(d['energy_corrected_error']),2e-10)
            check(f'smooth_helicity_{R}',abs(d['helicity_corrected_error']),2e-10)
            check(f'smooth_existing_comparison_{R}',max(abs(d[k]-ref[k]) for k in ['energy','helicity','energy_flux','helicity_flux','energy_residual_work','helicity_residual_work']),2e-11)
        try:piecewise_ball_balance(PiecewiseField(template.metadata,coeff),zero_pressure,2.)
        except ValueError:check('interface_radius_rejected',0,0)
        else:check('interface_radius_rejected',1,0)
    except Exception as exc:
        import traceback;traceback.print_exc();exception=repr(exc)
    files=[Path(__file__),ROOT/'src/piecewise_balances.py',ROOT.parent/'research/interface_balances/PROOF.md']
    out=dict(recorded_utc=datetime.now(timezone.utc).isoformat(),elapsed_seconds=time.monotonic()-start,checks=ROWS,exception=exception,
             all_passed=exception is None and all(x['passed'] for x in ROWS),source_sha256={str(p.relative_to(ROOT.parent)):hashlib.sha256(p.read_bytes()).hexdigest() for p in files})
    (ROOT/'results/piecewise_balances_tests.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:out[k] for k in ['all_passed','elapsed_seconds','exception']}));raise SystemExit(0 if out['all_passed'] else 1)
if __name__=='__main__':main()
