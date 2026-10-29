#!/usr/bin/env python3
"""Collect a completed pressure comparison, refusing incomplete or changed inputs."""
from pathlib import Path
from datetime import datetime, timezone
import argparse, hashlib, json
import numpy as np

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def main():
    p=argparse.ArgumentParser();p.add_argument('input',type=Path);p.add_argument('output',type=Path)
    a=p.parse_args();root=Path(__file__).resolve().parent.parent
    if not a.output.resolve().is_relative_to(root) or a.output.exists():
        raise ValueError('A fresh output in this lane is required')
    data=json.loads(a.input.read_text())
    if data.get('phase')!='complete':raise ValueError('Comparison is incomplete')
    for name, expected in data['source_hashes'].items():
        if digest(Path(name))!=expected:raise ValueError('Changed input: '+name)
    points=data['point_pressure_comparisons'];rows=[]
    for row in data['rows']:
        metrics=row['metrics']['equations']
        rows.append({k:row[k] for k in ['pressure_level','radius_label','a_eff','lmax','nangle','nradial']} |
                    {'rho_M_z':metrics['M_z']['rho'],'m_M_z':metrics['M_z']['m'],
                     'rho_q':metrics['q']['rho'],'rho_eta':metrics['eta']['rho']})
    changes=[]
    for old,new in zip(points,points[1:]):
        changes.append({'from':old['pressure_level'],'to':new['pressure_level'],
                        'max_pressure_change':float(np.max(np.abs(np.array(new['pressure'])-old['pressure']))),
                        'max_gradient_change':float(np.max(np.abs(np.array(new['gradient'])-old['gradient'])))})
    out={'created_utc':datetime.now(timezone.utc).isoformat(),'input':str(a.input.resolve()),
         'input_sha256':digest(a.input),'collector_sha256':digest(Path(__file__)),
         'run_completed_utc':data['updated_utc'],'run_wall_seconds':data['elapsed_seconds'],
         'run_cpu_seconds':data['cpu_seconds'],'point_count':len(points[-1]['pressure']),
         'point_errors':[{'pressure_level':x['pressure_level'],
                          'max_absolute_pressure_error_against_direct_newton':x['max_abs_error_against_direct_newton']} for x in points],
         'point_refinement_changes':changes,'collar_rows':rows,
         'scope':'Completed 20-point pressure and one-shell collar study. This is not a full A7 acceptance check or a reranking of all registered sets.'}
    a.output.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))
if __name__=='__main__':main()
