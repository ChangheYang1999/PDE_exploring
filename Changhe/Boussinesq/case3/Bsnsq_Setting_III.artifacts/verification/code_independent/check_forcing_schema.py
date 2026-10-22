"""Regression cases for actual legacy/new additive source archive semantics."""
from pathlib import Path
import numpy as np,json,hashlib,sys
from datetime import datetime,timezone
from fractions import Fraction
from r2_state_values import R2State
r=Path('verification/forcing_schema_20261020T2142');r.mkdir(exist_ok=True)
source=Path('verification/additive_driver_20261020T2128/lambda_seed_snapshot.npz')
with np.load(source,allow_pickle=False) as z:base={k:z[k].copy() for k in z.files}
raw=base['cG'];testpoints=np.array([[.1,.2],[1.,-2.],[50.,3.]])
cases=[('effective',dict(lam=.3,eps=1.,beta_seed=4.,cG_f=.7*raw,cG_f_effective=.2*raw),1.2),
       ('zero_lambda',dict(lam=0.,eps=1.,beta_seed=4.,cG_f=.7*raw,cG_f_effective=np.zeros(0)),1.),
       ('legacy',dict(lam=.3,eps=1.,cG_f=.2*raw),1.2),
       ('seed_only',dict(lam=.3,eps=1.,beta_seed=4.,cG_f=.7*raw),None)]
results=[]
for name,changes,scale in cases:
 data=base.copy();data.update(changes);p=r/(name+'.npz');np.savez(p,**data);s=R2State(p)
 if scale is None:
  try:s.mixed_omega(*testpoints.T);passed=False;message='ERROR: source omission silently accepted'
  except ValueError as e:passed=True;message=str(e)
  results.append(dict(case=name,passed=passed,message=message))
 else:
  err=float(np.max(abs(s.mixed_omega(*testpoints.T)-scale*s.omega(*testpoints.T))))
  results.append(dict(case=name,passed=err<2e-12,max_abs_error=err,schema=s.forcing_schema))
# Actual seed coefficient at phi=pi/2: all odd modes vanish exactly.
s=R2State(source);F=Fraction.from_float
exact=Fraction(0);rounded=Fraction(0)
for k in range(0,s.K,2):
 sign=(-1)**(k//2);a=float(s.Es.c[-1,k]);b=float(s.Gs.c[-1,k])
 exact+=sign*(F(a)-F(b));rounded+=sign*F(a-b)
coef={'exact_difference_sum':dict(numerator=exact.numerator,denominator=exact.denominator,negative=exact<0),
      'rounded_subtraction_sum':dict(numerator=rounded.numerator,denominator=rounded.denominator,negative=rounded<0),
      'leading_tail_on_positive_x_ray':'L^(1+1/beta_seed) times this sum',
      'seed_sha256':s.sha256,'beta_seed':s.bb}
(r/'exact_source_coefficient.json').write_text(json.dumps(coef,indent=2)+'\n')
out=dict(time=datetime.now(timezone.utc).isoformat(),checks=results,all_pass=all(a['passed'] for a in results),code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),reader_sha256=hashlib.sha256(Path('code_independent/r2_state_values.py').read_bytes()).hexdigest())
(r/'results.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));print('both exact source sums negative',exact<0,rounded<0)
