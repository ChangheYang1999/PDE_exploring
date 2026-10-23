"""Read-only numerical audit of a frozen report table and campaign ledgers."""
from __future__ import annotations
import argparse,csv,datetime,hashlib,json
from collections import Counter,defaultdict
from pathlib import Path
from ledger_reconstruction import audit
from ledger_bounds import bounded,stamp,length
ROOT=Path(__file__).resolve().parents[1]

def snapshot_audit(table,training,validation):
    rows=list(csv.DictReader(Path(table).open(),delimiter='\t'));pfx={r['sha256_prefix'] for r in rows}
    if len(pfx)!=len(rows):raise ValueError('Duplicate checkpoint in report table')
    ds={}
    for p in (ROOT/'evidence').glob('checkpoint-*.json'):
        d=json.loads(p.read_text());h=d.get('checkpoint_sha256','')[:16]
        if h in pfx and 'assessment' in d and (h not in ds or d['created_utc']>ds[h]['created_utc']):
            d['audit_evidence']=str(p.relative_to(ROOT));ds[h]=d
    if set(ds)!=pfx:raise ValueError('Missing independent evaluations: '+str(pfx-set(ds)))
    for r in rows:
        d=ds[r['sha256_prefix']];a=d['assessment']
        if abs(float(r['worst_eps_m'])-a['worst_momentum_relative'])>5.01e-7:raise ValueError('Mismatch momentum table')
        if r['worst_region']!=a['worst_sampled_region']:raise ValueError('Mismatch worst region')
        cp=Path(d['model_metadata']['checkpoint_path'])
        if hashlib.sha256(cp.read_bytes()).hexdigest()!=d['checkpoint_sha256']:raise ValueError('Checkpoint hash mismatch')
    by=defaultdict(list)
    for d in ds.values():by[(d['model_metadata']['feature_set'],d['c_l'])].append(d)
    best=[]
    for (feature,c),values in sorted(by.items()):
        d=min(values,key=lambda d:d['assessment']['worst_momentum_relative'])
        st=d['model_metadata']['checkpoint_metadata'].get('state',{})
        best.append(dict(feature=feature,c_l=c,count=len(values),sha256=d['checkpoint_sha256'],saved_step=st.get('global_step'),worst_eps_m=d['assessment']['worst_momentum_relative'],worst_region=d['assessment']['worst_sampled_region'],tail_nonlinear_relative=d['tail']['spheres'][-1]['nonlinear_term_relative'],evidence=d['audit_evidence']))
    funcs={'ring_n2':lambda d:d['angular']['n2_fraction'], 'affine_remainder':lambda d:d['core_affine_fit']['relative_remainder'],'core_nonaxisymmetric_fraction':lambda d:d['vector_group_average']['nonaxisymmetric_energy_fraction'],'n2_over_nonaxisymmetric_ring_energy':lambda d:d['angular']['n2_fraction']/d['angular']['nonaxisymmetric_fraction'],'minimum_directional_variation_fraction':lambda d:d['core_directional_dependence']['minimum_fraction'],'worst_eps_m':lambda d:d['assessment']['worst_momentum_relative']}
    ranges={k:[min(f(d) for d in ds.values()),max(f(d) for d in ds.values())] for k,f in funcs.items()}
    tails={}
    for feature in sorted({d['model_metadata']['feature_set'] for d in ds.values()}):
        for group,cond in [('primary',lambda d:.4<d['c_l']<.5),('control',lambda d:d['c_l']==.5)]:
            v=[d['tail']['spheres'][-1]['nonlinear_term_relative'] for d in ds.values() if d['model_metadata']['feature_set']==feature and cond(d)]
            if v:tails[feature+'_'+group]=[min(v),max(v)]
    primary=min((d for d in ds.values() if .4<d['c_l']<.5),key=lambda d:d['assessment']['worst_momentum_relative'])
    selected={k:primary[k] for k in ('checkpoint_sha256','c_l','assessment','core_affine_fit','core_directional_dependence','symmetry','volume_angular','axis','tail','geometry','cartesian_cylindrical','audit_evidence')}
    selected['regional_residuals']={name:{key:r[key]['relative_rms'] for key in ('momentum','divergence','vorticity','pressure_poisson')} for name,r in primary['regions'].items()}
    lg=audit(training);vr=[json.loads(l) for l in Path(validation).read_text().splitlines() if l.strip()]
    starts={r['interval_id']:r for r in vr if r.get('event')=='start'};stops=[r for r in vr if r.get('event')=='stop'];closed=[]
    for r in stops:
        start=starts[r['interval_id']]
        if start['start_utc']!=r['start_utc']:raise ValueError('Inconsistent validator interval')
        closed.append([stamp(r['start_utc']),stamp(r['end_utc'])])
    shrunk=[]
    for r in map(json.loads,Path(training).read_text().splitlines()):
        for s,e in r.get('chunks',r.get('active_intervals',[])):
            s,e=stamp(s),stamp(e)
            if e-s>2*.000502:shrunk.append([s+.000502,e-.000502])
    lg['combined_with_validation']=bounded(lg['groups'],closed+shrunk);lg['validation_only_seconds']=length(closed);lg['closed_validation_count']=len(closed);lg['unclosed_validator_intervals']=sorted(set(starts)-{r['interval_id'] for r in stops})
    result=dict(date_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),inputs={str(p):hashlib.sha256(Path(p).read_bytes()).hexdigest() for p in (table,training,validation)},checkpoint_count=len(ds),table_matches_evidence=True,worst_region_counts=dict(Counter(r['worst_region'] for r in rows)),ranges=ranges,tail_ranges=tails,best_by_representation_exponent=best,selected_primary=selected,ledger=lg)
    return result

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('table',type=Path);p.add_argument('training',type=Path);p.add_argument('validation',type=Path);p.add_argument('--output',type=Path,required=True);a=p.parse_args()
    out=snapshot_audit(a.table,a.training,a.validation);a.output.write_text(json.dumps(out,indent=2)+'\n');print(a.output);print('Checked',out['checkpoint_count'],'checkpoint hashes; best primary',out['selected_primary']['checkpoint_sha256'])
