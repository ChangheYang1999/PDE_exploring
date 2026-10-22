"""Bind source-matching proofs, exact checks, higher precision audit and actual Opus reviews."""
import json,hashlib,sys,os
from pathlib import Path
from datetime import datetime,timezone
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];E=B/'research/source_matching/evidence'
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def load(p):return json.loads(Path(p).read_text())
r=load(E/'checks.json');a=load(E/'output_audit.json');run=load(E/'local_run.json');arun=load(E/'audit_run.json')
assert r['status']==a['status']=='PASS' and run['returncode']==arun['returncode']==0
assert r['code_sha256']==a['check_code_sha256']==sha(B/'research/source_matching/code/check_source.py')=='54c678358f6c13dc412694b03744c49181651aefb8bf95c206dce15a4f3ffe3c'
assert r['proof_sha256']==a['proof_sha256']==sha(B/'research/source_matching/PROOF.md')=='1c3fccd61e2acdff0551b63f7e40217e209475e51758221f38a353d9215d45ee'
assert a['checks_sha256']==sha(E/'checks.json') and a['code_sha256']==sha(B/'research/source_matching/code/audit_output.py')=='c9acaf817ab31bcd074239b4921cdb75026a760ce0142f2ea0ee59d26fef6d30'
times=[run['start_utc'],r['utc'],run['end_utc'],arun['start_utc'],a['utc'],arun['end_utc']];assert all(datetime.fromisoformat(x)<datetime.fromisoformat(y) for x,y in zip(times,times[1:]))
paths={Path(__file__),B/'research/source_matching/PROOF.md',B/'research/source_matching/code/check_source.py',B/'research/source_matching/code/audit_output.py'}|{E/f for f in ['checks.json','output_audit.json','local_run.json','audit_run.json','proof_first.json','review_repairs.json','lead_prow1_question.md','lead_prow1_answer.md']};reviews={}
for tag in ['source_matching_proof','source_matching_closure']:
 m=load(B/f'notes/reviews/{tag}_metadata.json');resp=load(B/f'notes/reviews/{tag}_response.json');req=(B/f'notes/reviews/{tag}_request.txt').read_text();text=(B/f'notes/reviews/{tag}_response.md').read_text()
 assert m['actual_response_model']==resp['model']=='claude-opus-5-5' and m['stop_reason']==resp['stop_reason']=='end_turn'
 assert sha(B/f'notes/reviews/{tag}_request.txt')==m['input_sha256'] and text=='\n\n'.join(x['text'] for x in resp['content'] if x['type']=='text')+'\n'
 if tag.endswith('closure'):
  assert 'ACCEPT_STATED_SCOPE' in text and datetime.fromisoformat(arun['end_utc'])<datetime.fromisoformat(m['start_utc'])
  for f in m['files']:assert req.split('\n\nFILE '+f+'\n',1)[1].split('\n\nFILE ',1)[0]==(B/f).read_text()
 reviews[tag]={'model':m['actual_response_model'],'stop_reason':m['stop_reason'],'end_utc':m['end_utc']}
 for suf in ['metadata.json','request.txt','response.json','response.md']:paths.add(B/f'notes/reviews/{tag}_{suf}')
o={'utc':datetime.now(timezone.utc).isoformat(),'status':'CONFIRMED_CONDITIONAL_SOURCE_AND_MATCHING_RESULTS','confirmed':['Exact maximal distributional frozen inverse for3<sigma<2373/680 over the stated rational parameter box','Inverse upper500/1687 at31/10 and200/489 at13/4','P-row is implied by full equation under local C1 and explicit nonlocal hypotheses','Dini or power-controlled incoming-axis representation and origin matching','Scaling removes its own direction only at exact solutions with K in domain'],'refuted':['Necessary coupled inverse pole deduced by division by mu_P-1','Origin matching follows from R/x2 tending to0 alone','P-row redundancy by itself proves global surjectivity'],'open':['Variable-coefficient disc and global domain','Nonlocal tail and jet/remainder bounds','Global onto and kernel dimension','Quantitative trial normalization','All PDE existence/exclusion endpoints'],'frozen_bounds':{x['sigma']:x['inverse_upper_exact'] for x in r['margins']},'derivative_exports':{x['sigma']:x['public_strict_upper'] for x in r['derivative_exports']},'checks':{'corners':16,'rate_inequalities':r['rate_inequalities'],'symbolic_identities':r['symbolic_identities']},'methods':'Independent maximal-domain Fourier proof; exact rational extrema and symbolic identities; Arb512 versus iv180 with exact Machin-series pi; fresh Arb1536 audit.','reviews':reviews,'review_corrections':['Initial sigma>1/2 suggestion requires positive kappa; proof includes the upper window','Closure explanatory product2*5*5*5*8 is a reviewer arithmetic typo. The actual code and correct count are2*8*5*5=400. No numerical conclusion uses the typo.'],'review_provenance_limit':'Text reviewer did not execute code or recompute hashes; this local finalizer binds the actual current bundle and outputs.','runtime':r['runtime'],'files':{str(p.relative_to(B)):sha(p) for p in sorted(paths)}}
t=E/'verdict.json.tmp';t.write_text(json.dumps(o,indent=2)+'\n');os.replace(t,E/'verdict.json')
for p,h in o['files'].items():assert sha(B/p)==h
print(json.dumps({'utc':o['utc'],'status':o['status'],'sha256':sha(E/'verdict.json'),'pins':len(paths)}))
