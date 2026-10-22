"""Independent Cartesian-inverse and FD checks of packet94's annular source.
No numerics-lane code is imported. Proof94 preceded this checker.
"""
from pathlib import Path
from datetime import datetime,timezone
import json,time,hashlib
import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.integrate import quad
from cartesian_inverse import CartesianInverse,InverseSettings
from finite_difference import stencil


def bump(t):
 t=np.asarray(t);z=(t-1)*(2-t);out=np.zeros_like(t,dtype=float)
 np.exp(4-np.divide(1,z,out=np.full_like(z,np.inf),where=z>0),out=out,where=z>0)
 return out
I0,e0=quad(lambda t:float(bump(t)),1,2,epsabs=1e-13,epsrel=1e-13)
I2,e2=quad(lambda t:t*t*float(bump(t)),1,2,epsabs=1e-13,epsrel=1e-13)
gn,gw=leggauss(96)

def moments(z):
 z=np.asarray(z);J0=np.zeros_like(z);J2=np.zeros_like(z);J0[z>=2]=I0;J2[z>=2]=I2
 mid=(z>1)&(z<2)
 if np.any(mid):
  half=(z[mid]-1)/2;t=1+half[:,None]*(gn+1)
  values=bump(t);J0[mid]=half*(values@gw);J2[mid]=half*((values*t*t)@gw)
 return J0,J2

def source(x,y,R,D):
 x,y=np.broadcast_arrays(x,y);r=np.hypot(x,y)
 return -2*D/(R*I0)*bump(r/R)*np.divide(x,r,out=np.zeros_like(r),where=r>0)

def vel(points,R,D):
 points=np.atleast_2d(points);x,y=points.T;r=np.hypot(x,y);z=r/R
 J0,J2=moments(z);factor=np.divide(D*J2,I0*z*z,out=np.zeros_like(z),where=z>0)
 c=np.divide(x,r,out=np.zeros_like(r),where=r>0);sn=np.divide(y,r,out=np.zeros_like(r),where=r>0)
 return np.column_stack((-2*factor*c*sn,D*J0/I0+factor*(c*c-sn*sn)))

BETA=2.5;s=1/BETA;m=1-2*s;power=(1-s)/2

def base_omega(x,y):
 q=x*x+y*y
 return 4*power*x*(1+q)**(power-2)*(2+(power+1)*q)

def base_theta(x,y):return x*x*(1+x*x+y*y)**(-.5-s)

def base_velocity(points):
 x,y=points.T;q=x*x+y*y
 return np.column_stack((2*power*x*y*(1+q)**(power-1),-np.expm1(power*np.log1p(q))-2*power*x*x*(1+q)**(power-1)))

nodes,weights=stencil()
def derivative(fun,points,axis,relstep):
 steps=relstep*np.maximum(1,np.linalg.norm(points,axis=1));p=points[:,None,:]+np.zeros((1,len(nodes),2));p[:,:,axis]+=steps[:,None]*nodes
 return fun(p[:,:,0],p[:,:,1])@weights/steps

def gradient(fun,p,step):return np.column_stack([derivative(fun,p,i,step) for i in [0,1]])

start=time.monotonic();root=Path('research/94_annular_control_of_inverse_constant/verification')
out={'started_utc':datetime.now(timezone.utc).isoformat(),'scope':'Manufactured inverse-source and weighted-map tests, not a B2 profile or interval bound.','beta':BETA,'bump_moments':{'I0':I0,'I2':I2,'quadrature_estimates':[e0,e2]},'cartesian_inverse':[],'weighted_and_residual':[],'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
points=np.array([[0.,0.],[.13,.41],[.6,-.4],[1.13,.47],[1.6,-.8],[2.4,.2],[4.1,-1.2]])
for R in [1.,8.,64.]:
 D=.35;physical=R*points;exact=vel(physical,R,D)
 for order in [32,64,128]:
  inv=CartesianInverse(lambda x,y:source(x,y,R,D),InverseSettings(radius=6*R,core_radial_order=order,core_angular_order=order,exterior_radial_order=8,exterior_angular_order=8))
  calc=inv.relative(physical);ordinary0=inv.square_velocity([0.,0.]);row={'R':R,'D':D,'order':order,'max_error':float(np.max(abs(calc-exact))),'core_error':float(np.max(abs(calc[:3]))),'ordinary_velocity_at0':ordinary0.tolist(),'ordinary0_error':float(np.max(abs(ordinary0-np.array([0.,-D]))))};out['cartesian_inverse'].append(row);print('inverse',row,flush=True)
phi=2*np.pi*(np.arange(72)+.317)/72;e=np.column_stack((np.cos(phi),np.sin(phi)))
for R in [4.,16.,64.,256.,1024.]:
 D=.35;r=R*np.r_[.7,np.linspace(1.01,1.99,39),np.geomspace(2,1e3,60)];p=(r[:,None,None]*e[None,:,:]).reshape(-1,2);rr=np.linalg.norm(p,axis=1);x,y=p.T
 du=vel(p,R,D);dom=source(x,y,R,D);bt=base_theta(x,y);bo=base_omega(x,y);bv=base_velocity(p)
 rec={'R':R,'D':D,'source_weighted_j0':float(np.max((1+rr)**s*abs(dom))),'velocity_weighted_j0':float(np.max((1+rr)**(s-1)*np.linalg.norm(du,axis=1))),'tail_constant_difference':D,'grid_points':len(p),'FD':[],'positive_right_min_ratio':float(np.min((bo+dom)[x>0]/bo[x>0]))}
 for step in [2e-5,1e-5]:
  gt=gradient(base_theta,p,step);go=gradient(base_omega,p,step);gnew=gradient(lambda x,y:base_omega(x,y)+source(x,y,R,D),p,step);gd=gradient(lambda x,y:source(x,y,R,D),p,step)
  W=BETA*p+bv;Wnew=W+du
  oldT=np.sum(W*gt,axis=1)-(BETA-2)*bt;newT=np.sum(Wnew*gt,axis=1)-(BETA-2)*bt
  oldO=np.sum(W*go,axis=1)+bo-gt[:,0];newO=np.sum(Wnew*gnew,axis=1)+bo+dom-gt[:,0]
  predictedT=np.sum(du*gt,axis=1);predictedO=np.sum(W*gd+du*go+du*gd,axis=1)+dom
  rec['FD'].append({'step':step,'weighted_delta_RTheta':float(np.max((1+rr)**(-m)*abs(newT-oldT))),'weighted_delta_ROmega':float(np.max((1+rr)**s*abs(newO-oldO))),'identity_T_error':float(np.max(abs(newT-oldT-predictedT))),'identity_O_error':float(np.max(abs(newO-oldO-predictedO))),'source_weighted_j1':float(np.max((1+rr)**(s+1)*np.linalg.norm(gd,axis=1)))})
 out['weighted_and_residual'].append(rec);print('weighted',R,rec['source_weighted_j0'],rec['velocity_weighted_j0'],rec['FD'][-1]['weighted_delta_RTheta'],rec['FD'][-1]['weighted_delta_ROmega'],flush=True)
assert max(a['max_error'] for a in out['cartesian_inverse'] if a['order']==128)<1e-6
assert all(a['positive_right_min_ratio']>0 for a in out['weighted_and_residual'])
out.update(status='COMPLETE',ended_utc=datetime.now(timezone.utc).isoformat(),elapsed_seconds=time.monotonic()-start)
(root/'manufactured_checks.json').write_text(json.dumps(out,indent=2)+'\n');print('COMPLETE',out['elapsed_seconds'],flush=True)
