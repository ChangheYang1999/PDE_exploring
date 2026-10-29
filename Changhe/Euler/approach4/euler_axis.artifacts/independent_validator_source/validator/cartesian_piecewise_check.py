#!/usr/bin/env python3
"""Cartesian finite differences of value-only potential and swirl fields.

Fourth-order central stencils differentiate scalar values. The primary Taylor
adapter is used only as a comparison after all finite differences are formed.
Every stencil stays inside one smooth element. No cylindrical division occurs
on the rotation axis. Stencil arithmetic uses numpy.longdouble; final Euler
residuals and reported norms use float64.
"""
from pathlib import Path
from datetime import datetime, timezone
import argparse, json, time
import numpy as np
from piecewise_projection import PiecewiseValues
from piecewise_loading import load_piecewise
from piecewise_pressure import InterfaceGreenPoisson
from independent_artifacts import atomic_json, sha256, verify_source_identity
ROOT = Path(__file__).resolve().parent


def cartesian_difference(values, xyz, h):
    """Return U and DU from a callable returning scalar phi,q values."""
    xyz = np.asarray(xyz, dtype=np.longdouble)
    h = np.broadcast_to(np.asarray(h,dtype=np.longdouble),xyz.shape[:-1])
    f, q = values(xyz)
    f, q = np.asarray(f,dtype=np.longdouble), np.asarray(q,dtype=np.longdouble)
    grad = np.empty(xyz.shape,dtype=np.longdouble)
    qgrad = np.empty_like(grad)
    hess = np.empty(xyz.shape+(3,),dtype=np.longdouble)
    offsets = [-2,-1,1,2]
    weights = np.array([1,-8,8,-1],dtype=np.longdouble)/12
    for i in range(3):
        fs, qs = [], []
        for off in offsets:
            shift = np.zeros_like(xyz); shift[...,i] = h*off
            a,b = values(xyz+shift); fs.append(a); qs.append(b)
        fs, qs = np.asarray(fs),np.asarray(qs)
        grad[...,i] = np.einsum('k,k...->...',weights,fs)/h
        qgrad[...,i] = np.einsum('k,k...->...',weights,qs)/h
        hess[...,i,i] = (-fs[0]+16*fs[1]-30*f+16*fs[2]-fs[3])/(12*h*h)
    for i in range(3):
        for j in range(i):
            mixed = np.zeros_like(f)
            for oi, wi in zip(offsets,weights):
                for oj, wj in zip(offsets,weights):
                    shift=np.zeros_like(xyz);shift[...,i]=oi*h;shift[...,j]=oj*h
                    a,_=values(xyz+shift); mixed += wi*wj*a
            hess[...,i,j] = hess[...,j,i] = mixed/(h*h)
    x,y,z = np.moveaxis(xyz,-1,0)
    U = np.stack([-x*grad[...,2]-y*q, -y*grad[...,2]+x*q,
                  2*f+x*grad[...,0]+y*grad[...,1]],axis=-1)
    J = np.empty(xyz.shape+(3,),dtype=np.longdouble)
    for j in range(3):
        J[...,0,j] = -(j==0)*grad[...,2]-x*hess[...,2,j]-(j==1)*q-y*qgrad[...,j]
        J[...,1,j] = -(j==1)*grad[...,2]-y*hess[...,2,j]+(j==0)*q+x*qgrad[...,j]
        J[...,2,j] = 2*grad[...,j]+(j==0)*grad[...,0]+x*hess[...,0,j]+(j==1)*grad[...,1]+y*hess[...,1,j]
    return np.asarray(U,dtype=np.float64),np.asarray(J,dtype=np.float64)


def self_test():
    import sympy as sp
    x,y,z=sp.symbols('x y z');s=x*x+y*y
    phi=sp.Rational(1,5)+3*s/10+2*z/5+3*z*z/20-s*z/10+s*s/50+3*z**3/100
    q=sp.Rational(3,5)-z/5+7*s/100+11*z*z/100
    U=sp.Matrix([-x*sp.diff(phi,z)-y*q,-y*sp.diff(phi,z)+x*q,
                 2*phi+x*sp.diff(phi,x)+y*sp.diff(phi,y)])
    J=U.jacobian([x,y,z])
    f=sp.lambdify((x,y,z),(phi,q),'numpy')
    xyz=np.array([[0,0,0],[0,0,.7],[.3,-.2,-.9],[-.7,.5,.1],[1.3,.4,-.8]])
    values=lambda t:f(*np.moveaxis(t,-1,0))
    reference_U=np.array([np.array(U.subs({x:a,y:b,z:c}),dtype=float).ravel() for a,b,c in xyz])
    reference_J=np.array([np.array(J.subs({x:a,y:b,z:c}),dtype=float) for a,b,c in xyz])
    rows=[]
    for h in [.02,.01,.005]:
        got_U,got_J=cartesian_difference(values,xyz,h)
        rows.append(dict(h=h,U_error=float(np.max(abs(got_U-reference_U))),
                         DU_error=float(np.max(abs(got_J-reference_J)))))
    passed=all(max(r['U_error'],r['DU_error'])<1e-10 for r in rows)
    result=dict(recorded_utc=datetime.now(timezone.utc).isoformat(),all_passed=passed,rows=rows,
                source_sha256=sha256(__file__),method='Exact manufactured polynomial, independently symbolically differentiated.')
    atomic_json(ROOT/'results/cartesian_difference_self_test.json',result)
    print(json.dumps(result),flush=True)
    return 0 if passed else 1


def main():
    ap=argparse.ArgumentParser();ap.add_argument('candidate',type=Path,nargs='?')
    ap.add_argument('--geometry',type=Path);ap.add_argument('--output',type=Path)
    ap.add_argument('--self-test',action='store_true')
    a=ap.parse_args()
    if a.self_test:return self_test()
    if not (a.candidate and a.geometry and a.output):ap.error('candidate, --geometry and --output are required')
    out=a.output.resolve()
    if not out.is_relative_to(ROOT.parent):raise ValueError('output outside lane')
    if out.exists():raise FileExistsError('preserve previous result')
    out.parent.mkdir(parents=True,exist_ok=True)
    start=time.perf_counter();cpu=time.process_time()
    files=[Path(__file__),ROOT/'src/piecewise_projection.py',ROOT/'src/piecewise_adapter.py',ROOT/'src/piecewise_jacobi.py',
        ROOT/'src/piecewise_loading.py',ROOT/'src/piecewise_pressure.py',*sorted((ROOT/'src').glob('independent_*.py'))]
    hashes={str(p.relative_to(ROOT)):sha256(p) for p in files}
    candidate_hash=sha256(a.candidate);geometry_hash=sha256(a.geometry)
    def verify_inputs():
        verify_source_identity(ROOT,hashes)
        if sha256(a.candidate)!=candidate_hash or sha256(a.geometry)!=geometry_hash:
            raise RuntimeError('input changed during Cartesian validation')
    field,gauge=load_piecewise(a.candidate).reporting_gauge()
    geometry=json.loads(a.geometry.read_text());aeff=geometry['core']['a_eff']
    if abs(gauge['dilation_L']-geometry['gauge']['dilation_L'])>1e-13:raise ValueError('inconsistent reporting gauge')
    scalar=PiecewiseValues.load(a.candidate,dilation=field.dilation)
    # Origin, both axes, axis collars, generic azimuths, shell and far exterior.
    base=np.array([[0,0,0],[0,0,.1],[0,0,-.25],[1e-7,0,.3],[-1e-7,0,.3],
        [.21,-.17,.13],[.32,.11,-.22],[0,0,.52],[.73,-.24,.31],
        [0,0,-1.2],[2.1,.4,-.7],[0,0,4.],[5.,-3.,2.],[64.,21.,-7.]])
    xyz=aeff*base;radius=np.linalg.norm(xyz,axis=1)
    elements=np.searchsorted(field.interfaces,radius,side='left')
    scales=np.maximum(radius,aeff*.25)
    # The largest mixed stencil moves by at most 2 sqrt(2) h.
    margins=np.min(abs(radius[:,None]-field.interfaces[None,:]),axis=1)
    scales=np.minimum(scales,margins/.1)
    if np.any(scales<=0):raise ValueError('stencil point lies on an interface')
    def values(points):
        radii=np.sqrt(np.sum(points*points,axis=1))
        for element in range(3):
            mask=elements==element
            if not np.any(mask):continue
            lower=0 if element==0 else field.interfaces[element-1]
            upper=np.inf if element==2 else field.interfaces[element]
            if np.any(radii[mask]<lower) or np.any(radii[mask]>upper):
                raise ValueError('Cartesian difference stencil crosses an interface')
        phi=np.empty(len(points),dtype=np.longdouble);q=np.empty_like(phi)
        for element in range(3):
            mask=elements==element
            if not np.any(mask):continue
            s=points[mask,0]**2+points[mask,1]**2;z=points[mask,2]
            phi[mask]=scalar.evaluate('phi',s,z,element=element)
            q[mask]=scalar.evaluate('q',s,z,element=element)
        return phi,q
    reference_U,reference_J=field.cartesian(xyz,True)
    pressure=InterfaceGreenPoisson(field.source,interfaces=field.interfaces,decay_power=2*field.alpha,
        scale=field.phi.length,lmax=32,nangle=64,nradial=48)
    r=np.hypot(xyz[:,0],xyz[:,1]);P,g=pressure.evaluate(r,xyz[:,2])
    gradP=np.zeros_like(xyz);gradP[:,2]=g[:,1]
    np.divide(xyz[:,0]*g[:,0],r,out=gradP[:,0],where=r!=0)
    np.divide(xyz[:,1]*g[:,0],r,out=gradP[:,1],where=r!=0)
    def residual(U,J):return (1-field.c_l)*U+np.einsum('nij,nj->ni',J,field.c_l*xyz+U)+gradP
    reference_M=residual(reference_U,reference_J)
    result=dict(created_utc=datetime.now(timezone.utc).isoformat(),candidate_sha256=candidate_hash,geometry_sha256=geometry_hash,
        source_sha256=hashes,c_l=field.c_l,gauge=gauge,points_xyz=xyz.tolist(),elements=elements.tolist(),step_scales=scales.tolist(),
        reference_U=reference_U.tolist(),reference_DU=reference_J.tolist(),reference_M=reference_M.tolist(),pressure=P.tolist(),
        scope='Selected-point Cartesian value-stencil comparison. Bulk Green pressure is held fixed to isolate differentiation. No global residual or candidate acceptance claim.',
        arithmetic='longdouble scalar values and differences, then float64 U, DU, Euler residual and norms',steps=[])
    for factor in [.02,.01,.005,.0025,.00125]:
        h=factor*scales
        U,J=cartesian_difference(values,xyz,h);M=residual(U,J)
        row=dict(step_factor=factor,h=h.tolist(),U_max_error=float(np.max(abs(U-reference_U))),
                 DU_max_error=float(np.max(abs(J-reference_J))),M_max_error=float(np.max(abs(M-reference_M))),
                 divergence_max=float(np.max(abs(np.trace(J,axis1=1,axis2=2)))),
                 U_error_by_point=np.max(abs(U-reference_U),axis=1).tolist(),
                 DU_error_by_point=np.max(abs(J-reference_J),axis=(1,2)).tolist(),
                 M_error_by_point=np.max(abs(M-reference_M),axis=1).tolist(),M=M.tolist())
        result['steps'].append(row);result.update(updated_utc=datetime.now(timezone.utc).isoformat(),
            elapsed_seconds=time.perf_counter()-start,cpu_seconds=time.process_time()-cpu)
        verify_inputs();atomic_json(out,result)
        print(json.dumps({k:row[k] for k in ['step_factor','U_max_error','DU_max_error','M_max_error','divergence_max']}),flush=True)
    result['phase']='complete';verify_inputs();atomic_json(out,result)
    return 0
if __name__=='__main__':raise SystemExit(main())
