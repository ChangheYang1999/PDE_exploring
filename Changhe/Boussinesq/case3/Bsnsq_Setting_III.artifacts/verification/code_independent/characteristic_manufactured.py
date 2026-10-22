from pathlib import Path
from datetime import datetime,timezone
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq
import time,json,hashlib
from smooth_modal_flow import SmoothModalFlow,reconstruct
from finite_difference import derivative
root=Path('verification/characteristic_manufactured');root.mkdir(parents=True,exist_ok=True);start=time.monotonic()
# p2=c r^2(1+r^2)^(-a); a=1/6 yields slow nonintegrable vorticity.
def radial(r):
 c=.3;a=1/6;z=1+r*r;p=c*r*r*z**(-a)
 dp=2*c*r*z**(-a)-2*a*c*r**3*z**(-a-1)
 dpp=2*c*z**(-a)-10*a*c*r*r*z**(-a-1)+4*a*(a+1)*c*r**4*z**(-a-2)
 h=-dpp-dp/r+4*p/r**2
 return np.stack((0*r,p/r),axis=-1),np.stack((0*r,dp),axis=-1),np.stack((0*r,h),axis=-1)
def exactV(X):
 x,y=np.array(X);r=np.hypot(x,y);pr,dp,H=radial(r);ph=np.arctan2(x,-y)
 er=np.array([x,y])/r;et=np.array([-y,x])/r
 return -2*pr[1]*np.cos(2*ph)*er+dp[1]*np.sin(2*ph)*et
out={'started_utc':datetime.now(timezone.utc).isoformat(),'status':'RUNNING','interpolation':[],'transport':[]}
def save():
 out['elapsed_seconds']=time.monotonic()-start;(root/'results.json').write_text(json.dumps(out,indent=2)+'\n')
pts=np.array([[r*np.cos(th),r*np.sin(th)] for r in np.geomspace(2e-4,80,24) for th in [.13,.72,1.92,-1.1]])
for count in [100,200,400]:
 radii=np.geomspace(1e-4,100,count);pr,dp,H=radial(radii);f=SmoothModalFlow(3,radii,pr,dp,H)
 vv=[];jac=[];ell=[]
 for X in pts:
  W,D,om=f.values(X);V=W-3*X;vv.append(np.max(abs(V-exactV(X))))
  def fun0(x,y):return np.array([f.W(p)[0] for p in np.column_stack((np.ravel(x),np.ravel(y)))]).reshape(np.shape(x))
  def fun1(x,y):return np.array([f.W(p)[1] for p in np.column_stack((np.ravel(x),np.ravel(y)))]).reshape(np.shape(x))
  hs=2e-5*max(1.,np.linalg.norm(X))
  fd=np.array([[derivative(fun,X[None],ax,hs)[0] for ax in [0,1]] for fun in [fun0,fun1]])
  jac.append(float(np.max(abs(fd-D))));rad=float(np.linalg.norm(X));ph=np.arctan2(X[0],-X[1]);ell.append(float(abs(om-radial(rad)[2][1]*np.sin(2*ph))))
 row={'nodes':count,'max_velocity_error':max(vv),'max_DW_FD_difference':max(jac),'max_source_error':max(ell),'max_divV':max(abs(np.trace(f.DW(p))-6) for p in pts)}
 out['interpolation'].append(row);save();print('interpolation',row,flush=True)
# Exact area coordinates Xi=(x/g'(y),g(y)), g=(y+a tanh y)/(1+a).
class TestFlow:
 def __init__(self):self.beta=3.;self.lam=.5;self.mu=5.5;self.a=.35
 def gj(self,y):
  a=self.a;t=np.tanh(y);c=1-t*t;g=(y+a*t)/(1+a);p=(1+a*c)/(1+a);q=-2*a*c*t/(1+a);u=-2*a*c*(1-3*t*t)/(1+a)
  return g,p,q,u
 def W(self,X):
  x,y=X;g,p,q,u=self.gj(y);b=self.mu*g/p;A=self.lam+self.mu*g*q/p**2
  return np.array([A*x,b])
 def DW(self,X):
  x,y=X;g,p,q,u=self.gj(y);A=self.lam+self.mu*g*q/p**2
  Ay=self.mu*(q/p+g*u/p**2-2*g*q*q/p**3);by=self.mu*(1-g*q/p**2)
  return np.array([[A,x*Ay],[0.,by]])
 def theta_grad(self,X):
  x,y=X;g,p,q,u=self.gj(y);return x*x/p**2,np.array([2*x/p**2,-2*x*x*q/p**3])
 def omega(self,X):
  x,y=X;g,p,q,u=self.gj(y);xi=x/p
  def integrand(t):
   eta=np.exp(-self.mu*t)*g
   yy=brentq(lambda z:self.gj(z)[0]-eta,min(-1.,2*y),max(1.,2*y),xtol=1e-14)
   return np.exp(-(1+self.lam)*t)/self.gj(yy)[1]
  v,e=quad(integrand,0.,40.,epsabs=2e-12,epsrel=2e-12)
  return 2*xi*v
flow=TestFlow();points=[[.2,.3],[1.,-1.2],[3.,2.],[-.7,.6]]
for point in points:
 theta,grad=flow.theta_grad(point);omega=flow.omega(point)
 for cutoff in [1e-2,3e-3,1e-3]:
  row=reconstruct(flow,point,3.,1.,cutoff=cutoff)
  assert row['status']=='COMPLETE'
  row['exact_Theta']=theta;row['exact_gradient']=grad.tolist();row['independent_Omega_resolvent']=omega
  row['Theta_error']=abs(row['Theta']-theta);row['gradient_max_error']=float(np.max(abs(np.array(row['gradient'])-grad)));row['Omega_error']=abs(row['Omega']-omega)
  out['transport'].append(row);save()
 print('transport',point,[(r['cutoff'],r['Theta_error'],r['gradient_max_error'],r['Omega_error']) for r in out['transport'] if r['point']==point],flush=True)
out.update(status='COMPLETE',ended_utc=datetime.now(timezone.utc).isoformat(),scope='Interpolation and transport-resolvent manufactured tests only. Manufactured source flow is not claimed to satisfy the coupled vorticity-curl relation. No B2 profile.')
out['code_hashes']={n:hashlib.sha256(Path('code_independent',n).read_bytes()).hexdigest() for n in ['smooth_modal_flow.py','characteristic_manufactured.py']};save();print('COMPLETE',out['elapsed_seconds'],flush=True)
