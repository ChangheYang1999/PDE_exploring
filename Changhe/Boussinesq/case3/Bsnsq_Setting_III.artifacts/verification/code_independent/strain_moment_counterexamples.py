"""Independent Cartesian formulas and full-plane checks of packet47."""
from pathlib import Path
from datetime import datetime,timezone
import numpy as np
from numpy.polynomial.legendre import leggauss
import json,time,os,hashlib
from cartesian_inverse import CartesianInverse,InverseSettings
from finite_difference import derivative
class Field:
 def __init__(self,beta,A,delta):self.beta=beta;self.nu=1/beta;self.B=1/(2*beta);self.C=1+beta/2;self.A=A;self.delta=delta
 def values(self,x,y):
  x,y=np.broadcast_arrays(np.asarray(x,dtype=float),np.asarray(y,dtype=float));q=x*x+y*y;e=np.exp(-q);a=-self.nu/2
  H=np.stack((x,x*y,x*(x*x-3*y*y)),axis=-1);Hx=np.stack((np.ones_like(x),y,3*x*x-3*y*y),axis=-1);Hy=np.stack((np.zeros_like(x),x,-6*x*y),axis=-1)
  f=np.stack((self.B*np.expm1(-q),(self.C-self.delta)*e+self.delta*(1+q)**a,self.A*e),axis=-1);fp=np.stack((-self.B*e,-(self.C-self.delta)*e+self.delta*a*(1+q)**(a-1),-self.A*e),axis=-1);fpp=np.stack((self.B*e,(self.C-self.delta)*e+self.delta*a*(a-1)*(1+q)**(a-2),self.A*e),axis=-1)
  gx=np.sum(Hx*f+2*x[...,None]*H*fp,axis=-1);gy=np.sum(Hy*f+2*y[...,None]*H*fp,axis=-1);om=-np.sum(H*(4*q[...,None]*fpp+4*(np.arange(1,4)+1)*fp),axis=-1);return np.stack((-gy,gx),axis=-1),om
 def omega(self,x,y):return self.values(x,y)[1]
 def F(self,x,y):return (1+np.asarray(x)**2+np.asarray(y)**2)**(-(1+2*self.nu)/2)
 def theta(self,x,y):return np.asarray(x)**2*self.F(x,y)
 def moment(self,n):
  t,w=leggauss(n);t=(t+1)/2;w=w/2;q=t/(1-t);r=np.sqrt(q);phi=2*np.pi*(np.arange(32)+.219)/32;x=r[:,None]*np.cos(phi);y=r[:,None]*np.sin(phi);V,om=self.values(x,y);qq=x*x+y*y;kx=y*(qq-4*x*x)/qq**3;ky=x*(qq-4*y*y)/qq**3;integrand=om*(V[...,0]*kx+V[...,1]*ky);angular=integrand.mean(1)*2*np.pi;NL=np.sum(angular*w/(2*(1-t)**2))/np.pi
  p=-(1+2*self.nu)/2;tx=2*x*(1+qq)**p+2*p*x**3*(1+qq)**(p-1);KL=x*y/qq**2*tx;La=np.sum(KL.mean(1)*2*np.pi*w/(2*(1-t)**2))/np.pi
  return float(NL),float(La)
root=Path('research/47_strain_moment_counterexamples/verification');start=time.monotonic();out={'status':'RUNNING','started_utc':datetime.now(timezone.utc).isoformat(),'pid':os.getpid(),'source_hashes':{f:hashlib.sha256(Path('code_independent',f).read_bytes()).hexdigest() for f in ('strain_moment_counterexamples.py','cartesian_inverse.py','finite_difference.py')},'cases':[]}
for beta in (2.,2.5,3.):
 B=1/(2*beta);C=1+beta/2
 for delta in (0.,.7,-1.2):
  for A in (-1.,0.,1.,-B/3-2*C/(9*B)):
   f=Field(beta,A,delta);expected=-1.5*B*B-4.5*A*B;row={'beta':beta,'delta':delta,'A':A,'B':B,'C':C,'expected_NL':expected,'quadratures':[]}
   for n in (64,128,256):
    nl,la=f.moment(n);row['quadratures'].append({'order':n,'NL':nl,'Lambda':la,'NL_error':nl-expected})
   out['cases'].append(row)
 print('moments beta',beta,'maxerror',max(abs(c['quadratures'][-1]['NL_error'])for c in out['cases'] if c['beta']==beta),flush=True)
f=Field(3.,-(1/6)/3-2*2.5/(9*(1/6)),.7);pts=np.array([[.13,.27],[.63,-.42],[1.13,.73],[.47,0.],[2.03,-1.17]])
V,om=f.values(*pts.T);out['inverse_checks']=[]
for n in (24,48,72):
 inv=CartesianInverse(f.omega,InverseSettings(radius=8.,core_radial_order=n,core_angular_order=n,exterior_radial_order=n,exterior_angular_order=n,decay_power=f.nu));vv=inv.relative(pts);out['inverse_checks'].append({'order':n,'max_abs_error':float(abs(vv-V).max()),'values':vv.tolist()})
print('inverse',out['inverse_checks'][-1]['max_abs_error'],flush=True)
out['pde_checks']=[]
for h in (.001,.0005,.00025):
 tx=derivative(f.theta,pts,0,h);ty=derivative(f.theta,pts,1,h);W=f.beta*pts+V;R=W[:,0]*tx+W[:,1]*ty-(f.beta-2)*f.theta(*pts.T);out['pde_checks'].append({'h':h,'points':pts.tolist(),'temperature_residual':R.tolist(),'max_abs':float(abs(R).max())})
# Axis divided defect calculated directly from Cartesian stream differentiation.
ys=np.array([.04,.02,.01,.005,.0025]);p=-(1+2*f.nu)/2;H02=-3*f.A-f.B;expected=-4*H02
axisrows=[]
for y in ys:
 q=y*y;e=np.exp(-q);aa=-f.nu/2;ff2=(f.C-f.delta)*e+f.delta*(1+q)**aa;fp2=-(f.C-f.delta)*e+f.delta*aa*(1+q)**(aa-1)
 # H= B(e^-q-1)+y f2 + A(x²-3y²)e^-q, at x=0.
 Hy=-2*f.B*y*e+ff2+2*y*y*fp2+f.A*(-6*y+6*y**3)*e
 W2=f.beta*y+f.values(0.,y)[0][1];F=(1+q)**p;Fy=2*p*y*(1+q)**(p-1);RF=2*(f.beta-Hy)*F+W2*Fy-(f.beta-2)*F
 axisrows.append({'y':float(y),'RF_over_y':float(RF/y),'expected_limit':expected})
out['axis_expansion']=axisrows;out.update(status='COMPLETE',ended_utc=datetime.now(timezone.utc).isoformat(),elapsed_seconds=time.monotonic()-start);(root/'checks.json').write_text(json.dumps(out,indent=2)+'\n');print('COMPLETE',out['elapsed_seconds'],'axis',axisrows[-1],flush=True)
