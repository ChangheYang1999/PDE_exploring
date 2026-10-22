"""Freeze current reviewed preparation. This does not issue a full result."""
from common import *

def review(tag):
 root=B/'notes/reviews';m=load(root/(tag+'_metadata.json'));raw=load(root/(tag+'_response.json'));request=(root/(tag+'_request.txt')).read_text();text=(root/(tag+'_response.md')).read_text()
 assert m['requested_model']=='us.anthropic.claude-opus-5-5' and m['actual_response_model']==raw['model']=='claude-opus-5-5'
 assert m['stop_reason']==raw['stop_reason']=='end_turn' and m['input_sha256']==hashlib.sha256(request.encode()).hexdigest()
 assert text=='\n\n'.join(v['text'] for v in raw['content'] if v['type']=='text')+'\n'
 for phrase in ('no JavaScript/TypeScript','no servers/listeners/tunnels','no RLScience cluster'):assert phrase in request
 suffix='\n\n'+'\n\n'.join('FILE '+f+'\n'+(B/f).read_text() for f in m['files']);assert request.endswith(suffix),('changed review bundle',tag)
 return m,{'tag':tag,'model':raw['model'],'request_id':m['request_id'],'input_sha256':m['input_sha256'],'end_utc':m['end_utc'],'whole_current_bundle_checked':True}

def main():
 assert not (E/'preflight_manifest.json').exists();nodes,keys,tables,dep,selected=load_geometry();files=current_files(dep);reviews=[]
 for tag in ('flow_angular_full_proof','flow_angular_full_preflight'):
  m,r=review(tag);reviews.append(r)
  for rel in m['files']:files[rel]=sha(B/rel)
  for suffix in ('_metadata.json','_request.txt','_response.md','_response.json'):
   rel='notes/reviews/'+tag+suffix;files[rel]=sha(B/rel)
 manufactured=load(E/'manufactured_checks.json');restart=load(E/'restart_checks.json');adj=load(E/'review_adjudication.json')
 assert manufactured['status']=='PASS_FINITE_MANUFACTURED_DIAGNOSTICS' and manufactured['source_sha256']==sha(D/'code/check_manufactured.py')
 assert manufactured['counts']['exact_endpoint_path_agreements']==TOTAL and manufactured['counts']['deflated_wrong_coefficient_rejected']==12 and manufactured['counts']['zero_halfwidth_rejected']==12
 assert restart['status']=='PASS_RESTART_AND_REAL_CONTINUATION_DIAGNOSTICS' and all(restart['checks'].values()) and restart['source_sha256']==sha(D/'code/check_restart.py')
 assert adj['status']=='ACCEPT_PREPARATION_ONLY_AFTER_INDEPENDENT_REVIEW' and adj['response_sha256']==sha(B/'notes/reviews/flow_angular_full_preflight_response.md')
 indices=load(D/'source/plan.json')['smoke_indices']
 for tag in ('smoke','restart_live'):
  s=load(E/(tag+'_summary.json'));a=load(E/(tag+'_output_audit.json'));r=load(E/(tag+'_replay.json'))
  assert s['status']=='COMPUTED_REQUIRES_OUTPUT_AUDIT' and s['cells_complete']==len(indices) and s['footer_read']
  assert a['status']=='PASS_STRUCTURE_REQUIRES_FULL_FRESH_REPLAY' and not a['full_finite'] and a['cells_audited']==len(indices)
  assert r['status']=='PASS_EVERY_BOX_FRESH_REPLAY_REQUIRES_VERIFIER_CLOSURE' and not r['full_finite'] and r['cells_replayed']==len(indices)
  assert s['source_files']==a['source_files']==r['source_files']==current_files(dep)
  assert s['runtime']==a['runtime']==r['runtime']==runtime()
  assert s['rows_sha256']==a['rows_sha256']==r['rows_sha256']==sha(E/(tag+'_rows.jsonl'))
  assert a['summary_sha256']==r['summary_sha256']==sha(E/(tag+'_summary.json')) and r['output_audit_sha256']==sha(E/(tag+'_output_audit.json'))
  assert s['restarts_sha256']==a['restarts_sha256']==r['restarts_sha256']==sha(E/(tag+'_restarts.jsonl'))
  assert r['coefficient_checks']==len(indices)*COEFF and r['geometry_checks']==len(indices)*7 and len(r['observed_widths'])==8
  for suffix in ('_rows.jsonl','_summary.json','_output_audit.json','_replay.json','_restarts.jsonl'):
   p=E/(tag+suffix);files[str(p.relative_to(B))]=sha(p)
 for name in ('PREFLIGHT_NOTES.md','REVIEW_RESOLUTION.md'):
  p=D/name;files[str(p.relative_to(B))]=sha(p)
 for name in ('manufactured_checks.json','restart_preparation.json','restart_checks.json','review_adjudication.json','smoke_serial_events.jsonl'):
  p=E/name;files[str(p.relative_to(B))]=sha(p)
 v={'utc':utc(),'status':'READY_TO_QUEUE_NOT_A_CERTIFICATE','full_run_status':'OPEN_NOT_RUN','files':dict(sorted(files.items())),'runtime':runtime(),'model_reviews':reviews,'scope':'Regenerated128-bit source angular boxes only; ten-cell smoke and failure tests. All51000-cell claim, historical transfer and verifier closure remain OPEN.'}
 write_json(E/'preflight_manifest.json',v);print(canon({'utc':v['utc'],'status':v['status'],'files':len(files),'manifest_sha256':sha(E/'preflight_manifest.json')}),flush=True)
if __name__=='__main__':main()
