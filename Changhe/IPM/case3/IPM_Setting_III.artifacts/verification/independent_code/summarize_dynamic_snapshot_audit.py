from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,math
import mpmath as mp
p=Path('research/dynamic_rescaling_implementation/verification/dr_first_tau20/AUDIT.json');d=json.loads(p.read_text());assert d['status']=='COMPUTED'
rows=[]
for s in d['states']:
 assert s['status']=='COMPUTED' and len(s['multiprecision'])==2
 h=s['multiprecision'][-1];lo=s['multiprecision'][0];assert len(h['points'])==len(lo['points'])==6
 with mp.workdps(100):
  worst_precision=max(mp.mpf(v)for r in s['precision_comparisons']for v in r['errors'].values())
  assert worst_precision<mp.mpf('1e-52')
  direct=[]
  for j,point in enumerate(h['points']):
   fd=s['direct_checks'][-1]['points'][j];values=fd['residuals']
   error=abs(mp.mpf(values[-1]['R_Nf'])-mp.mpf(point['R_Nf']))
   direct.append({'point':[point['x'],point['y']],'MP_R':point['R'],'MP_Nf':point['Nf'],'MP_Nv':point['Nv'],'MP_R_Nf':point['R_Nf'],'MP_R_Nv':point['R_Nv'],'FD_R_Nf':values[-1]['R_Nf'],'FD_R_Nf_error':float(error),'FD_step_spread':max(v['R_Nf']for v in values)-min(v['R_Nf']for v in values)})
  row={'N':s['metadata']['N'],'M':s['metadata']['M'],'tau':s['metadata']['tau'],'cw':s['metadata']['cw'],'cx':s['metadata']['cx'],'a_star':h['a'],'source_sha256':s['source_sha256'],
       'canonical_c':s['canonical_c'],'producer_c_error':s['c_difference'],'normalized_center_defect':s['normalized_center_defect'],
       'trace_A3':s['tail']['A3'],'trace_K':s['tail']['K'],'max_trace_Bk_ge_1':s['tail']['max_absolute_endpoint_mode_k_ge_1'],
       'I1':s['moments'][-1]['values']['1.0'],'I10':s['moments'][-1]['values']['10.0'],'I100':s['moments'][-1]['values']['100.0'],
       'core_sampled_R_Nf':s['grid'][-1]['summary']['core']['R_Nf']['maximum'],'annulus_sampled_R_Nf':s['grid'][-1]['summary']['annulus']['R_Nf']['maximum'],
       'max_scaled_precision_difference':mp.nstr(worst_precision,20),'selected_checks':direct,
       'inverse_order_difference_over_Nf':s['grid'][-1]['inverse_difference_over_Nf']}
  rows.append(row)
result={'utc':datetime.now(timezone.utc).isoformat(),'status':'CONFIRMED for saved-field residuals; trajectory convergence OPEN','audit_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'rows':rows,
        'conclusions':['The three saved normalized fields are far from stationary under the canonical full-plane inverse.','Raw snapshots have an exterior moment near +0.135 from r>1 against total c near -0.0332; the nonlocal exterior term is substantial.','Stored times differ by up to 0.0111; these are not matched-time convergence data. The annular gradients differ substantially even near tau20.','N64 independent normalized center defect is about 6.24e-7; N96/N128 are about -2.8e-10/-2.2e-10.','55/85-digit finite primitives and independent Cartesian kernel/FD8 checks confirm the selected large residuals.','Actual projected time derivative, projection defect, matched time-step convergence and corrected physical-time bookkeeping remain to be audited on new producer runs.'],
        'scope':'No global uniform residual bound, trajectory convergence, existence, nonexistence or continuum instability is inferred.'}
out=p.parent/'SUMMARY.json';out.write_text(json.dumps(result,indent=2)+'\n')
lines=['# Independent dynamic-rescaling snapshot audit','',result['utc'],'','Three first-batch C=3 states near tau=20, frozen with source hashes in AUDIT.json. The densities are divided by their saved c_w; the canonical center condition is recomputed independently.','',
       '| N x M | Actual tau | a_star | Canonical center defect | Sampled core max R/Nf | Sampled annulus max R/Nf |',
       '|---|---:|---:|---:|---:|---:|']
for r in rows:lines.append(f"| {r['N']} x {r['M']} | {r['tau']:.9f} | {float(r['a_star']):.8f} | {r['normalized_center_defect']:+.4e} | {r['core_sampled_R_Nf']:.9f} | {r['annulus_sampled_R_Nf']:.9f} |")
lines+=['','The grid uses 98 radii (stored exactly in AUDIT.json), 53 angles including near-axis points and the vertical axis, and inverse orders 128/256. Counts should be read from AUDIT.json if this grid definition changes. Six selected points per state are reevaluated with the Cartesian cancellation-kernel inverse at two resolutions, eighth-order finite differences at three step sizes, and the finite canonical primitives at 55/85 target digits. No denominator threshold is used. The horizontal-axis identity zeros are omitted geometrically.','',
       'At (6,8), the normalized density, x derivative and residual R/Nf are:','',
       '| N | rho_star | partial_x rho_star | R/Nf |','|---|---:|---:|---:|']
for s in d['states']:
 v=s['multiprecision'][-1]['points'][-1];lines.append(f"| {s['metadata']['N']} | {float(v['rho']):.9f} | {float(v['gradient'][0]):+.9f} | {float(v['R_Nf']):.9f} |")
lines+=['','These differences disallow treating the entire annulus as resolved from agreement of a few core scalar diagnostics. They occur at slightly different saved times, so they are not by themselves an estimate of a fixed-time discretization error.','','Exterior moments I_R = integral_R^infinity f3/r^2 dr:','',
       '| N | c | I_1 | I_10 | I_100 |','|---|---:|---:|---:|---:|']
for r in rows:lines.append(f"| {r['N']} | {r['canonical_c']:+.10f} | {r['I1']:+.10f} | {r['I10']:+.10f} | {r['I100']:+.10f} |")
lines+=['','The exact rational center formula and the independent exterior polynomial quadrature agree to a few 1e-15 in raw strain. The source terms have opposite signs: -a/4 is near -0.25 and I_0 is near +0.2168. A relative percentage of the small difference c would be misleading without showing those terms.','','Verdicts: canonical saved-field residuals CONFIRMED; far-from-stationary snapshots CONFIRMED; an inference of nonnormal growth from eigenvector localization REFUTED by the symmetric 2x2 counterexample in PROOF.md; trajectory convergence and continuum instability OPEN. The run remains UNRESOLVED.','']
# Derive counts rather than relying on prose constants.
lines=[x.replace('98 radii','%d radii'%len(d['states'][0]['grid_log_radius'])).replace('53 angles','%d angles'%len(d['states'][0]['grid_theta']))for x in lines]
(p.parent/'SUMMARY.md').write_text('\n'.join(lines))
print(json.dumps({'utc':result['utc'],'rows':[{k:r[k]for k in ['N','tau','normalized_center_defect','core_sampled_R_Nf','annulus_sampled_R_Nf','max_scaled_precision_difference']}for r in rows]}))
