"""Finite integer checks for the block-support proof; no coefficient model."""
from pathlib import Path
from datetime import datetime, timezone
from hashlib import sha256
import json,time
start=time.monotonic();count=0
for Q in [3,5,7,9,11]:
 for u in range(2,8):
  for v in range(2,8):
   for r in range(Q):
    for s in range(1,Q+1):
     i,j=Q*u+r,Q*v+s
     w=(i+j-1)//Q;e=w-u-v
     assert e in (0,1)
     assert (i+j)//Q<=w+1
     for a in range(u):
      for b in range(v):
       for ell in [0,1]:
        degree=u+v-2-a-b-ell
        if degree<0:continue
        d=w-1-degree
        assert a+b+ell==d-1-e
        assert a+b<=d-1
        count+=1
solutions=0
for Kstar in range(2,101):
 A=Kstar+3;C=[]
 for d in range(101):
  values=[Kstar,d+1]+[x+3 for x in C]
  values += [C[a]+C[b]+3 for a in range(d) for b in range(d-a)]
  C.append(max(values));assert C[d]<=A*(d+1)-3
  solutions+=1
out=Path('research/69_log_degree_gap')
result=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds').replace('+00:00','Z'),block_degree_identities=count,support_recurrence_inequalities=solutions,all_passed=True,actual_elapsed_s=time.monotonic()-start,code_sha256=sha256(Path(__file__).read_bytes()).hexdigest())
(out/'verification/block_arithmetic.json').write_text(json.dumps(result,indent=2)+'\n')
(out/'sources/log_degree_block_arithmetic.py.txt').write_bytes(Path(__file__).read_bytes())
print(json.dumps(result))
