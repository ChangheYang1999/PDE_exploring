"""Measure the hidden-annulus defect and independently check the full inverse."""
from pathlib import Path
import json,time
from datetime import datetime,timezone
import numpy as np
from cutoff_polynomial import CutoffPolynomial
from finite_difference import cartesian_residuals,desingularized_residuals
from cartesian_inverse import CartesianInverse,InverseSettings

start=time.monotonic()
rows=[]
for R in (8.,16.,32.):
    profile=CutoffPolynomial(R)
    angle=2*np.pi*(np.arange(37)+.31)/37
    radii=R*np.r_[0.,.02,.1,.4,.7,.9,1.03,1.1,1.25,1.5,1.75,1.9,2.1,2.5]
    p=np.column_stack(((radii[:,None]*np.cos(angle)).ravel(),(radii[:,None]*np.sin(angle)).ravel()))
    p=np.vstack((p,np.column_stack((np.zeros(2*len(radii)),np.r_[radii,-radii])),np.column_stack((np.r_[radii,-radii],np.zeros(2*len(radii))))))
    r=np.linalg.norm(p,axis=1)
    steps=[]
    for h in (R*.003,R*.0015,R*.00075):
        v=lambda q:profile.velocity(q,relative=True)
        raw=cartesian_residuals(profile.theta,profile.omega,profile.psi,v,p,profile.beta,h)
        div=desingularized_residuals(profile.theta,profile.omega,profile.psi,v,p,profile.beta,h)
        quantities=raw|div
        regions={}
        for name,mask in [('core',r<.95*R),('transition',(r>R)&(r<2*R)),('outside',r>2.01*R)]:
            regions[name]={k:float(np.max(np.abs(quantities[k][mask]))) for k in ['R_Omega','R_Theta','E','normalized_Omega','normalized_Theta','R_F','R_G','R_H','normalized_F','normalized_G']}
        steps.append({'step':h,'regions':regions})
    ip=np.array([[0.,0.],[.4,-.2],[.2*R,.1*R]])
    expected=profile.velocity(ip,relative=True)
    inverses=[]
    for order in (16,32,64):
        inv=CartesianInverse(profile.omega,InverseSettings(radius=2.25*R,core_radial_order=order,core_angular_order=2*order,exterior_radial_order=8,exterior_angular_order=8))
        v=inv.relative(ip)
        center=inv.square_velocity([0.,0.])
        inverses.append({'order':order,'core_radius':2.25*R,'relative_velocity_max_error':float(np.max(np.abs(v-expected))),'center_velocity':center.tolist(),'center_velocity_max_error':float(np.max(np.abs(center-[0.,profile.v0])))})
    row={'cutoff_radius':R,'beta':profile.beta,'a0':profile.a0,'c':profile.c,'b0':profile.b,'v0':profile.v0,'steps':steps,'inverse':inverses}
    rows.append(row)
    result={'utc':datetime.now(timezone.utc).isoformat(),'run_status':'RUNNING','rows':rows,'meaning':'manufactured adversarial counterexample, not a candidate','elapsed_seconds':time.monotonic()-start}
    Path('verification/cutoff_polynomial_trap.json').write_text(json.dumps(result,indent=2)+'\n')
    print('R',R,'core',steps[-1]['regions']['core'],'transition',steps[-1]['regions']['transition'],'inverse',inverses[-1],flush=True)
result['run_status']='COMPLETE';result['elapsed_seconds']=time.monotonic()-start
Path('verification/cutoff_polynomial_trap.json').write_text(json.dumps(result,indent=2)+'\n')
