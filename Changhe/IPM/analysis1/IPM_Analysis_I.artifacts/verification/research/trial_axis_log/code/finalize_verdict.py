"""Bind the topic60 proof, computations, exact exports, and completed reviews."""
import json,hashlib,sys,os
from pathlib import Path
from datetime import datetime,timezone
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];E=B/'research/trial_axis_log/evidence'
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def load(p):return json.loads(Path(p).read_text())
r=load(E/'checks.json');a=load(E/'output_audit.json');run=load(E/'local_run.json');arun=load(E/'audit_run.json')
assert r['status']==a['status']=='PASS' and run['returncode']==arun['returncode']==0
assert r['code_sha256']==a['check_code_sha256']==sha(B/'research/trial_axis_log/code/check_log.py')
assert r['proof_sha256']==a['proof_sha256']==sha(B/'research/trial_axis_log/PROOF.md')
assert a['checks_sha256']==sha(E/'checks.json') and a['code_sha256']==sha(B/'research/trial_axis_log/code/audit_output.py') and a['exact_modes_sha256']==sha(E/'exact_modes.json')
assert r['input_sha256']==sha(B/'data_exact/modal_v2.json')=='57f67a53c1ee5c8fd5ede8480428f1a5584123ac4e54b6d3530d091ea2a67ca6'
assert r['original_npz_sha256']==sha(B/'research/modal_exactification/evidence/trial_v2_h0.008.npz')=='a069d85d102e17340778042f85c003705716ba799c0f68873d10c1c582ea4874'
times=[run['start_utc'],r['utc'],run['end_utc'],arun['start_utc'],a['utc'],arun['end_utc']];assert all(datetime.fromisoformat(x)<datetime.fromisoformat(y) for x,y in zip(times,times[1:]))
paths={Path(__file__),B/'research/trial_axis_log/PROOF.md',B/'research/trial_axis_log/code/check_log.py',B/'research/trial_axis_log/code/audit_output.py',B/'data_exact/modal_v2.json',B/'research/modal_exactification/evidence/trial_v2_h0.008.npz'}|{E/f for f in ['checks.json','exact_modes.json','output_audit.json','local_run.json','audit_run.json','proof_first.json','review_repairs.json','lead_pinf_B3.md','first_check_failure.log','first_check_failure_run.json','check_repair.json']};reviews={}
for tag in ['trial_axis_log_proof','trial_axis_log_closure']:
 m=load(B/f'notes/reviews/{tag}_metadata.json');resp=load(B/f'notes/reviews/{tag}_response.json');req=(B/f'notes/reviews/{tag}_request.txt').read_text();text=(B/f'notes/reviews/{tag}_response.md').read_text()
 assert m['actual_response_model']==resp['model']=='claude-opus-5-5' and m['stop_reason']==resp['stop_reason']=='end_turn'
 assert sha(B/f'notes/reviews/{tag}_request.txt')==m['input_sha256'] and text=='\n\n'.join(x['text'] for x in resp['content'] if x['type']=='text')+'\n'
 if tag.endswith('closure'):
  assert 'ACCEPT_STATED_SCOPE' in text and datetime.fromisoformat(arun['end_utc'])<datetime.fromisoformat(m['start_utc'])
  for f in m['files']:assert req.split('\n\nFILE '+f+'\n',1)[1].split('\n\nFILE ',1)[0]==(B/f).read_text()
 reviews[tag]={'model':m['actual_response_model'],'stop_reason':m['stop_reason'],'end_utc':m['end_utc'],'status':'ACCEPT_STATED_SCOPE' if tag.endswith('closure') else 'SUPERSEDED: two reviewer errors explicitly rejected; see review_repairs.json'}
 for suf in ['metadata.json','request.txt','response.json','response.md']:paths.add(B/f'notes/reviews/{tag}_{suf}')
o={'utc':datetime.now(timezone.utc).isoformat(),'status':'CONFIRMED_TRIAL_LOG_COEFFICIENTS_AND_REFUTED_ESTIMATOR_PREMISE','confirmed':['Exact degree-five angular resonance gives lambda=3H7 at x5logx in w','Q_f has nonzero x4logx coefficient -30H7/A','Q_total including cubic defect has nonzero x6logx coefficient (6-p)(15-p)lambda*b2/(4A)','Generalized logarithmic finite part of HG3 has zero local constant'],'refuted':['Polynomial-only Q=q2x2+q4x4+q6x6+O(x8) for either integrand of this exact modal trial','Use of the plain B1 cutoff estimate for this trial without logarithmic subtractions'],'open':['Generalized numerical B3[f] and its cutoff error','Stability in a density topology and any nontrivial exclusion ball','PDE existence, exclusion and every decisive endpoint'],'strict_brackets':{k:v['common_strict_bracket'] for k,v in r['coefficients'].items()},'checks':r['checks'],'methods':'Exact independent hex/binary NPY parsing; trigonometric versus complex Laurent angular differentiation; symbolic differential identities; Arb512 versus iv180 different exponential formulas; fresh Arb768 saved-output audit.','reviews':reviews,'review_repairs':load(E/'review_repairs.json'),'review_provenance_limit':'Opus performed text review and did not execute code or rehash. This finalizer binds the actual current review bundle, sources, exact inputs, outputs and run times. Shared exact inputs do not constitute independent data acquisition.','runtime':r['runtime'],'files':{str(p.relative_to(B)):sha(p) for p in sorted(paths)}}
t=E/'verdict.json.tmp';t.write_text(json.dumps(o,indent=2)+'\n');os.replace(t,E/'verdict.json')
for p,h in o['files'].items():assert sha(B/p)==h
print(json.dumps({'utc':o['utc'],'status':o['status'],'sha256':sha(E/'verdict.json'),'pins':len(paths)}))
