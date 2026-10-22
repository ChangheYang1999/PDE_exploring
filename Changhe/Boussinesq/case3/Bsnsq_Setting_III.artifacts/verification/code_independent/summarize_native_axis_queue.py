"""Reduce own completed axis audits without importing or executing NUM code."""
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib
import numpy as np
from scipy.interpolate import CubicHermiteSpline
root=Path('verification/native_axis_K24_K32_20261021T040425Z')
rows=[];details=[];now=datetime.now(timezone.utc).isoformat()
for name,numname in [('K24_l096','blam24v_lambda0.96'),('K24_l0955','blam24v_lambda0.955'),('K24_l095','blam24v_lambda0.95'),('K32_l095','blam32v_lambda0.95')]:
 folder=root/name;data=json.loads((folder/'results.json').read_text());meta=data['metadata']
 assert data['status']=='COMPLETE' and all(not q['failed']for q in data['quadrature'].values())
 runs={(q['kind'],q['axis'],q['grid'],q['epsilon']):q for q in data['runs']}
 numpath=Path('../numerics/runs',f'axis_{numname}.json');num=json.loads(numpath.read_text())
 with np.load(folder/'self_axis.npz')as f:r=f['radii'].copy();sv=f['v_over_r'].copy();sd=f['vp'].copy()
 with np.load(folder/'seed_axis.npz')as f:assert np.array_equal(r,f['radii']);ev=f['v_over_r'].copy();ed=f['vp'].copy()
 for kind in ['self','transport']:
  for j,axis in enumerate(['up','down']):
   base=runs[kind,axis,'fine',1e-4];rad=np.asarray(base['radii']);idx=list(rad).index(1e8)
   eps=meta['lam']if kind=='transport' else 0.
   vr=meta['beta']+sv[:,j]+eps*ev[:,j];vp=meta['beta']+sd[:,j]+eps*ed[:,j]
   herm=CubicHermiteSpline(np.log(r),np.log(vr),vp/vr-1)
   factors=np.exp(herm(np.log(rad)))/meta['beta']
   compare=[]
   for ep in [1e-4,1e-6,1e-8]:
    a=runs[kind,axis,'fine',ep];b=runs[kind,axis,'coarse',ep]
    compare.append({'epsilon':ep,'maximum_relative_coarse_fine_Q_raw_difference':float(np.max(abs(np.asarray(a['Q_raw'])/np.asarray(b['Q_raw'])-1))),
      'Q_R14':a['Q_raw'][-1], 'Q_R8':a['Q_raw'][idx],
      'relative_to_eps1e4_R14':a['Q_raw'][-1]/base['Q_raw'][-1]-1})
   row={'state':name,'beta':meta['beta'],'lambda':meta['lam'],'kind':kind,'axis':axis,
     'center_slope_error':base['center_slope_error'],'center_H_power':base['exponent_h'],
     'Q_raw_R8':base['Q_raw'][idx],'Q_raw_R14':base['Q_raw'][-1],
     'integral_tail_only_Q_R14':base['Q_integral_tail_only'][-1],
     'raw_R8_relative_to_R14':base['Q_raw'][idx]/base['Q_raw'][-1]-1,
     'actual_g_amplitude_R8':float(base['Q_raw'][idx]*factors[idx]),
     'actual_g_amplitude_R14':float(base['Q_raw'][-1]*factors[-1]),
     'factor_v_over_beta_r_R8':float(factors[idx]),'factor_v_over_beta_r_R14':float(factors[-1]),
     'refinement':compare,'source_archive_sha256':data['archive_sha256']}
   if kind=='transport':
    row.update(NUM_finite_Q_R8=num['axis'][axis]['Q_closed_form_est'],NUM_relative_to_own_raw_R8=num['axis'][axis]['Q_closed_form_est']/base['Q_raw'][idx]-1,
     NUM_projected_strain_shift=num.get('strain_projection',{}).get('shift'),NUM_file=str(numpath),NUM_sha256=hashlib.sha256(numpath.read_bytes()).hexdigest())
   details.append(row)
 summary={'state':name,'beta':meta['beta'],'lambda':meta['lam'],'center_strain_error':data['center']['strain_error'],'archive_sha256':data['archive_sha256'],
  'fine_radii':data['fine_radii'],'coarse_radii':data['coarse_radii'],'elapsed_seconds':data['elapsed_seconds']}
 rows.append(summary)
result={'utc':now,'verdict':'CONFIRMED numerical diagnostics; no candidate and no rigorous quadrature bound',
 'baseline_inner_cutoff':1e-4,'rows':details,'states':rows,
 'interpretation':'Q_raw is the finite-center, finite-C_R integral functional. The true finite-radius amplitude is Q_raw*v/(beta*r). Integral-tail-only correction leaves C_R error. Inexact center slope prevents a nonzero finite exactly normalized axis solution.',
 'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(root/'reduction.json').write_text(json.dumps(result,indent=2)+'\n')
lines=[f'# Independent axis continuation diagnostics\n\nCompleted {now}. Verdict: CONFIRMED numerical measurements, with the cutoff and normalization qualifications below. No B2 candidate is accepted.\n',
 'Own adaptive whole-plane physical-radius inverse was evaluated at735 radii; a nested479-radius grid supplies the interpolation comparison. The seed forcing was evaluated in its independently serialized basis. Hermite interpolation used both the computed velocity and its derivative, followed by adaptive log-radius integration. All inverse quadratures reported convergence. These are floating-point error studies, not rigorous enclosures.\n',
 '| State | beta | direction | Q raw at1e8 | Q raw at1e14 | Integral-tail-only at1e14 | NUM finite estimate at1e8 |\n| --- | ---: | --- | ---: | ---: | ---: | ---: |']
for d in details:
 if d['kind']=='transport':lines.append(f"| {d['state']} | {d['beta']:.10f} | {d['axis']} | {d['Q_raw_R8']:.9f} | {d['Q_raw_R14']:.9f} | {d['integral_tail_only_Q_R14']:.9f} | {d['NUM_finite_Q_R8']:.9f} |")
lines.append('\nAll table rows use inner cutoff1e-4 and the explicitly forced transport velocity. They do not describe B2-P transport. NUM metadata records a center-strain projection for K24 lambda.96 and K32 lambda.95. The older K24 lambda.955/.95 JSON files omit that provenance, so their historical projection is not verified here. The current NUM source applies a projection. This verifier uses the actual inverse without a projection. Reading the NUM source establishes that its quoted Q estimate ends at1e8; its separate displayed trajectory array stops at5e7. No NUM code was imported, executed or reused.\n')
lines.append('| State | self upper Q at1e14 | self lower Q at1e14 | center strain defect |\n| --- | ---: | ---: | ---: |')
for st in rows:
 q=[d for d in details if d['state']==st['state']and d['kind']=='self']
 lines.append(f"| {st['state']} | {q[0]['Q_raw_R14']:.9f} | {q[1]['Q_raw_R14']:.9f} | {st['center_strain_error']:.6g} |")
maxgrid=max(q['maximum_relative_coarse_fine_Q_raw_difference']for d in details for q in d['refinement'])
maxinner=max(abs(q['relative_to_eps1e4_R14'])for d in details for q in d['refinement'])
lines.append(f'\nAcross both velocities, axes and inner cutoffs1e-4/1e-6/1e-8, the largest relative coarse/fine Q difference is {maxgrid:.6g}; the largest change of Q(1e14) from varying the inner cutoff is {maxinner:.6g}. Every center strain defect is nonzero. Packet112 proves that exact center-normalized axis transport then fails and predicts a power-law dependence on the inner cutoff. These small finite-cutoff changes must not be called a converged exact profile slope.\n')
lines.append('\nQ raw is a finite integral functional, not the actual finite-radius amplitude g(r)r^(1+1/beta). The latter equals Q raw times v(r)/(beta r); both are included in reduction.json. Adding only the leading missing integral tail does not correct the finite C_R factor. Thus neither the third nor fourth numeric column is presented as a certified asymptotic limit. The upper values still change noticeably beyond radius1e8, and the raw-versus-NUM differences include quadrature, interpolation and the center projection.\n')
lines.append('\nReproduce the reduction: python3 code_independent/summarize_native_axis_queue.py. Each subfolder contains its immutable archive and manifest, full results, axis arrays, quadrature evidence and source-code hashes. The serial inverse/ODE queue ran04:04:25.640368 to04:10:40.803915Z,375.164s. No additional inverse computation was performed for this reduction.\n')
(root/'SUMMARY.md').write_text('\n'.join(lines)+'\n')
inputs=[Path(__file__),root/'queue_status.json']+[p for name in ['K24_l096','K24_l0955','K24_l095','K32_l095']for p in [(root/name/'manifest.json'),(root/name/'results.json'),(root/name/'self_axis.npz'),(root/name/'seed_axis.npz')]]
(root/'build_inputs.json').write_text(json.dumps({'utc':now,'inputs':[{'path':str(p.resolve()),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}for p in inputs]},indent=2)+'\n')
print('summary',now,'maxgrid',maxgrid,'maxinner',maxinner)
for d in details:
 if d['kind']=='transport':print(d['state'],d['axis'],'amplitudeR8/R14',d['actual_g_amplitude_R8'],d['actual_g_amplitude_R14'],'NUMrelative',d['NUM_relative_to_own_raw_R8'])
