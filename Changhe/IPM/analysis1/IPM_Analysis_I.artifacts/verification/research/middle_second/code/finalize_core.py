"""Freeze the reviewed second-method sources and contracts, not the full result."""
import os
os.environ['PYTHONDONTWRITEBYTECODE']='1'
import sys,json,hashlib
from pathlib import Path
from datetime import datetime,timezone
BASE=Path(__file__).resolve().parents[3];E=BASE/'research/middle_second/evidence'
assert not sys.flags.optimize

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def load(p):return json.loads(Path(p).read_text())
def reviewed(tag,paths):
 meta=load(BASE/f'notes/reviews/{tag}_metadata.json')
 assert meta['actual_response_model']=='claude-opus-5-5' and meta['stop_reason']=='end_turn'
 request=(BASE/f'notes/reviews/{tag}_request.txt').read_text();assert hashlib.sha256(request.encode()).hexdigest()==meta['input_sha256']
 for name in paths:
  marker='\n\nFILE '+name+'\n';assert request.count(marker)==1
  text=request.split(marker,1)[1].split('\n\nFILE ',1)[0]
  assert text==(BASE/name).read_text(),name
 assert (BASE/f'notes/reviews/{tag}_response.md').read_text().strip()
 return meta

def main():
 tags=['middle_second_source','middle_second_strengthened','middle_second_driver_review','middle_second_driver_closure']
 metas={tag:reviewed(tag,[]) for tag in tags}
 reviewed(tags[2],['research/middle_second/PROOF.md','research/middle_second/code/cell_iv.py','research/middle_second/code/check_cells.py'])
 reviewed(tags[3],['research/middle_second/code/run_full.py','research/middle_second/code/audit_full.py','research/middle_second/code/check_driver.py','research/middle_second/evidence/driver_contracts.json','research/middle_second/evidence/smoke_strengthened_summary.json'])
 paths={Path(__file__),BASE/'research/middle_second/PROOF.md'}
 for name in ['cell_iv','check_cells','run_full','audit_full','check_driver','check_algebra','check_contracts','summarize_smoke','check_freeze']:paths.add(BASE/f'research/middle_second/code/{name}.py')
 for name in ['contracts','algebra_contracts','driver_contracts','smoke_strengthened','smoke_strengthened_summary','prefreeze_keys']:
  path=E/(name+'.json');paths.add(path);obj=load(path)
  assert obj['status'].startswith('PASS')
  if 'pins' in obj:
   for rel,h in obj['pins'].items():assert sha(BASE/rel)==h;paths.add(BASE/rel)
  if 'cell_iv_sha256' in obj:assert obj['cell_iv_sha256']==sha(BASE/'research/middle_second/code/cell_iv.py')
 summary=load(E/'smoke_strengthened_summary.json');assert summary['full_output_sha256']==sha(E/'smoke_strengthened.json')
 for name,item in summary['contracts'].items():assert item['sha256']==sha(E/(name+'.json'))
 assert [r['cell'] for r in summary['cells']]==[0,3925,5000]
 for row in summary['cells']:
  assert row['primary_scalar_equality_checks']==22 and row['coefficient_overlap_checks']==8874 and row['center_moment_overlap_checks']==522 and row['shifted_density_overlap_checks']==2096
  pc=row['point_comparison'];expected=522 if row['cell'] in [0,3925] else 0
  assert pc['independent_point_iv_coefficient_overlaps']==pc['independent_point_coefficient_overlaps']==expected
 keys=load(E/'prefreeze_keys.json');assert keys['missing']==[] and set(keys['required'])<=set(keys['provided'])
 for tag in tags:
  for suffix in ['request.txt','response.json','response.md','metadata.json']:paths.add(BASE/f'notes/reviews/{tag}_{suffix}')
 now=datetime.now(timezone.utc).isoformat()
 result={'utc':now,'status':'CONFIRMED_METHOD_AND_CONTRACTS_ONLY','complete_secondary_run':'OPEN','primary_prepare_execution':'OPEN','middle_region_certificate':'OPEN','method':'Independent density moment ODE and complete-antiderivative iv160 implementation, exact integer convolution and complete product/ODE remainders; source review, exact contracts and three full-cell comparisons. Common canonical archive remains an accepted shared dependency, not validated by agreement.','reviews':{tag:{'model':m['actual_response_model'],'end_utc':m['end_utc']} for tag,m in metas.items()},'prefreeze_required_keys':len(keys['required']),'checks':{name:load(E/(name+'.json')).get('checks',{}) for name in ['contracts','algebra_contracts','driver_contracts']},'selected_cells':[0,3925,5000],'files':{str(p.relative_to(BASE)):sha(p) for p in sorted(paths)},'scope':'This freezes sources for prepare and exhaustive execution. It supplies no unsampled-cell, global residual, derivative norm, inverse, fixed-point, existence, exclusion or decisive endpoint.'}
 tmp=E/'core_acceptance.json.tmp';tmp.write_text(json.dumps(result,indent=2)+'\n');os.replace(tmp,E/'core_acceptance.json')
 for rel,h in result['files'].items():assert sha(BASE/rel)==h
 print(json.dumps({'utc':now,'status':result['status'],'file_pins':len(result['files']),'sha256':sha(E/'core_acceptance.json')}))
if __name__=='__main__':main()
