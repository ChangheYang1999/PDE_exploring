"""Independent scalar and exact polynomial checks of the high majorant."""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[key]='1'
from pathlib import Path
from fractions import Fraction as F
from math import factorial,comb
from datetime import datetime,timezone
import json,hashlib
from flint import arb,ctx
ROOT=Path(__file__).resolve().parents[1];LANE=ROOT.parents[1]
ctx.prec=1024;ctx.threads=1

def aa(x):
 x=F(x);return arb(x.numerator)/x.denominator

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def val(d,key):return arb(d[key]['ball'])
def polyadd(a,b):
 out=[F(0)]*max(len(a),len(b))
 for i,x in enumerate(a):out[i]+=x
 for i,x in enumerate(b):out[i]+=x
 return out

def mul(a,b):
 out=[F(0)]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):out[i+j]+=x*y
 return out

def audit_file(path):
 d=json.loads(path.read_text());assert d['input_sha256']==sha(LANE.parent/'source/analysis1/IPM_Analysis_I.artifacts/numerics/data/trial_v2_h0.008.npz')
 assert d['spline_spans']==1558 and d['outer_leading_terms_removed']==262
 # Separate convolution implementation of the differential polynomial recurrence.
 p=[F(1)];checks=0
 for row,cb in zip(d['weight_polynomials'],d['weight_derivative_bounds']):
  assert p==list(map(F,row));assert sum(map(abs,p),F(0))==F(cb);checks+=1
  pd=[i*p[i] for i in range(1,len(p))]
  p=polyadd(mul([F(-9,5),F(53,10)],p),mul([F(0),F(1),F(-1)],pd or [F(0)]))
  while len(p)>1 and p[-1]==0:p.pop()
 mid=[arb(x['ball']) for x in d['middle_M']];inn=[arb(x['ball']) for x in d['inner_M']];out=[arb(x['ball']) for x in d['outer_M']]
 L=aa(F(d['t_plus'])-F(d['t_minus']));di=aa(F(1,10));do=aa(F(1,2)-2*F(d['k']))
 A=L*mid[0]+inn[0]/di+out[0]/do
 B=L*mid[7]+inn[7]/di+out[7]/do+3116*mid[6]+inn[6]+out[6]
 assert A.overlaps(val(d,'A')) and B.overlaps(val(d,'B'))
 # Recompute cutoff bound using the partition form of Bell polynomials.
 H=[aa(1)]+[aa(factorial(j)*(9*j)**j) for j in range(1,9)];R=[aa(2).exp()]
 for n in range(1,9):R.append(aa(2).exp()*sum((comb(n,l)*2*H[l]*R[n-l] for l in range(1,n+1)),arb(0)))
 S=[sum((comb(n,l)*H[l]*R[n-l] for l in range(n+1)),arb(0)) for n in range(9)]
 def partitions(total,lo=1):
  if total==0:yield []
  for first in range(lo,total+1):
   for tail in partitions(total-first,first):yield [first]+tail
 M8=arb(0);pc=0
 for part in partitions(8):
  mult={j:part.count(j) for j in set(part)};term=S[len(part)]*factorial(8)
  for j,k in mult.items():term*=aa(F(72,7)*2**j)**k/(factorial(k)*factorial(j)**k)
  M8+=term;pc+=1
 assert M8.overlaps(val(d,'M8'))
 sig=aa(F(25,4));two=aa(2)**sig
 Cchi=two.sqrt()*(1+2*two.sqrt()*aa(F(7,3))*M8)
 assert Cchi.overlaps(val(d,'C_chi'))
 R2=two/arb.pi()*(A*A+2*B*B)
 C2=2*arb.pi()*aa(1+1044**2)**sig*R2
 Cplus2=2*arb.pi()*aa(1+1047**2)**sig*R2
 eta=(R2+two**2*Cplus2+4*Cchi**2*C2).sqrt()
 assert eta.overlaps(val(d,'eta_star_bound'))
 assert eta<aa(10)**163
 if d.get('inner_method')=='green':
  assert eta<aa(6321*10**126)
  assert C2.sqrt()<aa(1195*10**90)
 return {'file':path.name,'sha256':sha(path),'polynomial_checks':checks,'Bell_partitions':pc,'scalar_reconstruction':'PASS','strict_eta_less_than_10_power_163':'PASS','green_sharp_bounds':'PASS' if d.get('inner_method')=='green' else 'NOT_APPLICABLE','eta_bound':eta.str(60)}

results=[audit_file(ROOT/'evidence'/name) for name in ('production_512.json','replay_768.json','green_512.json','green_768.json')]
out={'date':datetime.now(timezone.utc).isoformat(),'status':'SCALAR_AUDIT_PASSED','precision_bits':ctx.prec,'results':results,'script_sha256':sha(Path(__file__)),'proof_sha256':sha(ROOT/'PROOF.md')}
(ROOT/'evidence/scalar_audit.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
