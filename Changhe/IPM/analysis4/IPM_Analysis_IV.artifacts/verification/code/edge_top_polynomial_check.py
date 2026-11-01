"""Exact first-order kernel identities and certified finite polynomial-rate checks."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import json,time,sys
sys.dont_write_bytecode=True
from gmpy2 import mpq as Q
from flint import arb,fmpq,ctx
ctx.prec=512
start=time.monotonic()
source=sorted(Path('research/113_edge_top_radii/verification').glob('*/checks.json'))[-1]
raw=source.read_bytes();data=json.loads(raw)
assert data['all_checks_pass']
ball=lambda x:arb(fmpq(str(x)))
text=lambda x:x.str(35,radius=True)
cache={};previous={};rows=[]
counts=dict(kernel_remainder_identities=0,probability_sums=0,mean_order=0,
            mean_below_limit=0,special_exponents=0,subsolutions=0,supersolutions=0)
for row in data['rows']:
 delta=Q(row['delta']);B=row['B'];K=row['K'];eta=B-delta;d=delta/(1-delta)
 key=(str(delta),B)
 if key not in cache:
  h=[Q(0),Q(1)]
  for n in range(2,31):
   h.append(sum((Q(2*B*(n-i))/(eta*i+2)-1)*h[i]*h[n-i] for i in range(1,n))/(4*d*(n-1)))
  cache[key]=h
 h=cache[key];R=ball(Q(row['R_lower'])).union(ball(Q(row['R_upper'])))
 pp=[ball(Q(B)*h[i]/(2*d*(eta*i+2)))*R**i for i in range(1,K+1)]
 assert sum(pp,arb(0)).contains(1);counts['probability_sums']+=1
 mu=sum((i*p for i,p in enumerate(pp,1)),arb(0));b=ball(2*(B-1)/eta)
 assert mu<b;counts['mean_below_limit']+=1
 if key in previous:
  assert mu>previous[key];counts['mean_order']+=1
 previous[key]=mu
 s=2-ball(delta)/B-arb(B-2)/(B*mu)
 if B==2:
  assert (s-ball(2-delta/2)).contains(0);counts['special_exponents']+=1
 if K==1:
  assert (s-ball(1+(2-delta)/B)).contains(0);counts['special_exponents']+=1
 for n in [2*K+1,4*K+1,10*K+1,100*K+1]:
  for i in range(1,K+1):
   Di=i-1+(eta*i+2)/B
   ratio=(Q(n-i)+(eta*i+2)*Q(i)/(eta*(n-i)+2)-(eta*i+2)/B)/(n-1)
   remainder=-Di/Q(n*(n-1))+Q(i)*(eta*i+2)/((n-1)*(eta*(n-i)+2))
   assert ratio==1-Di/n+remainder
   counts['kernel_remainder_identities']+=1
 comparisons=[]
 for n in [100_000,1_000_000]:
  values={}
  for sign in [-1,1]:
   exponent=s+arb(sign)/10;value=arb(0)
   for i,p in enumerate(pp,1):
    Di=i-1+(eta*i+2)/B
    ratio=1-Di/(n-1)+Q(i)*(eta*i+2)/((n-1)*(eta*(n-i)+2))
    value+=p*ball(ratio)*(1-arb(i)/n)**(-exponent)
   if sign<0:
    assert value<1;counts['supersolutions']+=1
   else:
    assert value>1;counts['subsolutions']+=1
   values[str(sign)]=text(value-1)
  comparisons.append(dict(n=n,recurrence_ratio_minus_one=values))
 rows.append(dict(delta=str(delta),B=B,K=K,mean=text(mu),mean_limit=text(b),
                  exponent=text(s),limit_exponent=text(1+1/b),comparisons=comparisons))
stamp=datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')
root=Path('research/114_edge_top_polynomial_rate/verification')/stamp;(root/'sources').mkdir(parents=True)
result=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds'),
            all_checks_pass=True,counts=counts,rows=rows,
            input_path=str(source),input_sha256=sha256(raw).hexdigest(),
            actual_elapsed_s=time.monotonic()-start,
            scope='Finite arithmetic checks. The all-order comparison and limits require the standalone proof.')
(root/'checks.json').write_text(json.dumps(result,indent=2)+'\n')
for p in [Path('code/edge_top_polynomial_check.py'),Path('research/114_edge_top_polynomial_rate/PROOF.md')]:
 (root/'sources'/(p.name+'.txt')).write_bytes(p.read_bytes())
manifest={str(p.relative_to(root)):dict(bytes=p.stat().st_size,sha256=sha256(p.read_bytes()).hexdigest()) for p in root.rglob('*') if p.is_file()}
(root/'MANIFEST.json').write_text(json.dumps(dict(files=manifest),indent=2)+'\n')
print(json.dumps(dict(output_directory=str(root),all_checks_pass=True,counts=counts,actual_elapsed_s=result['actual_elapsed_s']),indent=2))
