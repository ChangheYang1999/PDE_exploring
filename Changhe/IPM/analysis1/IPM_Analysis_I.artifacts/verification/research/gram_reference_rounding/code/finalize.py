from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,sys
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/gram_reference_rounding';R=B/'notes/reviews'
def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def load(p):return json.loads(p.read_text())
def check(v,s):
 if not v:raise ValueError(s)
pins={}
for name,status in [('compute.json', 'PASS_FROZEN_STEP_REPRODUCTION_AND_EXACT_ENDPOINT_AUDIT'), ('independent.json', 'PASS_INDEPENDENT_HEX_IEEE_NPY_AND_DIRECT_DERIVATIVE_SUMS'), ('float_binding.json', 'PASS_EXACT_RATIONAL_POWERS_AND_NEAREST_EVEN_SOURCE_COEFFICIENT_REPRODUCTION')]:
 a=load(D/'evidence'/name);check(a['status']==status,'calculation status')
 for n,h in a['files'].items():check(sha(B/n)==h,'calculation pin');check(n not in pins or pins[n]==h,'conflict');pins[n]=h
check(load(D/'evidence/proof_first.json')['proof_sha256']==sha(D/'PROOF.md'),'proof first')
reviews={}
for tag,stop in [('gram_reference_rounding_proof','end_turn'),('gram_reference_rounding_final','end_turn')]:
 m=load(R/(tag+'_metadata.json'));raw=load(R/(tag+'_response.json'));req=(R/(tag+'_request.txt')).read_text()
 check(m['requested_model']=='us.anthropic.claude-opus-5-5' and m['actual_response_model']==raw['model']=='claude-opus-5-5','actual model');check(m['stop_reason']==raw['stop_reason']==stop,'stop');check(hashlib.sha256(req.encode()).hexdigest()==m['input_sha256'],'request digest')
 check(req[req.index('\n\nFILE ')+2:]=='\n\n'.join('FILE '+n+'\n'+(B/n).read_text() for n in m['files']),'current bundle')
 text='\n\n'.join(q['text'] for q in raw['content'] if q['type']=='text')+'\n';check(text==(R/(tag+'_response.md')).read_text(),'raw text')
 if tag=='gram_reference_rounding_final':check('VERDICT: CONFIRM_SCOPED_REFERENCES' in text.splitlines(),'accepted restricted theorem')
 reviews[tag]={k:m[k] for k in ['actual_response_model','stop_reason','request_id','input_sha256','start_utc','end_utc']}
 for suffix in ['_metadata.json','_response.json','_response.md','_request.txt']:
  p=R/(tag+suffix);pins[str(p.relative_to(B))]=sha(p)
for n in ['PROOF.md','ADDENDUM.md','REVIEW_RESOLUTIONS.md','FINAL_ADJUDICATION.md']:check((D/n).is_file(),'mandatory document')
for p in D.rglob('*'):
 if p.is_file() and not p.is_symlink() and p.name!='verdict.json':
  n=str(p.relative_to(B));h=sha(p);check(n not in pins or pins[n]==h,'final conflict');pins[n]=h
for n,h in pins.items():check(sha(B/n)==h,'final pin')
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'CONFIRMED_UNIT_WIDTH_REFERENCE_C4_AND_REFUTED_ENCODED_WIDE_REFERENCE_CONFORMITY','reviews':reviews,'files':dict(sorted(pins.items())),'scope':'Mandatory PROOF,ADDENDUM,REVIEW_RESOLUTIONS,FINAL_ADJUDICATION. Frozen current source reproduced on captured M24 scalars: two references C4, wide reference outside X. No historical/future matrix or singular vector, spectrum, inverse or PDE claim.'}
p=D/'evidence/verdict.json';check(not p.exists(),'immutable output');p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'utc':out['utc'],'status':out['status'],'pins':len(pins),'sha256':sha(p)}))
