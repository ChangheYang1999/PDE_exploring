"""Accept complete scalar assembly only after actual output review and adjudication."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
import json,hashlib,sys,os
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/global_residual_second';R=B/'notes/reviews'
def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def load(p):return json.loads(p.read_text())
def need(v,s):
 if not v:raise ValueError(s)
m=load(D/'data_exact/manifest.json');a=load(D/'evidence/arb_assembly.json');q=load(D/'evidence/output_audit.json');e=load(D/'evidence/review_extract.json');full=load(B/'research/middle_second/evidence/full_q16_verdict.json');pins={}
need(m['status']=='PASS_ACTUAL_ACCEPTED_FULL_MIDDLE_AND_REGIONAL_INPUTS' and a['status']=='COMPUTED_GLOBAL_SECOND_ASSEMBLY_REQUIRES_IV_AND_EXACT_CHECK' and q['status']=='PASS_GLOBAL_SECOND_SCALAR_ASSEMBLY_IV220_AND_EXACT_INTEGER_CHECK' and e['status']=='PASS_COMPLETED_GLOBAL_SECOND_REVIEW_EXTRACT','actual completed statuses')
need(full['status']=='CONFIRMED_COMPLETE_INDEPENDENT_MIDDLE_RESIDUAL_SHARED_CANONICAL_INPUTS' and full['cells']==7809 and full['spans']==1558,'accepted complete second middle')
need(m['cells']==e['cells']=={'inner':54,'middle':7809,'outer':89},'whole cover count');need(m['actual_full_middle_verdict_sha256']==e['actual_full_middle_verdict_sha256']==sha(B/'research/middle_second/evidence/full_q16_verdict.json'),'actual full digest');need(m['old_global_verdict_sha256']==e['old_global_verdict_sha256']=='5e451a9a8e03564044539f9c292a76c55c35b11dead58d918501b496af798d93','old global anchor')
for obj in [m,a,q,e]:
 for n,h in obj['files'].items():need(sha(B/n)==h,'input digest');need(n not in pins or pins[n]==h,'pin conflict');pins[n]=h
for n in ['research/global_residual_assembly/evidence/verdict.json','research/middle_second/evidence/full_q16_verdict.json','research/global_residual_assembly/evidence/primary_assembly_v2.json','notes/middle_full_closure/result.json','notes/middle_full_closure/POSTREVIEW_ADJUDICATION.md']:need(n in pins,'mandatory accepted input')
need(a['squared_norm_exact']==q['squared_norm_exact']==e['squared_norm_exact'],'squared norm identity');S=F(a['squared_norm_exact']);upper=F(q['strict_root_ceiling_exact']);need(S>0 and S<upper*upper and upper==F(q['strict_root_ceiling_decimal'])==F(e['strict_root_ceiling_exact'])==F(e['strict_root_ceiling_decimal']),'strict final norm ceiling');need(e['suprema']==a['suprema'] and set(q['suprema_checked'])==set(a['suprema']),'four supremum bindings')
for key,v in a['suprema'].items():need(F(v['upper_exact'])<F(v['strict_ceiling']['exact'])==F(v['strict_ceiling']['decimal']),'strict final sup ceiling')
reviews={}
for tag,suffixver in [('global_residual_second_proof','CONFIRM_GLOBAL_SECOND_ASSEMBLY_PROOF_ONLY'),('global_residual_second_code',None),('global_residual_second_code_repaired','CONFIRM_GLOBAL_SECOND_ASSEMBLY_CODE_ONLY'),('global_residual_second_complete','CONFIRM_WHOLE_PLANE_RESIDUAL_WITH_COMPLETE_SECOND_MIDDLE_SHARED_CANONICAL_INPUTS')]:
 rm=load(R/(tag+'_metadata.json'));raw=load(R/(tag+'_response.json'));req=(R/(tag+'_request.txt')).read_text();txt='\n\n'.join(c['text'] for c in raw['content'] if c['type']=='text')+'\n';need(rm['requested_model']=='us.anthropic.claude-opus-5-5' and rm['actual_response_model']==raw['model']=='claude-opus-5-5' and rm['stop_reason']==raw['stop_reason']=='end_turn','actual completed model');need(hashlib.sha256(req.encode()).hexdigest()==rm['input_sha256'] and txt==(R/(tag+'_response.md')).read_text(),'actual review bytes');need(req[req.index('\n\nFILE ')+2:]=='\n\n'.join('FILE '+n+'\n'+(B/n).read_text() for n in rm['files']),'current review bundle');lines=[v.strip().strip('*').strip() for v in txt.splitlines()];need(suffixver is None or [v for v in lines if v.startswith('VERDICT: ')]==['VERDICT: '+suffixver],'unique scoped review')
 if tag.endswith('complete'):
  required=['PROOF.md','ADDENDUM.md','FINAL_ADJUDICATION.md','CODE_REVIEW_RESOLUTIONS.md','CODE_INPUT_PATH_REPAIR.md','code/prepare_v3.py','code/compute_arb.py','code/check_iv_v2.py','code/review_extract.py','code/finalize_v3.py','evidence/review_extract.json'];need({'research/global_residual_second/'+n for n in required}<=set(rm['files']),'complete review bundle');need('research/global_residual_second/POSTREVIEW_ADJUDICATION.md' not in rm['files'] and 'research/global_residual_second/evidence/postreview_record.json' not in rm['files'],'postreview later files')
 reviews[tag]={k:rm[k] for k in ['actual_response_model','stop_reason','request_id','input_sha256','start_utc','end_utc']}
 for su in ['_metadata.json','_response.json','_response.md','_request.txt']:
  pp=R/(tag+su);pins[str(pp.relative_to(B))]=sha(pp)
rm=load(R/'global_residual_second_complete_metadata.json');post=load(D/'evidence/postreview_record.json');need(post['status']=='CONFIRMED_AFTER_INDEPENDENT_READING_OF_ACTUAL_COMPLETE_REVIEW','postreview status');need(post['review_input_sha256']==rm['input_sha256'] and post['review_request_id']==rm['request_id'] and post['review_response_sha256']==sha(R/'global_residual_second_complete_response.json') and post['adjudication_sha256']==sha(D/'POSTREVIEW_ADJUDICATION.md'),'actual postreview binding');times=[full['utc'],m['utc'],a['utc'],q['utc'],e['utc'],rm['start_utc'],rm['end_utc'],post['utc']];need(all(datetime.fromisoformat(x)<datetime.fromisoformat(y) for x,y in zip(times,times[1:])) and datetime.fromisoformat(post['utc'])<=datetime.now(timezone.utc),'full output chronology')
for n in ['PROOF.md','ADDENDUM.md','CODE_REVIEW_RESOLUTIONS.md','FINAL_ADJUDICATION.md','POSTREVIEW_ADJUDICATION.md']:need((D/n).is_file(),'mandatory document')
for p in D.rglob('*'):
 if p.is_file() and not p.is_symlink() and p.name!='verdict.json' and '__pycache__' not in p.parts:
  n=str(p.relative_to(B));h=sha(p);need(n not in pins or pins[n]==h,'final conflict');pins[n]=h
for n,h in pins.items():need(sha(B/n)==h,'final digest')
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'CONFIRMED_WHOLE_PLANE_RESIDUAL_WITH_COMPLETE_SECOND_MIDDLE_SHARED_CANONICAL_INPUTS','cells':m['cells'],'squared_norm_exact':str(S),'N2_strict_ceiling_exact':str(upper),'N2_strict_ceiling_decimal':q['strict_root_ceiling_decimal'],'suprema':a['suprema'],'actual_full_middle_verdict_sha256':m['actual_full_middle_verdict_sha256'],'reviews':reviews,'postreview_record':post,'files':dict(sorted(pins.items())),'scope':'Mandatory PROOF ADDENDUM FINAL_ADJUDICATION POSTREVIEW_ADJUDICATION. Full-plane zeroth residual of exact normalized modal trial. Analytic inner/outer certificates inherited; middle has actual complete independent density-moment method and scalar replay. Shared original-knot canonical archive remains a dependency. No canonical-linkage closure, original X3 distance, global derivatives/forcing, inverse, nonlinear closure or IPM endpoint.'}
p=D/'evidence/verdict.json'
with p.open('x') as f:json.dump(out,f,indent=2);f.write('\n');f.flush();os.fsync(f.fileno())
print(json.dumps({'utc':out['utc'],'status':out['status'],'N2_ceiling':q['strict_root_ceiling_decimal'],'pins':len(pins),'sha256':sha(p)}))
