from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,sys
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/residual_cell_cauchy';R=B/'notes/reviews'
def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def load(p):return json.loads(p.read_text())
def check(v,s):
 if not v:raise ValueError(s)
a=load(D/'evidence/output_audit.json');e=load(D/'evidence/review_extract.json');l=load(D/'evidence/label_audit.json');pins={}
check(a['status']=='PASS_COMPLETE_THREE_CELL_CAUCHY_OUTPUT_AUDIT' and e['status']=='PASS_SCOPED_OUTPUT_REVIEW_EXTRACT' and l['status']=='PASS_EXPLICIT_SAVED_ROW_BINDING_AND_ALL_LABELS','audit statuses')
expected={'cells':3,'coefficient_comparisons':101790,'point_jet_comparisons':18792,'opposite_arithmetic_disk_checks':36,'cell_derivative_bounds':63,'ball_polynomial_products_recorded':6,'integer_polynomial_products_recorded':24}
check(a['counts']==e['counts']==expected,'counts');check(a['comparison_counts']==l['comparison_counts']==e['comparison_counts']=={'INDEPENDENT_UPPER_TOO_LARGE_TO_VALIDATE_SAVED_CAP':63},'all caps unvalidated');check(l['source_rows_checked']==7809 and l['selected_comparisons_checked']==63,'local row guard')
for x in [a,e,l]:
 for n,h in x['files'].items():check(sha(B/n)==h,'source pin');check(n not in pins or pins[n]==h,'pin conflict');pins[n]=h
reviews={}
for tag in ['residual_cell_cauchy_proof','residual_cell_cauchy_code','residual_cell_cauchy_code_followup','residual_cell_cauchy_complete']:
 m=load(R/(tag+'_metadata.json'));raw=load(R/(tag+'_response.json'));request=(R/(tag+'_request.txt')).read_text();text='\n\n'.join(c['text'] for c in raw['content'] if c['type']=='text')+'\n'
 check(m['requested_model']=='us.anthropic.claude-opus-5-5' and m['actual_response_model']==raw['model']=='claude-opus-5-5','actual model');check(m['stop_reason']==raw['stop_reason']==('max_tokens' if tag=='residual_cell_cauchy_code' else 'end_turn'),'review completion or explicit incomplete history');check(hashlib.sha256(request.encode()).hexdigest()==m['input_sha256'],'request digest');check(text==(R/(tag+'_response.md')).read_text(),'raw review text');check(request[request.index('\n\nFILE ')+2:]=='\n\n'.join('FILE '+n+'\n'+(B/n).read_text() for n in m['files']),'current bundle')
 if tag=='residual_cell_cauchy_code_followup':check([v for v in text.splitlines() if v.startswith('VERDICT: ')]==['VERDICT: CONFIRM_SELECTED_CELL_PROOF_AND_CODE_ONLY'],'completed code scope')
 if tag=='residual_cell_cauchy_complete':
  check([v for v in text.splitlines() if v.startswith('VERDICT: ')]==['VERDICT: CONFIRM_THREE_CELL_DERIVATIVE_ENCLOSURES_CANONICAL_INPUTS_INHERITED'],'completed output scope');required=['research/residual_cell_cauchy/PROOF.md','research/residual_cell_cauchy/ADDENDUM.md','research/residual_cell_cauchy/REVIEW_RESOLUTIONS.md','research/residual_cell_cauchy/code/audit_output.py','research/residual_cell_cauchy/code/check_labels.py','research/residual_cell_cauchy/evidence/review_extract.json','research/residual_cell_cauchy/FINAL_ADJUDICATION.md','research/residual_cell_cauchy/code/finalize.py'];check(set(required)<=set(m['files']),'substantive output bundle')
 reviews[tag]={k:m[k] for k in ['actual_response_model','stop_reason','request_id','input_sha256','start_utc','end_utc']};reviews[tag]['counts_as_completed_review']=tag!='residual_cell_cauchy_code'
 for suffix in ['_metadata.json','_response.json','_response.md','_request.txt']:
  p=R/(tag+suffix);pins[str(p.relative_to(B))]=sha(p)
for name in ['PROOF.md','ADDENDUM.md','REVIEW_RESOLUTIONS.md','FINAL_ADJUDICATION.md']:check((D/name).is_file(),'mandatory document')
for p in D.rglob('*'):
 if p.is_file() and not p.is_symlink() and p.name!='verdict.json' and '__pycache__' not in p.parts:
  n=str(p.relative_to(B));h=sha(p);check(n not in pins or pins[n]==h,'final pin conflict');pins[n]=h
for n,h in pins.items():check(sha(B/n)==h,'final digest')
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'CONFIRMED_THREE_CELL_DERIVATIVE_ENCLOSURES_CANONICAL_INPUTS_INHERITED','counts':expected,'comparison_counts':a['comparison_counts'],'reviews':reviews,'files':dict(sorted(pins.items())),'scope':'Mandatory PROOF, ADDENDUM, REVIEW_RESOLUTIONS, FINAL_ADJUDICATION. Three cells only, derivative orders i+j<=5, canonical inputs inherited. All63 bounds exceed saved caps; no validation or refutation of those tighter caps. No global forcing, inverse, nonlinear closure or IPM endpoint.'}
p=D/'evidence/verdict.json'
with p.open('x') as f:json.dump(out,f,indent=2);f.write('\n')
print(json.dumps({'utc':out['utc'],'status':out['status'],'pins':len(pins),'sha256':sha(p)}))
