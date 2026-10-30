"""Independent integer-index product audit of finite-family L2 floors."""
from pathlib import Path
from fractions import Fraction as Q
from datetime import datetime, timezone
from flint import arb,ctx
import json,hashlib,time,sys
sys.set_int_max_str_digits(0)
ctx.prec=512
ROOT=Path(__file__).resolve().parents[1]
def A(x):
 x=Q(x);return arb(x.numerator)/x.denominator
start=time.monotonic()
p=ROOT/'source/stationary_principal.json';data=json.loads(p.read_text())
target=ROOT/'source/N4_floors.json';old=json.loads(target.read_text())
oldrows={(v['branches'],v['K']):v for v in old['rows']}
delta=1-1/Q(data['cl']);N,D=delta.numerator,delta.denominator
s=Q(1,131072);eta=Q(1,163840)
rows=[];cutoff=None
for B in range(4,9):
 assert D>2*B # prevents any collision of different fractional classes
 E=(arb.pi()*A(sum((Q(x)**2 for x in data['branches'][B-1]['forcing_sin'].values()),Q(0)))).sqrt()
 assert E.overlaps(arb(data['branches'][B-1]['forcing_full_circle_norm']))
 normfactor=(1-A(34*s))*512*E/arb(2).sqrt()
 distance=(arb(D)/((B+1)*N-2*D)).sqrt()
 selected={K for b,K in oldrows if b==B and (B==4 or K==150)}
 maximum=max(selected);count=0;removed=0
 def add(k):
  global distance,count,removed
  for ell in range(1,2*B+1):
   if ell*N+2*D*k<=2*D:continue
   count+=1
   numerator=abs((ell-B-1)*N+2*D*k)
   denominator=(ell+B+1)*N+2*D*(k-2)
   assert denominator>0 and numerator<denominator
   if numerator==0:
    assert ell==B+1 and k==0;removed+=1;continue
   distance*=arb(numerator)/denominator
 for k in range(5):add(k)
 previous=None
 for K in range(maximum+1):
  if K:
   add(2*K+3);add(2*K+4)
  assert removed==1
  if B==4:
   value=normfactor*distance
   if cutoff is None and value<A(eta):
    assert previous is not None and previous>A(eta)
    cutoff={'branches':4,'last_excluded_K':K-1,'first_K_not_excluded_by_this_floor':K,
      'previous_X_lower':previous.str(100),'current_X_lower':value.str(100),
      'threshold':str(eta),'scope':'No inference of feasibility at or above the first nonexcluded K.'}
   previous=value
  if K not in selected:continue
  G0=E*distance/arb(2).sqrt();X=normfactor*distance;ref=oldrows[B,K]
  assert count==ref['power_count']
  checks={key:val.overlaps(arb(ref[key])) for key,val in
          [('power_distance',distance),('L2_lower',G0),('X_lower_at_s2m17',X)]}
  assert all(checks.values()),(B,K,checks)
  assert bool(X>A(eta))==ref['excludes_T4_019_threshold']
  rows.append({'branches':B,'K':K,'power_count':count,'fixed_sector_norm':E.str(80),
     'power_distance':distance.str(80),'L2_lower':G0.str(80),'X_lower_at_s2m17':X.str(80),
     'excludes_T4_019_threshold':bool(X>A(eta)),'N4_interval_overlaps':checks})
  print('B',B,'K',K,'X>=',X.str(20),flush=True)
result={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'precision_bits':ctx.prec,
 'method':'Direct successive products of positive integer ratios, no gamma function; exact coefficient energy.',
 'input_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'N4_target_sha256':hashlib.sha256(target.read_bytes()).hexdigest(),
 'rows':rows,'four_branch_cutoff':cutoff,'elapsed_seconds':time.monotonic()-start}
(ROOT/'verification/reproduction.json').write_text(json.dumps(result,indent=2)+'\n')
print('cutoff',cutoff,'elapsed',result['elapsed_seconds'],flush=True)
