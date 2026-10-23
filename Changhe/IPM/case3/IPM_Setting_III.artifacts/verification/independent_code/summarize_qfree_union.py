"""Lightweight immutable-output aggregation; no inverse or differentiation recomputation."""
from pathlib import Path
from datetime import datetime,timezone
import json,math,hashlib
regions=[('all',0,float('inf')),('center',0,.01),('core',.01,1),('middle',1,100),('far',100,float('inf'))]
output={'utc':datetime.now(timezone.utc).isoformat(),'levels':[],'scope':'Union of three independently chosen point sets, 204 samples per quadrature. Point maxima only; exact horizontal-axis ratios excluded geometrically. Three full-plane kernel quadratures and Cartesian FD8, no producer inverse.','verdict':'REFUTED exactness of this finite interpolant; CONFIRMED numerical residual findings; OPEN convergence of any refined sequence.'}
for level in range(3):
 points=[];sources=[]
 for tag in ['qfree_N64_first','qfree_N64_far','qfree_N64_center']:
  path=Path('evidence/q_evaluations')/tag/('q'+str(level)+'.json');d=json.loads(path.read_text());assert d.get('finished_utc')
  points+=d['points'];sources.append({'path':str(path),'sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'finished_utc':d['finished_utc']})
 ct=d['center_and_tail'];meta=d['metadata'];a=ct['a0'];K=ct['actual_axis_K'];eta=1/meta['map_kappa'];Lcan=(K/a)**(1/eta)
 row={'level':level,'sources':sources,'metadata':meta,'center_and_tail':ct,'reporting_Lcan':Lcan,'center_native_length':meta['L']*2**(-meta['map_kappa']),'center_jet_defects_in_Lcan_gauge':{'T1_Lcan2_over_a02':ct['forced_cubic_T1']*Lcan**2/a**2,'T2_Lcan2_over_a02':ct['forced_cubic_T2']*Lcan**2/a**2},'regions':{}}
 for name,lo,hi in regions:
  selected=[v for v in points if lo<=v['radius']<hi];good=[v for v in selected if v['y']!=0]
  reg={'point_count':len(selected),'nonaxis_count':len(good),'exact_axis_excluded':len(selected)-len(good)}
  for key in ['abs_R','R_Nf','R_Nv']:
   candidates=selected if key=='abs_R' else good
   top=max(candidates,key=lambda v:v['residuals'][-1][key]);reg[key]={'maximum':top['residuals'][-1][key],'x':top['x'],'y':top['y'],'radius':top['radius']}
  reg['max_parity_error']=max(max(abs(v) for v in point['parity'].values()) for point in selected)
  reg['FD8_step_difference_R_Nf']=max(abs(v['residuals'][-1]['R_Nf']-v['residuals'][-2]['R_Nf']) for v in good)
  row['regions'][name]=reg
 output['levels'].append(row)
output['interlevel_comparisons']={}
for key in ['abs_R','R_Nf','R_Nv']:
 output['interlevel_comparisons'][key]=[abs(output['levels'][i]['regions']['all'][key]['maximum']-output['levels'][2]['regions']['all'][key]['maximum']) for i in range(2)]
path=Path('evidence/q_evaluations/qfree_union_summary.json');path.write_text(json.dumps(output,indent=2)+'\n')
print(json.dumps({'utc':output['utc'],'Lcan':output['levels'][-1]['reporting_Lcan'],'jets':output['levels'][-1]['center_jet_defects_in_Lcan_gauge'],'regions_q2':output['levels'][-1]['regions']},indent=2))
