"""Bind the conditional far-domain proof, source, outputs and model exchange."""
import json,hashlib,sys,os
from pathlib import Path
from datetime import datetime,timezone
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];E=B/'research/far_domain/evidence';sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest();load=lambda p:json.loads(Path(p).read_text())
r=load(E/'checks.json');a=load(E/'output_audit.json');s=load(E/'review_summary.json');run=load(E/'local_run.json');arun=load(E/'audit_run.json')
assert r['status']==a['status']=='PASS' and run['returncode']==arun['returncode']==0
assert r['code_sha256']==a['check_code_sha256']==sha(B/'research/far_domain/code/check_domain.py')
assert r['proof_sha256']==a['proof_sha256']==sha(B/'research/far_domain/PROOF.md')
assert a['checks_sha256']==s['checks_sha256']==sha(E/'checks.json') and s['audit_sha256']==sha(E/'output_audit.json') and a['code_sha256']==sha(B/'research/far_domain/code/audit_output.py')
assert a['fresh_containments']==26 and len(r['exact_identities'])==12
assert r['data_sha256']==sha(B/'data_exact/modal_v2.json')=='57f67a53c1ee5c8fd5ede8480428f1a5584123ac4e54b6d3530d091ea2a67ca6'
times=[run['start_utc'],r['utc'],run['end_utc'],arun['start_utc'],a['utc'],arun['end_utc']];assert all(datetime.fromisoformat(x)<datetime.fromisoformat(y) for x,y in zip(times,times[1:]))
paths={Path(__file__),B/'research/far_domain/PROOF.md',B/'research/far_domain/code/check_domain.py',B/'research/far_domain/code/audit_output.py',B/'data_exact/modal_v2.json'}|{E/f for f in ['checks.json','output_audit.json','review_summary.json','local_run.json','audit_run.json','proof_first.json','review_repairs.json']};reviews={}
for tag in ['far_domain_proof','far_domain_closure']:
 m=load(B/f'notes/reviews/{tag}_metadata.json');resp=load(B/f'notes/reviews/{tag}_response.json');req=(B/f'notes/reviews/{tag}_request.txt').read_text();text=(B/f'notes/reviews/{tag}_response.md').read_text()
 assert m['actual_response_model']==resp['model']=='claude-opus-5-5' and m['stop_reason']==resp['stop_reason']=='end_turn'
 assert sha(B/f'notes/reviews/{tag}_request.txt')==m['input_sha256'] and text=='\n\n'.join(x['text'] for x in resp['content'] if x['type']=='text')+'\n'
 if tag.endswith('closure'):
  assert 'ACCEPT_STATED_SCOPE' in text and 'That was false' in text and datetime.fromisoformat(arun['end_utc'])<datetime.fromisoformat(m['start_utc'])
  for f in m['files']:assert req.split('\n\nFILE '+f+'\n',1)[1].split('\n\nFILE ',1)[0]==(B/f).read_text()
 reviews[tag]={'model':m['actual_response_model'],'stop_reason':m['stop_reason'],'end_utc':m['end_utc']}
 for suf in ['metadata.json','request.txt','response.json','response.md']:paths.add(B/f'notes/reviews/{tag}_{suf}')
o={'utc':datetime.now(timezone.utc).isoformat(),'status':'CONFIRMED_CONDITIONAL_FAR_DOMAIN_OBSTRUCTION','confirmed':['Nonzero exact transported density is outside H_gamma for gamma<1+1/cl, without homogeneous asymptotics','E rho and K=(E-1)rho are outside H_gamma for1<gamma<1+k under the stated sublinear hypotheses','Compact smooth parity-compatible perturbation with ell>1.33e-7 explicitly constructed','U[h].grad rho belongs to H_gamma and cannot cancel (ell/3)E rho in the far field','Jet-plus-remainder embedding into H_gamma under the specified norms','Canonical scaling covariance and conditional cubic coefficient2'],'refuted':['Dropping the exterior U[h].grad rho term for compact h','Full linearized mapping into this far target from a domain containing the stated compact core'],'open':['Existence of an exact profile satisfying these hypotheses','Mapping and inverse after explicit tail coordinates','Fredholm index and coupled kernel dimensions','Any PDE existence or exclusion endpoint'],'methods':r['methods']+' Fresh1536-bit output audit26containments.','reviews':reviews,'review_corrections':['Delta psi=-partial_x rho and -Delta psi=partial_x rho are identical; first reviewer claim of sign change explicitly withdrawn','Scaling uses V_lambda and canonical uniqueness is proved','A smaller abstract domain need not retain compact core; only domains containing the specified core are excluded'],'review_limit':'Text reviewers did not execute or rehash; local finalizer verifies the reviewed source/output chain.','files':{str(p.relative_to(B)):sha(p) for p in sorted(paths)}}
t=E/'verdict.json.tmp';t.write_text(json.dumps(o,indent=2)+'\n');os.replace(t,E/'verdict.json')
for p,h in o['files'].items():assert sha(B/p)==h
print(json.dumps({'utc':o['utc'],'status':o['status'],'sha256':sha(E/'verdict.json'),'pins':len(paths)}))
