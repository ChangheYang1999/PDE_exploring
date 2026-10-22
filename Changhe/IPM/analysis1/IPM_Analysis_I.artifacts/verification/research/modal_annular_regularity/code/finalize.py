"""Close only the annular regularity audit, after actual review and reread."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,re,sys
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/modal_annular_regularity';E=D/'evidence';R=B/'notes/reviews';tag='modal_annular_regularity'
now=lambda:datetime.now(timezone.utc).isoformat()
def sha(p):
 with Path(p).open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def load(p):return json.loads(Path(p).read_text())
def when(x):return datetime.fromisoformat(x)
pins={}
def pin(p,h=None):
 p=Path(p);p=p if p.is_absolute() else B/p
 n=str(p.relative_to(B)) if p.is_relative_to(B) else str(p);a=sha(p)
 assert h is None or a==h,n
 assert n not in pins or pins[n]==a,n
 pins[n]=a
checks=load(E/'checks.json')
assert checks['status']=='PASS_EXACT_MODAL_ENDPOINTS_AND_ANNULAR_REGULARITY_PREMISES'
for n,h in checks['files'].items():pin(n,h)
green=load(E/'green_factor_checks.json')
assert green['status']=='PASS_CORRECTED_CANONICAL_GREEN_PREFACTOR' and green['modes']==261 and green['coefficient_comparisons']==1566 and green['wrong_prefactor_rejected_at_n']==[2,135]
for n,h in green['files'].items():pin(n,h)
raw=load(R/(tag+'_response.json'));m=load(R/(tag+'_metadata.json'));req=(R/(tag+'_request.txt')).read_text()
text='\n\n'.join(v['text'] for v in raw['content'] if v['type']=='text')+'\n'
assert m['requested_model']=='us.anthropic.claude-opus-5-5' and m['actual_response_model']==raw['model']=='claude-opus-5-5'
assert m['stop_reason']==raw['stop_reason']=='end_turn'
assert text==(R/(tag+'_response.md')).read_text() and hashlib.sha256(req.encode()).hexdigest()==m['input_sha256']
assert all(x in req for x in ['no JavaScript/TypeScript','no servers/listeners/tunnels','no RLScience cluster','no Lean/Lake builds'])
assert m['files']==load(D/'review_files.json')
mandatory=['PROOF.md','SPLINE_DERIVATIVE_DETAILS.md','RESULTS.md','code/check.py','code/finalize.py','evidence/checks.json','evidence/proof_first.json','GREEN_FACTOR_CORRECTION.md','code/check_green_factor.py','evidence/green_factor_checks.json']
assert all(str((D/n).relative_to(B)) in m['files'] for n in mandatory)
assert req[req.index('\n\nFILE ')+2:]=='\n\n'.join('FILE '+n+'\n'+(B/n).read_text() for n in m['files'])
for n in m['files']:pin(n)
assert re.findall(r'^VERDICT: (\w+)\s*$',text,re.M)==['CONFIRM_EXACT_MODAL_ANNULAR_REGULARITY']
assert [v for v in text.splitlines() if v.strip()][-1]=='VERDICT: CONFIRM_EXACT_MODAL_ANNULAR_REGULARITY'
post=load(E/'postreview.json')
assert when(checks['utc'])<when(m['start_utc'])<when(m['end_utc'])<when(post['utc'])
assert post['status']=='CONFIRMED_AFTER_COMPLETE_REVIEW_AND_OWN_ADJUDICATION'
assert post['request_id']==m['request_id'] and post['input_sha256']==m['input_sha256'] and post['response_sha256']==sha(R/(tag+'_response.json'))
assert post['all_substantive_objections_resolved'] is True and post['adjudication_sha256']==sha(D/'POSTREVIEW_ADJUDICATION.md')
for suf in ['_request.txt','_response.json','_response.md','_metadata.json']:pin(R/(tag+suf))
for p in sorted(D.rglob('*')):
 if p.is_file() and p.name!='verdict.json':pin(p)
out={'utc':now(),'status':'CONFIRMED_EXACT_MODAL_ANNULAR_REGULARITY','counts':checks['counts'],'green_factor_check':{k:green[k] for k in ['status','modes','coefficient_comparisons','wrong_prefactor_rejected_at_n']},'actual_review':{k:m[k] for k in ['requested_model','actual_response_model','stop_reason','request_id','input_sha256','start_utc','end_utc']},'postreview':post,'scope':'Exact normalized modal trial is C6 away from0, canonical stream C7, velocity C6, residual C5. Finite-mode regularity premise of163 discharged only. Physical W, numerical moments, tails, inverse and IPM endpoints OPEN.','files':pins}
with (E/'verdict.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
print(json.dumps({'utc':out['utc'],'status':out['status'],'pins':len(pins),'sha256':sha(E/'verdict.json')}))
