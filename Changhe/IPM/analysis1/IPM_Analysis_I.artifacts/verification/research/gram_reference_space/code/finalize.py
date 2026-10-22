from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,sys
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/gram_reference_space';R=B/'notes/reviews'
def sha(p):
 with p.open('rb') as h:return hashlib.file_digest(h,'sha256').hexdigest()
def load(p):return json.loads(p.read_text())
def check(x,s):
 if not x:raise ValueError(s)
a=load(D/'evidence/exact_check.json');b=load(D/'evidence/independent_check.json')
check(a['status']=='PASS_EXACT_POLYNOMIAL_LAURENT_AND_SELECTED_SOURCE_CHECKS' and b['status']=='PASS_INDEPENDENT_BETA_CARTESIAN_AND_SOURCE_AUDIT','completed calculations')
check(b['exact_result_sha256']==sha(D/'evidence/exact_check.json') and b['code_sha256']==sha(D/'code/independent_check.py'),'audit source')
check(b['input_hashes_checked']==19 and b['bindings_checked']==14 and b['floating_records_checked']==9,'counts')
pins=dict(a['files'])
for name,h in pins.items():check(sha(B/name)==h,'input '+name)
check(load(D/'evidence/proof_first.json')['proof_sha256']==sha(D/'PROOF.md'),'proof first')
reviews={}
for tag,expected,stop in [('gram_reference_proof','45fcd509008784a20963599823fa1d8192836cd78ec9898ec091def4427bd0cb','max_tokens'),('gram_reference_complete','7d8d45b922ea73fc3a65393b888115e917a51729adeb6bfb6ec1c9bfc23c5c9f','end_turn'),('gram_reference_scope',None,'end_turn')]:
 m=load(R/(tag+'_metadata.json'));raw=load(R/(tag+'_response.json'));req=(R/(tag+'_request.txt')).read_text()
 check(m['requested_model']=='us.anthropic.claude-opus-5-5' and m['actual_response_model']==raw['model']=='claude-opus-5-5' and m['stop_reason']==raw['stop_reason']==stop,'actual model')
 check(hashlib.sha256(req.encode()).hexdigest()==m['input_sha256'] and (expected is None or expected==m['input_sha256']),'request digest')
 check(req[req.index('\n\nFILE ')+2:]=='\n\n'.join('FILE '+f+'\n'+(B/f).read_text() for f in m['files']),'current bundle')
 text='\n\n'.join(q['text'] for q in raw['content'] if q['type']=='text')+'\n';check(text==(R/(tag+'_response.md')).read_text(),'raw text')
 if tag=='gram_reference_complete':check('CONFIRMED_J_REFERENCE_SPACE_OBSTRUCTION_AND_UNBOUNDED_CENTER_COEFFICIENT is justified' in text,'accepted theorem')
 if tag=='gram_reference_scope':check('ACCEPTED as restricted. No substantive disagreement remains.' in text and 'withdrawn' in text,'final scope')
 reviews[tag]={k:m[k] for k in ['actual_response_model','stop_reason','request_id','input_sha256','start_utc','end_utc']}
 for s in ['_metadata.json','_response.json','_response.md','_request.txt']:
  p=R/(tag+s);pins[str(p.relative_to(B))]=sha(p)
for root in [D,D/'code',D/'evidence',D/'sources']:
 for p in root.iterdir():
  if not p.is_file() or p.is_symlink() or p.name=='verdict.json':continue
  name=str(p.relative_to(B));h=sha(p);check(name not in pins or pins[name]==h,'hash conflict');pins[name]=h
out=dict(utc=datetime.now(timezone.utc).isoformat(),status='CONFIRMED_J_REFERENCE_SPACE_OBSTRUCTION_AND_UNBOUNDED_CENTER_COEFFICIENT',refuted='Global H1m/H1 norm and angle interpretation for the explicitly listed jumping references; not the floating conforming SVD.',open='Spline and tail exact conformity, actual finite spectrum, continuum bounds, stronger final inverse domain, all PDE endpoints.',reviews=reviews,files=dict(sorted(pins.items())),scope='Mandatory FINAL_ADJUDICATION, PROOF, ADDENDUM and FINAL_SCOPE. Current source/JSON snapshots, no historical matrix replay.')
p=D/'evidence/verdict.json';check(not p.exists(),'immutable output');p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'utc':out['utc'],'status':out['status'],'pins':len(pins),'sha256':sha(p)}))
