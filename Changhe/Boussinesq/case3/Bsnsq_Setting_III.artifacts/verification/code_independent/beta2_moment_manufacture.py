"""A smooth kinematic manufacture for the beta2 finite-part constant.
It is NOT a Boussinesq profile. All inverse code is the verifier's own.
"""
from pathlib import Path
from datetime import datetime,timezone
import numpy as np,json,time
from numpy.polynomial.legendre import leggauss
from cartesian_inverse import CartesianInverse,InverseSettings
start=time.monotonic();A=2/7;D=-3/5
ac=-5*A/4;b1=-2*D;C=-A;mstar=A-D/2

def fg(q):
 f=A*(np.expm1(.25*np.log1p(q)))+D/2*np.log1p(q)
 fp=A/4*(1+q)**(-.75)+D/2/(1+q)
 fpp=-3*A/16*(1+q)**(-1.75)-D/2/(1+q)**2
 return f,fp,fpp

def omega(x,y):
 q=x*x+y*y;f,fp,fpp=fg(q);return -x*(8*fp+4*q*fpp)

def vel(pts):
 pts=np.asarray(pts);x=pts[:,0];y=pts[:,1];f,fp,_=fg(x*x+y*y)
 return np.column_stack((-2*x*y*fp,f+2*x*x*fp))
rows=[]
for n in [16,32,64]:
 t,w=leggauss(n)
 for R in [4,16,256,4096,65536,1048576]:
  umax=np.log1p(R*R);u=(t+1)*umax/2;q=np.expm1(u)
  f,fp,fpp=fg(q);g=-(8*fp+4*q*fpp)
  mr=float(np.dot(w,g*np.exp(u))*umax/8)
  theta=2*np.pi*(np.arange(128)+.375)/128
  vp=vel(np.column_stack((R*np.cos(theta),R*np.sin(theta))))
  vmean=np.mean(vp,axis=0)
  finitepart=mr-ac*np.sqrt(R)-b1/2*np.log(R)
  rows.append({'n':n,'R':R,'m_R':mr,'circular_mean_error':float(np.max(np.abs(vmean+np.array([0,mr])))),'finitepart':finitepart,'finitepart_error':finitepart-mstar})
pts=np.array([[0,0],[0,1],[1,-2],[-.5,3],[2,0]],float);exact=vel(pts);invrows=[]
for n in [16,32,48]:
 for R in [6,12,24]:
  inv=CartesianInverse(omega,InverseSettings(radius=R,core_radial_order=n,core_angular_order=n,exterior_radial_order=n,exterior_angular_order=n,decay_power=.5))
  val=inv.relative(pts);cut=inv.relative(pts,include_exterior=False)
  invrows.append({'n':n,'core_radius':R,'maximum_abs_error':float(np.max(np.abs(val-exact))),'maximum_without_exterior':float(np.max(np.abs(cut-exact)))})
out={'utc':datetime.now(timezone.utc).isoformat(),'scope':'kinematic inverse/moment test only, not B2','parameters':{'A':A,'D':D,'a_cos':ac,'b1':b1,'exact_C':C,'exact_mstar':mstar},'finite_radius_rows':rows,'fullplane_inverse_rows':invrows,'sample_points':pts.tolist(),'elapsed_seconds':time.monotonic()-start}
Path('research/54_beta2_scattering_identities/verification/moment_manufacture.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'elapsed_seconds':out['elapsed_seconds'],'n64_rows':[r for r in rows if r['n']==64],'inverse':invrows},indent=2))
