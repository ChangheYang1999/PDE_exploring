from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,sys
if sys.flags.optimize:raise RuntimeError('optimized refused')
ROOT=Path('verification')
if Path.cwd().resolve()!=ROOT:raise RuntimeError('wrong lane')
R=ROOT/'research/angular_quadrature_grid_audit';V=R/'verification';checks=[];bindings={}
def ck(n,b):
 checks.append(dict(name=n,passed=bool(b)))
 if not b:raise AssertionError(n)
def bind(p,h=None):
 p=Path(p);p=p if p.is_absolute()else ROOT/p;p=p.resolve();b=p.read_bytes();a=hashlib.sha256(b).hexdigest();ck('stable read '+str(p),p.read_bytes()==b)
 if h is not None:ck('binding '+str(p),a==h)
 bindings[str(p)]=a;return b
if (V/'FINAL_BINDINGS.json').exists():raise FileExistsError('accepted evidence preserved')
for name,status,n in [('CHECKS.json','PASS_COMPLETE_FINITE_ANGULAR_QUADRATURE_AUDIT_REVIEW_PENDING',107),('PROTOCOL_CHECKS.json','PASS_ANGULAR_GRID_PROTOCOL_RECORDS_REVIEW_PENDING',184)]:
 d=json.loads(bind(V/name));ck('passing '+name,d['status']==status and d['count']==len(d['checks'])==n and all(c['passed']for c in d['checks']))
 for p,h in d['bindings'].items():bind(p,h)
reviews=[]
for label in ['design','design_followup','results','results_followup_retry','final']:
 f=V/('opus_'+label);m=json.loads(bind(f/'metadata.json'));resp=json.loads(bind(f/'response.json'));q=bind(f/'request.txt');a=bind(f/'answer.md').decode()
 ck('actual model '+label,m['requested_model']=='us.anthropic.claude-opus-5-5'and m['returned_model']==resp['model']=='claude-opus-5-5')
 ck('complete answer '+label,m['stop_reason']==resp['stop_reason']=='end_turn'and m['answer_nonempty'])
 ck('request identity '+label,hashlib.sha256(q).hexdigest()==m['request_sha256'])
 ck('answer identity '+label,'\n\n'.join(z['text']for z in resp['content']if z['type']=='text').strip()==a.strip())
 reviews.append(dict(label=label,request_id=m['request_id'],finished_utc=m['finished_utc']))
f=json.loads(bind(V/'opus_results_followup/metadata.json'));ck('API failure is not review',not f.get('answer_nonempty',False)and'InternalServerException'in f['error'])
for p in R.rglob('*'):
 if p.is_file():bind(p)
bind(__file__)
ck('failed source retained and finally bound',str((V/'PROTOCOL_CHECKER_FAILED_LABELS.py').resolve())in bindings)
ck('corrected limited provenance wording','does not bind this historical failed source'in (R/'PROTOCOL_CHECK_PROOF.md').read_text())
for p,h in bindings.items():ck('final stable '+Path(p).name,hashlib.sha256(Path(p).read_bytes()).hexdigest()==h)
out=dict(status='CONFIRMED_COMPLETE_FINITE_ANGULAR_QUADRATURE_COMPARISON',utc=datetime.now(timezone.utc).isoformat(),count=len(checks),checks=checks,bindings=bindings,reviews=reviews,scope='107 main checks/30600 scalar fields and184 execution-record checks; two bitwise-identical full A/C passes; finite empirical quadrature agreement only. Runtime worker PID and bytecode use not attested; first-process module origin unrecorded; ordinary filesystem trust; no continuum enclosure or primary endpoint.')
(V/'FINAL_BINDINGS.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:out[k]for k in ['status','utc','count','reviews']},indent=2));print('SHA',hashlib.sha256((V/'FINAL_BINDINGS.json').read_bytes()).hexdigest())
