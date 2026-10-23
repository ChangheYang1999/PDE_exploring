"""Recompute checks from completed independent result201/192 data; no solve."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction
import json,hashlib,math
import numpy as np
import mpmath as mp
now=lambda:datetime.now(timezone.utc).isoformat()
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
load=lambda p:json.loads(Path(p).read_text())
checks=[]
def check(name,condition):
    checks.append(dict(name=name,passed=bool(condition)))
    if not condition:raise AssertionError(name)
def close(a,b,rtol=2e-12,atol=2e-15):return math.isclose(a,b,rel_tol=rtol,abs_tol=atol)
r=Path('research/hydrostatic_jacobian_audit/verification');p=r/'states/hsA_c3.0_N48/AUDIT.json';d=load(p)
check('matrix audit complete',d['status']=='DONE')
check('current driver hash',d['code_sha256']==sha('independent_code/audit_hydrostatic_jacobian_state.py'))
for path,h in d['gate_dependencies'].items():check('gate dependency '+path,sha(path)==h)
for path,h in d['input_hashes'].items():check('frozen input '+path,sha(Path('research/hydrostatic_exports_report_audit/verification')/path)==h)
rows=[]
for i,m in enumerate(d['matrices']):
 a,b,c=m['level'];f=p.parent/f'level_{a}_{b}_{float(c).hex()}.npz'
 with np.load(f,allow_pickle=False)as z:
  check(f'level{i} F norm',close(float(np.linalg.norm(z['F'])),m['F_norm']))
  check(f'level{i} F max',close(float(np.max(abs(z['F']))),m['F_max']))
  for key,arr in [('full_with_norm','S_full_with_norm_rows'),('residual_only','S_full'),('visible_residual','S_vis')]:
   s=z[arr];q=m[key];check(f'level{i} {key} spectrum saved',np.array_equal(s,np.array(q['singular_values'])))
 spectra={}
 for key in ['full_with_norm','residual_only','visible_residual','visible_with_norm']:
  q=m[key];s=np.array(q['singular_values']);check(f'level{i} {key} nonincreasing positive',np.all(np.diff(s)<=0) and s[-1]>0)
  for cut,count in q['counts'].items():check(f'level{i} {key} count {cut}',int(np.sum(s<float(cut)*s[0]))==count)
  check(f'level{i} {key} ratio',close(s[-1]/s[0],q['relative_smin']))
  if 'residual_fractions'in q:
   fr=q['residual_fractions'];check(f'level{i} {key} Pythagoras',abs(sum(fr[k]**2 for k in ['kept','dropped','outside'])-1)<1e-12)
   check(f'level{i} {key} gradient identity',close(fr['grad'],q['gradient_norm']/(q['smax']*m['F_norm'])))
   check(f'level{i} {key} eta bound',fr['grad']**2<=q['gradient_square_upper_bound']+1e-14)
  spectra[key]={k:v for k,v in q.items()if k!='singular_values'}
 if i:
  change=m['previous_quadrature_change'];prev=d['matrices'][i-1];delta=max(abs(np.array(m['full_with_norm']['singular_values'])-np.array(prev['full_with_norm']['singular_values'])))
  check(f'level{i} observed Weyl bound',delta<=change['J']['frobenius']*(1+1e-10))
 rows.append(dict(level=m['level'],F_norm=m['F_norm'],F_max=m['F_max'],producer_F_change=m['producer_F_change'],spectra=spectra,quadrature_change=m.get('previous_quadrature_change'),quadratic_remainder=m['quadratic_remainder_error'],file=str(f),sha256=sha(f)))
c=d['center_comparison'];q=c['exact_rational'];exact=Fraction(int(q['numerator'],16),int(q['denominator'],16));check('exact center encoding',q['encoding']=='hexadecimal_integers' and float(exact)==c['exact_float']);check('center row discrepancy',close(c['matrix']-float(exact),c['matrix_minus_exact'],atol=1e-18))
check('same visible dimensions',d['mode_space']['dimensions_equal']);check('orthogonal visible basis',d['mode_space']['orthogonality_error']<1e-12)
sum201=dict(utc=now(),status='CONFIRMED_FINITE_DIAGNOSTICS',source_sha256=d['source_sha256'],export_sha256=d['export_sha256'],audit_sha256=sha(p),started_utc=d['started_utc'],finished_utc=d['finished_utc'],checks=checks.copy(),rows=rows,center={k:v for k,v in c.items()if k!='exact_rational'},dilation=d['dilation'],mode_space={k:v for k,v in d['mode_space'].items()if k!='per_mode'},scope='Finite analytic-derivative matrices and observed quadrature changes only; weakest exact singular values and continuum kernels OPEN; primary endpoint OPEN')
(r/'N48_SUMMARY.json').write_text(json.dumps(sum201,indent=2)+'\n')
text=f'''# Independent N48 hydrostatic Jacobian audit

Completed {d['finished_utc']}; summary checked {sum201['utc']}. Source SHA256 {d['source_sha256']}. Export SHA256 {d['export_sha256']}. Verdict: CONFIRMED finite diagnostics; exact small singular values, continuum kernel and original endpoint OPEN.

The saved c=3,N48,M12 field has522 coefficient unknowns and576 PDE samples, with two affine normalization residuals. This verifier reconstructed Cartesian density derivatives analytically and applied its separate full-line vertical inverse to every basis column. The producer uses a finite-difference map. The parameter bytes, source/export/metadata hashes and all manufactured-gate dependencies were checked. The last gate has56 manufactured checks and40 edge checks. No producer implementation was executed. The spectral restriction retains504 visible coefficient directions, with the same per-mode dimensions as the export; its orthogonality defect is3.05e-14.

| inverse order, tail order, split | norm F | max abs F | observed norm change F | observed Frobenius change J |
| --- | ---: | ---: | ---: | ---: |
'''
for row in rows:
 c=row['quadrature_change'];text+=f"| {row['level']} | {row['F_norm']:.12g} | {row['F_max']:.12g} | {c['F']['frobenius'] if c else 'initial'} | {c['J']['frobenius'] if c else 'initial'} |\n"
text+='''
The finest F differs from the producer F by0.16745 of the producer norm. This compares two specified finite maps, not an identity that they should satisfy. The two last J matrices differ by4.82849e-4 in Frobenius norm; the largest observed singular-value change is2.74315e-5. These are numerical differences, not bounds for either matrix's error to the exact inverse.

| matrix | columns | smallest singular value | relative smallest | counts below relative1e-13,1e-8,1e-4 |
| --- | ---: | ---: | ---: | --- |
'''
for key,q in rows[-1]['spectra'].items():text+=f"| {key} | {q['columns']} | {q['smin']:.12g} | {q['relative_smin']:.12g} | {list(q['counts'].values())} |\n"
text+=f'''
The normalization rows change the smallest direction. A single kernel attributed to dilation does not explain all weak finite directions: the unnormalized matrix has48 relative singular values below1e-8, and the visible restriction still has30. These counts refer to this coefficient norm and numerical threshold. The smallest singular values are far below the observed quadrature perturbation scale; their nonzero numerical values do not prove injectivity of the exact matrix, and their smallness does not prove a continuum kernel.

The full normalized matrix gives ||J^T F||/(||J||_2||F||_2)=0.4208979963, with99.999718 percent of the residual norm in its full column range and an outside fraction0.0023737545. The normalized gradient is not small for this finite analytic map, and the observed state is not a stationary point of that least-squares map. This does not assert failure of the producer's stopping condition or identify an exact stationary point.

The independently projected dilation has relative projection defect3.1153e-5 and agrees with the exported coefficients to4.31e-9 in relative norm. Its continuum derivatives of a and C are zero, and that of K is(1-p)K. The finite projected rows are a'=-2.22e-16, K'=0.6666655648 and C'=-0.0036241183. The latter is a representation/functional discrepancy, not an exact symmetry violation. The exact rational center is{sum201['center']['exact_float']:.12g}. The center row agrees with that exact functional to1.012e-10; it is not one of the two fitted normalization rows. The projected direction has ||Jv||/(||J|| ||v||)=1.99e-9 for the PDE rows and5.22e-7 with normalization. At a trial field the continuum identity is DR[g](g-X.grad g)=R-X.grad R, so dilation is not asserted to be a residual kernel without the PDE.

The pre-review N48 matrices and the exact-rational serialization failure are preserved under review_repairs. The rerun changes guards, representation checks and diagnostics; its valid matrix formulas and computed spectra agree with the earlier actual run. External jac201 review was another referee analysis; its requested Opus API call failed for unavailable credentials. The lead's separate Opus5.5 review remains distinguishable from that failed call. See PROOF.md, SPECTRAL_PROOF.md and REVIEW_REPAIR_PROOF.md for complete hypotheses and derivations. All {len(checks)} postprocessing checks pass.
'''
(r/'N48_SUMMARY.md').write_text(text)
print('201',len(checks),'PASS')
checks=[];mp.mp.dps=140
r=Path('research/smooth_N44_refinement_audit/verification/critical_points');p=r/'AUDIT.json';d=load(p);check('critical audit complete',d['status']=='DONE');rows=[]
for s in d['states']:
 check(s['tag']+' completed',s['status']=='DONE');check(s['tag']+' source',sha(s['source'])==s['source_sha256']);a=load(s['exact_input']);check(s['tag']+' exact input',sha(s['exact_input'])==s['exact_input_sha256']);num=lambda z:mp.mpf(z['numerator'])/mp.mpf(z['denominator']);alpha=num(a['alpha']);ell=num(a['cl']);mpchecks=[]
 for grid in s['grids']:
  check(s['tag']+f" grid{grid['level']} no candidate cells",all(z==0 for z in grid['candidate_cell_counts'].values()))
  for e in grid['extents']:
   check(s['tag']+f" grid{grid['level']} extent{e['extent']} positive samples",all(z==0 for z in e['sampled_nonpositive_counts'].values()) and all(m['value']>0 for m in e['minima'].values()))
 for ax in s['axis_roots']:check(s['tag']+' axis '+ax['axis']+' '+ax['kind'],not ax['brackets'] and not ax['roots'] and not ax['sampled_exact_zeros'])
 check(s['tag']+' no interior seeds',not s['interior_attempts']);check(s['tag']+' exact origin classification',s['origin']['equilibrium'] and not s['origin']['density_critical'])
 for i,pair in enumerate(s['MP']):
  lo,hi=pair['evaluations'];fields=['rho','psi','U1','U2','rho_x','rho_y','R','Nf','Nv'];errors={k:abs(mp.mpf(lo[k])-mp.mpf(hi[k]))/max(1,abs(mp.mpf(hi[k])))for k in fields};check(s['tag']+f' MP{i} precision',max(errors.values())<mp.mpf('1e-60'))
  x,y=mp.mpf(hi['x']),mp.mpf(hi['y']);radius=mp.sqrt(x*x+y*y);wx,wy=ell*x+mp.mpf(hi['U1']),ell*y+mp.mpf(hi['U2']);gx,gy=mp.mpf(hi['rho_x']),mp.mpf(hi['rho_y']);scale=(1+radius**2)**alpha;vals=dict(Wnorm_scaled=mp.sqrt(wx*wx+wy*wy)/radius,gradnorm_scaled=mp.sqrt(gx*gx+gy*gy)*scale,W1_over_x=wx/x if x else None,W2_over_y=wy/y if y else None,gy_scaled=gy*scale);check(s['tag']+f' MP{i} positive',all(z is None or z>0 for z in vals.values()));mpchecks.append(dict(x=float(x),y=float(y),values={k:mp.nstr(z,40)if z is not None else None for k,z in vals.items()},max_precision_scaled_difference=mp.nstr(max(errors.values()),12)))
 finest=s['grids'][-1];matches=[]
 for key,witness in finest['extents'][-1]['minima'].items():
  found=next(z for z in mpchecks if z['x']==witness['x'] and z['y']==witness['y']);v=mp.mpf(found['values'][key]);err=abs(v-mp.mpf(witness['value']))/abs(v);matches.append(dict(field=key,grid=witness['value'],MP=mp.nstr(v,40),relative_difference=mp.nstr(err,12)));check(s['tag']+' MP-grid '+key,err<mp.mpf('1e-8'))
 rows.append(dict(tag=s['tag'],source_sha256=s['source_sha256'],origin=s['origin'],grids=s['grids'],axis_roots=s['axis_roots'],MP=mpchecks,finest_witness_comparisons=matches))
out=dict(utc=now(),status='CONFIRMED_FINITE_SEARCH',finished_utc=d['finished_utc'],audit_sha256=sha(p),checks=checks,rows=rows,scope='No sampled or bracketed new equilibria or density critical points; finite search completeness and exact limiting geometry OPEN; endpoint OPEN')
(r/'SUMMARY.json').write_text(json.dumps(out,indent=2)+'\n')
text=f'''# Independent apparent-critical-point search

Completed {d['finished_utc']}; postprocessing {out['utc']}. Verdict: CONFIRMED finite search; completeness and limiting geometry OPEN.

For each of the three original-equation N36,N40,N44 fields, W=(5/2)X+U[rho] is computed with the independent full-plane inverse. The origin is an equilibrium by parity and has density gradient(0,a0), with nonzero a0. It is not a density critical point. Its Jacobian is diag(ell-c,ell+c), close to diag(4,1), retaining the measured center defect.

Three physical meshes have(radial,angular) sizes(129,95),(257,159),(513,287), with radii1e-8 through1e8. Angles include both axes and extra near-axis layers. The finest mesh has147231 points and is repeated at inverse orders128 and192. Results are separately recorded inside extents10,100,1e4,1e8; a floating comparison tolerance retains the nominal extent endpoints. All axis sign brackets, exact sampled zeros and interior cells whose two components straddle zero are recorded. There were none, so there were no root seeds to refine.

| N | min W1/x | min W2/y | min norm(W)/r | min scaled norm(grad rho) | min scaled rho_y |
| --- | ---: | ---: | ---: | ---: | ---: |
'''
for n,s in zip([36,40,44],rows):
 v=s['grids'][-1]['extents'][-1]['minima'];text+=f"| {n} | "+' | '.join(f"{v[k]['value']:.12g}"for k in ['W1_over_x','W2_over_y','Wnorm_scaled','gradnorm_scaled','gy_scaled'])+' |\n'
text+='''
The positive gradient scaling is(1+r^2)^alpha with the exact saved binary alpha. The ratios W1/x and W2/y use their analytic limiting values on the relevant axes. All reported minima are sampled values, not certified lower bounds. Five selected minima in each state were independently re-evaluated at75 and110 target digits with automatically increased working precision. Their fields agree to better than1e-60 after scaling by max(1,abs(field)); the corresponding five minima agree with the grid to better than1e-8 relative. Exact locations, values, all extents and inverse-order changes are in SUMMARY.json.

This supports stable finite sampled geometry for these three approximations. It does not exclude between-node zeros, zeros beyond the sampled range, or critical points appearing in an unestablished limit. The same sequence still lacks demonstrated slope, high-jet and normalized-residual convergence. No numerical YES follows from this search alone. The proof of the parity reductions and the predeclared search protocol is CRITICAL_POINT_PROOF.md; no change to the prompt's numerical endpoint standard is made.
'''
(r/'SUMMARY.md').write_text(text);(r/'VERDICT.md').write_text(f"{out['utc']}: CONFIRMED finite search ({len(checks)} postprocessing checks). Complete zero exclusion and exact limiting geometry OPEN. Original endpoint OPEN. See SUMMARY.md and CRITICAL_POINT_PROOF.md.\n");print('192critical',len(checks),'PASS')
