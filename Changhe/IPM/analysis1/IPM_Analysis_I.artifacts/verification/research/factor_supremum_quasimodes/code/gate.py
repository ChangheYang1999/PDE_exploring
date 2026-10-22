"""Strict local provenance and acceptance gate for topic213. No PDE computation."""
import sys,json,hashlib,os
from pathlib import Path
from datetime import datetime,timezone
if sys.flags.optimize:raise RuntimeError('optimized Python is forbidden')
sys.dont_write_bytecode=True
ROOT=Path(__file__).resolve().parents[3];D=ROOT/'research/factor_supremum_quasimodes';E=D/'evidence';R=ROOT/'notes/reviews'
def now():return datetime.now(timezone.utc).isoformat()
def dt(s):
 x=datetime.fromisoformat(s)
 if x.tzinfo is None:raise ValueError('timezone required')
 return x
def pairs(ps):
 d={}
 for k,v in ps:
  if k in d:raise ValueError('duplicate JSON key')
  d[k]=v
 return d
def load(p):return json.loads(Path(p).read_text(),object_pairs_hook=pairs,parse_constant=lambda s:(_ for _ in ()).throw(ValueError(s)))
def sha(p):
 with Path(p).open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def check(b,msg):
 if not b:raise RuntimeError(msg)
def save(p,v):
 p=Path(p);check(p.resolve().is_relative_to(D),'outside write')
 with p.open('x') as f:f.write(json.dumps(v,indent=2,allow_nan=False)+'\n');f.flush();os.fsync(f.fileno())
def pin(pins,n,h=None):
 p=ROOT/n;got=sha(p);check(h is None or got==h,'changed '+str(n));check(n not in pins or pins[n]==got,'conflicting pin');pins[n]=got

def auth(pins,tag,terminal,rebind=None):
 m=load(R/(tag+'_metadata.json'));v=load(R/(tag+'_response.json'));text=(R/(tag+'_response.md')).read_text();req=(R/(tag+'_request.txt')).read_text();rebind=rebind or {}
 check(m['requested_model']=='us.anthropic.claude-opus-5-5' and m['actual_response_model']==v['model']=='claude-opus-5-5','wrong model')
 check(m['stop_reason']==v['stop_reason']=='end_turn' and 'availability_error' not in m,'incomplete response')
 pre=req.split('\n\nFILE ',1)[0]
 for phrase in ['no JavaScript/TypeScript','no servers/listeners/tunnels','no RLScience cluster']:check(phrase in pre,'restriction missing')
 check(len(set(m['files']))==len(m['files']),'duplicate input')
 body=pre+'\n\n'+'\n\n'.join('FILE '+n+'\n'+(ROOT/rebind.get(n,n)).read_text() for n in m['files'])
 check(req==body and hashlib.sha256(req.encode()).hexdigest()==m['input_sha256'],'input reconstruction failed')
 check(text=='\n\n'.join(c['text'] for c in v['content'] if c['type']=='text')+'\n','response reconstruction failed')
 check(text.rstrip().splitlines()[-1]==terminal,'terminal mismatch')
 check(dt(m['start_utc'])<dt(m['end_utc'])<datetime.now(timezone.utc),'review timing')
 for n in m['files']:pin(pins,rebind.get(n,n))
 for s in ['metadata.json','request.txt','response.json','response.md']:pin(pins,str((R/(tag+'_'+s)).relative_to(ROOT)))
 return {k:m[k] for k in ['request_id','requested_model','actual_response_model','input_sha256','start_utc','end_utc','stop_reason']}

P='research/canonical_residual_composition/evidence/verdict.json'
PH='902700a07aa5078bcdeb4082a6d217d42382c9b88a60632e5040dfb387328222'
OWN=['PROOF.md','DEPENDENCY_SCOPE.md','PROOF_REVIEW1_ADJUDICATION.md','FOLLOWUP_ADJUDICATION.md','code/symbolic_check.py','code/rational_check.py','code/gate.py','evidence/proof_first.json','evidence/proof_first_v2.json','evidence/proof_version3.json','evidence/proof_review1.md','evidence/symbolic_check_initial.py.txt','evidence/initial_symbolic_failure.json','evidence/symbolic_checks.json','evidence/rational_checks.json','evidence/followup_adjudication.json']

def core():
 pins={};v=load(ROOT/P);check(v['status']=='CONFIRMED_CANONICAL_RESIDUAL_ARCHIVE_PREMISE_DISCHARGED','parent status');pin(pins,P,PH)
 for n,h in v['files'].items():pin(pins,n,h)
 for n in ['research/canonical_inverse/evidence/audit_verdict.json','research/canonical_inverse/PROOF.md','research/trial_regularities/PROOF.md']:
  pin(pins,n)
 a=load(ROOT/'research/modal_repair/evidence/audit_verdict.json');check(a['verdict']=='CONFIRMED','normalization status')
 for n,h in a['source_and_evidence_sha256'].items():pin(pins,n,h)
 for n in OWN:pin(pins,str((D/n).relative_to(ROOT)))
 for stem,status,src in [('symbolic_checks','PASS_SYMBOLIC_IDENTITIES','symbolic_check.py'),('rational_checks','PASS_INDEPENDENT_RATIONAL_DIFFERENTIAL_RING','rational_check.py')]:
  c=load(E/(stem+'.json'));check(c['status']==status and all(x is True for x in c['checks'].values()),'finite checks failed');check(c['source_sha256']==sha(D/'code'/src) and c['proof_sha256']==sha(D/'PROOF.md'),'finite source mismatch')
 first=auth(pins,'factor213_proof','CONFIRM_FACTOR_SUPREMUM_QUASIMODE_PROOF',{'research/factor_supremum_quasimodes/PROOF.md':'research/factor_supremum_quasimodes/evidence/proof_review1.md'})
 follow=auth(pins,'factor213_followup','CONFIRM_REPAIRED_FACTOR_SUPREMUM_QUASIMODES_AND_FINITE_CHECKS')
 post=load(E/'followup_adjudication.json');check(post['request_id']==follow['request_id'] and post['response_sha256']==sha(R/'factor213_followup_response.json') and post['adjudication_sha256']==sha(D/'FOLLOWUP_ADJUDICATION.md'),'followup disposition mismatch');check(dt(first['end_utc'])<dt(follow['start_utc'])<dt(follow['end_utc'])<dt(post['utc']),'followup ordering');check(post['all_substantive_objections_resolved'] is True,'open objection')
 return pins,first,follow

if __name__=='__main__':
 action=sys.argv[1]
 if action=='prepare':
  pins,a,b=core();save(E/'prepared_packet.json',{'utc':now(),'status':'PREPARED_NOT_FINAL','parent':{'path':P,'sha256':PH,'pins':len(load(ROOT/P)['files'])},'first_review':a,'followup_review':b,'files':dict(sorted(pins.items()))});print('PREPARED',len(pins))
 elif action=='finalize':
  check(not (E/'verdict.json').exists(),'already final');pins,a,b=core();packet=load(E/'prepared_packet.json');check(packet['files']==dict(sorted(pins.items())),'prepared source changed');pin(pins,str((E/'prepared_packet.json').relative_to(ROOT)))
  actual=auth(pins,'factor213_actual','CONFIRM_FACTOR_SUPREMUM_QUASIMODES_COMPLETED_PACKET');check(dt(packet['utc'])<dt(actual['start_utc']),'actual did not follow packet')
  post=load(E/'final_adjudication.json');check(post['status']=='CONFIRMED_AFTER_COMPLETE_ACTUAL_REVIEW_AND_OWN_ADJUDICATION' and post['request_id']==actual['request_id'] and post['input_sha256']==actual['input_sha256'] and post['response_sha256']==sha(R/'factor213_actual_response.json') and post['adjudication_sha256']==sha(D/'FINAL_ADJUDICATION.md') and post['all_substantive_objections_resolved'] is True,'final disposition mismatch');check(dt(actual['end_utc'])<dt(post['utc'])<datetime.now(timezone.utc),'final timing')
  pin(pins,str((D/'FINAL_ADJUDICATION.md').relative_to(ROOT)));pin(pins,str((E/'final_adjudication.json').relative_to(ROOT)))
  save(E/'verdict.json',{'utc':now(),'status':'CONFIRMED_FACTOR_SUPREMUM_STRAIN_ZERO_WEAK_NULL_QUASIMODES','scope':'Under stated background hypotheses, unit weak-null smooth compact exact-strain-zero quasimodes in the continuous weighted factor supremum norm. No containing closed linear Fredholm realization and no bounded linear compact remainder estimate in that norm. Application to exact canonical modal trial. No X3 distance, inverse in another norm, nonlinear closure or decisive endpoint.','first_review':a,'followup_review':b,'actual_review':actual,'postreview':post,'mandatory_addenda':['DEPENDENCY_SCOPE.md','PROOF_REVIEW1_ADJUDICATION.md','FOLLOWUP_ADJUDICATION.md','FINAL_ADJUDICATION.md'],'files':dict(sorted(pins.items()))});print('FINAL',len(pins),sha(E/'verdict.json'))
 else:raise ValueError(action)
