from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
import sys,json,hashlib
import numpy as np
root=Path(__file__).resolve().parents[1];sys.path.insert(0,str(root.parent/'inverse/code'))
from collocation import NodalDensity
from density import gradient_fd
from linearized import direction_coefficients,LinearDensity
p=root/'verification/physical.json';z=json.loads(p.read_text());assert 'date_end' in z
out={'date':datetime.now(timezone.utc).isoformat(),'physical_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'method':'Independent numerator derivative divided by fixed base report N_f; not an orbit-map derivative or a continuum spectral bound','radius_correction':'Raw evaluation metadata used observer radius10. The two nominal radius10 binary points are slightly outside that ball. Exact bounds below use radius11 and encompass every actual binary point. Physical values are unaffected; no quadrature rerun needed.','states':[]}
T=F(10**30);R0=F(11);bound=lambda C:F(5,2)*C*R0/F(10**24)/(1-(R0/T)**2)**2
for pt in z['points']:assert sum(F(x)**2 for x in pt)<=121
for s,state in zip(z['states'],['dnB_n96m40S.npz','dnSB_n120m48.npz']):
 d=NodalDensity(root/'data'/state);v=np.load(root/'data'/('directions_'+s['tag']+'.npz'))['V'];co=direction_coefficients(d,v);cpu=[LinearDensity(d,co[:,:,j],v[-2,j]) for j in range(v.shape[1])]
 ubase=bound(F(s['tail_base_C']));uds=[bound(F(x)) for x in s['tail_delta_C']];old=[x for x in s['evaluations'] if x['nang']==2048];new=[x for x in s['evaluations'] if x['nang']==4096];assert len(old)==len(new)==4 and len(s['parameter_checks'])==4
 A=np.array([x['delta_R_over_fixed_N_report_f'] for x in new]);B=np.array([x['delta_R_over_fixed_N_report_f'] for x in old]);errs=[];rows=[]
 for x in new:
  pt=x['point'];g=gradient_fd(d,*pt,relative_step=.0005);dg=np.array([gradient_fd(f,*pt,relative_step=.0005) for f in cpu]);err=(np.array(list(map(float,uds)))*np.sum(abs(g))+float(ubase)*np.sum(abs(dg),axis=1))/x['N_report_f'];errs.append(err)
  rows.append({'point':pt,'fixed_N_report_f':x['N_report_f'],'base_gradient':g.tolist(),'direction_gradients':dg.tolist(),'delta_U':x['delta_U'],'delta_R':x['delta_R'],'delta_R_in_fixed_units':x['delta_R_over_fixed_N_report_f'],'tail_contribution_R0_11_in_fixed_units':err.tolist()})
 r={'tag':s['tag'],'state_md5':s['state_md5'],'labels':s['labels'],'node_norms':s['node_norms'],'dcl':s['dcl'],'max_abs_physical_action_by_direction':abs(A).max(0).tolist(),'four_point_action_l2_by_direction':np.linalg.norm(A,axis=0).tolist(),'max_quadrature_refinement_change_by_direction':abs(A-B).max(0).tolist(),'max_spatial_step_change_by_direction':np.array([x['spatial_step_change_fixed_units'] for x in new]).max(0).tolist(),'max_finite_parameter_discrepancy_fixed_units':max(abs(x['R_difference_from_linear_in_fixed_units']) for x in s['parameter_checks']),'max_finite_parameter_U_discrepancy':max(max(abs(y) for y in x['U_difference_from_linear']) for x in s['parameter_checks']),'cpu_gpu_density_error':s['cpu_gpu_density_max_error'],'base_U_tail_bound_exact':str(ubase),'delta_U_tail_bounds_exact':list(map(str,uds)),'max_delta_U_tail_bound':max(map(float,uds)),'max_tail_contribution_fixed_units':float(np.max(errs)),'tail_scope':'Velocity envelopes exact from binary coefficients, corrected observer radius11. Residual conversion uses independently differenced numerical gradients; interior quadrature and differentiation are not interval certified.','rows':rows}
 out['states'].append(r);print(s['tag'],'actions max',r['max_abs_physical_action_by_direction'],'quad',max(r['max_quadrature_refinement_change_by_direction']),'FD',max(r['max_spatial_step_change_by_direction']),'param',r['max_finite_parameter_discrepancy_fixed_units'],'tail',r['max_tail_contribution_fixed_units'])
(root/'verification/physical_summary.json').write_text(json.dumps(out,indent=2)+'\n')
