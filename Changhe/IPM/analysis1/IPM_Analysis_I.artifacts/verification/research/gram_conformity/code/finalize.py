from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,sys
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/gram_conformity';R=B/'notes/reviews'
def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def load(p):return json.loads(p.read_text())
def check(v,s):
 if not v:raise ValueError(s)
a=load(D/'evidence/exact_check.json');b=load(D/'evidence/independent_check.json')
check(a['status']=='PASS_EXPANDED_POLYNOMIAL_AND_AFFINE_EXPONENT_CHECKS','exact status')
check(b['status']=='PASS_METRIC_PULLBACK_PHYSICAL_EXPONENTS_AND_ANTIDERIVATIVE_RECURRENCE','independent status')
pins={}
for r in [a,b]:
 check(r['prior_pins_rechecked']==40,'inherited count')
 for n,h in r['files'].items():check(sha(B/n)==h,'current arithmetic '+n);pins[n]=h
prior=load(B/'research/gram_reference_space/evidence/verdict.json');check(len(prior['files'])==40,'prior count')
for n,h in prior['files'].items():check(sha(B/n)==h,'prior '+n);check(n not in pins or pins[n]==h,'pin conflict');pins[n]=h
check(load(D/'evidence/proof_first.json')['proof_sha256']==sha(D/'evidence/first_review_snapshot/PROOF.md'),'original proof binding')
reviews={}
for tag,stop in [('gram_conformity_proof','max_tokens'),('gram_conformity_complete','end_turn')]:
 m=load(R/(tag+'_metadata.json'));raw=load(R/(tag+'_response.json'));req=(R/(tag+'_request.txt')).read_text()
 check(m['requested_model']=='us.anthropic.claude-opus-5-5' and m['actual_response_model']==raw['model']=='claude-opus-5-5','actual model')
 check(m['stop_reason']==raw['stop_reason']==stop,'stop reason');check(hashlib.sha256(req.encode()).hexdigest()==m['input_sha256'],'request digest')
 chunks=[]
 for n in m['files']:
  p=B/n
  if tag=='gram_conformity_proof' and n in ['research/gram_conformity/PROOF.md','research/gram_conformity/evidence/exact_check.json','research/gram_conformity/evidence/independent_check.json']:p=D/'evidence/first_review_snapshot'/p.name
  chunks.append('FILE '+n+'\n'+p.read_text())
 check(req[req.index('\n\nFILE ')+2:]=='\n\n'.join(chunks),'review bundle')
 text='\n\n'.join(q['text'] for q in raw['content'] if q['type']=='text')+'\n';check(text==(R/(tag+'_response.md')).read_text(),'raw text')
 if stop=='end_turn':check('CONFIRMED_EXACT_CONTINUITY_CRITERION_AND_DENSE_CENTER_LEVEL_SETS is accepted' in text and 'no unresolved substantive objection' in text,'acceptance')
 reviews[tag]={k:m[k] for k in ['actual_response_model','stop_reason','request_id','input_sha256','start_utc','end_utc']}
 for suffix in ['_metadata.json','_response.json','_response.md','_request.txt']:
  p=R/(tag+suffix);pins[str(p.relative_to(B))]=sha(p)
for p in D.rglob('*'):
 if p.is_file() and not p.is_symlink() and p.name!='verdict.json':
  n=str(p.relative_to(B));h=sha(p);check(n not in pins or pins[n]==h,'final conflict');pins[n]=h
for n,h in pins.items():check(sha(B/n)==h,'final pin')
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'CONFIRMED_EXACT_CONTINUITY_CRITERION_AND_DENSE_CENTER_LEVEL_SETS','reviews':reviews,'files':dict(sorted(pins.items())),'scope':'Mandatory current PROOF and FINAL_ADJUDICATION. Actual floating conformity, spectra, operator near-kernels, continuum convergence, full inverse and PDE endpoints OPEN.'}
p=D/'evidence/verdict.json';check(not p.exists(),'immutable output');p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'utc':out['utc'],'status':out['status'],'pins':len(pins),'sha256':sha(p)}))
