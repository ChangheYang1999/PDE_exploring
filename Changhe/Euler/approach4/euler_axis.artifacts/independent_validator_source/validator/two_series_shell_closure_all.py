#!/usr/bin/env python3
"""All seven prescribed fields, with a tighter source cutoff and ODE tolerance."""
from pathlib import Path
from datetime import datetime,timezone
import argparse,json,time
import numpy as np
from scipy.special import roots_legendre
from fast_two_series import FastTwoSeries
from audit_t1_deformation import transport
from independent_artifacts import atomic_json,sha256
BASE=Path(__file__).resolve().parent;ROOT=BASE.parent
EXPORT=BASE/'external_exports/T1_two_series_20261029T012051.154539Z'
LEVELS=[('fine',128,1e-6,5e-12),('reference',256,1e-6,5e-12)]
def field_path(name):
    return EXPORT/('results/best' if name=='free' else 'results/ladder')/name

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output',required=True,type=Path);ap.add_argument('--wall-limit',type=float,default=235);ap.add_argument('--chunk',type=int,default=9);a=ap.parse_args()
    out=a.output.resolve()
    if not out.is_relative_to(ROOT):raise ValueError('Output outside lane')
    out.mkdir(exist_ok=True,parents=True);summary=out/'summary.json';start=time.perf_counter();cpu=time.process_time()
    paths=[Path(__file__),BASE/'fast_two_series.py',BASE/'audit_t1_deformation.py',BASE/'src/independent_artifacts.py',ROOT/'research/characteristic_shell_closure/PROOF.md',ROOT/'research/characteristic_shell_closure/verification/results.json']
    paths+=[field_path(name)/f for name in ['c068_n08','c068_n16','c068_n24','c074_n08','c074_n16','c074_n24','free']for f in ['metadata.json','grid.npz']]
    hashes={str(p.relative_to(ROOT)):sha256(p)for p in paths}
    if summary.exists():
        rec=json.loads(summary.read_text())
        if rec['source_sha256']!=hashes or rec['chunk']!=a.chunk:raise ValueError('Changed source or configuration')
        for row in rec['batches']:
            if sha256(out/row['file'])!=row['sha256']:raise ValueError('Changed checkpoint')
        if rec['phase']=='complete':print('already complete');return
    else:
        rec=dict(created_utc=datetime.now(timezone.utc).isoformat(),source_sha256=hashes,levels=LEVELS,chunk=a.chunk,batches=[],summaries=[],active_wall_seconds=0.,cpu_seconds=0.,scope='Fixed prescribed phi; source-normalized physical-time transport at every shell node. Finite-shell diagnostic, not a global residual bound. Stored K is retained; S is not recomputed. Active time is a checkpointed lower bound if a process was killed between checkpoints.')
    oldwall=rec['active_wall_seconds'];oldcpu=rec['cpu_seconds']
    def checkpoint(phase):
        for name,h in hashes.items():
            if sha256(ROOT/name)!=h:raise RuntimeError('Changed source: '+name)
        rec.update(phase=phase,updated_utc=datetime.now(timezone.utc).isoformat(),active_wall_seconds=oldwall+time.perf_counter()-start,cpu_seconds=oldcpu+time.process_time()-cpu)
        atomic_json(summary,rec);print(phase,len(rec['batches']),rec['active_wall_seconds'],flush=True)
    checkpoint('running')
    done={(r['name'],r['level'],r['start']):r for r in rec['batches']}
    for name in ['c068_n08','c068_n16','c068_n24','c074_n08','c074_n16','c074_n24','free']:
        path=field_path(name);meta=json.loads((path/'metadata.json').read_text());field=FastTwoSeries(meta);K2=float(meta['K2'])
        with np.load(path/'grid.npz',allow_pickle=False)as grid:
            radii=grid['shell_R'].copy();ref_mu=grid['shell_mu'].copy();ref_weights=grid['shell_weights'].copy();saved_eta=grid['shell_eta'].copy();saved_eps=grid['shell_eps'].copy()
        if len(radii)!=81 or np.any(np.diff(radii)<=0):raise ValueError('Unexpected radial grid')
        for level,na,cutoff,tol in LEVELS:
            if level=='reference':mu=ref_mu;weights=ref_weights
            else:
                mu,weights=roots_legendre(na);mu=(mu+1)/2;weights=weights/2
            if len(mu)!=na or np.any(mu<=0) or np.any(mu>=1) or abs(weights.sum()-1)>1e-12:raise ValueError('Angular grid')
            for first in range(0,len(radii),a.chunk):
                if (name,level,first)in done:continue
                if time.perf_counter()-start>a.wall_limit:checkpoint('paused_at_batch_boundary');return
                last=min(len(radii),first+a.chunk);R=radii[first:last,None];r=R*np.sqrt(1-mu[None,:]**2);z=R*mu[None,:]
                got=transport(field,r,z,source_radius=cutoff,rtol=tol,atol=tol/100)
                eta=K2*got['e'];elliptic=field.jets(r,z)['eta_phi'];num=np.sum(weights*(elliptic-eta)**2,axis=1);den=np.sum(weights*eta**2,axis=1)
                if not np.all(np.isfinite(eta))or np.any(den<=0):raise RuntimeError('Invalid transported vorticity')
                eps=np.sqrt(num/den);file=f'{name}_{level}_{first:02d}_{last:02d}.npz';target=out/file
                if target.exists():raise FileExistsError('Unregistered batch file: '+file)
                np.savez_compressed(target,R=radii[first:last],mu=mu,weights=weights,h=got['h'],e=got['e'],eta=eta,elliptic_eta=elliptic,eps=eps,numerator=num,denominator=den)
                row=dict(name=name,level=level,start=first,stop=last,nangle=na,file=file,sha256=sha256(target),diagnostics={k:v for k,v in got.items()if k not in ['h','e']})
                if level=='reference':
                    delta=eta-saved_eta[first:last];saved_den=np.sum(weights*saved_eta[first:last]**2,axis=1)
                    row['saved_eta_shell_relative_errors']=np.sqrt(np.sum(weights*delta**2,axis=1)/saved_den).tolist();row['saved_eta_max_abs_error']=float(np.max(abs(delta)))
                rec['batches'].append(row);done[name,level,first]=row;checkpoint('batch_complete')
            if any(t['name']==name and t['level']==level for t in rec['summaries']):continue
            rows=sorted([r for r in rec['batches']if r['name']==name and r['level']==level],key=lambda r:r['start']);eps=[]
            for row in rows:
                with np.load(out/row['file'],allow_pickle=False)as f:eps.extend(f['eps'].tolist())
            eps=np.array(eps)
            if len(eps)!=len(radii):raise RuntimeError('Incomplete level')
            k=int(np.argmax(eps));bands=[]
            for lo,hi in [(.02,.2),(.2,3.),(3.,50.)]:
                mask=(radii>=lo*(1-1e-12))&(radii<=hi*(1+1e-12));bands.append(dict(lo=lo,hi=hi,count=int(mask.sum()),rms=float(np.sqrt(np.mean(eps[mask]**2))),maximum=float(np.max(eps[mask]))))
            rec['summaries'].append(dict(name=name,level=level,c_l=meta['c'],K2=K2,source_radius=cutoff,rtol=tol,radial_count=len(radii),nangle=na,E=float(np.sqrt(np.mean(eps**2))),saved_E=meta['E'],E_minus_saved=float(np.sqrt(np.mean(eps**2))-meta['E']),max_eps=float(eps[k]),R_at_max=float(radii[k]),eps=eps.tolist(),max_shell_eps_difference_from_saved=float(np.max(abs(eps-saved_eps))),bands=bands,max_endpoint_log_error=max(row['diagnostics']['endpoint_log_error']for row in rows)))
            checkpoint('level_complete')
    checkpoint('complete')
if __name__=='__main__':main()
