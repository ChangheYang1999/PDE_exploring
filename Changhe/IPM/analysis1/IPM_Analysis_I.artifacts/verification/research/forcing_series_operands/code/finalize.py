"""Freeze topic120 after the finite audit and completed actual-model exchanges."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,sys
assert not sys.flags.optimize
D=Path(__file__).resolve().parents[1];B=D.parents[1];R=B/'notes/reviews'
def read(p):return json.loads(p.read_text())
def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for v in iter(lambda:f.read(1048576),b''):h.update(v)
 return h.hexdigest()
a=read(D/'evidence/finite_audit.json');assert a['status']=='PASS_SERIES_FINITE_AUDIT_MODEL_REVIEW_PENDING';pins=dict(a['pins']);assert len(pins)==226
for f,h in pins.items():assert sha(B/f)==h,f
expected={'parameters':'PASS_SOURCE_PARAMETERS_BRANCH_IMPORTS_AND_BODY_EXTRACTION','batch':'PASS_FULL_GEOMETRIC_BATCH_AND_OPERAND_BIT_REPLAY','source_completion':'PASS_COMPLETE_ELEMENTWISE_PATH_EXTRACTION','runtime_bindings':'PASS_FINAL_RUNTIME_SOURCE_BINDINGS'}
for k,s in expected.items():assert read(D/'evidence'/f'{k}.json')['status']==s
assert len(read(D/'evidence/runtime_bindings.json')['functions'])==9
reviews={}
for tag,h in [('forcing_series_operands','73033bd088b25b289b75d63c330336a73e188eed91d03a4385199b3fcba92428'),('forcing_series_followup','71d26bd4c2b990ce68ae486a9b1a47af0c491d03bedf6d105380d4e83e52e5f8'),('forcing_series_closure','feba2c4e44f27618c056ed95bd35bc4381d30351993cd01a0be8de1c8b4d468c')]:
 m=read(R/(tag+'_metadata.json'));raw=read(R/(tag+'_response.json'));request=(R/(tag+'_request.txt')).read_text();text=(R/(tag+'_response.md')).read_text()
 assert m['actual_response_model']==raw['model']=='claude-opus-5-5' and m['stop_reason']==raw['stop_reason']=='end_turn';assert hashlib.sha256(request.encode()).hexdigest()==m['input_sha256']==h
 assert request[request.index('\n\nFILE ')+2:]=='\n\n'.join('FILE '+f+'\n'+(B/f).read_text() for f in m['files'])
 assert text=='\n\n'.join(c['text'] for c in raw['content'] if c['type']=='text')+'\n'
 if tag.endswith('closure'):assert 'Once the binding checks pass' in text and 'No mathematical gap remains' in text
 reviews[tag]={k:m[k] for k in ['actual_response_model','stop_reason','request_id','input_sha256','start_utc','end_utc']}
 for suffix in ['_metadata.json','_request.txt','_response.json','_response.md']:
  p=R/(tag+suffix);pins[str(p.relative_to(B))]=sha(p)
for p in [B/'research/forcing_composed_cutoff/evidence/verdict.json',*sorted(D.glob('*.md')),*sorted((D/'code').glob('*.py')),*sorted((D/'evidence').glob('*')),*sorted((D/'evidence/batch_replay').glob('*'))]:
 if p.is_dir() or p==D/'evidence/verdict.json':continue
 pins[str(p.relative_to(B))]=sha(p)
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'CONFIRMED_CONTEMPORARY_SERIES_OPERANDS_AND_DIRECT_GEOMETRY','blocks':832,'active_series':789,'fallback_ratio_only':43,'coefficient_intervals':13413,'direct_geometry_methods':2,'reviews':reviews,'last_review_conditions':'9runtime function bindings and2module identities independently checked after the third review, exactly as requested. No mathematical gap remained in that review.','files':dict(sorted(pins.items())),'scope':'PROOF, GEOMETRY_ADDENDUM, SOURCE_ADDENDUM and FINAL_ADJUDICATION mandatory. No physical Taylor-model, residual, full forcing norm, historical execution or PDE endpoint accepted.'}
p=D/'evidence/verdict.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'utc':out['utc'],'status':out['status'],'pins':len(pins),'sha256':sha(p)}))
