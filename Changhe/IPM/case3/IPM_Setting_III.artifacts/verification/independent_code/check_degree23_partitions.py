"""Two independent complete integer-partition enumerations and lemma witnesses."""
from pathlib import Path
from datetime import datetime,timezone
from collections import Counter
from fractions import Fraction
import json
from degree23_inputs import ROOT as R,VERIFY as V,load,certificate,sha
checks=[]
def ck(n,b,e=None):checks.append(dict(name=n,passed=bool(b),evidence=e))
def slots(total,length,least=1):
 if length==0:
  if total==0:yield()
  return
 for a in range(least,total//length+1):
  for rest in slots(total-a,length-1,a):yield(a,)+rest

def counts(total,part):
 if part==0:
  if total==0:yield()
  return
 for k in range(total//part+1):
  for rest in counts(total-k*part,part-1):yield rest+(part,)*k

def structural(mu):
 sizes=sorted(Counter(mu).values())
 if len(sizes)==2:
  if sizes[0]==1:return'exceptional_remaining'
  if sizes[0]==2 and sizes[1]>=3:return'I'
  if sizes==[3,3]:return'III'
  if sizes==[3,4]:return'V'
  if sizes==[3,5]:return'V5'
 if len(sizes)==3:
  if sizes[:2]==[1,1]:return'II'
  if sizes==[1,2,2]:return'IV'
  if sizes==[1,2,3]:return'VI'
  if sizes==[1,2,4]:return'VI4'
 return'UNCLASSIFIED'
a=[];b=[]
for A in range(1,24,2):
 total=(23-A)//2
 for k in range(3,total+1):a.extend((A,mu)for mu in slots(total,k))
 b.extend((A,mu)for mu in counts(total,total)if len(mu)>=3)
ck('two complete enumerations agree',sorted(a)==sorted(b));ck('both enumerations duplicate free',len(a)==len(set(a))and len(b)==len(set(b)));ck('153patterns',len(a)==153)
rows=[];survivors=[]
for A,mu in a:
 classes=Counter(mu);reason=None;witness={}
 ck('hypotheses '+str((A,mu)),A>0 and A%2==1 and A+2*sum(mu)==23 and len(mu)>=3 and tuple(sorted(mu))==mu)
 if len(classes)==1:reason='equal'
 elif len(classes)==2:
  singletons=[v for v,k in classes.items()if k==1]
  if len(singletons)==1:
   nu=singletons[0];common=next(v for v in classes if v!=nu)
   if nu>common:reason='exceptional_larger'
   elif A>=3 or common-nu<=1:reason='exceptional_smaller'
   witness=dict(singleton_multiplicity=nu,repeated_multiplicity=common)
 if reason is None and sum(k%2 for k in classes.values())>=3:reason='three_odd_classes';witness=dict(odd_classes=sum(k%2 for k in classes.values()))
 if reason is None and sorted(classes.values())==[2,2]:
  aa,bb=[2*q for q in sorted(classes)];margin=(25*A-23)*(aa+bb)-aa*bb
  if A>=3 or min(aa,bb)==2:
   ck('strict two-pair margin '+str((A,mu)),margin>0,margin);reason='two_pairs';witness=dict(minimum_T=25*A-23,weights=[aa,bb],strict_margin=margin)
 row=dict(A0=A,mu=list(mu),e=len(mu)-1,type=reason or structural(mu),excluded_by_lemma=reason is not None,witness=witness,id='_'.join(map(str,[A,*reversed(mu)])))
 if reason is None:survivors.append(row);ck('all survivors structurally covered '+row['id'],row['type']!='UNCLASSIFIED')
 rows.append(row)
ext=load('d23/certificates/enumeration.json');key=lambda r:(r['A0'],tuple(sorted(r['mu'])));ours={key(q):q for q in rows};theirs={key(q):q for q in ext['all_patterns']}
ck('full pattern bijection',len(theirs)==len(ext['all_patterns'])==153 and ours.keys()==theirs.keys());ck('d/counts',ext['d']==23 and ext['total']==153 and ext['survivor_count']==49)
for k,q in ours.items():
 other=theirs[k];ck('full classification '+q['id'],all(q[name]==other[name]for name in ['type','e','excluded_by_lemma','id']))
expected={'equal':13,'exceptional_larger':47,'exceptional_smaller':11,'three_odd_classes':29,'two_pairs':4,'I':12,'II':22,'III':1,'IV':5,'V':2,'VI':4,'V5':1,'VI4':1,'exceptional_remaining':1};actual=dict(Counter(q['type']for q in rows));ck('all classification counts',actual==expected,actual)
ck('49unique survivors',len(survivors)==49 and len({key(q)for q in survivors})==49 and {key(q)for q in survivors}=={key(q)for q in ext['survivors']})
e_counts={e:[sum(q['e']==e for q in rows),sum(q['e']==e for q in survivors)]for e in range(2,11)};ck('all e counts',e_counts=={2:[41,1],3:[38,17],4:[29,10],5:[19,12],6:[12,5],7:[7,3],8:[4,1],9:[2,0],10:[1,0]},e_counts)
for q in survivors:
 cert=certificate(q['id']);p=cert['pattern'];ck('coefficient certificate identity '+q['id'],all(q[n]==p[n]for n in ['A0','e','type','id'])and tuple(sorted(p['mu']))==tuple(q['mu'])and cert['type']==('exceptional'if q['type']=='exceptional_remaining'else q['type']))
ck('two-pair formerly surviving tuple excluded',ours[(3,(2,2,3,3))]['type']=='two_pairs');ck('conditional corollary arithmetic',23+2==25 and Fraction(1)+Fraction(25,2)==Fraction(27,2))
for path in ['research/report79_new_lemma_audit/verification/FINAL_BINDINGS.json','research/degree21_grouped_moment_obstruction/verification/FINAL_BINDINGS.json']:
 d=json.loads(Path(path).read_text())
 if 'status'in d:ck('dependency PASS '+path,d['status']=='PASS')
 else:
  g=json.loads(Path('research/report79_new_lemma_audit/verification/LEMMA_CHECKS.json').read_text());ck('lemma5307PASS',g['status']=='PASS'and g['count']==5307 and all(c['passed']for c in g['checks']))
 for record in d.get('files',[])+d.get('bindings',[]):
  ck('dependency binding '+record['path'],sha(record['path'])==record['sha256'])
(V/'PARTITIONS.json').write_text(json.dumps(rows,indent=2)+'\n')
out=dict(status='PASS'if all(c['passed']for c in checks)else'FAIL',utc=datetime.now(timezone.utc).isoformat(),count=len(checks),checks=checks,survivors=survivors,e_counts=e_counts,inputs_sha256=sha(V/'INPUTS.json'),reader_sha256=sha('independent_code/degree23_inputs.py'),driver_sha256=sha(__file__),proof_sha256=sha(R/'PROOF.md'),scope='Complete enumeration/filter application only. Remaining algebra and fullplane problem OPEN.')
(V/'PARTITION_CHECKS.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'],len(checks));print([c for c in checks if not c['passed']]);raise SystemExit(out['status']!='PASS')
