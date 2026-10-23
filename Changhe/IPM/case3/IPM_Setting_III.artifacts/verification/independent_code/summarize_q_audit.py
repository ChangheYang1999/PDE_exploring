"""Summarize retained independent quadrature and derivative evidence, without recomputation."""
from pathlib import Path
from datetime import datetime,timezone
import argparse,json,math,hashlib

p=argparse.ArgumentParser();p.add_argument('tag');p.add_argument('--mp-tag');a=p.parse_args()
base=Path('evidence/q_evaluations')/a.tag
levels=[json.loads((base/f'q{k}.json').read_text()) for k in range(3)]
identity=levels[0]['metadata']['sha256']
assert all(v['metadata']['sha256']==identity for v in levels)
assert all(v.get('finished_utc') for v in levels)

def finite(value):
    if isinstance(value,float):return math.isfinite(value)
    if isinstance(value,dict):return all(finite(v) for v in value.values())
    if isinstance(value,list):return all(finite(v) for v in value)
    return True
assert all(finite(v) for v in levels)

def keyed(v):return {(row['x'],row['y']):row for row in v['points']}
by=[keyed(v) for v in levels];assert all(set(v)==set(by[0]) for v in by)
comparisons=[]
for lo,hi in [(0,1),(1,2)]:
    rows=[]
    for xy,q in by[hi].items():
        old=by[lo][xy];rr=q['residuals'][-1];oo=old['residuals'][-1]
        if xy[1]==0:continue
        rec={'x':xy[0],'y':xy[1],'R_Nf_difference':abs(rr['R_Nf']-oo['R_Nf']),'R_Nv_difference':abs(rr['R_Nv']-oo['R_Nv']),'U_relative_difference':math.hypot(*(u-v for u,v in zip(q['U'],old['U'])))/max(math.hypot(*q['U']),1e-300)}
        rows.append(rec)
    comparisons.append({'levels':[lo,hi],**{k:max(rows,key=lambda r:r[k]) for k in ['R_Nf_difference','R_Nv_difference','U_relative_difference']}})
finest=levels[-1]
fd=[]
for q in finest['points']:
    if q['y']==0:continue
    for key in ['R_Nf','R_Nv']:
        values=[r[key] for r in q['residuals']]
        fd.append({'metric':key,'x':q['x'],'y':q['y'],'spread':max(values)-min(values)})
out={'utc':datetime.now(timezone.utc).isoformat(),'tag':a.tag,'sha256_state':identity,'method':'Aggregation of previously computed independent full-plane kernel, FD8 and optional MP analytic-derivative data; no producer residual imported.','metadata':finest['metadata'],'center_and_tail':finest['center_and_tail'],'all_numeric_values_finite':True,'level_summaries':[{'level':k,'finished_utc':d['finished_utc'],'summary':d['summary']} for k,d in enumerate(levels)],'quadrature_comparisons':comparisons,'FD8_spreads':{key:max((r for r in fd if r['metric']==key),key=lambda r:r['spread']) for key in ['R_Nf','R_Nv']},'scope':'Sampled finite-interpolant results. Quadrature and FD sensitivity are not rigorous global upper bounds or interval enclosures.'}
if a.mp_tag:
    pp=Path('research/finite_q_far_coefficients/verification')/(a.mp_tag+'.json');mp=json.loads(pp.read_text());rows=mp['full_far_derivative_comparisons'];assert mp['status']=='PASS' and rows
    out['mp_derivative_audit']={'source':str(pp),'sha256_source':hashlib.sha256(pp.read_bytes()).hexdigest(),'precision_digits':mp['precision_digits'],'point_count':len(rows),'maxima':{key:max(rows,key=lambda r:float(r[key])) for key in ['mp_abs_R','mp_R_Nf','mp_R_Nv','FD8_relative_gradient_error','relative_density_difference']},'axis_angular_row':mp['angular_rows'][-1],'ell_p_minus1':mp['ell_p_minus1'],'scope':'Arbitrary precision density and derivatives; existing independent double-precision canonical velocity. This is not a multiprecision inverse.'}
(base/'comparison.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'tag':a.tag,'center':out['center_and_tail'],'all':finest['summary']['all'],'pair12':comparisons[-1],'mp':out.get('mp_derivative_audit')},indent=2))
