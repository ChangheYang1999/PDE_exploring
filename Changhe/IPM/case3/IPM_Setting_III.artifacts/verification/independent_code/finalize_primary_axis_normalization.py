from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,sys
ROOT=Path('verification');assert Path.cwd().resolve()==ROOT and not sys.flags.optimize
R=ROOT/'research/primary_axis_normalization_closure';V=R/'verification';dest=V/'FINAL_BINDINGS.json';assert not dest.exists();checks=[];bindings={};reviews=[]
def ck(n,b):checks.append(dict(name=n,passed=bool(b)));assert b,n
def bind(p,h=None):
 p=Path(p).resolve();b=p.read_bytes();a=hashlib.sha256(b).hexdigest();ck('identity '+str(p),p.read_bytes()==b and(h is None or a==h));bindings[str(p)]=a;return b
for p in [__file__,R/'FINAL_ACCEPTANCE_PROTOCOL.md',R/'FOLLOWUP_RESOLUTION.md']:bind(p)
for name,n in [('CHECKS.json',40),('SUPPLEMENT_CHECKS.json',249)]:
 d=json.loads(bind(V/name));ck(name+'allpassed',d['count']==len(d['checks'])==n and all(c['passed']for c in d['checks']))
 for p,h in d['bindings'].items():bind(p,h)
I=json.loads((ROOT/'research/primary_fresh_sample/verification/INPUTS.json').read_text());C=json.loads((V/'CHECKS.json').read_text());ck('exactly three source states',len(I['states'])==len(C['rows'])==3);ck('no zip omission',[x['N']for x in I['states']]==[x['N']for x in C['rows']]==[36,40,44])
for tag in ['results','followup']:
 m=json.loads(bind(V/('opus_'+tag)/'metadata.json'));d=json.loads(bind(V/('opus_'+tag)/'response.json'));a=bind(V/('opus_'+tag)/'answer.md');q=bind(V/('opus_'+tag)/'request.txt',m['request_sha256']);ck('actual complete '+tag,m['returned_model']==d['model']=='claude-opus-5-5'and m['stop_reason']==d['stop_reason']=='end_turn'and bool(a.strip())and m['answer_nonempty']);reviews.append(m)
for p,h in bindings.items():ck('stable '+p,hashlib.sha256(Path(p).read_bytes()).hexdigest()==h)
out=dict(status='CONFIRMED_EXACT_FINITE_PRIMARY_AXIS_NORMALIZATION',utc=datetime.now(timezone.utc).isoformat(),count=len(checks),checks=checks,bindings=bindings,actual_reviews=reviews,primary_verdict='UNRESOLVED',scope='Exact coefficient functionals and rigorous saved-finite-formula reporting length bounds only. No exact transport or IPM endpoint.');dest.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:out[k]for k in ['status','utc','count']}));print(hashlib.sha256(dest.read_bytes()).hexdigest())
