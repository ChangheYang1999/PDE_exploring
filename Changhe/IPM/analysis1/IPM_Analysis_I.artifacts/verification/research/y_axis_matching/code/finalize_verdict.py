"""Bind the conditional y-axis jet proof, source, outputs and model exchange."""
import json,hashlib,sys,os
from pathlib import Path
from datetime import datetime,timezone
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];E=B/'research/y_axis_matching/evidence';sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest();load=lambda p:json.loads(Path(p).read_text())
r=load(E/'checks.json');a=load(E/'output_audit.json');s=load(E/'review_summary.json');run=load(E/'local_run.json');arun=load(E/'audit_run.json')
assert r['status']==a['status']=='PASS' and run['returncode']==arun['returncode']==0
assert r['code_sha256']==a['check_code_sha256']==sha(B/'research/y_axis_matching/code/check_jets.py')
assert r['proof_sha256']==a['proof_sha256']==sha(B/'research/y_axis_matching/PROOF.md')
assert a['checks_sha256']==s['checks_sha256']==sha(E/'checks.json') and s['audit_sha256']==sha(E/'output_audit.json') and a['code_sha256']==sha(B/'research/y_axis_matching/code/audit_output.py')
assert a['fresh_containments']==44 and len(r['exact_identities'])==24
assert r['data_sha256']==sha(B/'data_exact/modal_v2.json')=='57f67a53c1ee5c8fd5ede8480428f1a5584123ac4e54b6d3530d091ea2a67ca6'
times=[run['start_utc'],r['utc'],run['end_utc'],arun['start_utc'],a['utc'],arun['end_utc']];assert all(datetime.fromisoformat(x)<datetime.fromisoformat(y) for x,y in zip(times,times[1:]))
paths={Path(__file__),B/'research/y_axis_matching/PROOF.md',B/'research/y_axis_matching/code/check_jets.py',B/'research/y_axis_matching/code/audit_output.py',B/'data_exact/modal_v2.json'}|{E/f for f in ['checks.json','output_audit.json','review_summary.json','local_run.json','audit_run.json','proof_first.json','review_repairs.json']};reviews={}
for tag in ['y_axis_matching_proof','y_axis_matching_closure']:
 m=load(B/f'notes/reviews/{tag}_metadata.json');resp=load(B/f'notes/reviews/{tag}_response.json');req=(B/f'notes/reviews/{tag}_request.txt').read_text();text=(B/f'notes/reviews/{tag}_response.md').read_text()
 assert m['actual_response_model']==resp['model']=='claude-opus-5-5' and m['stop_reason']==resp['stop_reason']=='end_turn'
 assert sha(B/f'notes/reviews/{tag}_request.txt')==m['input_sha256'] and text=='\n\n'.join(x['text'] for x in resp['content'] if x['type']=='text')+'\n'
 if tag.endswith('closure'):
  assert 'ACCEPT_STATED_SCOPE' in text and datetime.fromisoformat(arun['end_utc'])<datetime.fromisoformat(m['start_utc'])
  for f in m['files']:assert req.split('\n\nFILE '+f+'\n',1)[1].split('\n\nFILE ',1)[0]==(B/f).read_text()
 reviews[tag]={'model':m['actual_response_model'],'stop_reason':m['stop_reason'],'end_utc':m['end_utc']}
 for suf in ['metadata.json','request.txt','response.json','response.md']:paths.add(B/f'notes/reviews/{tag}_{suf}')
o={'utc':datetime.now(timezone.utc).isoformat(),'status':'CONFIRMED_EXACT_JETS_AND_CONDITIONAL_DIAGONAL_MATCHING','confirmed':['Canonical Fourier-y trace and velocity Taylor coefficients','Exact coupled x2 and x4 rows and cubic range compatibility','Far endpoint uniqueness and explicit weighted integral bounds for known diagonal forcing','Resonant second-jet condition and independent cubic normalization','Cutoff-independent regularized fourth-jet matching and Sobolev exclusion at s>=p2+1/2','Homogeneous diagonal Sobolev rate and manufactured divergent bare integrals'],'refuted':['A convergent bare fourth-jet integral for every smooth admissible solution','Inferring coupled cokernel dimension from the diagonal matching count'],'open':['Canonical trace boundedness on the proposed completed spaces','Positivity of v and sufficient smoothness for the numerical trial','Coupled index, Fredholmness and inverse','Any PDE existence or exclusion endpoint'],'methods':r['method']+' Fresh1536-bit output audit44containments.','reviews':reviews,'review_corrections':['Proof review requests R1-R7 answered in review_repairs.json and current closure','The rational numerical endpoint example is not compactly supported; the separate compact smooth example is proved analytically','Symbolic cubic_unconstrained includes a tautological strain cancellation; the standalone argument proves the coefficient identity'],'review_limit':'Text reviewers did not execute or rehash; local finalizer verifies the reviewed source/output chain.','files':{str(p.relative_to(B)):sha(p) for p in sorted(paths)}}
t=E/'verdict.json.tmp';t.write_text(json.dumps(o,indent=2)+'\n');os.replace(t,E/'verdict.json')
for p,h in o['files'].items():assert sha(B/p)==h
print(json.dumps({'utc':o['utc'],'status':o['status'],'sha256':sha(E/'verdict.json'),'pins':len(paths)}))
