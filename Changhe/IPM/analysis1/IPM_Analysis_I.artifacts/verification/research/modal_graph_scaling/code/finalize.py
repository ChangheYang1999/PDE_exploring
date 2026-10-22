from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,sys
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/modal_graph_scaling';R=B/'notes/reviews'
def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def load(p):return json.loads(p.read_text())
def check(v,s):
 if not v:raise ValueError(s)
pins={}
for name,status in [('compute.json','PASS_SYMBOLIC_SPATIAL_IDENTITIES_AND_EXACT_MODAL_INPUT_CONDITIONS'),('independent.json','PASS_INDEPENDENT_HEX_DECIMAL_PARSING_FREE_JET_ALGEBRA_AND_FINITE_RESONANCES'),('nonzero_image.json','PASS_TWO_EXACT_SCALING_IMAGE_COEFFICIENT_DERIVATIONS_ARB512_AND_IV180')]:
 a=load(D/'evidence'/name);check(a['status']==status,'calculation status')
 for n,h in a['files'].items():check(sha(B/n)==h,'calculation pin');check(n not in pins or pins[n]==h,'conflict');pins[n]=h
check(load(D/'evidence/proof_first.json')['proof_sha256']==sha(D/'PROOF.md'),'proof first')
reviews={}
for tag,stop in [('modal_graph_scaling_proof','end_turn'),('modal_graph_scaling_final','end_turn')]:
 m=load(R/(tag+'_metadata.json'));raw=load(R/(tag+'_response.json'));req=(R/(tag+'_request.txt')).read_text()
 check(m['requested_model']=='us.anthropic.claude-opus-5-5' and m['actual_response_model']==raw['model']=='claude-opus-5-5','actual model');check(m['stop_reason']==raw['stop_reason']==stop,'stop');check(hashlib.sha256(req.encode()).hexdigest()==m['input_sha256'],'request digest')
 check(req[req.index('\n\nFILE ')+2:]=='\n\n'.join('FILE '+n+'\n'+(B/n).read_text() for n in m['files']),'current bundle')
 text='\n\n'.join(q['text'] for q in raw['content'] if q['type']=='text')+'\n';check(text==(R/(tag+'_response.md')).read_text(),'raw text')
 if tag=='modal_graph_scaling_final':check('VERDICT: CONFIRM_ACTUAL_MODAL_GRAPH_SCALING_NONZERO_IMAGE' in text.splitlines(),'accepted restricted theorem')
 reviews[tag]={k:m[k] for k in ['actual_response_model','stop_reason','request_id','input_sha256','start_utc','end_utc']}
 for suffix in ['_metadata.json','_response.json','_response.md','_request.txt']:
  p=R/(tag+suffix);pins[str(p.relative_to(B))]=sha(p)
for n in ['PROOF.md','ADDENDUM.md','NONZERO_IMAGE.md','REVIEW_RESOLUTIONS.md','FINAL_ADJUDICATION.md']:check((D/n).is_file(),'mandatory document')
for p in D.rglob('*'):
 if p.is_file() and not p.is_symlink() and p.name!='verdict.json':
  n=str(p.relative_to(B));h=sha(p);check(n not in pins or pins[n]==h,'final conflict');pins[n]=h
for n,h in pins.items():check(sha(B/n)==h,'final pin')
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'CONFIRMED_ACTUAL_MODAL_GRAPH_SCALING_AND_NONZERO_IMAGE','reviews':reviews,'files':dict(sorted(pins.items())),'scope':'Mandatory PROOF,ADDENDUM,NONZERO_IMAGE,REVIEW_RESOLUTIONS,FINAL_ADJUDICATION. Actual exact modal scaling vector belongs to the specified broad X graph domain, J=-2, Sigma=0, LK=epsilon-Eepsilon is nonzero, and K has a nonzero leading tail. Necessary inverse quotient only, not numerically evaluated. No fixed-tail inclusion, actual kernel, matrix transfer, inverse, nonlinear closure or PDE endpoint.'}
p=D/'evidence/verdict.json';check(not p.exists(),'immutable output');p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'utc':out['utc'],'status':out['status'],'pins':len(pins),'sha256':sha(p)}))
