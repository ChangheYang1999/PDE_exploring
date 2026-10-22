from pathlib import Path
from datetime import datetime,timezone
import csv,json
R=Path('research/294_tight_quadrature_roots');V=R/'verification';a=json.loads((V/'tail_stage_checks.json').read_text());assert a['passed']==a['total'];d=json.loads((V/'results.json').read_text());m=json.loads((V/'manifest.json').read_text());rows=[];tab=[];sens=[]
for state,rec in zip(d['states'],a['records']):
 assert state['sha256']==rec['sha256'];fine={x['kind']:x for x in state['runs']if x['relative_step']==1e-5};coarse={x['kind']:x for x in state['runs']if x['relative_step']==2e-5}
 for kind,run in fine.items():
  for field,z in run['summary'].items():
   rows.append(dict(state=state['label'],kind=kind,field=field,sampled_max_normalized=z['max_ratio'],sampled_max_absolute=z['max_abs'],normalized_max_x=z['max_ratio_point'][0],normalized_max_y=z['max_ratio_point'][1],absolute_max_x=z['max_abs_point'][0],absolute_max_y=z['max_abs_point'][1]));sens.append(abs(z['max_ratio']-coarse[kind]['summary'][field]['max_ratio']))
 tab.append(f"| {rec['order']} | {fine['transport']['summary']['F']['max_ratio']:.10g} | {fine['transport']['summary']['G']['max_ratio']:.10g} | {fine['self']['summary']['F']['max_ratio']:.10g} | {fine['self']['summary']['G']['max_ratio']:.10g} | {rec['center']['self']['ratioF']:.10g} |")
with (V/'GLOBAL_RESIDUALS.csv').open('w')as f:w=csv.DictWriter(f,fieldnames=rows[0]);w.writeheader();w.writerows(rows)
s=f'''# Two tighter quadrature secant runs: independent verification

Written {datetime.now(timezone.utc).isoformat()}. The finite comparisons below are CONFIRMED, with explicit numerical limits. Both literal archives are REFUTED as B2 profiles by exact nonzero center defects and whole-plane tail obstructions. General B2 remains OPEN.

The complete proof preceded computation. Two primary fields and16supporting inputs were frozen at {m['started_utc']}. The single sequential pipeline completed06:31:15Z. Full-plane PDE evaluation took {d['elapsed_seconds']:.6f}s. The separate exact-tail and saved-stage consumer passed{a['passed']}/{a['total']} in{a['elapsed_seconds']:.6f}s. Its first attempt stopped on missing start_sha256 metadata in a secant archive; the correction checks each secant's source coefficients and geometry directly, retaining final-archive restart hashes. Original code and the correction are preserved.

## Finite scalar comparison

Both logs use beta3.062, K32, angular sampling parameter Nphi64, radial parameter Nt56, native source basis3, initiallambda0.93171, inner tolerance3e-6 and outertolerance1e-7. Each run has four scalar trials0..3 with positive and negative first two mismatches, followed by two secant updates. All inner solves report fixed-point convergence; final saved arrays match secant3. Exact-binary secant arithmetic agrees within1e-14 with the saved lambda values.

| Nominal Gauss order | Saved lambda | Logged final m | Exact saved forced m, rounded | First-pair finite slope |
|---|---:|---:|---:|---:|
'''
for r in a['records']:s+=f"| {r['order']} | {r['metadata']['lam']:.16g} | {r['new_logged_m']:.12g} | {r['saved_forced_m']:.12g} | {r['sample_slope']:.12g} |\n"
s+=f'''
The exact difference lambda48-lambda12 is {a['lambda_difference_exact']}, or {a['lambda_difference_float']:.16g}. These are two computed finite secant states. Their mismatch signs do not supply continuity, interval evaluations, a scalar root enclosure or discretization convergence. The unknown fields change while the source block and geometry remain bitwise unchanged. Both lambda values differ from the older stored value. The quadrature orders are verified from frozen logs, not archive metadata, which omits them. Both saved exact forced mismatches are nonzero and below the nominal outertolerance. They differ from the logged last pre-update values by about4e-10 to5e-10.

## Independent defining PDE, center and full plane

The defining velocity is W=beta X+B[Omega], with the canonical full-plane relative inverse. The separately labeled forced calculation adds lambda B[f] in its native basis. Our own evaluator uses adaptive physical-radius Green integrals through infinity and seven-point Cartesian differences, with no numerical-lane code imported or executed. It evaluates15,456points,161radii from1e-5to1e8, both x signs and both axis directions. Two Cartesian steps give at most{max(sens):.10g} change in these normalized maxima. This is finite sensitivity, not an enclosure or supremum certificate. The physical Cartesian normalizers and divided normalizers are distinguished, with no denominator floor.

| Gauss order label | Forced F | Forced G | B2 F | B2 G | Exact self center F ratio, rounded |
|---|---:|---:|---:|---:|---:|
'''+ '\n'.join(tab)+'''

Every exact self center thermal defect is nonzero, so neither represented field satisfies the defining PDE. The Cartesian residual vanishes on the symmetry axis, but its normalized off-axis limit equals the positive divided center ratio proved in PROOF.md. Both fields retain the a0=1.011258 normalization label, and neither approaches zero forcing in this comparison. These are literal-field conclusions, not a nonexistence theorem for corrected profiles.

Exact rational endpoint witnesses establish nonzero H0, ET, DT, EO and DO, including simple source-stream zeros at both axis angles. With3<beta<4, the thermal powers1-3/beta and2/3-2/beta are distinct and positive, above the decaying remainder1-4/beta. The absolute whole-plane thermal residual is therefore infinite for both the defining and forced equations. The representation covers the whole plane; the map scale is no physical boundary.

| Gauss order label | Certified C2 interval | Raw objective |
|---|---|---:|
'''
for r in a['records']:
 lo,hi=r['C2']['C2_enclosure_float'];s+=f"| {r['order']} | [{lo:.3f}, {hi:.3f}] | {r['new_objective']:.12g} |\n"
s+='''
The noticeably different C2 values are exact certificates for two stored fields. No continuum value or convergence rate follows. All radial bands, absolute and normalized residuals, maximizing points and input hashes remain in verification/. This audit does not reproduce the numerical lane's runtime interpolation or establish its error. P291 separately checks finite runtime-norm comparisons with conditional scope.

## Verdict and dependencies

CONFIRMED: literal archive provenance, four secant trials at each nominal order, exact saved scalar difference, nonzero center defects, exact tail obstructions, and negative inverse constants. CONFIRMED as finite floating-point observations: sampled PDE residuals and step sensitivity. REFUTED: either literal archive as an unforced B2 profile. OPEN: continuum root displacement, convergence, rigorous finite-grid error bounds and general smooth B2 existence or nonexistence. No decisive endpoint or T_end is declared.
'''
(R/'SUMMARY.md').write_text(s);(V/'SUMMARY.md').write_text(s);print(len(rows),max(sens))
