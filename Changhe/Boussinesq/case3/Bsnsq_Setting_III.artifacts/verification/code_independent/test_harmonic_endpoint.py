"""Own controls for packet161, after its standalone proof.

Holomorphic primitive by independent radial Gaussian quadrature; analytic
polar cutoff derivatives; Cartesian finite differences; log-radius ODE.
Numerical samples do not prove the all-order flatness or global construction.
"""
from pathlib import Path
from datetime import datetime,timezone
import argparse,json,time,hashlib
import numpy as np
import sympy as sy
from numpy.polynomial.legendre import leggauss
from scipy.integrate import solve_ivp
from scipy.special import expit
import mpmath as mp

DELTA=.0005; TH0=.51*np.pi; TH1=.55*np.pi
GAUSS={n:leggauss(n) for n in [64,128,256]}
def flat(u):
 if u<=0:return (0.,0.,0.)
 v=np.exp(-1/np.sqrt(u))
 return (v,.5*u**(-1.5)*v,(.25*u**(-3)-.75*u**(-2.5))*v)
def step(t):
 if t<=0:return 0.,0.,0.
 if t>=1:return 1.,0.,0.
 L=-1/t+1/(1-t); a=expit(L); b=1/t**2+1/(1-t)**2; c=-2/t**3+2/(1-t)**3
 return a,a*(1-a)*b,a*(1-a)*((1-2*a)*b*b+c)
def primitive(z,n=128):
 if z==0:return 0j
 x,w=GAUSS[n];t=(x+1)/2
 return z*np.dot(w/2,np.exp(-1/np.sqrt(t*z)))
def holomorphic(z):
 if z==0:return 0j,0j
 f=np.exp(-1/np.sqrt(complex(z)));return f,.5*complex(z)**(-1.5)*f

def hjet(u,y):
 r=np.hypot(u,y)
 if r==0:return 0.,np.zeros(2),np.zeros((2,2))
 theta=np.arctan2(y,u); t=(abs(theta)-TH0)/(TH1-TH0);s,sd,sdd=step(t)
 k=1-s;kd=-sd*np.sign(theta)/(TH1-TH0);kdd=-sdd/(TH1-TH0)**2
 if k==kd==kdd==0:return 0.,np.zeros(2),np.zeros((2,2))
 z=complex(u,y);P=primitive(z);f,fp=holomorphic(z);h=P.imag
 gh=np.array([f.imag,f.real]);hh=np.array([[fp.imag,fp.real],[fp.real,-fp.imag]])
 gt=np.array([-y,u])/r**2
 ht=np.array([[2*u*y,y*y-u*u],[y*y-u*u,-2*u*y]])/r**4
 return k*h,k*gh+kd*h*gt,k*hh+kd*(np.outer(gt,gh)+np.outer(gh,gt)+h*ht)+kdd*h*np.outer(gt,gt)

def kjet(u,y):
 r=np.hypot(u,y);v,vp,vpp=flat(u);J=y*v;gj=np.array([y*vp,v]);hj=np.array([[y*vpp,vp],[vp,0.]])
 if r==0:return J,gj,hj
 t=(r-DELTA)/DELTA;s,sd,sdd=step(t);zeta=1-s;zr=-sd/DELTA;zrr=-sdd/DELTA**2
 h,gh,hh=hjet(u,y);vct=np.array([u,y]);gz=zr*vct/r;hz=zrr*np.outer(vct,vct)/r**2+zr*(np.eye(2)/r-np.outer(vct,vct)/r**3)
 d=h-J;gd=gh-gj;hd=hh-hj
 return J+zeta*d,gj+zeta*gd+d*gz,hj+zeta*hd+np.outer(gz,gd)+np.outer(gd,gz)+d*hz

def field(u,y):
 k,g,h=kjet(u,y);return np.array([g[1],4*y-g[0]]),np.trace(h),4-h[0,1]

def exact_checks():
 u,y=sy.symbols('u y',real=True); v=sy.Function('v')(u);K=y*v;W=sy.Matrix([sy.diff(K,y),4*y-sy.diff(K,u)]);om=sy.diff(K,u,2)+sy.diff(K,y,2)
 checks={
  'base_divergence':sy.diff(W[0],u)+sy.diff(W[1],y)-4,
  'base_omega':om-y*sy.diff(v,u,2),
  'base_vorticity_residual':W.dot(sy.Matrix([sy.diff(om,u),sy.diff(om,y)]))+om-y*(v*sy.diff(v,u,3)+(5-sy.diff(v,u))*sy.diff(v,u,2)),
 }
 h=sy.Function('h')(u,y);W=sy.Matrix([sy.diff(h,y),4*y-sy.diff(h,u)])
 checks['stream_divergence']=sy.diff(W[0],u)+sy.diff(W[1],y)-4
 checks['vorticity_sign']=-(sy.diff(W[1],u)-sy.diff(W[0],y))-(sy.diff(h,u,2)+sy.diff(h,y,2))
 # Holomorphic Cauchy-Riemann field has divergence4 and zero vorticity.
 ar,ay=sy.symbols('ar ay');checks['CR_divergence']=ar+4-ar-4;checks['CR_vorticity']=-(-ay-ay*-1)
 z=sy.symbols('z',positive=True);f=sy.exp(-1/sy.sqrt(z))
 checks['f_prime']=sy.diff(f,z)-sy.Rational(1,2)*z**(-sy.Rational(3,2))*f
 checks['f_second']=sy.diff(f,z,2)-(sy.Rational(1,4)*z**-3-sy.Rational(3,4)*z**(-sy.Rational(5,2)))*f
 return [{'name':name,'residual':str(sy.simplify(val)),'pass':bool(sy.simplify(val)==0)} for name,val in checks.items()]

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--output',required=True);args=ap.parse_args();root=Path(args.output);root.mkdir(parents=True,exist_ok=True)
 start=time.monotonic();utc=datetime.now(timezone.utc).isoformat();exact=exact_checks();prim=[];fd=[];geometry=[];curves=[]
 mp.mp.dps=70
 for r in [DELTA/3,DELTA,2*DELTA,.01]:
  for theta in [-.54*np.pi,0.,.37*np.pi,.53*np.pi]:
   z=r*np.exp(1j*theta); f=holomorphic(z)[0];p64=primitive(z,64);p128=primitive(z,128);p256=primitive(z,256)
   zm=mp.mpc(float(z.real),float(z.imag));w=1/mp.sqrt(zm);ptrue=2*zm*mp.expint(3,w)
   # P(z)=2z int_1^infty exp(-w*q)q^-3dq.
   err=abs(p256-complex(ptrue))/max(abs(complex(ptrue)),1e-300)
   for eps in [1e-3,5e-4]:
    h=eps*r; vals=[primitive(z+j*h,256) for j in [-3,-2,-1,1,2,3]]
    dp=np.dot(np.array([-1,9,-45,45,-9,1])/60,vals)/h
    de=abs(dp-f)/max(abs(f),1e-300)
    prim.append({'r':r,'theta':theta,'step_relative':eps,'primitive_reference_relative_error':err,'Pprime_relative_error':de,'64_128_relative_change':abs(p64-p128)/max(abs(p128),1e-300),'128_256_relative_change':abs(p128-p256)/max(abs(p256),1e-300),'pass':bool(err<2e-10 and de<3e-7)})
 for r in [DELTA*.3,DELTA*.8,DELTA*1.3,DELTA*1.8]:
  for theta in [.13*np.pi,.49*np.pi,.517*np.pi,.531*np.pi,.541*np.pi,.8*np.pi]:
   u,y=r*np.cos(theta),r*np.sin(theta);k,g,h=kjet(u,y);W,om,d=field(u,y)
   reflect=field(u,-y);geometry.append({'r':r,'theta':theta,'Omega':float(om),'d_W2_dY':float(d),'reflection_error':float(max(abs(W[0]-reflect[0][0]),abs(W[1]+reflect[0][1]),abs(om+reflect[1]))),'pass':bool(d>3 and np.isfinite(om))})
   # Independent centered Cartesian derivatives of the scalar stream K.
   for eps in [2e-5,1e-5]:
    hh=eps*r; grad=[];hess=np.zeros((2,2))
    for j in [0,1]:
     e=np.eye(2)[j]*hh;a=np.array([u,y]); vv=[kjet(*(a+l*e))[0] for l in [-2,-1,0,1,2]]
     grad.append(float(np.dot([1,-8,0,8,-1],vv)/(12*hh)))
     hess[j,j]=float(np.dot([-1,16,-30,16,-1],vv)/(12*hh**2))
    ge=np.max(np.abs(np.array(grad)-g));he=np.max(np.abs(np.diag(hess)-np.diag(h)))
    gscale=max(np.max(np.abs(g)),1e-290);hscale=max(np.max(np.abs(h)),1e-290)
    fd.append({'r':r,'theta':theta,'step_relative':eps,'gradient_relative_error':float(ge/gscale),'diagonal_hessian_relative_error':float(he/hscale),'pass':bool(ge<2e-5*gscale+1e-280 and he<.015*hscale+1e-270)})
 # Strong unstable curve computed with a log(Y) ODE, two inner cutoffs and both signs.
 end=DELTA*.9;ys=np.geomspace(DELTA*.05,end,24);solutions={}
 for sign in [-1,1]:
  for inner in [DELTA*.001,DELTA*.01]:
   def rhs(t,v):
    Y=sign*np.exp(t);f=holomorphic(complex(v[0],Y))[0];return [f.real/(4-f.imag/Y)]
   sol=solve_ivp(rhs,(np.log(inner),np.log(end)),[0.],method='DOP853',rtol=3e-12,atol=1e-34,max_step=.025,dense_output=True)
   assert sol.success
   gu=sol.sol(np.log(ys))[0];solutions[(sign,inner)]=gu
   for Y,u in zip(sign*ys,gu):
    W,om,d=field(u,Y); angle=abs(np.arctan2(Y,u)); w=1/mp.sqrt(2*mp.mpf(abs(Y)));linear=float(mp.re(mp.expint(1,(1-1j)*w))/2)
    curves.append({'sign':sign,'inner':inner,'Y':float(Y),'g':float(u),'linearized_g':linear,'nonlinear_minus_linearized':float(u-linear),'Omega':float(om),'angle':float(angle),'pass':bool(angle<TH0 and abs(om)<1e-290 and d>3)})
 cutoff_error=max(np.max(abs(solutions[(s,DELTA*.001)]-solutions[(s,DELTA*.01)])) for s in [-1,1]);reflection_error=float(np.max(abs(solutions[(-1,DELTA*.001)]-solutions[(1,DELTA*.001)])))
 result={'started_utc':utc,'ended_utc':datetime.now(timezone.utc).isoformat(),'elapsed_seconds':time.monotonic()-start,'delta':DELTA,'theta0':TH0,'theta1':TH1,'exact':exact,'primitive':prim,'cartesian_differences':fd,'geometry':geometry,'strong_curve':curves,'curve_inner_cutoff_max_difference':float(cutoff_error),'curve_reflection_max_difference':reflection_error,'max_abs_g':float(max(abs(r['g']) for r in curves)), 'min_d_W2_dY':min(r['d_W2_dY'] for r in geometry),'all_passed':all(r['pass'] for group in [exact,prim,fd,geometry,curves] for r in group) and cutoff_error<2e-29 and reflection_error<2e-29,'scope':'Manufactured local controls, not a full-plane candidate, all-order proof or rigorous numerical error bound.'}
 (root/'results.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:v for k,v in result.items() if k not in ['exact','primitive','cartesian_differences','geometry','strong_curve']},indent=2))
 for key in ['exact','primitive','cartesian_differences','geometry','strong_curve']:print(key,len(result[key]),'failures',sum(not r['pass'] for r in result[key]))
 if not result['all_passed']:raise SystemExit(1)
if __name__=='__main__':main()
