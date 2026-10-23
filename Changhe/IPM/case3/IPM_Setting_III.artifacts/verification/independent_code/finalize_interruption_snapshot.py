from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,sys
ROOT=Path('verification');assert Path.cwd().resolve()==ROOT and not sys.flags.optimize
R=ROOT/'research/final_report_closure_audit';V=R/'verification';assert not(V/'INTERRUPTIONS_FINAL_BINDINGS.json').exists()
checks=[];bindings={};reviews=[]
def ck(n,b):
 checks.append(dict(name=n,passed=bool(b)))
 if not b:raise AssertionError(n)
def bind(p,h=None):
 p=Path(p).resolve();b=p.read_bytes();got=hashlib.sha256(b).hexdigest();ck('bind '+str(p),b==p.read_bytes()and(h is None or got==h));bindings[str(p)]=got;return b
bind(__file__)
c=json.loads(bind(V/'INTERRUPTIONS_CLOSURE_CHECKS.json'));ck('124 closure gates',c['count']==len(c['checks'])==124 and all(x['passed']for x in c['checks']))
for p,h in c['bindings'].items():bind(p,h)
a=json.loads(bind(V/'INTERRUPTIONS_CHECKS.json'));ck('278 original census gates',a['count']==len(a['checks'])==278 and all(x['passed']for x in a['checks']))
ck('ten explicit historical sources',len(c['historical_sources'])==10 and len({x['source']for x in c['historical_sources']})==10)
for x in c['historical_sources']:
 ck('historical mapping '+x['source'],a['bindings'][x['source']]==a['bindings'][x['snapshot']]==x['sha256'] and x['observed_utc']==a['snapshot_utc']);bind(x['snapshot'],x['sha256'])
failed=V/'interruptions_snapshot_failed_membership';ck('only failed lead snapshot',sorted(p.name for p in failed.iterdir())==['analysis_shifts.log']);ck('failed and successful lead copy equality',bind(failed/'analysis_shifts.log')==bind(V/'interruptions_snapshot/analysis_shifts.log'))
for p in (V/'interruptions_snapshot').glob('*_shifts.log'):ck('no CR bytes '+str(p),b'\r'not in bind(p))
for p in sorted(R.glob('INTERRUPTIONS*.md')):bind(p)
for p in sorted(V.glob('INTERRUPTIONS*')):
 if p.is_file():bind(p)
for stage in ['interruption','interruption_followup']:
 d=V/('opus_'+stage);m=json.loads(bind(d/'metadata.json'));r=json.loads(bind(d/'response.json'));answer=bind(d/'answer.md').decode();req=bind(d/'request.txt')
 ck('actual Opus5.5 '+stage,m['requested_model']=='us.anthropic.claude-opus-5-5'and m['returned_model']==r['model']=='claude-opus-5-5'and m['stop_reason']==r['stop_reason']=='end_turn'and m['answer_nonempty']and bool(answer.strip()))
 body='\n'.join(x['text']for x in r['content']if x.get('type')=='text')
 ck('matching actual answer '+stage,body.strip()==answer.strip())
 ck('matching actual request '+stage,hashlib.sha256(req).hexdigest()==m['request_sha256'])
 reviews.append(dict(stage=stage,request_id=m['request_id'],actual_model=r['model'],started_utc=m['started_utc'],finished_utc=m['finished_utc']))
ck('closure final model ID',reviews[-1]['request_id']=='d01b6359-8089-431d-b2bc-716684cba180')
for p,h in bindings.items():ck('stable final '+p,hashlib.sha256(Path(p).read_bytes()).hexdigest()==h)
out=dict(status='CONFIRMED_FROZEN_INTERRUPTION_RECORD',utc=datetime.now(timezone.utc).isoformat(),count=len(checks),checks=checks,bindings=bindings,actual_reviews=reviews,scope='Frozen2026-10-22T10:41:17.839289Z census only. Rule/context procedure scope, no universal runtime attestation. New final-build census mandatory; actual T_end unreached.')
(V/'INTERRUPTIONS_FINAL_BINDINGS.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:out[k]for k in ['status','utc','count']}));print('sha256',hashlib.sha256((V/'INTERRUPTIONS_FINAL_BINDINGS.json').read_bytes()).hexdigest())
