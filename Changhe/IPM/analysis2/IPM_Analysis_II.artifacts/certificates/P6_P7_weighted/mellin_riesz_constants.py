from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
from flint import arb,ctx
import json
ctx.prec=384

def A(v):
 v=Q(v);return arb(v.numerator)/arb(v.denominator)
rows=[]
for a,b,target in [(1,Q(4,5),Q(16,3)),(2,Q(4,5),Q(9,5)),(1,Q(-1,5),Q(3,2)),(2,Q(-6,5),Q(8,3))]:
 b0=abs(b);pure=Q(a+b0,a-b0);H=arb(2)**A(abs(1-b0)/2)*A(pure);C=(1+H)/2
 assert C.is_finite() and C<A(target)
 rows.append({'a':a,'beta':str(b),'pure_power_B_norm':str(pure),'regular_weight_B_bound':H.str(65),'velocity_bound':C.str(65),'certified_upper':str(target)})
 # Check the exact squared-ratio inequality in n and rational tau without floating arithmetic.
 for n in range(-20,21):
  if not n or (a==2 and n%2):continue
  for t in [Q(0),Q(1,10),Q(1),Q(10),Q(1000)]:
   assert (t*t+(n+b)**2)<=(pure*pure)*(t*t+(n-b)**2)
out={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'precision_bits':ctx.prec,'results':rows,'sample_rational_ratio_checks':'PASS; these supplement the analytic proof'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
