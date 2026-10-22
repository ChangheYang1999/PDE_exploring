"""Bind local regularity proof, independent checks and actual model exchange."""
import sys,json,hashlib,os
from pathlib import Path
from datetime import datetime,timezone
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];E=B/'research/lower_regularity/evidence';sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest();load=lambda p:json.loads(Path(p).read_text())
r=load(E/'checks.json');a=load(E/'output_audit.json');s=load(E/'review_summary.json');run=load(E/'local_run.json');arun=load(E/'audit_run.json');first=load(E/'proof_first.json')
assert r['status']==a['status']=='PASS' and run['returncode']==arun['returncode']==0
assert r['code_sha256']==a['check_code_sha256']==sha(B/'research/lower_regularity/code/check_regularity.py')
assert r['proof_sha256']==a['proof_sha256']==sha(B/'research/lower_regularity/PROOF.md')
assert r['input_sha256']==sha(E/'inputs.json') and r['data_sha256']==sha(B/'data_exact/modal_v2.json')=='57f67a53c1ee5c8fd5ede8480428f1a5584123ac4e54b6d3530d091ea2a67ca6'
assert a['checks_sha256']==s['checks_sha256']==sha(E/'checks.json') and s['audit_sha256']==sha(E/'output_audit.json') and a['code_sha256']==sha(B/'research/lower_regularity/code/audit_output.py')
assert len(r['exact_identities'])==19 and a['fresh_containments']==54 and a['fresh_differential_cancellations']==8
assert first['original_proof_sha256']==sha(E/'proof_before_review.md')
times=[first['proof_existed_by_utc'],run['start_utc'],r['utc'],run['end_utc'],arun['start_utc'],a['utc'],arun['end_utc']];assert all(datetime.fromisoformat(x)<datetime.fromisoformat(y) for x,y in zip(times,times[1:]))
paths={Path(__file__),B/'research/lower_regularity/PROOF.md',B/'research/lower_regularity/code/check_regularity.py',B/'research/lower_regularity/code/audit_output.py',B/'data_exact/modal_v2.json'}|{E/n for n in ['inputs.json','checks.json','output_audit.json','review_summary.json','local_run.json','audit_run.json','proof_first.json','proof_before_review.md','review_repairs.json','audit_first_diagnostic.json','audit_first_diagnostic.log']};reviews={}
for tag in ['lower_regularity_proof','lower_regularity_closure']:
 m=load(B/f'notes/reviews/{tag}_metadata.json');resp=load(B/f'notes/reviews/{tag}_response.json');req=(B/f'notes/reviews/{tag}_request.txt').read_text();text=(B/f'notes/reviews/{tag}_response.md').read_text()
 assert m['actual_response_model']==resp['model']=='claude-opus-5-5' and m['stop_reason']==resp['stop_reason']=='end_turn'
 assert sha(B/f'notes/reviews/{tag}_request.txt')==m['input_sha256'] and text=='\n\n'.join(x['text'] for x in resp['content'] if x['type']=='text')+'\n'
 if tag.endswith('closure'):
  assert 'ACCEPT_STATED_SCOPE' in text and datetime.fromisoformat(arun['end_utc'])<datetime.fromisoformat(m['start_utc'])
  for f in m['files']:assert req.split('\n\nFILE '+f+'\n',1)[1].split('\n\nFILE ',1)[0]==(B/f).read_text()
 reviews[tag]={'model':m['actual_response_model'],'stop_reason':m['stop_reason'],'end_utc':m['end_utc']}
 for suf in ['metadata.json','request.txt','response.json','response.md']:paths.add(B/f'notes/reviews/{tag}_{suf}')
deps={}
for topic,h in [('far_domain','34423a02e39dae286420c5bbd3723c0344868be3c51c4d715237eaea529ab6d8'),('pure_source','1164a6d074aab61625760ad68e4362fa2c3de0306ab608cbd00b88dc457a5a1e'),('y_axis_matching','d9253ca5809b2691434d1cb0efa6274f0ac4337c39c8f4554d1cb4b8218cdcaa')]:
 p=B/f'research/{topic}/evidence/verdict.json';assert sha(p)==h;v=load(p)
 for f,hs in v['files'].items():assert sha(B/f)==hs
 paths.add(p);deps[topic]=h
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'CONFIRMED_LOCAL_OBSTRUCTIONS_AND_CONDITIONAL_IDENTITIES','confirmed':['Frozen nonlocal source recurrence and harmonic local forcing','Exact Sobolev threshold p+1/2 including endpoint failure','Same-operator global domain-transfer lemma and affine nonlinear identities','Exact whole-plane unweighted strain norm, endpoint H2 failure, center-vanishing t<2 sequence','Unaugmented low-order bilinear estimate fails','C2alpha and H3.1 do not imply continuous center factorization','Interpolation constant1 and cutoff derivative bound','Corrected weight window and frozen energy signs','Conditional index change and explicitly defined annular norm threshold'],'refuted':['Local smooth forcing alone upgrades frozen-source Sobolev regularity','Unaugmented Ht strain continuity for t<=2','Regularity alone implies the required center factorization'],'open':['Global high-order tame estimate','SPEC fractional norm equivalence and actual corner projection','Full inverse and every profile existence or exclusion endpoint'],'methods':r['method']+' Fresh1536-bit54containments;4096-bit exact Machin bracket audit;8fresh differential cancellations.','reviews':reviews,'dependencies':deps,'review_limit':'Text reviews did not execute or verify hashes. This local finalizer verifies their current bundles and all cited evidence.','files':{str(p.relative_to(B)):sha(p) for p in sorted(paths)}}
p=E/'verdict.json.tmp';p.write_text(json.dumps(out,indent=2)+'\n');os.replace(p,E/'verdict.json')
for f,h in out['files'].items():assert sha(B/f)==h
print(json.dumps({'utc':out['utc'],'status':out['status'],'pins':len(paths),'sha256':sha(E/'verdict.json')}))
