#!/usr/bin/env python3
"""Collect immutable completed audits without upgrading finite checks to bounds."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json
ROOT=Path(__file__).resolve().parent

def main():
    stamp=datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S.%fZ')
    out=ROOT/'results/audit_collections'/stamp;out.mkdir(parents=True)
    sources={}
    def read(name):
        p=ROOT/'results'/name;sources[name]=hashlib.sha256(p.read_bytes()).hexdigest();return json.loads(p.read_text())
    result={'recorded_utc':datetime.now(timezone.utc).isoformat(),'source_sha256':sources,'collector_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'precision':{},'peaks':{},'s1':[]}
    for level in ['l1','l2']:
        d=read(f'ladder_{level}_precision.json');assert d['phase']=='complete'
        metrics={}
        for name in d['rows'][0]['precisions'][-1]['float64_errors']:
            rows=[(r['precisions'][-1]['float64_errors'][name],r['point_r_z']) for r in d['rows']]
            worst_abs=max(rows,key=lambda r:r[0]['max_abs_error']);worst_rel=max(rows,key=lambda r:r[0]['relative_error'])
            metrics[name]={'max_absolute':worst_abs[0]['max_abs_error'],'at_absolute':worst_abs[1],'max_relative':worst_rel[0]['relative_error'],'at_relative':worst_rel[1],'max_70_to_100_digit_change':max(float(r['precisions'][-1]['changes_from_previous_precision'][name]) for r in d['rows'])}
        result['precision'][level]={k:d[k] for k in ['updated_utc','elapsed_seconds','cpu_seconds','scope']};result['precision'][level].update(point_count=len(d['rows']),metrics=metrics)
        d=read(f'ladder_{level}_peaks.json');assert d['phase']=='complete'
        equations={}
        for eq in ['q','eta']:
            fresh=max(d['rows'],key=lambda r:r['equations'][eq]['fresh_m'])
            points=[dict(shell_index=r['shell_index'],**p) for r in d['rows'] for p in r['equations'][eq]['peaks']]
            peak=max(points,key=lambda p:p['m_with_frozen_denominator'])
            equations[eq]={'fresh_max_m':fresh['equations'][eq]['fresh_m'],'fresh_max_shell':fresh['shell_index'],'optimized_max_m':peak,'optimized_point_count':len(points),'optimizer_success_count':sum(p['optimizer_success'] for p in points)}
        result['peaks'][level]={k:d[k] for k in ['updated_utc','elapsed_seconds','cpu_seconds','scope']};result['peaks'][level].update(shell_count=len(d['rows']),fresh_point_count=sum(r['samples'] for r in d['rows']),equations=equations)
    for level in ['L0','L1','L2']:
        d=read(f's1_refinement_c074_q2/{level}/summary.json')
        candidate=Path(d['candidate_path']);sources[str(candidate.relative_to(ROOT))]=hashlib.sha256(candidate.read_bytes()).hexdigest()
        assert d['candidate_sha256']==sources[str(candidate.relative_to(ROOT))]
        config=json.loads(candidate.with_name('configuration.json').read_text());sources[str(candidate.with_name('configuration.json').relative_to(ROOT))]=hashlib.sha256(candidate.with_name('configuration.json').read_bytes()).hexdigest()
        search=json.loads(candidate.with_name('summary.json').read_text());sources[str(candidate.with_name('summary.json').relative_to(ROOT))]=hashlib.sha256(candidate.with_name('summary.json').read_bytes()).hexdigest()
        result['s1'].append(dict(level=level,aggregate=d['aggregate'],completed_utc=d['completed_utc'],process_wall_seconds=d['current_process_elapsed_seconds'],candidate_sha256=d['candidate_sha256'],configuration=config,search_termination=search['reason'],search_objective=search['holdout']['objective_squared']))
    for name in ['deformed_t1_quick','deformed_t1_portrait','deformed_t1_transport','two_series_data']:
        d=read(name+'.json')
        result[name]={k:v for k,v in d.items() if k not in ['source_hashes','source_sha256','bernstein_coefficients','axis_limit_samples']}
    (out/'collection.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'output':str(out),'precision':result['precision'],'peaks':result['peaks'],'s1':[dict(level=r['level'],rho=r['aggregate']['rho_max'],m=r['aggregate']['m_max'],completed_utc=r['completed_utc'],configuration=r['configuration']) for r in result['s1']]},indent=2))
if __name__=='__main__':main()
