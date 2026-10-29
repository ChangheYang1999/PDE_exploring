#!/usr/bin/env python3
"""Source-repaired, independently transported vorticity and 5D strain moment."""
from pathlib import Path
from datetime import datetime,timezone
import argparse,json,os,time
import numpy as np
from scipy.integrate import simpson
from source_radial_transport import NativePhi,SourceCoefficients
from radial_transport_solver import angular_grid,angular_moment_weights,radial_step
from piecewise_loading import load_piecewise
from independent_artifacts import atomic_json,atomic_npz,sha256
ROOT=Path(__file__).resolve().parent


def main():
    p=argparse.ArgumentParser();p.add_argument('candidate',type=Path);p.add_argument('--output',type=Path,required=True)
    p.add_argument('--angular',type=int,default=65);p.add_argument('--dx',type=float,default=.04);p.add_argument('--start',type=float,default=1e-4)
    p.add_argument('--K',type=float,default=3.5);p.add_argument('--repair-radius',type=float,default=.3)
    p.add_argument('--cutoffs',type=float,nargs='+',default=[.3,3.,30.,250.,500.,1000.]);p.add_argument('--resume',action='store_true');a=p.parse_args()
    out=a.output.resolve()
    if not out.is_relative_to(ROOT.parent):raise ValueError('Output outside lane')
    if out.exists() and not a.resume:raise FileExistsError('Keep previous audit')
    out.mkdir(parents=True,exist_ok=True);begin=time.perf_counter();cpu=time.process_time();candidate=a.candidate.resolve()
    sources=[Path(__file__),ROOT/'source_radial_transport.py',ROOT/'radial_transport_solver.py',ROOT/'src/piecewise_precision.py',ROOT.parent/'research/source_centered_vorticity_transport/PROOF.md']
    hashes={str(f.relative_to(ROOT.parent)):sha256(f) for f in sources};chash=sha256(candidate)
    model=SourceCoefficients(NativePhi(load_piecewise(candidate)),K=a.K,repair_radius=a.repair_radius)
    mu=angular_grid(a.angular);weights=angular_moment_weights(mu);cutoffs=sorted(set(a.cutoffs))
    if a.start<=0 or a.dx<=0 or cutoffs[0]<=a.start:raise ValueError('Invalid radial grid')
    radii=[a.start]
    for upper in cutoffs:
        radii.extend(np.geomspace(radii[-1],upper,1+int(np.ceil(np.log(upper/radii[-1])/a.dx)))[1:])
    radii=np.asarray(radii);xs=np.log(radii)
    h=model.hz*a.start*mu;eta=np.full_like(mu,model.eta0);moments=[float(weights@eta)];step=0;max_endpoint=0.;max_remap=0.
    config=dict(angular=a.angular,maximum_log_radius_step=a.dx,start_radius=a.start,K=a.K,repair_radius=a.repair_radius,cutoffs=cutoffs)
    result=dict(created_utc=datetime.now(timezone.utc).isoformat(),config=config,candidate_sha256=chash,source_sha256=hashes,
                source=model.source,c_l=model.c_l,source_repair_applied=True,coordinate_convention='Native working coordinates, spherical radius centred at the numerically located source.',
                scope='Independent semi-Lagrangian transport on the Gaussian-repaired saved potential. Piecewise-classical continuation; numerical refinement, not an enclosure or global basin certificate.',
                accumulated_wall_seconds=0.,accumulated_cpu_seconds=0.,bands=[])
    if a.resume:
        result=json.loads((out/'progress.json').read_text())
        if result['config']!=config or result['source_sha256']!=hashes or result['candidate_sha256']!=chash:raise RuntimeError('Resume identity changed')
        with np.load(out/'checkpoint.npz',allow_pickle=False) as old:
            h=old['h'];eta=old['eta'];moments=old['moments'].tolist();step=int(old['step']);max_endpoint=float(old['max_endpoint']);max_remap=float(old['max_remap'])
        if sha256(out/'checkpoint.npz')!=result['checkpoint_sha256']:raise RuntimeError('Inconsistent checkpoint')
    wall_before=result['accumulated_wall_seconds'];cpu_before=result['accumulated_cpu_seconds']
    def save(phase):
        for n,v in hashes.items():
            if sha256(ROOT.parent/n)!=v:raise RuntimeError('Implementation changed')
        if sha256(candidate)!=chash:raise RuntimeError('Candidate changed')
        atomic_npz(out/'checkpoint.npz',dict(h=h,eta=eta,mu=mu,radii=radii[:step+1],moments=np.asarray(moments),step=np.array(step),max_endpoint=np.array(max_endpoint),max_remap=np.array(max_remap)))
        result.update(phase=phase,updated_utc=datetime.now(timezone.utc).isoformat(),completed_steps=step,total_steps=len(xs)-1,
                      radius=float(radii[step]),minimum_sampled_F=model.minimum_F,maximum_endpoint_mu_error=max_endpoint,
                      maximum_gradient_remap_difference=max_remap,accumulated_wall_seconds=wall_before+time.perf_counter()-begin,
                      accumulated_cpu_seconds=cpu_before+time.process_time()-cpu,checkpoint_sha256=sha256(out/'checkpoint.npz'))
        atomic_json(out/'progress.json',result)
        print(json.dumps({k:result[k] for k in ['phase','updated_utc','completed_steps','radius','accumulated_wall_seconds']}),flush=True)
    model(xs[step],mu)
    save('initialized' if not a.resume else 'resumed')
    for j in range(step,len(xs)-1):
        h,eta,check=radial_step(model,xs[j],mu,h,eta,xs[j+1]-xs[j]);step=j+1
        max_endpoint=max(max_endpoint,check['maximum_endpoint_mu_error']);max_remap=max(max_remap,check['maximum_gradient_remap_difference']);moments.append(float(weights@eta))
        if any(abs(radii[step]/r-1)<1e-13 for r in cutoffs):
            previous=result['bands'][-1]['step'] if result['bands'] else 0
            contribution=.75*simpson(radii[previous:step+1]*np.asarray(moments[previous:step+1]),x=xs[previous:step+1])
            total=sum(row['strain_contribution'] for row in result['bands'])+float(contribution)
            power=1+1/model.c_l;tail=.75*radii[step]*moments[-1]/(power-1)
            row=dict(step=step,lower_radius=float(radii[previous]),upper_radius=float(radii[step]),strain_contribution=float(contribution),
                     cumulative_strain_without_inner_ball=total,estimated_tail=float(tail),strain_with_estimated_tail=total+float(tail),
                     minimum_q=float(a.K*np.exp(np.min(h))),maximum_q=float(a.K*np.exp(np.max(h))),maximum_abs_eta=float(np.max(abs(eta))))
            result['bands'].append(row);atomic_npz(out/f'band_{len(result["bands"]):02d}.npz',dict(mu=mu,h=h,eta=eta,radius=np.array(radii[step])))
            save('band_complete')
        elif step%25==0:save('running')
    result['inner_ball_scope']='No inner-ball estimate was added; vary the positive start radius. The constant source eta has exactly zero angular moment.'
    result['tail_scope']='The last tail is a leading-power extrapolation using p=1+1/c_l, not a rigorous remainder bound. Compare multiple cutoffs.'
    result['accepted_as_A']=False;save('complete')


if __name__=='__main__':main()
