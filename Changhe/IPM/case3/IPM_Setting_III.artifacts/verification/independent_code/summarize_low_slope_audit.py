"""Collect independently generated diagnostics, enforcing frozen-source agreement."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
import json,hashlib
import mpmath as mp

root=Path('research/low_slope_state_audit/verification')
load=lambda p:json.loads(Path(p).read_text())
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
exact=load(root/'EXACT_QUOTIENT_WITNESSES.json');assert exact['status']=='PASS'
jets=load('evidence/q_exact_jets/LOW_SLOPE_2/diagnostic.json');assert jets['status']=='COMPUTED_EXACT'
rows=[];manifest={str(root/'EXACT_QUOTIENT_WITNESSES.json'):sha(root/'EXACT_QUOTIENT_WITNESSES.json')}
with mp.workdps(145):
 for ex,j in zip(exact['rows'],jets['rows']):
  tag=ex['tag'];h=ex['source_sha256'];assert sha(ex['source'])==h==j['metadata']['sha256']
  paths={k:str(Path(base)/tag/'diagnostic.json') for k,base in [('quotient','evidence/low_slope_quotient'),('dense','evidence/q_residual_grid'),('MP','evidence/q_mp_inverse')]}
  q,d,m=(load(paths[k]) for k in ['quotient','dense','MP'])
  assert q['status']==d['status']==m['status']=='COMPUTED'
  assert q['source_sha256']==d['sha256']==m['source_sha256']==h
  assert [r['digits'] for r in q['MP']]==[80,120]
  assert [r['target_digits'] for r in m['rows']]==[75,110]
  for p in paths.values():manifest[p]=sha(p)
  manifest[ex['source']]=h
  mm=m['rows'][-1]
  peaks={key:max(mm['points'],key=lambda p:mp.mpf(p[key])) for key in ['R_Nf','R_Nv']}
  qsets=[]
  for i,r in enumerate(q['rows']):
   coords={(p['x'],p['y']):p for p in q['MP'][-1]['points']}
   rr={k:v for k,v in r.items() if k!='extrema'};rr['extrema']={}
   for k,p in r['extrema'].items():
    assert (p['x'],p['y']) in coords
    rr['extrema'][k]={**p,'q_MP120':coords[(p['x'],p['y'])]['q']}
   qsets.append(rr)
  row={'tag':tag,'source':ex['source'],'source_sha256':h,'metadata':j['metadata'],
    'a':mm['a'],'c':mm['c'],'delta':mm['delta'],'a_over_D':mp.nstr(mp.mpf(mm['a'])/(mp.mpf(j['exact']['ell']['exact'])-1),35),
    'b_core':j['exact']['b_core']['approx'],'e_core':j['exact']['e_core']['approx'],
    'q_y_derivative_at_sigma_zero':ex['q_y_derivative_at_sigma_zero'],
    'exact_witness_s_1_2048':next(w for w in ex['witnesses'] if w['sigma']=='1/2048'),
    'quotient_grids':qsets,'quotient_MP_max_scaled_difference':mp.nstr(max(map(mp.mpf,q['precision_differences'])),30),
    'dense_grids':[{'grid':r['grid'],'inverse_order':r['inverse_order'],'radii':r['radii'],'angles':r['angles'],'maxima':r['summary']['all']} for r in d['rows']],
    'MP_point_count':len(mm['points']),'MP_precisions':[r['target_digits'] for r in m['rows']],
    'MP_working_precisions':[r['working_digits'] for r in m['rows']],
    'MP_max_scaled_difference':mp.nstr(max(mp.mpf(v) for r in m['precision_comparisons'] for v in r['scaled_absolute_differences'].values()),30),
    'MP_selected_maxima':peaks,
    'actual_exponent':mm['actual_exponent'],'far_linear_defect':mm['far_linear_defect'],
    'far_axis_amplitude':mm['far_vertical_leading_amplitude'],'far_axis_limit_R_Nf':mm['far_axis_limit_R_Nf'],
    'files':paths}
  rows.append(row)
now=datetime.now(timezone.utc).isoformat()
result={'completed_utc':now,'status':'CONFIRMED_FINITE_AUDIT','rows':rows,'manifest':manifest,'summary_code_sha256':sha(__file__),
 'verdicts':{'same_saved_data':'CONFIRMED','two_finite_densities_are_smooth_and_have_nonflat_h':'CONFIRMED','global_q_le_one_for_either_saved_formula':'REFUTED','either_saved_formula_is_exact_normalized_profile':'REFUTED','producer_finitewindow_q_extrema':'CONFIRMED','fixed_state_has_small_residual':'REFUTED','released_state_remains_in_a_lt_2D':'REFUTED','any_exact_low_slope_branch_is_absent':'OPEN','uniform_residual_bounds':'OPEN'},
 'scope':'Two frozen saved iterates only. Exact finite witness and exact center identities supplemented by empirical dense-grid and multiprecision convergence. No interval error enclosure or global residual supremum. No full YES/NO endpoint.'}
(root/'SUMMARY.json').write_text(json.dumps(result,indent=2)+'\n')
text=f'''# Independent audit of two low-slope saved iterates

Completed {now}. Result 145. Endpoint remains UNRESOLVED.

The source hashes, all diagnostics and computed quantities are in SUMMARY.json. The proof is ../PROOF.md, including the exact rational quotient witness. No numerics-lane evaluation or differentiation code is reused. The inverse is the verifier's canonical whole-plane density-moment inverse with complete exterior integrals. The polynomial density derivatives and canonical inverse are recomputed together in multiprecision. Previous manufactured gates for this inverse remain applicable; the new exact quotient gate passed 96 checks.

| Frozen state | ell | a | canonical c | Delta=ell+c-1 | a/(ell-1) |
| --- | ---: | ---: | ---: | ---: | ---: |
'''
for r in rows:
 text+=f"| {r['tag']} | {r['metadata']['cl']:.15g} | {float(r['a']):.15g} | {float(r['c']):.15g} | {float(r['delta']):.12g} | {float(r['a_over_D']):.12g} |\n"
text+='''
Both exact a Delta are nonzero. Thus neither stored formula satisfies the exact center transport condition. The fixed state has a small but nonzero slope and a large residual, which is consistent with the observed collapse but does not prove an actual limit. The released state leaves the intended a<2(ell-1) regime. Both formulas are smooth and rho-a y is nonflat. The sentence in NUM_REPORT (c22) saying the iterates meet none of the listed hypotheses was therefore reported as literally false. They fail the joint hypotheses needed for the cited conditional theorem.

| Frozen state | Canonical MP selected max |R|/N_f | Canonical MP selected max |R|/N_v | Point count | Largest scaled 75/110-digit difference |
| --- | ---: | ---: | ---: | ---: |
'''.replace('max |R|/','max abs(R)/')
for r in rows:
 text+=f"| {r['tag']} | {float(r['MP_selected_maxima']['R_Nf']['R_Nf']):.13g} | {float(r['MP_selected_maxima']['R_Nv']['R_Nv']):.13g} | {r['MP_point_count']} | {r['MP_max_scaled_difference']} |\n"
text+='''
The dense wide grid has 652 radii from 10^-160 to 10^250 and 373 quadrant angles, followed by two 129 by 161 local grids. Wide inverse orders are 128 and 256; local orders are 128, 192 and 256. Exact x-axis residual ratios are excluded by parity; positive denominators have no floor. Selected MP points include the extrema, origin and far regions, and quotient extrema. Working precisions are 322/357 digits for the fixed formula and 544/579 for the release, to handle cancellation in finite polynomial primitives. The finite observed precision agreement is not an error enclosure. At a fixed-state point all signed contributions attain the triangle upper bound abs(R)/N_f=1; tiny double-precision overshoots beyond 1 are roundoff. The maximum abs(R)/N_v is nearly 3, which is permitted because N_v groups the linear and advective terms differently.

The release NF maximizer lies at approximately (1.2117905e12, 4.1944661e11), with R=-4.1661117e6 and N_f=4.6235004e11. Its NV maximizer is approximately (1.2205279e12,3.9329818e11). A small absolute core residual does not control these distant points. Double-precision enormous far absolute residuals are not reported as reliable global bounds. The actual stored radial exponent is retained; asymptotic linear defects are about -2.96e-16 and +4.11e-17. In the near-affine release, the nonlinear term can still dominate that limiting defect at radius 10^250, so an asymptotic limiting ratio is not a bound on the sampled far values.

| Frozen state | Producer-window MP q minimum | Producer-window MP q maximum | Exact q(0,y)-1 at s=1/2048 | Approximate y |
| --- | ---: | ---: | ---: | ---: |
'''
for r in rows:
 q=r['quotient_grids'][0]['extrema'];w=r['exact_witness_s_1_2048']
 text+=f"| {r['tag']} | {float(q['min']['q_MP120']):.13g} | {float(q['max']['q_MP120']):.13g} | {w['q_minus_one']['approx']:.13g} | {w['approximate_y']:.13g} |\n"
text+='''
The producer-window grid has 400 logarithmic radii from 10^-4 to 10^6 and 128 angular midpoints. The independent quotient grid has 661 radii from 10^-100 to 10^250 and 293 angles including axes and narrow wedges. Its release maximum is 1.0000004471576936836 near (4.76e-20,1.50544e-14), independently stable at 80 and 120 digits. More decisively, the rational s=1/2048 witnesses prove global q<=1 false for both finite formulas without any floating-point radial inversion. Exact a>0 and e_core>0 give the same conclusion for every sufficiently small positive y. The producer-window q extrema themselves are reproduced. Absence of a violation in that window was never sufficient for a global bound.

CONFIRMED: frozen data, parities, smoothness, finite-window quotient extrema, exact near-origin quotient violations, canonical center defects and the finite numerical residual observations above. REFUTED: either formula is an exact normalized profile; either obeys global q<=1; the fixed state has a small residual; the released state remains in the low-slope regime. OPEN: any full-plane exact low-slope branch, uniform residual bounds, convergence of either family and the task's decisive YES/NO endpoint. Only these two snapshots were independently audited here, not the producer's full 24-run table.
'''
(root/'SUMMARY.md').write_text(text)
print(json.dumps({'completed_utc':now,'status':result['status'],'rows':len(rows),'files':len(manifest)},indent=2))
