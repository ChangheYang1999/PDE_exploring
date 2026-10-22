"""Link the completed corner proof, two methods, audit repair and Opus closure."""
import json,hashlib,sys,os
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];E=B/'research/corner_coupling/evidence'
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def load(p):return json.loads(Path(p).read_text())
def main():
 pins=load(E/'finalization_pins.json')
 for p,h in pins.items():assert sha(B/p)==h
 r=load(E/'checks.json');a=load(E/'algebra.json');o=load(E/'output_audit.json');run=load(E/'final_run.json');repair=load(E/'audit_repair_run.json')
 assert r['status']=='PASS_TWO_METHOD_CONSTANTS' and a['status']=='PASS_EXACT_ALGEBRA' and o['status']=='PASS'
 for item,src in [(r,'check_constants.py'),(a,'check_algebra.py'),(o,'audit_output.py')]:
  assert item['source_sha256']==sha(B/'research/corner_coupling/code'/src) and item['proof_sha256']==sha(B/'research/corner_coupling/PROOF.md')
 assert r['dependency_verdict_sha256']==sha(B/'research/double_remainder/evidence/verdict.json')
 dep=load(B/'research/double_remainder/evidence/verdict.json')
 for p,h in dep['files'].items():assert sha(B/p)==h
 assert o['checks_sha256']==sha(E/'checks.json') and o['algebra_sha256']==sha(E/'algebra.json')
 assert r['checks']=={'rows':2,'shifted_rows':46,'overlaps':618,'beta_containments':2,'endpoint_containments':10,'nonfinite_rejections':3}
 assert o['checks']=={'block_endpoint_containments':828,'shifted_endpoint_containments':368,'final_endpoint_containments':40,'beta_integral_containments':2,'public_comparisons':20}
 assert [x['returncode'] for x in run['runs']]==[0,0,1] and repair['returncode']==0
 assert [x['command'] for x in run['runs']]==[['python3','research/corner_coupling/code/'+s] for s in ['check_constants.py','check_algebra.py','audit_output.py']]
 stamps=[run['start_utc'],r['utc'],run['runs'][0]['end_utc'],a['utc'],run['runs'][1]['end_utc'],run['end_utc'],repair['start_utc'],o['utc'],repair['end_utc']]
 assert all(datetime.fromisoformat(x)<datetime.fromisoformat(y) for x,y in zip(stamps,stamps[1:]))
 for row,public in zip(r['rows'],o['public_bounds']):
  assert all(row[k]==public[k] for k in ['a_exact','b_exact','gamma_exact'])
  for name,bound in public['strict_bounds'].items():
   for method in ['arb','iv']:assert F(row['constants'][name][method]['upper_exact'])<F(bound)
 paths={B/p for p in pins}|{Path(__file__),E/'checks.json',E/'algebra.json',E/'output_audit.json',E/'final_run.json',E/'audit_repair_run.json',E/'review_repairs.json',E/'proof_first.json',E/'finalization_pins.json',E/'review_summary.json'}
 reviews={}
 for tag in ['corner_coupling_proof','corner_coupling_closure']:
  meta=load(B/f'notes/reviews/{tag}_metadata.json');resp=load(B/f'notes/reviews/{tag}_response.json');req=(B/f'notes/reviews/{tag}_request.txt').read_text();text=(B/f'notes/reviews/{tag}_response.md').read_text()
  assert meta['actual_response_model']==resp['model']=='claude-opus-5-5' and meta['stop_reason']==resp['stop_reason']=='end_turn'
  assert sha(B/f'notes/reviews/{tag}_request.txt')==meta['input_sha256']
  assert text=='\n\n'.join(x['text'] for x in resp['content'] if x['type']=='text')+'\n'
  if tag.endswith('closure'):
   assert 'ACCEPT_STATED_SCOPE' in text and datetime.fromisoformat(repair['end_utc'])<datetime.fromisoformat(meta['start_utc'])
   for p in meta['files']:assert req.split('\n\nFILE '+p+'\n',1)[1].split('\n\nFILE ',1)[0]==(B/p).read_text()
  reviews[tag]={'actual_model':meta['actual_response_model'],'stop_reason':meta['stop_reason'],'end_utc':meta['end_utc']}
  for s in ['metadata.json','request.txt','response.json','response.md']:paths.add(B/f'notes/reviews/{tag}_{s}')
 result={'utc':datetime.now(timezone.utc).isoformat(),'status':'CONFIRMED','claims':['Local weighted corner remainder bound for a C8 factor, unit-box source','Local weighted corner remainder bound for C8 factor and arbitrary composite-weight source','All stated finite constants and exact public ceilings at two rational weight pairs'], 'methods':'Independent Taylor-product and kernel derivation; Arb512 finite vectors and special functions versus iv180 exact r+s/pi forms, 128-term geometric sums with rigorous tail, grouped constants and positive4096-cell Beta integral; exact polynomial/rational algebra. Arb768 saved-scalar audit is not a third independent method.','checks':r['checks'],'algebra_checks':a['checks'],'output_checks':o['checks'],'public_bounds':o['public_bounds'],'runtime':r['runtime'],'reviews':reviews,'review_corrections':['Near cutoff agreement with the bounded extension was made explicit.','The c/3 strain sign and exact coefficient were independently checked.','The auditor first failed on an exact integer iv singleton versus an unsimplified Arb pi/pi ball. Repaired comparison uses an exactly equal r+s/pi form and a separate overlap with the unreduced expression; no saved scalar was loosened.','Reviewer shorthand for C_str squared omitted pi^-2 and shorthand for M_d squared repeated the x factor. The proof and code use the correct pi^-2 and distinct x,y factors.','No optimality of the C8 requirement is asserted.'],'scope':'Conditional local zeroth-order remainder estimate only. Current modal trial factor is not C2 and cannot be inserted. No smallness, inverse, conormal derivative, global completion of canonical velocity, nonlinear closure, or PDE endpoint.','files':{str(p.relative_to(B)):sha(p) for p in sorted(paths)}}
 temp=E/'verdict.json.tmp';temp.write_text(json.dumps(result,indent=2)+'\n');os.replace(temp,E/'verdict.json')
 for p,h in result['files'].items():assert sha(B/p)==h
 print(json.dumps({'utc':result['utc'],'status':result['status'],'sha256':sha(E/'verdict.json'),'pins':len(paths)}))
if __name__=='__main__':main()
