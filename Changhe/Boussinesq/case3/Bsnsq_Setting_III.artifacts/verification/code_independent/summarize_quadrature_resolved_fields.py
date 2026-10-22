"""Publish only independently computed P287 results and frozen-stage facts."""
from pathlib import Path
from datetime import datetime,timezone
import json,csv,hashlib
R=Path('research/287_quadrature_resolved_fields');V=R/'verification'
a=json.loads((V/'tail_stage_checks.json').read_text());assert a['passed']==a['total']
d=json.loads((V/'results.json').read_text());m=json.loads((V/'manifest.json').read_text())
rows=[];short=[];sensitivity=[]
for s,rec in zip(d['states'],a['records']):
 assert s['sha256']==rec['sha256']
 fine={x['kind']:x for x in s['runs'] if x['relative_step']==1e-5}
 coarse={x['kind']:x for x in s['runs'] if x['relative_step']==2e-5}
 for kind,run in fine.items():
  for field,value in run['summary'].items():
   rows.append({'state':s['label'],'kind':kind,'field':field,'sampled_max_normalized':value['max_ratio'],'sampled_max_absolute':value['max_abs'],'normalized_max_x':value['max_ratio_point'][0],'normalized_max_y':value['max_ratio_point'][1],'absolute_max_x':value['max_abs_point'][0],'absolute_max_y':value['max_abs_point'][1]})
   sensitivity.append(abs(value['max_ratio']-coarse[kind]['summary'][field]['max_ratio']))
 short.append(f"| {s['label']} | {fine['transport']['summary']['F']['max_ratio']:.9g} | {fine['transport']['summary']['G']['max_ratio']:.9g} | {fine['self']['summary']['F']['max_ratio']:.9g} | {fine['self']['summary']['G']['max_ratio']:.9g} | {rec['saved_forced_m']:.9g} | {rec['center']['self']['ratioF']:.9g} |")
with (V/'GLOBAL_RESIDUALS.csv').open('w') as f:
 w=csv.DictWriter(f,fieldnames=rows[0]);w.writeheader();w.writerows(rows)
text=f'''# Six 48-point-quadrature re-solves: independent verification

Written {datetime.now(timezone.utc).isoformat()}. Verdict: CONFIRMED as the finite observations and exact literal-field obstructions below; REFUTED as six literal unforced B2 profiles. The general B2 question remains OPEN.

The complete informal proof is PROOF.md. The six inputs and 24 supporting files were frozen at {m['started_utc']}, before computation. The sequential independent pipeline completed at 2026-10-22T06:07:51Z. Its full-plane PDE evaluation took {d['elapsed_seconds']:.6f} seconds. The separate metadata and exact witness consumer passed {a['passed']}/{a['total']} controls in {a['elapsed_seconds']:.6f} seconds ({a['started_utc']} to {a['ended_utc']}). The first run passed 265/266: its sole mistaken expectation was that the one-inner-iteration lineage-2 rerun changed its vorticity array. That array is bitwise unchanged. Both original control and correction are retained.

## Independent PDE and center checks

Each state uses 15,456 points on 161 radii, 1e-5 through 1e8, both x signs and both axis directions. The verifier uses its own adaptive physical-log-radius Green inverse over the whole plane and seven-point Cartesian differences of the raw represented fields. The fixed source is evaluated in its native source basis. No NUM code was imported or executed. The two steps h=2e-5 max(1,r) and h=1e-5 max(1,r) give at most {max(sensitivity):.9g} difference in the reported maxima of normalized residuals. This is sensitivity, not an error enclosure or a supremum certificate. No denominator floor is used. The precise Cartesian and divided fields, absolute maxima and maximizing points are in verification/GLOBAL_RESIDUALS.csv; all radial bands are in REGIONAL_RESIDUALS.json and .md.

The defining B2 velocity is beta X+B[Omega]. The separately labeled forced velocity adds lambda B[f]. Their normalized divided residuals must not be conflated. The exact center consumer independently reloads the binary coefficients and computes rational B-spline moments.

| State | Forced F | Forced G | B2 F | B2 G | Exact saved forced m, rounded | Exact self center F ratio, rounded |
|---|---:|---:|---:|---:|---:|---:|
'''+ '\n'.join(short)+'''

Every exact self thermal center ratio is strictly positive. Every state therefore fails the defining PDE, independently of finite-grid sampling. The first five retain a0=1.011258, so they also retain that normalization defect; the final state has a0=1. No convergence to a zero-forcing state is inferred from a small forced residual.

## Exact tails and inverse

For every field, separate rational Laurent evaluations confirm nonzero H0, ET, DT, EO and DO, together with simple zeros of the source stream at both axis angles. Since 3<beta<4, the leading self thermal residual power 1-3/beta and next forced power 2/3-2/beta are positive and distinct, above the decaying remainder 1-4/beta. Hence the absolute thermal residual is infinite on the whole plane, for both defining and forced equations. The result concerns each literal spline field, and does not preclude a nearby corrected smooth field. There is no physical truncation wall at the map scale L.

A separate inverse-constant certificate and its consumer give the following rational negative intervals. These are properties of the stored field, not estimates of a limiting continuum branch.

| State | Certified C2 interval |
|---|---|
'''
for rec in a['records']:
 lo,hi=rec['C2']['C2_enclosure_float'];text+=f"| {rec['label']} | [{lo:.3f}, {hi:.3f}] |\n"
text+='''
## Saved-stage comparisons

All six new logs specify ng_quad=48, while none of their archives records ng_quad. They accept the inherited lambda at secant zero, with a finite permissive objective acceptance factor 1e9, inner tolerance 3e-5 and outer tolerance 1e-5. The source coefficients and source geometry are bitwise unchanged in every pair. All temperature vectors change. The five lineage-1 vorticity vectors change; the lineage-2 vector is unchanged after one inner iteration. These facts establish neither a new root nor a bound on its displacement.

| State | Inner iterations | Objective increase, percent | Logged m | Exact saved m minus logged m, rounded |
|---|---:|---:|---:|---:|
'''
for rec in a['records']:
 text+=f"| {rec['label']} | {rec['iterations']} | {rec['objective_increase_percent']:.9g} | {rec['new_logged_m']:.9g} | {rec['saved_minus_logged_m']:.9g} |\n"
text+='''
The logged mismatch is the last pre-update stopping value. The saved-field mismatch is separately recomputed and differs by up to 4.54e-7. Thus the statement that the logged values have absolute value below 1.5e-6 is true, but it must not be applied to every saved-field value: the 40-mode beta3.092 field has saved absolute mismatch 1.5745137e-6. The last, lineage-2 objective increase is 0.0266 percent, outside the 0.475 to 3.50 percent range for the five lineage-1 fields.

This packet does not certify the numerical lane's runtime interpolant or its 12-versus-48-point runtime velocity comparison. A difference between two quadrature orders is not an error bound relative to the exact inverse. The new numerical lane wording of 06:03 makes this distinction; its runtime numbers require a separate independent reproduction. Root-shift, discretization-convergence and unforced-profile claims remain OPEN.

## Verification record and dependencies

- CONFIRMED: six archive identities, source and geometry preservation, inherited lambda and logged acceptance, distinct saved and logged strain.
- CONFIRMED: exact nonzero self-center defects; exact leading thermal residual witnesses and infinite absolute whole-plane thermal residuals; certified negative inverse constants.
- CONFIRMED as floating-point observations: independent finite-grid residuals and step sensitivity, with the stated limits.
- REFUTED: each literal frozen archive as an unforced B2 profile.
- OPEN: solver runtime-interpolation error, exact scalar root shifts, continuum convergence and general smooth B2 existence/nonexistence.

Earlier independent manufactured tests and analytic dependencies are identified in PROOF.md; no new tests are claimed for unchanged code. The complete input hashes, code hashes, rational certificates and raw-array reductions remain alongside this summary. The broader run has no decisive endpoint and no T_end here.
'''
(R/'SUMMARY.md').write_text(text);(V/'SUMMARY.md').write_text(text)
print('published draft summary',len(rows),'rows; max sensitivity',max(sensitivity))
