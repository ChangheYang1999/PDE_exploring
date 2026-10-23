"""Independent whole-space integral diagnostics, no server or trainer imports."""
from __future__ import annotations
import argparse
import json
import math
from pathlib import Path
import numpy as np
from core import differentiate,curl,stats
from models import Seed
from evaluate import Interval,atomic_json,ROOT


def sphere_quadrature(nmu=20,nphi=40):
    mu,wm=np.polynomial.legendre.leggauss(nmu)
    phi=2*math.pi*np.arange(nphi)/nphi
    m=np.repeat(mu,nphi);p=np.tile(phi,nmu)
    n=np.column_stack([np.sqrt(1-m*m)*np.cos(p),np.sqrt(1-m*m)*np.sin(p),m])
    # Weights already divide surface area by 4*pi.
    weights=np.repeat(wm,nphi)/(2*nphi)
    return n,weights


def integrate(source,targets,nmu=20,nphi=40,nrad=10,max_radius=64.,mode='pressure'):
    """source returns scalar f for pressure, vector Omega for velocity."""
    directions,wa=sphere_quadrature(nmu,nphi)
    nodes,weights=np.polynomial.legendre.leggauss(nrad)
    boundaries=[0.,.25,.5,1.,2.,4.]
    while boundaries[-1]<max_radius:
        boundaries.append(min(max_radius,2*boundaries[-1]))
    boundaries=[b for b in boundaries if b<=max_radius]
    if boundaries[-1]!=max_radius:
        boundaries.append(max_radius)
    total=np.zeros((len(targets),3));partial=[]
    for low,high in zip(boundaries,boundaries[1:]):
        rad=low+(nodes+1)*(high-low)/2
        wr=weights*(high-low)/2
        displacements=(rad[:,None,None]*directions[None,:,:]).reshape(-1,3)
        source_directions=np.tile(directions,(nrad,1))
        full_weights=(wr[:,None]*wa[None,:]).ravel()
        for i,x in enumerate(targets):
            points=displacements+x
            values=source(points)
            if mode=='pressure':
                value=source_directions*values[:,None]
            elif mode=='velocity':
                value=np.cross(source_directions,values)
            else:
                raise ValueError(mode)
            total[i]+=np.sum(value*full_weights[:,None],axis=0)
        partial.append(dict(outer_radius=high,integral=total.copy().tolist()))
    return dict(value=total.tolist(),partial_integrals=partial,nmu=nmu,nphi=nphi,nrad_per_interval=nrad,
                max_radius=max_radius,targets=np.asarray(targets).tolist(),mode=mode,
                scope='finite-radius quadrature, no analytic tail-error enclosure')


def manufactured_tests():
    targets=np.array([[0.,0.,0.],[.3,-.2,.1],[.7,.1,-.4],[0.,0.,1.1],[1.6,-.4,.2]])
    def f(x):
        s=np.sum(x*x,axis=1);return (6-4*s)*np.exp(-s)
    def omega(x):
        a,b,z=x.T
        return np.column_stack([2*a*z,2*b*z,2*(1-a*a-b*b)])*np.exp(-np.sum(x*x,axis=1))[:,None]
    Pexact=-2*targets*np.exp(-np.sum(targets*targets,axis=1))[:,None]
    Uexact=np.column_stack([-targets[:,1],targets[:,0],np.zeros(len(targets))])*np.exp(-np.sum(targets*targets,axis=1))[:,None]
    out=[]
    for nmu,nrad in [(12,8),(20,12),(28,16)]:
        rp=integrate(f,targets,nmu,2*nmu,nrad,16,'pressure')
        ru=integrate(omega,targets,nmu,2*nmu,nrad,16,'velocity')
        p_error=stats(np.array(rp['value'])-Pexact)
        u_error=stats(np.array(ru['value'])-Uexact)
        out.append(dict(pressure=p_error,velocity=u_error,nmu=nmu,nrad=nrad,
                        pressure_integral=rp,velocity_integral=ru))
    return dict(tests=out,passed=(out[-1]['pressure']['sampled_max']<2e-10 and out[-1]['velocity']['sampled_max']<2e-10))


def model_integral(model,nmu=16,nrad=10,max_radius=64.):
    targets=np.array([[0.,0.,0.],[.3,-.2,.1],[.7,.1,-.4],[0.,0.,1.1],[1.6,-.4,.2]])
    def f(x):
        _,J,_=differentiate(model,x,step=.002,order=6,hessian=False)
        return np.einsum('nij,nji->n',J[:,:3],J[:,:3])
    def om(x):
        _,J,_=differentiate(model,x,step=.002,order=6,hessian=False)
        return curl(J[:,:3])
    values,J,H=differentiate(model,targets,step=.001,order=6,hessian=False)
    pressure=integrate(f,targets,nmu,2*nmu,nrad,max_radius,'pressure')
    velocity=integrate(om,targets,nmu,2*nmu,nrad,max_radius,'velocity')
    dp=np.array(pressure['value'])-J[:,3]
    du=np.array(velocity['value'])-values[:,:3]
    return dict(pressure=pressure,velocity=velocity,provided_pressure_gradient=J[:,3].tolist(),
                provided_velocity=values[:,:3].tolist(),pressure_gradient_difference=stats(dp),velocity_difference=stats(du),
                scope='finite outer radius and resolution. Convergence and analytic tail control are separate requirements.')


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--seed-calibration',action='store_true')
    args=parser.parse_args()
    with Interval('whole-space-manufactured-quadrature',dict(method='Gaussian radial/angular quadrature')):
        test=manufactured_tests()
    atomic_json(ROOT/'evidence/whole_space_unit_tests.json',test)
    print('manufactured tests',test['passed'])
    for r in test['tests']:
        print(r['nmu'],r['pressure']['sampled_max'],r['velocity']['sampled_max'])
    if not test['passed']:
        raise SystemExit(1)
    if args.seed_calibration:
        seed=Seed(c_l=.45)
        with Interval('seed-whole-space-c045',dict(c_l=.45)):
            result=dict(model_metadata=seed.metadata,refinements=[model_integral(seed,nmu=n,nrad=k,max_radius=64.) for n,k in [(12,8),(20,12),(28,16)]])
        atomic_json(ROOT/'evidence/seed_whole_space_c045.json',result)
        for r in result['refinements']:
            print('seed quadrature',r['pressure']['nmu'],r['pressure_gradient_difference'],r['velocity_difference'])

if __name__=='__main__':
    main()
