"""All saved cutoff bounds, exact intervals and complete algebraic extrema."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
from math import comb
import json,time,hashlib,argparse
from flint import arb,arb_poly,ctx
D=Path(__file__).resolve().parents[1];ctx.prec=256;start=time.monotonic()
ap=argparse.ArgumentParser();ap.add_argument('--limit',type=int,default=0);args=ap.parse_args()
def ff(x):return F.from_float(float(x))
def b(x):return arb(x.numerator)/x.denominator
def lo(x):return F(str(x.lower().fmpq()))
def hi(x):return F(str(x.upper().fmpq()))
raw=json.loads((D/'source/runs/forcing/p9_K64_n16_P8_merged.json').read_text());rows=raw['cells'];rows=rows[:args.limit] if args.limit else rows
S=[[1,0,0,0,0,-126,420,-540,315,-70]]
for j in range(1,6):S.append([i*S[-1][i] for i in range(1,len(S[-1]))])
Q=[None,[-630],[-2520,5040],[-7560,35280,-35280],[-15120,136080,-317520,211680]]
for j in range(1,5):
 a=5-j;fac=[0]*a+[(-1)**i*comb(a,i) for i in range(a+1)];out=[0]*(len(fac)+len(Q[j])-1)
 for k,v in enumerate(fac):
  for l,w in enumerate(Q[j]):out[k+l]+=v*w
 assert out==S[j]
# Independently expand -15120 P4(2v-1) to check the final critical polynomial.
p4=[0]*5
for deg,c in [(4,35),(2,-30),(0,3)]:
 for k in range(deg+1):p4[k]+=F(-15120*c,8)*comb(deg,k)*2**k*(-1)**(deg-k)
assert p4==S[5]
polys=[arb_poly(v) for v in S];crit={1:[arb(1)/2],2:[(7-arb(7).sqrt())/14,(7+arb(7).sqrt())/14],3:[(7-arb(21).sqrt())/14,arb(1)/2,(7+arb(21).sqrt())/14],4:sorted([(1+e*((15+d*2*arb(30).sqrt())/35).sqrt())/2 for e in [-1,1] for d in [-1,1]],key=lambda x:float(x.mid()))}
for j,roots in crit.items():
 assert len(roots)==j
 for v in roots:assert 0<lo(v)<=hi(v)<1 and polys[j+1](v).contains(0)
 for a,z in zip(roots,roots[1:]):assert hi(a)<lo(z)
# Precompute absolute critical values. Including roots on overlap is safe.
critvals={j:[(lo(v),hi(v),hi(abs(polys[j](v)))) for v in vals] for j,vals in crit.items()}
delta=F(33,2000);rin=7*delta/4;rout=9*delta/4;half=delta/2;scale=[b((2/delta)**j) for j in range(5)]
fail=[];checks=0;inside=0;transition=0;maxrat={k:F(0) for k in ['T0','T1','TL','TL1','TL2']};endpoint_inward={'low':0,'high':0};t2f=[]
for row in rows:
 d0,d1=map(ff,[row['dmin'],row['dmax']]);assert d0<=d1 and d0<rout
 aa=(d0-rin)/half;zz=(d1-rin)/half;a=max(F(0),min(F(1),aa));z=max(F(0),min(F(1),zz));assert a<=z
 endpoint_inward['low']+=ff(row['sigma'][0])>aa;endpoint_inward['high']+=ff(row['sigma'][1])<zz
 key=[row[k] for k in ['ci','q','ks','kp']]
 if d1<=rin:inside+=1;vals=dict(T0=F(1),T1=F(0),TL=F(0),TL1=F(0),TL2=F(0));hess=arb(0)
 else:
  transition+=1;A=b(a);Z=b(z);T=[arb(1) if a==0 else polys[0](A)]
  for j in range(1,5):
   m=max(hi(abs(polys[j](A))),hi(abs(polys[j](Z))))
   for c0,c1,v in critvals[j]:
    if c0<=z and c1>=a:m=max(m,v)
   T.append(b(m)*scale[j])
  inv=b(1/max(d0,rin));vals=dict(T0=hi(T[0]),T1=hi(T[1]),TL=hi(T[2]+T[1]*inv),TL1=hi(T[3]+T[2]*inv+T[1]*inv**2),TL2=hi(T[4]+2*T[3]*inv+T[2]*inv**2+T[1]*inv**3));hess=(T[2]**2+(T[1]*inv)**2).sqrt()
 for k,v in vals.items():
  checks+=1;saved=ff(row[k]);assert saved>=0
  if v>saved:fail.append(dict(key=key,quantity=k,own_upper=str(v),saved=str(saved)))
  if saved: maxrat[k]=max(maxrat[k],v/saved)
 # Compact outward binary endpoint for missing Hessian input, verified back
 # against its Arb upper bound, for optional later conditional replay only.
 import math
 hp=math.nextafter(float(hess.upper()),math.inf);assert ff(hp)>=hi(hess);t2f.append(hp)
out=dict(utc=datetime.now(timezone.utc).isoformat(),status='PASS_FINITE_CUTOFF_EXTREMA' if not fail else 'OPEN_CUTOFF_FAILURES',rows=len(rows),partial=bool(args.limit),checks=checks,inside=inside,transition=transition,seconds=time.monotonic()-start,inward_sigma_exports=endpoint_inward,max_ratio_upper={k:float(v) for k,v in maxrat.items()},failures=fail[:30],failure_count=len(fail),source_sha256=hashlib.sha256((D/'source/src/cert_forcing.py').read_bytes()).hexdigest(),method='Arb256, exact sigma endpoints, all algebraic critical points; direct factor and Legendre identities',scope='Cutoff fields only on supplied distance intervals. No residual field or full forcing acceptance.')
tag='cutoff_extrema_sample' if args.limit else 'cutoff_extrema';(D/'evidence'/f'{tag}.json').write_text(json.dumps(out,indent=2)+'\n')
if not args.limit:(D/'evidence/cutoff_hessian_bounds.json').write_text(json.dumps(dict(rows=len(rows),T2F=t2f,method='independent upper endpoints; not producer T2F'),separators=(',',':'))+'\n')
print(out['utc'],out['status'],'rows',len(rows),'failures',len(fail),'seconds',out['seconds']);assert not fail,fail[:2]
