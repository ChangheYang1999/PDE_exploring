from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,sys
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/gram_jump_rank';R=B/'notes/reviews'
def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def load(p):return json.loads(p.read_text())
def check(v,s):
 if not v:raise ValueError(s)
pins={}
for name,status in [('compute.json','PASS_EXACT_TRIANGULAR_JUMP_RANK_AND_REPORTED_COUNT_COMPARISON'),('independent.json','PASS_INDEPENDENT_STRUCTURAL_ZEROS_MODULAR_RANK_AND_DIRECT_POWER_SUM'),('summary.json','PASS_STRUCTURED_RADIAL_COPY_AND_DIAGONAL_PRODUCT_AUDIT'),('extra_columns.json','PASS_LOCAL_PIECE_REGULARITY_AND_ACTUAL_M24_FREE_COLUMN_COUNT'),('selectors.json','PASS_ALL_SELECTED_COORDINATES_IN_ALL_SECTIONS_AND_RAW_SHAPES')]:
 a=load(D/'evidence'/name);check(a['status']==status,'calculation status')
 for n,h in a['files'].items():check(sha(B/n)==h,'calculation pin');check(n not in pins or pins[n]==h,'conflict');pins[n]=h
check(load(D/'evidence/proof_first.json')['proof_sha256']==sha(D/'PROOF.md'),'proof first')
reviews={}
for tag,stop in [('gram_jump_rank_proof','end_turn'),('gram_jump_rank_final','end_turn')]:
 m=load(R/(tag+'_metadata.json'));raw=load(R/(tag+'_response.json'));req=(R/(tag+'_request.txt')).read_text()
 check(m['requested_model']=='us.anthropic.claude-opus-5-5' and m['actual_response_model']==raw['model']=='claude-opus-5-5','actual model');check(m['stop_reason']==raw['stop_reason']==stop,'stop');check(hashlib.sha256(req.encode()).hexdigest()==m['input_sha256'],'request digest')
 check(req[req.index('\n\nFILE ')+2:]=='\n\n'.join('FILE '+n+'\n'+(B/n).read_text() for n in m['files']),'current bundle')
 text='\n\n'.join(q['text'] for q in raw['content'] if q['type']=='text')+'\n';check(text==(R/(tag+'_response.md')).read_text(),'raw text')
 if tag=='gram_jump_rank_final':check('CONFIRM `CONFIRMED_ENCODED_SPAN_CONFORMING_DIMENSION_UPPER_BOUNDS`' in text and 'Gap 6.1 from my prior review is now closed' in text,'accepted restricted theorem')
 reviews[tag]={k:m[k] for k in ['actual_response_model','stop_reason','request_id','input_sha256','start_utc','end_utc']}
 for suffix in ['_metadata.json','_response.json','_response.md','_request.txt']:
  p=R/(tag+suffix);pins[str(p.relative_to(B))]=sha(p)
for p in D.rglob('*'):
 if p.is_file() and not p.is_symlink() and p.name!='verdict.json':
  n=str(p.relative_to(B));h=sha(p);check(n not in pins or pins[n]==h,'final conflict');pins[n]=h
for n,h in pins.items():check(sha(B/n)==h,'final pin')
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'CONFIRMED_ENCODED_SPAN_CONFORMING_DIMENSION_UPPER_BOUNDS','reviews':reviews,'files':dict(sorted(pins.items())),'scope':'Mandatory PROOF,ADDENDUM,REVIEW_RESOLUTIONS,FINAL_ADJUDICATION. Exact encoded-span conforming dimension upper bounds; no actual Q rank, historical SVD, reconstruction or PDE claim.'}
p=D/'evidence/verdict.json';check(not p.exists(),'immutable output');p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'utc':out['utc'],'status':out['status'],'pins':len(pins),'sha256':sha(p)}))
