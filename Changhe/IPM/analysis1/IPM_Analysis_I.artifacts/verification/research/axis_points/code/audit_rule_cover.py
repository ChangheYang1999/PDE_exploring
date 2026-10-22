"""Exact Gaussian root/weight and rational covering audit, no quadrature summation."""
import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS'):os.environ[key]='1'
import sys,json,hashlib,bisect
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
from flint import arb,ctx
BASE=Path(__file__).resolve().parents[3];sys.path.insert(0,str(BASE/'research/canonical_inverse/code'))
from exact_audit import legendre,dyadic
ctx.threads=1
checks=[]
for n in (28,32):
 ctx.prec=160;old=[arb.legendre_p_root(n,j,weight=True) for j in range(n)];ctx.prec=384;p=legendre(n);dp=p.derivative();fine=[arb.legendre_p_root(n,j) for j in range(n)]
 for j,x in enumerate(fine):
  lo,hi=dyadic(x.lower()),dyadic(x.upper());assert -1<lo<hi<1 and p(lo)*p(hi)<0
  if j+1<n:assert dyadic(fine[j+1].upper())<lo
  value=arb(0)
  for i in range(dp.degree(),-1,-1):value=value*x+arb(dp[i].numerator)/dp[i].denominator
  weight=2/((1-x*x)*value*value);assert old[j][0].contains(x) and old[j][1].contains(weight)
 checks.append({'n':n,'disjoint_exact_rational_sign_changes':n,'old_160_bit_node_weight_balls_contain_new_384_bit_certificates':True})
raw=json.loads((BASE/'data_exact/x3.json').read_text());knots=[F.from_float(float.fromhex(v)) for v in raw['spline_knots_hex']];parts=[]
for tag in ('axis7','axis10'):
 path=BASE/'research/axis_points/evidence'/(tag+'_partition.json')
 if not path.exists():continue
 d=json.loads(path.read_text());cap=F(d['cap_q']);ha,hb=map(F,d['removed_q_strip']);qs=[tuple(map(F,row)) for row in d['q']];assert qs[0][0]==cap and qs[-1][1]==1-cap
 gaps=[]
 for i,(a,b) in enumerate(qs):
  assert a<b and (b<=ha or a>=hb);j=bisect.bisect_right(knots,(a+b)/2)-1;assert knots[j]<=a<b<=knots[j+1]
  if i and qs[i-1][1]!=a:gaps.append((qs[i-1][1],a))
 assert gaps==[(ha,hb)] and sum((b-a for a,b in qs),F(0))==1-2*cap-(hb-ha)
 ts=[tuple(map(F,row)) for row in d['theta_over_pi_half']];assert ts[0][0]==0 and ts[-1][1]==1-F(d['cap_theta_normalized']) and all(a<b for a,b in ts) and all(ts[i-1][1]==ts[i][0] for i in range(1,len(ts)))
 for name,row in d['errors_before_prefactor'].items():assert arb(row['lower']).union(arb(row['upper']))>0
 parts.append({'tag':tag,'partition_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'q_cells':len(qs),'angle_cells':len(ts),'rational_coverage_and_original_spline_span_containment':'PASS','all_error_components_positive':'PASS'})
out={'utc':datetime.now(timezone.utc).isoformat(),'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'gaussian_rules':checks,'partition_checks':parts,'verdict':'CONFIRMED for rules and covers; the integral and Cauchy-bound code require their separate audit'}
(BASE/'research/axis_points/evidence/rule_cover_audit.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
