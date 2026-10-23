"""Read-only aggregation of independent sampled evaluations; no computation backend."""
from pathlib import Path
from datetime import datetime, timezone
import json, math, hashlib

def load(p):return json.loads(Path(p).read_text())
def samepoints(a,b,quantity):
    aa={(p['x'],p['y']):p for p in a};bb={(p['x'],p['y']):p for p in b};out=[]
    for xy in aa.keys()&bb.keys():
        if xy[1]==0:continue
        av,bv=aa[xy].get(quantity),bb[xy].get(quantity)
        if av is not None and bv is not None and math.isfinite(av) and math.isfinite(bv):
            out.append(dict(x=xy[0],y=xy[1],difference=abs(av-bv),first=av,second=bv))
    return max(out,key=lambda p:p['difference'])if out else None

def winner(records,key):
    available=[dict(p[key],sample_set=label)for label,p in records if key in p]
    return max(available,key=lambda p:p['maximum'])if available else None

now=datetime.now(timezone.utc).isoformat();result=dict(utc=now,smooth=[],parity=[])
for n,m in [(20,16),(24,20),(28,24),(32,28),(36,32)]:
    tag=f'common1000_cl2.5_N{n}M{m}'
    dense=Path('evidence/smooth_residual_grid')/tag/'diagnostic.json'
    coarse=Path('evidence/complementary_charts')/tag/'diagnostic.json'
    if not dense.exists()or not coarse.exists():continue
    d,c=load(dense),load(coarse)
    if not d.get('finished_utc'):continue
    samples=[(f"dense_{r['grid']}_order256",r['summary']['all'])for r in d['rows']if r['inverse_order']==256]
    samples.append(('coarse705_order192',c['rows'][-1]['summary']['all']))
    extra=Path('evidence/smooth_coarse_peak_refinement')/tag/'diagnostic.json'
    if extra.exists():
        e=load(extra)
        if e.get('finished_utc'):
            samples.extend((f"coarse_refined_{r['grid']}_order256",r['summary']['all'])for r in e['rows']if r['inverse_order']==256)
    rec=dict(tag=tag,source=d['source'],sha256=d['sha256'],ell=d['ell'],a=d['a'],c=d['c'],delta=d['delta'],coarse705=c['rows'][-1]['summary']['all'],dense_only={q:winner(samples[:-1]if not extra.exists()else [(l,p)for l,p in samples if l!='coarse705_order192'],q)for q in ['abs_R','R_Nf','R_Nv']},union={q:winner(samples,q)for q in ['abs_R','R_Nf','R_Nv']},FD={})
    pts=load(Path('evidence/complementary_charts')/(tag+'_dense_peaks')/'diagnostic.json')['rows'][-1]['points']
    fdsets=[]
    for level in [1,2]:
        path=Path('evidence/smooth_evaluations')/(tag+'_dense_peaks')/f'q{level}.json'
        if not path.exists():continue
        f=load(path)
        if not f.get('finished_utc'):continue
        fp=[dict(x=p['x'],y=p['y'],**p['residuals'][-1])for p in f['points']]
        prev=[dict(x=p['x'],y=p['y'],**p['residuals'][-2])for p in f['points']]
        rec['FD'][f'level{level}_versus_angular']={q:samepoints(fp,pts,q)for q in ['R_Nf','R_Nv']}
        rec['FD'][f'level{level}_step_change']={q:samepoints(fp,prev,q)for q in ['R_Nf','R_Nv']}
        fdsets.append(fp)
    if len(fdsets)==2:rec['FD']['inverse_level_change']={q:samepoints(*fdsets,q)for q in ['R_Nf','R_Nv']}
    rec['regional_dense']={reg:{q:winner([(r['grid'],r['summary'][reg])for r in d['rows']if r['inverse_order']==256 and reg in r['summary']],q)for q in ['abs_R','R_Nf','R_Nv']}for reg in ['origin','core','middle','far','extent_2','extent_4','extent_8','extent_12','extent_50','extent_250']}
    result['smooth'].append(rec)
for tag in ['QFIXF12_N128','QFIXF12_N96','QFIXF11_N96_fd_worst','QFIXF12_N64_fd_worst','QFIXF12_N96_fd_worst']:
    p=Path('evidence/parity_axis_inverse')/tag/'diagnostic.json'
    if not p.exists():continue
    d=load(p)
    if not d.get('finished_utc'):continue
    row=dict(tag=tag,source=d['source'],sha256=d['sha256'],finished_utc=d['finished_utc'],count=len(d['rows']),rows=d['rows'],scope=d['scope'])
    row['largest_difference']={q:max(abs(r[q]-r['angular_'+q])for r in d['rows'])for q in ['R_Nf','R_Nv']}
    result['parity'].append(row)
result['scope']='Finite sampled comparisons only. Union maxima retain larger coarse-grid values. Multiprecision density checks do not imply a multiprecision inverse. No residual certificate or parameter-convergence claim.'
Path('evidence/REFINEMENT_FOLLOWUPS.json').write_text(json.dumps(result,indent=2)+'\n')
lines=['# Independent refinement follow-ups','',now,'','All maxima below are sampled. The union retains the larger value from the705-point evaluation and the dense or local grids. Exact horizontal-axis normalized ratios are undefined and omitted. The full records include both denominators and the source SHA-256.','', '| smooth basis | a | max R/Nf | max R/Nv | x at R/Nf | y at R/Nf | Nf there | Nv there | absR there |','|---|---:|---:|---:|---:|---:|---:|---:|---:|']
for s in result['smooth']:
    p=s['union']['R_Nf'];v=s['union']['R_Nv'];lines.append('| '+s['tag']+' | '+' | '.join(f'{x:.12g}'for x in [s['a'],p['maximum'],v['maximum'],p['x'],p['y'],p['Nf'],p['Nv'],p['maximum']*p['Nf']])+' |')
lines+=['','The controls share fixedell=2.5, one frozen N24 seed, coefficient padding or truncation, common jet scale368.7801401458402, the same tolerances and a1000-evaluation ceiling. Fixingell restricts the search and does not use the spatial scaling symmetry. Actual function evaluations differ. The declining finite-grid residual and the changing invariant slope are both retained.','', '| basis | direct FD2 versus angular max difference R/Nf | FD inverse-level change | coarse R/Nv | dense R/Nv | union R/Nv source |','|---|---:|---:|---:|---:|---|']
for s in result['smooth']:
    def val(key):
        v=s['FD'].get(key,{}).get('R_Nf');return f"{v['difference']:.6g}"if v else 'pending'
    lines.append('| '+s['tag']+' | '+val('level2_versus_angular')+' | '+val('inverse_level_change')+' | '+f"{s['coarse705']['R_Nv']['maximum']:.12g} | {s['dense_only']['R_Nv']['maximum']:.12g} | "+s['union']['R_Nv']['sample_set']+' |')
lines+=['','For N24/M20 the original local refinement missed the larger Nv ratio at the earlier y-axis sample. The union above preserves that point. An additional local refinement is recorded separately when completed. Regional absolute residuals, through cumulative radii1e2 to1e250, are retained in JSON. At extreme radii, subtraction of growing terms and the stored binary exponent defect affect absolute residuals. Those values are not certified digits or uniform bounds.','', '## Direct inverse near the symmetry axis','', '| Q state | independent comparisons | largest corrected versus angular R/Nf difference | R/Nv difference |','|---|---:|---:|---:|']
for s in result['parity']:lines.append(f"| {s['tag']} | {s['count']} | {s['largest_difference']['R_Nf']:.12g} | {s['largest_difference']['R_Nv']:.12g} |")
lines+=['','The corrected direct evaluator uses odd parity of U2 and interpolates the even quotient U2(x,y)/y from direct full-plane cancellation-kernel integrals at nonzero y. Two inverse levels and three interpolation widths are compared. Density derivatives use Cartesian FD8. Angular velocity is used only for the final comparison. The original raw cancellation-sensitive values remain in the records. The interpolation error has a conditional fourth-derivative remainder; that derivative has not been bounded, so this is an empirical agreement test.','', 'CONFIRMED: the stored finite comparisons and arithmetic aggregation. OPEN: uniform residual bounds, convergence of a andell, smooth-profile existence and a decisive endpoint.']
Path('evidence/REFINEMENT_FOLLOWUPS.md').write_text('\n'.join(lines)+'\n')
print('\n'.join(lines[:16]))
print('Parity:',[(s['tag'],s['largest_difference'])for s in result['parity']])
