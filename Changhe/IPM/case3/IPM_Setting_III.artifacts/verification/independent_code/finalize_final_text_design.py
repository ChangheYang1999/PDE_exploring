from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,sys
ROOT=Path('verification');R=ROOT/'research/final_report_closure_audit';V=R/'verification'
assert not sys.flags.optimize and Path.cwd().resolve()==ROOT
checks=[];bindings={}
def ck(n,b):
 checks.append(dict(name=n,passed=bool(b)))
 if not b:raise AssertionError(n)
def bind(p,h=None):
 p=Path(p).resolve();b=p.read_bytes();a=hashlib.sha256(b).hexdigest();ck('stable '+str(p),p.read_bytes()==b and(h is None or a==h));bindings[str(p)]=a;return b
for p in [__file__,R/'FINAL_TEXT_DESIGN_CLOSURE.md']:bind(p)
for name,num in [('dry_v4/CHECKS.json',170),('FINAL_TEXT_MANUFACTURES_v4.json',31)]:
 j=json.loads(bind(V/name));ck(name+' passing',j['count']==len(j['checks'])==num and all(c['passed']for c in j['checks']))
 for p,h in j['bindings'].items():bind(p,h)
ck('test actually pinned','32a2e7b5c9ba72938b694a94128fa7cd91da58f2c6886993196715b2dc33ed0a' in (ROOT/'independent_code/check_final_report_text.py').read_text())
reviews=[]
for name,rid in [('text_design','2eb030de-3430-4ec3-9025-7a94a9ffff24'),('text_followup','082f4537-c450-44c9-9734-2c2c6bd32c2e'),('text_pin_closure','8fedd6cc-40c0-458c-9e88-b5888833969c')]:
 d=V/('opus_'+name);m=json.loads(bind(d/'metadata.json'));response=json.loads(bind(d/'response.json'));request=bind(d/'request.txt');answer=bind(d/'answer.md')
 ck('actual reviewed model '+name,m['requested_model']=='us.anthropic.claude-opus-5-5'and m['returned_model']==response['model']=='claude-opus-5-5'and m['stop_reason']==response['stop_reason']=='end_turn'and m['request_id']==rid and m['answer_nonempty']and bool(answer.strip())and m['request_sha256']==hashlib.sha256(request).hexdigest())
 reviews.append(dict(request_id=rid,actual_model=m['returned_model'],finished_utc=m['finished_utc']))
for name in ['FINAL_TEXT_REPAIR_RECORD.json','FINAL_TEXT_TEST_PIN_REPAIR_RECORD.json','FINAL_TEXT_v3_FAILURE.json']:
 j=json.loads(bind(V/name))
 if 'source_mapping'in j:
  for live,row in j['source_mapping'].items():bind(row['archived'],row['sha256'])
# All archival files below are ordinary preserved bytes. No claim that a changed live
# source has an old historical digest is made.
for p in sorted(V.glob('FINAL_TEXT_*')):
 if p.is_file()and p.name!='FINAL_TEXT_DESIGN_BINDINGS.json':bind(p)
for directory in ['dry_1102','dry_v2','dry_v3']:
 d=json.loads(bind(V/directory/'CHECKS.json'));ck('retained prior dry '+directory,d['status']=='PASS_DRY_FINAL_TEXT_AND_CENSUS'and all(x['passed']for x in d['checks']))
for p,h in bindings.items():ck('final byte agreement '+p,hashlib.sha256(Path(p).read_bytes()).hexdigest()==h)
out=dict(status='CONFIRMED_FINAL_TEXT_DESIGN_ONLY',utc=datetime.now(timezone.utc).isoformat(),count=len(checks),checks=checks,bindings=bindings,actual_reviews=reviews,scope='Current reviewed source, dry predicate and31 controls; explicitly mapped historical failures. No actual final report, installation, endpoint, or verifier end time accepted here.')
p=V/'FINAL_TEXT_DESIGN_BINDINGS.json';ck('fresh output',not p.exists());out['count']=len(checks);p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:out[k]for k in ['status','utc','count']}))
