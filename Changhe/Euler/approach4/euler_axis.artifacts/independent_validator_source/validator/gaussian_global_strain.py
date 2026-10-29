#!/usr/bin/env python3
"""Checkpointed full-space strain of the two refined Gaussian fields."""
from pathlib import Path
from datetime import datetime,timezone
import argparse,json,time
import numpy as np
from fast_gaussian_trial_field import FastGaussianTrialField
from audit_t1_deformation import transport
from global_strain_quadrature import strain_rule,strain_values
from independent_artifacts import atomic_json,sha256
BASE=Path(__file__).resolve().parent;ROOT=BASE.parent
EXPORT=BASE/'external_exports/T1_gaussian_nk_20261029T031456.661955Z'
LEVELS=[('coarse',16,64,128.,1e-5,2e-10),('fine',24,96,256.,1e-6,5e-12)]
NAMES=['gaussian_c068_n20','gaussian_c074_n20']
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output',required=True,type=Path);ap.add_argument('--wall-limit',type=float,default=235);ap.add_argument('--chunk',type=int,default=3);a=ap.parse_args()
    out=a.output.resolve()
    if not out.is_relative_to(ROOT)or a.chunk<1:raise ValueError('Invalid output or chunk')
    out.mkdir(exist_ok=True,parents=True);summary=out/'summary.json';start=time.perf_counter();cpu=time.process_time()
    paths=[Path(__file__),BASE/'fast_two_series.py',BASE/'fast_gaussian_trial_field.py',BASE/'gaussian_trial_field.py',BASE/'audit_t1_deformation.py',BASE/'global_strain_quadrature.py',BASE/'src/independent_artifacts.py',ROOT/'research/two_series_global_strain/PROOF.md',ROOT/'research/two_series_global_strain/verification/results.json']
    paths+=[EXPORT/'results'/name/f for name in NAMES for f in ['summary.json','checkpoint.npz']]
    paths+=[EXPORT/'inputs'/tag/'metadata.json'for tag in ['c068','c074']]
    paths+=[ROOT/'research/gaussian_trial_validation/PROOF.md',ROOT/'research/gaussian_trial_validation/verification/results.json',ROOT/'research/gaussian_trial_validation/verification/fast_results.json']
    hashes={str(p.relative_to(ROOT)):sha256(p)for p in paths}
    if summary.exists():
        rec=json.loads(summary.read_text())
        if rec['source_sha256']!=hashes or rec['chunk']!=a.chunk:raise ValueError('Changed source or configuration')
        for row in rec['batches']:
            if sha256(out/row['file'])!=row['sha256']:raise ValueError('Changed checkpoint')
        if rec['phase']=='complete':print('already complete');return
    else:rec=dict(created_utc=datetime.now(timezone.utc).isoformat(),source_sha256=hashes,levels=LEVELS,names=NAMES,chunk=a.chunk,batches=[],summaries=[],active_wall_seconds=0.,cpu_seconds=0.,scope='Fixed prescribed phi, physical-time source transport, global numerical strain integral. Global source portrait and smooth transport remain hypotheses; successful trajectories at quadrature points are not a global certificate. No interval enclosure. K is held fixed for the scalar compatibility diagnostic.')
    oldwall=rec['active_wall_seconds'];oldcpu=rec['cpu_seconds']
    def checkpoint(phase):
        for name,h in hashes.items():
            if sha256(ROOT/name)!=h:raise RuntimeError('Changed source: '+name)
        rec.update(phase=phase,updated_utc=datetime.now(timezone.utc).isoformat(),active_wall_seconds=oldwall+time.perf_counter()-start,cpu_seconds=oldcpu+time.process_time()-cpu)
        atomic_json(summary,rec);print(phase,len(rec['batches']),rec['active_wall_seconds'],flush=True)
    checkpoint('running');done={(r['name'],r['level'],r['start']):r for r in rec['batches']}
    for name in NAMES:
        field=FastGaussianTrialField(EXPORT,name);meta=dict(field.parameters,K2=field.K**2)
        for level,nr,na,cutoff,source_radius,tol in LEVELS:
            rule=strain_rule(field.c_l,nr,na,cutoff);radii=rule['R'];mu=rule['mu']
            for first in range(0,len(radii),a.chunk):
                if(name,level,first)in done:continue
                if time.perf_counter()-start>a.wall_limit:checkpoint('paused_at_batch_boundary');return
                last=min(len(radii),first+a.chunk);R=radii[first:last,None];r=R*np.sqrt(1-mu[None,:]**2);z=R*mu[None,:]
                got=transport(field,r,z,source_radius=source_radius,rtol=tol,atol=tol/100)
                if not np.all(np.isfinite(got['e'])):raise RuntimeError('Nonfinite transport')
                file=f'{name}_{level}_{first:03d}_{last:03d}.npz';target=out/file
                if target.exists():raise FileExistsError('Unregistered batch: '+file)
                np.savez_compressed(target,R=radii[first:last],radial_weights=rule['radial_weights'][first:last],band=rule['band'][first:last],mu=mu,angular_weights=rule['angular_weights'],h=got['h'],e=got['e'])
                row=dict(name=name,level=level,start=first,stop=last,file=file,sha256=sha256(target),diagnostics={k:v for k,v in got.items()if k not in ['h','e']})
                rec['batches'].append(row);done[name,level,first]=row;checkpoint('batch_complete')
            if any(s['name']==name and s['level']==level for s in rec['summaries']):continue
            rows=sorted([row for row in rec['batches']if row['name']==name and row['level']==level],key=lambda r:r['start']);es=[]
            for row in rows:
                with np.load(out/row['file'],allow_pickle=False)as f:es.append(f['e'])
            values=strain_values(rule,np.concatenate(es));radial=values.pop('radial_contributions');bands=[]
            for b in sorted(set(rule['band'])):
                mask=rule['band']==b;bands.append(dict(band=int(b),lo=None if b==-1 else rule['edges'][b],hi=None if b==-1 else rule['edges'][b+1],S=float(np.sum(radial[mask]))))
            values.update(name=name,level=level,c_l=field.c_l,K2=meta['K2'],saved_S=meta['S'],S_minus_saved=values['S']-meta['S'],strain_defect=2*meta['K2']*values['S']-1,required_K2=(.5/values['S']if values['S']>0 else None),nradial=nr,nangle=na,cutoff=cutoff,source_radius=source_radius,rtol=tol,total_radii=len(radii),max_radius=float(max(radii)),max_endpoint_log_error=max(row['diagnostics']['endpoint_log_error']for row in rows),bands=bands)
            rec['summaries'].append(values);checkpoint('level_complete')
    checkpoint('complete')
if __name__=='__main__':main()
