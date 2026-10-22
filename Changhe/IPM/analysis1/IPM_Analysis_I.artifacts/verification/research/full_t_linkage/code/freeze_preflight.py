"""Verify review provenance and pin the concrete readiness evidence, not a theorem."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
B=Path(__file__).resolve().parents[3];D=B/'research/full_t_linkage';E=D/'evidence'
def sha(p):
 h=hashlib.sha256()
 with Path(p).open('rb') as f:
  for x in iter(lambda:f.read(1048576),b''):h.update(x)
 return h.hexdigest()
def load(p):return json.loads(Path(p).read_text())
reviews=[];files=set()
for tag in ('full_t_linkage_proof','full_t_linkage_preflight'):
 base=B/'notes/reviews';meta=load(base/(tag+'_metadata.json'));raw=load(base/(tag+'_response.json'));text=(base/(tag+'_response.md')).read_text();request=(base/(tag+'_request.txt')).read_text()
 assert meta['requested_model']=='us.anthropic.claude-opus-5-5' and meta['actual_response_model']==raw['model']=='claude-opus-5-5'
 assert meta['stop_reason']==raw['stop_reason']=='end_turn' and meta['input_sha256']==hashlib.sha256(request.encode()).hexdigest()
 assert text=='\n\n'.join(c['text'] for c in raw['content'] if c['type']=='text')+'\n'
 suffix='\n\n'+'\n\n'.join('FILE '+f+'\n'+(B/f).read_text() for f in meta['files']);assert request.endswith(suffix),('current whole bundle mismatch',tag)
 for phrase in ('no JavaScript/TypeScript','no servers/listeners/tunnels','no RLScience cluster'):assert phrase in request
 reviews.append({'tag':tag,'actual_model':raw['model'],'request_id':meta['request_id'],'end_utc':meta['end_utc'],'input_sha256':meta['input_sha256'],'current_whole_bundle_checked':True})
 files.update(meta['files'])
 for suffix in ('_metadata.json','_response.json','_response.md','_request.txt'):files.add(str((base/(tag+suffix)).relative_to(B)))
required={str((D/f).relative_to(B)) for f in ('PROOF.md','ADDENDUM.md','REVIEW_RESOLUTION.md','PREFLIGHT_NOTES.md','code/check_coefficients.py','code/audit_coefficients.py','code/replay_spans.py','code/run_queue.py','code/wait_priority.sh','code/check_manufactured.py','code/check_newton_manufactured.py','code/check_restart.py')}
required.update(('research/middle_residual/evidence/partition_exact.json','research/middle_residual/evidence/knot_audit.json'))
files.update(required);files.update(('research/full_t_linkage/PREFLIGHT_GATE.md','research/full_t_linkage/code/freeze_preflight.py','research/full_t_linkage/evidence/proof_first.json','research/full_t_linkage/evidence/addendum_first.json','research/full_t_linkage/evidence/smoke_spans.jsonl','research/full_t_linkage/evidence/restart_ok_spans.jsonl','research/full_t_linkage/evidence/restart_ok_summary.json','research/full_t_linkage/evidence/restart_ok_output_audit.json','research/full_t_linkage/evidence/restart_ok_resume_events.jsonl','research/middle_residual/evidence/knot_manifest.json'))
audit=load(E/'smoke_output_audit.json');summary=load(E/'smoke_summary.json');replay=load(E/'smoke_replay.json');restart=load(E/'restart_checks.json')
assert audit['status']=='OPEN_PARTIAL_AUDIT_PASSED' and not audit['full_run'] and audit['cells']==11 and audit['spans']==1
assert summary['status']=='OPEN_PARTIAL_DIAGNOSTIC' and audit['output_sha256']==summary['output_sha256']==replay['input_stream_sha256']==sha(E/'smoke_spans.jsonl')
assert audit['source_sha256']==sha(D/'code/audit_coefficients.py') and summary['source_sha256']==sha(D/'code/check_coefficients.py') and replay['source_sha256']==sha(D/'code/replay_spans.py')
assert replay['mandatory_restart_spans']==audit['replay_required_spans']==[0] and replay['spans_replayed'][0]['span']==0
assert restart['status']=='PASS_DIAGNOSTIC_RESTART_FAULTS' and all(restart['checks'].values()) and restart['source_sha256']==sha(D/'code/check_restart.py')
with (E/'smoke_spans.jsonl').open() as f:header=load_header=json.loads(next(f))
assert len(header['sample_triples'])==255
files.update(summary['files']);files.update(audit['inherited_source_pins'])
for rel,digest in {**summary['files'],**audit['inherited_source_pins']}.items():assert sha(B/rel)==digest,rel
pins={f:sha(B/f) for f in sorted(files)};assert required<=set(pins)
result={'utc':datetime.now(timezone.utc).isoformat(),'status':'READY_TO_QUEUE_NOT_A_CERTIFICATE','files':pins,'required_gate_files':sorted(required),'actual_model_reviews':reviews,'full_run_status':'OPEN_NOT_RUN','scope':'Only full-run readiness; final current-output audit and review still required.'}
p=E/'preflight_manifest.json';assert not p.exists();p.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({'utc':result['utc'],'status':result['status'],'files':len(pins),'sha256':sha(p)}))
