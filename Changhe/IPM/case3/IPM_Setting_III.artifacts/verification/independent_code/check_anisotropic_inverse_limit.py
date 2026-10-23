"""Independent symbolic and two-quadrature audit of result174."""
import os
for k in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS']:os.environ[k]='1'
from pathlib import Path
from datetime import datetime,timezone
import math,hashlib,json,time
import sympy as S
from scipy.integrate import quad
from scipy.special import gamma as Gamma,expit
import mpmath as mp

root=Path('research/anisotropic_inverse_limit/verification');root.mkdir(parents=True,exist_ok=True)
start=time.monotonic();out={'started_utc':datetime.now(timezone.utc).isoformat(),'status':'RUNNING','proof_sha256':hashlib.sha256(Path('research/anisotropic_inverse_limit/PROOF.md').read_bytes()).hexdigest(),'symbolic':[],'numerical':[]}
def save():out['updated_utc']=datetime.now(timezone.utc).isoformat();(root/'CHECKS.json').write_text(json.dumps(out,indent=2)+'\n')
def check(name,expr):
 z=S.simplify(S.expand(expr));assert z==0,(name,z);out['symbolic'].append(name)
x,y,xi,ell,h=S.symbols('x y xi ell h',real=True);h=S.symbols('h',positive=True)
g=xi**2*y+3*y+xi**4*y**3-y**5;phi=2*xi*y-3*xi*y**3+xi**3*y+xi**5*y**3
for sign in [1,-1]:
 a=sign*h**2;rho=a*g.subs(xi,x/h);psi=h*phi.subs(xi,x/h)
 ux=-S.diff(psi,y);uy=S.diff(psi,x)
 r=(ell*x+ux)*S.diff(rho,x)+(ell*y+uy)*S.diff(rho,y)-rho
 target=(ell*xi-S.diff(phi,y))*S.diff(g,xi)+(ell*y+S.diff(phi,xi))*S.diff(g,y)-g
 check(f'transport-sign-{sign}',r.subs(x,h*xi)/a-target)
 po=(-S.diff(psi,x,2)-S.diff(psi,y,2)-S.diff(rho,x)).subs(x,h*xi)/h
 check(f'poisson-sign-{sign}',po-(-S.diff(phi,y,2)-S.diff(phi,xi,2)/h**2-sign*S.diff(g,xi)))
 check(f'strain-sign-{sign}',S.diff(psi,x,y).subs(x,h*xi)-S.diff(phi,xi,y))
 b,e=S.symbols('b e');rp=a*y+b*x*x*y+e*y**3;gp=S.expand(rp.subs(x,h*xi)/a)
 check(f'cubic-sign-{sign}',gp-(y+sign*b*xi**2*y+e/a*y**3))
p=S.symbols('p',positive=True);K=S.symbols('K');check('stratified-positive-half',y*S.diff(K*y**p,y)-p*K*y**p)
q,s=S.symbols('q s',positive=True);Y=S.symbols('Y',positive=True)
low=S.exp(-q*s)*S.sinh(q*Y)/q;high=S.exp(-q*Y)*S.sinh(q*s)/q
check('kernel-low-ode',-S.diff(low,Y,2)+q*q*low);check('kernel-high-ode',-S.diff(high,Y,2)+q*q*high)
check('kernel-continuity',(high-low).subs(Y,s));check('kernel-derivative-jump',(S.diff(high,Y)-S.diff(low,Y)).subs(Y,s)+1)
alpha,bb=S.symbols('alpha bb',positive=True);J=S.pi/(2*alpha*bb*(alpha+bb));check('gaussian-angular-integral',J+bb*S.diff(J,bb)/2-S.pi/(4*bb*(alpha+bb)**2))
ga=S.symbols('ga',positive=True);f=y*(1+y*y)**((ga-2)/2)
check('tail-antiderivative',S.diff((1+y*y)**(ga/2)/ga,y)-f)
ht=S.exp(-xi*xi);ph0=-S.sqrt(S.pi)*xi*ht*S.erf(y)/2;gm=ht*y*S.exp(-y*y)
check('schwartz-limit-poisson',-S.diff(ph0,y,2)-S.diff(gm,xi));check('schwartz-limit-slope',S.diff(gm,y).subs({xi:0,y:0})-1)
check('schwartz-limit-strain',S.diff(ph0,xi,y).subs({xi:0,y:0})+1)
out['symbolic_count']=len(out['symbolic']);save()
for gma in [.25,.5,.75]:
 nu=1-gma/2;D=2**(2-gma)*Gamma(gma)*Gamma((3-gma)/2)/math.sqrt(math.pi)
 D2=2*Gamma(2-gma)*Gamma(gma)/Gamma(nu);assert abs(D-D2)<2e-14*D
 row={'gamma':gma,'D_gaussian':D,'D_beta':D2,'eps':[]};out['numerical'].append(row)
 for ep in [1.,1e-2,1e-4,1e-8,1e-12]:
  center=-.5*math.log(ep)
  def ff(z):
   if 2*z+math.log(ep)>7:return 0.
   sig=expit(z)
   return math.exp((2-gma)*z-2*float(__import__('numpy').logaddexp(0,z))-ep*math.exp(2*z))
  ranges=sorted(set([-55.,0.,center,center+3.]))
  val=err=0.
  for a,b in zip(ranges[:-1],ranges[1:]):
   v,e1=quad(ff,a,b,epsabs=2e-13,epsrel=2e-13,limit=250);val+=v;err+=e1
  scaled=-2*val/Gamma(nu)
  with mp.workdps(55):
   eg=mp.mpf(gma);en=1-eg/2;ee=mp.mpf(ep);ec=-mp.log(ee)/2
   def fm(z):return mp.exp((2-eg)*z-ee*mp.exp(2*z))/(1+mp.exp(z))**2
   parts=sorted(set([mp.mpf(-75),mp.mpf(0),ec,ec+4]))
   ref=-2*mp.quad(fm,parts)/mp.gamma(en)
  diff=abs(float(ref)-scaled);assert diff<2e-11*max(1,abs(scaled))
  row['eps'].append({'epsilon':ep,'scaled_strain':scaled,'unscaled_strain':scaled*ep**(-gma/2),'relative_to_limit':scaled/-D,'quad_error_estimate':2*err/Gamma(nu),'mp55_reference':mp.nstr(ref,45),'quadrature_difference':diff})
 save()
out['status']='PASS';out['elapsed_seconds']=time.monotonic()-start;out['finished_utc']=datetime.now(timezone.utc).isoformat();save();print(json.dumps({'status':'PASS','symbolic':out['symbolic_count'],'numerical_cases':sum(len(r['eps']) for r in out['numerical']),'seconds':out['elapsed_seconds']}))
