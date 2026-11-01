"""Independently replay and admit all-index period-ten response infima."""
from pathlib import Path
import argparse,json,time
from flint import arb,fmpq,fmpq_poly,ctx
from certificate_admission import read,ref,checkref,reviewed,admit
ap=argparse.ArgumentParser();ap.add_argument('--entry',type=int,required=True);ap.add_argument('--review',required=True);a=ap.parse_args()
t0=time.monotonic();ctx.prec=1536
base=Path('research/292_period_ten_response_infima');v=base/'verification';d=read(v/'checks.json.gz')
assert d['all_checks_pass'] and d['bits']==1024 and len(d['rows'])==14
for item in d['inputs']:checkref(item)
source=Path('research/282_period_ten_symbolic_response/verification')
rec=read(source/'admission.json');assert rec['all_checks_pass'] and rec['root_count']==14
for key in ['evidence','proof','independent_review']:checkref(rec[key])
gen=read(source/'reduced_generic.json.gz');small=read(source/'small_responses.json.gz');fac=read(source/'factors.json')
poly=lambda x:fmpq_poly([fmpq(c) for c in x])
N=[poly(x) for x in gen['numerator_by_b_degree']];D=poly(gen['denominator']);limit=poly(fac['limit_coefficients'])
assert len(N)==11 and D.degree()==109 and D[109]==1
assert limit==fmpq_poly([col[109] for col in N])
small={x['k']:poly(x['coefficients']) for x in small['small']}
roots=read('research/281_period_ten_finite_algebra/verification/obstruction_checks.json')['real_roots']
def ev(p,I):
 y=arb(0)
 for c in reversed(list(p)):y=y*I+arb(c)
 return y
def fixed(k):
 if k in small:return small[k]
 dv=D(k);assert dv>0
 return fmpq_poly([col(k)/dv for col in N])
shiftcache={};counts=dict(positive=0,exact_zero=0,finite_strict=0,defining_equalities=0);indices=[];values=[]
for i,(row,root) in enumerate(zip(d['rows'],roots),1):
 assert row['root_index']==i and row['root_interval']==root['interval']
 lo,hi=map(fmpq,root['interval']);I=arb(lo).union(arb(hi));k=row['candidate_index'];K=row['K'];sign=row['tail_sign']
 assert sign in [-1,1] and K>=21 and (k is None or 2<=k<K) and row['attained']==(k is not None)
 T=poly(row['target_polynomial']);c=limit if k is None else fixed(k)
 cval=ev(c,I);assert cval>0 or cval<0
 assert T==(c if cval>0 else -c)
 tv=ev(T,I);lv=ev(limit,I);assert tv>0 and sign*lv>0 and tv.overlaps(arb(row['infimum']))
 if k is not None:assert abs(lv)>tv
 if K not in shiftcache:
  arg=fmpq_poly([K,1]);DD=D(arg);NN=[col(arg) for col in N]
  assert DD.degree()==109 and all(c>0 for c in DD)
  shiftcache[K]=(NN,DD)
 NN,DD=shiftcache[K]
 assert [x['degree'] for x in row['tail_coefficients']]==list(range(110))
 zeros=[]
 for j,stored in enumerate(row['tail_coefficients']):
  P=fmpq_poly([sign*col[j]-T[m]*DD[j] for m,col in enumerate(NN)])
  assert stored['exact_zero']==(not bool(P))
  if P:
   val=ev(P,I);assert val>0 and val.overlaps(arb(stored['enclosure']));counts['positive']+=1
  else:
   assert arb(stored['enclosure']).is_zero();zeros.append(j);counts['exact_zero']+=1
 assert zeros==([109] if k is None else [])
 assert [x['k'] for x in row['finite_checks']]==list(range(2,K))
 for item in row['finite_checks']:
  kk=item['k'];p=fixed(kk);value=ev(p,I);assert value>0 or value<0
  s=1 if value>0 else -1;assert s==item['sign']
  gap=s*p-T;gv=ev(gap,I);assert gv.overlaps(arb(item['gap']))
  assert item['candidate']==(kk==k)
  if kk==k:assert not gap;counts['defining_equalities']+=1
  else:assert gv>0;counts['finite_strict']+=1
 indices.append(k);values.append(tv.str(35))
review=reviewed(base,a.review)
replay=v/'replay.json';replay.write_text(json.dumps(dict(all_checks_pass=True,bits=1536,counts=counts,indices=indices,infima=values,source=ref(v/'checks.json.gz'),actual_elapsed_s=time.monotonic()-t0),indent=2)+'\n')
indextext=', '.join('limit' if k is None else str(k) for k in indices)
result=f'The fourteen ordered roots have global minimizing indices [{indextext}], where limit means a positive nonattained limiting infimum. Exact shifted-polynomial positivity and all smaller integer comparisons pass. A separate1536-bit replay reconstructs every comparison polynomial: {counts["positive"]} positive tail coefficients, {counts["exact_zero"]} exact zero leading coefficients, {counts["finite_strict"]} strict finite comparisons and {counts["defining_equalities"]} defining equalities. Producer computation took{d["actual_elapsed_s"]:.6f}seconds and the independent algebraic replay took{time.monotonic()-t0:.6f}seconds.'
admit(base,a.entry,'Exact global period-ten response infima','The response modulus at each of the fourteen fixed algebraic roots has the stated global minimum or nonattained infimum.','Use the exact response identity282, its isolated compatibility roots281, and the polynomial comparison criterion of292. Independently reconstruct the shifted denominator and every signed numerator difference at1536 bits, then check all finite indices below the tail cutoff.',result,'The global response-infimum statement is PROVED. Neither tail monotonicity, an eventual coefficient growth rate nor a sharp exterior radius is asserted.',v/'checks.json.gz',review,dict(replay=ref(replay),symbolic_admission=ref(source/'admission.json'),indices=indices,counts=counts))
lines=['# Global period-ten response infima','',f'PROVED in V{a.entry}. Unit leading amplitude. Directed enclosures are shown below; the exact algebraic definitions are in PROOF.md.','','| Root | Global minimizing index | Infimum of modulus |','|---|---:|---|']
for i,(k,value) in enumerate(zip(indices,values),1):lines.append(f'| {i} | {k if k is not None else "Not attained; limit"} | {value} |')
(v/'INFIMA.md').write_text('\n'.join(lines)+'\n')
(base/'sources/admit_period_ten_infima.py').write_bytes(Path(__file__).read_bytes())
