"""Summarize actual saved independent observations, without extrapolated errors."""
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib
import numpy as np
root=Path('verification/slaved_states_20261020T1900');source=root/'results.json';d=json.loads(source.read_text())
if d['status']!='COMPLETE':raise SystemExit('Audit still running; no complete summary emitted')
summary={'utc':datetime.now(timezone.utc).isoformat(),'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'elapsed_seconds':d['elapsed_seconds'],'states':[]}
for row in d['states']:
 result={'file':row['file'],'sha256':row['sha256'],'center':row['center'],'self':{},'mixed':{},'far':{},'field_parity':row['parity']}
 for kind in ['self','mixed']:
  runs=[v for v in row['residual_runs'] if v['kind']==kind and v['order']==64]
  a,b=runs
  result[kind]['residuals']={k:{z:b[k][z] for z in ['max_abs','max_ratio','max_ratio_point','zero_N','subnormal_terms']} for k in ['Theta','Omega','F','G']}
  result[kind]['difference_step_change']={k:{z:float(abs(np.array(a[k][z])-np.array(b[k][z])).max()) for z in ['R','ratio']} for k in ['Theta','Omega','F','G']}
  vref=next(v for v in row['inverse_runs'] if v['core']==24 and v['order']==64)
  result[kind]['velocity_domain_spread']=max(float(abs(np.array(v[kind]['V'])-np.array(vref[kind]['V'])).max()) for v in row['inverse_runs'] if v['order']==64)
  result[kind]['velocity_order_change_core24']=float(abs(np.array(next(v for v in row['inverse_runs'] if v['core']==24 and v['order']==32)[kind]['V'])-np.array(vref[kind]['V'])).max())
  result[kind]['omitted_exterior_max_core24']=vref[kind]['omitted_exterior_max']
  vv=np.array(vref[kind]['V']);result[kind]['velocity_reflection_defects']={'V1_odd':float(vv[3,0]+vv[7,0]),'V2_even':float(vv[3,1]-vv[7,1])}
  result[kind]['axis_A_step_change']=max(abs(z['A']-w['A']) for z,w in zip(b['axis_checks'][:2],b['axis_checks'][2:]))
 f=next(v for v in row['far_runs'] if v['core']==400 and v['order']==64)
 result['far']['residuals']={k:{z:f[k][z] for z in ['max_abs','max_ratio','max_ratio_point']} for k in ['Theta','Omega','F','G']}
 result['far']['velocity_domain_spread']=max(float(abs(np.array(v['W'])-np.array(f['W'])).max()) for v in row['far_runs'] if v['order']==64)
 result['far']['velocity_order_change_core400']=float(abs(np.array(next(v for v in row['far_runs'] if v['core']==400 and v['order']==32)['W'])-np.array(f['W'])).max())
 result['verdict']='REJECTED as evidence for a B2 profile; measured residuals remain large'
 summary['states'].append(result)
(root/'summary.json').write_text(json.dumps(summary,indent=2)+'\n')
lines=['# Independent slaved-amplitude state audit','',f"Actual completion: {d['ended_utc']}; computation elapsed {d['elapsed_seconds']:.6f} seconds.",'','All four intermediate states are rejected as evidence for a B2 profile. The following are sampled true B2-P residuals from the self-source full-plane inverse. They are not the forcing-homotopy objective and not a proof of nonexistence.','', '| State | a0 represented | max abs RTheta | max ratio Theta | max abs ROmega | max ratio Omega | max ratio F including axis | max ratio G including axis |','|---|---:|---:|---:|---:|---:|---:|---:|']
for s in summary['states']:
 r=s['self']['residuals'];lines.append(f"| {s['file']} | {s['center']['a0_represented']:.8g} | {r['Theta']['max_abs']:.6g} | {r['Theta']['max_ratio']:.6g} | {r['Omega']['max_abs']:.6g} | {r['Omega']['max_ratio']:.6g} | {r['F']['max_ratio']:.6g} | {r['G']['max_ratio']:.6g} |")
lines+=['','Core24, quadrature64, difference step4e-5; eleven specified Cartesian points. Absolute maxima for divided F/G and exact locations, both step sizes, the forced residuals, and far-point residuals are in results.json and summary.json. Cartesian axis ratios are excluded as vacuous; divided limits are retained. No denominator floor is used.','', '| State | center b0-4a0/beta | self velocity core spread | self velocity order32 to64 change | omitted exterior at core24 | largest ratio change on halving difference step |','|---|---:|---:|---:|---:|---:|']
for s in summary['states']:
 r=s['self'];step=max(z['ratio'] for z in r['difference_step_change'].values());lines.append(f"| {s['file']} | {s['center']['b0_minus_4a0_over_beta']:.6g} | {r['velocity_domain_spread']:.6g} | {r['velocity_order_change_core24']:.6g} | {r['omitted_exterior_max_core24']:.6g} | {step:.6g} |")
lines+=['','The source data are immutable local snapshots with SHA256 in sources.json. The a0 metadata is a solver parameter; the represented value F(0,0) is what enters the independent PDE check. All represented a0 values stay nonzero, so these sampled defects are not explained by collapse to zero temperature. This observation does not exclude other degeneracies or certify a full profile.','', 'The core radii12,24,48 all retain the exact represented source in the complementary infinite region. Their spread and the order changes are empirical quadrature diagnostics, not rigorous error bounds. Exterior omission materially changes velocities. Far checks use radius100 at two angles and cores200,400,800; they do not establish uniform asymptotics. Only two quadrature orders and two derivative steps were used; these are rejection diagnostics, not the complete three-resolution candidate acceptance programme.','', 'The value reader and inverse are separately implemented in this lane. No numerics-lane code is executed or imported. Current-state pointwise div-curl and a stream-based Poisson residual have not been recomputed by this run; prior manufactured validations of the inverse are not a certificate for these four sources. All raw observations are retained. No full endpoint is approved.']
(root/'REPORT.md').write_text('\n'.join(lines)+'\n')
print('\n'.join(lines))
