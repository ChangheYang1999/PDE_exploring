from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
import hashlib,json,sys
ROOT=Path('verification');assert Path.cwd().resolve()==ROOT and not sys.flags.optimize
R=ROOT/'research/run_closure';V=R/'verification';dest=V/'FINAL_BINDINGS.json';assert not dest.exists();checks=[];bindings={};reviews=[];substitutions=[]
def ck(n,b):checks.append(dict(name=n,passed=bool(b)));assert b,n
def bind(p,h=None):
 p=Path(p).resolve();b=p.read_bytes();a=hashlib.sha256(b).hexdigest();ck('identity '+str(p),p.read_bytes()==b and(h is None or a==h));bindings[str(p)]=a;return b
for p in [__file__,R/'PROOF.md',R/'FINAL_ACCEPTANCE_PROTOCOL.md',R/'FINAL_TIME_PROTOCOL.md',R/'END_WRITER_REVISION_PROTOCOL.md',R/'PUBLICATION_TIME_RESOLUTION.md',ROOT/'independent_code/install_verifier_end_record.py',V/'EARLY_TIME_GATE_TEST.json',V/'CLOSING_DISK_OBSERVATION.json',V/'CLOSING_PROCESS_OBSERVATION.json',V/'SECOND_EARLY_TIME_GATE_TEST.json',V/'END_WRITER_REVIEWED_FIRST.py.txt',R/'RESULTS.md']:bind(p)
candidate=json.loads(bind(V/'PUBLICATION_CANDIDATE_CHECKS.json'));ck('4517 actual passes',candidate['status']=='PASS_CURATED_CLOSURE_CANDIDATE'and candidate['count']==len(candidate['checks'])==4517 and all(c['passed']for c in candidate['checks'])and candidate['failed']==[]);ck('14 prior manifests',len(candidate['accepted_manifests'])==14)
live=ROOT/'shifts/shifts.log'
for p,h in candidate['bindings'].items():
 if Path(p)==live:
  b=live.read_bytes();ck('live log matches accepted candidate',hashlib.sha256(b).hexdigest()==h);snap=V/'FROZEN_SHIFT_LOG_AT_ACCEPTANCE.log';ck('new immutable log snapshot',not snap.exists());snap.write_bytes(b);bind(snap,h);substitutions.append(dict(original_path=str(live),snapshot_path=str(snap),sha256=h,observed_utc=datetime.now(timezone.utc).isoformat(),reason='Coordinator may append a shift-end event after this turn. Historical checks remain observations of then-current source bytes.'))
 else:bind(p,h)
ck('only one mutable observation substitution',len(substitutions)==1)
full=bind(V/'SYNTHESIS_PUBLICATION_CANDIDATE.md');body=bind(V/'PUBLICATION_BODY_CANDIDATE.md');ck('publication body exact',full[full.index(b'## Problem and exact safeguards'):]==body)
for p,b in [(V/'REVIEWED_BODY.md',body),(V/'SYNTHESIS_REVIEWED.md',full)]:ck('new frozen publication '+str(p),not p.exists());p.write_bytes(b);bind(p)
for tag in ['synthesis','synthesis_followup','publication','time_followup']:
 base=V/('opus_'+tag);m=json.loads(bind(base/'metadata.json'));d=json.loads(bind(base/'response.json'));a=bind(base/'answer.md');q=bind(base/'request.txt',m['request_sha256']);ck('actual complete '+tag,m['returned_model']==d['model']=='claude-opus-5-5'and m['stop_reason']==d['stop_reason']=='end_turn'and bool(a.strip())and m['answer_nonempty']);ck('answer matches raw '+tag,('\n\n'.join(c.get('text','')for c in d.get('content',[])if c.get('type')=='text')+'\n').encode()==a);reviews.append(m)
 if tag=='publication':ck('actual publication text reviewed',('\nFILE '+str(V/'SYNTHESIS_PUBLICATION_CANDIDATE.md')+'\n').encode()+full+b'\n'in q)
 if tag=='time_followup':ck('actual end writer reviewed',('\nFILE '+str(ROOT/'independent_code/install_verifier_end_record.py')+'\n').encode()+(ROOT/'independent_code/install_verifier_end_record.py').read_bytes()+b'\n'in q)
I=json.loads((ROOT/'research/primary_fresh_sample/verification/INPUTS.json').read_text());scope=json.loads(bind(V/'FRESH_RADIUS_SCOPE.json'));rr=[]
for pt in I['points']:
 x,y=[F(float.fromhex(h))for h in pt['hex']];rr.append(x*x+y*y)
ck('actual101radii below1e12',len(rr)==scope['count']==101 and all(q<F(10)**24 for q in rr));ck('exact largest squared radius',max(rr)==F(scope['max_radius_squared_exact'])and rr.index(max(rr))==scope['max_radius_index'])
ck('primary remains unresolved',b'**Verdict: UNRESOLVED for the smooth, nondegenerate primary class.**'in full);ck('no premature end',b'Actual T_end: **NOT YET REACHED**'in full and not(V/'END_RECORD.json').exists())
for p,h in bindings.items():ck('stable '+p,hashlib.sha256(Path(p).read_bytes()).hexdigest()==h)
out=dict(status='CONFIRMED_CLOSING_SYNTHESIS_UNRESOLVED',utc=datetime.now(timezone.utc).isoformat(),count=len(checks),checks=checks,bindings=bindings,actual_reviews=reviews,observation_substitutions=substitutions,reviewed_body_sha256=hashlib.sha256(body).hexdigest(),accepted_manifests=candidate['accepted_manifests'],primary_verdict='UNRESOLVED',T_end=None,scope='Accurate limited synthesis,4517publication checks,14previously accepted manifests and unchanged observed evidence. Live loop log is replaced only by an identical frozen snapshot. Actual end remains pending; no primary YES/NO.');dest.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:out[k]for k in ['status','utc','count','reviewed_body_sha256','T_end']}));print('final manifest sha256',hashlib.sha256(dest.read_bytes()).hexdigest())
