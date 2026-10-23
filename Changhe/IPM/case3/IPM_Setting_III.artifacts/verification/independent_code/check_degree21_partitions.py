"""Our two independent finite enumerations and structural classification."""
from pathlib import Path
from datetime import datetime,timezone
from collections import Counter
from fractions import Fraction
import json,hashlib
R=Path('research/degree21_grouped_moment_obstruction');V=R/'verification';E=V/'external';checks=[];sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def ck(n,b,e=None):checks.append(dict(name=n,passed=bool(b),evidence=e))
def slots(total,length,least=1):
 if length==0:
  if total==0:yield()
  return
 for first in range(least,total//length+1):
  for rest in slots(total-first,length-1,first):yield(first,)+rest

def mults(total,part):
 if part==0:
  if total==0:yield()
  return
 for count in range(total//part+1):
  for rest in mults(total-count*part,part-1):yield rest+(part,)*count

def classify(mu):
 c=sorted(Counter(mu).values())
 if len(c)==2:
  if c[0]==1:return'exception'
  if c==[2,2]:return'two_pairs'
  if c[0]==2:return'I'
  if c==[3,3]:return'III'
  if c==[3,4]:return'V'
 elif len(c)==3:
  if c[:2]==[1,1]:return'II'
  if c==[1,2,2]:return'IV'
  if c==[1,2,3]:return'VI'
 return'UNCLASSIFIED'
Aset=[];Bset=[]
for A in range(1,22,2):
 total=(21-A)//2
 for length in range(3,total+1):Aset.extend((A,mu)for mu in slots(total,length))
 Bset.extend((A,mu)for mu in mults(total,total)if len(mu)>=3)
ck('complete enumerations identical',sorted(Aset)==sorted(Bset));ck('no duplicates',len(Aset)==len(set(Aset))and len(Bset)==len(set(Bset)));ck('total103',len(Aset)==103)
rows=[];survivors=[]
for A,mu in Aset:
 counts=Counter(mu);reason=None;witness={};ck('valid '+str((A,mu)),A>0 and A%2==1 and A+2*sum(mu)==21 and len(mu)>=3 and tuple(sorted(mu))==mu)
 if len(counts)==1:reason='equal'
 elif len(counts)==2:
  ones=[v for v,c in counts.items()if c==1]
  if len(ones)==1:
   nu=ones[0];common=next(v for v in counts if v!=nu)
   if nu>common or A>=3 or common-nu<=1:reason='one_exception';witness=dict(nu=nu,common=common)
 if reason is None and sum(c%2 for c in counts.values())>2:reason='real_node_bound';witness=dict(odd_classes=sum(c%2 for c in counts.values()))
 if reason is None and sorted(counts.values())==[2,2]:
  a,b=[2*q for q in sorted(counts)];margin=(23*A-21)*(a+b)-a*b
  if A>=3 or min(a,b)==2:ck('strict two-pair condition '+str((A,mu)),margin>0,margin);reason='two_pairs';witness=dict(margin=margin)
 row=dict(A0=A,mu=list(mu),e=len(mu)-1,filter=reason,witness=witness)
 if reason is None:row['type']=classify(mu);survivors.append(row);ck('structural class '+str((A,mu)),row['type']!='UNCLASSIFIED')
 rows.append(row)
counts=Counter(row['filter']or'survivor'for row in rows);expected=dict(equal=12,one_exception=41,real_node_bound=18,two_pairs=3,survivor=29);ck('exact filter counts',dict(counts)==expected,dict(counts));kinds=Counter(r['type']for r in survivors);ck('exact structural counts',dict(kinds)==dict(I=8,II=12,III=1,IV=3,V=1,VI=1,exception=2,two_pairs=1),dict(kinds))
ext=json.loads((E/'enumeration.json').read_text());key=lambda r:(r['A0'],tuple(sorted(r['mu'])));ours={key(r):r for r in rows};theirs={key(r):r for r in ext['all_patterns']};ck('external full set not just counts',ours.keys()==theirs.keys() and len(theirs)==len(ext['all_patterns'])==103)
for key_,row in ours.items():ck('source reason '+str(key_),row['filter']==theirs[key_]['filter'])
ck('external counts match',ext['total']==103 and ext['d']==21 and ext['filter_counts']==expected);certs=[]
for i in range(1,30):
 p=E/f'certificate_{i:02d}.json';s=json.loads(p.read_text());pat=s['pattern'];key_=key(pat);certs.append(key_);own=ours.get(key_);ck('certificate coverage '+str(i),own is not None and own['filter']is None and own['type']==pat['type']and own['e']==pat['e'],pat)
ck('certificate bijection',len(certs)==len(set(certs))==29 and set(certs)=={key(r)for r in survivors});ck('omitted tuple included',(7,(1,1,1,2,2))in certs);ck('generic patterns26',sum(kinds[k]for k in ['I','II','III','IV','V','VI'])==26);ck('next odd degree andP',21+2==23 and Fraction(1)+Fraction(23,2)==Fraction(25,2))
for rel in ['research/report79_new_lemma_audit/verification/FINAL_BINDINGS.json','research/degree19_grouped_moment_obstruction/verification/FINAL_BINDINGS.json']:
 d=json.loads(Path(rel).read_text())
 if 'status'in d:ck('dependencyPASS '+rel,d['status']=='PASS')
 else:
  actual=json.loads(Path('research/report79_new_lemma_audit/verification/LEMMA_CHECKS.json').read_text());ck('dependency actual lemmaPASS',actual['status']=='PASS'and actual['count']==5307 and all(c['passed']for c in actual['checks']))
 for row in d['files']:ck('dependency hash '+row['path'],sha(row['path'])==row['sha256'])
(V/'PARTITIONS.json').write_text(json.dumps(rows,indent=2)+'\n');out=dict(status='PASS'if all(c['passed']for c in checks)else'FAIL',utc=datetime.now(timezone.utc).isoformat(),count=len(checks),checks=checks,partition_count=103,survivors=survivors,source_sha256=sha(E/'enumeration.json'),proof_sha256=sha(R/'PARTITION_PROOF.md'),driver_sha256=sha(__file__),scope='Coverage only. Degree21 algebra still has separate gates; fullplane UNRESOLVED.')
(V/'PARTITION_CHECKS.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'],len(checks));print([c for c in checks if not c['passed']]);raise SystemExit(out['status']!='PASS')
