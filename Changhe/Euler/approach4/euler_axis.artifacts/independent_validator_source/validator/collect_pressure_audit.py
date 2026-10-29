"""Check retained pressure arrays and arithmetic without rerunning quadrature."""
from pathlib import Path
from datetime import datetime, timezone
import argparse,hashlib,json,time
import numpy as np
ROOT=Path(__file__).resolve().parent.parent
ap=argparse.ArgumentParser();ap.add_argument('input',type=Path);ap.add_argument('candidate',type=Path);ap.add_argument('--output',type=Path,required=True);a=ap.parse_args()
assert a.output.resolve().is_relative_to(ROOT) and not a.output.exists()
start,cpu=time.perf_counter(),time.process_time();checks=[]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def check(name,passed):
    checks.append(dict(name=name,passed=bool(passed)))
    if not passed:raise AssertionError(name)
d=json.loads(a.input.read_text());check('complete pressure audit',d['phase']=='complete')
check('candidate identity',sha(a.candidate)==d['candidate_sha256'])
for name,h in d['source_sha256'].items():
    p=Path(name)
    if not p.is_absolute():p=(ROOT if name.startswith(('research/','axisymmetric_euler_24h/'))else ROOT/'axisymmetric_euler_24h')/p
    check('source '+name,sha(p)==h)
points=np.asarray(d['points_r_z']);check('twenty points',points.shape==(20,2))
coarse,fine=d['green_refinements'];p=np.array(fine['pressure']);g=np.array(fine['gradient'])
check('pressure and gradient shapes',p.shape==(20,) and g.shape==(20,2))
for label,item in [('coarse',coarse),('fine',fine)]:
    check(label+' finite arrays',np.all(np.isfinite(item['pressure'])) and np.all(np.isfinite(item['gradient'])))
for name,calculated in [('pressure',np.max(abs(p-np.array(coarse['pressure'])))),('gradient',np.max(abs(g-np.array(coarse['gradient']))))]:
    check('Green refinement '+name,calculated==d['green_refinement_max_abs'][name])
for name in ['pressure','gradient']:
    x=np.array(d['stress_surface_correction'][name]);check('stress '+name,np.max(abs(x))==d['stress_surface_correction']['max_abs_'+name])
rows=[]
for row in d['direct_newton_values']:
    direct=np.array(row['pressure']);delta=direct-p
    check('direct finite and shape '+str(row['nradial']),direct.shape==(20,) and np.all(np.isfinite(direct)))
    check('direct maximum '+str(row['nradial']),np.max(abs(delta))==row['max_abs_error_against_fine_green'])
    i=int(np.argmax(abs(delta)));rows.append(dict(nradial=row['nradial'],nangle=row['nangle'],max_abs_pressure_difference=float(abs(delta[i])),worst_point_index=i,worst_point=points[i].tolist(),pointwise_absolute_differences=abs(delta).tolist()))
for row in d['direct_gradient_checks']:
    i=row['point_index']
    for step in row['steps']:
        check('direct gradient '+str(i)+' '+str(step['h']),np.max(abs(np.array(step['gradient'])-g[i]))==step['max_abs_error'])
change=np.array(d['direct_newton_values'][1]['pressure'])-np.array(d['direct_newton_values'][0]['pressure'])
result=dict(completed_utc=datetime.now(timezone.utc).isoformat(),verdict='CONFIRMED',check_count=len(checks),all_passed=all(r['passed']for r in checks),checks=checks,candidate_sha256=d['candidate_sha256'],input_sha256={str(a.input.resolve().relative_to(ROOT)):sha(a.input),str(Path(__file__).relative_to(ROOT)):sha(Path(__file__))},source_completed_utc=d['updated_utc'],source_wall_seconds=d['elapsed_seconds'],source_cpu_seconds=d['cpu_seconds'],green_refinement_max_abs=d['green_refinement_max_abs'],stress_maxima={k:v for k,v in d['stress_surface_correction'].items()if k.startswith('max')},direct_rows=rows,direct_refinement_max_abs=float(np.max(abs(change))),direct_gradient_checks=d['direct_gradient_checks'],saved_sample_comparison=d.get('saved_sample_pressure_comparison'),collector_wall_seconds=time.perf_counter()-start,collector_cpu_seconds=time.process_time()-cpu,scope='Retained-array arithmetic and provenance audit. The 765-point saved comparison is quoted from its hash-checked computation; full reconstructed sample arrays were not retained. This is not a new quadrature calculation, interval error bound, shell-normalized A7 check or proof of Euler closure.')
a.output.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items()if k not in ['checks','direct_rows','direct_gradient_checks','input_sha256','saved_sample_comparison']},indent=2))
