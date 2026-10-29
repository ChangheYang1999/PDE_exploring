#!/usr/bin/env python3
"""Reproducible independent manufactured tests, with retained numerical errors."""
from pathlib import Path
import datetime
import hashlib
import json
import os
import platform
import time
import numpy as np
import sympy as sp
from independent_fields import ScalarExpansion,PotentialField,manufactured_gaussian,manufactured_power
from independent_pressure import GreenPoisson,DirectNewtonPressure

ROOT=Path(__file__).resolve().parents[1]
RESULTS=[]


def check(name,error,tolerance,detail=None):
    error=float(error)
    entry={"name":name,"error":error,"tolerance":float(tolerance),"passed":bool(np.isfinite(error) and error<=tolerance)}
    if detail is not None:
        entry["detail"]=detail
    RESULTS.append(entry)
    print(json.dumps(entry),flush=True)


def maximum(a):
    return np.max(np.abs(a),initial=0)


def symbolic_expression(expansion,s,z):
    result=0
    for t in expansion.terms:
        kernel=(expansion.length**2+s+z*z)**(-t.beta) if expansion.kernel=="power" else sp.exp(-t.beta*(s+z*z))
        result+=t.coefficient*s**t.i*z**t.j*kernel
    return result


def derivative_tests():
    rng=np.random.default_rng(62817)
    ss=np.r_[0.,0.,1e-18,rng.uniform(0,4,40)]
    zz=np.r_[0.,.7,-.4,rng.uniform(-2,2,40)]
    s,z=sp.symbols('s z',real=True)
    for index,field in enumerate([manufactured_gaussian(),manufactured_gaussian(-.6,-.4,.9),manufactured_power()]):
        for name,scalar in [('phi',field.phi),('q',field.q)]:
            expr=symbolic_expression(scalar,s,z)
            worst=0.
            for ds in range(4):
                for dz in range(4-ds):
                    expected=sp.lambdify((s,z),sp.diff(expr,s,ds,z,dz),modules='numpy')(ss,zz)
                    actual=scalar.evaluate(ss,zz,ds,dz)
                    worst=max(worst,maximum(actual-expected)/(1+maximum(expected)))
            check(f'symbolic_jets_{index}_{name}',worst,2e-12)
        r=np.sqrt(ss)
        d=field.cylindrical(r,zz)
        reduced=field.reduced(r,zz)
        check(f'divergence_{index}',maximum(d['divergence']),2e-14)
        check(f'circulation_equivalence_{index}',maximum(reduced['gamma']-ss*reduced['q']),3e-14)
        check(f'primitive_swirl_equivalence_{index}',maximum(field.primitive_cylindrical(r,zz)[...,1]-r*reduced['q']),2e-14)
        xyz=np.stack((r,np.zeros_like(r),zz),axis=-1)
        U,J=field.cartesian(xyz,True)
        omega_theta=J[:,0,2]-J[:,2,0]
        check(f'vorticity_stream_identity_{index}',maximum(omega_theta-r*d['eta']),5e-14)
        check(f'pressure_source_cartesian_{index}',maximum(np.einsum('...ij,...ji->...',J,J)-d['source']),1e-13)
        check(f'primitive_cartesian_cylindrical_{index}',maximum(field.primitive_cartesian(xyz)-field.primitive_cylindrical(r,zz)),3e-14)
        check(f'cartesian_divergence_{index}',maximum(np.trace(J,axis1=-2,axis2=-1)),2e-14)
        for L in [.17,3.7]:
            scaled=field.dilate(L)
            check(f'dilation_velocity_{index}_{L}',maximum(scaled.cartesian(L*xyz)-L*U),1e-13)
            check(f'dilation_reduced_q_{index}_{L}',maximum(scaled.reduced(L*r,L*zz)['q']-reduced['q']),2e-13)
            check(f'dilation_reduced_eta_{index}_{L}',maximum(L*scaled.reduced(L*r,L*zz)['eta']-reduced['eta']),5e-13)
            check(f'dilation_primitive_{index}_{L}',maximum(scaled.primitive_cartesian(L*xyz)-L*field.primitive_cartesian(xyz)),3e-13)


def finite_difference_tests():
    field=manufactured_gaussian(.31,.62,-.47)
    xyz=np.array([[0,0,0],[0,0,.7],[1e-9,-1e-9,-.3],[.4,-.3,.2],[1.2,.7,-.8]],dtype=np.float64)
    U,J=field.cartesian(xyz,True)
    errors=[]
    for h in [.02,.01,.005,.0025,.00125]:
        Jfd=np.empty_like(J)
        for j in range(3):
            step=np.zeros(3);step[j]=h
            Jfd[...,j]=(-field.cartesian(xyz+2*step)+8*field.cartesian(xyz+step)-8*field.cartesian(xyz-step)+field.cartesian(xyz-2*step))/(12*h)
        errors.append(maximum(J-Jfd))
    check('cartesian_fourth_order_fd',errors[-1],1e-9,{'steps':[.02,.01,.005,.0025,.00125],'errors':errors})
    check('cartesian_fd_convergence',max(errors[k+1]/errors[k] for k in range(3)),.08)
    z=np.linspace(-1,1,11)
    eps=1e-3
    p0=field.phi.evaluate(np.zeros_like(z),z)
    p1=field.phi.evaluate(np.zeros_like(z),z,1,0)
    q0=field.q.evaluate(np.zeros_like(z),z)
    q1=field.q.evaluate(np.zeros_like(z),z,1,0)
    d=field.cylindrical(np.full_like(z,eps),z)
    check('axis_quadratic_axial_velocity',maximum(d['U'][:,2]-(2*p0+4*eps**2*p1)),2e-11)
    check('axis_quadratic_swirl_quotient',maximum(d['U'][:,1]/eps-(q0+eps**2*q1)),2e-12)


def torch_tests():
    import torch
    torch.set_num_threads(1)
    torch.set_num_interop_threads(1)
    torch.set_default_dtype(torch.float64)
    field=manufactured_power(.64)
    points=np.array([[0.,0.,0.],[0.,0.,.8],[.4,-.3,.2],[1.4,.2,-.8]])
    Uref,Jref=field.cartesian(points,True)
    devices=['cpu']+(['cuda:0'] if torch.cuda.is_available() else [])
    for device in devices:
        xyz=torch.tensor(points,device=device,requires_grad=True)
        x,y,z=xyz.unbind(-1)
        s=x*x+y*y
        def scalar(expansion):
            result=torch.zeros_like(s)
            for t in expansion.terms:
                result=result+t.coefficient*s**t.i*z**t.j*(expansion.length**2+s+z*z)**(-t.beta)
            return result
        phi,q=scalar(field.phi),scalar(field.q)
        ps=torch.autograd.grad(phi.sum(),s,create_graph=True,retain_graph=True)[0]
        pz=torch.autograd.grad(phi.sum(),z,create_graph=True,retain_graph=True)[0]
        U=torch.stack((-x*pz-y*q,-y*pz+x*q,2*phi+2*s*ps),dim=-1)
        J=torch.stack([torch.autograd.grad(U[:,i].sum(),xyz,create_graph=True,retain_graph=True)[0] for i in range(3)],dim=1)
        check(f'torch_ad_velocity_{device}',maximum(U.detach().cpu().numpy()-Uref),3e-14)
        check(f'torch_ad_jacobian_{device}',maximum(J.detach().cpu().numpy()-Jref),5e-14)
        check(f'torch_dtype_{device}',0 if U.dtype==torch.float64 and J.dtype==torch.float64 and J.sum().dtype==torch.float64 else 1,0)
        # A spatial JVP obtained by AD, compared to a separate centered finite difference.
        v=np.array([.3,-.7,.2])
        ad=np.einsum('...ij,j->...i',J.detach().cpu().numpy(),v)
        h=1e-5
        fd=(field.cartesian(points+h*v)-field.cartesian(points-h*v))/(2*h)
        check(f'spatial_jvp_{device}',maximum(ad-fd),2e-9)
        if device.startswith('cuda'):
            print(json.dumps({'gpu_name':torch.cuda.get_device_name(0),'visible_devices':os.environ.get('CUDA_VISIBLE_DEVICES')}),flush=True)


def pressure_tests():
    radii=np.array([0.,.03,.3,1.,3.,12.])
    mu=np.array([-.91,-.4,0.,.53,.98])
    for dimension in [3,5]:
        for p in [.72,1.,1.63,2.]:
            known=ScalarExpansion([(1.,0,0,p/2),(.23,0,1,(p+1)/2),(-.11,1,0,(p+2)/2)])
            def source(r,z):
                s=r*r
                return -(2*(dimension-1)*known.evaluate(s,z,1,0)+4*s*known.evaluate(s,z,2,0)+known.evaluate(s,z,0,2))
            inv=GreenPoisson(source,dimension=dimension,decay_power=p,lmax=8,nangle=20,nradial=28)
            got,grad=inv.on_spheres(radii,mu)
            r=radii[:,None]*np.sqrt(1-mu[None,:]**2)
            z=radii[:,None]*mu[None,:]
            expected=known.evaluate(r*r,z)
            expected_grad=np.stack((2*r*known.evaluate(r*r,z,1,0),known.evaluate(r*r,z,0,1)),axis=-1)
            check(f'green_value_d{dimension}_p{p}',maximum(got-expected),3e-10)
            check(f'green_gradient_d{dimension}_p{p}',maximum(grad-expected_grad),3e-10)
    # Independent Newton quadrature of an analytically known pressure.
    known=ScalarExpansion([(1.,0,0,.6),(.2,0,1,1.1)])
    def source(r,z):
        s=r*r
        return -(4*known.evaluate(s,z,1,0)+4*s*known.evaluate(s,z,2,0)+known.evaluate(s,z,0,2))
    points=[(0.,0.),(0.,.7),(.4,.3)]
    for r,z in points:
        expected=known.evaluate(r*r,z)
        errors=[]
        for n in [20,40,80]:
            got=DirectNewtonPressure(source,decay_power=1.2,nradial=n,nangle=n).evaluate(r,z)
            errors.append(abs(got-expected))
        check(f'direct_newton_{r}_{z}',errors[-1],8e-6,{'orders':[20,40,80],'errors':[float(e) for e in errors]})
    field=manufactured_gaussian()
    inv=GreenPoisson(field.eta,dimension=5,decay_power=1.,lmax=8,nangle=20,nradial=28)
    got,_=inv.on_spheres(radii,mu)
    r=radii[:,None]*np.sqrt(1-mu[None,:]**2);z=radii[:,None]*mu[None,:]
    check('delta5_inverse_manufactured',maximum(got-field.phi.evaluate(r*r,z)),2e-11)
    inv=GreenPoisson(field.source,decay_power=2.,lmax=10,nangle=24,nradial=28)
    for r,z in points:
        spectral=inv.evaluate(r,z)[0]
        direct=DirectNewtonPressure(field.source,decay_power=2.,nradial=80,nangle=80).evaluate(r,z)
        check(f'field_pressure_two_routes_{r}_{z}',abs(spectral-direct),2e-5)


def main():
    start=time.time()
    error=None
    try:
        derivative_tests()
        finite_difference_tests()
        torch_tests()
        pressure_tests()
    except Exception as exc:
        import traceback
        traceback.print_exc()
        error=repr(exc)
    output={'recorded_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'elapsed_seconds':time.time()-start,
            'python':platform.python_version(),'affinity':sorted(os.sched_getaffinity(0)),
            'source_sha256':{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in [Path(__file__),ROOT/'src/independent_fields.py',ROOT/'src/independent_pressure.py']},
            'checks':RESULTS,'exception':error,'all_passed':error is None and all(r['passed'] for r in RESULTS)}
    (ROOT/'results/operator_tests.json').write_text(json.dumps(output,indent=2)+'\n')
    print(json.dumps({'all_passed':output['all_passed'],'checks':len(RESULTS),'elapsed_seconds':output['elapsed_seconds']}))
    raise SystemExit(0 if output['all_passed'] else 1)

if __name__=='__main__':
    main()
