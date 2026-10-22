import sys
sys.dont_write_bytecode=True
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,re
B=Path(__file__).resolve().parents[3];D=B/'research/assembled_scaling_image';E=D/'evidence';R=B/'notes/reviews'
def need(v,s):
 if not v:raise ValueError(s)
def now():return datetime.now(timezone.utc).isoformat()
def when(s):return datetime.fromisoformat(s)
def sha(p):
 with Path(p).open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def load(p):return json.loads(Path(p).read_text())
def write(p,x):
 with Path(p).open('x') as f:json.dump(x,f,indent=2);f.write('\n')
def pin(ps,p,h=None):
 p=Path(p);p=(p if p.is_absolute() else B/p).resolve();need(p.is_relative_to(B),'lane-only');n=str(p.relative_to(B));actual=sha(p);need(h is None or h==actual,'fixed input '+n);need(n not in ps or ps[n]==actual,'conflicting pin');ps[n]=actual

def auth(ps,tag,verdict,files=None):
 m=load(R/(tag+'_metadata.json'));raw=load(R/(tag+'_response.json'));req=(R/(tag+'_request.txt')).read_text();text='\n\n'.join(v['text'] for v in raw['content'] if v['type']=='text')+'\n';need(m['requested_model']=='us.anthropic.claude-opus-5-5' and m['actual_response_model']==raw['model']=='claude-opus-5-5' and m['stop_reason']==raw['stop_reason']=='end_turn','actual complete Opus5.5');need(hashlib.sha256(req.encode()).hexdigest()==m['input_sha256'] and text==(R/(tag+'_response.md')).read_text(),'raw review bytes');need(all(v in req for v in ['no JavaScript/TypeScript','no servers/listeners/tunnels','no RLScience cluster','no Lean/Lake builds']),'delegated restrictions');need(req[req.index('\n\nFILE ')+2:]=='\n\n'.join('FILE '+n+'\n'+(B/n).read_text() for n in m['files']),'complete unchanged review bundle');need(re.findall(r'^\W*VERDICT\W*:\W*(\w+)',text,re.M|re.I)==[verdict] and text.strip().splitlines()[-1]=='VERDICT: '+verdict,'unique scoped verdict')
 if files is not None:need(m['files']==files,'fixed actual bundle')
 for n in m['files']:pin(ps,n)
 for suf in ['_metadata.json','_request.txt','_response.json','_response.md']:pin(ps,R/(tag+suf))
 return {k:m[k] for k in ['requested_model','actual_response_model','stop_reason','request_id','input_sha256','start_utc','end_utc']}

def collect():
 ps={};a=load(E/'checks.json');b=load(E/'supplement.json');need(a['status']=='PASS_EXACT_SAVED_ALL_MODE_IMAGE_SUM_AND_DISCRETE_NORMS_REQUIRES_REVIEW' and b['status']=='PASS_RAW_PAYLOAD_EXACT_COEFFICIENT_AND_MANUFACTURED_SUPPLEMENT','actual complete outputs');need(a['checks']=={'manual_ieee_values':881864,'summed_entries_twice':18680,'shape_checks':301,'range_checks':42,'geometry_checks':39228} and a['interval_overlaps']==64 and a['literal_scalar_checks']==18 and a['arb_bits']==320 and a['iv_digits']==100,'all actual main checks');need(b['raw_payload_equalities']==87 and b['two_exact_positive_coefficients']==1866 and len(b['manufactured_forms'])==4 and len(b['parser_cases'])==11 and b['ieee_boundary_values']==8 and b['independent_complete_modes']==260 and b['invalid_range_mutations']==8,'complete supplement');failed=[k for k,v in a['original_diagnostic_tolerances_passed'].items() if v is False];need(failed==[p+'/'+r for p in ['functionals_difference','rel_difference'] for r in ['L2','L2q','H1','H1q']]+['max_abs_img_diff'],'retained nine failed diagnostics');need(when(a['utc'])<when(b['start_utc'])<when(b['utc']),'actual ordered execution')
 for x in [a,b]:
  for n,h in x['files'].items():pin(ps,n,h)
 for n in ['PROOF.md','REVIEW_RESOLUTION.md','SAVED_SUMMARY_DISCREPANCY.md','RESULTS.md','code/check.py','code/supplement.py','code/common.py','code/extract.py','code/finalize.py','code/launch_actual_review.py','actual_review_files.json','actual_review_question.txt','evidence/checks.json','evidence/supplement.json']:pin(ps,D/n)
 proof=auth(ps,'assembled_scaling_image_proof','OBJECTIONS');pin(ps,B/'notes/reviews/focused_review.py')
 return ps,a,b,proof
