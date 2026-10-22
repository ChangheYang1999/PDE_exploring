"""Authenticate old reviewed files and new finite linkage checks separately."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import json,hashlib
D=Path(__file__).resolve().parents[1];B=D.parents[1];R=B/'notes/reviews'
def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for c in iter(lambda:f.read(1048576),b''):h.update(c)
 return h.hexdigest()
def read(p):return json.loads(p.read_text())
a=read(D/'evidence/finite_audit.json');assert a['status']=='CONFIRMED_FINITE_COMPONENTS_ONLY_FULL_FORCING_OPEN';pins=dict(a['pins'])
for f,h in pins.items():assert sha(B/f)==h,f
s=read(D/'evidence/structure.json');assert s['n']==523 and s['retained_table']==117 and s['full_table']==425 and s['parts']==13 and s['power_entry_identity_checks']==598 and s['prior_source_pins']==42
for f,h in s['pins'].items():assert sha(B/f)==h,f;pins[f]=h
r=read(D/'evidence/r2_condition.json');assert r['n_values']==4096 and r['exact_and_interval_constant_checks']==24576 and len(r['native_boundary_cases'])==7
assert F(r['actual_n_threshold_exact'])==523*F(2)**-1021 and r['generic_counterexample_still_fails']
p=read(D/'evidence/public_binding.json');assert p['parsed_claims']==36 and p['downward_displays']==22 and p['report_sha256']==sha(D/'source/NUM_REPORT_7_10.md') and p['public_checker_sha256']==sha(D/'code/check_public_bounds.py') and p['public_audit_sha256']==sha(D/'evidence/public_bounds_audit.json')
for stem,proof in [('data_structure','DATA_STRUCTURE.md'),('r2_certificate_condition','R2_CERTIFICATE_CONDITION.md')]:assert read(D/'evidence'/(stem+'_proof_first.json'))['sha256']==sha(D/proof)
reviews={};historical_supplied_versions=[]
for tag in ['localized_forcing_analytic','localized_forcing_product_followup','localized_forcing_finite_closure']:
 m=read(R/(tag+'_metadata.json'));raw=read(R/(tag+'_response.json'));req=(R/(tag+'_request.txt')).read_text()
 assert m['actual_response_model']==raw['model']=='claude-opus-5-5' and m['stop_reason']==raw['stop_reason']=='end_turn'
 assert hashlib.sha256(req.encode()).hexdigest()==m['input_sha256']
 pos=req.index('\n\nFILE ')+2
 for i,f in enumerate(m['files']):
  prefix='FILE '+f+'\n';assert req[pos:].startswith(prefix);pos+=len(prefix)
  end=req.index('\n\nFILE '+m['files'][i+1]+'\n',pos) if i+1<len(m['files']) else len(req)
  old=req[pos:end];current=(B/f).read_text();pos=end+2
  if old!=current:
   assert tag=='localized_forcing_product_followup' and f=='research/localized_forcing/GEOMETRY_AUDIT.md'
   assert hashlib.sha256(old.encode()).hexdigest()=='576498166237292fb36ca6494d17c5751fe479b44f561e0aed64344319b9bc55' and current.startswith(old)
   assert sha(B/f)=='9e914441806ebf7bc78a480267621a8ce3ee622f6ba3f945adf14950f45c7d82'
   historical_supplied_versions.append({'tag':tag,'file':f,'change':'Later disk-coverage paragraph appended; current complete file reviewed in finite_closure.'})
 text='\n\n'.join(c['text'] for c in raw['content'] if c['type']=='text')+'\n';assert text==(R/(tag+'_response.md')).read_text()
 if tag.endswith('finite_closure'):assert 'ACCEPT for the restricted finite scope' in text
 for suffix in ['_request.txt','_metadata.json','_response.json','_response.md']:p=R/(tag+suffix);pins[str(p.relative_to(B))]=sha(p)
 reviews[tag]={k:m[k] for k in ['actual_response_model','stop_reason','request_id','input_sha256','end_utc']}
for rel in ['evidence/finite_audit.json','DATA_STRUCTURE.md','R2_CERTIFICATE_CONDITION.md','FOLLOWUP_ADJUDICATION.md','code/check_structure.py','code/check_r2_condition.py','code/check_public_binding.py','code/audit_followup.py','evidence/structure.json','evidence/r2_condition.json','evidence/public_binding.json','evidence/data_structure_proof_first.json','evidence/r2_certificate_condition_proof_first.json','source/NUM_REPORT_7_10.md']:
 p=D/rel;pins[str(p.relative_to(B))]=sha(p)
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_FINITE_FOLLOWUP_REQUIRES_REVIEW_PHYSICAL_FORCING_OPEN','prior_finite_pins':len(a['pins']),'reviews':reviews,'historical_supplied_versions':historical_supplied_versions,'pins':dict(sorted(pins.items())),'new_counts':{'source_assignments':len(s['source_assignments']),'power_table_identity':598,'source_predecessor_pins':42,'r2_constant_checks':24576,'native_boundary_cases':7,'public_parsed_claims':36,'downward_displays':22},'scope':'Finite linkage and universal sufficient r2 condition only; no actual r2 data or full physical forcing accepted.'}
(D/'evidence/followup_audit.json').write_text(json.dumps(out,indent=2)+'\n');print(out['utc'],out['status'],len(pins),'pins')
