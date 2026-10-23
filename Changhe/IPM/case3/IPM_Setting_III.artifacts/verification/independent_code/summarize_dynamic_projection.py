"""Summarize frozen result167 and its independent precision checks."""
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib
root=Path('research/dynamic_projection_audit/verification');audit=json.loads((root/'AUDIT.json').read_text());mp=json.loads((root/'MP_PEAKS.json').read_text())
assert audit['status']==mp['status']=='COMPUTED'
rows=[]
for c in audit['cases']:
 for z in c['rows'][-1]['projections']:
  for location in ['nodes','between']:
   for region,v in z[location].items():
    rows.append(dict(N=c['N'],M=c['M'],tau=c['tau'],cw=c['cw'],cx=c['cx'],rcond=z['rcond'],location=location,region=region,**v))
s={'utc':datetime.now(timezone.utc).isoformat(),'verdict':'CONFIRMED finite projection discrepancy; continuum and time-convergence claims OPEN','audit_sha256':hashlib.sha256((root/'AUDIT.json').read_bytes()).hexdigest(),'mp_sha256':hashlib.sha256((root/'MP_PEAKS.json').read_bytes()).hexdigest(),'rows':rows,'MP_peaks':mp['cases'],'scope':audit['scope']}
(root/'SUMMARY.json').write_text(json.dumps(s,indent=2)+'\n')
lines=['# Independent DR projection audit','',s['utc'],'','CONFIRMED for the six frozen finite fields and the specified projector. This is canonical G passed through an independently evaluated projector. It is not automatically the actual derivative of the producer trajectory, whose own approximate G and coefficient derivative must be compared.','',
'G = cw rho - (cx X + U) dot grad rho. Gp is the reconstructed projected density derivative. The norm ratio below is ||Gp-G||_infinity / ||G||_infinity on the same sampled set, not a pointwise relative residual. Regions are core r<1, annulus 1<=r<100 and far r>=100. Nodal and between-node grids differ with N; saved times are not identical. No time-convergence or uniform-error claim follows.','',
'| N | actual tau | grid | core defect | annular G maximum | annular defect | defect / G maximum |', '|---:|---:|:---|---:|---:|---:|---:|']
for c in audit['cases']:
 z=c['rows'][-1]['projections'][0]
 for where in ['nodes','between']:
  a=z[where]['annulus'];d=z[where]['core']['projection_defect_sup'];lines.append(f"| {c['N']} | {c['tau']:.9f} | {where} | {d:.7g} | {a['canonical_rhs_sup']:.9g} | {a['projection_defect_sup']:.9g} | {a['defect_over_rhs_sup']:.7g} |")
lines+=['','At tau=0 the largest core/annular discrepancies are at floating point roundoff. At tau about20, annular projection defects remain substantial and decrease over these three saved states. At N64 the annular defect is nearly unchanged over cutoffs1e-13,1e-10,1e-8, while the reconstructed coefficient maximum drops from about2.14e6 to23.2. This experiment concerns one frozen state at each size, not cutoff independence of evolved trajectories.','',
'Canonical inverse orders128/256 differ globally by at most3.18e-9 among these nodal and between-node grids; differences at the six annular peak witnesses are checked below with55/85-digit independent finite primitives. Nodal coefficient cancellation is recorded separately in AUDIT.json and is much smaller than the displayed annular defects. SVD orthogonality, projector symmetry and idempotence pass at3e-13.','',
'| N | grid | x | y | canonical G (MP) | Gp-G (MP G, double Gp) | double G minus MP |', '|---:|:---|---:|---:|---:|---:|---:|']
for c in mp['cases']:
 for pt in c['points']:
  v=pt['values'][-1]['fields'];x,y=pt['point'];lines.append(f"| {c['N']} | {pt['kind']} | {x:.10g} | {y:.10g} | {float(v['G']):.12g} | {float(v['Gp_minus_G']):.12g} | {float(v['quadrature_G_minus_MP']):.4g} |")
lines+=['','The independently differentiated high-precision canonical values agree across55/85 digits at the recorded precision. These checks validate the large peak discrepancies; they do not certify the entire grid. Complete precision comparisons, pointwise density, velocity, derivatives, residuals and denominators are in MP_PEAKS.json. Coefficients, all nodal/between-node arrays, source hashes, singular values and cutoff ranks are in AUDIT.json and its NPZ artifacts.','',
'Neither the canonical right-hand side nor the projected derivative is close to zero in the observed annulus. Calling the unprojected right-hand side the numerical time derivative is incorrect without measuring this defect. A matched-time and matched-inverse trajectory comparison remains OPEN.']
(root/'SUMMARY.md').write_text('\n'.join(lines)+'\n')
print(s['utc'],len(rows),'regional rows',sum(len(c['points'])for c in mp['cases']),'MP points')
