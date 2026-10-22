"""Bind the conditional y-axis jet proof, source, outputs and model exchange."""
import json,hashlib,sys,os
from pathlib import Path
from datetime import datetime,timezone
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];E=B/'research/tail_coordinates/evidence';sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest();load=lambda p:json.loads(Path(p).read_text())
r=load(E/'checks.json');a=load(E/'output_audit.json');s=load(E/'review_summary.json');run=load(E/'local_run.json');arun=load(E/'audit_run.json')
assert r['status']==a['status']=='PASS' and run['returncode']==arun['returncode']==0
assert r['code_sha256']==a['check_code_sha256']==sha(B/'research/tail_coordinates/code/check_tail.py')
assert r['proof_sha256']==a['proof_sha256']==sha(B/'research/tail_coordinates/PROOF.md')
assert a['checks_sha256']==s['checks_sha256']==sha(E/'checks.json') and s['audit_sha256']==sha(E/'output_audit.json') and a['code_sha256']==sha(B/'research/tail_coordinates/code/audit_output.py')
assert a['fresh_containments']==120 and len(r['exact_identities'])==38
assert r['data_sha256']==sha(B/'data_exact/modal_v2.json')=='57f67a53c1ee5c8fd5ede8480428f1a5584123ac4e54b6d3530d091ea2a67ca6'
times=[run['start_utc'],r['utc'],run['end_utc'],arun['start_utc'],a['utc'],arun['end_utc']];assert all(datetime.fromisoformat(x)<datetime.fromisoformat(y) for x,y in zip(times,times[1:]))
paths={Path(__file__),B/'research/tail_coordinates/PROOF.md',B/'research/tail_coordinates/code/check_tail.py',B/'research/tail_coordinates/code/audit_output.py',B/'data_exact/modal_v2.json'}|{E/f for f in ['checks.json','output_audit.json','review_summary.json','local_run.json','audit_run.json','proof_first.json','review_repairs.json']};reviews={}
for tag in ['tail_coordinates_proof','tail_coordinates_closure']:
 m=load(B/f'notes/reviews/{tag}_metadata.json');resp=load(B/f'notes/reviews/{tag}_response.json');req=(B/f'notes/reviews/{tag}_request.txt').read_text();text=(B/f'notes/reviews/{tag}_response.md').read_text()
 assert m['actual_response_model']==resp['model']=='claude-opus-5-5' and m['stop_reason']==resp['stop_reason']=='end_turn'
 assert sha(B/f'notes/reviews/{tag}_request.txt')==m['input_sha256'] and text=='\n\n'.join(x['text'] for x in resp['content'] if x['type']=='text')+'\n'
 if tag.endswith('closure'):
  assert 'ACCEPT_STATED_SCOPE' in text and datetime.fromisoformat(arun['end_utc'])<datetime.fromisoformat(m['start_utc'])
  for f in m['files']:assert req.split('\n\nFILE '+f+'\n',1)[1].split('\n\nFILE ',1)[0]==(B/f).read_text()
 reviews[tag]={'model':m['actual_response_model'],'stop_reason':m['stop_reason'],'end_utc':m['end_utc']}
 for suf in ['metadata.json','request.txt','response.json','response.md']:paths.add(B/f'notes/reviews/{tag}_{suf}')
dependency=load(B/'research/far_domain/evidence/verdict.json')
assert dependency['status']=='CONFIRMED_CONDITIONAL_FAR_DOMAIN_OBSTRUCTION'
for f,h in dependency['files'].items():assert sha(B/f)==h
paths|={B/'research/far_domain/evidence/verdict.json',B/'research/far_domain/PROOF.md'}
o={'utc':datetime.now(timezone.utc).isoformat(),'status':'CONFIRMED_TAIL_IDENTITIES_AND_CONDITIONAL_BLOCK_CRITERIA','confirmed':['Cartesian tail jets, log correction and nonzero angular-fourth/zero Cartesian-fourth counterexample','Full-tail remainder still diverges radially after angular jet subtraction','Exact scalar extraction including strain of both tail columns','Sufficient zeroth-order far bounds and exact uniform angular trace integration','Fixed-cutoff multipliers2/nu2 and24/nu4, cancellations and flat high-frequency trace estimate','Half-plane strain kernel and exact dual remainder constant','Reduced matching column, conditional transversality and onto-preserving block closure'],'refuted':['Using a nonzero angular fourth coefficient as a proxy for nonzero Cartesian fourth jet','Inferring conormal graph membership of the scaling remainder from radial pointwise decay alone'],'open':['Full conormal mapping and canonical velocity on the completion','Actual coupled cokernel, nonzero pairing and block constants','Scaling remainder graph membership','Any PDE existence or exclusion endpoint'],'methods':r['method']+' Fresh1536-bit audit120containments.','reviews':reviews,'review_corrections':['Initial actualOpus proof review required no mathematical repairs; explicit C7 and matrix illustrations were added before code','All finite matrices are illustrative, not profile discretizations','The graph-domain and zeroth-order-only qualifications are retained'],'review_limit':'Text reviewers did not execute or rehash; local finalizer checks the current reviewed bundle and dependency manifest.','files':{str(p.relative_to(B)):sha(p) for p in sorted(paths)}}
t=E/'verdict.json.tmp';t.write_text(json.dumps(o,indent=2)+'\n');os.replace(t,E/'verdict.json')
for p,h in o['files'].items():assert sha(B/p)==h
print(json.dumps({'utc':o['utc'],'status':o['status'],'sha256':sha(E/'verdict.json'),'pins':len(paths)}))
