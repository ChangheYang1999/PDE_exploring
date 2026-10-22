"""Freeze reviewed programs and smoke evidence. This never issues a final verdict."""
from common import *

def review(tag,current=True):
 root=BASE/'notes/reviews';m=load(root/(tag+'_metadata.json'));raw=load(root/(tag+'_response.json'));request=(root/(tag+'_request.txt')).read_text();text=(root/(tag+'_response.md')).read_text()
 assert m['requested_model']=='us.anthropic.claude-opus-5-5' and m['actual_response_model']==raw['model']=='claude-opus-5-5'
 assert m['stop_reason']==raw['stop_reason']=='end_turn' and m['input_sha256']==hashlib.sha256(request.encode()).hexdigest()
 assert text=='\n\n'.join(v['text'] for v in raw['content'] if v['type']=='text')+'\n'
 for phrase in ('no JavaScript/TypeScript','no servers/listeners/tunnels','no RLScience cluster'):assert phrase in request
 if current:
  suffix='\n\n'+'\n\n'.join('FILE '+f+'\n'+(BASE/f).read_text() for f in m['files']);assert request.endswith(suffix),('current whole bundle mismatch',tag)
 return m,{'tag':tag,'model':raw['model'],'request_id':m['request_id'],'input_sha256':m['input_sha256'],'end_utc':m['end_utc'],'whole_current_bundle_checked':current}

def main():
 assert not (OUT/'preflight_manifest.json').exists();pins=current_pins();files=set();reviews=[]
 for tag in ('radial_tm_full_proof','radial_tm_full_preflight'):
  m,v=review(tag);reviews.append(v);files.update(m['files'])
  for suffix in ('_metadata.json','_request.txt','_response.md','_response.json'):files.add('notes/reviews/'+tag+suffix)
 # Historical engine review is retained and authenticated separately. Its common.py snapshot was repaired before smoke_v2.
 m,v=review('radial_tm_full_engines',False);reviews.append(v)
 for suffix in ('_metadata.json','_request.txt','_response.md','_response.json'):files.add('notes/reviews/radial_tm_full_engines'+suffix)
 engine_audit=load(OUT/'engine_review_audit.json');assert engine_audit['input_sha256']==m['input_sha256']
 for item in engine_audit['files']:
  assert sha(BASE/item['reviewed_snapshot'])==item['sha256'];files.add(item['reviewed_snapshot'])
 manufactured=load(OUT/'manufactured_checks.json');restart=load(OUT/'restart_checks.json')
 assert manufactured['status']=='PASS_FINITE_MANUFACTURED_DIAGNOSTICS' and manufactured['source_sha256']==sha(DIR/'code/check_manufactured.py')
 assert manufactured['counts']['deflated_coefficient_rejected']==2 and manufactured['counts']['zero_remainder_budget_rejected']==4 and manufactured['counts']['subnormal_budget_direction']==2
 assert restart['status']=='PASS_RESTART_AND_REAL_CONTINUATION_DIAGNOSTICS' and all(restart['checks'].values()) and restart['source_sha256']==sha(DIR/'code/check_restart.py')
 for tag,needed in (('smoke_v2',[0,7808]),('restart_live',[0,4102,7808])):
  s=load(OUT/(tag+'_summary.json'));a=load(OUT/(tag+'_output_audit.json'));r=load(OUT/(tag+'_replay.json'))
  assert s['status']=='COMPUTED_REQUIRES_SEPARATE_OUTPUT_AUDIT' and s['cells']==[0,4102,7808] and s['modes']==list(range(1,262))
  assert s['input_pins']==pins==a['source_pins']==r['source_pins']
  assert s['counts']=={'arb512_coefficients':20358,'arb512_remainders':1566,'iv180_rational_exp_coefficients':20358,'iv180_rational_exp_remainders':1566,'forcing':6264}
  assert a['status']=='PASS_OUTPUT_AND_FRESH_PARTICULAR_AUDIT' and a['cells_audited']==3 and not a['full_middle']
  assert s['rows_sha256']==a['rows_sha256']==sha(OUT/(tag+'_rows.jsonl')) and a['input_summary_sha256']==sha(OUT/(tag+'_summary.json'))
  assert r['status']=='PASS_COMPLETE_CELL_REPLAY' and r['output_audit_sha256']==sha(OUT/(tag+'_output_audit.json'))
  assert r['required_cells']==r['replayed_cells']==a['replay_required_cells']==needed
  assert a['fresh_records_sha256']==sha(OUT/(tag+'_fresh_audit.jsonl'))
  for suffix in ('_summary.json','_output_audit.json','_replay.json','_rows.jsonl','_fresh_audit.jsonl','_restarts.jsonl'):
   p=OUT/(tag+suffix)
   if p.exists():files.add(str(p.relative_to(BASE)))
 for p in (DIR/'code').glob('*'):
  if p.is_file():files.add(str(p.relative_to(BASE)))
 for name in ('PROOF.md','ADDENDUM.md','OPTIMIZATION.md','REVIEW_RESOLUTION.md','PREFLIGHT_NOTES.md','PREFLIGHT_GATE.md'):files.add(str((DIR/name).relative_to(BASE)))
 for name in ('proof_first.json','proof_review_audit.json','engine_review_audit.json','manufactured_checks.json','restart_checks.json'):files.add(str((OUT/name).relative_to(BASE)))
 for v in pins.values():
  p=Path(v['path'])
  if p.is_relative_to(BASE):files.add(str(p.relative_to(BASE)))
 result={'utc':utc(),'status':'READY_TO_QUEUE_NOT_A_CERTIFICATE','input_pins':pins,'files':{p:sha(BASE/p) for p in sorted(files)},'model_reviews':reviews,'full_run_status':'OPEN_NOT_RUN','scope':'Reviewed readiness and complete three-cell diagnostics. Full7809-cell computation, output audit, independent closure and canonical-data linkage remain open.'}
 (OUT/'preflight_manifest.json').write_text(canonical(result)+'\n');print(canonical({'utc':result['utc'],'status':result['status'],'files':len(files),'manifest_sha256':sha(OUT/'preflight_manifest.json')}))
if __name__=='__main__':main()
