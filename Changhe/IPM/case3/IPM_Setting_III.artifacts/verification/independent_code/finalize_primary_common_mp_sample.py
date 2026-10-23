from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,sys
ROOT=Path('verification');assert Path.cwd().resolve()==ROOT and not sys.flags.optimize
R=ROOT/'research/primary_common_mp_sample';V=R/'verification';assert not(V/'FINAL_BINDINGS.json').exists()
checks=[];bindings={};reviews=[]
def ck(n,b):
 checks.append(dict(name=n,passed=bool(b)))
 if not b:raise AssertionError(n)
def bind(p,h=None):
 p=Path(p).resolve();b=p.read_bytes();got=hashlib.sha256(b).hexdigest();ck('bind '+str(p),b==p.read_bytes()and(h is None or got==h));bindings[str(p)]=got;return b
bind(__file__)
for f,count in [('CHECKS.json',1910),('PRECISION_DETAIL_CHECKS.json',389)]:
 j=json.loads(bind(V/f));ck('accepted finite checks '+f,j['count']==len(j['checks'])==count and all(x['passed']for x in j['checks']))
 for p,h in j['bindings'].items():bind(p,h)
d=json.loads(bind(V/'DESIGN_ACCEPTANCE.json'));ck('accepted design',d['status']=='ACCEPTED_FINITE_COMMON_SAMPLE_DESIGN')
for p,h in d['bindings'].items():bind(p,h)
m=json.loads(bind(V/'MANUFACTURES.json'));ck('15 worker manufactures',m['count']==len(m['checks'])==15 and all(x['passed']for x in m['checks']))
bind(ROOT/'independent_code/run_primary_common_mp_sample.py',m['worker_sha256']);bind(ROOT/'independent_code/smooth_mp_primitives.py',m['implementation_sha256']);bind(R/'PROOF.md',m['proof_sha256'])
for p in sorted(R.glob('*.md')):bind(p)
for p in sorted(V.iterdir()):
 if p.is_file():bind(p)
for stage in ['design','design_followup','design_final','results','results_followup','closure']:
 d=V/('opus_'+stage);m=json.loads(bind(d/'metadata.json'));r=json.loads(bind(d/'response.json'));answer=bind(d/'answer.md').decode();req=bind(d/'request.txt')
 ck('actual Opus5.5 '+stage,m['requested_model']=='us.anthropic.claude-opus-5-5'and m['returned_model']==r['model']=='claude-opus-5-5'and m['stop_reason']==r['stop_reason']=='end_turn'and m['answer_nonempty']and bool(answer.strip()))
 body='\n'.join(x['text']for x in r['content']if x.get('type')=='text')
 ck('matching actual answer '+stage,body.strip()==answer.strip())
 ck('matching actual request '+stage,hashlib.sha256(req).hexdigest()==m['request_sha256'])
 reviews.append(dict(stage=stage,request_id=m['request_id'],actual_model=r['model'],started_utc=m['started_utc'],finished_utc=m['finished_utc']))
ck('closure final model ID',reviews[-1]['request_id']=='e083389d-0c15-4a8f-b338-c1e77abe52d4')
for p,h in bindings.items():ck('stable final '+p,hashlib.sha256(Path(p).read_bytes()).hexdigest()==h)
out=dict(status='CONFIRMED_FINITE_PRIMARY_COMMON_MP_SAMPLE',utc=datetime.now(timezone.utc).isoformat(),count=len(checks),checks=checks,bindings=bindings,actual_reviews=reviews,scope='Three fixed primary smooth trial fields on51 frozen common points,75/110displaydigits. Finite precision and arithmetic comparisons; no enclosure, independent-domain refinement, limiting profile or primary endpoint.')
(V/'FINAL_BINDINGS.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:out[k]for k in ['status','utc','count']}));print('sha256',hashlib.sha256((V/'FINAL_BINDINGS.json').read_bytes()).hexdigest())
