"""Close only the archive-dependency classification, after actual review and reread."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,re,sys
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/source_archive_dependencies';E=D/'evidence';R=B/'notes/reviews';tag='source_archive_dependencies_followup'
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
manifest=load(E/'dependency_manifest.json');checks=load(E/'checks.json')
assert checks['status']=='PASS_SOURCE_ARCHIVE_DEPENDENCY_BINDING_AND_EXACT_SCALAR_AUDIT'
assert checks['manifest_sha256']==sha(E/'dependency_manifest.json')
for n,h in manifest['files'].items():pin(n,h)
raw=load(R/(tag+'_response.json'));m=load(R/(tag+'_metadata.json'));req=(R/(tag+'_request.txt')).read_text()
text='\n\n'.join(v['text'] for v in raw['content'] if v['type']=='text')+'\n'
assert m['requested_model']=='us.anthropic.claude-opus-5-5' and m['actual_response_model']==raw['model']=='claude-opus-5-5'
assert m['stop_reason']==raw['stop_reason']=='end_turn'
assert text==(R/(tag+'_response.md')).read_text() and hashlib.sha256(req.encode()).hexdigest()==m['input_sha256']
assert all(x in req for x in ['no JavaScript/TypeScript','no servers/listeners/tunnels','no RLScience cluster','no Lean/Lake builds'])
assert m['files']==load(D/'review_files_v2.json')
mandatory=['PROOF.md','TABLE.md','RESULTS.md','REVIEW_RESOLUTION.md','code/check.py','code/check_resolution.py','code/finalize_v2.py','evidence/checks.json','evidence/resolution_checks.json']
assert all(str((D/n).relative_to(B)) in m['files'] for n in mandatory)
initial='source_archive_dependencies'
i=load(R/(initial+'_metadata.json'));rawi=load(R/(initial+'_response.json'));qi=(R/(initial+'_request.txt')).read_text()
ti='\n\n'.join(v['text'] for v in rawi['content'] if v['type']=='text')+'\n'
assert i['request_id']=='82103615-86d5-4942-b33f-54481405b1e9' and i['input_sha256']=='081311d850e28d0a7ff5d8d339d09862ab20a3ebba46e43b2f38877225d2beb0'
assert i['requested_model']=='us.anthropic.claude-opus-5-5' and i['actual_response_model']==rawi['model']=='claude-opus-5-5' and i['stop_reason']==rawi['stop_reason']=='end_turn'
assert ti==(R/(initial+'_response.md')).read_text() and hashlib.sha256(qi.encode()).hexdigest()==i['input_sha256']
assert i['files']==load(D/'review_files.json') and all(str((D/n).relative_to(B)) in i['files'] for n in ['PROOF.md','TABLE.md','code/check.py','evidence/checks.json'])
assert qi[qi.index('\n\nFILE ')+2:]=='\n\n'.join('FILE '+n+'\n'+(B/n).read_text() for n in i['files'])
for n in i['files']:pin(n)
for suf in ['_request.txt','_response.json','_response.md','_metadata.json']:pin(R/(initial+suf))
r=load(E/'resolution_checks.json');assert r['status']=='PASS_INDEPENDENT_INITIAL_BRACKET_UNIQUENESS_AND_D_MARGIN_COMPARISONS'
for n,h in r['files'].items():pin(n,h)
assert when(i['end_utc'])<when(r['start_utc'])<when(r['utc'])<when(m['start_utc'])
assert req[req.index('\n\nFILE ')+2:]=='\n\n'.join('FILE '+n+'\n'+(B/n).read_text() for n in m['files'])
for n in m['files']:pin(n)
assert re.findall(r'^VERDICT: (\w+)\s*$',text,re.M)==['CONFIRM_DEPENDENCY_CLASSIFICATION_ONLY']
assert [v for v in text.splitlines() if v.strip()][-1]=='VERDICT: CONFIRM_DEPENDENCY_CLASSIFICATION_ONLY'
post=load(E/'postreview.json')
assert when(checks['utc'])<when(m['start_utc'])<when(m['end_utc'])<when(post['utc'])
assert post['status']=='CONFIRMED_AFTER_COMPLETE_REVIEW_AND_OWN_ADJUDICATION'
assert post['request_id']==m['request_id'] and post['input_sha256']==m['input_sha256'] and post['response_sha256']==sha(R/(tag+'_response.json'))
assert post['all_substantive_objections_resolved'] is True and post['adjudication_sha256']==sha(D/'POSTREVIEW_ADJUDICATION.md')
for suf in ['_request.txt','_response.json','_response.md','_metadata.json']:pin(R/(tag+suf))
for p in sorted(D.rglob('*')):
 if p.is_file() and p.name!='verdict.json':pin(p)
out={'utc':now(),'status':'CONFIRMED_SOURCE_ARCHIVE_DEPENDENCY_CLASSIFICATION_ONLY','counts':checks['counts'],'actual_review':{k:m[k] for k in ['requested_model','actual_response_model','stop_reason','request_id','input_sha256','start_utc','end_utc']},'postreview':post,'scope':'TABLE.md classifications concern mathematical dependence on topic31 archive. Category b uses only density H and geometry; c uses shared I/J moments. Independent full I/J replay is not asserted complete. Exact inherited point inequalities confirmed using Fraction and fmpq. No newly integrated field, global inverse, existence, exclusion of an X3 neighbourhood, or decisive endpoint.','files':pins}
with (E/'verdict.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
print(json.dumps({'utc':out['utc'],'status':out['status'],'pins':len(pins),'sha256':sha(E/'verdict.json')}))
