"""All cutoff fields via exact rational Bernstein subdivisions and squared Hessian."""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
from math import comb
import argparse,json,time,hashlib,math
D=Path(__file__).resolve().parents[1];tic=time.monotonic()
ap=argparse.ArgumentParser();ap.add_argument('--start',type=int,default=0);ap.add_argument('--count',type=int,default=0);args=ap.parse_args()
p=D/'source/runs/forcing/v22_p9_merged.json';digest=hashlib.sha256(p.read_bytes()).hexdigest();assert digest=='b5f597c90a0928dd9a5ea87af12953bcc33f46321ef60c3d5b014d9bef3a7201'
raw=json.loads(p.read_text());assert args.start>=0 and args.count>=0
end=min(len(raw['cells']),args.start+args.count) if args.count else len(raw['cells']);rows=raw['cells'][args.start:end]
def q(x):assert math.isfinite(x);return Q.from_float(float(x))
def horner(p,x):
 z=Q(0)
 for v in p[::-1]:z=z*x+v
 return z
def bern_abs(p,a,h):
 n=len(p)-1;c=[]
 ap=[Q(1)];hp=[Q(1)]
 for k in range(n):ap.append(ap[-1]*a);hp.append(hp[-1]*h)
 for l in range(n+1):c.append(hp[l]*sum((p[k]*comb(k,l)*ap[k-l] for k in range(l,n+1)),Q(0)))
 return max(abs(sum((c[l]*Q(comb(i,l),comb(n,l)) for l in range(i+1)),Q(0))) for i in range(n+1))

S=[1,0,0,0,0,-126,420,-540,315,-70]
polys=[S]
for j in range(1,5):polys.append([k*polys[-1][k] for k in range(1,len(polys[-1]))])
rin=Q(231,8000);rout=Q(297,8000);half=Q(33,4000);scale=[half**(-j) for j in range(5)]
fields=['T0','T1','T2F','TL','TL1','TL2'];counts={};inside=0;checks=0;fail=[]
for row in rows:
 d0,d1=q(row['dmin']),q(row['dmax']);assert d0<=d1 and d1>=0 and d0<rout
 saved={k:q(row[k]) for k in fields};assert min(saved.values())>=0
 if d1<=rin:
  assert saved['T0']>=1;inside+=1;checks+=6;continue
 a=max(Q(0),(d0-rin)/half);z=min(Q(1),(d1-rin)/half);assert 0<=a<=z<=1
 assert horner(S,a)<=saved['T0'];checks+=1
 inv=1/max(d0,rin);passed=False
 for nsub in (1,2,4,8,16,32,64,128):
  step=(z-a)/nsub;maxs=[Q(0)]*5
  for i in range(nsub):
   aa=a+i*step;zz=aa+step
   for j in range(1,5):maxs[j]=max(maxs[j],bern_abs(polys[j],aa,step))
  t=[maxs[j]*scale[j] for j in range(5)]
  vals={'T1':t[1],'TL':t[2]+t[1]*inv,'TL1':t[3]+t[2]*inv+t[1]*inv**2,'TL2':t[4]+2*t[3]*inv+t[2]*inv**2+t[1]*inv**3}
  hess2=t[2]**2+(t[1]*inv)**2
  if all(vals[k]<=saved[k] for k in vals) and hess2<=saved['T2F']**2:
   passed=True;counts[nsub]=counts.get(nsub,0)+1;break
 checks+=5
 if not passed:fail.append(dict(key=[row[k] for k in ['ci','q','bs','bp','ks','kp']],linear_failures=[k for k in vals if vals[k]>saved[k]],hessian_failure=hess2>saved['T2F']**2))
assert len(raw['cells'])==43949
out=dict(utc=datetime.now(timezone.utc).isoformat(),seconds=time.monotonic()-tic,status='PASS_V22_SIX_CUTOFF_FULL_POLYNOMIAL_BERNSTEIN' if not fail else 'OPEN_CUTOFF_EXACT_FAILURES',data_sha256=digest,start_index=args.start,end_index=end,total_rows=len(raw['cells']),rows=len(rows),checks=checks,inside=inside,subdivisions_used=counts,failures=fail[:30],failure_count=len(fail),partial=bool(args.start or args.count),method='Exact rational full derivative polynomials and Bernstein coefficients, rational subdivisions, squared Frobenius comparison; no algebraic critical points or floating arithmetic',scope='Six cutoff fields only on previously independently checked physical distance intervals. No residual or composed forcing bound.')
tag=f'cutoff_full_bernstein_{args.start:06d}_{end:06d}'
(D/'evidence'/f'{tag}.json').write_text(json.dumps(out,indent=2)+'\n');print(out['utc'],out['status'],'rows',len(rows),'checks',checks,'seconds',out['seconds'],'subdivisions',counts,flush=True);assert not fail,fail[:2]
