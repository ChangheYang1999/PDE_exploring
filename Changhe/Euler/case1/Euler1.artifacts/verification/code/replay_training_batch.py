"""Recover one stage-zero last batch only after exact RNG endpoint verification.

The draw order is transcribed from the documented sampler. No trainer module is
imported. Calibration requires exact agreement with the archived holdout arrays.
Sampler replay is data reconstruction and receives no campaign-time credit.
"""
from __future__ import annotations
import argparse,hashlib,io,json,math,time
from pathlib import Path
import numpy as np
import torch
from evaluate import ROOT,atomic_json,utc
from reference_compare import snapshot

torch.set_num_threads(1)
torch.set_default_dtype(torch.float64)
NAMES=('core','shell','axis','origin')

def draw(g,c,counts,positions=True):
    result={}
    for name in NAMES:
        n=int(counts.get('n_'+name,0))
        if n<=0:continue
        if name in ('core','shell','origin'):
            u=torch.rand(n,1,generator=g,dtype=torch.float64)
            v=torch.randn(n,3,generator=g,dtype=torch.float64)
            if not positions:continue
            direction=v/v.norm(dim=-1,keepdim=True)
            if name=='shell':
                width=math.log(c['R_max'])-math.log(c['R_core'])
                radius=torch.exp(math.log(c['R_core'])+u*width)
                y=radius*direction
                w=4*math.pi*radius[:,0]**3*width/n
            else:
                radius=c['R_core'] if name=='core' else c.get('R_origin',.5)
                y=radius*u**(1/3)*direction
                w=torch.full((n,),4/3*math.pi*radius**3/n,dtype=torch.float64)
        else:
            ur=torch.rand(n,generator=g,dtype=torch.float64)
            ut=torch.rand(n,generator=g,dtype=torch.float64)
            uz=torch.rand(n,generator=g,dtype=torch.float64)
            us=torch.rand(n,generator=g,dtype=torch.float64)
            if not positions:continue
            rt=c['r_tube'];zmin=c.get('z_min',.01)
            width=math.log(c['R_max'])-math.log(zmin)
            radius=rt*torch.sqrt(ur);angle=2*math.pi*ut
            az=torch.exp(math.log(zmin)+uz*width)
            signs=torch.where(us<.5,-1.,1.)
            y=torch.stack([radius*torch.cos(angle),radius*torch.sin(angle),signs*az],-1)
            w=math.pi*rt**2*2*az*width/n
        result[name]=(y,w)
    return result

def state_hash(g):return hashlib.sha256(g.get_state().numpy().tobytes()).hexdigest()

def replay(checkpoint,holdout):
    path,sha,data=snapshot(checkpoint);hp,hsha,hd=snapshot(holdout)
    ck=torch.load(io.BytesIO(data),map_location='cpu',weights_only=False)
    val=torch.load(io.BytesIO(hd),map_location='cpu',weights_only=False)
    cfg=ck['cfg'];state=ck['state'];stage=cfg['stages'][0]
    if state['stage']!=0 or state['step']!=state['global_step'] or state['step']<=0 or state.get('nan_count',0):
        raise ValueError('Replay implemented only for stage zero, positive matching step count and no NaN steps')
    if int(stage.get('resample_every',1))!=1:raise ValueError('Requires a fresh batch on every step')
    if 'sampler' not in ck:raise ValueError('Full sampler-state checkpoint required')
    base=dict(cfg['sampling']);seed=int(cfg['rng_seed'])
    vc=cfg.get('val_counts',dict(n_core=4096,n_shell=4096,n_axis=1024,n_origin=512))
    gen=torch.Generator().manual_seed(seed+7919);reconstructed=draw(gen,base,vc)
    calibration={name:dict(points_exact=torch.equal(reconstructed[name][0],pair[0].cpu()),weights_exact=torch.equal(reconstructed[name][1],pair[1].cpu()),max_point_difference=float(torch.max(abs(reconstructed[name][0]-pair[0].cpu()))),max_weight_difference=float(torch.max(abs(reconstructed[name][1]-pair[1].cpu())))) for name,pair in val.items()}
    if not all(r['points_exact'] and r['weights_exact'] for r in calibration.values()):
        atomic_json(ROOT/'evidence'/f'training-replay-{sha[:16]}-failure.json',dict(date_utc=utc(),calibration=calibration))
        raise ValueError('Sampler calibration did not reproduce archived holdout arrays exactly')
    base.update(stage.get('sampling',{}));counts=dict(cfg.get('counts',dict(n_core=4096,n_shell=4096,n_axis=1024,n_origin=512)));counts.update(stage.get('counts',{}))
    if base!=ck['sampler'].get('cfg'):raise ValueError('Saved sampler configuration differs from reconstructed stage')
    gen=torch.Generator().manual_seed(seed+1);last=None;start=time.monotonic();before=None
    for i in range(state['step']):
        if i==state['step']-1:before=gen.get_state().clone()
        last=draw(gen,base,counts,positions=(i==state['step']-1))
        if (i+1)%500==0:print('replayed',i+1,'elapsed',time.monotonic()-start,flush=True)
    matches=torch.equal(gen.get_state(),ck['sampler']['g'].cpu())
    result=dict(date_utc=utc(),checkpoint_sha256=sha,holdout_sha256=hsha,checkpoint_snapshot=str(path.relative_to(ROOT)),holdout_snapshot=str(hp.relative_to(ROOT)),calibration=calibration,stage=0,global_step=state['global_step'],counts=counts,sampling=base,rng_seed=seed+1,torch_version=torch.__version__,endpoint_exact=matches,replayed_endpoint_sha256=state_hash(gen),saved_endpoint_sha256=hashlib.sha256(ck['sampler']['g'].cpu().numpy().tobytes()).hexdigest(),scope='One last stage-zero training batch, recovered by full deterministic sampler replay and exact saved-RNG endpoint match. No trainer module imported; no numerical activity credit for replay.')
    if matches:
        out=ROOT/'snapshots'/f'training-batch-{sha[:16]}.npz'
        arrays={name+'_'+k:t.numpy() for name,pair in last.items() for k,t in zip(('points','weights'),pair)}
        arrays['rng_before']=before.numpy();arrays['rng_after']=gen.get_state().numpy();np.savez(out,**arrays)
        result.update(batch_snapshot=str(out.relative_to(ROOT)),batch_sha256=hashlib.sha256(out.read_bytes()).hexdigest())
    atomic_json(ROOT/'evidence'/f'training-replay-{sha[:16]}.json',result)
    if not matches:raise ValueError('RNG endpoint mismatch; no recovered training batch is asserted')
    print('EXACT endpoint match',result['batch_snapshot'],flush=True)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('checkpoint');p.add_argument('holdout');args=p.parse_args();replay(args.checkpoint,args.holdout)
