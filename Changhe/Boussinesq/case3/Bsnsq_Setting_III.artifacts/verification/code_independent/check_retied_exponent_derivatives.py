"""P201 exact algebra and native-field beta differences, independently written."""
from pathlib import Path
from datetime import datetime,timezone
import copy,json,time,hashlib
import numpy as np
import sympy as sp
from scipy.interpolate import BSpline
from r2_state_values import R2State

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'research/201_retied_exponent_derivatives/verification'
def now():return datetime.now(timezone.utc).isoformat()

def retied(s,b):
 v=copy.copy(s);v.bb=float(b);v.beta=float(b);v.meta=dict(s.meta,beta=b,beta_basis=b)
 return v

def analytic(s,points,kind):
 x,y=points.T;r=np.hypot(x,y);phi=np.arctan2(x,-y);b=s.bb
 ell=.5*np.log1p((r/s.L)**2);zeta=np.exp(-ell/b);t=-np.expm1(-ell/b)
 spline=s.Gs if kind=='G' else s.Fs;q=1 if kind=='G' else 2
 ang=np.cos(np.arange(s.K)[None,:]*phi[:,None]);ang[:,1::2]*=(r/np.hypot(r,s.L))[:,None]
 S=np.sum(spline(t)*ang,axis=1);St=np.sum(spline(t,1)*ang,axis=1);Stt=np.sum(spline(t,2)*ang,axis=1)
 D=np.exp(-ell-q*ell/b)
 first=D*ell/b**2*(q*S-zeta*St)
 second=D*(ell**2/b**4*(q*q*S-(2*q+1)*zeta*St+zeta*zeta*Stt)-2*ell/b**3*(q*S-zeta*St))
 pref=x if kind=='G' else x*x
 return first*pref,second*pref

def main():
 started=now();start=time.monotonic();b,ell,q=sp.symbols('b ell q',positive=True);t=1-sp.exp(-ell/b);zeta=1-t
 poly=sp.Symbol('c0')+sp.Symbol('c1')*sp.Symbol('t')+sp.Symbol('c2')*sp.Symbol('t')**2+sp.Symbol('c3')*sp.Symbol('t')**3
 tt=sp.Symbol('t');S=poly.subs(tt,t);St=sp.diff(poly,tt).subs(tt,t);Stt=sp.diff(poly,tt,2).subs(tt,t);D=sp.exp(-ell-q*ell/b)
 checks={
 'first_chain_rule':sp.simplify(sp.diff(D*S,b)-D*ell/b**2*(q*S-zeta*St))==0,
 'second_chain_rule':sp.simplify(sp.diff(D*S,b,2)-D*(ell**2/b**4*(q*q*S-(2*q+1)*zeta*St+zeta*zeta*Stt)-2*ell/b**3*(q*S-zeta*St)))==0}
 lam,cf=sp.symbols('lam cf');qq=sp.Matrix([2,-3]);z0=sp.Matrix([sp.Symbol('z1'),sp.Symbol('z2')]);qb=b*qq;Q=qb.dot(qb);cb=lambda v:b*qq.dot(v)
 p=z0+qb*(1+b/2-cb(z0)-lam*cf)/Q
 identities={'p_lambda':p.diff(lam)+cf*qb/Q,'p_b':p.diff(b)-(lam*cf-1)*qb/(b*Q),
             'p_bb':p.diff(b,2)+2*p.diff(b)/b,'p_b_lambda':p.diff(b,lam)-cf*qb/(b*Q)}
 for name,value in identities.items():checks[name]=all(sp.simplify(v)==0 for v in value)
 checks['projection_total_derivative']=sp.simplify(cb(p.diff(b))+cb(p)/b-sp.Rational(1,2))==0
 # A genuine exactly solvable affine fixed point checks the implicit derivative signs.
 aa=sp.Matrix([[sp.Rational(1,4),sp.Rational(1,6)],[sp.Rational(1,5),sp.Rational(1,3)]]);rhs=sp.Matrix([b*b+lam,b*lam+1]);I=sp.eye(2)
 zs=(I-aa).inv()*rhs;mm=cb(zs)+lam*cf-1-b/2
 for par in [b,lam]:
  deriv=-(aa-I).inv()*rhs.diff(par)
  checks['implicit_'+str(par)]=all(sp.simplify(v)==0 for v in deriv-zs.diff(par))
  reduced=cb(deriv)+(cb(zs)/b-sp.Rational(1,2) if par==b else cf)
  checks['reduced_'+str(par)]=sp.simplify(reduced-sp.diff(mm,par))==0
 states=[]
 sources=list((ROOT/'research/196_forced_tail_coefficients/verification').glob('*.npz'))
 radii=np.r_[0.,np.geomspace(2e-5,1e8,24)];angles=[.23,.79,1.61,2.82,3.59]
 points=np.array([[r*np.sin(phi),-r*np.cos(phi)] for r in radii for phi in angles])
 for path in sources:
  s=R2State(path);item={'file':str(path.relative_to(ROOT)),'sha256':s.sha256,'beta_basis':s.bb,'physical_points':len(points),'checks':[]}
  for kind in ['F','G']:
   d1,d2=analytic(s,points,kind)
   for step in [2e-3,1e-3,5e-4]:
    values=[]
    for j in [-2,-1,0,1,2]:
     ss=retied(s,s.bb+j*step);fn=ss.theta if kind=='F' else ss.omega
     values.append(fn(*points.T))
    a1=(values[0]-8*values[1]+8*values[3]-values[4])/(12*step)
    a2=(-values[0]+16*values[1]-30*values[2]+16*values[3]-values[4])/(12*step*step)
    err1=abs(a1-d1);err2=abs(a2-d2)
    item['checks'].append({'field':kind,'step':step,'first_absolute_max':float(max(err1)),
      'second_absolute_max':float(max(err2)),'first_scaled_max':float(max(err1/(1+abs(d1)))),
      'second_scaled_max':float(max(err2/(1+abs(d2)))),'scale_definition':'1+abs(exact derivative), not a PDE normalizer'})
  if s.native_source:
   ints=BSpline(s.knots,np.eye(s.nb),s.degree).integrate(0,1);grad=np.zeros((s.K,s.nb));grad[1]=-s.bb*s.L*ints/4
   if s.K>3:grad[3]=s.bb*s.L*ints/4
   for k in range(s.K):grad[k,:k//2]=0
   grad=grad.ravel();z=s.rawG.ravel();cfv=float(s.strain('native_seed'));lv=float(s.meta['lam']);b0=s.bb
   def proj(bb,ll):
    g=grad*bb/b0;c=g@z
    return z+g*(1+bb/2-c-ll*cfv)/(g@g)
   exact=(lv*cfv-1)*grad/(b0*(grad@grad));h=1e-4
   fd=(proj(b0-2*h,lv)-8*proj(b0-h,lv)+8*proj(b0+h,lv)-proj(b0+2*h,lv))/(12*h)
   item['projection_beta_difference_max']=float(max(abs(fd-exact)))
   item['center_strain_response_error']=float(abs(grad@exact+(grad@proj(b0,lv))/b0-.5))
  states.append(item)
 # An analytic r2 field with constant endpoint sum supplies a tail-topology diagnostic.
 # Logs of critical weighted values avoid overflow and do not replace the exact proof.
 topology=[];b0=3.;delta=.001
 for logr in [10.,100.,1000.,10000.]:
  ellv=.5*np.logaddexp(0.,2*logr)
  for bb in [b0-delta,b0,b0+delta]:
   logweighted=logr+logr/b0-ellv-ellv/bb
   topology.append({'log_r':logr,'beta':bb,'log_critical_weighted_Omega':float(logweighted),
                    'relative_beta_derivative':float(ellv/bb**2)})
 out={'started_utc':started,'ended_utc':now(),'elapsed_seconds':time.monotonic()-start,
      'exact_checks':checks,'all_exact_passed':all(checks.values()),'states':states,'topology_samples':topology,
      'scope':'Exact formulas and sampled finite differences of the serialized basis, not a fixed point, derivative certificate or unseen matrix audit.'}
 OUT.joinpath('checks.json').write_text(json.dumps(out,indent=2)+'\n')
 print(json.dumps({'utc':out['ended_utc'],'elapsed_seconds':out['elapsed_seconds'],'exact_checks':checks,
  'states':len(states),'max_first_scaled_error':max(r['first_scaled_max'] for s in states for r in s['checks']),
  'max_second_scaled_error':max(r['second_scaled_max'] for s in states for r in s['checks']),
  'max_projection_difference':max(s.get('projection_beta_difference_max',0.) for s in states)},indent=2),flush=True)
 if not all(checks.values()):raise RuntimeError('exact identity failed')

if __name__=='__main__':main()
