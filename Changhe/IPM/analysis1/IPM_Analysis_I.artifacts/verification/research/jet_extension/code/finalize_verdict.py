"""Bind the fixed-extension proof, independent enclosures, audit and actual model reviews."""
import json,hashlib,sys,os
from pathlib import Path
from datetime import datetime,timezone
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];E=B/'research/jet_extension/evidence'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
load=lambda p:json.loads(Path(p).read_text())
r=load(E/'checks.json');a=load(E/'output_audit.json');run=load(E/'local_run.json');arun=load(E/'audit_run.json')
assert r['status']==a['status']=='PASS' and run['returncode']==arun['returncode']==0
assert r['code_sha256']==a['check_code_sha256']==sha(B/'research/jet_extension/code/check_extension.py')=='b04818d8616e409498b4f938348cb77d2faa79f6ba2c4de64d6f17643690d2cd'
assert r['proof_sha256']==a['proof_sha256']==sha(B/'research/jet_extension/PROOF.md')=='ce8ecd6e365885514924d9774fdbc801236c07f18453e419e78b2f192289f458'
assert a['checks_sha256']==sha(E/'checks.json') and a['code_sha256']==sha(B/'research/jet_extension/code/audit_output.py')=='41777c106a5c96d8993036743616e454252a48a48d7cf9fa2d4b2aa38685a95d'
times=[run['start_utc'],r['utc'],run['end_utc'],arun['start_utc'],a['utc'],arun['end_utc']];assert all(datetime.fromisoformat(x)<datetime.fromisoformat(y) for x,y in zip(times,times[1:]))
assert a['fresh_constant_containments']==6 and a['fresh_frequency_containments']==16 and a['exact_midpoints']==8192 and a['exact_positive_moments']==161
paths={Path(__file__),B/'research/jet_extension/PROOF.md',B/'research/jet_extension/code/check_extension.py',B/'research/jet_extension/code/audit_output.py',B/'research/jet_extension/code/diagnose_extension.py'}|{E/f for f in ['checks.json','output_audit.json','local_run.json','audit_run.json','proof_first.json','review_repairs.json','failed_first_check.log','failed_first_local_run.json','failed_first_check_extension.py.txt','diagnostic.log','diagnostic_run.json']};reviews={}
for tag in ['jet_extension_proof','jet_extension_closure']:
 m=load(B/f'notes/reviews/{tag}_metadata.json');resp=load(B/f'notes/reviews/{tag}_response.json');req=(B/f'notes/reviews/{tag}_request.txt').read_text();text=(B/f'notes/reviews/{tag}_response.md').read_text()
 assert m['actual_response_model']==resp['model']=='claude-opus-5-5' and m['stop_reason']==resp['stop_reason']=='end_turn'
 assert sha(B/f'notes/reviews/{tag}_request.txt')==m['input_sha256'] and text=='\n\n'.join(x['text'] for x in resp['content'] if x['type']=='text')+'\n'
 if tag.endswith('closure'):
  assert 'ACCEPT_STATED_SCOPE' in text and 'That remark was wrong' in text and datetime.fromisoformat(arun['end_utc'])<datetime.fromisoformat(m['start_utc'])
  for f in m['files']:assert req.split('\n\nFILE '+f+'\n',1)[1].split('\n\nFILE ',1)[0]==(B/f).read_text()
 reviews[tag]={'model':m['actual_response_model'],'stop_reason':m['stop_reason'],'end_utc':m['end_utc']}
 for suf in ['metadata.json','request.txt','response.json','response.md']:paths.add(B/f'notes/reviews/{tag}_{suf}')
o={'utc':datetime.now(timezone.utc).isoformat(),'status':'CONFIRMED_FIXED_EXTENSION_AND_CONDITIONAL_INVERSE','confirmed':['Canonical U1 and U2_y multipliers and strain signs','B gains one Sobolev derivative; P=Id-S with S arbitrarily smoothing','Explicit L1 kernel bounds and noncompactness on the whole line','Exact induced coupling N_chi including strain divided by3','Finite-interval two-sided inverse when M*n<1','Illustrative exact C2 cutoff constants and four frequency enclosures'],'refuted':['Smoothing alone implies compactness on the whole line','Low-frequency stream singularity b_hat/k for this odd-source extension','Lower precision ball must be contained in higher precision enclosure'],'open':['Domain-compatible global jet extension','Actual candidate M,n and matching','Full variable-coefficient inverse','PDE existence and exclusion endpoints'],'constants':{k:v['public_strict_upper'] for k,v in r['constant_exports'].items()},'methods':'Analytic Green and kernel derivations; Arb512 incomplete-gamma moments versus iv180 positive series with full remainder; exact rational midpoint quadrature; fresh Arb1536 endpoint-derivative audit.','reviews':reviews,'review_limit':'Text reviewer did not execute code or recompute hashes. This local finalizer binds the current reviewed bundle.','preserved_failure':'First check demanded invalid precision nesting. Diagnostic confirmed overlap and fresh narrower audit passes both.','runtime':r['runtime'],'files':{str(p.relative_to(B)):sha(p) for p in sorted(paths)}}
t=E/'verdict.json.tmp';t.write_text(json.dumps(o,indent=2)+'\n');os.replace(t,E/'verdict.json')
for p,h in o['files'].items():assert sha(B/p)==h
print(json.dumps({'utc':o['utc'],'status':o['status'],'sha256':sha(E/'verdict.json'),'pins':len(paths)}))
