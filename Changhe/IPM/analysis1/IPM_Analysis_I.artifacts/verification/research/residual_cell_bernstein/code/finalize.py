"""Accept only completed outputs, explicit guards and actual scoped Opus reviews."""
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,sys,os
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/residual_cell_bernstein';R=B/'notes/reviews'
def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def load(p):return json.loads(p.read_text())
def check(v,s):
 if not v:raise ValueError(s)
a=load(D/'evidence/output_audit.json');g=load(D/'evidence/guard_audit.json');e=load(D/'evidence/review_extract.json');pins={}
check(a['status']=='PASS_COMPLETE_THREE_CELL_BERNSTEIN_RANGE_AUDIT' and g['status']=='PASS_EXPLICIT_INPUT_PINS_DIMENSIONS_CHRONOLOGY_AND_ORDER_BINDING' and e['status']=='PASS_SCOPED_COMPLETED_BERNSTEIN_REVIEW_EXTRACT','statuses')
expected={'cells':3,'mode_records':1566,'chunks':27,'saved_modal_maximum_enclosure_checks':75168,'coefficient_radius_checks':9396,'recorded_Bernstein_coefficient_checks':4698000,'coefficient_stream_matches':9396,'cell_derivative_bounds':63}
check(a['counts']==e['counts']==expected,'counts');check(a['comparison_counts']==e['comparison_counts'] and sum(a['comparison_counts'].values())==63,'comparisons');check(g['coefficient_row_dimensions_checked']==3132 and g['cell_derivative_bindings']==63 and g['chunk_chronology_and_primary_pins_checked']==27,'guard counts')
for obj in [a,g,e]:
 for n,h in obj['files'].items():check(sha(B/n)==h,'current source digest');check(n not in pins or pins[n]==h,'digest conflict');pins[n]=h
reviews={}
for tag in ['residual_cell_bernstein_proof','residual_cell_bernstein_code','residual_cell_bernstein_complete']:
 m=load(R/(tag+'_metadata.json'));raw=load(R/(tag+'_response.json'));request=(R/(tag+'_request.txt')).read_text();text='\n\n'.join(c['text'] for c in raw['content'] if c['type']=='text')+'\n'
 check(m['requested_model']=='us.anthropic.claude-opus-5-5' and m['actual_response_model']==raw['model']=='claude-opus-5-5','actual model');check(m['stop_reason']==raw['stop_reason']=='end_turn','completed review');check(hashlib.sha256(request.encode()).hexdigest()==m['input_sha256'],'request digest');check(text==(R/(tag+'_response.md')).read_text(),'raw review text');check(request[request.index('\n\nFILE ')+2:]=='\n\n'.join('FILE '+n+'\n'+(B/n).read_text() for n in m['files']),'current review bundle')
 lines=[v.strip().strip('*').strip() for v in text.splitlines()];verdicts=[v for v in lines if v.startswith('VERDICT: ')]
 if tag=='residual_cell_bernstein_code':check(verdicts==['VERDICT: CONFIRM_BERNSTEIN_PROOF_AND_CODE_ONLY'],'code-only review')
 if tag=='residual_cell_bernstein_complete':
  check(verdicts==['VERDICT: CONFIRM_THREE_CELL_BERNSTEIN_ENCLOSURES_CANONICAL_INPUTS_INHERITED'],'complete output scope');required=['research/residual_cell_bernstein/'+n for n in ['PROOF.md','ADDENDUM.md','REVIEW_RESOLUTIONS.md','FINAL_ADJUDICATION.md','code/audit_output.py','code/check_guards.py','code/review_extract.py','code/finalize.py','evidence/review_extract.json']];check(set(required)<=set(m['files']),'substantive completed output bundle');check(datetime.fromisoformat(e['utc'])<datetime.fromisoformat(m['start_utc']),'output before review')
 reviews[tag]={k:m[k] for k in ['actual_response_model','stop_reason','request_id','input_sha256','start_utc','end_utc']}
 for suffix in ['_metadata.json','_response.json','_response.md','_request.txt']:
  p=R/(tag+suffix);pins[str(p.relative_to(B))]=sha(p)
m=load(R/'residual_cell_bernstein_complete_metadata.json');post=load(D/'evidence/postreview_record.json');check(post['status']=='CONFIRMED_AFTER_INDEPENDENT_READING_OF_ACTUAL_COMPLETE_REVIEW','post-review status');check('research/residual_cell_bernstein/POSTREVIEW_ADJUDICATION.md' not in m['files'] and 'research/residual_cell_bernstein/evidence/postreview_record.json' not in m['files'],'post-review excluded from reviewed bundle');check(post['review_input_sha256']==m['input_sha256'] and post['review_response_sha256']==sha(R/'residual_cell_bernstein_complete_response.json') and post['review_request_id']==m['request_id'],'post-review actual response binding');check(post['adjudication_sha256']==sha(D/'POSTREVIEW_ADJUDICATION.md'),'written post-review assessment');check(datetime.fromisoformat(a['utc'])<datetime.fromisoformat(g['utc'])<datetime.fromisoformat(e['utc'])<datetime.fromisoformat(m['start_utc'])<=datetime.fromisoformat(m['end_utc'])<datetime.fromisoformat(post['utc'])<=datetime.now(timezone.utc),'complete chronology')
for n in ['PROOF.md','ADDENDUM.md','REVIEW_RESOLUTIONS.md','FINAL_ADJUDICATION.md','POSTREVIEW_ADJUDICATION.md']:check((D/n).is_file(),'mandatory document')
for p in D.rglob('*'):
 if p.is_file() and not p.is_symlink() and p.name!='verdict.json' and '__pycache__' not in p.parts:
  n=str(p.relative_to(B));h=sha(p);check(n not in pins or pins[n]==h,'final digest conflict');pins[n]=h
for n,h in pins.items():check(sha(B/n)==h,'final source digest')
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'CONFIRMED_THREE_CELL_BERNSTEIN_ENCLOSURES_CANONICAL_INPUTS_INHERITED','counts':expected,'comparison_counts':a['comparison_counts'],'reviews':reviews,'postreview_record':post,'files':dict(sorted(pins.items())),'scope':'Mandatory PROOF, ADDENDUM, REVIEW_RESOLUTIONS, FINAL_ADJUDICATION and POSTREVIEW_ADJUDICATION. Same3 cells only, all522 modes, i+j<=5. Exact polynomial range refinement; canonical inputs and analytic tails inherited. Counts include recorded prior coefficient checks bound by exact stream commitments. Cap comparison only for the indicated cell/order. No complete cover, global forcing, inverse, nonlinear closure or IPM endpoint.'}
p=D/'evidence/verdict.json'
with p.open('x') as f:json.dump(out,f,indent=2);f.write('\n');f.flush();os.fsync(f.fileno())
print(json.dumps({'utc':out['utc'],'status':out['status'],'pins':len(pins),'sha256':sha(p)}))
