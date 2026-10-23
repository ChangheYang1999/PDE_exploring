from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
import json,hashlib
import mpmath as mp
load=lambda p:json.loads(Path(p).read_text())
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
tag='common1000_moments_cl2.5_N44M40';source=Path('evidence/smooth_solver')/tag/'final.npz';h=sha(source)
paths={k:Path(v)for k,v in {'solver':f'evidence/smooth_solver/{tag}/result.json','metadata':f'evidence/smooth_solver/{tag}/metadata.json','jets':f'evidence/smooth_exact_jets/{tag}/jets.json','input':f'evidence/smooth_exact_jets/{tag}/exact_input.json','dense':f'evidence/smooth_residual_grid/{tag}/diagnostic.json','charts':f'evidence/complementary_charts/{tag}/diagnostic.json','MP':f'evidence/smooth_mp_inverse/{tag}/diagnostic.json','MP_FD':f'evidence/smooth_mp_inverse/{tag}_fdpoints/diagnostic.json','FD1':f'evidence/smooth_evaluations/{tag}_dense_peaks/q1.json','FD2':f'evidence/smooth_evaluations/{tag}_dense_peaks/q2.json'}.items()}
d={k:load(v)for k,v in paths.items()}
for k in ['jets','input','MP','MP_FD']:assert d[k]['source_sha256']==h
for k in ['dense','charts','FD1','FD2']:assert d[k]['sha256']==h
for k in ['solver','dense','charts','MP','MP_FD','FD1','FD2']:assert d[k]['finished_utc']
assert d['jets']['poisson_exact_zero'] and d['solver']['nfev']==1000 and d['solver']['solver_status']==0
meta=d['metadata']['arguments'];old=load('research/smooth_N40_refinement_audit/verification/SUMMARY.json');oldargs=old['solver_arguments']
assert sha(old['source'])==old['source_sha256']
changing={'radial','angular','tag'}
assert set(meta)==set(oldargs) and all(meta[k]==oldargs[k]for k in meta if k not in changing)
assert meta['radial']==44 and meta['angular']==40
frac=lambda x:F(int(x['numerator']),int(x['denominator']))
co=[[frac(x)for x in row]for row in d['input']['chebyshev_coefficients']]
a=sum(((-1)**j*v for j,v in enumerate(co[0])),F(0));K=sum(((-1)**k*sum(row,F(0))for k,row in enumerate(co)),F(0));assert a==frac(d['jets']['a'])
with mp.workdps(150):
 val=mp.mpf;short=lambda x:mp.nstr(x,42)
 precision={};union={}
 for key in ['MP','MP_FD']:
  assert [r['digits']for r in d[key]['rows']]==[75,110]
  assert [r['working_digits']for r in d[key]['rows']]==[75+50+meta['radial']+meta['angular'],110+50+meta['radial']+meta['angular']]
  diffs=[]
  assert len(d[key]['rows'][0]['points'])==len(d[key]['rows'][1]['points'])
  for lo,hi in zip(*[r['points']for r in d[key]['rows']]):
   assert (float(lo['x']),float(lo['y']))==(float(hi['x']),float(hi['y']))
   for f in ['rho','psi','U1','U2','rho_x','rho_y','R','Nf','Nv','R_Nf','R_Nv']:
    if lo[f]is None or hi[f]is None:assert lo[f]is hi[f];continue
    diffs.append(dict(x=hi['x'],y=hi['y'],field=f,scaled_difference=short(abs(val(lo[f])-val(hi[f]))/(1+abs(val(hi[f]))))))
   union[float(hi['x']),float(hi['y'])]=hi
  precision[key]=dict(points=len(d[key]['rows'][-1]['points']),max_difference=max(diffs,key=lambda r:val(r['scaled_difference'])),comparisons=diffs)
 peaks={f:max((p for p in union.values()if p[f]is not None),key=lambda p:val(p[f]))for f in ['R_Nf','R_Nv']}
 fd={}
 for key in ['FD1','FD2']:
  rows=[]
  for p in d[key]['points']:
   q=union[p['x'],p['y']];r=p['residuals'][-1];g=[val(q[f])for f in ['rho_x','rho_y']];u=[val(q[f])for f in ['U1','U2']]
   uh=list(map(val,p['U']));gh=[val(r[f])for f in ['rho_x','rho_y']];du=[uh[i]-u[i]for i in range(2)];dg=[gh[i]-g[i]for i in range(2)];dr=val(p['rho'])-val(q['rho'])
   vt=[du[i]*g[i]for i in range(2)];gt=[(val('2.5')*val(q[f])+uh[i])*dg[i]for i,f in enumerate(['x','y'])];pred=sum(vt)+sum(gt)-dr;obs=val(r['R'])-val(q['R']);err=obs-pred
   assert abs(err)/(1+abs(val(q['rho'])))<val('2e-15')
   row=dict(x=p['x'],y=p['y'],U_error=list(map(short,du)),gradient_error=list(map(short,dg)),density_error=short(dr),velocity_contributions=list(map(short,vt)),gradient_contributions=list(map(short,gt)),observed_delta_R=short(obs),predicted_delta_R=short(pred),arithmetic_defect=short(err),MP_R=q['R'],FD_R=r['R'],MP_R_Nf=q['R_Nf'],FD_R_Nf=r['R_Nf'])
   for f in ['R_Nf','R_Nv']:
    row[f+'_error']=None if q[f]is None else short(val(r[f])-val(q[f]));row[f+'_step_range']=None if q[f]is None else max(s[f]for s in p['residuals'])-min(s[f]for s in p['residuals'])
   rows.append(row)
  fd[key]=dict(rows=rows,max_ratio_errors={f:max((r for r in rows if r[f+'_error']is not None),key=lambda r:abs(val(r[f+'_error'])))for f in ['R_Nf','R_Nv']})
 changes=dict(relative_a=float(a)/old['exact_center']['a']-1,relative_NF=float(peaks['R_Nf']['R_Nf'])/float(old['MP_selected_maxima']['R_Nf']['R_Nf'])-1,relative_NV=float(peaks['R_Nv']['R_Nv'])/float(old['MP_selected_maxima']['R_Nv']['R_Nv'])-1)
 center=dict(a_exact=str(a),K_exact=str(K),K_minus_a_exact=str(K-a),K_minus_a=float(K-a),a=float(a),c=d['jets']['c_float'],Delta=d['jets']['delta_float'],Delta_exact=str(frac(d['jets']['delta'])),L_axis=short((val(K.numerator)/K.denominator/(val(a.numerator)/a.denominator))**(1/(2*val(frac(d['input']['alpha']).numerator)/frac(d['input']['alpha']).denominator))))
 far=max(union.values(),key=lambda p:val(p['radius']))
fixed_old=Path('evidence/smooth_residual_grid/common1000_moments_cl2.5_N40M36/base_grid.json')
fixed_new=Path('evidence/smooth_residual_grid')/tag/'base_grid.json'
assert fixed_old.read_bytes()==fixed_new.read_bytes()
assert d['dense']['fixed_reference']['tag']=='common1000_moments_cl2.5_N40M36'
assert {r['grid']for r in d['dense']['rows']} >= {'wide','reference_local_R_Nf'}
now=datetime.now(timezone.utc).isoformat();out=Path('research/smooth_N44_refinement_audit/verification')
result=dict(completed_utc=now,status='CONFIRMED_FINITE_AUDIT',source=str(source),source_sha256=h,solver=d['solver'],solver_arguments=meta,point_count_training=d['metadata']['point_count'],jacobian_FD_relative_error=d['metadata']['jacobian_FD_relative_error'],exact_center=center,jets_by_degree=d['jets']['by_degree'],MP_precision=precision,MP_union_points=len(union),MP_selected_maxima=peaks,FD_comparison=fd,comparison_N40=dict(source=old['source'],sha256=old['source_sha256'],exact_center=old['exact_center'],maxima=old['MP_selected_maxima']),refinement_changes=changes,dense_rows=[{k:r[k]for k in ['grid','inverse_order','radii','angles','summary']}for r in d['dense']['rows']],chart_rows=[dict(order=r['order'],points=len(r['points']),summary=r['summary'])for r in d['charts']['rows']],far_sample=far,actual_exponent_exact=d['MP']['rows'][-1]['effective_exponent_exact'],far_leading_defect_exact=d['MP']['rows'][-1]['far_leading_defect_exact'],proof_sha256=sha('research/smooth_N44_refinement_audit/PROOF.md'),code_sha256=sha(__file__),manifest={str(p):sha(p)for p in [source,*paths.values()]},verdicts=dict(finite_formula_gauge_and_values='CONFIRMED',exact_saved_profile='REFUTED',stationarity='OPEN',continuum_convergence='OPEN',primary_endpoint='OPEN'))
(out/'SUMMARY.json').write_text(json.dumps(result,indent=2)+'\n')
num=lambda x:f'{float(x):.12g}'
text=f'''# Independent N44 M40 finite audit

Completed {now}. Result192. Endpoint UNRESOLVED.

Frozen source {source}, SHA {h}. Exact formula and audit argument: ../PROOF.md. The verifier's own basis, solver, full-plane inverse and independent MP primitives are used. The literal saved exponent is retained. All input hashes and pointwise values are in SUMMARY.json.

The solve used the same N24 seed, inverse order108, coefficient transfer, jet scale and1000-evaluation budget as N40. Only radial/angular sizes, their prescribed training grid and output tag differ in the arguments. It stopped at the evaluation budget after {d['solver']['elapsed_seconds']:.3f} seconds, with optimality {num(d['solver']['optimality'])}, cost {num(d['solver']['cost'])}, {d['metadata']['point_count']} training points and training NF {num(d['solver']['max_training_R_Nf'])}. Its directional Jacobian check is {num(d['metadata']['jacobian_FD_relative_error'])}. These do not establish stationarity.

| Finite approximation | a | Selected canonical max abs(R)/N_f | Selected canonical max abs(R)/N_v |
| --- | ---: | ---: | ---: |
| N40 M36 | {num(old['exact_center']['a'])} | {num(old['MP_selected_maxima']['R_Nf']['R_Nf'])} | {num(old['MP_selected_maxima']['R_Nv']['R_Nv'])} |
| N44 M40 | {num(a)} | {num(peaks['R_Nf']['R_Nf'])} | {num(peaks['R_Nv']['R_Nv'])} |

Slope change {100*changes['relative_a']:.6f}%, observed NF change {100*changes['relative_NF']:.6f}%. This controlled finite comparison gives no limiting slope. The MP NF maximum is at ({peaks['R_Nf']['x']},{peaks['R_Nf']['y']}), R={num(peaks['R_Nf']['R'])}, Nf={num(peaks['R_Nf']['Nf'])}, Nv={num(peaks['R_Nf']['Nv'])}. The NV maximum is at ({peaks['R_Nv']['x']},{peaks['R_Nv']['y']}). These are observed selected maxima, not a uniform supremum.

Exact binary arithmetic gives c={center['c']:.17g}, Delta=ell+c-1={center['Delta']:.17g}, K-a={center['K_minus_a']:.17g}, L_axis={center['L_axis']}. The nonzero exact a*Delta disproves exact transport for this particular finite formula. Cubic b={num(d['solver']['b'])}, e={num(d['solver']['e'])}. The formal Poisson identity to the audited Taylor degree11 is exact. No fitted harmonic strain is added.

The wide grid has652 radii, log10(r) from-160 to250, and373 angles at inverse orders128/256. Local refinement includes the unchanged N40 physical rectangles and additional rectangles centered on N44 wide-grid peaks, each with129 radii by161 angles at orders128/192/256. The complementary chart has650 points at orders64/128/192. Two independent MP checks use{len(union)} distinct points at75/110 target digits and209/244 base working digits, with further radius-dependent guard precision. Their largest scaled precision differences are {precision['MP']['max_difference']['scaled_difference']} and {precision['MP_FD']['max_difference']['scaled_difference']}.

The independent Cartesian kernel/FD8 check uses{len(d['FD1']['points'])} points, two inverse configurations and three derivative steps. Every residual discrepancy is decomposed into velocity, gradient and density contributions in SUMMARY.json. The largest NF discrepancies are:

'''
for key in ['FD1','FD2']:
 r=fd[key]['max_ratio_errors']['R_Nf'];text+=f"- {key}: at ({r['x']},{r['y']}), FD NF={num(r['FD_R_Nf'])}, MP NF={num(r['MP_R_Nf'])}, difference {r['R_Nf_error']}, step range {num(r['R_Nf_step_range'])}; dU2={r['U_error'][1]}.\n"
text+=f'''
These independent estimates must be assessed at their actual cancellation scale; agreement between derivative steps alone does not certify velocity accuracy. A separate parity interpolation audit at the two unchanged N40 witnesses is recorded in verification/parity/AUDIT.json; its raw and corrected values remain separately visible.

At radius {far['radius']}, MP abs(R)={far['abs_R']} and NF={far['R_Nf']}. The exact multiplier ell*p_saved-1={result['far_leading_defect_exact']} explains its leading growth. This is a retained artifact of the literal exponent. Separately defined exact-exponent fields are the subject of result164; this audit does not silently replace the exponent or infer a mathematical obstruction from its rounding.

| Taylor degree | R coefficient l1 norm | R derivative tensor Frobenius norm | rho derivative tensor Frobenius norm |
| --- | ---: | ---: | ---: |
'''
for r in d['jets']['by_degree']:text+=f"| {r['degree']} | {num(r['R']['coefficient_l1'])} | {num(r['R']['derivative_frobenius'])} | {num(r['rho']['derivative_frobenius'])} |\n"
text+='''
CONFIRMED: these finite formula, gauge and residual calculations. REFUTED: exactness of the literal finite field. OPEN: solver stationarity, continuum convergence with stable center/far data, and either decisive endpoint. High derivative residuals alone prove no singular limiting profile. A rigorous uniform certificate would be stronger evidence but is not imposed here as an extra condition on the prompt's numerical YES route. The current finite sequence does not establish the requested convergence checks.
'''
(out/'SUMMARY.md').write_text(text)
print(json.dumps({k:result[k]for k in ['completed_utc','source_sha256','exact_center','MP_union_points','refinement_changes']},indent=2))
