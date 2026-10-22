from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,sys
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/gram_c2_repair';R=B/'notes/reviews'
def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def load(p):return json.loads(p.read_text())
def check(v,s):
 if not v:raise ValueError(s)
pins={}
for name,status in [('compute.json', 'PASS_EXACT_C2_HERMITE_LINEAR_SYSTEM_AND_ARB512_BROKEN_NORM_BOUNDS'), ('independent.json', 'PASS_INDEPENDENT_NUMPY_FREE_IEEE_HERMITE_BASIS_HILBERT_MOMENTS_AND_IV120'), ('binding.json', 'PASS_SAME_RAW_FAMILY_COMMON_PARTITION_WEIGHT_AND_C0_BINDING'), ('norm_semantics.json', 'PASS_C0_FIELD_IS_NORM_RATIO_BY_EXACT_SQUARED_INEQUALITIES_AND_SOURCE_AST')]:
 a=load(D/'evidence'/name);check(a['status']==status,'calculation status')
 for n,h in a['files'].items():check(sha(B/n)==h,'calculation pin');check(n not in pins or pins[n]==h,'conflict');pins[n]=h
check(load(D/'evidence/proof_first.json')['proof_sha256']==sha(D/'PROOF.md'),'proof first')
reviews={}
for tag,stop in [('gram_c2_repair_proof','end_turn'),('gram_c2_repair_final','end_turn'),('gram_c2_repair_norm_final','end_turn')]:
 m=load(R/(tag+'_metadata.json'));raw=load(R/(tag+'_response.json'));req=(R/(tag+'_request.txt')).read_text()
 check(m['requested_model']=='us.anthropic.claude-opus-5-5' and m['actual_response_model']==raw['model']=='claude-opus-5-5','actual model');check(m['stop_reason']==raw['stop_reason']==stop,'stop');check(hashlib.sha256(req.encode()).hexdigest()==m['input_sha256'],'request digest')
 check(req[req.index('\n\nFILE ')+2:]=='\n\n'.join('FILE '+n+'\n'+(B/n).read_text() for n in m['files']),'current bundle')
 text='\n\n'.join(q['text'] for q in raw['content'] if q['type']=='text')+'\n';check(text==(R/(tag+'_response.md')).read_text(),'raw text')
 if tag=='gram_c2_repair_norm_final':check('VERDICT: CONFIRM_SCOPED_C2_REPAIR' in text.splitlines(),'accepted restricted theorem')
 reviews[tag]={k:m[k] for k in ['actual_response_model','stop_reason','request_id','input_sha256','start_utc','end_utc']}
 for suffix in ['_metadata.json','_response.json','_response.md','_request.txt']:
  p=R/(tag+suffix);pins[str(p.relative_to(B))]=sha(p)
for n in ['PROOF.md','ADDENDUM.md','REVIEW_RESOLUTIONS.md','NORM_SEMANTICS.md','FINAL_ADJUDICATION.md']:check((D/n).is_file(),'mandatory document')
for p in D.rglob('*'):
 if p.is_file() and not p.is_symlink() and p.name!='verdict.json':
  n=str(p.relative_to(B));h=sha(p);check(n not in pins or pins[n]==h,'final conflict');pins[n]=h
for n,h in pins.items():check(sha(B/n)==h,'final pin')
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'CONFIRMED_EXACT_C2_SPLINE_REPAIR_AND_SINGLE_COLUMN_NORM_BOUNDS','reviews':reviews,'files':dict(sorted(pins.items())),'scope':'Mandatory PROOF,ADDENDUM,REVIEW_RESOLUTIONS,NORM_SEMANTICS,FINAL_ADJUDICATION. New exact C2,1 repairs,277 columns,13296 jet checks; norm ratios and true single-column X distance only. No matrix, operator-image norm, inverse or endpoint transfer.'}
p=D/'evidence/verdict.json';check(not p.exists(),'immutable output');p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'utc':out['utc'],'status':out['status'],'pins':len(pins),'sha256':sha(p)}))
