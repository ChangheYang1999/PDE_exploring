"""Final exact rank/source verdict, after actual source-repair review and assessment."""
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,sys,os
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/external_constraint_rank';R=B/'notes/reviews'
def sha(p):
 with p.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def load(p):return json.loads(p.read_text())
def need(v,s):
 if not v:raise ValueError(s)
a=load(D/'evidence/output_audit.json');g=load(D/'evidence/source_audit_v2.json');pins={}
need(a['status']=='PASS_EXACT_EXTERNAL_RANK_SOURCE_ELIMINATION_AND_DETERMINANT_CHECK' and g['status']=='PASS_STATIC_EXTERNAL_CONSTRAINT_AND_COORDINATE_SOURCE_BINDING','audit statuses')
need(a['counts']=={'source_columns':160,'matrix_entries':640,'permutation_terms':960,'elimination_pivots':160},'arithmetic counts')
need([(r['M'],r['Fminus_columns_including_KP_TAU'],r['external_rank'],r['external_kernel_coefficient_dimension']) for r in a['families']]==[(16,1955,64,1891),(24,5259,96,5163)],'families')
need((g['assignment_checks'],g['complete_constraint_functions'],g['complete_jet_functions'],g['Fminus_coordinate_selections'],g['raw_export_field_checks'])==(18,2,2,2,4),'static source counts')
for o in [a,g]:
 for n,h in o['files'].items():need(sha(B/n)==h,'source digest');need(n not in pins or pins[n]==h,'pin conflict');pins[n]=h
reviews={}
for tag in ['external_constraint_rank_first','external_constraint_rank_repaired']:
 m=load(R/(tag+'_metadata.json'));raw=load(R/(tag+'_response.json'));req=(R/(tag+'_request.txt')).read_text();txt='\n\n'.join(c['text'] for c in raw['content'] if c['type']=='text')+'\n'
 need(m['requested_model']=='us.anthropic.claude-opus-5-5' and m['actual_response_model']==raw['model']=='claude-opus-5-5' and m['stop_reason']==raw['stop_reason']=='end_turn','actual completed model');need(hashlib.sha256(req.encode()).hexdigest()==m['input_sha256'],'review digest');need(txt==(R/(tag+'_response.md')).read_text(),'raw response');need(req[req.index('\n\nFILE ')+2:]=='\n\n'.join('FILE '+n+'\n'+(B/n).read_text() for n in m['files']),'unchanged review bundle')
 lines=[x.strip().strip('*').strip() for x in txt.splitlines()];ver=[x for x in lines if x.startswith('VERDICT: ')]
 if tag.endswith('repaired'):
  need(ver==['VERDICT: CONFIRM_EXACT_EXTERNAL_RANK_WITH_EXPLICIT_RUNTIME_HYPOTHESES'],'review verdict');required=['PROOF.md','SOURCE_BINDING_V2.md','FINAL_ADJUDICATION_V2.md','code/compute.py','code/check.py','code/check_source.py','code/finalize.py','evidence/output_audit.json','evidence/source_audit_v2.json'];need({'research/external_constraint_rank/'+n for n in required}<=set(m['files']),'complete evidence review');need('research/external_constraint_rank/POSTREVIEW_ADJUDICATION.md' not in m['files'] and 'research/external_constraint_rank/evidence/postreview_record.json' not in m['files'],'postreview files excluded')
 reviews[tag]={k:m[k] for k in ['actual_response_model','stop_reason','request_id','input_sha256','start_utc','end_utc']}
 for suffix in ['_metadata.json','_response.json','_response.md','_request.txt']:
  p=R/(tag+suffix);pins[str(p.relative_to(B))]=sha(p)
m=load(R/'external_constraint_rank_repaired_metadata.json');post=load(D/'evidence/postreview_record.json');need(post['status']=='CONFIRMED_AFTER_INDEPENDENT_READING_OF_ACTUAL_REPAIRED_REVIEW','post status');need(post['review_input_sha256']==m['input_sha256'] and post['review_request_id']==m['request_id'] and post['review_response_sha256']==sha(R/'external_constraint_rank_repaired_response.json') and post['adjudication_sha256']==sha(D/'POSTREVIEW_ADJUDICATION.md'),'post response binding');need(datetime.fromisoformat(a['utc'])<datetime.fromisoformat(g['utc'])<datetime.fromisoformat(m['start_utc'])<=datetime.fromisoformat(m['end_utc'])<datetime.fromisoformat(post['utc'])<=datetime.now(timezone.utc),'chronology')
for n in ['PROOF.md','SOURCE_BINDING.md','SOURCE_BINDING_V2.md','FINAL_ADJUDICATION.md','FINAL_ADJUDICATION_V2.md','POSTREVIEW_ADJUDICATION.md']:need((D/n).is_file(),'mandatory document')
for p in D.rglob('*'):
 if p.is_file() and not p.is_symlink() and p.name!='verdict.json' and '__pycache__' not in p.parts:
  n=str(p.relative_to(B));h=sha(p);need(n not in pins or pins[n]==h,'final pin conflict');pins[n]=h
for n,h in pins.items():need(sha(B/n)==h,'final digest')
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'CONFIRMED_EXACT_EXTERNAL_RANK_WITH_EXPLICIT_RUNTIME_HYPOTHESES','families':a['families'],'counts':a['counts'],'reviews':reviews,'postreview_record':post,'files':dict(sorted(pins.items())),'scope':'Exact frozen unscaled source-defined external matrices only; static source binding has explicit matching-runtime-array and finite-positive-scaling hypotheses. Mandatory PROOF, SOURCE_BINDING_V2 and FINAL_ADJUDICATION_V2 and POSTREVIEW_ADJUDICATION. Not actual SVD rank, retained-vector membership, KP/TAU physical trace validation, internal matching, Sobolev membership, inverse or IPM endpoint.'}
p=D/'evidence/verdict.json'
with p.open('x') as f:json.dump(out,f,indent=2);f.write('\n');f.flush();os.fsync(f.fileno())
print(json.dumps({'utc':out['utc'],'status':out['status'],'pins':len(pins),'sha256':sha(p)}))
