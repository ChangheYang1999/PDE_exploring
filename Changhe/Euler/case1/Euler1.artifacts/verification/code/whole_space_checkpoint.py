"""Tail-inclusive finite quadrature for a saved profile, with shared FD sources."""
from __future__ import annotations
import argparse
import numpy as np
from checkpoint import load
from core import differentiate,curl,stats
from evaluate import ROOT,Interval,atomic_json,utc
from whole_space import sphere_quadrature


def joint_integral(model,targets,nmu,nrad,max_radius,on_partial=None):
    directions,wa=sphere_quadrature(nmu,2*nmu)
    nodes,weights=np.polynomial.legendre.leggauss(nrad)
    boundaries=[0.,.25,.5,1.,2.,4.]
    while boundaries[-1]<max_radius:boundaries.append(min(max_radius,2*boundaries[-1]))
    pressure=np.zeros((len(targets),3));velocity=pressure.copy();partial=[]
    for low,high in zip(boundaries,boundaries[1:]):
        rad=low+(nodes+1)*(high-low)/2;wr=weights*(high-low)/2
        shifts=(rad[:,None,None]*directions[None,:,:]).reshape(-1,3)
        ns=np.tile(directions,(nrad,1));ws=(wr[:,None]*wa[None,:]).ravel()
        for i,target in enumerate(targets):
            x=shifts+target
            for start in range(0,len(x),256):
                y=x[start:start+256];n=ns[start:start+256];w=ws[start:start+256]
                _,J,_=differentiate(model,y,order=6,hessian=False,steps=.002*np.maximum(1.,abs(y)))
                gu=J[:,:3];source=np.einsum('nij,nji->n',gu,gu);om=curl(gu)
                pressure[i]+=np.sum(w[:,None]*n*source[:,None],axis=0)
                velocity[i]+=np.sum(w[:,None]*np.cross(n,om),axis=0)
        row=dict(outer_radius=high,pressure_gradient=pressure.tolist(),velocity=velocity.tolist())
        partial.append(row)
        if on_partial:on_partial(partial)
    values,J,_=differentiate(model,targets,step=.001,order=6,hessian=False)
    return dict(nmu=nmu,nphi=2*nmu,nrad_per_interval=nrad,max_radius=max_radius,
        targets=targets.tolist(),pressure_gradient=pressure.tolist(),velocity=velocity.tolist(),
        provided_pressure_gradient=J[:,3].tolist(),provided_velocity=values[:,:3].tolist(),
        pressure_gradient_difference=stats(pressure-J[:,3]),velocity_difference=stats(velocity-values[:,:3]),
        partial_integrals=partial,source_derivatives='physical FD6, h_j=.002 max(1,abs(y_j))',
        scope='Numerical quadrature over balls centered at each target. No rigorous quadrature or exterior error enclosure.')


def main():
    p=argparse.ArgumentParser();p.add_argument('checkpoint');p.add_argument('--max-radius',type=float,default=256.);a=p.parse_args()
    model=load(a.checkpoint);sha=model.metadata['checkpoint_sha256'];output=ROOT/'evidence'/('whole-space-'+sha[:16]+'.json')
    targets=np.array([[0.,0.,0.],[.7,.1,-.4],[0.,0.,1.1]])
    result=dict(created_utc=utc(),checkpoint_sha256=sha,model_metadata=model.metadata,refinements=[],status='in_progress',
        scope='Independent FD sources and target-centered Newton/Biot-Savart quadrature. Finite refinement is diagnostic, not proof.')
    for nmu,nrad in [(8,6),(12,8)]:
        def save_partial(partial):
            result['current_partial']=dict(nmu=nmu,nrad=nrad,partial_integrals=partial)
            atomic_json(output,result)
        with Interval('whole-space-checkpoint-'+sha[:16],dict(nmu=nmu,nrad=nrad,max_radius=a.max_radius),sha):
            row=joint_integral(model,targets,nmu,nrad,a.max_radius,save_partial)
        result['refinements'].append(row);result.pop('current_partial',None);atomic_json(output,result)
        print(nmu,row['pressure_gradient_difference'],row['velocity_difference'],flush=True)
    coarse,fine=result['refinements']
    result['refinement_pressure_gradient_difference']=stats(np.array(fine['pressure_gradient'])-coarse['pressure_gradient'])
    result['refinement_velocity_difference']=stats(np.array(fine['velocity'])-coarse['velocity'])
    result['status']='completed';result['completed_utc']=utc();atomic_json(output,result)
    print(output,flush=True)
if __name__=='__main__':main()
