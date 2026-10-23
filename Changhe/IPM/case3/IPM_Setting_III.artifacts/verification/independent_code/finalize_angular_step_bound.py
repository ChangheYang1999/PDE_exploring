from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,sys
if sys.flags.optimize:raise RuntimeError('optimized Python refused')
ROOT=Path('verification')
if Path.cwd().resolve()!=ROOT:raise RuntimeError('wrong lane')
R=ROOT/'research/angular_step_error_bound';V=R/'verification';checks=[];bindings={}
def ck(n,b):
 checks.append(dict(name=n,passed=bool(b)))
 if not b:raise AssertionError(n)
def bind(p,h=None):
 p=Path(p).resolve();b=p.read_bytes();a=hashlib.sha256(b).hexdigest();ck('stable read '+str(p),p.read_bytes()==b)
 if h is not None:ck('binding '+str(p),h==a)
 bindings[str(p)]=a;return b
if (V/'FINAL_BINDINGS.json').exists():raise FileExistsError('accepted evidence preserved')
d=json.loads(bind(V/'CHECKS.json'));ck('218 checks pass',d['status']=='PASS_STEP_BOUND_SYMBOLIC_AND_GAUSSIAN_CHECKS_REVIEW_PENDING'and d['count']==218 and len(d['checks'])==218 and all(c['passed']for c in d['checks']))
for p,h in d['bindings'].items():bind(p,h)
reviews=[]
for label in ['review','followup']:
 f=V/('opus_'+label);m=json.loads(bind(f/'metadata.json'));resp=json.loads(bind(f/'response.json'));q=bind(f/'request.txt');answer=bind(f/'answer.md').decode()
 ck('actual requested model '+label,m['requested_model']=='us.anthropic.claude-opus-5-5')
 ck('actual returned model '+label,m['returned_model']==resp['model']=='claude-opus-5-5')
 ck('complete nonempty answer '+label,m['stop_reason']==resp['stop_reason']=='end_turn'and m['answer_nonempty'])
 ck('request identity '+label,hashlib.sha256(q).hexdigest()==m['request_sha256'])
 ck('answer identity '+label,'\n\n'.join(z['text']for z in resp['content']if z['type']=='text').strip()==answer.strip())
 reviews.append(dict(label=label,request_id=m['request_id'],finished_utc=m['finished_utc']))
for p in R.rglob('*'):
 if p.is_file():bind(p)
for p in [__file__,ROOT/'independent_code/scalar_mp_hydrostatic_density.py',ROOT/'independent_code/independent_hydrostatic.py',ROOT/'research/independent_hydrostatic_evaluator/PROOF.md']:bind(p)
for p,h in bindings.items():ck('final stable '+Path(p).name,hashlib.sha256(Path(p).read_bytes()).hexdigest()==h)
out=dict(status='CONFIRMED_CONDITIONAL_AUXILIARY_QUADRATIC_STEP_BOUND',utc=datetime.now(timezone.utc).isoformat(),count=len(checks),checks=checks,bindings=bindings,reviews=reviews,scope='Exact conditional analytic theorem plus finite diagnostic checks; extra weighted fourth-derivative and compact-x tail hypotheses; no candidate-specific M or inverse enclosure; primary UNRESOLVED.')
(V/'FINAL_BINDINGS.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:out[k]for k in ['status','utc','count','reviews']},indent=2));print('SHA',hashlib.sha256((V/'FINAL_BINDINGS.json').read_bytes()).hexdigest())
