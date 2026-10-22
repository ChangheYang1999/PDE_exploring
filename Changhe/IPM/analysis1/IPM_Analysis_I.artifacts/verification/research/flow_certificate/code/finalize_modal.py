"""Finalizes only the finite middle modal maps, not the flow certificate."""
import sys,json,hashlib,os
from pathlib import Path
from datetime import datetime,timezone
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];E=B/'research/flow_certificate/evidence';sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest();load=lambda p:json.loads(Path(p).read_text())
r=load(E/'modal_integer_full.json');run=load(E/'modal_integer_full_run.json');s=load(E/'modal_review_summary.json')
assert run['returncode']==0 and run['middle_resumed'] and r['status']=='PASS_EXACT_INTEGER_INPUT_BOX_IMAGES' and r['first']==0 and r['stop_exclusive']==r['cells']==7809 and r['checks']==7809*6264 and r['alpha_exact']=='0'
d=hashlib.sha256()
for ci in range(7809):d.update(f'{ci}:{(ci+1)*6264}\n'.encode())
assert r['coverage_digest']==s['coverage_digest_recomputed']==d.hexdigest() and s['full_run']==r and s['wrapper']==run
for f,h in r['files'].items():assert sha(f)==h
src=(E/'source/cert_resid.py').read_text();flow=(E/'source/cert_flow.py').read_text()
assert 'self.T = MR(d["T_mid"], d["T_rad"])' in src
assert '[(0.0, C.T[ci])]' in flow
assert 'return f_terms, R_terms' in src
paths={Path(__file__),B/'research/flow_certificate/PROOF.md',B/'research/flow_certificate/code/audit_modal_integer.py',B/'research/flow_certificate/code/check_modal_maps.py',E/'source/cert_resid.py',E/'source/cert_flow.py',E/'source/midrad.py'}|{E/n for n in ['modal_integer_full.json','modal_integer_full_run.json','modal_integer_full.log','modal_review_summary.json','modal_benchmark.json','modal_integer_benchmark.json','modal_stress.json']};reviews={}
for tag in ['flow_modal_exact_review','flow_modal_exact_closure']:
 m=load(B/f'notes/reviews/{tag}_metadata.json');resp=load(B/f'notes/reviews/{tag}_response.json');req=(B/f'notes/reviews/{tag}_request.txt').read_text();text=(B/f'notes/reviews/{tag}_response.md').read_text()
 assert m['actual_response_model']==resp['model']=='claude-opus-5-5' and m['stop_reason']==resp['stop_reason']=='end_turn'
 assert sha(B/f'notes/reviews/{tag}_request.txt')==m['input_sha256'] and text=='\n\n'.join(x['text'] for x in resp['content'] if x['type']=='text')+'\n'
 if tag.endswith('closure'):
  assert 'ACCEPT_FINITE_MODAL_RESULT' in text and datetime.fromisoformat(run['end_utc'])<datetime.fromisoformat(m['start_utc'])
  for f in m['files']:assert req.split('\n\nFILE '+f+'\n',1)[1].split('\n\nFILE ',1)[0]==(B/f).read_text()
 reviews[tag]={'actual_model':m['actual_response_model'],'stop_reason':m['stop_reason'],'end_utc':m['end_utc']}
 for suf in ['metadata.json','request.txt','response.json','response.md']:paths.add(B/f'notes/reviews/{tag}_{suf}')
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'CONFIRMED_FINITE_MIDDLE_MODAL_MAPS_ONLY','cells':7809,'exact_checks':48915576,'data_pin':{f:h for f,h in r['files'].items() if f.endswith('.npz')},'source_tuple':'R_terms stores(alpha,R,dR); f_terms stores(alpha,F); F rows transpose to degree-major. C.T is MR(T_mid,T_rad) with no transformation; middle cell_iter supplies exact0.','method':r['method'],'scope':'Only actual input box images for R,dR,F produced in the completed frozen-source audit. No historical flow_middle output provenance, field arithmetic, other regions, tail or full-flow acceptance.','rounding_scope':'FE_TONEAREST checked after the run, not during; no promise that a later changed environment returns identical outputs.','review_limit':'Actual text reviews checked mathematics, not hashes; this finalizer binds files and completed runs.','reviews':reviews,'files':{str(p.relative_to(B)):sha(p) for p in sorted(paths)}}
(E/'modal_verdict.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'utc':out['utc'],'status':out['status'],'pins':len(paths),'sha256':sha(E/'modal_verdict.json')}))
