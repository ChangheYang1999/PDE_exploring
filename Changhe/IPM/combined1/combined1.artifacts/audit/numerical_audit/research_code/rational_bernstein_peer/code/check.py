"""Own exact acceptance checks for the independent rational range review."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
from math import comb,factorial
from flint import fmpq as Q,fmpq_poly as Poly,arb,ctx
import json,time
R=Path(__file__).resolve().parents[3];B=R/'research/rational_bernstein_peer';P=R.parent/'c1-t4/research/rational_bernstein_audit';ctx.prec=768
sha=lambda p:sha256(Path(p).read_bytes()).hexdigest();ar=lambda q:arb(Q(q).numerator)/Q(q).denominator

def bern(poly,n,a,b):
 local=poly(Poly([a,b-a]));return [sum((local[k]*Q(comb(i,k),comb(n,k)) for k in range(min(i,local.degree())+1)),Q(0)) for i in range(n+1)]
def recover(rows):
 t=Poly([0,1]);n=len(rows)-1;return sum((p*comb(n,i)*t**i*(1-t)**(n-i) for i,p in enumerate(rows)),Poly([]))
def main():
 tick=time.monotonic();out=B/'verification/result.json';assert not out.exists();inputs={};bindings={};checks={}
 def own(p,h=None):
  p=Path(p);actual=sha(p);assert h is None or actual==h,(str(p),actual,h);inputs[str(p.relative_to(R))]=actual
 def freeze(rel,h=None):
  src=P/rel;blob=src.read_bytes();actual=sha256(blob).hexdigest();assert h is None or actual==h
  dest=B/'source'/rel;dest.parent.mkdir(parents=True,exist_ok=True)
  with dest.open('xb') as f:f.write(blob)
  own(dest,actual);bindings[str(src)]=actual;return json.loads(blob) if src.suffix=='.json' else None
 own(B/'PROOF.md');own(Path(__file__));result=freeze('verification/result.json','41af39a8be9adbc104f312e899557593438dca86aa59224e76d3899d80dcf73d')
 for rel,h in result['inputs'].items():freeze(rel,h)
 manifest=json.loads((B/'source/data/manifest.json').read_text())
 for name,info in manifest['source_files'].items():
  freeze('source/'+name,info['sha256'])
  if name!='N4_partial_cover.json':own(Path(info['source']),info['sha256'])
 own(R/'research/scaled_rational_background_cover/verification/fixtures.json');fixture=json.loads((R/'research/scaled_rational_background_cover/verification/fixtures.json').read_text())
 for rel,h in fixture['inputs'].items():own(R/rel,h)
 checks['peer_scope']=result['all_assertions_passed'] and not result['whole_plane_bound_established'] and result['precision_bits']==768
 checks['fixture_counts']=len(result['fixture_checks'])==fixture['fixture_count']==20 and result['point_overlap_count']==fixture['point_checks']==80 and result['fixture_denominator_coefficients']==184
 for i,row in enumerate(result['fixture_checks']):checks[f'fixture_review{i}']=row['positive_denominator'] and row['exact_bernstein_recovery'] and row['peer_point_overlaps']
 t=Poly([0,1]);D=(1+2499*(1-t))**19;count=0;coeffcount=0;records=[]
 for row in result['actual_denominator_checks']:
  a,b,n=Q(row['a']),Q(row['b']),row['n'];assert n in [103,109] and Q(0)<=a<b<=1;coeffs=bern(D,n,a,b);left,right=1+2499*(1-a),1+2499*(1-b)
  elevated=[sum((Q(comb(19,j)*comb(n-19,i-j),comb(n,i))*left**(19-j)*right**j for j in range(max(0,i-n+19),min(19,i)+1)),Q(0)) for i in range(n+1)]
  assert coeffs==elevated and all(v>0 for v in coeffs);assert recover(coeffs)==D(Poly([a,b-a]));assert row['positive'] and row['independent_elevation_match'] and row['coefficient_count']==len(coeffs)
  records.append({'a':str(a),'b':str(b),'degree':n,'coefficient_count':len(coeffs),'exact_recovery':True,'positive':True});count+=1;coeffcount+=len(coeffs)
 checks['actual_denominator_transforms']=count==12 and coeffcount==1284
 ptcount=0
 for row in fixture['records']:
  assert row['denominator_coefficients_positive']
  for point in row['points']:
   x,z=Q(point['t']),Q(point['z']);kind=row['kind'];val=ar(x) if kind=='radial_linear' else ar(z) if kind=='angular_linear' else ar(1-x)**ar(Q(1,3)) if kind=='fractional_power' else ar(Q(-7,3) if kind=='negative_constant' else 1)
   assert val.overlaps(arb(point['value']))
   for label in ['plain_a','correlated_a']:
    if row[label] is not None:
     lo,hi=map(arb,row[label]);assert val.lower()>=lo.lower() and val.upper()<=hi.upper(),(kind,label,x,val,lo,hi)
   ptcount+=1
 checks['actual_fixture_point_enclosures']=ptcount==80
 tay=[]
 for q in [Q(0),Q(1,3),Q(7,3),Q(6),Q(7),Q(8)]:
  a,b=Q(1,4),Q(1,2);mu=(a+b)/2;h=(b-a)/2;fall=Q(1);coef=[]
  for k in range(7):
   if k:fall*=q-k+1
   coef.append(ar((-1)**k*fall/Q(factorial(k)))*ar(1-mu)**ar(q-k))
  error=ar(abs(fall*(q-6))*h**7/Q(factorial(7)))*max(ar(1-a)**ar(q-7),ar(1-b)**ar(q-7))
  for frac in [Q(0),Q(1,3),Q(1,2),Q(1)]:
   x=a+(b-a)*frac;diff=ar(1-x)**ar(q)-sum((cc*ar(x-mu)**k for k,cc in enumerate(coef)),arb(0))
   if q in [Q(0),Q(6)]:assert diff.contains(0) and error==0
   else:assert abs(diff).upper()<=error.upper() or (abs(diff)-error).contains(0)
  tay.append({'exponent':str(q),'point_count':4,'remainder_check':True})
 checks['Taylor_replay']=len(tay)==len(result['taylor_checks'])==6 and all(row['remainder_verified'] and row['points']==4 for row in result['taylor_checks'])
 partial=json.loads((B/'source/source/N4_partial_cover.json').read_text());paths=[row['path'] for row in partial['accepted']]+partial['pending'];leaves=set(paths);children={}
 assert len(paths)==len(leaves)==247
 for path in paths:
  for k,ch in enumerate(path):assert path[:k] not in leaves;children.setdefault(path[:k],set()).add(ch)
 checks['partial_complete_tree']=len(children)==246 and all(cs in [{'t','T'},{'z','Z'}] for cs in children.values())
 checks['partial_scope']=not partial['all_pass'] and len(partial['accepted'])==result['accepted_leaves']==196 and len(partial['pending'])==result['pending_leaves']==51 and partial['utc']==result['partial_cover_snapshot_utc'] and Q(result['exact_area'])==2 and result['disjoint_pairs_checked']==30381
 checks['partial_lower_bounds']=all(row['pass'] and arb(row['bound']).lower()>=0 and arb(row['denominator_coefficient_lower']).lower()>0 for row in partial['accepted'])
 assert all(checks.values()),{k:v for k,v in checks.items() if not v}
 for rel,h in inputs.items():assert sha(R/rel)==h
 rec={'utc':datetime.now(timezone.utc).isoformat(),'checks':checks,'check_count':len(checks),'inputs':inputs,'peer_bindings':bindings,'peer_result_sha256':sha(B/'source/verification/result.json'),'exact_denominator_records':records,'denominator_coefficient_count':coeffcount,'fixture_point_count':ptcount,'Taylor_records':tay,'partial_cover_utc':partial['utc'],'foreign_code_executed':False,'verdict':'CONFIRMED N4-285 through independent T4-377; actual reconstruction and leaf replay separate','elapsed_seconds':time.monotonic()-tick}
 with out.open('x') as f:json.dump(rec,f,indent=2);f.write('\n')
 print('CONFIRMED',len(checks),'checks',len(bindings),'bindings',sha(out),rec['utc'],'seconds',rec['elapsed_seconds'])
if __name__=='__main__':main()
