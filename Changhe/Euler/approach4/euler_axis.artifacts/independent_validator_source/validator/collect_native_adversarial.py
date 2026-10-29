"""Audit retained native-field diagnostics, including characteristic arithmetic."""
from pathlib import Path
from datetime import datetime,timezone
import argparse,hashlib,json,time
import numpy as np
from fast_native_field import FastNativeField
ROOT=Path(__file__).resolve().parent.parent
ap=argparse.ArgumentParser();ap.add_argument('candidate',type=Path);ap.add_argument('--stem',required=True);ap.add_argument('--geometry',type=Path,required=True);ap.add_argument('--registered',type=Path,required=True);ap.add_argument('--output',type=Path,required=True);a=ap.parse_args()
assert a.output.resolve().is_relative_to(ROOT)and not a.output.exists()
start,cpu=time.perf_counter(),time.process_time();checks=[];sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def check(name,passed):
    checks.append(dict(name=name,passed=bool(passed)))
    if not passed:raise AssertionError(name)
def near(x,y):return bool(np.allclose(x,y,rtol=3e-13,atol=3e-15))
inputs=[a.candidate,a.geometry,a.registered,Path(__file__)];data={}
for tag in ['dynamics','peaks','precision']:
    path=ROOT/'axisymmetric_euler_24h/results'/f'{a.stem}_{tag}.json';inputs.append(path);d=json.loads(path.read_text());data[tag]=d
    check(tag+' complete',d['phase']=='complete');check(tag+' candidate',d['candidate_sha256']==sha(a.candidate))
    for name,h in d['source_sha256'].items():check(tag+' source '+name,sha(ROOT/name)==h)
    if 'geometry_sha256'in d:check(tag+' geometry',d['geometry_sha256']==sha(a.geometry))
    if 'registered_sha256'in d:check(tag+' registered',d['registered_sha256']==sha(a.registered))
d=data['dynamics'];summaries=[]
for row in d['swirl_fractions']:
    check('core swirl '+str(row['nradial']),near(row['s_core'],np.sqrt(row['swirl_velocity_squared_integral']/row['total_velocity_squared_integral'])))
v=d['vorticity_maximum'];check('vorticity squared',near(v['vorticity_squared'],np.dot(v['vorticity'],v['vorticity'])))
check('vorticity stretching defect',near(v['maximum_identity_defect'],v['stretching']-v['vorticity_squared']))
check('vorticity finite-search scope',v['global_maximum_proved']is False)
check('twelve characteristic runs',len(d['characteristics'])==12)
for i,row in enumerate(d['characteristics']):
    for j,x in enumerate(row['path']):
        check(f'path {i} {j} corrected',near(x['corrected_error'],x['weighted_gamma']-row['initial_gamma']-x['integrated_residual']-x['jump_sum']))
        check(f'path {i} {j} uncorrected',near(x['uncorrected_change'],x['weighted_gamma']-row['initial_gamma']))
    for k,field in [('max_corrected_error','corrected_error'),('max_uncorrected_change','uncorrected_change')]:check(f'path {i} '+k,near(row[k],max(abs(x[field])for x in row['path'])))
    scale=max(abs(row['initial_gamma']),max(abs(x['weighted_gamma'])for x in row['path']),1e-300)
    for label in ['corrected_error','uncorrected_change']:check(f'path {i} relative '+label,near(row['max_relative_'+label],row['max_'+label]/scale))
    summaries.append({k:row[k]for k in ['trajectory_index','requested_endpoint','reached_endpoint','success','rtol','max_relative_corrected_error','max_relative_uncorrected_change']})
p=data['peaks'];check('nineteen peak shells',len(p['rows'])==19);peaks={}
for key in ['q','eta']:
    all_peaks=[]
    for row in p['rows']:
        r=row['equations'][key];den=r['registered_denominator']
        if den>0:
            check(f'fresh {key} {row["shell_index"]}',near(r['fresh_m'],r['fresh_maximum']/den))
            for j,x in enumerate(r['peaks']):
                check(f'peak {key} {row["shell_index"]} {j}',near(x['m_with_frozen_denominator'],abs(x['residual'])/den))
                all_peaks.append(dict(shell_index=row['shell_index'],**x))
    fresh=max((row for row in p['rows']if row['equations'][key]['registered_denominator']>0),key=lambda row:row['equations'][key]['fresh_m'])
    peaks[key]=dict(fresh_max_m=fresh['equations'][key]['fresh_m'],fresh_max_shell=fresh['shell_index'],optimized_max=max(all_peaks,key=lambda x:x['m_with_frozen_denominator']),peak_count=len(all_peaks))
f=FastNativeField.load(a.candidate);precision=data['precision'];check('thirteen precision points',len(precision['rows'])==13);metrics={}
for i,row in enumerate(precision['rows']):
    check('precision orders '+str(i),[x['dps']for x in row['precisions']]==[70,100])
    r,z=row['point_r_z'];xyz=np.array([r,0.,z]);U,J=f.cartesian(xyz,True);red=f.reduced(r,z)
    actual={'velocity':U,'jacobian':J,'primitive_without_pressure':f.primitive_cartesian(xyz),'source':f.source(r,z),'q_residual':red['q'],'eta_residual':red['eta']}
    for ref in row['precisions']:
        for key,x in actual.items():
            given=ref['float64_errors'][key];reference=np.array(ref['reference'][key],dtype=float)
            error=float(abs(reference-np.asarray(x)).max());scale=float(abs(reference).max())
            check(f'precision {i} {ref["dps"]} {key} abs',near(error,given['max_abs_error']))
            check(f'precision {i} {ref["dps"]} {key} scale',near(scale,given['reference_scale']))
    for key in actual:
        x=row['precisions'][-1]['float64_errors'][key];m=metrics.setdefault(key,dict(max_abs_error=0.,max_relative_error=0.,max_70_to_100_change=0.))
        m['max_abs_error']=max(m['max_abs_error'],x['max_abs_error']);m['max_relative_error']=max(m['max_relative_error'],x['relative_error']or 0.)
        m['max_70_to_100_change']=max(m['max_70_to_100_change'],float(row['precisions'][-1]['changes_from_previous_precision'][key]))
result=dict(completed_utc=datetime.now(timezone.utc).isoformat(),verdict='CONFIRMED',check_count=len(checks),all_passed=all(x['passed']for x in checks),checks=checks,vorticity_maximum=v,swirl_maximum=d['swirl_maximum']['best'],detected_roots=d['stagnation_inventory']['roots'],characteristics=summaries,peaks=peaks,precision=metrics,point_count=len(precision['rows']),fresh_point_count=sum(x['samples']for x in p['rows']),timing={k:dict(completed=v['updated_utc'],wall_seconds=v['elapsed_seconds'],cpu_seconds=v['cpu_seconds'])for k,v in data.items()},input_sha256={str(p.resolve().relative_to(ROOT)):sha(p)for p in inputs},collector_wall_seconds=time.perf_counter()-start,collector_cpu_seconds=time.process_time()-cpu,scope='Finite diagnostics and retained arithmetic, not certified maxima, a complete stagnation inventory, a global source portrait or interval precision bounds. Characteristic residual corrections verify an identity and do not remove Euler defects. Peak search fresh arrays were not retained; their summary arithmetic and source hashes are checked.')
a.output.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:v for k,v in result.items()if k not in ['checks','input_sha256','detected_roots']},indent=2))
