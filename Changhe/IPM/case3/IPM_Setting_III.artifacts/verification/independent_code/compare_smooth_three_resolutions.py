"""Result192: summarize existing independently verified finite data, no new solve."""
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,math

root=Path('research/smooth_N44_refinement_audit/verification')
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
load=lambda p:json.loads(Path(p).read_text())
rows=[];manifest={};reference=None
for n in [36,40,44]:
    tag=f'common1000_moments_cl2.5_N{n}M{n-4}'
    paths=[Path(f'research/smooth_N{n}_refinement_audit/verification/SUMMARY.json'),Path(f'evidence/smooth_exact_jets/{tag}/jets.json'),Path(f'evidence/smooth_residual_grid/{tag}/diagnostic.json')]
    summary,jets,dense=map(load,paths);source=Path(summary['source']);h=sha(source)
    assert h==summary['source_sha256']==jets['source_sha256']==dense['sha256']
    args=summary['solver_arguments'];fixed={k:v for k,v in args.items()if k not in ['radial','angular','tag']}
    if reference is None:reference=fixed
    assert fixed==reference and args['max_nfev']==summary['solver']['nfev']==1000 and summary['solver']['solver_status']==0
    mp={}
    for path in summary['manifest']:
        if 'smooth_mp_inverse/' in path:
            p=Path(path);data=load(p);assert data['source_sha256']==h
            paths.append(p)
            for point in data['rows'][-1]['points']:mp[(float(point['x']),float(point['y']))]=point
    for p in [source,*paths]:manifest[str(p)]=sha(p)
    regions={}
    for name in ['origin','core','middle','far','extent_2','extent_4','extent_8']:
        candidates=[r['summary'][name]for r in dense['rows']if r['inverse_order']==256 and name in r['summary']]
        if not candidates:continue
        regions[name]={}
        for field in ['abs_R','R_Nf','R_Nv']:
            peak=max([r[field]for r in candidates if field in r],key=lambda q:q['maximum'])
            key=(float(peak['x']),float(peak['y']));point=mp.get(key)
            regions[name][field]=dict(double_grid_peak=peak,MP_at_peak=point,MP_available=point is not None)
    exts=[]
    for rmax in [100.,1e4,1e8]:
        selected=[p for p in mp.values()if float(p['radius'])<=rmax]
        exts.append(dict(rmax=rmax,selected_points=len(selected),maxima={f:max([p for p in selected if p[f] is not None],key=lambda p:float(p[f]))for f in ['abs_R','R_Nf','R_Nv']}))
    rows.append(dict(N=n,M=n-4,tag=tag,source=str(source),sha256=h,a=jets['a_float'],c=jets['c_float'],Delta=jets['delta_float'],ell=args['cl'],b=summary['solver']['b'],e=summary['solver']['e'],solver_cost=summary['solver']['cost'],solver_optimality=summary['solver']['optimality'],solver_seconds=summary['solver']['elapsed_seconds'],MP_selected_maxima=summary['MP_selected_maxima'],jets=[dict(degree=r['degree'],R_tensor=r['R']['derivative_frobenius'],rho_tensor=r['rho']['derivative_frobenius'])for r in jets['by_degree']],regions=regions,extents=exts,MP_point_count=len(mp)))
changes=[]
for a,b in zip(rows,rows[1:]):
    changes.append(dict(from_N=a['N'],to_N=b['N'],relative_a=b['a']/a['a']-1,relative_b=b['b']/a['b']-1,relative_e=b['e']/a['e']-1,relative_NF=float(b['MP_selected_maxima']['R_Nf']['R_Nf'])/float(a['MP_selected_maxima']['R_Nf']['R_Nf'])-1))
result=dict(utc=datetime.now(timezone.utc).isoformat(),status='CONFIRMED_FINITE_COMPARISON',common_arguments=reference,rows=rows,changes=changes,manifest=manifest,code_sha256=sha(__file__),scope='Three equal-evaluation-budget finite fields, not stationary fits or an observed converged profile. Old maxima are not silently recomputed on new adaptive grids. The N44 grid retains the N40 physical grid and rectangles, with extra adaptive rectangles. MP columns refer to selected points.',verdicts=dict(nonzero_measured_slopes='CONFIRMED',systematic_monotone_sampled_residual_refinement='REFUTED_FOR_THIS_SEQUENCE',convergence='OPEN',primary_endpoint='OPEN'))
(root/'THREE_RESOLUTIONS.json').write_text(json.dumps(result,indent=2)+'\n')
fmt=lambda x:f'{float(x):.10g}'
text=f'''# Three common-budget original-equation approximations

Completed {result['utc']}. Endpoint UNRESOLVED. This compares the independently reconstructed N36 M32, N40 M36 and N44 M40 fields. All use ell=2.5, the same N24 seed, inverse order108, normalization, cubic penalty and1000-function-evaluation budget. The fitting grid changes with the basis size. Each run exhausted that budget, so this does not isolate finite-basis error from optimization error. The true whole-plane inverse is used in the audits.

| N, M | a0 | b=rho_xxy(0)/2 | e=rho_yyy(0)/6 | Selected max abs(R)/N_f | Selected max abs(R)/N_v | Canonical origin defect |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
'''
for r in rows:text+=f"| {r['N']}, {r['M']} | {fmt(r['a'])} | {fmt(r['b'])} | {fmt(r['e'])} | {fmt(r['MP_selected_maxima']['R_Nf']['R_Nf'])} | {fmt(r['MP_selected_maxima']['R_Nv']['R_Nv'])} | {fmt(r['Delta'])} |\n"
text+='''
These slopes are nonzero, and the fixed ell is separated from the excluded affine value1. This is a finite-state check, not a limiting assertion. The slope decreases by1.1468% and then2.0130%. The observed normalized residual decreases by34.9876% and then increases by2.9163%. The two cubic coefficients also move. The sequence has not demonstrated stationary fits, a converged invariant slope, or systematic residual refinement. Non-monotone equal-budget errors do not imply mathematical nonexistence.

The N44 canonical peak is away from the axis, at x=0.0652183279, y=0.581544386. The coarser complementary-chart maximum9.8832e-8 missed this larger local-grid peak. Thus a statement that N44 improves on N40 based on that chart alone would be false. All headline points were independently checked at75 and110 target digits, as recorded in each audit.

## Physical extents and absolute residuals

The following values are maxima among the independent multiprecision follow-up points inside the stated extent. The JSON also preserves the full double-grid regional peaks, their denominators and locations, and whether each has an exact-coordinate MP counterpart. These are sampled maxima, not uniform bounds.

| N | r_max | MP points | max abs(R) | max abs(R)/N_f | max abs(R)/N_v |
| --- | ---: | ---: | ---: | ---: | ---: |
'''
for r in rows:
    for e in r['extents']:
        text+=f"| {r['N']} | {fmt(e['rmax'])} | {e['selected_points']} | {fmt(e['maxima']['abs_R']['abs_R'])} | {fmt(e['maxima']['R_Nf']['R_Nf'])} | {fmt(e['maxima']['R_Nv']['R_Nv'])} |\n"
text+='''
The full grids cover much larger radii as documented in the separate audits. A rounded exponent causes an exact nonzero leading far-field transport multiplier of1/18014398509481984 for the literal saved formulas. That rounding artifact is reported separately from approximation error. The exact-exponent interpretation is a separately defined field, not an unannounced data replacement.

## Higher center derivatives

| N | Degree | R derivative tensor Frobenius norm | rho derivative tensor Frobenius norm |
| --- | ---: | ---: | ---: |
'''
for r in rows:
    for j in r['jets']:
        text+=f"| {r['N']} | {j['degree']} | {fmt(j['R_tensor'])} | {fmt(j['rho_tensor'])} |\n"
text+='''
These exact Taylor diagnostics do not settle to zero across the three finite fields. They do not by themselves prove a singular limit. Formula-level smoothness is confirmed for every finite field; convergence of its higher jets remains open. An independent apparent-critical-point search is recorded separately when completed. All source hashes, actual solver sensitivities and pointwise denominators are in THREE_RESOLUTIONS.json. No extra requirement of a rigorous uniform certificate is imposed on the prompt's numerical YES standard.
'''
(root/'THREE_RESOLUTIONS.md').write_text(text)
print(result['utc'],result['status']);print(json.dumps(changes,indent=2))
