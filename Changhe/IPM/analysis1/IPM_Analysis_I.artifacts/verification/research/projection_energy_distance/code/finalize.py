"""Close only the projection scalar audit, after actual review and reread."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,re,sys
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/projection_energy_distance';E=D/'evidence';R=B/'notes/reviews';tag='projection_energy_distance'
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
assert checks['status']=='PASS_SAVED_PROJECTION_SCALARS_WITH_REFUTED_OLD_NORM_INTERPRETATION'
for n,h in checks['files'].items():pin(n,h)
for n,item in load(E/'source_snapshot.json')['files'].items():pin(n,item['sha256'])
raw=load(R/(tag+'_response.json'));m=load(R/(tag+'_metadata.json'));req=(R/(tag+'_request.txt')).read_text()
text='\n\n'.join(v['text'] for v in raw['content'] if v['type']=='text')+'\n'
assert m['requested_model']=='us.anthropic.claude-opus-5-5' and m['actual_response_model']==raw['model']=='claude-opus-5-5'
assert m['stop_reason']==raw['stop_reason']=='end_turn'
assert text==(R/(tag+'_response.md')).read_text() and hashlib.sha256(req.encode()).hexdigest()==m['input_sha256']
assert all(x in req for x in ['no JavaScript/TypeScript','no servers/listeners/tunnels','no RLScience cluster','no Lean/Lake builds'])
assert m['files']==load(D/'review_files.json')
mandatory=['PROOF.md','ADDENDUM.md','RESULTS.md','code/check.py','code/finalize.py','evidence/checks.json','evidence/source_snapshot.json','source/c2_Kproj.py']
assert all(str((D/n).relative_to(B)) in m['files'] for n in mandatory)
assert req[req.index('\n\nFILE ')+2:]=='\n\n'.join('FILE '+n+'\n'+(B/n).read_text() for n in m['files'])
for n in m['files']:pin(n)
assert re.findall(r'^VERDICT: (\w+)\s*$',text,re.M)==['CONFIRM_PROJECTION_SCALAR_AUDIT_ONLY']
assert [v for v in text.splitlines() if v.strip()][-1]=='VERDICT: CONFIRM_PROJECTION_SCALAR_AUDIT_ONLY'
post=load(E/'postreview.json')
assert when(checks['utc'])<when(m['start_utc'])<when(m['end_utc'])<when(post['utc'])
assert post['status']=='CONFIRMED_AFTER_COMPLETE_REVIEW_AND_OWN_ADJUDICATION'
assert post['request_id']==m['request_id'] and post['input_sha256']==m['input_sha256'] and post['response_sha256']==sha(R/(tag+'_response.json'))
assert post['all_substantive_objections_resolved'] is True and post['adjudication_sha256']==sha(D/'POSTREVIEW_ADJUDICATION.md')
for suf in ['_request.txt','_response.json','_response.md','_metadata.json']:pin(R/(tag+suf))
for p in sorted(D.rglob('*')):
 if p.is_file() and p.name!='verdict.json':pin(p)
out={'utc':now(),'status':'CONFIRMED_PROJECTION_SCALAR_ARITHMETIC_ONLY','counts':checks['counts'],'actual_review':{k:m[k] for k in ['requested_model','actual_response_model','stop_reason','request_id','input_sha256','start_utc','end_utc']},'postreview':post,'scope':'Exact Hilbert projection identity and frozen floating scalar arithmetic only. Legacy full-norm ratios and 99.5percent energy to 0.5percent distance interpretation refuted. Current scalar schema objection withdrawn. Physical projections, Gram, images, tails, graph norm, inverse and IPM endpoints OPEN.','files':pins}
with (E/'verdict.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
print(json.dumps({'utc':out['utc'],'status':out['status'],'pins':len(pins),'sha256':sha(E/'verdict.json')}))
