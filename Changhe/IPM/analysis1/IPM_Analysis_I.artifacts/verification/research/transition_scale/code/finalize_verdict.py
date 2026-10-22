"""Bind exact transition-symbol identities and their restricted obstruction scope."""
import json,hashlib,sys,os
from pathlib import Path
from datetime import datetime,timezone
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];E=B/'research/transition_scale/evidence'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
load=lambda p:json.loads(Path(p).read_text())
r=load(E/'checks.json');a=load(E/'output_audit.json');run=load(E/'local_run.json');arun=load(E/'audit_run.json')
assert r['status']==a['status']=='PASS' and run['returncode']==arun['returncode']==0
assert r['code_sha256']==a['check_code_sha256']==sha(B/'research/transition_scale/code/check_transition.py')=='fa4b3f96eb3cbc8e1830329c7bc86175968b62e14606d7152adc3f855d4d8373'
assert r['proof_sha256']==a['proof_sha256']==sha(B/'research/transition_scale/PROOF.md')=='4483b7264552fc17b7c5655a837597613311764854395c0ae36718e00e335cfe'
assert a['checks_sha256']==sha(E/'checks.json') and a['code_sha256']==sha(B/'research/transition_scale/code/audit_output.py')=='532918045498d3a17f23ff6aa4f3e7df1b01a340a33f70c8b77a26191ff9ed90'
times=[run['start_utc'],r['utc'],run['end_utc'],arun['start_utc'],a['utc'],arun['end_utc']];assert all(datetime.fromisoformat(x)<datetime.fromisoformat(y) for x,y in zip(times,times[1:]))
assert a['fresh_matrix_containments']==8 and a['exact_corners']==4 and a['exact_collapse_rates']==34
paths={Path(__file__),B/'research/transition_scale/PROOF.md',B/'research/transition_scale/code/check_transition.py',B/'research/transition_scale/code/audit_output.py'}|{E/f for f in ['checks.json','output_audit.json','local_run.json','audit_run.json','proof_first.json','review_repairs.json','check_repair.json','lead_prow1_answer.md','failed_first_check.log','failed_first_local_run.json','failed_first_check_transition.py.txt']};reviews={}
for tag in ['transition_scale_proof','transition_scale_closure']:
 m=load(B/f'notes/reviews/{tag}_metadata.json');resp=load(B/f'notes/reviews/{tag}_response.json');req=(B/f'notes/reviews/{tag}_request.txt').read_text();text=(B/f'notes/reviews/{tag}_response.md').read_text()
 assert m['actual_response_model']==resp['model']=='claude-opus-5-5' and m['stop_reason']==resp['stop_reason']=='end_turn'
 assert sha(B/f'notes/reviews/{tag}_request.txt')==m['input_sha256'] and text=='\n\n'.join(x['text'] for x in resp['content'] if x['type']=='text')+'\n'
 if tag.endswith('closure'):
  assert 'ACCEPT_STATED_SCOPE' in text and 'withdrawn' in text and datetime.fromisoformat(arun['end_utc'])<datetime.fromisoformat(m['start_utc'])
  for f in m['files']:assert req.split('\n\nFILE '+f+'\n',1)[1].split('\n\nFILE ',1)[0]==(B/f).read_text()
 reviews[tag]={'model':m['actual_response_model'],'stop_reason':m['stop_reason'],'end_utc':m['end_utc']}
 for suf in ['metadata.json','request.txt','response.json','response.md']:paths.add(B/f'notes/reviews/{tag}_{suf}')
o={'utc':datetime.now(timezone.utc).isoformat(),'status':'CONFIRMED_HAMILTON_IDENTITIES_AND_CONDITIONAL_NEGATIVITY_OBSTRUCTIONS','confirmed':['Hamilton stretching and scale term with constant exponent b','Variable b contributes additional V1*bprime*log(a)','Finite-endpoint collapse makes beta_perp unbounded above under stated hypotheses','Pure-strip characteristic rate with w and mu nonzero and iterated source limit','Exact source-model lower290443/10000 in the illustrative box','Moving cutoff commutator'],'refuted':['Uniform negativity of this beta in the stated scale-collapse regime','Uniform negative pure-strip characteristic rate near the stated source model'],'open':['Global fractional realization and operator calculus','Remainders and nonlocal rank-one strain estimate','Any full inverse or Fredholm conclusion','PDE existence/exclusion endpoints'],'exact_source_rate_lower':'290443/10000','methods':'Independent Hamilton differentiation; exact rational corners and examples; Arb512 and iv180 symmetric-matrix radicals; fresh Arb1536 output audit.','reviews':reviews,'review_corrections':['Stationary F fixes signs of coupling and damping, contrary to first reviewer optional remarks; closure withdraws those remarks','Variable-b extra term need not diverge if its coefficient vanishes. Only its exact algebraic presence is claimed in the proof.'],'review_limit':'Text reviews do not execute code; this finalizer binds reviewed source and outputs.','runtime':r['runtime'],'files':{str(p.relative_to(B)):sha(p) for p in sorted(paths)}}
t=E/'verdict.json.tmp';t.write_text(json.dumps(o,indent=2)+'\n');os.replace(t,E/'verdict.json')
for p,h in o['files'].items():assert sha(B/p)==h
print(json.dumps({'utc':o['utc'],'status':o['status'],'sha256':sha(E/'verdict.json'),'pins':len(paths)}))
