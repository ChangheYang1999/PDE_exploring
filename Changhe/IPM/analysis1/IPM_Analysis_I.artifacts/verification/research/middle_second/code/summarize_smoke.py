"""Hash-checked compact view of the full selected-cell evidence."""
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import hashlib,json,os
BASE=Path(__file__).resolve().parents[3];E=BASE/'research/middle_second/evidence'
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
p=E/'smoke_strengthened.json';data=json.loads(p.read_text())
for path,h in data['pins'].items():assert sha(BASE/path)==h
contracts={}
for name in ['contracts','algebra_contracts','driver_contracts']:
 q=E/(name+'.json');c=json.loads(q.read_text())
 if 'cell_iv_sha256' in c:assert c['cell_iv_sha256']==sha(BASE/'research/middle_second/code/cell_iv.py')
 if 'pins' in c:
  for path,h in c['pins'].items():assert sha(BASE/path)==h
 contracts[name]={'sha256':sha(q),'status':c['status'],'checks':c.get('checks',{k:v for k,v in c.items() if 'checks' in k})}
summary={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_STRENGTHENED_SELECTED_CELLS_ONLY','source_sha256':sha(Path(__file__)),'full_output_sha256':sha(p),'pins_checked':len(data['pins']),'contracts':contracts,'cells':[],'scope':data['scope']}
for r in data['cells']:
 ir=r['independent_iv_integer'];width=F(ir['max_center_moment_interval_width_exact']);assert width>=0
 summary['cells'].append({'cell':r['cell'],'primary_scalar_equality_checks':r['primary_scalar_equality_checks'],'coefficient_overlap_checks':ir['coefficient_overlap_checks'],'center_moment_overlap_checks':ir['center_moment_overlap_checks'],'shifted_density_overlap_checks':ir['shifted_density_overlap_checks'],'max_center_moment_interval_width_exact':str(width),'point_comparison':r['independent_point_comparison'],'Wm_arb_exact':r['arb']['W_over_m_upper_exact'],'Wm_iv':ir['W_over_m'],'iv_seconds':ir['seconds']})
q=E/'smoke_strengthened_summary.json';tmp=q.with_suffix('.json.tmp');tmp.write_text(json.dumps(summary,indent=2)+'\n');os.replace(tmp,q)
assert sha(p)==summary['full_output_sha256'];print(json.dumps({'summary_sha256':sha(q),'cells':[r['cell'] for r in summary['cells']],'contracts':contracts}))
