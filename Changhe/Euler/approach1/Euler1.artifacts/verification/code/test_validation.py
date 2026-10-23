"""Adversarial tests for the independent evaluator, run without the trainer."""
from __future__ import annotations
import datetime
import json
import os
from pathlib import Path
import time
import numpy as np
import sympy as sp
from core import differentiate, residuals, cylindrical_residual, curl, stats, uniform_shell, angular_diagnostics, affine_fit
from models import Affine, Seed, Polynomial

ROOT=Path(__file__).resolve().parents[1]

def utc():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()

def analytic_functions(expr, xyz):
    f=sp.lambdify(xyz,expr,'numpy',cse=True)
    dj=[sp.diff(e,x) for e in expr for x in xyz]
    dh=[sp.diff(e,x,y) for e in expr for x in xyz for y in xyz]
    jf=sp.lambdify(xyz,dj,'numpy',cse=True)
    hf=sp.lambdify(xyz,dh,'numpy',cse=True)
    def evaluate(fn,pts,shape):
        arr=fn(*pts.T)
        return np.stack([np.broadcast_to(e,(len(pts),)) for e in arr],axis=1).reshape((len(pts),)+shape)
    return lambda p:evaluate(f,p,(len(expr),)),lambda p:evaluate(jf,p,(len(expr),3)),lambda p:evaluate(hf,p,(len(expr),3,3))


def main():
    tests=[]
    def record(name,error,tolerance,notes=''):
        tests.append(dict(name=name,error=float(error),tolerance=float(tolerance),passed=bool(error<tolerance),notes=notes))
    rng=np.random.default_rng(928731)
    points=rng.uniform(-1.3,1.3,(80,3))
    points[:,0]+=.21
    start=utc(); t0=time.monotonic()
    affine=Affine(C=.23)
    for order in [4,6]:
        f,J,H=differentiate(affine,points,order=order)
        r=residuals(points,f,J,H,affine.c_l,affine.C)
        record(f'affine momentum order {order}',np.max(abs(r['momentum'])),2e-11)
        record(f'affine pressure Poisson order {order}',np.max(abs(r['pressure_poisson'])),2e-8)
        record(f'affine vorticity order {order}',np.max(abs(r['vorticity'])),2e-8)
        record(f'affine divergence order {order}',np.max(abs(r['divergence'])),2e-11)
    # Symbolic polynomial derivatives provide an independent analytic reference.
    x,y,z=sp.symbols('x y z',real=True); xyz=(x,y,z)
    expr=[sp.Rational(2,5)*x+sp.Rational(6,5)*y*z+sp.Rational(13,100)*x*z*z,
          2*x*z-2*x+sp.Rational(3,10)*y+sp.Rational(7,100)*y**3,
          sp.Rational(8,5)*x*y-sp.Rational(7,10)*z+sp.Rational(11,100)*z*z,
          z**3+sp.Rational(1,5)*x*x*z+sp.Rational(7,10)*x*y+sp.Rational(1,10)*y*y*z*z]
    f_exact,j_exact,h_exact=analytic_functions(expr,xyz)
    poly=Polynomial()
    f,J,H=differentiate(poly,points,order=4)
    record('manufactured polynomial forward',np.max(abs(f-f_exact(points))),2e-13)
    record('manufactured polynomial gradient',np.max(abs(J-j_exact(points))),2e-10)
    record('manufactured polynomial Hessian',np.max(abs(H-h_exact(points))),2e-8)
    r=residuals(points,f_exact(points),j_exact(points),h_exact(points),poly.c_l,poly.C)
    U=sp.Matrix(expr[:3]); P=expr[3]; Jsy=U.jacobian(xyz)
    V=sp.Rational(9,20)*sp.Matrix(xyz)+U+sp.Matrix([0,0,sp.Rational(17,100)])
    rm=(1-sp.Rational(9,20))*U+Jsy*V+sp.Matrix([sp.diff(P,v) for v in xyz])
    rmf,rmj,_=analytic_functions(list(rm),xyz)
    record('manufactured symbolic momentum',np.max(abs(r['momentum']-rmf(points))),1e-12)
    record('nonzero-divergence curl correction',np.max(abs(curl(rmj(points))-r['vorticity']-r['divergence'][:,None]*r['Omega'])),3e-12)
    grad_delta=np.column_stack([np.sum(h_exact(points)[:,np.arange(3),np.arange(3),k],axis=1) for k in range(3)])
    expected=r['divergence']+np.sum(r['V']*grad_delta,axis=1)-r['pressure_poisson']
    record('nonzero-divergence pressure correction',np.max(abs(np.trace(rmj(points),axis1=1,axis2=2)-expected)),3e-12)
    # This verifies derivatives on nonpolynomial physical coordinate maps.
    mapped=[sp.tanh(sp.asinh(x/2)+sp.asinh(y/3)/2)*sp.cos(z/5),
            sp.sin(x/3)*sp.tanh(sp.asinh(z)),sp.tanh(x*y/(1+z*z)),
            (1+x*x+y*y+z*z)**sp.Rational(-7,9)]
    mf,mj,mh=analytic_functions(mapped,xyz)
    for order in [4,6]:
        ff,jj,hh=differentiate(mf,points,step=.01,order=order)
        record(f'mapped gradient order {order}',np.max(abs(jj-mj(points))),2e-6 if order==4 else 2e-8)
        record(f'mapped Hessian order {order}',np.max(abs(hh-mh(points))),2e-5 if order==4 else 4e-7)
    seed=Seed()
    # Curl of the potential, computed numerically rather than using its closed U formula.
    def potential(pts):
        s=np.sum(pts*pts,axis=1)
        return -np.cross(pts,pts@seed.M.T)*(1+s)[:,None]**(-1/(2*seed.c_l))/3
    _,pa,_=differentiate(potential,points,step=.001,order=6,hessian=False)
    record('seed analytic forward versus potential curl',np.max(abs(curl(pa)-seed(points)[:,:3])),2e-10)
    sf,sj,sh=differentiate(seed,points,step=.0015,order=6)
    sr=residuals(points,sf,sj,sh,seed.c_l)
    record('seed divergence',np.max(abs(sr['divergence'])),2e-9)
    for field in [affine,seed,poly]:
        f,J,H=differentiate(field,points,step=.0015,order=6)
        rr=residuals(points,f,J,H,field.c_l,field.C)
        cyl,cd=cylindrical_residual(field,points,field.c_l,field.C,step=.0015,order=6)
        record(f'cylindrical momentum {type(field).__name__}',np.max(abs(cyl-rr['momentum'])),3e-9)
        record(f'cylindrical divergence {type(field).__name__}',np.max(abs(cd-rr['divergence'])),3e-9)
    # Time derivative of the unsteady ansatz tests the sign independently.
    tau=.83; dt=2e-5; c=.45
    xx=points*tau**c
    def physical(tau_):
        return tau_**(c-1)*seed(xx/tau_**c)[:,:3]
    ut=(physical(tau-dt)-physical(tau+dt))/(2*dt)
    expected=tau**(c-2)*((1-c)*sf[:,:3]+c*np.einsum('nij,nj->ni',sj[:,:3],points))
    record('physical-time sign check',np.max(abs(ut-expected)),2e-8)
    # Exact affine field is nonaxisymmetric but must fail non-affinity.
    spectrum=angular_diagnostics(affine,radii=(.5,1),zlevels=(0.,.3),ntheta=64)
    record('affine has resolvable n2 content',max(0.,.05-spectrum['n2_fraction']),1e-15)
    fit=affine_fit(points,affine(points)[:,:3])
    record('affine rejection diagnostic',fit['relative_remainder'],2e-14)
    record('even cylindrical harmonics only',max(a['odd_frequency_energy'] for a in spectrum['rings']),1e-24)
    # physical volume sampling has the correct radial law.
    pts=uniform_shell(rng,200000,1,3)
    observed=np.mean(np.sum(pts*pts,axis=1)); target=(3/5)*(3**5-1)/(3**3-1)
    record('shell physical-volume radial second moment',abs(observed/target-1),.005)
    # Spatial rescaling preserves gradient and vorticity, not velocity.
    a=1.7
    def scaled(pts):
        f=seed(pts/a).copy(); f[:,:3]*=a; f[:,3]*=a*a; return f
    _,j1,_=differentiate(scaled,points,step=.001,order=6,hessian=False)
    _,j2,_=differentiate(seed,points/a,step=.001,order=6,hessian=False)
    record('spatial scale leaves vorticity amplitude invariant',np.max(abs(curl(j1[:,:3])-curl(j2[:,:3]))),2e-10)
    elapsed=time.monotonic()-t0; end=utc()
    output=dict(start_utc=start,end_utc=end,elapsed_seconds=elapsed,passed=all(t['passed'] for t in tests),tests=tests,
                active_time_scope='Numerical unit tests plus symbolic reference generation. NOT counted toward campaign active time because setup and symbolic preparation are interleaved.')
    dest=ROOT/'evidence'/'unit_tests.json'
    dest.write_text(json.dumps(output,indent=2)+'\n')
    for t in tests:
        print(('PASS' if t['passed'] else 'FAIL'),t['name'],t['error'],'<',t['tolerance'])
    print('OUTPUT',dest)
    if not output['passed']:
        raise SystemExit(1)

if __name__=='__main__':
    main()
