"""Independent manufactured beta2 inverse with leading tail, resonance and constant.
No Boussinesq transport solution is claimed. No fitting-lane imports.
"""
from pathlib import Path
from datetime import datetime,timezone
import json,time,hashlib
import numpy as np
from scipy.integrate import quad
from cartesian_inverse import CartesianInverse,InverseSettings

A=.4;B=1.4;G=2.
def omega(x,y):
 x=np.asarray(x);y=np.asarray(y);s=x*x+y*y
 return -A*x*(2+1.25*s)/(1+s)**1.75+B*x*(s+2)/(1+s)**2+3*G*x*y*(s+2)/(1+s)**2.5

def velocity(points):
 x,y=np.asarray(points).T;s=x*x+y*y
 f=np.expm1(.25*np.log1p(s));fp=.25*(1+s)**(-.75)
 u1=-2*A*x*y*fp+(B/2)*x*y/(1+s)-G*x*((1+s)**(-.5)-y*y*(1+s)**(-1.5))
 u2=A*(f+2*x*x*fp)-(B/4)*np.log1p(s)-(B/2)*x*x/(1+s)+G*y*((1+s)**(-.5)-x*x*(1+s)**(-1.5))
 return np.column_stack((u1,u2))

def asymptotic_without_constant(points):
 points=np.asarray(points);r=np.linalg.norm(points,axis=1);e=points/r[:,None];c=e[:,0];sn=e[:,1]
 # u0 from Psi0=A*x*sqrt(r).
 leading=A*np.sqrt(r)[:,None]*np.column_stack((-.5*c*sn,1+.5*c*c))
 # g=(G/2)sin(2theta)=G*c*sn, g'=G*(c*c-sn*sn).
 gp=G*(c*c-sn*sn);g=G*c*sn;n=np.column_stack((-sn,c))
 angular=-gp[:,None]*e+g[:,None]*n+(B/2)*np.column_stack((c*sn,-c*c))
 return leading+angular+np.column_stack((np.zeros_like(r),-(B/2)*np.log(r)))

def cutoff(r,r0):
 t=(r-r0)/r0
 if t<=0:return 0.
 if t>=1:return 1.
 aa=np.exp(-1/t);bb=np.exp(-1/(1-t));return aa/(aa+bb)

def eta_radial(r,r0):
 if r>1:
  h=r**(-2);v=-1.75*np.log1p(h)
  leading=A*r**(-.5)*(-1.25*np.expm1(v)-2*h*np.exp(v))
 else:
  leading=-A*r*(2+1.25*r*r)/(1+r*r)**1.75+1.25*A*r**(-.5)
 if r>=2*r0:
  second=-B/(r*(1+r*r)**2)
 else:
  second=B*r*(r*r+2)/(1+r*r)**2-B*cutoff(r,r0)/r
 return leading+second

start=time.monotonic();out={'started_utc':datetime.now(timezone.utc).isoformat(),'scope':'Manufactured inverse only, not a B2 profile','parameters':{'A':A,'B':B,'G':G},'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'runs':[],'constant_cutoffs':[],'asymptotic':[]}
points=np.array([[0.,0.],[.001,.002],[.17,.41],[1.13,-.73],[0.,2.1],[6.3,3.7]])
exact=velocity(points);out['points']=points.tolist();out['exact_velocity']=exact.tolist()
for radius in (8.,16.,32.):
 for order in (12,24,48):
  inverse=CartesianInverse(omega,InverseSettings(radius=radius,core_radial_order=order,core_angular_order=order,exterior_radial_order=order,exterior_angular_order=order,decay_power=.5))
  full=inverse.relative(points);cut=inverse.relative(points,include_exterior=False)
  row={'core_radius':radius,'order':order,'full_error':float(np.max(np.abs(full-exact))),'without_exterior_error':float(np.max(np.abs(cut-exact))),'computed':full.tolist()};out['runs'].append(row)
  print('inverse',radius,order,row['full_error'],row['without_exterior_error'],flush=True)
for r0 in (.25,1.,4.):
 L=quad(lambda r:cutoff(r,r0)/r,r0,2*r0,epsabs=1e-12,epsrel=1e-12)[0]-np.log(2*r0)
 # Remove the integrable r^-1/2 singularity by r=t^2 on the first interval.
 first,e0=quad(lambda t:2*t*eta_radial(t*t,r0),0,np.sqrt(r0),epsabs=1e-11,epsrel=1e-11)
 middle,e1=quad(lambda r:eta_radial(r,r0),r0,2*r0,epsabs=1e-11,epsrel=1e-11)
 last,e2=quad(lambda r:eta_radial(r,r0),2*r0,np.inf,epsabs=1e-11,epsrel=1e-11)
 drift=.5*(first+middle+last);C=B*(.25-.5*L)-drift
 row={'cutoff_radius':r0,'L_chi':float(L),'U_eta_2_at0':float(drift),'C_extracted':float(C),'C_exact':-A,'absolute_error':float(abs(C+A)),'quad_error_estimate_not_rigorous':float(.5*(e0+e1+e2))};out['constant_cutoffs'].append(row);print('constant',row,flush=True)
theta=2*np.pi*(np.arange(720)+.371)/720;e=np.column_stack((np.cos(theta),np.sin(theta)))
for r in (10.,100.,1000.,10000.,100000.):
 pts=r*e;raw=velocity(pts)-asymptotic_without_constant(pts);error=raw-np.array([0.,-A])
 # Equivalent angular-mean extraction: remove leading and log, then add B/4.
 extracted=float(raw[:,1].mean())
 row={'radius':r,'maximum_remainder':float(np.max(np.abs(error))),'r_to_three_halves_scaled_remainder':float(r**1.5*np.max(np.abs(error))),'C_from_corrected_angular_mean':extracted,'C_error':float(abs(extracted+A))};out['asymptotic'].append(row);print('asymptotic',row,flush=True)
out['ended_utc']=datetime.now(timezone.utc).isoformat();out['elapsed_seconds']=time.monotonic()-start
Path('research/38_velocity_second_terms/verification/manufactured.json').write_text(json.dumps(out,indent=2)+'\n')
print('COMPLETE',out['elapsed_seconds'],flush=True)
