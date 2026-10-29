#!/usr/bin/env python3
"""Independent fixed-K transport near the first compact spline knots."""
from pathlib import Path
from datetime import datetime,timezone
import argparse,json,time
import numpy as np
from scipy.special import roots_legendre
from nested_trial_field import NestedTrialField
from audit_t1_deformation import transport
from independent_artifacts import atomic_json,sha256
BASE=Path(__file__).resolve().parent;ROOT=BASE.parent
LEVELS=[('inner64',64,'inner'),('inner128',128,'inner')]
def main():
    ap=argparse.ArgumentParser();ap.add_argument('registration',type=Path);ap.add_argument('--checks',type=Path,required=True);ap.add_argument('--output',type=Path,required=True);ap.add_argument('--wall-limit',type=float,default=230);ap.add_argument('--chunk',type=int,default=3);a=ap.parse_args()
    out=a.output.resolve();registration=a.registration.resolve();audit_path=a.checks.resolve()
    audit=json.loads(audit_path.read_text())
    if not audit.get('passed'):raise ValueError('Operator audit did not pass')
    expected=str(registration.relative_to(ROOT))
    if audit.get('source_sha256',{}).get(expected)!=sha256(registration):raise ValueError('Operator audit is for a different registration')
    for rel,digest in audit['source_sha256'].items():
        if sha256(ROOT/rel)!=digest:raise ValueError('Changed audited source: '+rel)
    if not out.is_relative_to(ROOT)or a.chunk<1:raise ValueError('Invalid output or chunk')
    out.mkdir(exist_ok=True,parents=True);summary=out/'summary.json';start=time.perf_counter();cpu=time.process_time();field=NestedTrialField(registration);K2=field.K**2
    paths=[Path(__file__),BASE/'nested_trial_field.py',BASE/'fast_gaussian_trial_field.py',BASE/'gaussian_trial_field.py',BASE/'fast_two_series.py',BASE/'audit_t1_deformation.py',BASE/'src/independent_artifacts.py',registration,ROOT/'research/nested_trial_validation/PROOF.md',audit_path]
    paths+=[ROOT/path for path in field.record['input_sha256']]
    paths+=[field.start.export/'results'/field.start.name/p for p in ['checkpoint.npz','summary.json']]
    paths+=[field.start.export/'inputs'/field.parameters['tag']/'metadata.json']
    hashes={str(p.relative_to(ROOT)):sha256(p)for p in paths}
    if summary.exists():
        rec=json.loads(summary.read_text())
        if rec['source_sha256']!=hashes or rec['chunk']!=a.chunk:raise ValueError('Changed source or configuration')
        for row in rec['batches']:
            if sha256(out/row['file'])!=row['sha256']:raise ValueError('Changed checkpoint')
        if rec['phase']=='complete':print('already complete');return
    else:rec=dict(created_utc=datetime.now(timezone.utc).isoformat(),source_sha256=hashes,name=field.name,operator_audit=str(audit_path.relative_to(ROOT)),levels=LEVELS,chunk=a.chunk,batches=[],summaries=[],active_wall_seconds=0.,cpu_seconds=0.,scope='Fixed frozen C4 potential and stored K; independent physical-time transport. Finite inner-shell numerical diagnostic around the first compact spline knots, including the primary reported R=0.001023. No uniform residual bound or full primitive Euler acceptance.')
    oldwall=rec['active_wall_seconds'];oldcpu=rec['cpu_seconds']
    def checkpoint(phase):
        for path,h in hashes.items():
            if sha256(ROOT/path)!=h:raise RuntimeError('Changed source: '+path)
        rec.update(phase=phase,updated_utc=datetime.now(timezone.utc).isoformat(),active_wall_seconds=oldwall+time.perf_counter()-start,cpu_seconds=oldcpu+time.process_time()-cpu)
        atomic_json(summary,rec);print(phase,len(rec['batches']),rec['active_wall_seconds'],flush=True)
    checkpoint('running');done={(r['level'],r['start']):r for r in rec['batches']}
    with np.load(field.export/'results'/field.name/'grid.npz',allow_pickle=False)as g:
        core_x=g['shell_x'].copy();far_x=g['far_shell_x'][::2].copy();saved_eta=g['shell_eta'].copy();saved_eps=g['shell_eps'].copy();saved_mu=g['shell_mu'].copy();saved_weights=g['shell_weights'].copy()
    for level,na,region in LEVELS:
        radii=np.unique(np.r_[np.exp(np.r_[-9.,-8.,-7.2,np.linspace(-7.,-6.6,21),-6.]),0.001023])
        mu,weights=roots_legendre(na);mu=(mu+1)/2;weights=weights/2
        if level=='core256':mu=saved_mu;weights=saved_weights
        if len(mu)!=na or np.any(mu<=0)or np.any(mu>=1)or abs(weights.sum()-1)>1e-12:raise ValueError('Angular grid')
        for first in range(0,len(radii),a.chunk):
            if(level,first)in done:continue
            if time.perf_counter()-start>a.wall_limit:checkpoint('paused_at_batch_boundary');return
            last=min(len(radii),first+a.chunk);R=radii[first:last,None];r=R*np.sqrt(1-mu[None,:]**2);z=R*mu[None,:]
            got=transport(field,r,z,source_radius=1e-6,rtol=5e-12,atol=5e-14)
            eta=K2*got['e'];elliptic=field.jets(r,z)['eta_phi'];num=np.sum(weights*(elliptic-eta)**2,axis=1);den=np.sum(weights*eta**2,axis=1)
            if not np.all(np.isfinite(eta))or np.any(den<=0):raise RuntimeError('Invalid transported vorticity')
            eps=np.sqrt(num/den);file=f'{level}_{first:03d}_{last:03d}.npz';target=out/file
            if target.exists():raise FileExistsError('Unregistered batch file: '+file)
            np.savez_compressed(target,R=radii[first:last],mu=mu,weights=weights,h=got['h'],e=got['e'],eta=eta,elliptic_eta=elliptic,eps=eps,numerator=num,denominator=den)
            row=dict(level=level,region=region,start=first,stop=last,nangle=na,file=file,sha256=sha256(target),diagnostics={k:v for k,v in got.items()if k not in ['h','e']})
            if level=='core256':
                delta=eta-saved_eta[first:last];saved_den=np.sum(weights*saved_eta[first:last]**2,axis=1)
                row['saved_eta_shell_relative_errors']=np.sqrt(np.sum(weights*delta**2,axis=1)/saved_den).tolist();row['saved_eta_max_abs_error']=float(np.max(abs(delta)))
            rec['batches'].append(row);done[level,first]=row;checkpoint('batch_complete')
        if any(t['level']==level for t in rec['summaries']):continue
        rows=sorted([r for r in rec['batches']if r['level']==level],key=lambda r:r['start']);eps=[]
        for row in rows:
            with np.load(out/row['file'],allow_pickle=False)as f:eps.extend(f['eps'].tolist())
        eps=np.array(eps)
        if len(eps)!=len(radii):raise RuntimeError('Incomplete level')
        k=int(np.argmax(eps));bands=[]
        for lo,hi in [(1e-4,5e-4),(5e-4,2e-3),(2e-3,3e-3)]:
            mask=(radii>=lo*(1-1e-12))&(radii<=hi*(1+1e-12))
            if mask.any():bands.append(dict(lo=lo,hi=hi,count=int(mask.sum()),rms=float(np.sqrt(np.mean(eps[mask]**2))),maximum=float(np.max(eps[mask]))))
        item=dict(level=level,region=region,c_l=field.c_l,K2=K2,source_radius=1e-6,rtol=5e-12,radial_count=len(radii),nangle=na,E=float(np.sqrt(np.mean(eps**2))),max_eps=float(eps[k]),R_at_max=float(radii[k]),eps=eps.tolist(),bands=bands,max_endpoint_log_error=max(row['diagnostics']['endpoint_log_error']for row in rows))
        if region=='core':item.update(saved_E=field.parameters['E'],E_minus_saved=item['E']-field.parameters['E'],max_shell_eps_difference_from_saved=float(np.max(abs(eps-saved_eps))))
        rec['summaries'].append(item);checkpoint('level_complete')
    checkpoint('complete')
if __name__=='__main__':main()
