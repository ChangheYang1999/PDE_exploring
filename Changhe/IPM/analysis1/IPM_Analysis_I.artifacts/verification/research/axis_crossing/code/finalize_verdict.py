"""Bind the audited local crossing, its inherited data, and both model reviews."""
import json,hashlib,sys,os
from pathlib import Path
from datetime import datetime,timezone
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];E=B/'research/axis_crossing/evidence'
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
load=lambda p:json.loads(Path(p).read_text())
r=load(E/'checks.json');a=load(E/'output_audit.json');run=load(E/'local_run.json');arun=load(E/'audit_run.json');s=load(E/'review_summary.json')
assert r['status']==a['status']=='PASS' and run['returncode']==arun['returncode']==0
assert r['code_sha256']==a['check_code_sha256']==sha(B/'research/axis_crossing/code/check_crossing.py')=='47e6b496a7052ca2a4dd9d96cb0d373defb4391d8d47f83c8c29b421f3856e29'
assert r['proof_sha256']==a['proof_sha256']==sha(B/'research/axis_crossing/PROOF.md')=='318bdc43a60c623a6c28f308a805cecb73f3cb6914b25042a542895be976593c'
assert a['checks_sha256']==s['checks_sha256']==sha(E/'checks.json') and s['audit_sha256']==sha(E/'output_audit.json')
assert a['code_sha256']==sha(B/'research/axis_crossing/code/audit_output.py')=='6a75339ee39de69e797eecc4f5a90bb1d600e97316a4ad7d58823b8567e2f665'
times=[run['start_utc'],r['utc'],run['end_utc'],arun['start_utc'],a['utc'],arun['end_utc']]
assert all(datetime.fromisoformat(x)<datetime.fromisoformat(y) for x,y in zip(times,times[1:]))
assert a['all_subcells']==64 and a['fresh_containments']==20 and a['endpoint_arb_overlaps']==2 and a['original_knot_span']==673
assert a['whole_cell_bounds_strict']==['10.1494','10.1525']
paths={Path(__file__),B/'research/axis_crossing/PROOF.md',B/'research/axis_crossing/code/check_crossing.py',B/'research/axis_crossing/code/audit_output.py'}|{p for p in E.iterdir() if p.is_file() and p.name not in ['verdict.json','verdict.json.tmp','finalize.log']}
sample=B/'research/residual_samples/evidence/sample_result.json';provpath=B/'research/residual_samples/evidence/review_summary.json';prov=load(provpath);sr=load(sample)
assert r['sample_sha256']==prov['sample_result_sha256']==sha(sample)=='0608fe74dbeef4eaf21e26aedffe61453f558e25e0e902dd72fda6b3084f630c'
assert prov['status']=='PASS' and prov['coefficients_audited']==sum(len(z['residual_coefficients']) for z in sr['samples'])==6786
assert len(sr['samples'])==13 and all(len(z['residual_coefficients'])==522 for z in sr['samples'])
source=B/'research/residual_samples/code/certify_samples.py';assert sr['source_sha256']==sha(source)=='d393d06a70d8209f3eca0bbb67ca309d45153ff9ca23abd4a54a961076c92257'
paths|={sample,provpath,source}
for key,(rel,hsh) in prov['dependencies'].items():assert sha(B/rel)==hsh;paths.add(B/rel)
sp=B/'research/modal_source/evidence/source_result.json';sa=B/'research/modal_source/evidence/output_audit.json'
assert load(sa)['verdict']=='PASS' and load(sa)['source_result_sha256']==r['source_result_sha256']==sha(sp)=='51f283cd4ea7145f633e5449236cdd0bc2879b9ccf922d9fbadb6a609afa4691';paths|={sp,sa}
reviews={}
for tag in ['axis_crossing_proof','axis_crossing_closure']:
 m=load(B/f'notes/reviews/{tag}_metadata.json');resp=load(B/f'notes/reviews/{tag}_response.json');req=(B/f'notes/reviews/{tag}_request.txt').read_text();text=(B/f'notes/reviews/{tag}_response.md').read_text()
 assert m['actual_response_model']==resp['model']=='claude-opus-5-5' and m['stop_reason']==resp['stop_reason']=='end_turn'
 assert sha(B/f'notes/reviews/{tag}_request.txt')==m['input_sha256'] and text=='\n\n'.join(x['text'] for x in resp['content'] if x['type']=='text')+'\n'
 if tag.endswith('closure'):
  assert 'ACCEPT_STATED_SCOPE' in text and 'They were wrong' in text and 'was wrong' in text and datetime.fromisoformat(arun['end_utc'])<datetime.fromisoformat(m['start_utc'])
  for f in m['files']:assert req.split('\n\nFILE '+f+'\n',1)[1].split('\n\nFILE ',1)[0]==(B/f).read_text()
 reviews[tag]={'model':m['actual_response_model'],'stop_reason':m['stop_reason'],'end_utc':m['end_utc']}
 for suf in ['metadata.json','request.txt','response.json','response.md']:paths.add(B/f'notes/reviews/{tag}_{suf}')
o={'utc':datetime.now(timezone.utc).isoformat(),'status':'CONFIRMED_LOCAL_AXIS_CROSSING_EXACT_CELL4102','cell':4102,'whole_cell_bounds_strict':['10.1494','10.1525'],'t_endpoints_exact':r['t_endpoints_exact'],'methods':'Arb512 finite polynomial ODE particular solution plus C2 subcell bounds; independent mpmath.iv180 Q16 density ODE remainder. Fresh Arb1536 integral-moment audit, exact rational coverage.','confirmed':['All64 exact subcells have strictly positive wprime','Opposite strict signs of x*w at exact endpoints','Exactly one zero on this exact cell','Prior independently isolated root lies strictly inside','The numerics printed r_hi exceeds exp(b) by a number in (3.92403e-6,3.92404e-6)'],'refuted':['Using the larger printed upper radius as though it were the exact certified cell endpoint'],'open':['Remaining axis cells and infinite tails','Full global flow REV2 certificate','Full inverse, nonlinear bound, existence or exclusion'],'data_dependency':'The two methods share independently audited 261 I/J balls at cell center. They are not two integrations from infinity.','provenance_clarification':'6786 is 13 samples times522 residual Fourier coefficients, not the number of density polynomial coefficients. Cell4102 has262 times8 density coefficients, produced by the pinned exact Cox source and exact modal projection. That construction and moment integrations were audited in residual_samples; the hash chain is verified here.','review_corrections':['First reviewer erroneous ds/s and shifted exponent definitions are withdrawn by closure; correct displayed radial moments are used','First reviewer m-cancels remark withdrawn; factor2n is retained','Closure incidental |ell|<=518h is not adopted: max moment |lambda| is526 and code uses each exact lambda; there is no such upper bound assumed by the proof','20 fresh containments mean18 center containments plus2 iv endpoint containments; the two Arb endpoint enclosures overlap and are separately strict-sign certified'],'reviews':reviews,'review_limit':'Text reviews did not execute code. Exact reviewed files, executed outputs, and inherited input provenance are pinned here.','files':{str(p.relative_to(B)):sha(p) for p in sorted(paths)}}
t=E/'verdict.json.tmp';t.write_text(json.dumps(o,indent=2)+'\n');os.replace(t,E/'verdict.json')
for p,hsh in o['files'].items():assert sha(B/p)==hsh
print(json.dumps({'utc':o['utc'],'status':o['status'],'sha256':sha(E/'verdict.json'),'pins':len(paths)}))
