"""Canonical inverse regression of a smooth zero-slope deflation counterexample."""
from pathlib import Path
from datetime import datetime,timezone
import json
import numpy as np
from q_checkpoint_reader import QCheckpoint
from direct_inverse import DirectInverse,Quadrature,cartesian_gradient
out=Path('research/deflated_center_counterexample/verification');rows=[]
for ell in [1.5,2.,3.]:
    kap=ell/(ell-1);G=2.;v=-8*(ell-1)/(1+2*kap);u=v+G
    c=object.__new__(QCheckpoint);c.kappa=kap;c.L=1.;c.M=2;c.coeff=[np.array([u/2,u/2]),np.array([v])]
    ell_rows=[]
    for q,(nr,nt,ne,of) in enumerate([(24,128,96,2.),(40,256,144,4.),(64,512,224,8.)]):
        length=2**(-kap);inv=DirectInverse(c.rho,Quadrature(nr,nt,ne,of,length,1/ell,16.,kap))
        hh=length*np.array([.016,.008,.004,.002,.001]);slopes=np.array([inv.velocity(0,h)[1]/h for h in hh])
        extrap=np.polynomial.polynomial.polyfit(hh*hh,slopes,3)[0]
        y=hh[-1];rho=float(c.rho(0.,y));vel=inv.velocity(0.,y);gx,gy=cartesian_gradient(c.rho,0.,y,.0015,0.)
        tx=0.;ty=(ell*y+vel[1])*gy;R=float(ty-rho);nf=float(abs(ty)+abs(rho));nv=float(abs(rho)+abs(y*gy)+abs(vel[1]*gy))
        e3=2**(2*kap)*G
        entry={'ell':ell,'kappa':kap,'level':q,'canonical_c_expected':1-ell,'canonical_c_extrapolated':float(extrap),'center_error':float(abs(extrap-(1-ell))),'a0_exact':0.,'gK_exact':G,'axis_y':y,'rho_over_y3':rho/y**3,'e3_exact':e3,'R_over_y3':R/y**3,'R_Nf':abs(R)/nf,'R_Nv':abs(R)/nv,'Nf_limit':.5,'Nv_limit':2/(4+3*(ell-1))}
        ell_rows.append(entry);rows.append(entry)
        (out/'checks.json').write_text(json.dumps({'utc':datetime.now(timezone.utc).isoformat(),'rows':rows},indent=2)+'\n')
    assert ell_rows[-1]['center_error']<5e-10
    assert abs(ell_rows[-1]['R_Nf']-.5)<1e-5
    assert abs(ell_rows[-1]['R_Nv']-ell_rows[-1]['Nv_limit'])<1e-5
result={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS','rows':rows,'scope':'Independent full-plane inverse and Cartesian differentiation for an explicit canonical non-profile with zero slope. The analytic counterexample and limits are proved separately.'}
(out/'checks.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result),flush=True)
