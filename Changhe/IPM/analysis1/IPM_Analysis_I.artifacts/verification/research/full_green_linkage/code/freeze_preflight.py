"""Pin the tested queue package and actual-model review bundles."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
B=Path(__file__).resolve().parents[3];D=B/'research/full_green_linkage';E=D/'evidence';R=B/'notes/reviews'
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
assert sha(D/'code/check_boundaries.py')=='64434bad6aa0c30246f3691c4a0e7fbd9319ad5c6816e413b26024be2b9018cb'
assert sha(D/'code/audit_boundaries.py')=='41c39254a7d435a92cb5cf2865924aeb4a3add3d6e9b7737fd68a5e9bdc33b95'
reviews=[];files={}
for tag in ('full_green_linkage_proof','full_green_linkage_precode_closure','full_green_linkage_preflight'):
 meta=json.loads((R/(tag+'_metadata.json')).read_text());raw=json.loads((R/(tag+'_response.json')).read_text());request=(R/(tag+'_request.txt')).read_text();response=(R/(tag+'_response.md')).read_text()
 assert meta['requested_model']=='us.anthropic.claude-opus-5-5' and meta['actual_response_model']==raw['model']=='claude-opus-5-5' and meta['stop_reason']==raw['stop_reason']=='end_turn'
 assert hashlib.sha256(request.encode()).hexdigest()==meta['input_sha256']
 assert response=='\n\n'.join(x['text'] for x in raw['content'] if x['type']=='text')+'\n'
 assert request.endswith('\n\n'.join('FILE '+p+'\n'+(B/p).read_text() for p in meta['files'])),('review bundle no longer current',tag)
 assert all(word in request for word in ('no JavaScript/TypeScript','no servers/listeners/tunnels','no RLScience cluster'))
 reviews.append({'tag':tag,'actual_model':raw['model'],'request_id':meta['request_id'],'end_utc':meta['end_utc'],'input_sha256':meta['input_sha256']})
 for suffix in ('metadata.json','request.txt','response.json','response.md'):p=R/(tag+'_'+suffix);files[str(p.relative_to(B))]=sha(p)
 for p in meta['files']:files[p]=sha(B/p)
assert 'ACCEPT preflight' in (R/'full_green_linkage_preflight_response.md').read_text()
for p in D.glob('*.md'):files[str(p.relative_to(B))]=sha(p)
for p in (D/'code').glob('*.py'):files[str(p.relative_to(B))]=sha(p)
for name in ('proof_first','addendum_first','audit_method_first','review_resolution_first','manufactured','third_manufactured','smoke_v2_summary','smoke_v2_output_audit','smoke_v2_replay','restart_failures','preflight_review_summary'):
 p=E/(name+'.json');files[str(p.relative_to(B))]=sha(p)
for name in ('smoke_v2_spans.jsonl','smoke_v2_sequence.log','smoke_v2_serial.json'):
 p=E/name;files[str(p.relative_to(B))]=sha(p)
for rel in ('research/middle_second/code/run_full.py','research/middle_second/code/audit_full.py'):files[rel]=sha(B/rel)
for key in ('manufactured','third_manufactured','restart_failures'):assert json.loads((E/(key+'.json')).read_text())['status']=='PASS_DIAGNOSTIC_ONLY'
s=json.loads((E/'smoke_v2_summary.json').read_text());a=json.loads((E/'smoke_v2_output_audit.json').read_text());r=json.loads((E/'smoke_v2_replay.json').read_text())
assert s['status']=='OPEN_PARTIAL_DIAGNOSTIC' and a['status']=='OPEN_PARTIAL_AUDIT_PASSED' and r['status']=='PASS_DIAGNOSTIC_WHOLE_SPAN_REPLAY'
assert s['boundaries']==a['boundaries']==11 and s['entries_per_engine']==a['entries_per_engine']==5742 and a['fresh_third_method_entries']==18
for key,digest in s['files'].items():assert sha(B/key)==digest
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'READY_TO_QUEUE_NOT_A_CERTIFICATE','files':files,'actual_model_reviews':reviews,'current_middle_required_cells':7809,'full_boundary_required_spans':1558,'full_boundary_required_boundaries':7810,'full_boundary_entries_per_engine':4076820,'scope':'Only preflight acceptance. All boundary membership remains OPEN until full run, full audit, replay and verifier closure.'}
p=E/'preflight_manifest.json';assert not p.exists();p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'utc':out['utc'],'status':out['status'],'files':len(files),'manifest_sha256':sha(p)},indent=2))
