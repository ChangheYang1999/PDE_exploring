"""Produce auditable tables from finished independent residual samples."""
import json,argparse
from pathlib import Path
from datetime import datetime,timezone
import numpy as np
ap=argparse.ArgumentParser();ap.add_argument('--tag',default='corrected');args=ap.parse_args()
base=Path('evidence/residuals');files=sorted(base.glob('*_'+args.tag+'_q*.json'))
rows=[];all_data={}
for path in files:
    data=json.loads(path.read_text())
    if 'finished_utc' not in data:continue
    key=path.name.rsplit('_q',1)[0];level=int(path.stem.rsplit('_q',1)[1])
    points=[p for p in data['points'] if p['y']!=0.]
    def metric(ps):
        if not ps:return None
        return {'sample_count':len(ps),'max_abs_R':max(abs(p['residuals'][-1]['R']) for p in ps),'max_R_Nf':max(p['residuals'][-1]['abs_R_over_Nf'] or 0 for p in ps),'max_R_Nv':max(p['residuals'][-1]['abs_R_over_Nv'] or 0 for p in ps)}
    row={'source':str(path),'state':key,'quadrature_level':level,'finished_utc':data['finished_utc'],'metadata':data['metadata'],'all':metric(points),'regions':{}}
    selections={'center_r_lt_0.01':lambda p:p['radius']<.01,'middle_0.01_to_10':lambda p:.01<=p['radius']<10,'far_r_ge_10':lambda p:p['radius']>=10,'near_x_axis':lambda p:abs(p['y'])/p['radius']<.03,'near_y_axis':lambda p:abs(p['x'])/p['radius']<.08}
    row['regions']={k:metric([p for p in points if select(p)]) for k,select in selections.items()}
    row['max_FD_residual_change_last_two']=max(abs(p['residuals'][-1]['R']-p['residuals'][-2]['R']) for p in points)
    row['max_FD_ratio_change_last_two']=max(abs(p['residuals'][-1]['abs_R_over_Nf']-p['residuals'][-2]['abs_R_over_Nf']) for p in points)
    previous=all_data.get(key)
    if previous:
        old={(p['x'],p['y']):p for p in previous['points']}
        common=[p for p in points if (p['x'],p['y']) in old]
        row['quadrature_change_max_U']=max(np.max(np.abs(np.array(p['U'])-np.array(old[(p['x'],p['y'])]['U']))) for p in common)
        row['quadrature_change_max_ratio']=max(abs(p['residuals'][-1]['abs_R_over_Nf']-old[(p['x'],p['y'])]['residuals'][-1]['abs_R_over_Nf']) for p in common)
    all_data[key]=data;rows.append(row)
result={'utc':datetime.now(timezone.utc).isoformat(),'tag':args.tag,'scope':'Sparse samples only; exact x-axis 0/0 points excluded, no global or interval residual bound. Three finite-difference steps are saved in the underlying files. Entire exterior integrated.','rows':rows}
(base/('summary_'+args.tag+'.json')).write_text(json.dumps(result,indent=2)+'\n')
text='| State | Q | max abs R | max R/Nf | max R/Nv | change R/Nf vs previous Q |\n|---|---:|---:|---:|---:|---:|\n'
for r in rows:
    q=r['all'];change=r.get('quadrature_change_max_ratio',float('nan'))
    text+=f"| {r['state']} | {r['quadrature_level']} | {q['max_abs_R']:.6g} | {q['max_R_Nf']:.6g} | {q['max_R_Nv']:.6g} | {change:.3g} |\n"
(base/('summary_'+args.tag+'.md')).write_text(text+'\n'+result['scope']+'\n')
print(text)
