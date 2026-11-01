"""Certify finite signed Poisson sums from retained dyadic coefficient balls."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
from fractions import Fraction
from math import factorial
from flint import arb,fmpq,ctx
import argparse,json,time,sys
sys.dont_write_bytecode=True
from stream_precision_audit import unpack
ap=argparse.ArgumentParser();ap.add_argument('snapshots',nargs='+');ap.add_argument('--orders',default='250,260,263,265,268');a=ap.parse_args()
ctx.prec=640;start=time.monotonic();text=lambda x:x.str(32,radius=True)
ball=lambda x:arb(fmpq(Fraction(x).numerator,Fraction(x).denominator))
inputs=[];available={}
for filename in a.snapshots:
 p=Path(filename)/'selected_packed_coefficients.json';raw=p.read_bytes();data=json.loads(raw);assert data['delta']=='2/3'
 inputs.append(dict(path=str(p),sha256=sha256(raw).hexdigest(),checkpoint_sha256=data['checkpoint_sha256']))
 for n in data['f']:available[int(n)]=(data,len(inputs)-1)
rows=[]
for n in map(int,a.orders.split(',')):
 data,source_index=available[n]
 F=[[arb(*unpack(x)) for x in row] for row in data['f'][str(n)]]
 G=[[arb(*unpack(x)) for x in row] for row in data['g'][str(n)]]
 degree=len(F)-1;P=Fraction(2)-Fraction(2*n,3)
 assert n%3 != 0
 fac=[factorial(h) for h in range(degree+1)]
 modecount=max(map(len,F));total_absolute=arb(0);selected=None;smallest=None
 for j in range(modecount):
  m=2*j+1;s=P+m+1;v=m+1-P
  assert s and v
  coeff=[row[j] if j<len(row) else arb(0) for row in F]
  if all(x==0 for x in coeff):continue
  B=sum((fac[h]*abs(x)/ball(abs(s))**(h+1) for h,x in enumerate(coeff)),arb(0))/2
  total_absolute+=B
  if smallest is None or abs(s)<smallest:
   smallest=abs(s)
   U=-sum(((-1)**h*fac[h]*x/ball(s)**(h+1) for h,x in enumerate(coeff)),arb(0))/2
   nxt=[row[j+1] if j+1<len(row) else arb(0) for row in F]
   D=sum((fac[h]*x/ball(v)**(h+1) for h,x in enumerate(nxt)),arb(0))/2
   target=G[0][(m+1)//2]
   assert target.overlaps(U+D)
   assert abs(U)>0 and abs(target)>0 and B>0
   H=sum((fac[h]*abs(x) for h,x in enumerate(coeff)),arb(0))/(2*ball(abs(s)))
   A=sum(map(abs,coeff),arb(0))
   assert abs(U)<=B or (abs(U)-B).contains(0)
   selected=dict(n=n,m=m,stream_mode=m+1,s=str(s),v=str(v),source_index=source_index,
       signed_upward=text(U),signed_downward=text(D),stored_stream_constant=text(target),identity_overlaps=True,
       absolute_bound=text(B),factorial_sum_without_shift_powers=text(H),input_plain_norm=text(A),
       log10_absolute_over_upward=text((B/abs(U)).log()/arb(10).log()),
       log10_factorial_over_upward=text((H/abs(U)).log()/arb(10).log()),
       log10_upward_over_plain=text((abs(U)/A).log()/arb(10).log()),
       log10_stream_over_plain=text((abs(target)/A).log()/arb(10).log()),
       log10_upward_over_stream=text((abs(U)/abs(target)).log()/arb(10).log()))
   selected_bound=B
 streamnorm=sum(map(abs,G[0]),arb(0))
 selected.update(total_absolute_upward_bound=text(total_absolute),stream_constant_column_norm=text(streamnorm),
     selected_mode_share_of_absolute_bound=text(selected_bound/total_absolute),
     log10_total_absolute_over_stream_norm=text((total_absolute/streamnorm).log()/arb(10).log()))
 rows.append(selected)
root=Path('research/77_poisson_cancellation');result=dict(checked_at_utc=datetime.now(timezone.utc).isoformat(timespec='seconds').replace('+00:00','Z'),
 precision_bits=640,inputs=inputs,results=rows,all_identity_overlaps=True,actual_elapsed_s=time.monotonic()-start)
(root/'verification/checks.json').write_text(json.dumps(result,indent=2)+'\n')
for name in ['poisson_cancellation_audit.py','stream_precision_audit.py']:(root/'sources'/(name+'.txt')).write_bytes(Path('code',name).read_bytes())
print(json.dumps(result,indent=2))
