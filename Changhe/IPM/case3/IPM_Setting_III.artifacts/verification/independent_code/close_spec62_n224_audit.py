from pathlib import Path
from datetime import datetime,timezone
import json,hashlib
R=Path('research/spec62_and_n224_text_audit');V=R/'verification';checks=[];bindings={};sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def ck(n,b):
 checks.append(dict(name=n,passed=bool(b)))
 if not b:raise AssertionError(n)
def bind(p,h=None):
 p=Path(p);s=sha(p);ck('binding '+str(p),h is None or h==s);bindings[str(p)]=s
for n,c in [('CHECKS.json',102),('REVIEW_SUPPLEMENT.json',133)]:
 p=V/n;bind(p);d=json.loads(p.read_text());ck('completed '+n,d['status']=='PASS_WITH_REQUIRED_SPEC_REPAIR'and d['count']==c==len(d['checks'])and all(x['passed']for x in d['checks']))
 for p,h in d['bindings'].items():bind(p,h)
p=Path('research/hydrostatic_c2_resolved_192_audit/verification/INPUTS.json');bind(p);row=json.loads(p.read_text())['states'][0];bind(row['frozen'],row['sha256']);ck('192manifest exact admitted source',row['sha256']=='5177b5ae4c8a480353f7d855e27cfb735accab264c56f53c1f54881476d737a0')
reviews=[]
for name in ['opus_review','opus_followup']:
 p=V/name;m=json.loads((p/'metadata.json').read_text());r=json.loads((p/'response.json').read_text());ck('actual model '+name,m['requested_model']=='us.anthropic.claude-opus-5-5'and m['returned_model']==r['model']=='claude-opus-5-5');ck('completed actual review '+name,m['stop_reason']==r['stop_reason']=='end_turn'and m['answer_nonempty']);bind(p/'request.txt',m['request_sha256']);ck('complete review text '+name,'\n\n'.join(z.get('text','')for z in r['content']if z['type']=='text').strip()==(p/'answer.md').read_text().strip())
 for n in ['answer.md','metadata.json','response.json']:bind(p/n)
 reviews.append(m)
for p in [Path(__file__),R/'PROOF.md',R/'REVIEW_RESOLUTION_PROOF.md',R/'FINAL_MODEL_RESOLUTION.md',R/'RESULTS.md',R/'CLOSURE_PROOF.md',V/'REQUEST_BUILD_FAILURE.json']:bind(p)
ck('scope explicit','Full-plane IPM: UNRESOLVED. Degree23: OPEN.'in(R/'RESULTS.md').read_text());b=json.loads((V/'CHECKS.json').read_text());out=dict(utc=datetime.now(timezone.utc).isoformat(),status='PASS_WITH_REQUIRED_SPEC_REPAIR',count=len(checks),checks=checks,bindings=bindings,actual_reviews=reviews,targets=dict(SPEC62=b['spec_sha256'],literal_proposal=b['proposal_sha256']),required_repair=b['repair'],scope='Finite content/source arithmetic only; SPEC repair required. No report installation, no historical execution authentication, no primary endpoint.')
(V/'FINAL_BINDINGS.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'],out['count'],out['utc'])
