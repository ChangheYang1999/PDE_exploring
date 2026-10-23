"""Compare independent physical FD derivatives with saved trainer metrics.

The exact saved holdout is used for this cross-implementation comparison. It is
not independent sampling evidence and not a training/holdout-gap measurement.
"""
from __future__ import annotations
import argparse
import hashlib
import io
import json
from pathlib import Path
import numpy as np
from checkpoint import load
from core import differentiate,residuals,stats
from evaluate import ROOT,Interval,atomic_json,utc

EDGES=[(0.,1.,'D1_R<1'),(1.,3.,'D2_1-3'),(3.,10.,'D3_3-10'),(10.,100.,'D4_10-100'),(100.,1000.,'D5_100-1e3'),(1000.,1e5,'D6_1e3-1e5')]

def snapshot(path):
    path=Path(path)
    if path.stat().st_size>512*1024**2:raise ValueError('Snapshot exceeds 512 MiB')
    data=path.read_bytes();digest=hashlib.sha256(data).hexdigest()
    target=ROOT/'snapshots'/(digest+path.suffix)
    if not target.exists():target.write_bytes(data)
    return target,digest,data

def norms(points,weights,values,J,c_l,C):
    r=residuals(points,values,J,None,c_l,C)
    radii=np.linalg.norm(points,axis=1);out={}
    for lo,hi,name in EDGES:
        m=(radii>=lo)&(radii<hi)
        if np.sum(m)<10:continue
        def l2(v):return float(np.sqrt(np.sum(weights[m]*np.sum(v[m]**2,axis=1))))
        terms=[l2(t) for t in r['momentum_terms']]
        numerator=l2(r['momentum']);den=sum(terms)
        legacy_den=den+(abs(C)-1)*terms[2]
        nonlinear=terms[3]+terms[4]
        out[name]=dict(sample_count=int(m.sum()),estimated_volume=float(weights[m].sum()),
            momentum_L2=numerator,term_L2=terms,denominator=den,
            eps_m=numerator/den if den else None,
            eps_m_legacy_C=numerator/legacy_den if legacy_den else None,
            eps_nl=numerator/nonlinear if nonlinear else None)
    return out

def compare(checkpoint,holdout,steps=(.002,.001),reference_measure='legacy'):
    if reference_measure not in ('legacy','disjoint'):
        raise ValueError('Reference measure must be explicitly legacy or disjoint')
    ck_path,ck_sha,_=snapshot(checkpoint)
    h_path,h_sha,h_data=snapshot(holdout)
    import torch
    torch.set_num_threads(1)
    saved=torch.load(io.BytesIO(h_data),map_location='cpu',weights_only=False)
    model=load(ck_path)
    reference=model.metadata['checkpoint_metadata'].get('val',{})
    if not reference:raise ValueError('A best checkpoint with saved val metrics is required')
    groups={name:(a.detach().cpu().numpy().astype(np.float64),w.detach().cpu().numpy().astype(np.float64)) for name,(a,w) in saved.items()}
    names=list(groups);lengths=[len(groups[k][0]) for k in names]
    points=np.concatenate([groups[k][0] for k in names]);weights=np.concatenate([groups[k][1] for k in names])
    labels=np.concatenate([np.full(len(groups[k][0]),k) for k in names]);mask=np.isin(labels,['core','shell'])
    result=dict(created_utc=utc(),checkpoint_sha256=ck_sha,holdout_sha256=h_sha,
        checkpoint_snapshot=str(ck_path.relative_to(ROOT)),holdout_snapshot=str(h_path.relative_to(ROOT)),
        model_metadata=model.metadata,groups=dict(zip(names,lengths)),refinements=[],reference_measure=reference_measure,
        scope='Matched trainer holdout and independent NumPy/FD derivatives. Both legacy support-multiplicity and disjoint core+shell measures are reported; the declared reference_measure alone is compared to saved values. This is not a training/holdout gap.')
    with Interval('matched-holdout-'+ck_sha[:16],dict(checkpoint=ck_sha,holdout=h_sha,steps=steps,reference_measure=reference_measure),ck_sha):
        previous=None
        for step in steps:
            vs=[];js=[]
            for start in range(0,len(points),256):
                y=points[start:start+256]
                value,j,_=differentiate(model,y,order=6,hessian=False,steps=step*np.maximum(1.,abs(y)))
                vs.append(value);js.append(j)
            values=np.concatenate(vs);J=np.concatenate(js)
            legacy=norms(points,weights,values,J,model.c_l,model.C)
            corrected=norms(points[mask],weights[mask],values[mask],J[mask],model.c_l,model.C)
            matched={}
            selected=legacy if reference_measure=='legacy' else corrected
            selected_momentum_key='eps_m_legacy_C' if reference_measure=='legacy' else 'eps_m'
            sample_count_checks={}
            for region,row in selected.items():
                ref_count=reference.get('n_'+region)
                sample_count_checks[region]=dict(independent=row['sample_count'],trainer=ref_count,
                    agrees=(int(ref_count)==row['sample_count']) if ref_count is not None else None)
                for own_key,ref_key in [(selected_momentum_key,'eps_m_'),('eps_nl','eps_nl_')]:
                    ref=reference.get(ref_key+region)
                    if ref is not None and row[own_key] is not None:
                        matched[ref_key+region]=dict(independent=row[own_key],trainer=float(ref),
                            absolute_difference=abs(row[own_key]-ref),relative_difference=abs(row[own_key]-ref)/abs(ref) if ref else None)
            sampler_scaled={}
            r=residuals(points,values,J,None,model.c_l,model.C)
            d=1-1/model.c_l
            for name in names:
                m=labels==name;s=np.sum(points[m]**2,axis=1)/model.l_env**2
                for suffix,exponent in [('nl',2*d-1),('lin',d)]:
                    scaled=np.linalg.norm(r['momentum'][m],axis=1)/(1+s)**(.5*exponent)
                    own=float(np.sqrt(np.mean(scaled**2)));ref=reference.get('val_mom_'+name+'_rms_'+suffix)
                    sampler_scaled[name+'_'+suffix]=dict(independent=own,trainer=ref,
                        absolute_difference=abs(own-ref) if ref is not None else None)
            f0,j0,_=differentiate(model,np.zeros((1,3)),step=step,order=6,hessian=False)
            origin=dict(U0=f0[0,:3].tolist(),P0=float(f0[0,3]),gradU0=j0[0,:3].tolist(),
                U0_z_abs_difference=abs(float(f0[0,2])-reference['U0_z']),
                P0_abs_difference=abs(float(f0[0,3])-reference['P0']),
                gradU0_max_abs_difference=float(np.max(abs(j0[0,:3]-np.asarray(reference['gradU0'])))))
            row=dict(step_rule='h_j=step*max(1,abs(y_j))',step=step,legacy_overlap_norms=legacy,
                     physical_core_shell_norms=corrected,matched_saved_metrics=matched,sample_count_checks=sample_count_checks,
                     sampler_envelope_scaled_metrics=sampler_scaled,origin_comparison=origin)
            if previous is not None:row['gradient_refinement_difference']=stats(J-previous)
            previous=J
            result['refinements'].append(row)
            print('step',step,'origin grad difference',origin['gradU0_max_abs_difference'],
                  'max eps difference',max(m['absolute_difference'] for m in matched.values()),flush=True)
    result['cross_implementation_passed']=bool(max(m['relative_difference'] or 0 for m in result['refinements'][-1]['matched_saved_metrics'].values())<1e-6 and result['refinements'][-1]['origin_comparison']['gradU0_max_abs_difference']<1e-8 and all(row['agrees'] is not False for row in result['refinements'][-1]['sample_count_checks'].values()))
    output=ROOT/'evidence'/('reference-compare-'+ck_sha[:16]+'-'+reference_measure+'.json')
    atomic_json(output,result)
    return output

def main():
    p=argparse.ArgumentParser();p.add_argument('checkpoint');p.add_argument('holdout')
    p.add_argument('--reference-measure',choices=['legacy','disjoint'],required=True)
    a=p.parse_args()
    print(compare(a.checkpoint,a.holdout,reference_measure=a.reference_measure))
if __name__=='__main__':main()
