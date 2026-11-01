"""Exact finite checks for the top-frequency edge hierarchy and a separate toy."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as Q
from hashlib import sha256
from math import factorial
import json,time,sys
sys.dont_write_bytecode=True
start=time.monotonic();N=30
counts=dict(kernel_identities=0,kernel_positivity=0,raw_symmetric_matches=0,positive_coefficients=0,prefix_matches=0,monotone_comparisons=0,strict_comparisons=0,first_differences=0,cartesian_coefficients=0,cartesian_log_zeroes=0,toy_prefix=0,toy_monotonic=0,toy_geometric=0,toy_central=0)
rows=[]
def sequence(delta,B,K):
 d=delta/(1-delta);eta=B-delta;h=[Q(0),Q(1)]
 for n in range(2,N+1):
  raw=Q(0);symmetric=Q(0)
  for i in range(1,n):
   j=n-i
   if K is not None and min(i,j)>K:continue
   lhs=Q(j)/(eta*i+2)+Q(i)/(eta*j+2)-Q(2*n)/(eta*n+4)
   rhs=eta*(eta*n+2)*(i-j)**2/((eta*i+2)*(eta*j+2)*(eta*n+4))
   assert lhs==rhs;counts['kernel_identities']+=1
   C=B*(Q(j)/(eta*i+2)+Q(i)/(eta*j+2))-1
   assert C>0;counts['kernel_positivity']+=1
   raw+=(Q(2*B*j)/(eta*i+2)-1)*h[i]*h[j]
   symmetric+=C*h[i]*h[j]
  assert raw==symmetric;counts['raw_symmetric_matches']+=1
  h.append(raw/(4*d*(n-1)));assert h[-1]>0;counts['positive_coefficients']+=1
 return h
stored={}
for delta in [Q(1,3),Q(2,3),Q(4,9)]:
 for B in [2,4,6]:
  full=sequence(delta,B,None);variants={K:sequence(delta,B,K) for K in range(1,7)}
  for K in range(1,6):
   v=variants[K];w=variants[K+1]
   for n in range(1,N+1):
    assert v[n]<=w[n]<=full[n];counts['monotone_comparisons']+=1
    if n<=2*K+1:assert v[n]==full[n];counts['prefix_matches']+=1
    else:assert v[n]<w[n];counts['strict_comparisons']+=1
   m=K+1;d=delta/(1-delta);eta=B-delta
   difference=(Q(2*B*m)/(eta*m+2)-1)*full[m]**2/(4*d*(2*m-1))
   assert difference==full[2*m]-v[2*m]>0;counts['first_differences']+=1
   rows.append(dict(delta=str(delta),B=B,K=K,first_difference_order=2*m,first_difference=str(difference),last_order=N,last_top_coefficient=str(v[N])))
  if delta==Q(2,3) and B==2:stored=variants
reference=Path('research/102_edge_recurrence_reference/verification/exact_reference.json');reference_raw=reference.read_bytes();ref=json.loads(reference_raw)
for K in [1,3]:
 for row in ref['variants'][str(K)]['rows']:
  n=row['n'];A=(-1)**(n-1)*stored[K][n]
  assert Q(row['density']['0'].get(str(2*n-1),'0'))==A
  assert Q(row['stream']['0'].get(str(2*n),'0'))==-A/(2*(Q(4,3)*n+2))
  counts['cartesian_coefficients']+=2
  for field,m in [('density',2*n-1),('stream',2*n)]:
   for q,col in row[field].items():
    if int(q)>0:
     assert Q(col.get(str(m),'0'))==0;counts['cartesian_log_zeroes']+=1
M=60
def toy(K):
 x=[0,1]
 for n in range(2,M+1):x.append(sum(factorial(min(i,n-i))*x[i]*x[n-i] for i in range(1,n) if K is None or min(i,n-i)<=K))
 return x
full=toy(None);toys={K:toy(K) for K in range(1,10)};toy_rows=[]
for m in range(1,M//2+1):
 assert full[2*m]>=factorial(m)*full[m]**2>=factorial(m);counts['toy_central']+=1
for K in range(1,9):
 x=toys[K];y=toys[K+1];c=[2*factorial(i)*x[i] for i in range(1,K+1)];A=max(1,2*sum(c));C=max(Q(x[n],A**n) for n in range(1,2*K+1))
 assert sum(Q(v,A**i) for i,v in enumerate(c,1))<=Q(1,2)
 for n in range(1,M+1):
  assert x[n]<=y[n]<=full[n];counts['toy_monotonic']+=1
  if n<=2*K+1:assert x[n]==full[n];counts['toy_prefix']+=1
  assert x[n]<=C*A**n;counts['toy_geometric']+=1
  if n>2*K:assert x[n]==sum(v*x[n-i] for i,v in enumerate(c,1))
 toy_rows.append(dict(K=K,A=str(A),C=str(C),last_order=M,full_at_last_digits=len(str(full[M])),edge_at_last_digits=len(str(x[M]))))
stamp=datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ');root=Path('research/112_edge_top_comparison/verification')/stamp;(root/'sources').mkdir(parents=True)
record=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds').replace('+00:00','Z'),all_checks_pass=True,counts=counts,top_order=N,toy_order=M,rows=rows,toy_rows=toy_rows,reference_path=str(reference),reference_sha256=sha256(reference_raw).hexdigest(),scope='Finite exact checks; all-order claims use the standalone proof. The toy is not an IPM recurrence.',actual_elapsed_s=time.monotonic()-start)
(root/'checks.json').write_text(json.dumps(record,indent=2)+'\n')
(root/'sources/edge_top_comparison_check.py.txt').write_bytes(Path('code/edge_top_comparison_check.py').read_bytes())
(root/'sources/PROOF.md').write_bytes(Path('research/112_edge_top_comparison/PROOF.md').read_bytes())
manifest={str(p.relative_to(root)):{'bytes':p.stat().st_size,'sha256':sha256(p.read_bytes()).hexdigest()} for p in root.rglob('*') if p.is_file()}
(root/'MANIFEST.json').write_text(json.dumps({'files':manifest},indent=2)+'\n')
print(json.dumps(dict(output_directory=str(root),all_checks_pass=True,counts=counts,actual_elapsed_s=record['actual_elapsed_s']),indent=2))
