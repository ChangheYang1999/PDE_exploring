"""Meaningful checks of the independent basis and its kernel matrix assembly."""
import json,time
from pathlib import Path
from datetime import datetime,timezone
import numpy as np
from smooth_basis import SmoothBasis,SmoothDensity
from kernel_basis import KernelBasis
from direct_inverse import DirectInverse,Quadrature,cartesian_gradient
from scipy.special import roots_legendre

rng=np.random.default_rng(238912)
b=SmoothBasis(8,6,1/3,1.)
z=rng.normal(size=b.size)/np.tile(1+np.arange(b.N+1)**3,b.M)/np.repeat(1+np.arange(b.M)**2,b.N+1)
d=SmoothDensity(b,z)
pts=np.array([[.3,.7],[3.,-2.],[100.,40.],[5.,.003],[0.,0.]])
gx,gy=d.gradient(pts[:,0],pts[:,1]); fx,fy=cartesian_gradient(d.rho,pts[:,0],pts[:,1],.0005,1.)
errgrad=np.max(np.abs(np.column_stack([gx-fx,gy-fy])))
records=[]
for n,a,e in [(16,64,48),(32,128,96),(48,256,144)]:
 conf=Quadrature(n,a,e,4.,1.,b.p,16.,1/(1-b.p))
 kin=KernelBasis(b,conf); din=DirectInverse(d.rho,conf)
 for x,y in pts[:3]:
  start=time.time();mat=kin.velocity_matrix(x,y);u=mat@z;check=din.velocity(x,y)
  records.append({'config':conf.__dict__,'point':[x,y],'matrix_scalar_error':float(np.max(np.abs(u-check))),'U':u.tolist(),'seconds':time.time()-start})
# A separate derivative-free polar moment computes c from density data.
v,wt=roots_legendre(128);v=(v+1)/2;wt=wt/2
th=(np.arange(64)+.5)*2*np.pi/64
# Integrate in logarithmic physical radius and attach small tails explicitly.
terms=[]
for lo in range(-25,26):
 rr=np.exp(lo+v)
 b3=d.polar_density(rr,th)@(2*np.sin(3*th)/len(th))
 terms.append(float(wt@(b3/rr)))
cmoment=-float(b.center_slope()@z)/4+sum(terms)
cexact=float(b.center_strain()@z)
result={'utc':datetime.now(timezone.utc).isoformat(),'basis':b.metadata(),'gradient_max_error':float(errgrad),'strain_explicit':cexact,'strain_log_integral_minus25_to26':cmoment,'strain_difference_including_unintegrated_tail':cmoment-cexact,'matrix_tests':records}
Path('research/smooth_representation/verification/component_tests.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2),flush=True)
if errgrad>1e-7 or max(q['matrix_scalar_error'] for q in records)>1e-8:raise RuntimeError('basis or matrix failed independent cross-check')
