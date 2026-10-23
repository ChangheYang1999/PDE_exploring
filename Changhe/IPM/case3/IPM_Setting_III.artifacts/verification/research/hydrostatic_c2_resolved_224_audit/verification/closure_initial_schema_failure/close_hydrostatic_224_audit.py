"""Final immutable bindings for independent finite auxiliary N224 audit289."""
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib
R=Path('research/hydrostatic_c2_resolved_224_audit');V=R/'verification';checks=[];bindings={};sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def ck(n,b,e=None):
 checks.append(dict(name=n,passed=bool(b),evidence=e))
 if not b:raise AssertionError((n,e))
def bind(p,h=None):
 p=Path(p);v=sha(p);ck('binding '+str(p),h is None or v==h);bindings[str(p)]=v
records={}
for name,count,status in [('PIPELINE.json',76,'DONE'),('SUMMARY.json',150,'PASS'),('SOURCE_GATE.json',16,'PASS'),('COMPLETED_IDENTITY.json',25,'PASS'),('RECOVERY_MANUFACTURES.json',42,'PASS'),('RESULTS_SUPPLEMENT.json',161,'PASS_FINITE_RESULTS_SUPPLEMENT'),('FINAL_EXTRA.json',108,'PASS_FINAL_EXTRA_FINITE_SCOPE')]:
 p=V/name;bind(p);d=json.loads(p.read_text());records[name]=d;ck(name+' completed',d['status']==status and len(d['checks'])==count and d.get('count',count)==count and all(x['passed']for x in d['checks']))
 for key in ['bindings','code_and_proof_sha256','modules']:
  for p,h in d.get(key,{}).items():bind(p,h)
 for row in d['checks']:
  e=row.get('evidence')
  if isinstance(e,dict)and set(['path','sha256'])<=set(e):bind(e['path'],e['sha256'])
pipe=records['PIPELINE.json'];s=records['SUMMARY.json'];source=records['SOURCE_GATE.json'];prep=json.loads((V/'PREPARATION_FINAL.json').read_text());bind(V/'PREPARATION_FINAL.json');ck('42manufactures recorded inprep',prep['synthetic_protocol_count']==42)
for p,h in prep['bindings'].items():bind(p,h)
for row in prep['checks']:
 ck('preparation AST '+row['name'],row['passed']);p=row['name'].removeprefix('AST ');bind(p,row['sha256'])
for p,h in records['RECOVERY_MANUFACTURES.json']['source_sha256'].items():bind(p,h)
bind(V/'INPUTS.json',pipe['input_sha256']);bind(V/'SOURCE_GATE.json',pipe['source_gate_sha256']);bind(source['frozen'],source['source_sha256']);bind(V/'producer_log_at_freeze.txt',source['log_sha256']);bind(V/'producer_launcher_at_freeze.txt',source['launcher_sha256'])
bind(Path('independent_code/summarize_hydrostatic_c2_resolved_224.py'),s['driver_sha256']);bind(R/'SUMMARY_PROOF.md',s['proof_sha256']);bind(V/'PIPELINE.json',s['pipeline_sha256']);ck('one completed224state',len(pipe['states'])==len(s['states'])==1 and pipe['states'][0]['status']=='DONE'and s['states'][0]['N']==224)
bind(V/'hsG_c2.0_N224_log.json',pipe['states'][0]['result_sha256']);raw=json.loads((V/'hsG_c2.0_N224_log.json').read_text());bind(V/'hsG_c2.0_N224_log.polynomials.json',raw['polynomial_sha256']);ck('inputdefiningidentity',records['COMPLETED_IDENTITY.json']['raw_source']['sha256']==raw['source_sha256']==source['source_sha256']);ck('exact negatives demonstrated',records['RESULTS_SUPPLEMENT.json']['exact']['delta']['float']<0 and records['RESULTS_SUPPLEMENT.json']['exact']['r2']['float']<0);ck('774primarysample14witness',all(len(x['points'])==774 for x in raw['levels'])and len(raw['witnesses']['points'])==14)
# Historical completed summary stage remains valid; do not bind the still-live computation log.
h=json.loads((V/'HANDOFF.json').read_text());bind(V/'HANDOFF.json');ck('only completed summary claimed',h['stages'][0]['status']=='PASS'and h['stages'][0]['returncode']==0);bind(V/'SUMMARY.json',h['stages'][0]['output_sha256']);t=json.loads((V/'summary_timeout_60.json').read_text());ck('preserved failedtimeout',t['returncode']==124)
reviews=[]
for folder in ['opus_design','opus_followup','opus_third','opus_results_shift7_archive','opus_results','opus_results_followup','opus_results_closure','opus_final']:
 d=V/folder;m=json.loads((d/'metadata.json').read_text());resp=json.loads((d/'response.json').read_text());ck('actualmodel '+folder,m['requested_model']=='us.anthropic.claude-opus-5-5'and m['returned_model']==resp['model']=='claude-opus-5-5');ck('requesthash '+folder,sha(d/'request.txt')==m['request_sha256']);text='\n'.join(x['text']for x in resp['content']if x['type']=='text').strip();ck('responsetext '+folder,text==(d/'answer.md').read_text().strip()and bool(text));ck('metadata stopreason '+folder,m['stop_reason']==resp['stop_reason'])
 if folder=='opus_final':ck('final followup completed',m['stop_reason']=='end_turn'and m['answer_nonempty'])
 if folder=='opus_results_followup':ck('truncated review retained aspartial',m['stop_reason']=='max_tokens')
 for name in ['metadata.json','response.json','request.txt','answer.md']:bind(d/name)
 reviews.append(dict(folder=folder,completed=m['stop_reason']=='end_turn',**m))
for p in [Path(__file__),R/'CLOSURE_PROOF.md',R/'FINAL_RESULTS_REVIEW_RESOLUTION_PROOF.md',R/'RESULTS.md',R/'RESULTS_SUPPLEMENT.md',R/'FINAL_MODEL_RESOLUTION.md',V/'SUMMARY.md',V/'summary_timeout_60.json',V/'summary_timeout_60.log',V/'RESULTS_before_results_review.md',V/'results_supplement_initial_failure/FAILURE.json',V/'results_supplement_initial_failure/check_hydrostatic_224_results_supplement.py']:bind(p)
ck('no primaryendpoint asserted','UNRESOLVED'in(R/'RESULTS.md').read_text()and 'UNRESOLVED'in(R/'RESULTS_SUPPLEMENT.md').read_text());out=dict(utc=datetime.now(timezone.utc).isoformat(),status='PASS_SCOPED_N224_AUXILIARY_AUDIT',count=len(checks),checks=checks,bindings=bindings,actual_reviews=reviews,check_groups={n:len(d['checks'])for n,d in records.items()},verdict='CONFIRMED finite diagnostics and exact-data center and far-axis necessary-condition failures for this represented auxiliary trial.',primary_endpoint='UNRESOLVED',scope='No inverse error enclosure, full-plane candidate, continuum supremum, convergence theorem, nearby-state exclusion, degree23 completion or causal quadrature-dominance conclusion.')
(V/'FINAL_BINDINGS.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'],out['count'],out['utc'])
