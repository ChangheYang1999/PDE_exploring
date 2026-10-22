"""Second cutoff method: factored derivatives and interval Bernstein ranges."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
from math import comb
from mpmath import iv
import json,time,argparse,hashlib
D=Path(__file__).resolve().parents[1];iv.dps=70;start=time.monotonic();ap=argparse.ArgumentParser();ap.add_argument('--limit',type=int,default=0);ap.add_argument('--start',type=int,default=0);ap.add_argument('--count',type=int,default=0);args=ap.parse_args()
def ff(x):return F.from_float(float(x))
def b(x):return iv.mpf(x.numerator)/x.denominator
def mpf(x):
 s,m,e,bc=x
 assert s in (0,1) and m>=0 and bc>=0 and ((m==0 and e==0 and bc==0) or (m>0 and m.bit_length()==bc)), ('nonfinite or noncanonical endpoint',x)
 return (-1 if s else 1)*F(m)*F(2)**e
def low(x):return mpf(x._mpi_[0])
def high(x):return mpf(x._mpi_[1])
def horner(p,v):
 z=iv.mpf(0)
 for c in p[::-1]:z=z*v+c
 return z
def bern_abs(p,A,H):
 n=len(p)-1;c=[]
 for l in range(n+1):
  z=iv.mpf(0)
  for k in range(l,n+1):z+=p[k]*comb(k,l)*A**(k-l)
  c.append(z*H**l)
 vals=[]
 for k in range(n+1):
  z=iv.mpf(0)
  for l in range(k+1):z+=c[l]*comb(k,l)/comb(n,l)
  vals.append(high(abs(z)))
 return max(vals)
S=[1,0,0,0,0,-126,420,-540,315,-70];Q=[None,[-630],[-2520,5040],[-7560,35280,-35280],[-15120,136080,-317520,211680]]
# No critical roots from the first engine enter this method.
raw=json.loads((D/'source/runs/forcing/v22_p9_merged.json').read_text());rows=raw['cells'];total_rows=len(rows);assert args.start>=0 and args.count>=0 and not(args.limit and args.count);end=min(total_rows,args.start+args.count) if args.count else total_rows;rows=rows[args.start:end];rows=rows[:args.limit] if args.limit else rows
rin=F(231,8000);rout=F(297,8000);half=F(33,4000);scale=[b(F(4000,33)**j) for j in range(5)]
fail=[];dist={};inside=0;checks=0
for row in rows:
 d0,d1=map(ff,[row['dmin'],row['dmax']]);assert d0<=d1<100 and d0<rout
 if d1<=rin:
  assert row['T0']>=1 and all(row[k]>=0 for k in ['T1','T2F','TL','TL1','TL2']);inside+=1;checks+=6;continue
 a=max(F(0),(d0-rin)/half);z=min(F(1),(d1-rin)/half);assert 0<=a<=z<=1
 t0=F(1) if not a else high(horner(S,b(a)));assert t0<=ff(row['T0']);checks+=1
 inv=b(1/max(d0,rin));saved={k:ff(row[k]) for k in ['T1','T2F','TL','TL1','TL2']};passed=False
 for nsub in [1,2,4,8,16,32,64]:
  Ts=[iv.mpf(0)]*5;maxs=[F(0)]*5;step=(z-a)/nsub
  for i in range(nsub):
   aa=a+i*step;zz=aa+step;A=b(aa);H=b(step)
   vmax=F(1,4) if aa<=F(1,2)<=zz else max(aa*(1-aa),zz*(1-zz))
   for j in range(1,5):maxs[j]=max(maxs[j],high(b(vmax**(5-j))*b(bern_abs(Q[j],A,H))))
  for j in range(1,5):Ts[j]=b(maxs[j])*scale[j]
  vals=dict(T1=high(Ts[1]),T2F=high(iv.sqrt(Ts[2]**2+(Ts[1]*inv)**2)),TL=high(Ts[2]+Ts[1]*inv),TL1=high(Ts[3]+Ts[2]*inv+Ts[1]*inv**2),TL2=high(Ts[4]+2*Ts[3]*inv+Ts[2]*inv**2+Ts[1]*inv**3))
  if all(vals[k]<=saved[k] for k in vals):passed=True;dist[nsub]=dist.get(nsub,0)+1;break
 checks+=5
 if not passed:fail.append({'key':[row[k] for k in ['ci','q','bs','bp','ks','kp']],'quantities':[k for k in vals if vals[k]>saved[k]]})
out=dict(utc=datetime.now(timezone.utc).isoformat(),status='PASS_V22_SIX_CUTOFF_SECOND_METHOD' if not fail else 'OPEN_FAILURES',rows=len(rows),partial=bool(args.limit or args.count),start_index=args.start,end_index=args.start+len(rows),total_rows=total_rows,checks=checks,inside=inside,subdivisions_used=dist,seconds=time.monotonic()-start,failures=fail[:20],failure_count=len(fail),data_sha256=hashlib.sha256((D/'source/runs/forcing/v22_p9_merged.json').read_bytes()).hexdigest(),method='mpmath.iv70 factored integer polynomial derivatives; exact v(1-v) max; Bernstein convexity with rational subdivisions; no critical-point list',scope='Cutoff fields conditional on saved distances only; not a physical residual forcing norm')
tag='cutoff_iv_sample' if args.limit else (f'cutoff_iv_{args.start:06d}_{end:06d}' if args.count else 'cutoff_iv');(D/'evidence'/f'{tag}.json').write_text(json.dumps(out,indent=2)+'\n');print(out['utc'],out['status'],len(rows),'seconds',out['seconds'],'subdivisions',dist);assert not fail,fail[:2]
