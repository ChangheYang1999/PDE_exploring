from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
from math import comb,factorial
import json,time
from flint import fmpq as Q,fmpq_poly as Poly,arb,ctx
B=Path(__file__).resolve().parents[1];ctx.prec=768;start=time.monotonic()
sha=lambda p:sha256(p.read_bytes()).hexdigest()
ar=lambda q:arb(Q(q).p)/Q(q).q
manifest=json.loads((B/'data/manifest.json').read_text())
for name,item in manifest['source_files'].items():assert sha(B/'source'/name)==item['sha256']

def bern(P,n,a,b):
 assert n>=P.degree() and a<b
 local=P(Poly([a,b-a]))
 return [sum((local[k]*Q(comb(i,k),comb(n,k)) for k in range(min(i,local.degree())+1)),Q(0)) for i in range(n+1)]

def recover(coeff):
 s=Poly([0,1]);n=len(coeff)-1
 return sum((coeff[i]*comb(n,i)*s**i*(1-s)**(n-i) for i in range(n+1)),Poly([]))

def rectangle(path):
 a,b,c,d=map(Q,[0,1,-1,1])
 for ch in path:
  if ch=='t':b=(a+b)/2
  elif ch=='T':a=(a+b)/2
  elif ch=='z':d=(c+d)/2
  elif ch=='Z':c=(c+d)/2
  else:raise AssertionError(ch)
 return a,b,c,d

fixtures=json.loads((B/'source/N4_fixtures.json').read_text())
assert len(fixtures['records'])==20
v=Poly([1,-1]);t=Poly([0,1]);D=(1+624*v)**2*(1+2499*v)**3
fixture_checks=[];point_count=0;coefficient_count=0
for row in fixtures['records']:
 a,b=Q(row['a']),Q(row['b']);kind=row['kind'];factor=Q(-7,3) if kind=='negative_constant' else Q(1)
 P=D*t if kind=='radial_linear' else D*factor
 n=P.degree()+3
 dc=bern(D,n,a,b);pc=bern(P,n,a,b)
 assert all(d>0 for d in dc)
 assert recover(dc)==D(Poly([a,b-a])) and recover(pc)==P(Poly([a,b-a]))
 ratios=[p/d for p,d in zip(pc,dc,strict=True)];coefficient_count+=len(dc)
 if kind in ('one','negative_constant','angular_linear','fractional_power'):assert all(x==factor for x in ratios)
 if kind=='radial_linear':assert min(ratios)>=a and max(ratios)<=b
 for point in row['points']:
  tv,zv=Q(point['t']),Q(point['z'])
  val=ar(tv) if kind=='radial_linear' else ar(zv) if kind=='angular_linear' else ar(1-tv)**ar(Q(1,3)) if kind=='fractional_power' else ar(factor)
  assert val.overlaps(arb(point['value']))
  for key in ('plain_a','correlated_a'):
   if row[key] is not None:
    lo,hi=map(arb,row[key]);assert val.upper()>=lo.lower() and val.lower()<=hi.upper()
  point_count+=1
 fixture_checks.append({'kind':kind,'a':str(a),'b':str(b),'positive_denominator':True,'exact_bernstein_recovery':True,'peer_point_overlaps':True})

# Actual denominator, at both the original and Taylor-elevated degrees.
DA=(1+2499*v)**19
assert DA(1)==1
actual=[]
for a,b in [(Q(0),Q(1)),(Q(0),Q(1,16)),(Q(1,2),Q(3,4)),(Q(15,16),Q(1)),(1-Q(1,2**30),Q(1)),(1-Q(1,2**30),1-Q(1,2**31))]:
 for n in manifest['actual_degrees']:
  ds=bern(DA,n,a,b);assert all(d>0 for d in ds)
  # Compare to degree elevation of the positive factor's product coefficients.
  left,right=1+2499*(1-a),1+2499*(1-b)
  exact=[]
  for i in range(n+1):
   exact.append(sum((Q(comb(19,k)*comb(n-19,i-k),comb(n,i))*left**(19-k)*right**k for k in range(max(0,i-(n-19)),min(19,i)+1)),Q(0)))
  assert ds==exact
  actual.append({'a':str(a),'b':str(b),'n':n,'coefficient_count':len(ds),'positive':True,'independent_elevation_match':True})

# Check Taylor factors at several exact points, including integer-polynomial cases.
taylor=[]
for exponent in [Q(0),Q(1,3),Q(7,3),Q(6),Q(7),Q(8)]:
 a,b=Q(1,4),Q(1,2);mu=(a+b)/2;half=(b-a)/2;fall=Q(1);coeff=[]
 for k in range(7):
  if k:fall*=exponent-k+1
  coeff.append(ar((-1)**k*fall/Q(factorial(k)))*ar(1-mu)**ar(exponent-k))
 E=ar(abs(fall*(exponent-6))*half**7/Q(factorial(7)))*max(ar(1-a)**ar(exponent-7),ar(1-b)**ar(exponent-7))
 for fraction in [Q(0),Q(1,3),Q(1,2),Q(1)]:
  x=a+(b-a)*fraction
  polynomial=sum((coeff[k]*ar(x-mu)**k for k in range(7)),arb(0))
  diff=ar(1-x)**ar(exponent)-polynomial
  if exponent in [Q(0),Q(6)]:assert diff.contains(0) and E==0
  else:assert abs(diff).upper() <= E.upper() or (abs(diff)-E).contains(0)
 taylor.append({'exponent':str(exponent),'points':4,'remainder_verified':True})

cover=json.loads((B/'source/N4_partial_cover.json').read_text())
paths=[r['path'] for r in cover['accepted']]+cover['pending']
assert len(paths)==len(set(paths)) and cover['pending'] and not cover['all_pass']
rects=[rectangle(p) for p in paths]
area=sum(((b-a)*(d-c) for a,b,c,d in rects),Q(0));assert area==2
paircount=0
for i,(a,b,c,d) in enumerate(rects):
 assert Q(0)<=a<b<=1 and Q(-1)<=c<d<=1
 for aa,bb,cc,dd in rects[:i]:
  assert max(a,aa)>=min(b,bb) or max(c,cc)>=min(d,dd)
  paircount+=1
assert all(arb(r['bound'])>=0 and arb(r['denominator_coefficient_lower'])>0 for r in cover['accepted'])
result={'utc':datetime.now(timezone.utc).isoformat(),'precision_bits':ctx.prec,
 'inputs':{str(p.relative_to(B)):sha(p) for p in [Path(__file__),B/'PROOF.md',B/'data/manifest.json']},
 'fixture_checks':fixture_checks,'point_overlap_count':point_count,'fixture_denominator_coefficients':coefficient_count,
 'actual_denominator_checks':actual,'taylor_checks':taylor,
 'partial_cover_snapshot_utc':cover['utc'],'accepted_leaves':len(cover['accepted']),'pending_leaves':len(cover['pending']),
 'exact_area':str(area),'disjoint_pairs_checked':paircount,'whole_plane_bound_established':False,
 'verdict':'CONFIRMED rational range theorem and inspected implementation; actual reconstruction and complete cover remain separate',
 'all_assertions_passed':True,'elapsed_seconds':time.monotonic()-start}
with (B/'verification/result.json').open('x') as f:json.dump(result,f,indent=2);f.write('\n')
print(result['utc'],'fixtures',len(fixture_checks),'points',point_count,'pairs',paircount,'seconds',result['elapsed_seconds'])
