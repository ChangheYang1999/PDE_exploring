from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
import json,hashlib,sys
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/gram_conformity'
def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def check(x,s):
 if not x:raise ValueError(s)
# Pull back the Euclidean metric from(a,3a+at,atheta), by matrix multiplication.
T=[[1,0,0],[3,1,0],[0,0,1]];G=[[sum(T[r][i]*T[r][j] for r in range(3)) for j in range(3)] for i in range(3)];check(G==[[10,3,0],[3,1,0],[0,0,1]],'metric')
# Direct physical-r exponents: near weight=-6, far weight=-2k-3,
# squared function has exponent2b; plane measure contributes+1; dr->dt adds+1.
# Affine basis ordered(k,j,d,constant), independent of the first script.
beta_in=(0,2,0,3);beta_out=(1,0,-1,0)
center=tuple(2*x+y for x,y in zip(beta_in,(0,0,0,-4)));far=tuple(2*x+y for x,y in zip(beta_out,(-2,0,0,-1)));check(center==(0,4,0,2) and far==(0,0,-2,-1),'physical exponents')
# Solve P-P'=(1+s)^n recursively, constructed by repeated multiplication.
powers=[Q(1)];moments={}
for n in range(13):
 if n:
  new=[Q(0)]*(len(powers)+1)
  for i,c in enumerate(powers):new[i]+=c;new[i+1]+=c
  powers=new
 P=[Q(0)]*(n+1)
 for j in range(n,-1,-1):P[j]=powers[j]+((j+1)*P[j+1] if j<n else 0)
 for j in range(n+1):check(P[j]-((j+1)*P[j+1] if j<n else 0)==powers[j],'antiderivative')
 if n%2==0:moments[n//2]=P[0]
check(moments[1]==5,'log squared integral')
# Beta recurrence from integral z^p(1-z)^q, without expanded polynomials.
def beta(p,q):
 z=Q(1,q+1)
 for i in range(1,p+1):z*=Q(i,i+q+1)
 return z
I0=beta(0,12)/2;Ic=-I0;I2=72*beta(2,10);total=9*I0+I2;check(total==Q(123,286),'compact cutoff')
a=json.loads((D/'evidence/exact_check.json').read_text());check(a['status']=='PASS_EXPANDED_POLYNOMIAL_AND_AFFINE_EXPONENT_CHECKS','first output');check({str(k):int(v) for k,v in moments.items()}==a['log_tail_integral_constants'],'independent tail moments');check(a['compact_reference_radial_integrals']==list(map(str,[I0,Ic,I2])) and a['bracket_integral']==str(total),'radial agreement');check(a['center_t_exponent']==[center[3],center[0],center[2],center[1]] and a['exterior_t_exponent']==[far[3],far[0],far[2],far[1]],'exponent agreement')
for n,h in a['files'].items():check(sha(B/n)==h,'first pin')
vpath=B/'research/gram_reference_space/evidence/verdict.json';v=json.loads(vpath.read_text());check(len(v['files'])==40 and sha(vpath)==a['prior_verdict_sha256'],'127 identity')
for n,h in v['files'].items():check(sha(B/n)==h,'127 pin')
r={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_METRIC_PULLBACK_PHYSICAL_EXPONENTS_AND_ANTIDERIVATIVE_RECURRENCE','metric':G,'affine_variables':['k','j','d','1'],'center_t_exponent':center,'exterior_t_exponent':far,'log_tail_integral_constants':{str(k):str(v) for k,v in moments.items()},'compact_reference_integrals':list(map(str,[I0,Ic,I2,total])),'prior_pins_rechecked':40,'files':{str(p.relative_to(B)):sha(p) for p in [D/'PROOF.md',D/'evidence/exact_check.json',vpath,Path(__file__)]},'scope':'Independent exact arithmetic of analytic formulas only; no matrix assembly, SVD, actual conformity or operator bound.'}
p=D/'evidence/independent_check.json';check(not p.exists(),'immutable');p.write_text(json.dumps(r,indent=2)+'\n');print(r['utc'],r['status'],sha(p))
