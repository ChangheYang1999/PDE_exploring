"""Own analytic-cutoff flow and adjoint coefficient check for packet77."""
from pathlib import Path
from datetime import datetime,timezone
import numpy as np
from scipy.integrate import solve_ivp,quad
from scipy.special import expit
import json,time,hashlib,shutil,sys
root=Path(sys.argv[1]);root.mkdir(exist_ok=True,parents=True);start=time.monotonic()
beta=3.;lam=(beta-2)/2;mu=(3*beta+2)/2;c=1+beta/2;alpha=2*beta-1;q=alpha/lam;kappa=mu/lam;u0=.25

def cutoff(r):
 if r<=1:return 1.,0.
 if r>=2:return 0.,0.
 v=expit(1/(r-1)-1/(2-r))
 return v,-v*(1-v)*(1/(r-1)**2+1/(2-r)**2)
def kernel(x,y):return x*y/(x*x+y*y)**2
def grad_kernel_y(x,y):return x*(x*x-3*y*y)/(x*x+y*y)**3
def field(X,d):
 x,y=X;r=np.hypot(x,y);ch,dc=cutoff(r);psi0=c*x*y+d*x**3
 if r==0:return np.zeros(2)
 return np.array([beta*x-c*x*ch-psi0*dc*y/r,beta*y+(c*y+3*d*x*x)*ch+psi0*dc*x/r])
def coeff(d,z,rtol=2e-12):
 k=3*d/(mu-2*lam);Y=np.array([u0,u0**kappa*z-k*u0*u0])
 def rhs(t,s):return np.r_[field(s[:2],d),np.exp(alpha*t)*kernel(*s[:2])]
 def event(t,s):return np.hypot(*s[:2])-2
 event.terminal=True;event.direction=1
 sol=solve_ivp(rhs,(0,100),np.r_[Y,0.],method='DOP853',rtol=rtol,atol=rtol*1e-3,events=event)
 if len(sol.t_events[0])!=1:raise RuntimeError('exit not reached')
 T=sol.t[-1];M=sol.y[2,-1]+np.exp(alpha*T)*kernel(*sol.y[:2,-1])
 fun=lambda v:v**(q-1)*kernel(v,v**kappa*z-k*v*v)
 loc,err=quad(fun,0,u0,epsabs=1e-14,epsrel=1e-13)
 return dict(d=d,z=z,A=u0**q*M+loc/lam,M_at_u0=M,local_integral=loc/lam,quad_error=err,exit_time=T,nfev=sol.nfev,rtol=rtol,status=int(sol.status))
out=dict(started_utc=datetime.now(timezone.utc).isoformat(),parameters=dict(beta=beta,lam=lam,mu=mu,c=c,alpha=alpha,q=q,kappa=kappa,u0=u0),values=[],derivatives=[],funnel=[],status='RUNNING')
for d in [0.,-1e-4,-.001,-.01]:
 for z in [0.,.25,.5,.75,1.]:out['values'].append(coeff(d,z))
 print('coefficient d',d,[(v['z'],v['A']) for v in out['values'][-5:]],flush=True)
for d in [0.,-1e-4,-.001,-.01]:
 for h in [.002,.001]:
  z=.5;vv=[coeff(d,z+j*h)['A'] for j in [-2,-1,1,2]]
  der=(vv[0]-8*vv[1]+8*vv[2]-vv[3])/(12*h)
  out['derivatives'].append(dict(d=d,z=z,h=h,A_prime=der))
# Independent tolerance check of the expensive finite outgoing integral.
out['tolerance_checks']=[coeff(-.01,.5,rtol=v) for v in [1e-10,2e-12,2e-13]]
d=-.01;k=3*d/(mu-2*lam);a0=-3*beta*d/2;z=.5
A=next(v['A'] for v in out['values'] if v['d']==d and v['z']==z)
Ap=next(v['A_prime'] for v in out['derivatives'] if v['d']==d and v['h']==.001)
for u in [.2,.1,.05,.025,.0125]:
 K=lambda v:kernel(v,v**kappa*z-k*v*v)
 Kz=lambda v:grad_kernel_y(v,v**kappa*z-k*v*v)*v**kappa
 inte=quad(lambda v:v**(q-1)*K(v),0,u,epsabs=1e-25,epsrel=2e-12)[0]
 intez=quad(lambda v:v**(q-1)*Kz(v),0,u,epsabs=1e-25,epsrel=2e-12)[0]
 R=-u**(-q)*inte/lam;Ru=-q*R/u-K(u)/(lam*u);Rz=-u**(-q)*intez/lam
 zx=2*k*u**(1-kappa)-kappa*z/u
 M=u**(-q)*A+R;Mx=u**(-q-1)*(-q*A-kappa*z*Ap)+2*k*u**(-q+1-kappa)*Ap+Ru+zx*Rz
 out['funnel'].append(dict(u=u,M=M,Mx=Mx,scaled_Mx=Mx*u**(q-1+kappa),predicted_limit=2*k*Ap,weighted_area_density=a0*u**(2+kappa)*abs(Mx),density_times_u_power_q_minus3=a0*u**(q-1+kappa)*abs(Mx)))
out.update(ended_utc=datetime.now(timezone.utc).isoformat(),elapsed_seconds=time.monotonic()-start,status='COMPLETE',scope='Numerical illustration of the exact proof; no interval bound, no global PDE solution. Narrow-funnel derivative evaluated through the proved exact coordinate formula, with outgoing coefficient computed by independent physical flow.',code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
(root/'results.json').write_text(json.dumps(out,indent=2)+'\n');shutil.copyfile(__file__,root/'adjoint_funnel_check_snapshot.py')
print('COMPLETE',out['elapsed_seconds'],flush=True)
