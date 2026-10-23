"""Summarize saved independent evaluations, never invoking the producer's code."""
from pathlib import Path
from datetime import datetime,timezone
import json, math
out=Path('evidence/published_forced');out.mkdir(exist_ok=True)
records=[]
for path in sorted(Path('evidence/residuals').glob('rf_s1_*_forced_q*.json')):
    data=json.loads(path.read_text())
    if 'finished_utc' not in data:continue
    points=data['points']
    def summarize(ps):
        result={'sample_count':len(ps),'off_xaxis_count':sum(p['y']!=0 for p in ps)}
        for eq in ['R','Rforced']:
            entries=[]
            for p in ps:
                row=p['residuals'][-1]
                entries.append((p,row))
            for measure in ['absolute','Nf','Nv']:
                eligible=[(p,v) for p,v in entries if measure=='absolute' or (p['y']!=0 and v[measure]>0)]
                if not eligible:continue
                def value(pr):
                    p,v=pr
                    return abs(v[eq]) if measure=='absolute' else abs(v[eq])/v[measure]
                p,v=max(eligible,key=value)
                result[eq+'_'+measure]={'maximum':value((p,v)),'x':p['x'],'y':p['y'],'r':p['radius'],'residual':v[eq],'Nf':v['Nf'],'Nv':v['Nv']}
        eligible=[p for p in ps if p['y']!=0]
        if eligible:
            result['min_Nf']=min(p['residuals'][-1]['Nf'] for p in eligible)
            result['min_Nv']=min(p['residuals'][-1]['Nv'] for p in eligible)
            result['max_normalized_FD_last_two_change']=max(abs(p['residuals'][-1]['R']-p['residuals'][-2]['R'])/p['residuals'][-1]['Nf'] for p in eligible)
        return result
    rec={'source':str(path),'metadata':data['metadata'],'config':data['config'],'finished_utc':data['finished_utc'],'overall':summarize(points),'regions':{}}
    for label,low,high in [('center',0,.01),('core',.01,1),('middle',1,100),('far',100,math.inf)]:
        rec['regions'][label]=summarize([p for p in points if low<=p['radius']<high])
    rec['regions']['near_xaxis']=summarize([p for p in points if p['y']!=0 and abs(p['y'])<.01*p['radius']])
    rec['regions']['yaxis']=summarize([p for p in points if p['x']==0 and p['y']!=0])
    records.append(rec)
# Compare pointwise U and resulting residual changes between completed levels.
comparisons=[]
for record in records:
    path=Path(record['source']);lev=int(path.stem.rsplit('q',1)[1])
    prev=path.with_name(path.name.rsplit('q',1)[0]+'q'+str(lev-1)+'.json')
    if not prev.exists():continue
    old=json.loads(prev.read_text());new=json.loads(path.read_text())
    if 'finished_utc' not in old:continue
    if len(old['points'])!=len(new['points']):raise ValueError('inconsistent points')
    vals=[]
    for a,b in zip(old['points'],new['points']):
        assert (a['x'],a['y'])==(b['x'],b['y'])
        if b['y']==0:continue
        du=math.hypot(*(b['U'][i]-a['U'][i] for i in range(2)))
        rd=abs(b['residuals'][-1]['R']-a['residuals'][-1]['R'])
        vals.append((du,rd,rd/b['residuals'][-1]['Nf'],b['x'],b['y']))
    comparisons.append({'old':str(prev),'new':str(path),'max_abs_dU':max(vals,key=lambda t:t[0]),'max_abs_dR':max(vals,key=lambda t:t[1]),'max_Nf_normalized_dR':max(vals,key=lambda t:t[2])})
result={'updated_utc':datetime.now(timezone.utc).isoformat(),'scope':'Sparse saved samples, not global or interval bounds. Exact x-axis excluded from ratios only; absolute values retained. Raw R checks the unforced primary equation; Rforced subtracts encoded source. Quad changes alter radial, angular and tail nodes and exterior splitting together.','records':records,'comparisons':comparisons}
(out/'residual_summary.json').write_text(json.dumps(result,indent=2)+'\n')
lines=['# Independent raw forced-state residual checks','',result['updated_utc'],'',result['scope'],'','| State | Quadrature | abs Rforced | Rforced/Nf | Rforced/Nv | abs R | R/Nf | R/Nv |','|---|---:|---:|---:|---:|---:|---:|---:|']
for r in records:
    o=r['overall'];q=Path(r['source']).stem.rsplit('q',1)[1]
    lines.append('| '+Path(r['source']).stem.rsplit('_forced_',1)[0]+' | '+q+' | '+' | '.join(f"{o[k]['maximum']:.8g}" for k in ['Rforced_absolute','Rforced_Nf','Rforced_Nv','R_absolute','R_Nf','R_Nv'])+' |')
for r in records:
    lines+=['','## '+Path(r['source']).stem,'','| Region | abs Rforced | Rforced/Nf | Rforced/Nv | abs R | R/Nf | R/Nv |','|---|---:|---:|---:|---:|---:|---:|']
    for label,o in r['regions'].items():
        lines.append('| '+label+' | '+' | '.join(f"{o[k]['maximum']:.8g}" if k in o else 'undefined' for k in ['Rforced_absolute','Rforced_Nf','Rforced_Nv','R_absolute','R_Nf','R_Nv'])+' |')
(out/'residual_summary.md').write_text('\n'.join(lines)+'\n')
print('\n'.join(lines[:8+len(records)]))
print('pointwise_comparisons',json.dumps(comparisons))
