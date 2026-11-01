"""Exact support and Poisson checks for the shifted analytic-input example."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
from fractions import Fraction as Q
import math,json,time,sys
sys.dont_write_bytecode=True
import logarithmic_verify as lv
from cartesian_verify import sin_field,Q as CQ
start=time.monotonic();rows=[]
for delta in map(Q,['1/2','2/3','3/4','2/5','4/7','4/9']):
 a,b=delta.numerator,delta.denominator;g=math.gcd(a,2);h=a//g;q0=2*b//g;epsilon=int(h==1)
 for k in range(1,9):
  n=q0*(k+1)+2;q=2*h*(k+1);m=q-1;p=1-n*delta;s=2*(1-delta)
  assert k<=max(0,(n-1)//q0-epsilon) and k<=delta*(n-2)/2 and m<=2*n-1
  assert 2-n*delta+q==s and s>0
  f=lv.LogField(CQ(str(p)),{k:sin_field(CQ(str(p)),{m:CQ(1)}).modes});stream,res=lv.poisson(f)
  observed=Q(stream.amplitudes('sine')['0'][str(q)]);expected=-Q((-1)**k*math.factorial(k),2)/s**(k+1)
  assert observed==expected
  rows.append(dict(delta=str(delta),k=k,n=n,frequency=m,stream_frequency=q,constant=str(observed),sharp_degree_bound=max(0,(n-1)//q0-epsilon)))
symbols=[]
for k in range(1,101):
 n=3*k+2;q=2*k;c=(2-Q(2*n,3))**2-q*q
 assert c==Q(4,9)-Q(8*k,3) and c!=0
 symbols.append(dict(k=k,n=n,q=q,symbol=str(c),quadratic_ratio=str(abs(c)/(n+q+1)**2)))
root=Path('research/105_fuchsian_scope');result=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),exact_cartesian_examples=len(rows),symbol_identities=len(symbols),examples=rows,symbol_checks=symbols,actual_elapsed_s=time.monotonic()-start)
(root/'verification/exact_checks.json').write_text(json.dumps(result,indent=2)+'\n')
(root/'sources/fuchsian_scope_audit.py.txt').write_bytes(Path(__file__).read_bytes())
print(json.dumps({k:v for k,v in result.items() if k not in ['examples','symbol_checks']}),flush=True)
