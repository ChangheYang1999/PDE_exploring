"""Bind analytic end-region inequalities and actual two-model exchange."""
import sys,json,hashlib,os
from pathlib import Path
from datetime import datetime,timezone
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];E=B/'research/flow_ends/evidence';sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest();load=lambda p:json.loads(Path(p).read_text())
r=load(E/'checks.json');a=load(E/'output_audit.json');s=load(E/'review_summary.json');run=load(E/'local_run.json');arun=load(E/'audit_run.json');first=load(E/'proof_first.json')
assert r['status']==a['status']=='PASS' and run['returncode']==arun['returncode']==0
assert r['code_sha256']==a['check_code_sha256']==sha(B/'research/flow_ends/code/check_ends.py') and a['code_sha256']==sha(B/'research/flow_ends/code/audit_output.py')
assert r['proof_sha256']==a['proof_sha256']==sha(B/'research/flow_ends/PROOF.md')
assert a['checks_sha256']==s['checks_sha256']==sha(E/'checks.json') and s['audit_sha256']==sha(E/'output_audit.json')
assert a['fresh_containments']==36 and a['angular_identities']==522 and a['factor_cancellations']==260
assert first['sha256']==sha(E/'proof_before_review.md')
times=[first['utc'],run['start_utc'],r['utc'],run['end_utc'],arun['start_utc'],a['utc'],arun['end_utc']];assert all(datetime.fromisoformat(x)<datetime.fromisoformat(y) for x,y in zip(times,times[1:]))
for f,h in r['dependency_pins'].items():assert sha(B/f)==h
for f in ['research/inner_majorant/evidence/inner_result.json','research/inner_majorant/evidence/inner_iv_audit.json','research/exterior_flow/evidence/checks.json']:
 assert f in r['dependency_pins']
for topic in ['inner_majorant','exterior_flow']:
 assert load(B/f'research/{topic}/evidence/verdict.json')['status']=='CONFIRMED'
paths={Path(__file__),B/'research/flow_ends/PROOF.md',B/'research/flow_ends/code/check_ends.py',B/'research/flow_ends/code/audit_output.py'}|{E/n for n in ['checks.json','output_audit.json','review_summary.json','local_run.json','audit_run.json','local_run.log','audit_run.log','proof_first.json','proof_before_review.md','review_repairs.json','audit_first_diagnostic.json','audit_first_diagnostic.log']}|{B/f for f in r['dependency_pins']};reviews={}
for tag in ['flow_ends_proof','flow_ends_closure']:
 m=load(B/f'notes/reviews/{tag}_metadata.json');resp=load(B/f'notes/reviews/{tag}_response.json');req=(B/f'notes/reviews/{tag}_request.txt').read_text();text=(B/f'notes/reviews/{tag}_response.md').read_text()
 assert m['actual_response_model']==resp['model']=='claude-opus-5-5' and m['stop_reason']==resp['stop_reason']=='end_turn'
 assert sha(B/f'notes/reviews/{tag}_request.txt')==m['input_sha256'] and text=='\n\n'.join(x['text'] for x in resp['content'] if x['type']=='text')+'\n'
 if tag.endswith('closure'):
  assert 'ACCEPT_STATED_SCOPE' in text and datetime.fromisoformat(arun['end_utc'])<datetime.fromisoformat(m['start_utc'])
  for f in m['files']:assert req.split('\n\nFILE '+f+'\n',1)[1].split('\n\nFILE ',1)[0]==(B/f).read_text()
 reviews[tag]={'model':m['actual_response_model'],'stop_reason':m['stop_reason'],'end_utc':m['end_utc']}
 for suf in ['metadata.json','request.txt','response.json','response.md']:paths.add(B/f'notes/reviews/{tag}_{suf}')
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'CONFIRMED_ANALYTIC_END_REGIONS','public':r['public'],'inner_domain':'0<r<=exp(-685794559684773/140737488355328); axis values by continuous extension','outer_domain':'r>=exp(2289893859708677/281474976710656+9), approximately27655556.8937; not all r>=20','confirmed':['Inner v2>21.289, v1<-10.138, T<-6.53 throughout the whole inner disk.','Exterior s>5.5752, vi>5.5752, T<-.278 throughout the stated infinite tail.','Exact trial density and gradient vanish on y-axis because every radial coefficient retains global x2y factor.'],'refuted':['Lead global_flow rev3 claim that the trial y-axis density and b+ are merely residual-sized, not zero.'],'open':['Finite middle and required finite outer flow arithmetic and coverage','Full coupled inverse and every existence or exclusion endpoint'],'methods':r['method']+' Fresh1536-bit36containments,522angular and260factor identities.','reviews':reviews,'review_limit':'Text reviewers did not execute code or verify hashes; local finalizer verifies bundles, outputs and pinned dependencies. First review mistook a globally factored trial for an arbitrary sine series; exact definition and per-mode cancellations resolve that objection.','files':{str(p.relative_to(B)):sha(p) for p in sorted(paths)}}
(E/'verdict.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'utc':out['utc'],'status':out['status'],'pins':len(paths),'sha256':sha(E/'verdict.json')}))
