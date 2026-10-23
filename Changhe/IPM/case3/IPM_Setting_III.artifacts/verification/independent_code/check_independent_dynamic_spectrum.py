"""Manufactured gates before the independent finite DR spectral audit."""
import os
for key in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS']:os.environ[key]='1'
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
import hashlib,json,math,time
import numpy as np
import mpmath as mp
import sympy as S
from independent_dynamic_spectrum import CanonicalCompression
from q_local_checkpoint import exact_affine_chebyshev
from q_mp_primitives import MPQPrimitives,mf,guard_digits

root=Path('research/independent_dynamic_spectrum/verification');root.mkdir(parents=True,exist_ok=True)
start=time.monotonic();out={'status':'RUNNING','started_utc':datetime.now(timezone.utc).isoformat(),'code_sha256':hashlib.sha256(Path('independent_code/independent_dynamic_spectrum.py').read_bytes()).hexdigest(),'derivatives':[],'inverse':[],'directional':[]}
def save():(root/'GATE.json').write_text(json.dumps(out,indent=2)+'\n')
m=CanonicalCompression(12,4)
rr=np.array([.03,.3,1.,4.,20.,100.]);lr=np.log(rr);theta=np.array([.13,.6,1.2]);x=S.symbols('x')
for k in range(m.M):
 co=np.array([(-1.)**j/(10+j) for j in range(m.N+1-k)])[:,None]
 tk=F(float(m.t[k]));cc=exact_affine_chebyshev(co[:,0],2/(1-tk),-(1+tk)/(1-tk))
 poly=sum(S.Rational(c.numerator,c.denominator)*S.chebyshevt(j,x) for j,c in enumerate(cc))*((1+x)/2)**k
 df=S.lambdify(x,S.diff(poly,x),'numpy');ts=np.array([-.99,-.6,0.,.5,.93]);own,der=m.mode_fields(k,ts,co)
 # Evaluate expanded polynomial at high precision to avoid a polynomial-basis comparison artifact.
 ref=np.array([float(S.diff(poly,x).subs(x,S.Rational(float(t))).evalf(80))for t in ts]);err=float(max(abs(der[:,0]-ref)))
 assert err<2e-9;out['derivatives'].append({'k':k,'complex_step_max_abs_error':err})
 coeff=[[F(0)]for _ in range(m.M)];coeff[k]=cc
 with mp.workdps(90+guard_digits(m.N,m.M,m.kappa)):
  p=MPQPrimitives(coeff,F(m.L),F(m.kappa),F(m.C));ref=[]
  for r in rr:
   row=[]
   for th in theta:
    X=mf(float(r))*mp.cos(mf(float(th)));Y=mf(float(r))*mp.sin(mf(float(th)));v=p.at(X,Y);ux,uy=v['U'];rho=v['rho'];gx,gy=v['gradient']
    row.append([float(ux/mf(float(r))),float(uy/mf(float(r)))])
   ref.append(row)
  strain=float(p.c)
 ref=np.array(ref);details=[]
 for order in [12,20,32]:
  ur,ut=m.polar_inverse(k,co,lr,theta,order);ux=ur[:,:,0]*np.cos(theta)-ut[:,:,0]*np.sin(theta);uy=ur[:,:,0]*np.sin(theta)+ut[:,:,0]*np.cos(theta)
  difference=float(np.max(abs(np.stack([ux,uy],axis=-1)-ref)));details.append({'order':order,'max_abs_error_U_over_r':difference})
 assert details[-1]['max_abs_error_U_over_r']<2e-8,details
 c=float(m.strain(k,co)[0]);assert abs(c-strain)<2e-11
 out['inverse'].append({'k':k,'strain':c,'primitive_strain':strain,'quadrature':details});save()
 # Independent centered difference of the quadratic field, with the same inverse values fixed only for this algebraic gate.
 br,bt=m.base_fields(20);br=br[:,:,0];bt=bt[:,:,0];ur,ut=m.polar_inverse(k,co,m.lr,m.theta,20);ur=ur[:,:,0];ut=ut[:,:,0]
 h,ht=m.mode_fields(k,m.t[1:],co);h=h[:,0];ht=ht[:,0]
 H=h[:,None]*m.angular[k];Ht=ht[:,None]*m.angular[k];Ha=h[:,None]*m.angular_d[k]
 Q=m.w[1:]+2*m.kappa*m.s[1:];Z=(1-2*m.s[1:]/Q)[:,None];T=(4*m.s[1:]*m.w[1:]/Q)[:,None];cot=1/np.tan(m.theta)
 dr=Z*H+T*Ht;da=cot*H+Ha;analytic=m.cw*H-(m.cx+br)*dr-bt*da-ur*Z-ut*cot-c/(m.C-1)*(1-m.C*Z)
 def field(t):
  B=1+t*H;Bdr=Z*B+t*T*Ht;Bda=cot*B+t*Ha;cw=(.25-t*c)/(m.C-1);cx=m.C*cw
  return cw*B-(cx+br+t*ur)*Bdr-(bt+t*ut)*Bda
 checks=[]
 for hstep in [1e-2,1e-3,1e-4]:
  fd=(field(hstep)-field(-hstep))/(2*hstep);checks.append({'step':hstep,'max_error':float(np.max(abs(fd-analytic)))})
 assert checks[0]['max_error']<1e-9
 out['directional'].append({'k':k,'checks':checks});save()
out.update(status='PASS',finished_utc=datetime.now(timezone.utc).isoformat(),elapsed_seconds=time.monotonic()-start);save();print(json.dumps({'status':'PASS','inverse_modes':len(out['inverse']),'elapsed':out['elapsed_seconds']}))
