"""Bind exact finite diagnostics and the narrowly scoped reviewed proof."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
R=Path('research/angular_collocation_kernel_audit');V=R/'verification';root=Path.cwd();checks=[];bindings={}
def ck(n,b):
 checks.append(dict(name=n,passed=bool(b)))
 if not b:raise AssertionError(n)
def bind(p,h=None):
 p=Path(p);p=p.relative_to(root)if p.is_absolute()else p
 s=hashlib.sha256(p.read_bytes()).hexdigest();ck('binding '+str(p),h is None or s==h);bindings[str(p)]=s;return p
for p in [__file__,R/'PROOF.md',R/'REVIEW_RESOLUTION_PROOF.md']:bind(p)
g=json.loads(bind(V/'CHECKS.json').read_text());ck('240 finite arithmetic checks',g['status']=='PASS_EXACT_FINITE_FORMULA_CHECKS'and g['count']==len(g['checks'])==240 and all(c['passed']for c in g['checks']))
for p,h in g['bindings'].items():bind(p,h)
for name in ['request.txt','response.json','metadata.json','answer.md']:bind(V/'opus_scope'/name)
m=json.loads((V/'opus_scope/metadata.json').read_text());r=json.loads((V/'opus_scope/response.json').read_text());a=(V/'opus_scope/answer.md').read_text();q=(V/'opus_scope/request.txt').read_text()
ck('actual Opus5.5 completed',m['returned_model']==r['model']=='claude-opus-5-5'and m['stop_reason']==r['stop_reason']=='end_turn'and m['answer_nonempty'])
ck('answer matches returned payload',a.strip()=='\n\n'.join(c['text']for c in r['content']if c['type']=='text').strip());ck('request bound',hashlib.sha256(q.encode()).hexdigest()==m['request_sha256'])
ck('review proof exact', (R/'PROOF.md').read_text()in q);ck('model mathematical conclusion','I found no false mathematical statement'in a)
for M in [1,2,3,4,5,7,8,16,24,32,40,48,56,64]:
 zeros=[j for j in range(3*M)if(2*j+1)%3==0 and((2*j+1)//3)%2==1]
 ck(str(M)+' oversampling exact zero indices',zeros==list(range(1,3*M,3))and len(zeros)==M)
 for k in range(5):ck(str((M,k))+' odd-multiple nodal half-integer phase',all(((2*k+1)*(2*j+1))%2==1 for j in range(M)))
for p,h in list(bindings.items()):ck('stable '+p,hashlib.sha256(Path(p).read_bytes()).hexdigest()==h)
out=dict(status='CONFIRMED_SCOPED_SAMPLING_THEOREM',utc=datetime.now(timezone.utc).isoformat(),count=len(checks),checks=checks,bindings=bindings,actual_model=m['returned_model'],request_id=m['request_id'],scope='Exact unrestricted smooth parity sampling kernel; injectivity in degree<M space. No authentication of any IPM candidate or inverse; primary UNRESOLVED.')
(V/'FINAL_BINDINGS.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'],out['count'])
