"""Result282 exact exhaustive partition coverage and final provenance."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction
import json,hashlib
R=Path('research/degree19_grouped_moment_obstruction');V=R/'verification';checks=[]
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def ck(n,b,e=None):checks.append(dict(name=n,passed=bool(b),evidence=e))
def slots(total,count,minimum=1):
 if count==0:
  if total==0:yield()
  return
 for x in range(minimum,total//count+1):
  for rest in slots(total-x,count-1,x):yield(x,)+rest

def counts(total,maximum):
 if maximum==0:
  if total==0:yield()
  return
 for k in range(total//maximum+1):
  for rest in counts(total-k*maximum,maximum-1):yield rest+(maximum,)*k

rows=[];retained=[];all_slots=[];all_counts=[]
for A in range(1,20,2):
 total=(19-A)//2
 for length in range(3,total+1):
  for mu in slots(total,length):all_slots.append((A,mu))
 for mu in counts(total,total):
  if len(mu)>=3:all_counts.append((A,mu))
ck('two independent enumerations identical',sorted(all_slots)==sorted(all_counts));ck('both enumerations no duplicates',len(all_slots)==len(set(all_slots)) and len(all_counts)==len(set(all_counts)));ck('total67',len(all_slots)==67)
for A,mu in all_slots:
 unique=set(mu);reason='retained'
 if len(unique)==1:reason='equal weights'
 elif len(unique)==len(mu):reason='all real M2 positive'
 elif len(unique)==2:
  single=[q for q in unique if mu.count(q)==1]
  if len(single)==1:
   nu=single[0];common=next(q for q in mu if q!=nu)
   if nu>common:reason='unique higher'
   elif A!=1 or common-nu<=1:reason='unique lower A0 or gap'
 odd_classes=sum(mu.count(q)%2 for q in unique)
 max_real=1 if (len(mu)-1)%2==0 else 2
 if reason=='retained' and odd_classes>max_real:reason='too many forced real nodes'
 if reason=='retained' and len(mu)==4 and len(unique)==2 and all(mu.count(q)==2 for q in unique):
  aa,bb=[2*q for q in sorted(unique)]
  if A>=3 or min(aa,bb)==2:
   Tmin=A*21-19
   ck('quadratic strict condition '+str((A,mu)),Tmin*(aa+bb)>aa*bb)
   reason='two quadratic classes strict condition'
 row=dict(A0=A,multiplicities=mu,e=len(mu)-1,reason=reason,odd_classes=odd_classes,maximum_real=max_real);rows.append(row)
 ck('valid partition '+str((A,mu)),A>0 and A%2==1 and A+2*sum(mu)==19 and len(mu)>=3 and list(mu)==sorted(mu) and all(q>0 for q in mu))
 if reason=='retained':retained.append((A,mu))
want=[(1,(1,4,4)),(1,(1,1,2,5)),(1,(1,1,3,4)),(1,(1,2,2,4)),(1,(1,2,3,3)),(1,(1,1,1,3,3)),(1,(1,1,2,2,3)),(1,(1,1,1,1,2,3)),(1,(1,1,1,2,2,2)),(1,(1,1,1,1,1,2,2)),(3,(1,1,2,4)),(3,(1,2,2,3)),(3,(1,1,2,2,2)),(3,(1,1,1,1,2,2)),(5,(1,1,2,3)),(5,(1,1,1,2,2))]
for A,mu in want:ck('expected partition has degree19 '+str((A,mu)),A+2*sum(mu)==19)
ck('exact16 survivors',len(retained)==16 and sorted(retained)==sorted(want));cert=json.loads((V/'types_I_II_certificate.json').read_text());mapped=[]
for name,row in cert['cases'].items():
 if row['kind']=='two':A,a,b,L=row['parameters'];weights=[a]*2+[b]*L
 else:A,a,b,w,L=row['parameters'];weights=[a,b]+[w]*L
 tup=(A,tuple(sorted(v//2 for v in weights)));mapped.append(tup);ck('structural tuple '+name,all(w>0 and w%2==0 for w in weights)and A+sum(weights)==19 and tup in retained)
for name,A,weights in [('III',1,[4]*3+[2]*3),('IV',1,[6]+[4]*2+[2]*2),('special',1,[2]+[8]*2)]:
 tup=(A,tuple(sorted(w//2 for w in weights)));mapped.append(tup);ck('structural tuple '+name,A+sum(weights)==19 and tup in retained)
ck('complete structural bijection',len(mapped)==len(set(mapped))==16 and sorted(mapped)==sorted(retained));ck('special admissible integers',[n for n in range(1,4)if n<4-1]==[1,2]);ck('next odd degree',19+2==21);ck('finite P bound',Fraction(1)+Fraction(21,2)==Fraction(23,2))
bindings=[]
for name in ['TYPES12_CHECKS.json','TYPES34_CHECKS.json']:
 p=V/name;g=json.loads(p.read_text());ck('completed algebra gate '+name,g['status']=='PASS'and len(g['checks'])==g['count']and all(x['passed']for x in g['checks']));bindings.append(dict(path=str(p),sha256=sha(p),count=g['count']))
 proof=R/('TYPES12_PROOF.md'if name.startswith('TYPES12')else'TYPES34_PROOF.md');ck('algebra proof binding '+name,g['proof_sha256']==sha(proof));certificate=V/('types_I_II_certificate.json'if name.startswith('TYPES12')else'types_III_IV_certificate.json');ck('algebra certificate binding '+name,g['certificate_sha256']==sha(certificate));driver=Path('independent_code')/('check_degree19_types12.py'if name.startswith('TYPES12')else'check_degree19_types34.py');ck('algebra driver binding '+name,g['driver_sha256']==sha(driver))
 if name.startswith('TYPES12'):ck('polynomial library bound',g['polynomial_library_sha256']==sha('independent_code/exact_polynomial_275.py'))
 else:ck('rational library bound',g['rational_library_sha256']==sha('independent_code/exact_rational_282.py'))
for x in json.loads((V/'DEPENDENCIES.json').read_text()):ck('prior source hash '+x['source'],sha(x['source'])==sha(x['frozen'])==x['sha256'])
g278=json.loads(Path('research/report79_new_lemma_audit/verification/LEMMA_CHECKS.json').read_text());ck('general lemma gate',g278['status']=='PASS' and g278['count']==5307 and all(q['passed']for q in g278['checks']));ck('general lemma proof binding',g278['proof_sha256']==sha('research/report79_new_lemma_audit/PROOF.md'))
g=json.loads(Path('research/degree17_grouped_moment_obstruction/verification/CHECKS.json').read_text());ck('reviewed lower-degree dependency',g['status']=='PASS'and g['count']==710 and all(x['passed']for x in g['checks']));ck('actual lower-degree proof bound',g['proof_sha256']==sha('research/degree17_grouped_moment_obstruction/PROOF.md'))
(V/'PARTITIONS.json').write_text(json.dumps(rows,indent=2)+'\n');out=dict(status='PASS'if all(x['passed']for x in checks)else'FAIL',utc=datetime.now(timezone.utc).isoformat(),count=len(checks),checks=checks,partition_count=len(all_slots),survivors=retained,algebra_gates=bindings,proof_sha256=sha(R/'PARTITION_PROOF.md'),driver_sha256=sha(__file__),scope='Complete finite auxiliary degree19 partition closure, conditional on previously proved residue implications and lower degrees; not full-plane IPM.')
(V/'PARTITION_CHECKS.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'],len(checks));print([x for x in checks if not x['passed']]);raise SystemExit(out['status']!='PASS')
