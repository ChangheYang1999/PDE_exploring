"""Replay the provenance and retained arithmetic of targeted pressure checks."""
from pathlib import Path
from datetime import datetime,timezone
import argparse,hashlib,json,time
import numpy as np
ROOT=Path(__file__).resolve().parent.parent
ap=argparse.ArgumentParser();ap.add_argument('origin',type=Path);ap.add_argument('geometry',type=Path);ap.add_argument('pressure',type=Path);ap.add_argument('--output',type=Path,required=True);a=ap.parse_args()
assert a.output.resolve().is_relative_to(ROOT) and not a.output.exists()
start,cpu=time.perf_counter(),time.process_time();checks=[]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def check(name,passed):
    checks.append(dict(name=name,passed=bool(passed)))
    if not passed:raise AssertionError(name)
def near(x,y):return bool(np.allclose(x,y,rtol=2e-13,atol=2e-15))
def load(path):
    d=json.loads(path.read_text());check(str(path)+' complete',d['phase']=='complete')
    for name,h in d.get('source_sha256',d.get('source_hashes',{})).items():
        p=Path(name)
        if not p.is_absolute():p=ROOT/p
        check('source '+name,sha(p)==h)
    return d
o,g,p=load(a.origin),load(a.geometry),json.loads(a.pressure.read_text())
check('pressure complete',p['phase']=='complete')
check('three direct moments',len(o['moments'])==3)
check('twelve origin sets',len(o['collar_rows'])==12)
check('six geometry sets',len(g['rows'])==6)
for row in o['moments']:
    s=str(row['lmax'])
    check('direct origin P sum '+s,near(row['P'],row['inner_P']+row['tail_P']))
    check('direct origin gradient sum '+s,near(row['gradient_z'],row['inner_gradient_z']+row['tail_gradient_z']))
    check('direct origin momentum '+s,near(row['M_z'],o['origin_axial_without_pressure']+row['gradient_z']))
summary=[]
for source,rows in [('origin',o['collar_rows']),('shell2',g['rows'])]:
    for row in rows:
        tag=f"{source} {row['lmax']} {row['radius_label']} {row['set']}"
        m=row['metrics'];check(tag+' finite reported',m['finite_arrays'])
        check(tag+' positive quadrature',m['weight_sum']>0)
        for eq,x in m['equations'].items():
            if not x['undefined_denominator']:
                check(tag+' '+eq+' rho',near(x['rho'],x['rms']/x['denominator']))
                check(tag+' '+eq+' maximum',near(x['m'],x['maximum']/x['denominator']))
        z=m['equations']['M_z'];summary.append(dict(source=source,lmax=row['lmax'],radius_label=row['radius_label'],set=row['set'],a_eff=row['a_eff'],Mz_rho=z['rho'],Mz_maximum_ratio=z['m'],Mz_rms=z['rms']))
points=np.array(p['points_r_z']);direct=np.array(p['direct_newton_values'][-1]['pressure']);grad40=np.array(p['green_refinements'][-1]['gradient']);point_rows=g['point_pressure_comparisons']
check('three pressure orders',len(point_rows)==3)
for row in point_rows:
    q=np.array(row['pressure']);h=np.array(row['gradient']);s=row['pressure_level']
    check(s+' point shapes',q.shape==(20,) and h.shape==(20,2))
    check(s+' direct pressure error',near(abs(q-direct).max(),row['max_abs_error_against_direct_newton']))
    check(s+' gradient change',near(abs(h-grad40).max(),row['max_abs_gradient_change_from_green40']))
coarse,fine=point_rows[-2:];dq=np.array(fine['pressure'])-np.array(coarse['pressure']);dg=np.array(fine['gradient'])-np.array(coarse['gradient'])
fd=[]
for row in p['direct_gradient_checks']:
    idx=row['point_index'];best=row['steps'][-1]
    fd.append(dict(point_index=idx,point=points[idx].tolist(),h=best['h'],max_abs_gradient_difference=float(abs(np.array(best['gradient'])-np.array(fine['gradient'])[idx]).max())))
result=dict(completed_utc=datetime.now(timezone.utc).isoformat(),verdict='CONFIRMED',check_count=len(checks),all_passed=all(c['passed'] for c in checks),checks=checks,origin_axial_without_pressure=o['origin_axial_without_pressure'],origin_moments=o['moments'],set_rows=summary,refined_pressure_max_abs_error_against_direct=fine['max_abs_error_against_direct_newton'],resolved_to_refined=dict(pressure_max_abs=float(abs(dq).max()),gradient_max_abs=float(abs(dg).max())),refined_gradient_direct_fd=fd,timing={name:dict(completed=d['updated_utc'],wall_seconds=d['elapsed_seconds'],cpu_seconds=d['cpu_seconds'])for name,d in [('origin',o),('geometry',g)]},input_sha256={str(path.resolve().relative_to(ROOT)):sha(path)for path in [a.origin,a.geometry,a.pressure,Path(__file__)]},collector_wall_seconds=time.perf_counter()-start,collector_cpu_seconds=time.process_time()-cpu,scope='Retained arithmetic and source hashes; selected-point convergence is not an interval or global pressure bound. Primitive residuals use the bulk pressure of a piecewise field; separate interface failures persist.')
a.output.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items()if k not in ['checks','input_sha256','set_rows']},indent=2))
