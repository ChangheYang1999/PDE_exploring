"""Accept only the completed primary middle calculation and assembly."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import json,hashlib,sys,os
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];E=B/'research/middle_residual/evidence'
def sha(p):
 h=hashlib.sha256()
 with Path(p).open('rb') as f:
  for block in iter(lambda:f.read(1<<20),b''):h.update(block)
 return h.hexdigest()
def load(p):return json.loads(Path(p).read_text())
def main():
 c=load(E/'primary_completion_checks.json');run=load(E/'completion_checks_run.json');a=load(E/'full_q16_output_audit.json');s=load(E/'primary_completion_summary.json')
 assert c['status']=='PASS_PRIMARY_COMPLETION_LINKS_AND_PUBLIC_BOUNDS' and run['returncode']==0
 assert c['source_sha256']==sha(B/'research/middle_residual/code/check_completion.py')
 for p,h in c['files'].items():assert sha(B/p)==h
 assert c['moment_phi_526_span_gate_minimum_bits']==295 and c['primary_full_footer_confirmed'] and c['setup_body_byte_identical']
 assert a['status']=='PASS' and a['cells_audited']==7809
 for row in c['strict_exact_comparisons']:
  value=F(a['maxima'][row['quantity']]['upper']);bound=F(row['strict_public_upper_exact']);assert value==F(row['audited_upper_exact'])<bound and bound-value==F(row['strict_gap_exact'])
 assert F(a['L2_squared_upper_exact'])<F(c['L2_strict_upper_exact'])**2 and F(a['L2_upper_exact'])<F(c['L2_strict_upper_exact'])
 paths={B/p for p in c['files']}|{Path(__file__),E/'primary_completion_checks.json',E/'completion_checks_run.json',E/'completion_checks.log'};reviews={}
 for tag in ['middle_primary_assembly','middle_primary_closure']:
  meta=load(B/f'notes/reviews/{tag}_metadata.json');resp=load(B/f'notes/reviews/{tag}_response.json');req=(B/f'notes/reviews/{tag}_request.txt').read_text();text=(B/f'notes/reviews/{tag}_response.md').read_text()
  assert meta['actual_response_model']==resp['model']=='claude-opus-5-5' and meta['stop_reason']==resp['stop_reason']=='end_turn' and 'ACCEPT_PRIMARY' in text
  assert sha(B/f'notes/reviews/{tag}_request.txt')==meta['input_sha256']
  assert text=='\n\n'.join(x['text'] for x in resp['content'] if x['type']=='text')+'\n'
  if tag.endswith('closure'):
   assert datetime.fromisoformat(run['utc_resume'])<datetime.fromisoformat(meta['start_utc'])
   for p in meta['files']:assert req.split('\n\nFILE '+p+'\n',1)[1].split('\n\nFILE ',1)[0]==(B/p).read_text()
  reviews[tag]={'actual_model':meta['actual_response_model'],'stop_reason':meta['stop_reason'],'end_utc':meta['end_utc'],'verdict':'ACCEPT_PRIMARY'}
  for suffix in ['metadata.json','request.txt','response.json','response.md']:paths.add(B/f'notes/reviews/{tag}_{suffix}')
 result={'utc':datetime.now(timezone.utc).isoformat(),'status':'CONFIRMED_PRIMARY_ASSEMBLY','cells':7809,'method':'All cells Q16 with exact dyadic ball arithmetic and Arb384 analytic primitives; full source/footer audit, Bernstein and analytic tails, separate Arb768 saved-output audit, exact public/coverage/source link checks. Full independent iv160 coefficient reconstruction remains running.','public_strict_bounds':s['public_strict_bounds'],'L2_strict_upper_exact':c['L2_strict_upper_exact'],'L2_definition':s.get('L2_definition','sqrt integral of |epsilon/m|^2 dX/[1+(r/L)^2] over the middle annulus'),'maxima_cell':4125,'reviews':reviews,'review_corrections':'Initial reviewer W and W/m decimals were wrong and explicitly withdrawn in follow-up. All published comparisons are checked using exact rational endpoints, including the square of the L2 bound.','files':{str(p.relative_to(B)):sha(p) for p in sorted(paths)},'scope':'Primary middle-region residual bounds for the exact modal candidate, not X3 distance, target forcing norm, coupled inverse, existence/exclusion or PDE endpoint. Full second coefficient pass OPEN.'}
 temp=E/'primary_acceptance.json.tmp';temp.write_text(json.dumps(result,indent=2)+'\n');os.replace(temp,E/'primary_acceptance.json')
 for p,h in result['files'].items():assert sha(B/p)==h
 print(json.dumps({'utc':result['utc'],'status':result['status'],'sha256':sha(E/'primary_acceptance.json'),'pins':len(paths)}))
if __name__=='__main__':main()
