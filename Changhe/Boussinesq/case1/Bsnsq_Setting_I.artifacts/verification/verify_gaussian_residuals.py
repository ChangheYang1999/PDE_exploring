"""Refined actual-data residual check using Gaussian full-plane velocities."""
import datetime,json,time
from pathlib import Path
import numpy as np
from read_polar_data import PolarData
from independent_residuals import residual_table
from gaussian_plane_inverse import GaussianRule,evaluate_velocity
from plane_quadrature import Rule,origin_strain

def utc():return datetime.datetime.now(datetime.timezone.utc).isoformat(timespec='seconds')
out=Path('runs/gaussian_polar_residuals');out.mkdir(parents=True,exist_ok=True)
obj=PolarData('runs/polar_prelim_b3_verification/source_coefficients.npz',radial_order=192)
old=np.load('runs/polar_prelim_b3_verification/pointwise_h0.0016.npz');points=old['points'];labels=old['labels'];regions=old['regions']
strain=origin_strain(obj.Omega,Rule(radial=144,angular_panels=48,outer_multiplier=2.,outer_minimum=2.))
rows=json.loads((out/'residuals.json').read_text()) if (out/'residuals.json').exists() else []
for hrel,n in [(.004,24),(.0016,32),(.00064,40)]:
 if any(row['hrel']==hrel for row in rows): continue
 start=time.monotonic();rule=GaussianRule(radial=n,angular_panels=n,gaussian_order=2*n,local_fraction=.16)
 arrays,summary=residual_table(obj,points,rule,hrel=hrel,inverse_evaluator=evaluate_velocity,strain_evaluator=lambda omega,rule:strain)
 by_group={};groups={'all':np.ones(len(points),bool),'interior':labels=='interior'}
 groups.update({v:labels==v for v in set(labels)});groups.update({v:regions==v for v in set(regions)})
 for name,take in groups.items():
  by_group[name]={'points':int(np.sum(take))}
  for key in ['R_Theta','R_Omega','E','D_Theta','D_Omega','D_E']:
   by_group[name][key]={'max_abs':float(np.max(np.abs(arrays[key][take]))),'max_ratio':float(np.max(arrays[key+'_ratio'][take]))}
 row={'utc':utc(),'hrel':hrel,'radial':n,'seconds':time.monotonic()-start,'summary':summary,'regions':by_group}
 rows.append(row);(out/'residuals.json').write_text(json.dumps(rows,indent=2)+'\n')
 np.savez_compressed(out/f'pointwise_h{hrel}.npz',points=points,labels=labels,regions=regions,**{k:np.asarray(v,float) for k,v in arrays.items()})
 print(json.dumps({'utc':utc(),'phase':'residual_done','hrel':hrel,'seconds':row['seconds'],'center':summary['center'],'middle':by_group['middle'],'far':by_group['far'],'outside_fit':by_group['outside_fit']}),flush=True)
(out/'finished.json').write_text(json.dumps({'utc':utc(),'status':'completed; no endpoint'},indent=2)+'\n')
