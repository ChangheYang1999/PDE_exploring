"""Exact superadditivity and high-harmonic coefficient majorant checks."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
from math import factorial
import json,time,pickle,sys
sys.dont_write_bytecode=True
sys.set_int_max_str_digits(0)
from flint import fmpq as Q
from log_degree_gap_audit import unpacked
start=time.monotonic();root=Path('research/73_improved_gevrey')
def B(A,k):return max(0,k-(k+3+A-1)//A)
count=0
for A in range(3,101):
 for u in range(101):
  for v in range(101):
   assert B(A,u)+B(A,v)<=B(A,u+v);count+=1
products=0
for q in [3,5,7,9,11]:
 for m in [q+2,q+4,q+8]:
  ks=(q*(m+1)+2)//4+1;A=ks+3
  for i in range(1,161):
   for j in range(1,161):
    assert B(A,i//q)+B(A,(j-1)//q)<=B(A,(i+j-1)//q);products+=1
cases=[]
for m in [5,9]:
 src=Path('research/69_log_degree_gap/verification')/f'Q3_M{m}.pkl';raw=src.read_bytes();fp,gp,_=pickle.loads(raw);fields={'f':unpacked(fp),'g':unpacked(gp)}
 ks=(3*(m+1)+2)//4+1;A=ks+3;C=84*(m+1);rows=[]
 for n in sorted(fields['f']):
  D=B(A,(n-1)//3);bound=Q(factorial(D)*(8*C)**(n-1),n)
  for f in ['f','g']:
   V=fields[f][n];norm=Q(0)
   for q,col in enumerate(V.a):
    physical=sum((2*abs(col[V.M+j]) for j in range(1,V.M+1)),Q(0))
    norm+=factorial(q)*12**q*physical
   rhs=bound*(12 if f=='g' else 1);assert norm<=rhs,(m,n,f)
   rows.append(dict(n=n,field=f,improved_D=D,degree=len(V.a)-1,exact_bound_holds=True,ratio_to_bound=str(norm/rhs)))
 cases.append(dict(harmonic=m,A=A,gevrey_order=str(Q(A-1,3*A)),N=max(fields['f']),source=str(src),source_sha256=sha256(raw).hexdigest(),checks=rows))
result=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds').replace('+00:00','Z'),superadditive_integer_checks=count,product_degree_checks=products,finite_norm_checks=sum(len(v['checks']) for v in cases),all_passed=True,cases=cases,actual_elapsed_s=time.monotonic()-start)
(root/'verification/checks.json').write_text(json.dumps(result,indent=2)+'\n')
for name in ['improved_gevrey_audit.py','log_degree_gap_audit.py','laurent_log_audit.py']:(root/'sources'/(name+'.txt')).write_bytes(Path('code',name).read_bytes())
print(json.dumps({k:v for k,v in result.items() if k!='cases'}))
