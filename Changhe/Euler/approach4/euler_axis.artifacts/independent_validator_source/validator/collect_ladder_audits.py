#!/usr/bin/env python3
"""Summarize completed independent records with preserved source hashes."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,math
ROOT=Path(__file__).resolve().parent

def read(name):return json.loads((ROOT/'results'/name).read_text())
def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def maxdiff(a,b):return max(abs(x-y) for x,y in zip(a,b))

def main():
    stamp=datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S.%fZ')
    out=ROOT/'results'/'audit_collections'/stamp;out.mkdir(parents=True)
    sources=['ladder_l1_geometry_pressure.json','ladder_l1_pressure.json','driver_t1_ladder_l1/registered/summary.json','driver_t1_ladder_l1/registered/geometry.json','ladder_l1_dynamics.json','ladder_l2_structure.json']
    p=read(sources[0]);ref=read(sources[1]);reg=read(sources[2]);geom=read(sources[3])
    assert p['phase']==ref['phase']=='complete'
    L=geom['gauge']['dilation_L'];newton=ref['direct_newton_values'][-1]['pressure'];fine=p['point_pressure_comparisons'][-1];resolved=p['point_pressure_comparisons'][-2]
    rows=[]
    for i,(point,P,N) in enumerate(zip(ref['points_r_z'],fine['pressure'],newton)):
        R=math.hypot(*point)*L
        shell=next(row for row in reg['rows'] if row['set']=='shell_gauss' and row['lower']<=R<=row['upper'])
        scale=shell['metrics']['pressure_rms']/L**2
        rows.append(dict(index=i,point_working=point,shell=shell['shell_index'],green=P,newton=N,error=abs(P-N),point_relative=abs(P-N)/abs(P),local_baseline_shell_pressure_rms=scale,shell_relative=abs(P-N)/scale))
    pressure=dict(completed_utc=p['updated_utc'],wall_seconds=p['elapsed_seconds'],cpu_seconds=p['cpu_seconds'],orders=[dict(label=r['pressure_level'],lmax=r['lmax'],nangle=r['nangle'],nradial=r['nradial']) for r in p['rows'][::2]],green_newton_max_abs=max(x['error'] for x in rows),green_newton_max_point_relative=max(x['point_relative'] for x in rows),green_newton_max_shell_relative=max(x['shell_relative'] for x in rows),green_refinement_max_abs=maxdiff(fine['pressure'],resolved['pressure']),green_gradient_refinement_max_abs=maxdiff(sum(fine['gradient'],[]),sum(resolved['gradient'],[])),point_checks=rows,momentum_collar=[dict(level=r['pressure_level'],radius=r['radius_label'],a_eff=r['a_eff'],rho_Mz=r['metrics']['equations']['M_z']['rho'],m_Mz=r['metrics']['equations']['M_z']['m']) for r in p['rows']],scope='Bulk pressure agreement at20points. Local scales are the stored baseline shell Gauss pressure RMS converted to working units. Full A7 also requires moment and regularity conditions and is not inferred.')
    dynamics={}
    for level in ['l1','l2']:
        name=f'ladder_{level}_dynamics.json';path=ROOT/'results'/name
        if not path.exists():continue
        d=read(name)
        if d.get('phase')!='complete':continue
        if name not in sources:sources.append(name)
        trajectories=[]
        for c in d['characteristics']:
            trajectories.append({k:c.get(k) for k in ['trajectory_index','requested_endpoint','reached_endpoint','rtol','status','success','nfev','initial_gamma','max_corrected_error','max_relative_corrected_error','max_uncorrected_change','max_relative_uncorrected_change']})
            trajectories[-1].update(crossings=len(c['crossings']),max_path_corrected_error=max(abs(x['corrected_error']) for x in c['path']),max_path_uncorrected_change=max(abs(x['uncorrected_change']) for x in c['path']))
        dynamics[level]=dict(completed_utc=d['updated_utc'],wall_seconds=d['elapsed_seconds'],cpu_seconds=d['cpu_seconds'],swirl_fractions=d['swirl_fractions'],far_swirl_fraction=d['far_swirl_fraction'],vorticity_maximum=d['vorticity_maximum'],swirl_maximum=d['swirl_maximum']['best'],roots=d['stagnation_inventory']['roots'],root_search_scope=d['stagnation_inventory']['scope'],axis_branches=d['axis_branches'],trajectories=trajectories)
    record=dict(recorded_utc=datetime.now(timezone.utc).isoformat(),source_sha256={n:sha(ROOT/'results'/n) for n in sources},collector_sha256=sha(Path(__file__)),pressure=pressure,dynamics=dynamics,L2_structure=read('ladder_l2_structure.json'))
    (out/'collection.json').write_text(json.dumps(record,indent=2)+'\n')
    print(json.dumps({'output':str(out),'pressure_max_abs':pressure['green_newton_max_abs'],'pressure_max_shell_relative':pressure['green_newton_max_shell_relative'],'green_refinement':pressure['green_refinement_max_abs'],'gradient_refinement':pressure['green_gradient_refinement_max_abs'],'completed_dynamics':list(dynamics)},indent=2))

if __name__=='__main__':main()
