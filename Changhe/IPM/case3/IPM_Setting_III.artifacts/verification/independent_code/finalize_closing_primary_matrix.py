from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,sys
ROOT=Path('verification');R=ROOT/'research/closing_endpoint_audit';V=R/'verification';checks=[];bindings={}
assert not sys.flags.optimize and Path.cwd().resolve()==ROOT
outpath=V/'FINAL_MATRIX_BINDINGS.json';assert not outpath.exists()
def ck(n,b):
 checks.append(dict(name=n,passed=bool(b)))
 if not b:raise AssertionError(n)
def bind(p,h=None):
 p=Path(p).resolve();b=p.read_bytes();d=hashlib.sha256(b).hexdigest();ck('stable '+str(p),p.read_bytes()==b and(h is None or d==h));bindings[str(p)]=d;return b
for p in [__file__,R/'CLOSING_REVIEW_RESOLUTION.md']:bind(p)
d=json.loads(bind(V/'FINAL_MATRIX_CHECKS.json'));ck('finite matrix467',d['count']==len(d['checks'])==467 and all(x['passed']for x in d['checks']) and d['status']=='PASS_CLOSING_MATRIX_FINITE_EVIDENCE_REVIEW_PENDING')
for p,h in d['bindings'].items():bind(p,h)
for n in ['nonzero_far_field','point_symmetries','small_gradient_exclusion','smooth_full_inverse_primitives']:bind(ROOT/'research'/n/'PROOF.md')
reviews=[]
for label,rid in [('closing','3acc4056-1e12-496c-9dd6-054d4aa0c8da'),('closing_complete','3e893545-1bb2-4711-8bcd-9a0dbc2d6f4d'),('closing_dependencies','5b919658-403d-4db0-a786-cd8c35fcdfae')]:
 rv=V/('opus_'+label);m=json.loads(bind(rv/'metadata.json'));rr=json.loads(bind(rv/'response.json'));request=bind(rv/'request.txt');answer=bind(rv/'answer.md');ck('actual complete model '+label,m['requested_model']=='us.anthropic.claude-opus-5-5' and m['returned_model']==rr['model']=='claude-opus-5-5' and m['stop_reason']==rr['stop_reason']=='end_turn' and m['request_id']==rid and m['request_sha256']==hashlib.sha256(request).hexdigest() and m['answer_nonempty'] and bool(answer.strip()));reviews.append(dict(request_id=rid,model=rr['model'],finished_utc=m['finished_utc']))
rv=V/'opus_closing_followup';m=json.loads(bind(rv/'metadata.json'));rr=json.loads(bind(rv/'response.json'))
for name in ['request.txt','answer.md']:bind(rv/name)
ck('incomplete review retained without approval',m['request_id']=='de48f0fb-cf2b-44ca-bde0-684debf9b0f6' and m['stop_reason']==rr['stop_reason']=='max_tokens' and m['returned_model']==rr['model']=='claude-opus-5-5')
for p,h in bindings.items():ck('final retained bytes '+p,hashlib.sha256(Path(p).read_bytes()).hexdigest()==h)
out=dict(status='CONFIRMED_CLOSING_MATRIX_SCOPE',primary_verdict='UNRESOLVED',utc=datetime.now(timezone.utc).isoformat(),count=len(checks),checks=checks,bindings=bindings,actual_reviews=reviews,scope='Exact-profile dependency audit and finite common51-point matrix. Fresh101 supplement, actual lead installation and verifier T_end remain separate. No decisive endpoint.')
outpath.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:out[k]for k in ['status','utc','count','primary_verdict']}))
