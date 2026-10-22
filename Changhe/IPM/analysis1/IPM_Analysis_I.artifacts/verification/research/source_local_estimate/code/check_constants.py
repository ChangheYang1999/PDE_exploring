"""Exact box extrema, symbolic identities and two independent interval engines."""
import os
for n in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS'):os.environ[n]='1'
import sys,json,hashlib,time,itertools,math
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
from collections import Counter
import sympy as sp
from flint import arb,ctx,fmpq
from mpmath import iv
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/source_local_estimate';E=D/'evidence'
ctx.prec=512;ctx.threads=1;iv.dps=180
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def aq(q):q=Q(q);return arb(fmpq(q.numerator,q.denominator))
def iq(q):q=Q(q);return iv.mpf(q.numerator)/q.denominator
def ep(x):m,e=x.man_exp();return Q(int(m))*Q(2)**int(e)
def vp(z):sign,m,e,_=z;return (-1 if sign else 1)*Q(int(m))*Q(2)**int(e)
def endpoints(z):
 if isinstance(z,arb):
  assert z.is_finite(),repr(z)
  return [ep(z.lower()),ep(z.upper())]
 return [vp(v) for v in z._mpi_]
def pack(z):return {'lower_exact':str(z[0]),'upper_exact':str(z[1]),'mid_approx':float((z[0]+z[1])/2)}
def main():
 tic=time.monotonic();cnt=Counter();s=Q(31,10);t=s-1;kap=Q(1687,500)
 exact={};box=[]
 for A,mu,g in itertools.product([Q(10),Q(51,5)],[Q(99,100),Q(101,100)],[Q(29),Q(30)]):
  slow=1+A/2+(Q(1,2)-s)*mu;fast=1+(Q(1,2)-s)*A+mu/2+g
  assert slow>=kap and fast>=Q(159,40);box.append([str(v) for v in [A,mu,g,slow,fast]]);cnt['exact_box_inequalities']+=2
 exact.update(kappa=kap,fast_margin=Q(159,40),sfast_box=Q(2373,680),C_V_multiplier=3*s+Q(9,2)*(s+Q(1,2))*2,K1_half_absorbed=2/kap,delta_grid_threshold=kap/(2*Q(33,2000)),inner_separation=Q(5,4)-Q(9,8),outer_separation=Q(15,8)-Q(7,4),far_distance_ratio=1-Q(9,4)/Q(5,2),far_distance_min=Q(5,2)-Q(9,4),K2_scale=3-2*s,K3_scale=3-3*s,K4_scale=-s-2)
 assert exact['C_V_multiplier']==Q(417,10) and exact['delta_grid_threshold']==Q(3374,33)
 # Rational parts of all alpha/beta squares, multiplied by pi.
 exact.update(alpha_t_squared_times_pi=1/(4*(t-1)),beta_t_squared_times_pi=1/(4*(t-1)*(t-2)))
 x,y,kx,ky,r,ss,tt,a,z=sp.symbols('x y kx ky r ss tt a z', real=True)
 ids={}
 def check(name,expr):assert sp.simplify(expr)==0,(name,expr);ids[name]=str(expr)
 uv=sp.Matrix([x*y/(x*x+y*y),-x*x/(x*x+y*y)]);jac=uv.jacobian([x,y]);perp=sp.Matrix([-y,x])
 check('velocity_symbol_norm_squared',(uv.T*uv)[0]-x*x/(x*x+y*y))
 for i in range(2):
  for j in range(2):check(f'symbol_derivative_gram_{i}_{j}',(jac.T*jac)[i,j]-perp[i]*perp[j]/(x*x+y*y)**2)
 K1=-x*y/(sp.pi*(x*x+y*y)**2);K2=(x*x-y*y)/(2*sp.pi*(x*x+y*y)**2)
 zz=x+sp.I*y
 for deg in range(5):
  for by in range(deg+1):
   bx=deg-by;formula=(-1)**deg*math.factorial(deg+1)*sp.I**by/(2*sp.pi*zz**(2+deg))
   # Derivatives of the full complex kernel verify both real components together.
   check(f'complex_kernel_derivative_{bx}_{by}',sp.diff(1/(2*sp.pi*zz**2),x,bx,y,by)-formula)
 check('complex_kernel_real',sp.re(1/(2*sp.pi*zz**2))-K2)
 check('complex_kernel_imag',sp.im(1/(2*sp.pi*zz**2))-K1)
 check('raw_strain_kernel',-sp.diff(K2,y)-y*(3*x*x-y*y)/(sp.pi*(x*x+y*y)**3))
 check('strain_angular_triple',3*sp.sin(tt)-4*sp.sin(tt)**3-sp.sin(3*tt))
 check('hessian_radial_factor',ss*(1+x*x+y*y)**((ss-2)/2)+ss*(ss-2)*(1+x*x+y*y)**((ss-4)/2)*(x*x+y*y)-ss*(1+x*x+y*y)**((ss-4)/2)*(1+(ss-1)*(x*x+y*y)))
 check('heat_second_integration_gamma_factor',(-ss/2)*(1-ss/2)-(ss/2)*(ss/2-1))
 check('CV_constant',3*sp.Rational(31,10)+sp.Rational(9,2)*(sp.Rational(31,10)+sp.Rational(1,2))*2-sp.Rational(417,10))
 # Comparison ODE solved using integrating factor with formal positive gap d.
 d,R,Y,asym=sp.symbols('d R Y asym', positive=True)
 sol=sp.exp(-asym*tt/ss)*(z+R/d*Y*(1-sp.exp(-d*tt/ss)))
 check('semigroup_comparison_ODE',sp.diff(sol,tt)+asym*sol/ss-R*Y*sp.exp(-(asym+d)*tt/ss)/ss)
 aa,bb,cc,ee,ff,rr=sp.symbols('aa bb cc ee ff rr')
 check('outer_elimination',(1-bb*ee)*((aa+bb*cc)*ff+rr)/(1-bb*ee)-((aa+bb*cc)*ff+rr))
 # Exact sample set: illustrative tests, not the universal proofs.
 vectors=[(Q(1,10),Q(1,20)),(Q(1),Q(0)),(Q(0),Q(1)),(Q(3),Q(4)),(Q(-2),Q(1)),(Q(1,100),Q(-1,30)),(Q(-7),Q(-3)),(Q(100),Q(1))]
 kvals=[(Q(1,1000),Q(1,2000)),(Q(1,2),Q(1,3)),(Q(-1),Q(2)),(Q(10),Q(-20)),(Q(-3),Q(-4)),(Q(1,10),Q(-1,20)),(Q(0),Q(1)),(Q(7),Q(3))]
 cases=[list(p+k) for p,k in itertools.product(vectors,kvals) if (p[0]+k[0],p[1]+k[1])!=(0,0)]
 def scalars(cv,pi,powf,gamma,sqrt,log):
  sv=cv(s);tv=cv(t);at=1/(2*sqrt(pi*(tv-1)));bt=1/(2*sqrt(pi*(tv-1)*(tv-2)))
  ds=powf(cv(2),sv)*gamma(cv(Q(51,20)))*(cv(Q(341,400)))/(pi*gamma(cv(Q(9,20))))
  out={k:cv(v) for k,v in exact.items()}
  out.update(alpha_t=at,beta_t=bt,scalar_commutator_prefactor=sv*powf(cv(2),sv-2),transport_remainder_prefactor=sv*(sv-1)*powf(cv(2),sv-4),U_commutator_prefactor=2*powf(cv(3),sv),D_s=ds,A10_over_log2=cv(10)/log(cv(2)))
  for dq in [Q(33,2000),Q(1,20),Q(1,10),Q(1,5)]:
   delta=cv(dq);name=str(dq).replace('/','_');out['Jdelta_'+name]=4*pi*ds/sv*powf(8/delta,sv)
   out['Cstrain_illustrative_p8.6_delta_'+name]=3*delta/(sqrt(pi)*(cv(Q(43,5))-3*delta)**3)
   out['CV_threshold_delta_'+name]=cv(kap)/(2*delta)
   for n in range(5):out['far_k'+str(n)+'_delta_'+name]=100*math.factorial(n+1)/(2*pi)*powf(4/delta,cv(n))
  return out
 def ratios(case,cv,powf,sqrt):
  xx,yy,kk,ll=map(cv,case);er=xx*xx+yy*yy;kr=kk*kk+ll*ll;rr=(xx+kk)*(xx+kk)+(yy+ll)*(yy+ll)
  eh=sqrt(1+er);kh=sqrt(1+kr);jh=powf(1+rr,cv(s/2));je=powf(1+er,cv(s/2));kn=sqrt(kr)
  mm=[(xx+kk)*(yy+ll)/rr-xx*yy/er,-(xx+kk)*(xx+kk)/rr+xx*xx/er]
  # Degree-zero even symbol agrees exactly on collinear nonzero vectors.
  md=cv(0) if case[0]*case[3]-case[1]*case[2]==0 else sqrt(mm[0]*mm[0]+mm[1]*mm[1])
  return {'U_symbol':jh*md/(2*powf(cv(3),cv(s))*powf(kh,cv(s))*powf(eh,cv(s-1))),
  'first_Taylor':abs(jh-je)/(cv(s)*powf(cv(2),cv(s-2))*(kn*powf(eh,cv(s-1))+powf(kn,cv(s)))),
  'second_Taylor':abs(jh-je-cv(s)*powf(1+er,cv((s-2)/2))*(xx*kk+yy*ll))/(cv(s*(s-1))*powf(cv(2),cv(s-4))*kr*(powf(eh,cv(s-2))+powf(kn,cv(s-2))))}
 engines={};case_bounds={}
 for name,cv,pi,powf,gamma,sqrt,log in [('arb512',aq,arb.pi(),lambda x,y:x**y,lambda z:z.gamma(),lambda z:z.sqrt(),lambda z:z.log()),('iv180',iq,iv.pi,iv.power,iv.gamma,iv.sqrt,iv.ln)]:
  zz=scalars(cv,pi,powf,gamma,sqrt,log);engines[name]={k:pack(endpoints(z)) for k,z in zz.items()}
  for k,v in exact.items():lo,hi=endpoints(zz[k]);assert lo<=v<=hi;cnt[name+'_exact_scalar_contains']+=1
  case_bounds[name]=[]
  for case in cases:
   values=ratios(case,cv,powf,sqrt);obj={}
   for key,val in values.items():
    if isinstance(val,arb):assert val.is_finite(),(name,key,case,repr(val))
    lo,hi=endpoints(val);assert lo<=hi and hi<1,(name,key,case,lo,hi);lo=max(Q(0),lo);obj[key]=pack([lo,hi]);cnt[name+'_finite_pointwise_inequalities']+=1
   case_bounds[name].append(obj)
 scalar_bounds={k:pack([min(Q(engines[n][k]['lower_exact']) for n in engines),max(Q(engines[n][k]['upper_exact']) for n in engines)]) for k in engines['arb512']}
 packed_cases=[]
 for i,case in enumerate(cases):packed_cases.append({'input_exact':[str(q) for q in case],'ratios':{k:pack([min(Q(case_bounds[n][i][k]['lower_exact']) for n in engines),max(Q(case_bounds[n][i][k]['upper_exact']) for n in engines)]) for k in case_bounds['arb512'][i]}})
 pins={str(p.relative_to(B)):sha(p) for p in [Path(__file__),D/'PROOF.md',E/'proof_first.json',E/'source_pins.json']}
 for p,h in json.loads((E/'source_pins.json').read_text())['files'].items():assert sha(B/p)==h;pins[p]=h
 out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_LOCAL_ESTIMATE_CONSTANTS','files':pins,'exact_constants':{k:str(v) for k,v in exact.items()},'box_corners':box,'symbolic_identities':ids,'scalar_enclosures':scalar_bounds,'cases':packed_cases,'counts':dict(cnt),'scope':'Abstract coefficient box and explicit formula constants. p=8.6 used only for labelled illustrative strain constants. Finite pointwise tests supplement universal analytical proofs, not replace them.','seconds':time.monotonic()-tic}
 (E/'checks.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'utc':out['utc'],'status':out['status'],'identities':len(ids),'scalars':len(scalar_bounds),'cases':len(cases),'counts':dict(cnt),'D_s':scalar_bounds['D_s'],'seconds':out['seconds']},indent=2))
if __name__=='__main__':main()
