"""Bind current finite-array gates and actual reviews. No inverse evaluation."""
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib
R=Path('research/hydrostatic_common_residual_audit');V=R/'verification';checks=[];bindings={};sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def ck(n,b):
 checks.append({'name':n,'passed':bool(b)})
 if not b:raise AssertionError(n)
def bind(p,h=None):
 p=Path(p);actual=sha(p)
 if h is not None:ck('binding '+str(p),actual==h)
 bindings[str(p)]=actual
 return p
expected={'RUN.json':155,'SUMMARY.json':758,'ADAPTIVE.json':610,'ADAPTIVE_SUMMARY.json':2718,'MP_JETS.json':163,'MP_EXTENDED_MANUFACTURES.json':112,'MP_MANUFACTURE_SMOKE.json':14,'MP_SENSITIVITY.json':233,'MP_SENSITIVITY_MANUFACTURES.json':9,'FRACTION_FIXED.json':173,'FRACTION_ADAPTIVE.json':417,'FRACTION_MANUFACTURES_FINAL.json':30,'FRACTION_IO_MANUFACTURES.json':14,'FRACTION_REVIEW_BINDINGS.json':129,'ARITHMETIC_BRIDGE.json':584,'FINAL_SCOPE_CHECKS.json':259,'SCOPE_COUNT_CHECKS.json':228}
gates={}
for name,count in expected.items():
 d=json.loads(bind(V/name).read_text());gates[name]=d
 ck(name+' completed',d['status'] in ['PASS','PASS_SCOPED_FINITE_ARRAYS'] and len(d['checks'])==count and all(x['passed'] for x in d['checks']) and d.get('count',count)==count)
 for key in ['bindings','source_sha256']:
  for p,h in d.get(key,{}).items():bind(p,h)
 for p,h in d.get('modules',{}).items():bind(Path(p) if '/' in p else Path('independent_code')/p,h)
 for f in d.get('files',[]):bind(f['path'],f['sha256'])
historical=json.loads(bind(V/'FRACTION_MANUFACTURES.json').read_text())
ck('historical manufacture executed driver archived',sha(V/'before_fraction_context_closure/check_residual_fraction_arithmetic.py')==historical['bindings'][str(Path('independent_code/check_residual_fraction_arithmetic.py').resolve())])
bind(V/'before_fraction_context_closure/check_residual_fraction_arithmetic.py')
for directory in ['closure_initial_failure','closure_second_failure']:
 for p in (V/directory).iterdir():
  if p.is_file():bind(p)
reviews=[]
for name in ['review','followup','mp_design','rational','rational_recheck','rational_final','rational_closure','numerical','numerical_followup','numerical_final']:
 d=V/('opus_'+name);m=json.loads((d/'metadata.json').read_text());raw=json.loads((d/'response.json').read_text())
 ck(name+' actual model',m['requested_model']=='us.anthropic.claude-opus-5-5' and m['returned_model']==raw['model']=='claude-opus-5-5');ck(name+' complete',m['stop_reason']=='end_turn' and m['answer_nonempty']);ck(name+' answer extraction','\n'.join(x['text'] for x in raw['content'] if x['type']=='text').strip()==(d/'answer.md').read_text().strip())
 if 'request_sha256' in m:ck(name+' send-time request hash',sha(d/'request.txt')==m['request_sha256'])
 else:
  ck(name+' old schema explicitly admitted',name in ['review','followup','mp_design'])
  proof=R/'PROOF.md' if name=='mp_design' else V/'EXECUTED_BASE_PROTOCOL.md'
  bind(proof,m['proof_sha256']);m['request_binding_scope']='Captured request hash bound now; older API metadata did not export a send-time request hash'
 for f in ['request.txt','response.json','metadata.json','answer.md']:bind(d/f)
 reviews.append({'name':name,**m})
d=V/'opus_rational_followup';m=json.loads((d/'metadata.json').read_text());ck('refusal retained as nonapproval',m['stop_reason']=='refusal' and not m['answer_nonempty'])
for f in ['request.txt','response.json','metadata.json','answer.md']:bind(d/f)
for p in R.glob('*.md'):bind(p)
for p in [Path(__file__),V/'producer_definition_static.py',V/'INPUTS.json']:bind(p)
sens=gates['MP_SENSITIVITY.json'];tokens=sens['tokens'];ck('original70',sum(t['version']=='original_q3' for t in tokens)==70);ck('revision117',sum(t['version']=='revision153' for t in tokens)==117)
ck('original58and12',sum(t['version']=='original_q3' and t['verdict']=='CONFIRMED' for t in tokens)==58 and sum(t['version']=='original_q3' and t['verdict']=='REFUTED' for t in tokens)==12)
ck('revision101and16',sum(t['version']=='revision153' and t['verdict']=='CONFIRMED' for t in tokens)==101 and sum(t['version']=='revision153' and t['verdict']=='REFUTED' for t in tokens)==16)
sc=gates['SCOPE_COUNT_CHECKS.json'];ck('finite sensitivity35of70',sc['counts']['mask_sensitive_distinct_triples']==35 and sc['counts']['distinct_triples']==70);ck('84records',sc['counts']['mask_sensitive_records']==84);ck('zeroT',[x['zero_T_rows'] for x in sc['zero_T_by_region']]==[2,6,3,0,0]);ck('outer source bound',sc['source_outer_endpoint']==1000001)
text=(R/'RESULTS.md').read_text()
for phrase in ['117 tokens from producer revision 153: 70 artifact tokens and 47 report tokens','Amended UTC','same aggregate counts within those label-changing scenarios','Numerical changes among label-stable scenarios were not counted','counts separate fixed-only from both-label changes','post hoc','true auxiliary inverse','not evidence for or against post-run editing']:
 ck('final wording '+phrase,phrase in text)
ck('ten actual completed reviews',len(reviews)==10)
out={'status':'PASS_SCOPED_FINITE_ARRAYS','utc':datetime.now(timezone.utc).isoformat(),'count':len(checks),'checks':checks,'bindings':bindings,'gates':expected,'actual_model':'claude-opus-5-5','completed_reviews':reviews,'refused_call':'opus_rational_followup: retained, no approval','post_review_repairs':'FINAL_REVIEW_RESOLUTION.md, independently checked by referee; no invented post-fix Opus review','verdict':'CONFIRMED stated finite represented values and comparisons; OPEN true auxiliary inverse error, unexported producer-mask attribution for84records/35triples, uniform bounds and exact profile','primary_verdict':'UNRESOLVED','scope':'Closure assertion count is bookkeeping, not an accuracy estimate. No full-plane endpoint.'}
(V/'FINAL_BINDINGS.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'],out['count'],out['utc'])
