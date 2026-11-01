"""Exact checks of a reciprocal-binomial norm and its Poisson obstruction."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
from math import comb,factorial
import time,json,sys
sys.dont_write_bytecode=True
from laurent_log_audit import Q,parse
from maximal_log_cartesian_check import poisson
start=time.monotonic();products=0;derivatives=0
for i in range(1,31):
 for j in range(1,31):
  for u in range(i):
   for v in range(j):
    assert comb(i-1,u)*comb(j-1,v)<=comb(i+j-1,u+v)
    products+=1
for k in range(2,101):
 for q in range(1,k):
  assert Q(q,comb(k-1,q-1))==Q(k-q,comb(k-1,q))
  derivatives+=1
rows=[]
for period in [3,4,5,9]:
 for k in range(2,16):
  n=period*k+1;q=k-1;m=2*k-3;delta=Q(2,period)
  F=parse(1-delta*n,{m:[Q(0)]*q+[Q(1)]})
  G=poisson(F)
  exact=Q(factorial(q),2)/delta**k
  observed=2*G.a[0][G.M+m+1]
  assert exact==observed
  rows.append(dict(Q=period,k=k,order=n,density_frequency=m,stream_frequency=m+1,degree=q,stream_constant=str(observed),formula=str(exact),equal=True))
root=Path('research/71_joint_weight_poisson_barrier')
result=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds').replace('+00:00','Z'),product_inequalities=products,derivative_identities=derivatives,poisson_witnesses=len(rows),all_passed=True,rows=rows,actual_elapsed_s=time.monotonic()-start)
result['sources']={name:sha256(Path('code',name).read_bytes()).hexdigest() for name in ['joint_weight_poisson_barrier.py','laurent_log_audit.py','maximal_log_cartesian_check.py']}
(root/'verification/checks.json').write_text(json.dumps(result,indent=2)+'\n')
for name in result['sources']:(root/'sources'/(name+'.txt')).write_bytes(Path('code',name).read_bytes())
print(json.dumps({k:v for k,v in result.items() if k not in ['rows','sources']}))
