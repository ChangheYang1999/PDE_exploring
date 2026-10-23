"""Matched residual diagnostics for a recovered last batch and saved holdout."""
from __future__ import annotations
import argparse,hashlib,io,json
from pathlib import Path
import numpy as np
from checkpoint import load
from core import differentiate,residuals,stats
from reference_compare import norms,snapshot
from evaluate import ROOT,Interval,atomic_json,utc

def run(replay_file):
    replay=json.loads(Path(replay_file).read_text())
    if not replay.get('endpoint_exact'):raise ValueError('Exact RNG endpoint verification required')
    checkpoint=ROOT/replay['checkpoint_snapshot'];bp=ROOT/replay['batch_snapshot'];hp=ROOT/replay['holdout_snapshot']
    for p,key in [(checkpoint,'checkpoint_sha256'),(bp,'batch_sha256'),(hp,'holdout_sha256')]:
        if hashlib.sha256(p.read_bytes()).hexdigest()!=replay[key]:raise ValueError('Input digest mismatch: '+str(p))
    model=load(checkpoint)
    with np.load(bp,allow_pickle=False) as f:
        train={name:(f[name+'_points'],f[name+'_weights']) for name in ('core','shell','axis','origin') if name+'_points' in f}
    import torch
    torch.set_num_threads(1)
    val={name:(a.numpy(),w.numpy()) for name,(a,w) in torch.load(io.BytesIO(hp.read_bytes()),map_location='cpu',weights_only=False).items()}
    result=dict(created_utc=utc(),checkpoint_sha256=replay['checkpoint_sha256'],global_step=replay['global_step'],training_replay_evidence=str(Path(replay_file)),holdout_sha256=replay['holdout_sha256'],refinements=[],scope='Same frozen physical fields and same diagnostics on one recovered final training batch and the saved holdout. This empirical last-batch gap is not a population generalization bound, a full training-set statistic or an exponent confidence interval. No gauge penalty is included.')
    with Interval('training-holdout-gap-'+replay['checkpoint_sha256'][:16],dict(checkpoint=replay['checkpoint_sha256'],batch=replay['batch_sha256']),replay['checkpoint_sha256']):
        for step in (.002,.001):
            comparison={}
            for label,groups in [('last_training_batch',train),('saved_holdout',val)]:
                names=list(groups);points=np.concatenate([groups[k][0] for k in names]);weights=np.concatenate([groups[k][1] for k in names]);labels=np.concatenate([np.full(len(groups[k][0]),k) for k in names]);values=[];jac=[]
                for i in range(0,len(points),256):
                    x=points[i:i+256];v,j,_=differentiate(model,x,order=6,hessian=False,steps=step*np.maximum(1.,abs(x)));values.append(v);jac.append(j)
                values=np.concatenate(values);jac=np.concatenate(jac);r=residuals(points,values,jac,None,model.c_l,model.C);mask=np.isin(labels,['core','shell'])
                physical=norms(points[mask],weights[mask],values[mask],jac[mask],model.c_l,model.C);by_sampler={};d=1-1/model.c_l
                for name in names:
                    m=labels==name;base=1+np.sum(points[m]**2,axis=1)/model.l_env**2
                    by_sampler[name]=dict(n=int(m.sum()),absolute=stats(r['momentum'][m]),linear_scaled=stats(r['momentum'][m]/base[:,None]**(.5*d)),nonlinear_scaled=stats(r['momentum'][m]/base[:,None]**(.5*(2*d-1))))
                comparison[label]=dict(physical_core_shell=physical,sampler_metrics=by_sampler)
                print(label,'step',step,'complete',flush=True)
            ratios={}
            for name,t in comparison['last_training_batch']['sampler_metrics'].items():
                h=comparison['saved_holdout']['sampler_metrics'][name]
                ratios[name]={key:h[key]['rms']/t[key]['rms'] if t[key]['rms'] else None for key in ('absolute','linear_scaled','nonlinear_scaled')}
            regional={}
            for name,t in comparison['last_training_batch']['physical_core_shell'].items():
                h=comparison['saved_holdout']['physical_core_shell'].get(name)
                if h:regional[name]={key:h[key]/t[key] if t[key] else None for key in ('eps_m','eps_nl')}
            result['refinements'].append(dict(step=step,datasets=comparison,holdout_over_last_training_batch_sampler_rms=ratios,holdout_over_last_training_batch_regional_ratios=regional))
    p=ROOT/'evidence'/f'training-holdout-gap-{replay["checkpoint_sha256"][:16]}.json';atomic_json(p,result);print(p,flush=True)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('replay_evidence');a=p.parse_args();run(a.replay_evidence)
