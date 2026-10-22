"""Authenticate inherited current evidence and the new actual-output review."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,re,os
B=Path(__file__).resolve().parents[3];D=B/'research/canonical_three_cell_linkage';E=D/'evidence';R=B/'notes/reviews'
def need(v,s):
 if not v:raise ValueError(s)
def now():return datetime.now(timezone.utc).isoformat()
def when(s):return datetime.fromisoformat(s)
def sha(p):
 with Path(p).open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def load(p):return json.loads(Path(p).read_text())
def write(p,v):
 with Path(p).open('x') as f:json.dump(v,f,indent=2);f.write('\n');f.flush();os.fsync(f.fileno())
def pin(pins,path,expected=None):
 p=Path(path);p=(p if p.is_absolute() else B/p).resolve();name=str(p.relative_to(B)) if p.is_relative_to(B) else str(p);h=sha(p);need(expected is None or h==expected,'unchanged pin '+name);need(name not in pins or pins[name]==h,'consistent pin');pins[name]=h

def auth(pins,tag,verdict):
 m=load(R/(tag+'_metadata.json'));raw=load(R/(tag+'_response.json'));request=(R/(tag+'_request.txt')).read_text();text='\n\n'.join(x['text'] for x in raw['content'] if x['type']=='text')+'\n'
 need(m['requested_model']=='us.anthropic.claude-opus-5-5' and m['actual_response_model']==raw['model']=='claude-opus-5-5' and m['stop_reason']==raw['stop_reason']=='end_turn','actual complete Opus5.5');need(hashlib.sha256(request.encode()).hexdigest()==m['input_sha256'] and text==(R/(tag+'_response.md')).read_text(),'exact request/response');need(all(s in request for s in ['no JavaScript/TypeScript','no servers/listeners/tunnels','no RLScience cluster','no Lean/Lake builds']),'delegation restrictions')
 need(request[request.index('\n\nFILE ')+2:]=='\n\n'.join('FILE '+f+'\n'+(B/f).read_text() for f in m['files']),'entire current model input bundle');need(re.findall(r'^\W*VERDICT\W*:\W*(\w+)',text,re.M|re.I)==[verdict] and text.strip().splitlines()[-1]=='VERDICT: '+verdict,'unique final scoped verdict')
 if tag=='canonical_three_cell_proof':need(m['request_id']=='a80e84e3-5b0b-4306-8c8c-2ed2a167b331' and m['input_sha256']=='32734a58e1546b696aa1ec330d66402875e6b9d3b89fb3a560aa423e1026e201','fixed actual proof identity')
 if tag=='canonical_three_cell_actual':need(m['files']==load(D/'actual_review_files.json') and request[:request.index('\n\nFILE ')]==(D/'actual_review_preamble.txt').read_text(),'fixed complete actual request')
 for f in m['files']:pin(pins,f)
 for suffix in ['_metadata.json','_request.txt','_response.json','_response.md']:pin(pins,R/(tag+suffix))
 return {k:m[k] for k in ['requested_model','actual_response_model','stop_reason','request_id','input_sha256','start_utc','end_utc']}

def collect():
 pins={};c=load(E/'checks.json');a=load(E/'audit.json');pf=load(E/'proof_first.json')
 need(c['status']=='PASS_COMPLETE_SELECTED_CANONICAL_INPUT_BINDINGS_CONDITIONAL_ON_ARCHIVE_MOMENTS' and a['status']=='PASS_ALL_SELECTED_F_RECORDS_AND_RATIONAL_E','both actual computations');need(c['source_sha256']==sha(D/'code/check.py') and a['source_sha256']==sha(D/'code/audit.py') and a['checks_sha256']==sha(E/'checks.json'),'actual output sources')
 need(c['counts']=={'input_arrays_identical':21,'input_scalar_entries_identical':15720,'candidate_arrays_pinned':45,'coordinate_memberships':6,'length_upper_bounds':3,'E_arb640_containments':3,'E_iv200_containments':3,'exact_F_images':6264,'signed_vs_collected_weights':262},'complete first counts');need(a['saved_records_recomputed']==6264 and a['independent_endpoint_equalities']==31320 and a['binary64_values_decoded']==25116 and a['exact_E_containments']==3,'complete second counts');need([x['cell'] for x in c['cells']]==[x['cell'] for x in a['rational_E_enclosures']]==[0,4102,7808],'all three cells')
 need(c['forcing_stream_sha256']==a['forcing_stream_sha256']==sha(E/'forcing_records.jsonl'),'same complete comparison stream');need(pf['proof_sha256']==sha(D/'PROOF.md') and when(pf['utc'])<when(c['start_utc'])<when(c['utc'])<when(a['start_utc'])<when(a['utc']),'proof and actual computation chronology')
 for obj in [c,a]:
  for n,h in obj['files'].items():pin(pins,n,h)
 review=auth(pins,'canonical_three_cell_proof','CONFIRM_THREE_CELL_COMPOSITION_PROOF')
 for n in ['PROOF.md','AUDIT_METHOD.md','code/check.py','code/audit.py','code/check_v1_rejected.py','code/check_v2_rejected.py','code/closure_common.py','code/extract.py','code/finalize.py','code/launch_actual_review.py','actual_review_files.json','actual_review_question.txt','actual_review_preamble.txt','evidence/checks.json','evidence/audit.json','evidence/proof_first.json','evidence/first_check_failure.json','evidence/second_check_failure.json','evidence/second_check_empty_stream.jsonl']:pin(pins,D/n)
 pin(pins,R/'focused_review.py');return pins,c,a,review
