"""Source-matched independent audit summary for the finite N36 refinement."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
import hashlib,json
import mpmath as mp

load=lambda p:json.loads(Path(p).read_text())
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
tag='common1000_moments_cl2.5_N36M32';source=Path('evidence/smooth_solver')/tag/'final.npz';h=sha(source)
paths={'solver':source.parent/'result.json','metadata':source.parent/'metadata.json','jets':Path('evidence/smooth_exact_jets')/tag/'jets.json','dense':Path('evidence/smooth_residual_grid')/tag/'diagnostic.json','charts':Path('evidence/complementary_charts')/tag/'diagnostic.json','MP':Path('evidence/smooth_mp_inverse')/tag/'diagnostic.json','MP_FD':Path('evidence/smooth_mp_inverse')/(tag+'_fdpoints')/'diagnostic.json','FD1':Path('evidence/smooth_evaluations')/(tag+'_dense_peaks')/'q1.json','FD2':Path('evidence/smooth_evaluations')/(tag+'_dense_peaks')/'q2.json','parity':Path('evidence/parity_axis_inverse')/(tag+'_smooth')/'diagnostic.json'}
d={k:load(v) for k,v in paths.items()}
for key in ['jets','MP','MP_FD']:assert d[key]['source_sha256']==h
for key in ['dense','charts','FD1','FD2','parity']:assert d[key]['sha256']==h
assert all(d[k].get('finished_utc') for k in ['solver','dense','charts','MP','MP_FD','FD1','FD2','parity'])
assert d['jets']['poisson_exact_zero'] and d['solver']['nfev']==1000 and d['solver']['solver_status']==0
assert d['metadata']['arguments']['inverse']=='density-moments'
assert d['metadata']['arguments']['seed_transfer']=='coefficients'
assert [r['digits']for r in d['MP']['rows']]==[75,110]
assert [r['digits']for r in d['MP_FD']['rows']]==[75,110]
assert all(r['working_digits'] in [193,228]for k in ['MP','MP_FD']for r in d[k]['rows'])

with mp.workdps(145):
 def short(x):return mp.nstr(x,40)
 def val(x):return mp.mpf(x)
 fields=['rho','psi','U1','U2','rho_x','rho_y','R','Nf','Nv','R_Nf','R_Nv']
 precision={};union={}
 for key in ['MP','MP_FD']:
  differences=[]
  for p,q in zip(d[key]['rows'][0]['points'],d[key]['rows'][1]['points']):
   assert (float(p['x']),float(p['y']))==(float(q['x']),float(q['y']))
   for f in fields:
    if p[f] is None or q[f] is None:assert p[f] is q[f];continue
    differences.append({'x':q['x'],'y':q['y'],'field':f,'scaled_difference':short(abs(val(p[f])-val(q[f]))/(1+abs(val(q[f]))))})
   union[(float(q['x']),float(q['y']))]=q
  precision[key]={'points':len(d[key]['rows'][1]['points']),'max_difference':max(differences,key=lambda r:val(r['scaled_difference'])),'comparisons':differences}
 peaks={f:max((p for p in union.values()if p[f] is not None),key=lambda p:val(p[f]))for f in ['R_Nf','R_Nv']}
 fdcompare={}
 for key in ['FD1','FD2']:
  rows=[]
  for p in d[key]['points']:
   q=union[p['x'],p['y']];r=p['residuals'][-1]
   x,y=val(q['x']),val(q['y']);g=[val(q[f])for f in ['rho_x','rho_y']];u=[val(q[f])for f in ['U1','U2']]
   uh=list(map(val,p['U']));gh=[val(r[f])for f in ['rho_x','rho_y']]
   du=[uh[i]-u[i]for i in range(2)];dg=[gh[i]-g[i]for i in range(2)];dr=val(p['rho'])-val(q['rho'])
   velterms=[du[i]*g[i]for i in range(2)];gradterms=[(val('2.5')*co+uh[i])*dg[i]for i,co in enumerate([x,y])]
   predicted=sum(velterms)+sum(gradterms)-dr
   observed=val(r['R'])-val(q['R'])
   arithmetic_defect=observed-predicted
   # Printed MP fields and roundoff in the final double residual addition.
   assert abs(arithmetic_defect)/(1+abs(val(q['rho'])))<mp.mpf('2e-15')
   row={'x':p['x'],'y':p['y'],'U_error':list(map(short,du)),'gradient_error':list(map(short,dg)), 'density_error':short(dr),'velocity_contributions':list(map(short,velterms)),'gradient_contributions':list(map(short,gradterms)),'observed_delta_R':short(observed),'predicted_delta_R':short(predicted),'arithmetic_defect':short(arithmetic_defect),'MP_R':q['R'],'FD_R':r['R']}
   for f in ['R_Nf','R_Nv']:
    if q[f] is None:row[f+'_error']=None;continue
    row[f+'_error']=short(val(r[f])-val(q[f]));row[f+'_step_range']=max(s[f]for s in p['residuals'])-min(s[f]for s in p['residuals'])
   rows.append(row)
  fdcompare[key]={'rows':rows,'max_ratio_errors':{f:max((r for r in rows if r[f+'_error'] is not None),key=lambda r:abs(val(r[f+'_error'])))for f in ['R_Nf','R_Nv']},'reported_maxima':d[key]['summary']['all']}
 cancellation=fdcompare['FD2']['max_ratio_errors']['R_Nf'];xy=(cancellation['x'],cancellation['y']);truth=union[xy]
 parity=[]
 for r in d['parity']['rows']:
  assert (r['x'],r['y'])==xy
  parity.append({'level':r['level'],'relative_h':r['interpolation']['relative_h'],'R':r['R'],'R_Nf':r['R_Nf'],'U2':r['U'][1],'U2_error':short(val(r['U'][1])-val(truth['U2'])),'R_Nf_error':short(val(r['R_Nf'])-val(truth['R_Nf'])),'weight_l1':r['interpolation']['weight_l1']})
 old=load('evidence/REFINEMENT_FOLLOWUPS.json')['smooth'];comparison=[]
 for row in old:
  assert sha(row['source'])==row['sha256']
  comparison.append({'tag':row['tag'],'a':row['a'],'R_Nf':row['dense_only']['R_Nf']['maximum'],'R_Nv':row['dense_only']['R_Nv']['maximum'],'source_sha256':row['sha256'],'evaluation':'own canonical dense-grid maxima (previously verified)'})
 baseline=next(row for row in comparison if row['tag']=='common1000_cl2.5_N32M28')
 anew=d['jets']['a_float'];nfnew=float(peaks['R_Nf']['R_Nf'])
 comparison.append({'tag':tag,'a':anew,'R_Nf':nfnew,'R_Nv':float(peaks['R_Nv']['R_Nv']),'source_sha256':h,'evaluation':'own canonical selected MP maxima after dense-grid search'})
 drift={'relative_slope_change_N32_to_N36':anew/baseline['a']-1,'relative_NF_change_N32_to_N36':nfnew/baseline['R_Nf']-1}
 jrows=[{'degree':r['degree'],'rho_coefficient_l1':r['rho']['coefficient_l1'],'rho_derivative_frobenius':r['rho']['derivative_frobenius'],'R_coefficient_l1':r['R']['coefficient_l1'],'R_derivative_frobenius':r['R']['derivative_frobenius']}for r in d['jets']['by_degree']]
now=datetime.now(timezone.utc).isoformat();out=Path('research/smooth_N36_refinement_audit/verification');out.mkdir(exist_ok=True)
result={'completed_utc':now,'status':'CONFIRMED_FINITE_AUDIT','source':str(source),'source_sha256':h,'solver':d['solver'],'solver_arguments':d['metadata']['arguments'],'point_count_training':d['metadata']['point_count'],'jacobian_FD_relative_error':d['metadata']['jacobian_FD_relative_error'],'exact_center':{k:d['jets'][k]for k in ['a_float','c_float','delta_float','poisson_exact_zero']},'jets_by_degree':jrows,'dense_rows':[{'grid':r['grid'],'order':r['inverse_order'],'radii':r['radii'],'angles':r['angles'],'summary':r['summary']}for r in d['dense']['rows']],'chart_rows':[{'order':r['order'],'points':len(r['points']),'summary':r['summary']}for r in d['charts']['rows']],'MP_precision':precision,'MP_selected_maxima':peaks,'MP_union_points':len(union),'FD_comparison':fdcompare,'near_axis_truth':truth,'near_axis_parity':parity,'refinement_comparison':comparison,'refinement_changes':drift,'actual_exponent_exact':d['MP']['rows'][-1]['effective_exponent_exact'],'far_leading_defect_exact':d['MP']['rows'][-1]['far_leading_defect_exact'],'far_sample':max(union.values(),key=lambda p:float(p['radius'])),'manifest':{str(p):sha(p)for p in [source,*paths.values()]},'proof_sha256':sha('research/smooth_N36_refinement_audit/PROOF.md'),'summary_code_sha256':sha(__file__),'verdicts':{'frozen_formula_and_gauge':'CONFIRMED','reported_finite_residuals':'CONFIRMED','raw_Cartesian_inverse_accurate_at_every_point':'REFUTED','near_axis_cancellation':'CONFIRMED','monotone_parity_stencil_convergence':'REFUTED','exact_saved_profile':'REFUTED','stationarity_and_continuum_convergence':'OPEN','uniform_residual_and_nearby_solution':'OPEN','full_primary_endpoint':'OPEN'}}
(out/'SUMMARY.json').write_text(json.dumps(result,indent=2)+'\n')
text=f'''# Independent N36 M32 refinement audit

Completed {now}. Result144. Endpoint UNRESOLVED.

Frozen source: {source}, SHA {h}. This is the verifier's separate smooth representation, solver and inverse implementation. The informal audit argument is ../PROOF.md; all numbers, point locations, hashes and precision comparisons are in SUMMARY.json. No numerical-lane evaluator is used.

The fixed ell=2.5 solve finished at {d['solver']['finished_utc']}, after {d['solver']['elapsed_seconds']:.3f} seconds and 1000 function evaluations. It stopped at the evaluation budget, not at demonstrated stationarity. It started from the same frozen N24 seed as the earlier common-budget sequence, using coefficient padding and projection onto c=1-ell and K=a. The new solve uses the independently gated density-moment inverse (order108) instead of the earlier Cartesian inverse matrix. This is therefore not a controlled comparison changing resolution alone. The analytic Jacobian directional finite-difference check was {d['metadata']['jacobian_FD_relative_error']:.6g}. The 4875 training points give max abs(R)/N_f=1.8274314e-7, cost=8.4924037e-12 and reported optimality=9.1234099e-6; none of those is a continuum bound.

The resulting a={anew:.15g}, c={d['jets']['c_float']:.15g}, K={d['solver']['K']:.15g}. Exact binary-coefficient arithmetic gives Delta={d['jets']['delta_float']:.15g} and nonzero a Delta, so this finite formula is not an exact profile. The stream satisfies its formal Poisson identity to the checked Taylor degree exactly; a fitted harmonic strain is not used. The physical cubic coefficients are b=-2.14142265412138 and e=-5.27978412071548, with L=1 and K/a approximately1.

| Common 1000-evaluation experiment | a | Observed canonical max abs(R)/N_f | Observed canonical max abs(R)/N_v |
| --- | ---: | ---: | ---: |
'''
for r in comparison:text+=f"| {r['tag']} | {r['a']:.12g} | {r['R_Nf']:.12g} | {r['R_Nv']:.12g} |\n"
text+=f'''
From N32 to N36 the slope changes by {100*drift['relative_slope_change_N32_to_N36']:.6f}% while the observed NF maximum decreases by {-100*drift['relative_NF_change_N32_to_N36']:.6f}%. These finite changes do not settle a limiting value or prove a branch. The table uses the previous own dense canonical searches and the current selected MP check of its dense search, not uniform suprema.

The complementary-chart check has 650 actual points at inverse orders64/128/192. Its NF maximum9.42743e-8 misses the denser search's larger maximum. The dense check uses652 radii from10^-160 to10^250 and373 angles at orders128/256, plus one129 by161 local refinement at orders128/192/256. The MP check covers11 initially selected points and the16 Cartesian-check points, {len(union)} distinct points total, at75/110 target digits and193/228 working digits. The largest scaled precision differences are3.16e-75 and3.64e-75. Canonical selected maxima are

    abs(R)/N_f = {peaks['R_Nf']['R_Nf'][:28]}, at (0,0.758632161037305),
    abs(R)/N_v = {peaks['R_Nv']['R_Nv'][:28]}, at (0,0.760681974293331).

At the NF point R=6.0987940e-6, N_f=31.0264015 and N_v=44.5769391. The finite local-grid absolute maximum is6.1157948e-6. Far absolute maxima in double precision are not claimed reliable. At a radius near10^250 the MP absolute residual is about1.44628e85, despite small normalized ratios; the exact saved exponent has ell*p_saved-1=1/18014398509481984. That arithmetic defect is retained, not silently corrected to the rational exponent2/5.

The Cartesian whole-plane kernel and FD8 check uses16 points, inverse configurations(40,256,144,4) and(64,512,224,8), and three derivative steps0.003/0.0015/0.00075. Away from the identified cancellation witness, the largest absolute NF discrepancy against MP is1.40e-12 at level1 and1.13e-12 at level2. At (0.008009861376660828,3.717848312496212e-8), however, level2 gives NF=1.234053656e-8 whereas MP gives9.013258480e-13. The FD steps change NF by only1.83e-13. The velocity discrepancy dU2=9.17567e-16, multiplied by rho_y about22.79316, explains the erroneous residual; the separate density/derivative contributions and the exact algebraic decomposition are recorded in SUMMARY.json. Refining this direct quadrature worsens cancellation at that point, so a blanket claim of Cartesian accuracy would be false.

Parity interpolation of U2/y, using only direct-kernel samples before MP comparison, reduces the error at two of the level2 stencils: h/x=0.008 and0.004 yield NF4.14e-12 and4.62e-12. At h/x=0.002 it deteriorates to1.33e-10. All results are retained. This supports a cancellation diagnosis but does not supply a certified stencil error or monotone convergence. The independent MP primitive remains the precise finite-point check. No denominator floor is used.

| Taylor degree | Sum of absolute R coefficients | Frobenius norm of the derivative tensor of R at0 | Corresponding rho norm |
| --- | ---: | ---: | ---: |
'''
for r in jrows:text+=f"| {r['degree']} | {r['R_coefficient_l1']:.9g} | {r['R_derivative_frobenius']:.9g} | {r['rho_derivative_frobenius']:.9g} |\n"
text+='''
These exact-jet-derived norms show that a small value residual does not control high derivatives at the center. They do not prove a singular limiting profile. The finite formulas are smooth, symmetric and nonzero; their canonical full-plane inverses include the exterior tails. What remains OPEN is stationarity, convergence with stable center and far-field data, uniform control of the residual and approximation error, and a nearby exact solution. The prompt's decisive YES/NO conditions are not met.
'''
(out/'SUMMARY.md').write_text(text)
print(json.dumps({'completed_utc':now,'status':result['status'],'source_sha256':h,'MP_union_points':len(union),'refinement_changes':drift},indent=2))
