"""Freeze the restricted geometric function result after repaired independent checks."""
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,sys
assert not sys.flags.optimize
D=Path(__file__).resolve().parents[1];B=D.parents[1];R=B/'notes/reviews'
def read(p):return json.loads(p.read_text())
def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for v in iter(lambda:f.read(1048576),b''):h.update(v)
 return h.hexdigest()
a=read(D/'evidence/finite_audit_repaired.json');assert a['status']=='PASS_FINITE_GEOMETRIC_AUDIT_MODEL_REVIEW_PENDING';pins=dict(a['pins']);assert len(pins)==270
for f,h in pins.items():assert sha(B/f)==h,f
z=read(D/'evidence/iv_finite.json');assert z['endpoint_checks']==391040 and z['special_value_rejections']==6 and z['coefficient_projection_tests']==194688
assert read(D/'evidence/conventions.json')['status']=='PASS_COORDINATE_CONVENTION_SOURCE_BINDING' and read(D/'evidence/convention_supplement.json')['status']=='PASS_OPTIONAL_CONVENTION_RECORDS'
reviews={}
for tag,h in [('forcing_geometric_models','89420913b54a7960fff940a85a9f83713162ca0e32aacc6d2039d1175e0a37b8'),('forcing_geometric_followup','55a6ef84722f92c8a76557324f4c32d9eae7ce74eddb7766bdae82156f3b5a1d')]:
 m=read(R/(tag+'_metadata.json'));raw=read(R/(tag+'_response.json'));request=(R/(tag+'_request.txt')).read_text();text=(R/(tag+'_response.md')).read_text();assert m['actual_response_model']==raw['model']=='claude-opus-5-5' and m['stop_reason']==raw['stop_reason']=='end_turn'
 assert hashlib.sha256(request.encode()).hexdigest()==m['input_sha256']==h
 assert request[request.index('\n\nFILE ')+2:]=='\n\n'.join('FILE '+f+'\n'+(B/f).read_text() for f in m['files'])
 assert text=='\n\n'.join(c['text'] for c in raw['content'] if c['type']=='text')+'\n'
 if tag.endswith('followup'):assert '**Verdict: ACCEPTED.**' in text
 reviews[tag]={k:m[k] for k in ['actual_response_model','stop_reason','request_id','input_sha256','start_utc','end_utc']}
 for suffix in ['_metadata.json','_request.txt','_response.json','_response.md']:
  p=R/(tag+suffix);pins[str(p.relative_to(B))]=sha(p)
for p in [*sorted(D.glob('*.md')),*sorted((D/'code').glob('*.py')),*sorted((D/'evidence').glob('*'))]:
 if p.is_dir() or p==D/'evidence/verdict.json':continue
 pins[str(p.relative_to(B))]=sha(p)
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'CONFIRMED_CONTEMPORARY_GEOMETRIC_FUNCTION_INCLUSIONS','blocks':832,'models':1664,'coefficients_per_engine':194688,'iv_finite_endpoint_checks':391040,'iv_special_value_rejections':6,'strict_budget_ratio_ceiling':'11/250','reviews':reviews,'files':dict(sorted(pins.items())),'scope':'PROOF, ADDENDUM, BINDING_ADDENDUM and FINAL_ADJUDICATION mandatory. Only geometric value inclusions for pinned topic120arrays; no true coefficient-box containment or derivative-remainder claim, no historical/newv22 array attestation, no physical forcing norm or PDE endpoint.'}
p=D/'evidence/verdict.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'utc':out['utc'],'status':out['status'],'pins':len(pins),'sha256':sha(p)}))
