"""Direct positive integer products for the two new B4 cutoffs; independent point arithmetic."""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime,timezone
from hashlib import sha256
from flint import arb,ctx
import json,time,sys
sys.set_int_max_str_digits(0);ctx.prec=512
root=Path(__file__).resolve().parents[1];start=time.monotonic()
def A(v):
 v=Q(v);return arb(v.numerator)/v.denominator
src=root.parent/'finite_family_l2_audit/source/stationary_principal.json'
dat=json.loads(src.read_text());delta=1-1/Q(dat['cl']);N,D=delta.numerator,delta.denominator
B=4;assert D>2*B
E=(arb.pi()*A(sum((Q(v)**2 for v in dat['branches'][B-1]['forcing_sin'].values()),Q(0)))).sqrt()
factor=E/arb(2).sqrt();distance=(arb(D)/(5*N-2*D)).sqrt()
cases={'sharp':(512,Q(76219,10**9)), 'sharpw':(1024,Q(4207,20*10**6))}
cutoffs={};previous={};count=0
def include(k):
 global distance,count
 for ell in range(1,9):
  if ell*N+2*D*k<=2*D:continue
  count+=1
  num=abs((ell-5)*N+2*D*k);den=(ell+5)*N+2*D*(k-2)
  assert 0<=num<den
  if num:distance*=arb(num)/den
for k in range(5):include(k)
for K in range(30001):
 if K:
  include(2*K+3);include(2*K+4)
 g0=factor*distance
 for name,(weight,eta) in cases.items():
  ratio=weight*g0/A(eta)
  if name not in cutoffs and ratio<1:
   assert previous[name]>1
   cutoffs[name]={'last_excluded_K':K-1,'first_inconclusive_K':K,'last_ratio':previous[name].str(100),
    'next_ratio':ratio.str(100),'threshold':str(eta),'raw_G0_threshold':str(eta/weight)}
  previous[name]=ratio
 if len(cutoffs)==len(cases):break
assert len(cutoffs)==2
wsrc=root.parent/'symmetry_point_witness/source/N4_cartesian_witnesses.json'
wits=json.loads(wsrc.read_text())['rows'];points=[]
for name,den,r in [('sharp',7744,Q(147,200000)),('sharpw',5184,Q(1351,10**6))]:
 s=arb(1)/den;c1r=A(r)/(4*(arb.pi()*s*(1+s)).sqrt());c0r=A(r)/(2*(arb.pi()*(1+s)).sqrt())
 for row in wits:
  f=row['fields'];F=abs(arb(f['residual']));V=arb(f['velocity_norm']);dr=arb(f['gradient_norm'])
  gap=F-c1r*V-c0r*(1+dr)-c1r*c0r
  points.append({'framework':name,'candidate':row['candidate'],'point':row['point'],'gap':gap.str(100),'excludes':bool(gap>0)})
out={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'method':'Direct integer-ratio products and exact coefficient energy, Arb512; no onset approximation',
 'comparison':'X_(s,w)(F) >= sqrt(w2) ||F||_2, with no fractional comparison loss',
 'scope':'B4 finite generator family from T4-025, all four exact stationary leaders, m<=k<=K. Next degree is inconclusive, not feasible.',
 'fixed_sector_norm':E.str(100),'cutoffs':cutoffs,'points':points,
 'source_sha256':sha256(src.read_bytes()).hexdigest(),'witness_sha256':sha256(wsrc.read_bytes()).hexdigest(),
 'code_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),'elapsed_seconds':time.monotonic()-start}
(root/'verification/floors_and_points.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(cutoffs,indent=2))
for p in points:print(p['framework'],p['candidate'],p['gap'][:45])
print('elapsed',out['elapsed_seconds'])
