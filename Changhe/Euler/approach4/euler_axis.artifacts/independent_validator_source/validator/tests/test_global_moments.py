#!/usr/bin/env python3
from pathlib import Path
import datetime,hashlib,json,time
import numpy as np
from scipy.special import roots_legendre,roots_jacobi
from independent_fields import manufactured_power
from independent_pressure import GreenPoisson,geometric_edges,shell_nodes
ROOT=Path(__file__).resolve().parents[1];checks=[]
def check(name,error,tolerance,detail=None):
    row={'name':name,'error':float(error),'tolerance':float(tolerance),'passed':bool(np.isfinite(error) and error<=tolerance)}
    if detail is not None:row['detail']=detail
    checks.append(row);print(json.dumps(row),flush=True)

def boundary_moments(field,R,mu,w):
    R=np.asarray(R).reshape(-1);sin=np.sqrt(1-mu*mu)
    r=R[:,None]*sin;z=R[:,None]*mu
    xyz=np.stack((r,np.zeros_like(r),z),axis=-1);U,J=field.cartesian(xyz,True)
    N=np.einsum('...ij,...j->...i',J,U)
    ur=U[...,0]*sin+U[...,2]*mu;nr=N[...,0]*sin+N[...,2]*mu
    n0=.5*(nr@w)
    i1=1.5*(R**3*((nr*mu)@w)-R**2*((U[...,2]*ur)@w))
    return n0,i1

def main():
    start=time.time();exception=None
    try:
        mu,w=roots_legendre(64)
        for c in [.5,2/3,.74]:
            field=manufactured_power(c);p=GreenPoisson(field.source,decay_power=2*field.alpha,lmax=12,nangle=40,nradial=36)
            for R in [.5,2.,16.,512.]:
                s,ws=shell_nodes(geometric_edges(R),36)
                f=field.source(s[:,None]*np.sqrt(1-mu*mu),s[:,None]*mu)
                I0=np.dot(ws*s*s,.5*(f@w));I1=np.dot(ws*s**3,1.5*((f*mu)@w))
                n0,i1=boundary_moments(field,[R],mu,w)
                err=max(abs(I0-R*R*n0[0])/(1+abs(I0)),abs(I1-i1[0])/(1+abs(I1)))
                check(f'global_flux_moments_c{c}_R{R}',err,5e-12,{'integrated':[I0,I1],'boundary':[R*R*n0[0],i1[0]]})
                x,wx=roots_jacobi(96,0,2*field.alpha-1);t=(x+1)/2;wt=wx/2**(2*field.alpha)
                n,_=boundary_moments(field,R/t,mu,w);P0=R*np.dot(wt,n/t**(2*field.alpha+1))
                x,wx=roots_jacobi(96,0,2*field.alpha);t=(x+1)/2;wt=wx/2**(2*field.alpha+1)
                _,i=boundary_moments(field,R/t,mu,w);P1=np.dot(wt,i*t**(2-2*field.alpha))/R**2
                pcoeff,_=p.radial(R)
                check(f'pressure_moment_representation_c{c}_R{R}',max(abs(pcoeff[0]-P0),abs(pcoeff[1]-P1)),7e-12,
                      {'green':pcoeff[:2].tolist(),'moment_integral':[P0,P1]})
    except Exception as exc:
        import traceback;traceback.print_exc();exception=repr(exc)
    paths=[Path(__file__),ROOT/'src/independent_fields.py',ROOT/'src/independent_pressure.py']
    record={'recorded_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'elapsed_seconds':time.time()-start,'checks':checks,
            'exception':exception,'source_sha256':{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths},
            'all_passed':exception is None and all(c['passed'] for c in checks)}
    (ROOT/'results/global_moment_tests.json').write_text(json.dumps(record,indent=2,allow_nan=False)+'\n')
    print(json.dumps({'all_passed':record['all_passed'],'checks':len(checks),'elapsed_seconds':record['elapsed_seconds']}))
    raise SystemExit(0 if record['all_passed'] else 1)
if __name__=='__main__':main()
