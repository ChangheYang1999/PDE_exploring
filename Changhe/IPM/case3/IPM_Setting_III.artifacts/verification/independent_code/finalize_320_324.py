"""Final identity and review gates for completed finite verifier audits."""
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,sys
if sys.flags.optimize:raise SystemExit('verification refuses optimized Python')
ROOT=Path('verification')
if Path.cwd().resolve()!=ROOT:raise SystemExit('wrong lane')
now=lambda:datetime.now(timezone.utc).isoformat()
class Collector:
 def __init__(self,root):self.root=root;self.V=root/'verification';self.bindings={};self.checks=[];self.reviews=[]
 def ck(self,n,b,e=None):
  self.checks.append(dict(name=n,passed=bool(b),evidence=e))
  if not b:raise AssertionError((n,e))
 def bind(self,p,h=None):
  p=Path(p).resolve();p.relative_to(ROOT);s=hashlib.sha256(p.read_bytes()).hexdigest();key=str(p)
  self.ck('binding '+key,(h is None or h==s) and (key not in self.bindings or self.bindings[key]==s));self.bindings[key]=s;return p
 def read(self,p):return json.loads(self.bind(p).read_text())
 def import_bindings(self,d):
  for p,h in d.get('bindings',{}).items():self.bind(p,h)
  for p,h in d.get('artifacts',{}).items():self.bind(p,h)
 def gate(self,p,status):
  d=self.read(p);self.ck('status '+str(p),d['status']==status)
  if 'checks'in d:self.ck('assertions '+str(p),d.get('count',len(d['checks']))==len(d['checks']) and all(z['passed']for z in d['checks']))
  self.import_bindings(d);return d
 def execution(self,p):
  d=self.read(p);self.ck('exit0 '+str(p),d['returncode']==0)
  for k in ['wrapper_pid','timeout_pid']:
   if k in d:self.ck('ceased '+str(p)+' '+k,not Path('/proc',str(d[k])).exists())
  if 'admission_path'in d:self.bind(d['admission_path'],d['admission_sha256'])
 def review(self,label):
  folder=self.V/('opus_'+label);m=self.read(folder/'metadata.json');resp=self.read(folder/'response.json');req=self.bind(folder/'request.txt',m['request_sha256']);answer=self.bind(folder/'answer.md').read_text()
  self.ck('actual completed model '+label,m['returned_model']==resp['model']=='claude-opus-5-5' and m['stop_reason']==resp['stop_reason']=='end_turn' and m['answer_nonempty'] and bool(answer.strip()))
  self.ck('answer is actual returned text '+label,answer.strip()=='\n\n'.join(z['text']for z in resp['content']if z['type']=='text').strip())
  self.reviews.append({k:m[k]for k in ['requested_model','returned_model','request_id','started_utc','finished_utc','stop_reason']})
 def finish(self,status,report,filename):
  self.bind(__file__)
  for p in self.root.glob('*.md'):self.bind(p)
  self.bind(report)
  for p,h in list(self.bindings.items()):self.ck('final stable '+p,hashlib.sha256(Path(p).read_bytes()).hexdigest()==h)
  out=dict(status=status,utc=now(),count=len(self.checks),checks=self.checks,bindings=self.bindings,reviews=self.reviews,report=str(report),scope='Identity, successful execution and actual model-review closure for the report\'s finite scope. No new integrand replay, no inverse error enclosure, no primary endpoint. T_end not reached.')
  (self.V/filename).write_text(json.dumps(out,indent=2)+'\n');print(status,out['utc'],len(self.checks),len(self.bindings),hashlib.sha256((self.V/filename).read_bytes()).hexdigest())
def main320():
 r=Path('research/accurate_map_final_audit');a=Collector(r);v=a.V
 for fn,st in [('DESIGN_ACCEPTANCE.json','ACCEPTED_FOR_FINITE_AUXILIARY_COMPUTATION'),('FINAL_DESIGN_ACCEPTANCE.json','ACCEPTED_CANDIDATE_FREE_FINAL_CHECKER_DESIGN'),('candidate/COMPLETE.json','COMPLETE_FINITE_ACCURATE_MAP_REQUIRES_FINAL_AUDIT'),('FINAL_CHECKS.json','PASS_FINITE_ACCURATE_MAP_FINAL_REQUIRES_MODEL_REVIEW'),('PRINTED_RECORD_CHECKS.json','PASS_PRINTED_ACCURATE_MAP_RECORDS_WITH_OPEN_TEXT_SCOPE'),('REVIEW_SUPPLEMENT_CHECKS.json','PASS_POST_RESULT_CLASSIFICATION_AND_PROVENANCE'),('FINAL_SOURCE_LINKAGE.json','PASS_STATIC_BOUND_INHERITANCE_AND_SIGN_RULE')]:a.gate(v/fn,st)
 a.execution(v/'EXECUTION_RESULT.json');a.execution(v/'FINAL_CHECK_EXECUTION_RESULT.json')
 final=a.read(v/'FINAL_CHECKS.json');link=a.read(v/'FINAL_SOURCE_LINKAGE.json');a.bind(v/'FINAL_CHECKS.json',link['final_checks_sha256']);normalized={str(Path(p).resolve()):h for p,h in final['bindings'].items()}
 for p,h in link['bindings'].items():a.ck('mechanical source linkage equals final audit '+p,normalized[str(Path(p).resolve())]==h);a.bind(p,h)
 for label in ['final_results','final_resolution','final_closure']:a.review(label)
 s=(r/'RESULTS_DRAFT3.md').read_text();s=s.replace('# Independent accurate-map audit: revised results awaiting final review','# Independent accurate-map audit: CONFIRMED finite results')
 s=s.replace('Actual model review and the interpretation decision are still pending.','Three actual claude-opus-5-5 result reviews completed at07:52:58,08:04:45 and08:08:03 UTC. Their objections were independently resolved as recorded in the resolution files; the final binding collector mechanically checked the source-linkage hashes against FINAL_CHECKS.json.')
 s=s.replace('This report requires the actual final results review and a binding manifest before its verdict can be CONFIRMED.','The final limited verdict is CONFIRMED, with verification/FINAL_BINDINGS.json recording the completed identity and review gates.')
 s=s.replace('This draft resolves its substantive issues independently; actual follow-up and final binding are pending.','That second draft was followed by two actual reviews and the independent resolutions recorded here.')
 s=s.replace('final source-linkage and counting evidence are in verification/FINAL_SOURCE_LINKAGE.json.','source-linkage and counting evidence are in verification/FINAL_SOURCE_LINKAGE.json. Its scope is static linkage and finite counting, not re-execution of the full final checker; the final collector separately performed the mechanical hash comparison requested by the model.')
 s+='\nFinalized '+now()+'. Verdict CONFIRMED only for the stated finite auxiliary audit and exact saved-trial exclusions. The angular discrepancy is unexplained. Primary IPM remains UNRESOLVED; the real run deadline has not been reached.\n'
 report=r/'RESULTS.md';report.write_text(s)
 (r/'FINAL_CLOSURE_RESOLUTION.md').write_text('''# Final independent closure

The third actual model was claude-opus-5-5, request dec0c018-4374-4ef7-87b2-4be02535357c, completed08:08:03UTC. Its remaining mechanical hash comparison is performed explicitly by finalize_320_324.py against the bound FINAL_CHECKS.json entries and the current bytes. Its stale-opening and static-scope presentation edits are applied in RESULTS.md. The by-hand model could not recompute hashes; the verifier did. Its confirmation of the interpolation counterargument is accepted, while no additional optional causal or historical lower-bound claim is added. All three original drafts and actual reviews remain preserved. No accepted numerical code, inverse rule or criterion changed.

The result is CONFIRMED within the report's finite auxiliary scope. The cause of31 versus6, inverse accuracy, continuum convergence and every primary IPM endpoint remain OPEN or UNRESOLVED as stated. Completing this audit is not an early-stop endpoint.
''')
 a.finish('CONFIRMED_FINITE_ACCURATE_MAP_AUXILIARY_AUDIT',report,'FINAL_BINDINGS.json')
def main324():
 r=Path('research/hydrostatic_tail_rule_provenance');a=Collector(r);v=a.V
 for fn,st in [('DESIGN_ACCEPTANCE.json','ACCEPTED_FINITE_SELECTED_TAIL_DIAGNOSTIC'),('CHECKS.json','PASS_FINITE_SELECTED_TAIL_RULES_REQUIRES_FINAL_REVIEW'),('FINAL_SELECTED_CHECKS.json','PASS_FINITE_SELECTED_TAIL_ALGEBRA_REQUIRES_RESULT_REVIEW'),('FINAL_SELECTED_CHECKS_V2.json','PASS_FINITE_SELECTED_TAIL_ALGEBRA_REQUIRES_RESULT_REVIEW'),('SELECTED_REVIEW_DIAGNOSTICS.json','PASS_OPTIMIZATION_REFUSAL_AND_INDEPENDENT_REVIEW_DIAGNOSTICS'),('SELECTED_REVIEW_DIAGNOSTICS_V2.json','PASS_DURABLE_REVIEW_DIAGNOSTIC_REPETITION')]:a.gate(v/fn,st)
 a.execution(v/'TAIL_EXECUTION_RESULT.json')
 for p in ['independent_code/check_selected_tail_final.py','independent_code/check_selected_tail_final_v2.py','independent_code/check_selected_tail_review.py','independent_code/check_tail_rule_provenance.py']:a.bind(p)
 for label in ['selected_final','selected_closure','selected_confirm']:a.review(label)
 s=(r/'SELECTED_RESULTS_DRAFT3.md').read_text().replace('# Selected analytic-derivative tails: revised final review pending','# Selected analytic-derivative tails: CONFIRMED finite diagnostic')
 s=s.replace('Final closure and binding are pending.','The final actual claude-opus-5-5 review, request ecd1fbfe-c86f-4323-99e7-304af215529f, completed08:08:34UTC and accepted the two counterarguments with no blocking defect. The final collector binds both original and revised checker sources, their outputs, all three drafts and all three actual result reviews.')
 for x,y in [('0 or1','0 or 1'),('and0,1 or2','and 0, 1 or 2'),('of12','of 12'),('completed08:04:49UTC','completed 08:04:49 UTC')]:s=s.replace(x,y)
 s+='\nFinalized '+now()+'. Verdict CONFIRMED within the finite selected-tail scope. verification/SELECTED_FINAL_BINDINGS.json contains the completed gates. Neither the tail integrands nor exact integrals were independently replayed by the final algebra checkers; their finite difference arithmetic was independently reconstructed. Primary IPM remains UNRESOLVED and T_end has not been reached.\n'
 report=r/'SELECTED_RESULTS.md';report.write_text(s)
 (r/'SELECTED_FINAL_CLOSURE_RESOLUTION.md').write_text('''# Final independent selected-tail closure

The actual third model was claude-opus-5-5, request ecd1fbfe-c86f-4323-99e7-304af215529f, completed08:08:34UTC. It accepted both independent counterarguments: the reported finite-sum argmax is determined while its exact-integral counterpart is not, and the actual cwd is precisely the verifier lane. The final collector directly binds both checker sources and outputs and all three drafts, satisfying the two remaining provenance notes. The earlier inline diagnostics and the later durable reproduction remain distinct. The final text removes stale pending status and clarifies spacing.

The model's phrase that derivative-tail sums were reproduced exactly must be read with the report's explicit scope: the final checkers independently reconstructed finite-sum difference algebra, not the candidate tail integrands. No exact integral, error enclosure, convergence rate or historical cause is established. The finite diagnostic is CONFIRMED; the primary IPM endpoint remains UNRESOLVED. This is not an early-stop endpoint.
''')
 a.finish('CONFIRMED_FINITE_SELECTED_TAIL_DIAGNOSTIC',report,'SELECTED_FINAL_BINDINGS.json')
if __name__=='__main__':
 if sys.argv[1]=='320':main320()
 elif sys.argv[1]=='324':main324()
 else:raise SystemExit('choose320 or324')
