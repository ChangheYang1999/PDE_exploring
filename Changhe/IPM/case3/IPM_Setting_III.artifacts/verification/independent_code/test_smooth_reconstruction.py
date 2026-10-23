"""Meaningful consistency checks for the independent smooth state evaluator."""
from pathlib import Path
from datetime import datetime,timezone
import json
import numpy as np
from smooth_basis import SmoothBasis,SmoothDensity
from evaluate_smooth_state import ReconstructedSmooth
from direct_inverse import cartesian_gradient
out=Path('research/smooth_representation/verification');out.mkdir(parents=True,exist_ok=True)
rng=np.random.default_rng(92618);cases=[]
for p,L in [(1/3,1.),(2/3,.3),(.96,3.)]:
    b=SmoothBasis(8,5,p,L);coeff=rng.normal(size=(b.M,b.N+1))
    coeff/=((1+np.arange(b.M))[:,None]**3*(1+np.arange(b.N+1))[None,:]**3)
    path=out/'reconstruction_test_input.npz'
    np.savez_compressed(path,radial=b.N,angular=b.M,exponent=p,length=L,cl=1/p,coefficients=coeff.reshape(-1))
    old=SmoothDensity(b,coeff.reshape(-1));new=ReconstructedSmooth(path)
    rr=L*np.logspace(-8,8,90);theta=np.linspace(-2.9,3.01,90)
    x=rr*np.cos(theta);y=rr*np.sin(theta)
    ov=old.rho(x,y);nv=new.rho(x,y);scale=np.maximum(1.,abs(ov))
    rho_error=float(np.max(abs(ov-nv)/scale));assert rho_error<2e-13,(p,rho_error)
    gx,gy=old.gradient(x,y);fx,fy=cartesian_gradient(new.rho,x,y,.0015,0.)
    gradscale=np.maximum(1.,np.maximum(abs(gx),abs(gy)))
    gradient_error=float(np.max(np.maximum(abs(gx-fx),abs(gy-fy))/gradscale));assert gradient_error<3e-10,(p,gradient_error)
    m=new.center_and_tail();c=float(b.center_strain()@coeff.reshape(-1));h=float(b.quartic_stream_difference()@coeff.reshape(-1))
    cerr=abs(m['adaptive_logradius_center'][-1]['c']-c);herr=abs(m['adaptive_logradius_center'][-1]['H']-h)
    assert cerr<1e-10*max(1,abs(c)) and herr<1e-10*max(1,abs(h)),(p,cerr,herr)
    assert np.max(abs(new.rho(-x,y)-nv))==0 and np.max(abs(new.rho(x,-y)+nv))==0
    cases.append({'p':p,'L':L,'reconstruction_error_scaled':rho_error,'Cartesian_FD8_gradient_error_scaled':gradient_error,'adaptive_c_vs_formula':cerr,'adaptive_H_vs_formula':herr,'exact_computed_density_parities':True})
path.unlink()
result={'utc':datetime.now(timezone.utc).isoformat(),'cases':cases,'scope':'Checks the separate scalar reconstruction, Cartesian finite differences, and adaptive full-radius moments. Does not test IPM existence.'}
(out/'independent_reconstruction.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
