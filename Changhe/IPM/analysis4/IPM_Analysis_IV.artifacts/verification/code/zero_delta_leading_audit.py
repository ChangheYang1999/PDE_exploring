"""Independent Cartesian exact leading-Laurent coefficient audit."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
from math import comb
import json,time,sys
sys.dont_write_bytecode=True
from laurent_log_audit import L,Poly,Q,parse
root=Path('research/85_zero_delta_limit');start=time.monotonic()
H={1:parse(Q(1),{3:['1']})};G={1:parse(Q(2),{2:['1/2']})};rows=[]
for n in range(1,61):
 if n>1:
  C=None
  for i in range(1,n):
   j=n-i
   J=G[i].X()*H[j].Y()-G[i].Y()*H[j].X()
   C=J if C is None else C+J
  H[n]=C.scale(Q(1,n-1))
 def sine(m):
  return 2*H[n].a[0][H[n].M+m] if H[n].a and m<=H[n].M else Q(0)
 h1,h3=sine(1),sine(3)
 if n==1: e1=Q(0)
 elif n==2: e1=Q(-2)
 elif n%2==0: e1=Q((-1)**(n//2))
 else:
  k=(n-1)//2;e1=Q((-1)**k*comb(2*k-2,k-1),4**(k-1))
 if n%2==0:e3=Q(0)
 else:
  k=(n-1)//2;e3=Q((-1)**k*(2*k+1)*comb(2*k,k),4**k)
 assert h1==e1,(n,'h1',str(h1),str(e1))
 assert h3==e3,(n,'h3',str(h3),str(e3))
 assert sine(2*n+1)==1,(n,'top')
 G[n]=parse(Q(2),{2:[str(h3/(2*n))]})
 rows.append(dict(n=n,h1=str(h1),h3=str(h3),top_coefficient='1',identities=True))
res=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),actual_elapsed_s=time.monotonic()-start,orders=rows,checks=3*len(rows),source_sha256={})
for name in ['zero_delta_leading_audit.py','laurent_log_audit.py']:
 raw=Path('code',name).read_bytes();(root/'sources'/(name+'.txt')).write_bytes(raw);res['source_sha256'][name]=sha256(raw).hexdigest()
(root/'verification/checks.json').write_text(json.dumps(res,indent=2)+'\n')
print(json.dumps({k:v for k,v in res.items() if k!='orders'}))
