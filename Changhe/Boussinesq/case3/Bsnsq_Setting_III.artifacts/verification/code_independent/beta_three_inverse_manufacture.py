"""Independent beta3 two leading powers plus third-source logarithmic inverse.
Verifier code only. Standalone informal manufacture precedes this check in91.
"""
from pathlib import Path
from datetime import datetime,timezone
import json,time,hashlib
import numpy as np
from scipy.integrate import quad
from cartesian_inverse import CartesianInverse,InverseSettings
A=.4;B=-.3;ALPHA=1.4;D=.7;G=2.
POWERS=[(1/3,A),(1/6,B)]

def omega(x,y):
 x=np.asarray(x);y=np.asarray(y);q=x*x+y*y
 out=ALPHA*x*(q+2)/(1+q)**2-8*D*x/(1+q)**3+3*G*x*y*(q+2)/(1+q)**2.5
 for a,w in POWERS:out-=w*x*(8*a*(1+q)**(a-1)+4*q*a*(a-1)*(1+q)**(a-2))
 return out

def velocity(points):
 x,y=np.asarray(points).T;q=x*x+y*y
 f=-ALPHA*np.log1p(q)/4+D*q/(1+q);fp=-ALPHA/(4*(1+q))+D/(1+q)**2
 for a,w in POWERS:
  f+=w*np.expm1(a*np.log1p(q));fp+=w*a*(1+q)**(a-1)
 u1=-2*x*y*fp-G*x*((1+q)**(-.5)-y*y*(1+q)**(-1.5))
 u2=f+2*x*x*fp+G*y*((1+q)**(-.5)-x*x*(1+q)**(-1.5))
 return np.column_stack((u1,u2))

def asymptotic(points):
 points=np.asarray(points);r=np.linalg.norm(points,axis=1);c=points[:,0]/r;sn=points[:,1]/r
 out=np.zeros_like(points)
 for a,w in POWERS:out+=w*r[:,None]**(2*a)*np.column_stack((-2*a*c*sn,1+2*a*c*c))
 out+=ALPHA/2*np.column_stack((c*sn,-c*c))-ALPHA/2*np.log(r)[:,None]*np.array([0.,1.])
 gp=G*(c*c-sn*sn);g=G*c*sn
 out+=-gp[:,None]*np.column_stack((c,sn))+g[:,None]*np.column_stack((-sn,c))
 return out

def cutoff(r,r0):
 t=(r-r0)/r0
 if t<=0:return 0.
 if t>=1:return 1.
 aa=np.exp(-1/t);bb=np.exp(-1/(1-t));return aa/(aa+bb)

def eta_radial(r,r0):
 out=0.
 for a,w in POWERS:
  if r>1:
   h=r**(-2);v=(a-2)*np.log1p(h)
   out+=-4*a*w*r**(2*a-1)*((a+1)*np.expm1(v)+2*h*np.exp(v))
  else:out+=-w*r*(8*a*(1+r*r)**(a-1)+4*r*r*a*(a-1)*(1+r*r)**(a-2))+4*a*(a+1)*w*r**(2*a-1)
 if r>=2*r0:out+=-ALPHA/(r*(1+r*r)**2)
 else:out+=ALPHA*r*(r*r+2)/(1+r*r)**2-ALPHA*cutoff(r,r0)/r
 out-=8*D*r/(1+r*r)**3
 return out

start=time.monotonic();out={'started_utc':datetime.now(timezone.utc).isoformat(),'scope':'Smooth manufactured full-plane inverse only; no B2 transport solution.','parameters':{'A':A,'B':B,'alpha':ALPHA,'D':D,'G':G},'C_exact':D-A-B,'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'runs':[],'cutoff_constants':[],'asymptotics':[]}
points=np.array([[0.,0.],[.001,.002],[.17,.41],[1.13,-.73],[0.,2.1],[6.3,3.7]])
exact=velocity(points);out['points']=points.tolist();out['exact_velocity']=exact.tolist()
for radius in (8.,16.,32.):
 for order in (12,24,48):
  inv=CartesianInverse(omega,InverseSettings(radius=radius,core_radial_order=order,core_angular_order=order,exterior_radial_order=order,exterior_angular_order=order,decay_power=1/3))
  full=inv.relative(points);cut=inv.relative(points,include_exterior=False)
  row={'core_radius':radius,'order':order,'full_error':float(np.max(abs(full-exact))),'without_exterior_error':float(np.max(abs(cut-exact))),'computed':full.tolist()};out['runs'].append(row);print('inverse',radius,order,row['full_error'],row['without_exterior_error'],flush=True)
for r0 in (.25,1.,4.):
 L=quad(lambda r:cutoff(r,r0)/r,r0,2*r0,epsabs=1e-12,epsrel=1e-12)[0]-np.log(2*r0)
 # r=t^3 removes the most singular r^-2/3 input at0.
 first,e0=quad(lambda t:3*t*t*eta_radial(t**3,r0),0,r0**(1/3),epsabs=1e-11,epsrel=1e-11)
 mid,e1=quad(lambda r:eta_radial(r,r0),r0,2*r0,epsabs=1e-11,epsrel=1e-11)
 last,e2=quad(lambda r:eta_radial(r,r0),2*r0,np.inf,epsabs=1e-11,epsrel=1e-11)
 drift=.5*(first+mid+last);C=ALPHA*(.25-.5*L)-drift
 row={'cutoff_radius':r0,'L_chi':float(L),'ordinary_U_zeta_2_at0':float(drift),'C_extracted':float(C),'absolute_error':float(abs(C-(D-A-B))),'quadrature_error_estimate_not_rigorous':float((e0+e1+e2)/2)};out['cutoff_constants'].append(row);print('constant',row,flush=True)
phi=2*np.pi*(np.arange(720)+.371)/720;e=np.column_stack((np.cos(phi),np.sin(phi)))
for radius in (10.,100.,1000.,10000.,100000.,1000000.):
 val=velocity(radius*e)-asymptotic(radius*e);err=val-np.array([0.,D-A-B])
 row={'radius':radius,'max_remainder':float(np.max(abs(err))),'scaled_r_to_4_3_error':float(radius**(4/3)*np.max(abs(err))),'angular_average_C':float(val[:,1].mean())};out['asymptotics'].append(row);print('asymptotic',row,flush=True)
out.update(ended_utc=datetime.now(timezone.utc).isoformat(),elapsed_seconds=time.monotonic()-start)
root=Path('research/91_beta_three_logarithmic_tail/verification');(root/'manufactured_inverse.json').write_text(json.dumps(out,indent=2)+'\n')
print('COMPLETE',out['elapsed_seconds'],flush=True)
