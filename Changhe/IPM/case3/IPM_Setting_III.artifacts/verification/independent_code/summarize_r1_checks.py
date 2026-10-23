"""Summarize frozen independent R1 audits with their original hashes and limits."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
import json,math,hashlib

def load(p):return json.loads(Path(p).read_text())
def winner(rows,key,region='all'):
    vals=[dict(r['summary'][region][key],grid=r['grid'])for r in rows if region in r['summary'] and key in r['summary'][region]]
    return max(vals,key=lambda x:x['maximum'])if vals else None

def diff(a,b,key):
    bb={(p['x'],p['y']):p for p in b};out=[]
    for p in a:
        xy=(p['x'],p['y']);v=p['residuals'][-1].get(key)
        if xy[1] and xy in bb and v is not None and bb[xy].get(key)is not None:
            out.append(dict(x=xy[0],y=xy[1],difference=abs(v-bb[xy][key]),direct=v,angular=bb[xy][key]))
    return max(out,key=lambda p:p['difference'])if out else None

out=dict(utc=datetime.now(timezone.utc).isoformat(),scope='Frozen producer R1 states evaluated independently. Exact rational jets, finite dense samples and independent direct-kernel Cartesian FD checks. No uniform bound or nearby profile theorem. Full MP audits are separately labelled pending or computed.',rows=[])
for path in sorted(Path('evidence/q_exact_jets').glob('R1*/diagnostic.json')):
    d=load(path)
    for raw in d['rows']:
        meta=raw['metadata'];e=raw['exact'];name=Path(meta['source']).name
        import re
        match=re.fullmatch(r'r1([CF])_cl([0-9.]+)_N([0-9]+).pt',name)
        if not match:continue
        branch,ell,n=match.groups();tag=f'R1{branch}_CL{ell.replace(".","P")}_N{n}'
        scale=2**(2*meta['map_kappa'])/meta['L']**2
        row=dict(tag=tag,source=meta['source'],sha256=meta['sha256'],metadata=meta,exact_diagnostic=str(path),a=e['a']['approx'],delta=e['delta'],c=e['c']['approx'],physical_cubics={k:e[k+'_core']['approx']*scale for k in ['b','e','q1','q2']},jet_elimination_over_6e=float(F(e['jet_elimination_core']['exact'])/(6*F(e['e_core']['exact']))),poisson=e['poisson'],physical_conversion='core coefficient times 2^(2 kappa)/L^2; displayed physical decimals are rounded',dense=None,FD={},MP='PENDING')
        aa=F(e['a']['exact']);AA=2*F(float(meta['cl']))-1
        bb=F(e['b_core']['exact']);ee=F(e['e_core']['exact']);qq1=F(e['q1_core']['exact']);qq2=F(e['q2_core']['exact'])
        target=(aa-4*AA)*bb/(3*aa);difference=qq1-qq2;defect=difference-target
        row['T2']=dict(core_difference_exact=str(difference),core_target_exact=str(target),core_defect_exact=str(defect),physical_difference=float(difference)*scale,physical_target=float(target)*scale,physical_defect=float(defect)*scale,relative_to_target=float(defect/target)if target else None,relative_two_term=float(abs(defect)/(abs(difference)+abs(target)))if difference or target else None)
        dense=Path('evidence/q_residual_grid')/tag/'diagnostic.json'
        if dense.exists():
            d=load(dense)
            if d.get('finished_utc'):
                assert d['sha256']==meta['sha256'];rr=[r for r in d['rows']if r['inverse_order']==256]
                row['dense']=dict(diagnostic=str(dense),sha256=hashlib.sha256(dense.read_bytes()).hexdigest(),grid='652 logarithmic radii,373 angles plus local grids; three inverse orders128/192/256, summary uses256',regions={region:{key:winner(rr,key,region)for key in ['abs_R','R_Nf','R_Nv']}for region in sorted(set(k for r in rr for k in r['summary']))})
        chart=Path('evidence/complementary_charts')/(tag+'_dense_peaks')/'diagnostic.json'
        if chart.exists():
            c=load(chart);assert c['sha256']==meta['sha256']
            for lev in [1,2]:
                f=Path('evidence/q_evaluations')/(tag+'_dense_peaks')/f'q{lev}.json'
                if f.exists():
                    dd=load(f)
                    if dd.get('finished_utc'):
                        assert dd['metadata']['sha256']==meta['sha256'];row['FD'][str(lev)]={k:diff(dd['points'],c['rows'][-1]['points'],k)for k in ['R_Nf','R_Nv']}
        mp=Path('evidence/q_mp_inverse')/tag/'diagnostic.json'
        if mp.exists():
            mm=load(mp);assert mm['source_sha256']==meta['sha256'];row['MP']=dict(status=mm['status'],path=str(mp),finished=mm.get('finished_utc'),selected_dense_peaks=[dict(pt,selected_metric=key)for key in ['R_Nf','R_Nv']for pt in (mm['rows'][-1]['points']if mm.get('rows')else[])if row['dense'] and (float(pt['x']),float(pt['y']))==(row['dense']['regions']['all'][key]['x'],row['dense']['regions']['all'][key]['y'])],precision_comparisons=mm.get('precision_comparisons'),scope='MP evaluation at selected double-grid peaks; not a globally optimized MP maximum')
        out['rows'].append(row)
out['rows'].sort(key=lambda r:r['tag'])
root=Path('evidence/q_exact_jets');(root/'R1_SUMMARY.json').write_text(json.dumps(out,indent=2)+'\n')
lines=['# Independent checks of the R1 candidate sequences','',out['utc'],'',out['scope'],'','Delta=ell+c-1; T1rel=[6e-(a-2A)b]/(6e), A=2ell-1. Every listed stored input has a nonzero exact Delta. Full-plane high precision residual checks remain pending where indicated.','', '| State | a | Delta | physical b | physical e | T1rel | sampled max R/Nf | sampled max R/Nv |','|---|---:|---:|---:|---:|---:|---:|---:|']
for r in out['rows']:
    den=r['dense'];reg=den['regions']['all']if den else {};nf=reg.get('R_Nf');nv=reg.get('R_Nv');lines.append('| '+r['tag']+' | '+f"{r['a']:.11g} | {r['delta']['approx']:.9g} | {r['physical_cubics']['b']:.10g} | {r['physical_cubics']['e']:.10g} | {r['jet_elimination_over_6e']:.9g} | "+(f"{nf['maximum']:.11g}"if nf else'pending')+' | '+(f"{nv['maximum']:.11g}"if nv else'pending')+' |')
lines+=['','The JSON includes full hashes, exact Delta fractions, point coordinates, both denominators, absolute residuals by region, and actual FD comparisons. Large absolute residuals at enormous radius are sensitive to cancellation and stored exponent error; the double precision values do not establish the asymptotic coefficient. Each direct FD discrepancy near the horizontal axis must be checked with parity interpolation or full MP evaluation before it is interpreted as a true residual.','']
for r in out['rows']:
    if not r['dense']:continue
    lines += [f"## {r['tag']}",'',f"Source SHA256 `{r['sha256']}`. Full MP: `{r['MP'].get('status') if isinstance(r['MP'],dict) else r['MP']}`; full selected-point values and comparisons in JSON.",'']
    for key in ['R_Nf','R_Nv']:
        p=r['dense']['regions']['all'][key];lines.append(f"{key} maximum {p['maximum']:.13g} at ({p['x']:.15g}, {p['y']:.15g}), Nf={p['Nf']:.13g}, Nv={p['Nv']:.13g}.")
    t=r['T2'];lines.append(f"T2: q1-q2={t['physical_difference']:.12g}, (a-4A)b/(3a)={t['physical_target']:.12g}, defect={t['physical_defect']:.12g}, defect/target={t['relative_to_target']}.")
    if isinstance(r['MP'],dict) and r['MP']['status']=='COMPUTED':
        for j,pt in enumerate(r['MP']['selected_dense_peaks']):
            lines.append(f"MP at selected {pt['selected_metric']} grid peak: |R|={abs(float(pt['R'])):.13g}, Nf={float(pt['Nf']):.13g}, Nv={float(pt['Nv']):.13g}, |R|/Nf={float(pt['R_Nf']):.13g}, |R|/Nv={float(pt['R_Nv']):.13g}.")
    lines.append('')
(root/'R1_SUMMARY.md').write_text('\n'.join(lines));print(json.dumps(dict(utc=out['utc'],rows=len(out['rows']),dense=sum(r['dense']is not None for r in out['rows']))))
