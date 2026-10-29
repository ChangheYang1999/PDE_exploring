#!/usr/bin/env python3
"""Surface-jump algebra and independent full-space five-dimensional inversion."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,time
import numpy as np
import sympy as sp
from piecewise_adapter import PiecewiseField
from piecewise_stream import jump_mode_coefficients,ReconstructedStream
ROOT=Path(__file__).resolve().parents[1];ROWS=[]
def check(name,error,tolerance):
    row=dict(name=name,error=float(error),tolerance=float(tolerance),passed=bool(np.isfinite(error) and error<=tolerance))
    ROWS.append(row);print(json.dumps(row),flush=True)
def main():
    start=time.monotonic();exception=None
    try:
        a,j,h=sp.symbols('a j h',nonzero=True)
        for d in (3,5):
            for ell in (0,1,2,5,12):
                inner=-(a*h+(ell+d-2)*j)/(2*ell+d-2)
                outer=(ell*j-a*h)/(2*ell+d-2)
                check(f'exact_value_jump_d{d}_ell{ell}',0 if sp.simplify(outer-inner-j)==0 else 1,0)
                check(f'exact_derivative_jump_d{d}_ell{ell}',0 if sp.simplify((-(ell+d-2)*outer-ell*inner)/a-h)==0 else 1,0)
                ii,oo=jump_mode_coefficients(ell,d,1.7,.23,-.41)
                check(f'implemented_jumps_d{d}_ell{ell}',max(abs(oo-ii-.23),abs((-(ell+d-2)*oo-ell*ii)/1.7+.41)),1e-14)
        template=PiecewiseField.load(ROOT/'external_exports/S1_pilot_L0_20261028T2003Z/coeffs.npz')
        for label,terms in [('constant',[(0,0,.7)]),('mixed_polynomial',[(0,0,.2),(1,0,-.3),(0,1,.04),(2,0,.21),(3,2,.07)])]:
            coefficients={k:np.zeros_like(v) for k,v in template.coefficients.items()}
            labels=template.elements[0]['labels']
            for n,k,A in terms:
                hit=[i for i,p in enumerate(labels) if p==[n,k]]
                assert len(hit)==1
                coefficients['phi_el0'][hit[0]]=A
            field=PiecewiseField(template.metadata,coefficients)
            inverse=ReconstructedStream(field,lmax=12,nangle=32,nradial=24)
            R=np.array([0.,.3,1.1,1.9,2.1,3.7,8.,11.,80.]);mu=np.array([-1.,-.47,0.,.21,1.])
            rr=R[:,None]*np.sqrt(1-mu*mu)[None,:];zz=R[:,None]*mu[None,:]
            jets=field.jets(rr*rr,zz,1);reference=jets['phi'][0,0]
            grad=np.stack([2*rr*jets['phi'][1,0],jets['phi'][0,1]],axis=-1)
            got,gg=inverse.on_spheres(R,mu)
            check(label+'_potential',np.max(abs(got-reference)),2e-11)
            check(label+'_gradient',np.max(abs(gg-grad)),2e-10)
            bulk,_=inverse.bulk.on_spheres(R,mu)
            check(label+'_surface_not_omitted',0 if np.max(abs(bulk-reference))>1e-3 else 1,0)
        # A genuinely smooth decaying global fixture has no interface source.
        from independent_fields import manufactured_gaussian
        field=manufactured_gaussian()
        from independent_pressure import GreenPoisson
        inverse=GreenPoisson(field.eta,dimension=5,decay_power=1.,lmax=12,nangle=32,nradial=32)
        rr=np.array([0.,0.,.3,1.1,4.]);zz=np.array([0.,.8,-.6,.2,1.])
        got,gg=inverse.evaluate(rr,zz);jets=field.phi.jet(rr*rr,zz,1)
        check('smooth_fixture_potential',np.max(abs(got-jets[0,0])),2e-10)
        check('smooth_fixture_gradient',np.max(abs(gg-np.stack([2*rr*jets[1,0],jets[0,1]],axis=-1))),2e-9)
    except Exception as exc:
        import traceback;traceback.print_exc();exception=repr(exc)
    files=[Path(__file__),ROOT/'src/piecewise_stream.py',ROOT/'src/piecewise_pressure.py',ROOT/'src/piecewise_adapter.py',ROOT.parent/'research/interface_stream_inverse/PROOF.md']
    out=dict(recorded_utc=datetime.now(timezone.utc).isoformat(),elapsed_seconds=time.monotonic()-start,checks=ROWS,exception=exception,
             all_passed=exception is None and all(x['passed'] for x in ROWS),source_sha256={str(p.relative_to(ROOT.parent)):hashlib.sha256(p.read_bytes()).hexdigest() for p in files},
             scope='Independent jump algebra and exact discontinuous polynomial fixtures; not an Euler profile test.')
    (ROOT/'results/interface_stream_tests.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:out[k] for k in ['all_passed','elapsed_seconds','exception']}));raise SystemExit(0 if out['all_passed'] else 1)
if __name__=='__main__':main()
