from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,sys
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/residual_point_jets';R=B/'notes/reviews'
def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def load(p):return json.loads(p.read_text())
def check(v,s):
 if not v:raise ValueError(s)
pins={};a=load(D/'evidence/output_audit.json');e=load(D/'evidence/review_extract.json')
check(a['status']=='PASS_COMPLETE_THIRTEEN_POINT_DERIVATIVE_OUTPUT_AUDIT','status')
for v in [a,e]:
 for n,h in v['files'].items():check(sha(B/n)==h,'source pin');check(n not in pins or pins[n]==h,'pin conflict');pins[n]=h
check(a['counts']==e['counts'],'extract counts')
check(a['counts']=={'coefficient_comparisons':40716,'order_zero_prior_comparisons':6786,'exact_Wiener_checks':273,'points':13,'integer_polynomial_products':2184,'Arb_scatter_pairs':5313438,'CONSISTENT_AT_SAMPLE':138,'NO_SAVED_FIELD':135},'full counts')
first=load(D/'evidence/proof_first.json');check(first['proof_sha256']==sha(D/'PROOF.md'),'proof first digest')
check(datetime.fromisoformat(first['utc'])<min(datetime.fromisoformat(load(D/'evidence'/('arb_%d.json'%r['cell']))['utc']) for r in a['records']),'proof before derivative outputs')
reviews={}
for tag in ['residual_point_jets_proof','residual_point_jets_preparation_followup','residual_point_jets_complete']:
 m=load(R/(tag+'_metadata.json'));raw=load(R/(tag+'_response.json'));request=(R/(tag+'_request.txt')).read_text()
 check(m['requested_model']=='us.anthropic.claude-opus-5-5' and m['actual_response_model']==raw['model']=='claude-opus-5-5','actual model');check(m['stop_reason']==raw['stop_reason']=='end_turn','review completed')
 check(hashlib.sha256(request.encode()).hexdigest()==m['input_sha256'],'request digest')
 check(request[request.index('\n\nFILE ')+2:]=='\n\n'.join('FILE '+n+'\n'+(B/n).read_text() for n in m['files']),'current bundle')
 text='\n\n'.join(c['text'] for c in raw['content'] if c['type']=='text')+'\n';check(text==(R/(tag+'_response.md')).read_text(),'raw text')
 if tag=='residual_point_jets_complete':check('VERDICT: CONFIRM_FINITE_POINT_DERIVATIVE_ENCLOSURES_CANONICAL_INPUTS_INHERITED' in text.splitlines(),'scoped accepted verdict')
 reviews[tag]={k:m[k] for k in ['actual_response_model','stop_reason','request_id','input_sha256','start_utc','end_utc']}
 for suffix in ['_metadata.json','_response.json','_response.md','_request.txt']:
  p=R/(tag+suffix);pins[str(p.relative_to(B))]=sha(p)
for n in ['PROOF.md','ADDENDUM.md','REVIEW_RESOLUTIONS.md','FINAL_ADJUDICATION.md']:check((D/n).is_file(),'mandatory proof document')
for p in D.rglob('*'):
 if p.is_file() and not p.is_symlink() and p.name!='verdict.json':
  n=str(p.relative_to(B));h=sha(p);check(n not in pins or pins[n]==h,'final conflict');pins[n]=h
for n,h in pins.items():check(sha(B/n)==h,'final digest')
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'CONFIRMED_FINITE_POINT_DERIVATIVE_ENCLOSURES_CANONICAL_INPUTS_INHERITED','reviews':reviews,'counts':a['counts'],'files':dict(sorted(pins.items())),'scope':'Mandatory PROOF,ADDENDUM,REVIEW_RESOLUTIONS,FINAL_ADJUDICATION. Thirteen point enclosures through order five. Canonical moment inputs inherited; no new integration. No whole-cell derivative enclosure, global forcing norm, inverse, nonlinear closure or endpoint.'}
p=D/'evidence/verdict.json'
with p.open('x') as f:json.dump(out,f,indent=2);f.write('\n')
print(json.dumps({'utc':out['utc'],'status':out['status'],'pins':len(pins),'sha256':sha(p)}))
