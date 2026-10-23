from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,sys
ROOT=Path('verification');assert Path.cwd().resolve()==ROOT and not sys.flags.optimize
R=ROOT/'research/primary_fresh_sample';V=R/'verification';dest=V/'FINAL_BINDINGS.json';assert not dest.exists();checks=[];bindings={}
def ck(n,b):checks.append(dict(name=n,passed=bool(b)));assert b,n
def bind(p,h=None):
 p=Path(p).resolve();b=p.read_bytes();a=hashlib.sha256(b).hexdigest();ck('bind '+str(p),p.read_bytes()==b and(h is None or a==h));bindings[str(p)]=a;return b
for p in [__file__,R/'PROOF.md',R/'FINAL_ACCEPTANCE_PROOF.md',R/'RESULTS_DRAFT.md',R/'RESULTS.md',R/'RESULTS_REVIEW_RESOLUTION.md',R/'CLOSING_REVIEW_NOTE.md']:bind(p)
for p,status,count in [(V/'CHECKS.json','PASS_PRIMARY_FRESH_SAMPLE_REVIEW_PENDING',3201),(V/'CLOSURE_SUPPLEMENT.json','PASS_FRESH_CLOSURE_SUPPLEMENT',63)]:
 d=json.loads(bind(p));ck('accepted checks '+p.name,d['status']==status and d['count']==count==len(d['checks'])and all(c['passed']for c in d['checks']))
 for q,h in d['bindings'].items():bind(q,h)
design=json.loads(bind(V/'DESIGN_ACCEPTANCE.json'));ck('prospective accepted',design['status']=='ACCEPTED_FINITE_FRESH_SAMPLE_DESIGN')
for p,h in design['bindings'].items():bind(p,h)
old=ROOT/'research/primary_common_mp_sample/verification/FINAL_BINDINGS.json';d=json.loads(bind(old,'0750932980dcee8cd6b52aa57f053718f1e8143941a2d931e71358fd6e5f33db'));ck('previous finite common observation accepted',d['status']=='CONFIRMED_FINITE_PRIMARY_COMMON_MP_SAMPLE'and d['count']==352==len(d['checks'])and all(c['passed']for c in d['checks']))
for p,h in d['bindings'].items():bind(p,h)
reviews=[]
for label in ['design','results','results_followup']:
 a=V/('opus_'+label);m=json.loads(bind(a/'metadata.json'));r=json.loads(bind(a/'response.json'));q=bind(a/'request.txt');ans=bind(a/'answer.md');ck('actual Opus5.5 '+label,m['returned_model']==r['model']=='claude-opus-5-5'and m['requested_model']=='us.anthropic.claude-opus-5-5'and m['stop_reason']==r['stop_reason']=='end_turn'and m['answer_nonempty']and bool(ans.strip())and m['request_sha256']==hashlib.sha256(q).hexdigest())
 if label.startswith('results'):ck('actual data bound '+label,hashlib.sha256((V/'CHECKS.json').read_bytes()).hexdigest().encode()in q)
 reviews.append(dict(label=label,request_id=m['request_id'],model=m['returned_model'],finished_utc=m['finished_utc']))
for p,h in bindings.items():ck('final stable '+p,hashlib.sha256(Path(p).read_bytes()).hexdigest()==h)
out=dict(status='CONFIRMED_FINITE_PRIMARY_FRESH_SAMPLE',utc=datetime.now(timezone.utc).isoformat(),count=len(checks),checks=checks,bindings=bindings,actual_reviews=reviews,primary_verdict='UNRESOLVED',scope='101 fixed points for three saved primary trial fields. Exact recombination of stored primitive fields, empirical cross-precision tolerance and finite maxima only. No inverse accuracy enclosure, uniform residual, continuum convergence, actual run end or new endpoint.337 is not a premise.');dest.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:out[k]for k in ['status','utc','count']}))
