"""Fresh exact/Arb1536 audit. No import of producer or its interval helpers."""
import os
for k in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS'):os.environ[k]='1'
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
from collections import Counter
import hashlib,json,itertools,math,time,sys
from flint import arb,fmpq,ctx
assert not sys.flags.optimize
ctx.prec=1536;ctx.threads=1
BASE=Path(__file__).resolve().parents[3];TOPIC=BASE/'research/source_local_estimate';EV=TOPIC/'evidence'
sha=lambda f:hashlib.sha256(Path(f).read_bytes()).hexdigest()
def b(q):
 q=F(q);return arb(fmpq(q.numerator,q.denominator))
def ep(x):
 m,e=x.man_exp();return F(int(m))*F(2)**int(e)
def fpow(q,r):return (b(q).log()*b(r)).exp()
def exactnorm2(x,y):return x*x+y*y
def main():
 tic=time.monotonic();data=json.loads((EV/'checks.json').read_text());counts=Counter()
 for name,digest in data['files'].items():assert sha(BASE/name)==digest;counts['current_producer_file_pins']+=1
 s=F(31,10);t=F(21,10);kap=F(1687,500);pi=arb.pi()
 def contains(key,value,record=None):
  r=data['scalar_enclosures'][key] if record is None else record
  lo,hi=F(r['lower_exact']),F(r['upper_exact']);vl,vh=ep(value.lower()),ep(value.upper())
  # Intersect with [0,infinity) only for analytically nonnegative sample ratios.
  if record is not None:vl=max(F(0),vl);vh=max(F(0),vh)
  assert lo<=vl<=vh<=hi,(key,lo,vl,vh,hi)
  counts['fresh_full_ball_containment']+=1
 # Affine coefficient computed before homogeneous endpoint substitution.
 for A,mu,g in itertools.product([F(10),F(51,5)],[F(99,100),F(101,100)],[F(29),F(30)]):
  outputs=[]
  for u in [F(0),F(1)]:
   margin=F(1)+(A+mu)/2-s*(mu+(A-mu)*u)+g*u
   assert margin>=kap;outputs.append(str(margin));counts['exact_affine_endpoint_bounds']+=1
  assert [str(A),str(mu),str(g)]+outputs in data['box_corners'];counts['exact_box_records']+=1
 ex=dict(kappa=kap,fast_margin=F(159,40),sfast_box=(F(1)+(F(51,5)+F(99,100))/2+29)/F(51,5),C_V_multiplier=3*s+9*(s+F(1,2)),K1_half_absorbed=F(1000,1687),delta_grid_threshold=F(3374,33),inner_separation=F(1,8),outer_separation=F(1,8),far_distance_ratio=F(1,10),far_distance_min=F(1,4),K2_scale=F(-16,5),K3_scale=F(-63,10),K4_scale=F(-51,10),alpha_t_squared_times_pi=F(5,22),beta_t_squared_times_pi=F(25,11))
 assert set(ex)==set(data['exact_constants'])
 for k,q in ex.items():assert F(data['exact_constants'][k])==q;counts['fresh_exact_constants']+=1
 # Gamma reflection replaces a quotient of Gamma factors by a square and sine.
 ds=fpow(2,s)*b(F(341,400)**2)*b(F(11,20)).gamma()**2*(pi*b(F(9,20))).sin()/pi**2
 scalar={k:b(v) for k,v in ex.items()}
 scalar.update(alpha_t=(b(F(5,22))/pi).sqrt(),beta_t=(b(F(25,11))/pi).sqrt(),scalar_commutator_prefactor=b(s)*fpow(2,F(11,10)),transport_remainder_prefactor=b(F(651,100))*fpow(2,F(-9,10)),U_commutator_prefactor=b(2)*fpow(3,s),D_s=ds,A10_over_log2=b(10)/b(2).log())
 for delta in [F(33,2000),F(1,20),F(1,10),F(1,5)]:
  tag=str(delta).replace('/','_');scalar['Jdelta_'+tag]=ds*pi*b(F(4)/s)*fpow(F(8)/delta,s)
  scalar['Cstrain_illustrative_p8.6_delta_'+tag]=b(F(3)*delta/(F(43,5)-3*delta)**3)/pi.sqrt()
  scalar['CV_threshold_delta_'+tag]=b(F(1687,1000)/delta)
  for j in range(5):scalar['far_k'+str(j)+'_delta_'+tag]=b(50*math.factorial(j+1)*(F(4)/delta)**j)/pi
 assert set(scalar)==set(data['scalar_enclosures'])
 for name,val in scalar.items():contains(name,val)
 for row in data['cases']:
  x,y,k,l=map(F,row['input_exact']);er=exactnorm2(x,y);kr=exactnorm2(k,l);rr=exactnorm2(x+k,y+l)
  # Entire angular-symbol difference squared is rational before any rounding.
  dot=x*k+y*l
  du=(x+k)*(y+l)/rr-x*y/er;dv=-(x+k)**2/rr+x*x/er
  diff=b(du*du+dv*dv).sqrt()
  jnew=fpow(1+rr,s/2);jold=fpow(1+er,s/2)
  u_ratio=jnew*diff/(2*fpow(3,s)*fpow(1+kr,s/2)*fpow(1+er,(s-1)/2))
  first=abs(jnew-jold)/(b(s)*fpow(2,s-2)*(b(kr).sqrt()*fpow(1+er,(s-1)/2)+fpow(kr,s/2)))
  second=abs(jnew-jold-b(s*dot)*fpow(1+er,(s-2)/2))/(b(s*(s-1)*kr)*fpow(2,s-4)*(fpow(1+er,(s-2)/2)+fpow(kr,(s-2)/2)))
  for name,val in [('U_symbol',u_ratio),('first_Taylor',first),('second_Taylor',second)]:
   assert val.is_finite() and ep(val.upper())<1;contains(name,val,row['ratios'][name]);counts['fresh_finite_pointwise_inequalities']+=1
 files=dict(data['files']);files.update({str((EV/'checks.json').relative_to(BASE)):sha(EV/'checks.json'),str(Path(__file__).relative_to(BASE)):sha(__file__)})
 out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_FRESH_LOCAL_CONSTANT_AUDIT','method':'Independent Arb1536 Gamma reflection and exp/log powers; exact affine box extrema; exact rational symbol difference norm before rounding; no producer imports. Sample tests are supplementary to universal proof.','files':files,'counts':dict(counts),'scalars':len(scalar),'cases':len(data['cases']),'seconds':time.monotonic()-tic}
 (EV/'output_audit.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k!='files'},indent=2))
if __name__=='__main__':main()
