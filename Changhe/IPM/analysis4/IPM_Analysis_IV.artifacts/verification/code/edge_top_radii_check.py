"""Exact recurrence and polynomial-root brackets for the edge top-mode theorem."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import json,time,sys
sys.dont_write_bytecode=True
from gmpy2 import mpq as Q
from flint import arb,fmpq,ctx
ctx.prec=512
start=time.monotonic();N=64;counts=dict(top_coefficients=0,tail_recurrence=0,coefficient_bounds=0,root_brackets=0,radius_ordering=0,radius_error_bounds=0,cartesian=0)
text=lambda x:x.str(36,radius=True)
def ball(x):return arb(fmpq(str(x)))
def generate(delta,B,K):
 d=delta/(1-delta);eta=B-delta;h=[Q(0),Q(1)]
 for n in range(2,N+1):
  h.append(sum((Q(2*B*(n-i))/(eta*i+2)-1)*h[i]*h[n-i] for i in range(1,n) if K is None or min(i,n-i)<=K)/(4*d*(n-1)))
  assert h[-1]>0;counts['top_coefficients']+=1
 return h
rows=[];references={}
for delta in [Q(1,3),Q(2,3),Q(4,9)]:
 for B in [2,4,6]:
  d=delta/(1-delta);eta=B-delta;full=generate(delta,B,None)
  a=2/eta;b=2*(B-1)/eta;aa=ball(a);bb=ball(b)
  beta=aa.gamma()*bb.gamma()/(aa+bb).gamma();RH=4*ball(d)*(aa*beta)**(1/aa)
  previous=None
  for K in [1,2,3,6,10,20,30]:
   h=generate(delta,B,K);cc=[Q(B)*full[i]/(2*d*(eta*i+2)) for i in range(1,K+1)]
   for n in range(2*K+1,N+1):
    tail=Q(0)
    for i,c_i in enumerate(cc,1):
     j=n-i;qn=full[i]*(B*(Q(j)/(eta*i+2)+Q(i)/(eta*j+2))-1)/(2*d*(n-1));Di=i-1+(eta*i+2)/B
     assert 0<qn<c_i and qn/c_i>=1-Di/(n-1);counts['coefficient_bounds']+=1
     tail+=qn*h[j]
    assert tail==h[n];counts['tail_recurrence']+=1
   def polynomial(x):return sum(v*x**i for i,v in enumerate(cc,1))-1
   lo=Q(0);hi=Q(1)
   while polynomial(hi)<0:hi*=2
   for iteration in range(140):
    mid=(lo+hi)/2
    if polynomial(mid)<=0:lo=mid
    else:hi=mid
   assert polynomial(lo)<=0<polynomial(hi);counts['root_brackets']+=1
   if K==1:assert lo<=2*d*(eta+2)/B<hi
   if previous is not None:assert hi<previous;counts['radius_ordering']+=1
   previous=lo
   assert ball(lo)>RH;counts['radius_error_bounds']+=1
   error_bound=4*d*(eta+2)/(eta*(K+1)+2)
   assert ball(hi)-RH<ball(error_bound)
   rows.append(dict(delta=str(delta),B=B,K=K,R_lower=str(lo),R_upper=str(hi),R_interval=text(arb.union(ball(lo),ball(hi))),full_R_H=text(RH),radius_gap=text(arb.union(ball(lo),ball(hi))-RH),proved_gap_upper=str(error_bound),last_order=N,last_top_root=text(ball(h[N])**(arb(1)/N))))
   if delta==Q(2,3) and B==2 and K in [1,3]:references[K]=h
reference=Path('research/102_edge_recurrence_reference/verification/exact_reference.json');raw=reference.read_bytes();ref=json.loads(raw)
for K,h in references.items():
 for row in ref['variants'][str(K)]['rows']:
  n=row['n'];assert Q(row['density']['0'][str(2*n-1)])==(-1)**(n-1)*h[n];counts['cartesian']+=1
stamp=datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ');root=Path('research/113_edge_top_radii/verification')/stamp;(root/'sources').mkdir(parents=True)
record=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds').replace('+00:00','Z'),all_checks_pass=True,counts=counts,rows=rows,reference_sha256=sha256(raw).hexdigest(),actual_elapsed_s=time.monotonic()-start,scope='Finite exact arithmetic and interval root brackets. The infinite coefficient-root limit is proved separately.')
(root/'checks.json').write_text(json.dumps(record,indent=2)+'\n')
for src in [Path('code/edge_top_radii_check.py'),Path('research/113_edge_top_radii/PROOF.md')]: (root/'sources'/(src.name+'.txt')).write_bytes(src.read_bytes())
manifest={str(p.relative_to(root)):{'bytes':p.stat().st_size,'sha256':sha256(p.read_bytes()).hexdigest()} for p in root.rglob('*') if p.is_file()}
(root/'MANIFEST.json').write_text(json.dumps({'files':manifest},indent=2)+'\n')
print(json.dumps(dict(output_directory=str(root),all_checks_pass=True,counts=counts,actual_elapsed_s=record['actual_elapsed_s'],unit_sine_delta_two_thirds=[r for r in rows if r['delta']=='2/3' and r['B']==2]),indent=2))
