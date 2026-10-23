from pathlib import Path
from datetime import datetime,timezone
import json,math,hashlib
now=datetime.now(timezone.utc).isoformat()
def load(p):return json.loads(Path(p).read_text())
def best(rows,region,key):
 choices=[r['summary'][region][key] for r in rows if region in r['summary'] and key in r['summary'][region]]
 return max(choices,key=lambda v:v['maximum']) if choices else None
def diff_points(a,b,key):
 aa={(v['x'],v['y']):v for v in a};bb={(v['x'],v['y']):v for v in b};rows=[]
 for xy in aa.keys()&bb.keys():
  if xy[1]==0:continue
  av,bv=aa[xy].get(key),bb[xy].get(key)
  if av is not None and bv is not None and math.isfinite(av) and math.isfinite(bv):rows.append(dict(difference=abs(av-bv),x=xy[0],y=xy[1],first=av,second=bv))
 return max(rows,key=lambda v:v['difference']) if rows else None
qs=[]
for tag in ['QFIXF11_N64','QFIXF11_N96','QFIXF12_N64','QFIXF12_N96','QFIXF12_N128','QFREEF_REF2_N96']:
 base=Path('evidence/q_residual_grid')/tag;d=load(base/'diagnostic.json');rows=[r for r in d['rows'] if r['inverse_order']==256]
 result=dict(tag=tag,source=d['source'],sha256=d['sha256'],ell=d['ell'],a=d['a'],delta=d['delta'],regions={})
 for region in ['all','origin','core','middle','far','extent_2','extent_4','extent_8','extent_12','extent_50','extent_250']:
  result['regions'][region]={k:best(rows,region,k) for k in ['abs_R','R_Nf','R_Nv']}
 mp=load(Path('evidence/complementary_mp')/(tag+'_dense_peaks')/'diagnostic.json');mprows=mp['rows']
 ma=[dict(x=p['x'],y=p['y'],**{k:float(p['comparisons'][-1]['variants']['binary_ell'][k]) for k in ['R_Nf','R_Nv']}) for p in mprows[0]['points']]
 mb=[dict(x=p['x'],y=p['y'],**{k:float(p['comparisons'][-1]['variants']['binary_ell'][k]) for k in ['R_Nf','R_Nv']}) for p in mprows[-1]['points']]
 result['mp70_110_ratio_difference']={k:diff_points(ma,mb,k) for k in ['R_Nf','R_Nv']}
 # These are high precision density calculations with double precision canonical velocity.
 result['mp_density_scope']='70/110-digit density and differentiation; inverse still the independently refined double-precision canonical quadrature. Not a fully multiprecision inverse.'
 result['mp_binary_leading_defect']=mprows[-1]['binary_leading_defect']
 result['mp_max_gradient_discrepancy']=max(float(c['relative_gradient_difference']) for p in mprows[-1]['points'] for c in p['comparisons'])
 result['mp_peak_order_change']={k:max(abs(float(p['comparisons'][-1]['variants']['binary_ell'][k])-float(p['comparisons'][-2]['variants']['binary_ell'][k])) for p in mprows[-1]['points']) for k in ['R_Nf','R_Nv']}
 chart=load(Path('evidence/complementary_charts')/(tag+'_dense_peaks')/'diagnostic.json')['rows'][-1]['points']
 fdrecords=[]
 for level in [1,2]:
  path=Path('evidence/q_evaluations')/(tag+'_dense_peaks')/f'q{level}.json'
  if not path.exists():continue
  fd=load(path)
  if not fd.get('finished_utc'):continue
  pts=[dict(x=p['x'],y=p['y'],**p['residuals'][-1]) for p in fd['points']]
  result[f'FD{level}_versus_chart']={k:diff_points(pts,chart,k) for k in ['R_Nf','R_Nv']}
  prev=[dict(x=p['x'],y=p['y'],**p['residuals'][-2]) for p in fd['points']]
  result[f'FD{level}_step_difference']={k:diff_points(prev,pts,k) for k in ['R_Nf','R_Nv']}
  fdrecords.append((level,pts))
 if len(fdrecords)==2:result['FD_inverse_level_difference']={k:diff_points(fdrecords[0][1],fdrecords[1][1],k) for k in ['R_Nf','R_Nv']}
 qs.append(result)
smooth=[]
for n,m in [(20,16),(24,20),(28,24),(32,28),(36,32)]:
 tag=f'common1000_cl2.5_N{n}M{m}';base=Path('evidence/smooth_solver')/tag;chart=Path('evidence/complementary_charts')/tag/'diagnostic.json'
 if not chart.exists():continue
 d=load(chart);r=load(base/'result.json');last=d['rows'][-1];pre=d['rows'][-2]
 s=dict(tag=tag,source=d['source'],sha256=d['sha256'],ell=d['ell'],a=d['a'],delta=d['delta'],summary=last['summary'],inverse_order=last['order'],point_count=len(last['points']),inverse_change={k:diff_points(pre['points'],last['points'],k)for k in ['R_Nf','R_Nv']},solver_result={k:v for k,v in r.items() if len(str(v))<1500})
 smooth.append(s)
output=dict(utc=now,Q=qs,smooth_common_ceiling=smooth,scope='Finite sampled comparisons. No uniform residual certificate, parameter convergence, nearby-profile result, or endpoint verdict.')
Path('evidence/DENSE_CHECKS.json').write_text(json.dumps(output,indent=2)+'\n')
lines=['# Independent dense residual checks','',now,'','Q densities were reconstructed solely from frozen coefficient data. The grid uses652 log radii and373 angles, including the axes, offset angular nodes and near-axis points. The log grid spans1e-160 to1e250; the dense main range is about1e-12 to1e12. Separate129-by161 local grids refine both ratio maxima. The canonical full-plane inverse is evaluated at orders128 and256 on the wide grid and128,192,256 locally. Exact horizontal-axis ratios are undefined and omitted; positive denominators are not floored.','', '| state | ell | a | max R/Nf | max R/Nv | x at R/Nf | y at R/Nf | Nf there | Nv there | absR there |','|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|']
for s in qs:
 p=s['regions']['all']['R_Nf'];v=s['regions']['all']['R_Nv']
 lines.append('| '+s['tag']+' | '+' | '.join(f'{x:.12g}' for x in [s['ell'],s['a'],p['maximum'],v['maximum'],p['x'],p['y'],p['Nf'],p['Nv'],p['maximum']*p['Nf']])+' |')
lines+=['','Each entry is the maximum of the saved wide and local grids at inverse order256. The tables do not establish maxima over the plane. Regional absolute maxima and their coordinates, and cumulative domain extents1e2,1e4,1e8,1e12,1e50,1e250, are in DENSE_CHECKS.json. Extreme far-field absolute values come from subtraction of large terms in double precision and require interpretation using the recorded leading exponent defect; their final digits are not certified.','', '| state | peak inverse192-to256 ratio change | MP density derivative relative discrepancy | FD2 versus angular R/Nf | FD1-toFD2 R/Nf |','|---|---:|---:|---:|---:|']
for s in qs:
 vals=[f"{s['mp_peak_order_change']['R_Nf']:.6g}",f"{s['mp_max_gradient_discrepancy']:.6g}"]
 for key in ['FD2_versus_chart','FD_inverse_level_difference']:
  val=s.get(key,{}).get('R_Nf');vals.append(f"{val['difference']:.6g}" if val else 'pending')
 lines.append('| '+s['tag']+' | '+' | '.join(vals)+' |')
lines+=['','MP means70/110-digit density and derivatives with the independently computed double precision velocity. It does not mean a70-digit Poisson inverse. FD8 uses a separately implemented Cartesian cancellation integral with exterior continuation and three differentiation steps. The point lists used by each comparison are retained.','', '## Common-ceiling smooth-basis controls','', 'All three original controls use the same frozen N24 seed, fixedell2.5, common jet scale368.7801401458402, the same stopping tolerances, and a1000 function-evaluation ceiling. Actual consumed evaluations differ and all original three stop onxtol. Fixingell is a search restriction, not a use of scaling freedom.','', '| basis | a | maxabsR | max R/Nf | max R/Nv | inverse128-to192 R/Nf change |','|---|---:|---:|---:|---:|---:|']
for s in smooth:
 row=s['summary']['all'];lines.append('| '+s['tag']+' | '+' | '.join(f'{x:.12g}' for x in [s['a'],row['abs_R']['maximum'],row['R_Nf']['maximum'],row['R_Nv']['maximum'],s['inverse_change']['R_Nf']['difference']])+' |')
lines+=['','These705 independent points give a systematic residual decrease under basis refinement with controlled optimizer ceiling, while the invariant origin slope still drifts. They do not show convergence to a single primary profile. The denser common grids and independent Cartesian FD peak checks are now in REFINEMENT_FOLLOWUPS.md/json; their union retains larger coarse-grid peaks. The32/28 and36/32 controls are in progress or queued. Raw near-axis FD discrepancies remain in this table; the parity-based direct-inverse checks in that supplement distinguish cancellation from a residual defect at selected points. The coarse absolute maximum is near(0,.8924073481); ratio maxima are near(0,.7003092822), except theN24 Nv maximum. JSON retains exact sampled coordinates and both denominators.','', 'Verdicts: computed finite-grid results CONFIRMED; uniform bounds, limiting slope, smooth profile existence and decisive YES remain OPEN.']
Path('evidence/DENSE_CHECKS.md').write_text('\n'.join(lines)+'\n')
print('\n'.join(lines[:18]));print('MP/FD')
for s in qs:print(s['tag'],s['mp_peak_order_change'],s.get('FD2_versus_chart'))
