"""Bind result296's independently checked claims and actual model exchange."""
from pathlib import Path
import hashlib,json
from datetime import datetime,timezone
R=Path('research/spec58_consistency_audit');V=R/'verification'
checks=[];bindings={}
def ck(n,v):
 checks.append({'name':n,'passed':bool(v)})
 if not v: raise AssertionError(n)
def bind(p,expected=None):
 p=Path(p);h=hashlib.sha256(p.read_bytes()).hexdigest()
 if expected is not None:ck('hash '+str(p),h==expected)
 bindings[str(p)]=h
 return h
D=json.loads((V/'CHECKS.json').read_text())
ck('arithmetic PASS',D['status']=='PASS')
ck('126 assertions',D['count']==126==len(D['checks']))
ck('all arithmetic assertions passed',all(x['passed'] for x in D['checks']))
ck('24 rounding entries',len(D['rounding'])==24)
for p,h in D['bindings'].items():bind(p,h)
for d in json.loads((V/'INPUTS.json').read_text())['files']:bind(d['frozen'],d['sha256'])
for label in ['review','followup']:
 p=V/('opus_'+label);m=json.loads((p/'metadata.json').read_text());r=json.loads((p/'response.json').read_text())
 ck(label+' requested5.5',m['requested_model']=='us.anthropic.claude-opus-5-5')
 ck(label+' returned5.5',m['returned_model']=='claude-opus-5-5'==r['model'])
 ck(label+' complete',m['stop_reason']=='end_turn'==r['stop_reason'])
 ck(label+' nonempty',m['answer_nonempty'] and bool((p/'answer.md').read_text().strip()))
 text='\n\n'.join(z['text'] for z in r['content'] if z['type']=='text')
 ck(label+' exact answer',(p/'answer.md').read_text().strip()==text.strip())
 bind(p/'request.txt',m['request_sha256'])
 for n in ['response.json','answer.md','metadata.json']:bind(p/n)
for n in ['PROOF.md','REVIEW_RESOLUTION_PROOF.md','REVIEW_COMPLETION.md']:bind(R/n)
for n in ['CHECKS.json','INPUTS.json','CHANGES.json','DIFF.txt']:bind(V/n)
bind(__file__)
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS','count':len(checks),'checks':checks,'bindings':bindings,'scope':'CONFIRMED scoped mathematics and numerical values; two requested SPEC wording repairs remain uninstalled; full-plane UNRESOLVED'}
(V/'REVIEW_BINDINGS.json').write_text(json.dumps(out,indent=2)+'\n')
print(out['utc'],out['status'],out['count'])
