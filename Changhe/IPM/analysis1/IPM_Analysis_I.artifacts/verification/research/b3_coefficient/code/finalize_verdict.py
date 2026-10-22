"""Bind topic59 proof, exact checks, independent enclosures and completed Opus review."""
import json,hashlib,sys,os
from pathlib import Path
from datetime import datetime,timezone
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];E=B/'research/b3_coefficient/evidence'
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def load(p):return json.loads(Path(p).read_text())
r=load(E/'checks.json');a=load(E/'output_audit.json');run=load(E/'local_run.json');arun=load(E/'audit_run.json')
assert r['status']==a['status']=='PASS' and run['returncode']==arun['returncode']==0
assert r['source_sha256']==sha(B/'research/b3_coefficient/code/check_b3.py')=='0bd807cdd7745d3e0a02a52ab6981ac1f9be8784ccbab0f9892a7ff575552276'
assert r['proof_sha256']==a['proof_sha256']==sha(B/'research/b3_coefficient/PROOF.md')=='e0bda870f04cd5c438871165eef3bc6849acd2c4e3627d6674c4b2cdbfd55e94'
assert a['checks_sha256']==sha(E/'checks.json') and a['code_sha256']==sha(B/'research/b3_coefficient/code/audit_output.py')=='ac187ac259d3e324dacdcc466dc13afa6b1a393c957d0c181a1e65be86696201'
assert r['input_sha256']==sha(B/'data_exact/modal_v2.json')=='57f67a53c1ee5c8fd5ede8480428f1a5584123ac4e54b6d3530d091ea2a67ca6'
assert datetime.fromisoformat(run['start_utc'])<datetime.fromisoformat(r['utc'])<datetime.fromisoformat(run['end_utc'])<datetime.fromisoformat(arun['start_utc'])<datetime.fromisoformat(a['utc'])<datetime.fromisoformat(arun['end_utc'])
paths={Path(__file__),B/'research/b3_coefficient/PROOF.md',B/'research/b3_coefficient/code/check_b3.py',B/'research/b3_coefficient/code/audit_output.py',B/'data_exact/modal_v2.json'}|{E/f for f in ['checks.json','output_audit.json','local_run.json','audit_run.json','proof_first.json','review_repairs.json','lead_pinf_B3.md']};reviews={}
for tag in ['b3_coefficient_proof','b3_coefficient_closure']:
 m=load(B/f'notes/reviews/{tag}_metadata.json');resp=load(B/f'notes/reviews/{tag}_response.json');req=(B/f'notes/reviews/{tag}_request.txt').read_text();text=(B/f'notes/reviews/{tag}_response.md').read_text()
 assert m['actual_response_model']==resp['model']=='claude-opus-5-5' and m['stop_reason']==resp['stop_reason']=='end_turn'
 assert sha(B/f'notes/reviews/{tag}_request.txt')==m['input_sha256'] and text=='\n\n'.join(x['text'] for x in resp['content'] if x['type']=='text')+'\n'
 if tag.endswith('closure'):
  assert 'ACCEPT_STATED_SCOPE' in text and datetime.fromisoformat(arun['end_utc'])<datetime.fromisoformat(m['start_utc'])
  for f in m['files']:assert req.split('\n\nFILE '+f+'\n',1)[1].split('\n\nFILE ',1)[0]==(B/f).read_text()
 reviews[tag]={'model':m['actual_response_model'],'stop_reason':m['stop_reason'],'end_utc':m['end_utc']}
 for suf in ['metadata.json','request.txt','response.json','response.md']:paths.add(B/f'notes/reviews/{tag}_{suf}')
# The reviewer could not recompute hashes. This local code performs that binding, independently of its assertion.
o={'utc':datetime.now(timezone.utc).isoformat(),'status':'CONFIRMED_CONDITIONAL_RESULTS_AND_SCOPED_REFUTATIONS','confirmed':['C3 conservative Peano derivation of cubic axis equation; div/curl identities','Exact-profile endpoint slope constraint, positive first trace reconstruction, unique bounded cubic trace','Correct integrating factor H=x^-p exp(+integral(q+p/t))','Polynomial-only finite part and cutoff bound conditional on Q Taylor remainder10','B3=0 for C6,alpha factor alpha>p-6 and remainder10 with6<p<7; P_infty supplies10','Endpoint-split pullback metric and explicit conditional Lipschitz bound','Conditional smooth-profile exclusion inequality with all missing inputs named'], 'refuted':['Printed negative sign in lead A4 integrating factor','C2,alpha regularity alone supplies cubic axis trace','Continuity of B3 in Cj norms j<=6','Generic endpoint remainder admits a global uniform O(t8) bound on(0,1)','C6 alone removes fractional coefficient'], 'open':['Trial polynomial-only Q expansion and generalized logarithmic finite part','Numerical-profile B3 and class-uniform remainder','Density-norm map into the pullback metric','Actual ball and exclusion/existence endpoint'], 'cutoff_upper_multipliers':{'delta_half':'159/1000','delta_one':'5547/10000'},'cutoff_scope':'K times these constants for the exact modal p used as an illustrative exponent. The polynomial Q test is not the trial.', 'checks':r['checks'],'methods':'Independent proof; exact symbolic and rational examples; Arb512 antiderivative versus iv180 positive midpoint quadrature with analytic remainder; fresh Arb768 midpoint-sum and exact saved-output audit.','reviews':reviews,'review_repairs':load(E/'review_repairs.json'),'review_provenance_limit':'The text-only reviewer did not recompute hashes or see local_run.json. Local audit and this finalizer independently bind all actual code/output/run times.','runtime':r['runtime'],'files':{str(p.relative_to(B)):sha(p) for p in sorted(paths)}}
t=E/'verdict.json.tmp';t.write_text(json.dumps(o,indent=2)+'\n');os.replace(t,E/'verdict.json')
for p,h in o['files'].items():assert sha(B/p)==h
print(json.dumps({'utc':o['utc'],'status':o['status'],'sha256':sha(E/'verdict.json'),'pins':len(paths)}))
