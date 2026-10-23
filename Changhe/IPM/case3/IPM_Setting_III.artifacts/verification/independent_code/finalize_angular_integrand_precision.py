from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,sys
ROOT=Path('verification');assert Path.cwd().resolve()==ROOT and not sys.flags.optimize
R=ROOT/'research/angular_integrand_precision';V=R/'verification';assert not(V/'FINAL_BINDINGS.json').exists()
checks=[];bindings={};reviews=[]
def ck(n,b):
 checks.append(dict(name=n,passed=bool(b)))
 if not b:raise AssertionError(n)
def bind(p,h=None):
 p=Path(p).resolve();b=p.read_bytes();got=hashlib.sha256(b).hexdigest();ck('bind '+str(p),b==p.read_bytes()and(h is None or got==h));bindings[str(p)]=got;return b
bind(__file__)
for f,count in [('CHECKS.json',533),('SUPPLEMENT_CHECKS.json',7140),('CLOSURE_CHECKS.json',730)]:
 j=json.loads(bind(V/f));ck('accepted finite checks '+f,j['count']==len(j['checks'])==count and all(x['passed']for x in j['checks']))
 for p,h in j['bindings'].items():bind(p,h)
for p in sorted(R.glob('*.md')):bind(p)
for p in sorted(V.iterdir()):
 if p.is_file():bind(p)
for stage in ['design','design_followup','design_final','replay_repair','results','results_followup','closure']:
 d=V/('opus_'+stage);m=json.loads(bind(d/'metadata.json'));r=json.loads(bind(d/'response.json'));answer=bind(d/'answer.md').decode();req=bind(d/'request.txt')
 ck('actual Opus5.5 '+stage,m['requested_model']=='us.anthropic.claude-opus-5-5'and m['returned_model']==r['model']=='claude-opus-5-5'and m['stop_reason']==r['stop_reason']=='end_turn'and m['answer_nonempty']and bool(answer.strip()))
 body='\n'.join(x['text']for x in r['content']if x.get('type')=='text')
 ck('matching actual answer '+stage,body.strip()==answer.strip())
 ck('matching actual request '+stage,hashlib.sha256(req).hexdigest()==m['request_sha256'])
 reviews.append(dict(stage=stage,request_id=m['request_id'],actual_model=r['model'],started_utc=m['started_utc'],finished_utc=m['finished_utc']))
ck('closure final model ID',reviews[-1]['request_id']=='c480e2ef-26f7-4b6c-802d-47fda9dc446c')
for p,h in bindings.items():ck('stable final '+p,hashlib.sha256(Path(p).read_bytes()).hexdigest()==h)
out=dict(status='CONFIRMED_FINITE_SELECTED_ANGULAR_INTEGRAND_PRECISION',utc=datetime.now(timezone.utc).isoformat(),count=len(checks),checks=checks,bindings=bindings,actual_reviews=reviews,scope='Only two selected auxiliary targets with frozen quadrature and rounded coordinates. Finite precision, arithmetic, replay and geometry observations; no enclosure, full-grid MP, primary endpoint or historical runtime attestation.')
(V/'FINAL_BINDINGS.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:out[k]for k in ['status','utc','count']}));print('sha256',hashlib.sha256((V/'FINAL_BINDINGS.json').read_bytes()).hexdigest())
