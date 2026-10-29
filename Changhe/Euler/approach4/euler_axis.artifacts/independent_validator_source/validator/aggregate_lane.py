#!/usr/bin/env python3
"""Make auditable lane tables without equating search losses with acceptance."""
from pathlib import Path
import csv,datetime,hashlib,json,shutil
import numpy as np
ROOT=Path(__file__).resolve().parent
LANE=ROOT.parent

def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def read(p):return json.loads(p.read_text())
def write_csv(path,rows,columns):
    with path.open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=columns);w.writeheader();w.writerows(rows)

def main():
    stamp=datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%dT%H%M%S.%fZ')
    out=ROOT/'results/aggregate_snapshots'/stamp;out.mkdir(parents=True)
    paths=set()
    for pattern in ['runs/*/summary.json','sweep*/*/summary.json','t2_sweep*/*/summary.json','green_sweep*/*/*/summary.json','free_c_pilot/summary.json','free_c_sweep*/*/summary.json','enriched_green_sweep*/*/summary.json','slaved_green_sweep*/*/summary.json']:
        paths.update((ROOT/'exploration').glob(pattern))
    rows=[];inputs={}
    for p in sorted(paths):
        config=p.with_name('configuration.json');coeff=p.with_name('best_field.json')
        if not config.exists():continue
        d=read(p);c=read(config)
        if 'holdout' not in d:continue
        for f in [p,config,coeff]:inputs[str(f.relative_to(LANE))]=digest(f)
        if d['best_field_sha256']!=digest(coeff):raise RuntimeError('coefficient changed: '+str(coeff))
        h=d['holdout'];family=p.relative_to(ROOT/'exploration').parts[0]
        early=family=='green_sweep1' and 'S1_' in p.parent.parent.name and not c.get('seed_potential')
        final_c=d.get('final_c_l',c['c_l'])
        rows.append(dict(run=str(p.parent.relative_to(LANE)),family=family,c_l=final_c,initial_c_l=c['c_l'],alpha=(1-final_c)/final_c,
            K=c.get('K',c.get('q0')),method=c.get('method','trf'),angular=c['angular'],radial=c['radial'],correction=c['correction'],correction_angular=c.get('correction_angular',''),
            unknown_count=d['unknown_count'],first_field_terms=d.get('phi_terms',d.get('eta_terms')),q_terms=d['q_terms'],
            training_objective_squared=d['training']['objective_squared'],holdout_objective_squared=h['objective_squared'],
            holdout_q_max=h['raw_q_max'],holdout_eta_max=h['raw_eta_max'],coefficient_max=h['max_coefficient'],
            wall_seconds=d['elapsed_seconds'],cpu_seconds=d['process_cpu_seconds'],nfev=d.get('nfev',d.get('function_evaluations','')),
            termination=d['reason'],completed_utc=d['completed_utc'],coefficient_sha256=d['best_field_sha256'],
            exponent_at_numerical_bound=d.get('exponent_at_numerical_bound',''),interpretation='Premature near-zero seed termination; see green_seed_diagnosis' if early else 'Search approximation; registered acceptance separate'))
    columns=list(rows[0]) if rows else ['run']
    write_csv(out/'PARAMETER_SWEEP.csv',rows,columns)
    registered=[];candidates=set((ROOT/'results/s1_refinement_c074_q2').glob('*/summary.json'))
    candidates.update((ROOT/'results/external').glob('*/registered_bulk/summary.json'))
    candidates.update((ROOT/'exploration/registered').glob('*/summary.json'))
    candidates.update((ROOT/'results/green_partial_free_L1_v2').glob('summary.json'))
    candidates.update((ROOT/'results').glob('driver_*/registered/summary.json'))
    # Other own audits are detected only in bounded, named validation directories.
    for dirname in ['validation','registered_validation']:
        candidates.update((ROOT/'exploration'/dirname).glob('*/summary.json'))
    for p in sorted(candidates):
        d=read(p)
        if 'aggregate' not in d:continue
        a=d['aggregate'];inputs[str(p.relative_to(LANE))]=digest(p)
        candidate=Path(d['candidate_path'])
        if digest(candidate)!=d['candidate_sha256']:raise RuntimeError('registered coefficient changed')
        inputs[str(candidate.relative_to(LANE))]=digest(candidate)
        if candidate.suffix=='.npz':
            with np.load(candidate,allow_pickle=False) as data:
                meta=json.loads(str(data['meta_json']));cl=meta.get('cl',meta.get('c_l'));count=sum(data[k].size for k in data.files if k.startswith(('phi_el','q_el')))
        else:
            meta=read(candidate);cl=meta['c_l'];count=sum(len(meta[k]['terms']) for k in ['phi' if 'phi' in meta else 'eta','q'])
        registered.append(dict(audit=str(p.parent.relative_to(LANE)),candidate=d.get('candidate_path',''),
            coefficient_sha256=d.get('candidate_sha256',''),c_l=cl,alpha=(1-cl)/cl,coefficient_count=count,complete_required_shell_set=d.get('complete_required_shell_set',False),
            rho_max=a['rho_max'],m_max=a['m_max'],rho_location=json.dumps(a['rho_max_at'],sort_keys=True),m_location=json.dumps(a['m_max_at'],sort_keys=True),
            A1_measured_pass=a['A1_measured_pass'],A2_measured_pass=a['A2_measured_pass'],a_eff=d.get('a_eff',d.get('core',{}).get('a_eff','')),
            completed_utc=d.get('completed_utc',''),verdict='REJECTED by measured A1/A2' if not(a['A1_measured_pass'] and a['A2_measured_pass']) else 'OPEN: remaining acceptance tests required'))
    registered.sort(key=lambda r:r['rho_max'])
    write_csv(out/'CANDIDATE_LEADERBOARD.csv',registered,list(registered[0]) if registered else ['audit'])
    groups={}
    for family in sorted({r['family'] for r in rows}):
        subset=[r for r in rows if r['family']==family]
        groups[family]=dict(completed_runs=len(subset),optimizer_wall_seconds_sum=sum(r['wall_seconds'] for r in subset),optimizer_cpu_seconds_sum=sum(r['cpu_seconds'] for r in subset),
            c_l_values=sorted({r['c_l'] for r in subset}),best_custom_objective_run=min(subset,key=lambda r:r['holdout_objective_squared']))
    summary=dict(created_utc=stamp,aggregator_sha256=digest(Path(__file__)),completed_search_runs=len(rows),registered_records=len(registered),groups=groups,input_sha256=inputs,
        scope='Ongoing lane snapshot. No comparison across custom objectives is an acceptance ranking. Sums of run times are not campaign elapsed time. Unfinished jobs are excluded.')
    (out/'summary.json').write_text(json.dumps(summary,indent=2)+'\n')
    for name in ['PARAMETER_SWEEP.csv','CANDIDATE_LEADERBOARD.csv']:shutil.copyfile(out/name,LANE/name)
    (ROOT/'results/latest_aggregate.txt').write_text(str(out.relative_to(ROOT))+'\n')
    print(json.dumps(dict(output=str(out),runs=len(rows),registered=len(registered))))
if __name__=='__main__':main()
