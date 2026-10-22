"""Separate Cartesian inverse, finite differences and high-precision jet checks."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,time
import numpy as np
import mpmath as mp
from shifted_power_flow import ShiftedPowerFlow
from cartesian_inverse import CartesianInverse,InverseSettings
from finite_difference import derivative,mixed

start=time.monotonic();out={'started_utc':datetime.now(timezone.utc).isoformat(),'scope':'Manufactured forcing, not full B2; proof precedes code','sources':{p:hashlib.sha256(Path('code_independent',p).read_bytes()).hexdigest() for p in ('shifted_power_flow.py','cartesian_inverse.py','test_shifted_power.py')},'runs':[]}
dest=Path('verification/shifted_power_manufacture.json')
for beta in (2.5,3.,4.,6.):
 f=ShiftedPowerFlow(beta);L=f.L
 pts=L*np.array([[.13,.1],[.7,-.4],[1.2,1.7],[-.63,.9],[0.,-.3],[0.,1.5]])
 row={'beta':beta,'parameters':vars(f),'fd':[],'inverse':[]}
 for relh in (.004,.002,.001):
  hh=relh*L
  E=-derivative(f.psi,pts,0,hh,order=2)-derivative(f.psi,pts,1,hh,order=2)-f.external_omega(*pts.T)
  ux=-derivative(f.psi,pts,1,hh);uy=derivative(f.psi,pts,0,hh)
  V=f.velocity(pts)
  row['fd'].append({'relative_step':relh,'elliptic_max':float(max(abs(E))),'velocity_max':float(max(abs(np.column_stack((ux,uy))-V).ravel())),'center_c':float(mixed(f.psi,[[0,0]],hh)[0]),'q0':float(derivative(f.external_omega,[[0,0]],0,hh)[0]),'qprime0':float(mixed(f.external_omega,[[0,0]],hh)[0])})
 # Broad deterministic point cloud checks the algebraic norm identity; the proof gives the uniform bound.
 rng=np.random.default_rng(711);pp=L*rng.normal(size=(600,2))*np.geomspace(1e-4,1e4,600)[:,None]
 err=[];mins=[]
 for x,y in pp:
  u,W,J,DW=f.field([x,y]);z=y-f.h;ss=x*x+z*z;S=L*L+ss;e=1-f.p
  rhs=(2*f.Bamp*f.p)**2*S**(2*f.p-2)*ss*(1-x*x*(2*e/S-e*e*ss/S**2))
  eig=np.linalg.eigvalsh((J+J.T)/2);err.append(abs(eig[-1]**2-rhs));mins.append(np.linalg.eigvalsh((DW+DW.T)/2)[0])
 row['symmetric_gradient']={'identity_max_abs':float(max(err)),'sampled_min_eigenvalue_DW':float(min(mins)),'analytic_lower_bound':f.lam}
 for radius in (4*L,8*L,16*L):
  for n in (16,32,48):
   op=CartesianInverse(f.external_omega,InverseSettings(radius=radius,core_radial_order=16,core_angular_order=n,exterior_radial_order=n,exterior_angular_order=n,decay_power=1/beta))
   value=op.relative(pts);without=op.relative(pts,include_exterior=False)
   row['inverse'].append({'R':radius,'n':n,'max_error':float(np.max(abs(value-f.velocity(pts)))),'without_exterior_max_error':float(np.max(abs(without-f.velocity(pts))))})
 row['exact_residual_xy']=(2*beta+1)*f.external_qprime0();out['runs'].append(row);dest.write_text(json.dumps(out,indent=2)+'\n');print('beta',beta,'inverse',row['inverse'][-1],'residual_xy',row['exact_residual_xy'],flush=True)
mp.mp.dps=65
beta=mp.mpf(4);p=(beta-1)/(2*beta);c=1+beta/2;L=3*c*mp.sqrt(beta)/4;h=mp.sqrt(beta)*L;B=c/(2*p*h*(L*L+h*h)**(p-1))
q=lambda y:4*B*p*(L*L+(y-h)**2)**(p-2)*(2*L*L+(p+1)*(y-h)**2)
b=lambda y:beta*y+B*((L*L+h*h)**p-(L*L+(y-h)**2)**p)
out['high_precision_beta4']={'q0':str(q(0)),'bprime':str(mp.diff(b,0)),'bsecond':str(mp.diff(b,0,2)),'residual_xy':str((2*beta+1)*mp.diff(q,0)),'error_from_17_over_15':str((2*beta+1)*mp.diff(q,0)-mp.mpf(17)/15)}
out.update(ended_utc=datetime.now(timezone.utc).isoformat(),elapsed_seconds=time.monotonic()-start);dest.write_text(json.dumps(out,indent=2)+'\n');print('COMPLETE',out['elapsed_seconds'],flush=True)
