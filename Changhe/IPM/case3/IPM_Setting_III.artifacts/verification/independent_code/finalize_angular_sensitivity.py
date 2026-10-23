from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,sys
if sys.flags.optimize:raise RuntimeError('optimized refused')
ROOT=Path('verification')
if Path.cwd().resolve()!=ROOT:raise RuntimeError('wrong lane')
R=ROOT/'research/angular_evaluator_sensitivity';V=R/'verification';checks=[];bindings={}
def ck(n,b):
 checks.append(dict(name=n,passed=bool(b)))
 if not b:raise AssertionError(n)
def bind(p,h=None):
 p=Path(p);p=p if p.is_absolute()else ROOT/p;p=p.resolve();b=p.read_bytes();a=hashlib.sha256(b).hexdigest();ck('stable '+str(p),p.read_bytes()==b)
 if h is not None:ck('hash '+str(p),a==h)
 bindings[str(p)]=a;return b
if (V/'FINAL_BINDINGS.json').exists():raise FileExistsError('accepted evidence preserved')
for name,status,n in [('CHECKS.json','PASS_FINITE_ANGULAR_SENSITIVITY_CHECKS_REVIEW_PENDING',191),('OFFSET_CHECKS.json','PASS_FINITE_OFFSET_DIAGNOSTIC',57)]:
 d=json.loads(bind(V/name));ck('passing '+name,d['status']==status and d['count']==len(d['checks'])==n and all(c['passed']for c in d['checks']))
 for p,h in d['bindings'].items():bind(p,h)
oldp=V/'OFFSET_CHECKS_BEFORE_TAIL_CLARIFICATION.json';newp=V/'OFFSET_CHECKS.json';old=json.loads(bind(oldp));new=json.loads(bind(newp))
ck('old 57 passing',old['status']=='PASS_FINITE_OFFSET_DIAGNOSTIC'and old['count']==len(old['checks'])==57 and all(c['passed']for c in old['checks']))
canon=lambda x:json.dumps(x,sort_keys=True,ensure_ascii=True,separators=(',',':')).encode('utf-8')
a,b=canon(old['records']),canon(new['records']);ck('canonical records identical',a==b)
changed=[p for p in old['bindings'] if old['bindings'][p]!=new['bindings'].get(p)]
ck('only old tail binding changed',set(old['bindings'])==set(new['bindings'])and changed==[str(R/'TAIL_DETAIL_PROOF.md')])
for p,h in old['bindings'].items():bind(V/'TAIL_DETAIL_PROOF_BEFORE_CLARIFICATION.md' if p in changed else p,h)
comparison=dict(method='json.dumps(records,sort_keys=True,ensure_ascii=True,separators=(comma,colon)).encode(UTF-8)',old_file_sha256=bindings[str(oldp)],new_file_sha256=bindings[str(newp)],old_records_sha256=hashlib.sha256(a).hexdigest(),new_records_sha256=hashlib.sha256(b).hexdigest(),equal_bytes=a==b,old_mtime_ns=oldp.stat().st_mtime_ns,new_mtime_ns=newp.stat().st_mtime_ns,scope='Observed local filesystem metadata only; no independent historical attestation of copy time.')
ck('observed old copy mtime before rerun',comparison['old_mtime_ns']<comparison['new_mtime_ns'])
f=ROOT/'research/angular_quadrature_grid_audit/verification/FINAL_BINDINGS.json';d=json.loads(bind(f,'83ada04e0c8bd0b157dfc7bd4a1082d2983bf5f96493b5fc06410dc1807e3c47'));ck('332 accepted',d['status']=='CONFIRMED_COMPLETE_FINITE_ANGULAR_QUADRATURE_COMPARISON'and all(c['passed']for c in d['checks']))
for p,h in d['bindings'].items():bind(p,h)
reviews=[]
for label in ['design2','design3','results','results_followup','final','closure']:
 f=V/('opus_'+label);m=json.loads(bind(f/'metadata.json'));resp=json.loads(bind(f/'response.json'));q=bind(f/'request.txt');a=bind(f/'answer.md').decode()
 ck('actual model '+label,m['requested_model']=='us.anthropic.claude-opus-5-5'and m['returned_model']==resp['model']=='claude-opus-5-5')
 ck('complete '+label,m['stop_reason']==resp['stop_reason']=='end_turn'and m['answer_nonempty'])
 ck('request '+label,hashlib.sha256(q).hexdigest()==m['request_sha256'])
 ck('answer '+label,'\n\n'.join(z['text']for z in resp['content']if z['type']=='text').strip()==a.strip())
 reviews.append(dict(label=label,request_id=m['request_id'],finished_utc=m['finished_utc']))
f=json.loads(bind(V/'opus_design/metadata.json'));ck('refusal excluded',f['stop_reason']=='refusal'and not f['answer_nonempty'])
for p in R.rglob('*'):
 if p.is_file():bind(p)
bind(__file__)
for p,h in bindings.items():ck('final stable '+Path(p).name,hashlib.sha256(Path(p).read_bytes()).hexdigest()==h)
out=dict(status='CONFIRMED_FINITE_ANGULAR_EVALUATOR_SENSITIVITY',utc=datetime.now(timezone.utc).isoformat(),count=len(checks),checks=checks,bindings=bindings,reviews=reviews,offset_record_comparison=comparison,scope='191 main gates with12250 scalar comparisons,57 offset gates, and accepted332 finite quadrature agreement. Six substantive327 actual Opus5.5 reviews and a separate refusal. No continuum enclosure, historical producer execution attestation, or primary endpoint.333 is not used.')
(V/'FINAL_BINDINGS.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:out[k]for k in ['status','utc','count','reviews','offset_record_comparison']},indent=2));print('SHA',hashlib.sha256((V/'FINAL_BINDINGS.json').read_bytes()).hexdigest())
