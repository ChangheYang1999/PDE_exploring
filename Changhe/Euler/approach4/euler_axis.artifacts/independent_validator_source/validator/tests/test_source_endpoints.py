#!/usr/bin/env python3
"""Independent quadratures for the source and endpoint identities.

All fields are manufactured non-solutions. Residual terms are retained.
"""
from pathlib import Path
import datetime, hashlib, json, time
import numpy as np
from scipy.integrate import quad
from scipy.special import roots_legendre, roots_jacobi, roots_genlaguerre, beta
from independent_fields import PotentialField, ScalarExpansion
ROOT = Path(__file__).resolve().parents[1]
ROWS = []
S4 = 8*np.pi**2/3

def check(name, error, tolerance, detail=None):
    row = dict(name=name, error=float(error), tolerance=float(tolerance),
               passed=bool(np.isfinite(error) and error <= tolerance))
    if detail is not None: row['detail'] = detail
    ROWS.append(row)
    print(json.dumps(row), flush=True)

def radial_grid(R, n):
    edges = [0., *[2.**j for j in range(-3, int(np.ceil(np.log2(R)))) if 2.**j < R], R]
    x,w=roots_legendre(n)
    return (np.concatenate([a+(b-a)*(x+1)/2 for a,b in zip(edges[:-1],edges[1:])]),
            np.concatenate([(b-a)*w/2 for a,b in zip(edges[:-1],edges[1:])]))

def source_integrals(field, n):
    R,wr=radial_grid(12.,n);mu,wm=roots_legendre(n)
    R=R[:,None];mu=mu[None,:]
    r=R*np.sqrt(1-mu*mu);z=R*mu
    d=field.cylindrical(r,z);res=field.reduced(r,z)
    weight=2*np.pi**2*wr[:,None]*wm[None,:]*(1-mu*mu)*R**4
    chi=z*R**-5;chi_r=-5*z*r*R**-7;kernel=R**-5-5*z*z*R**-7
    q=d['q'][0,0];q0=float(field.q.evaluate(0.,0.))
    qz=d['q'][0,1];eta=d['eta'];U=d['U']
    integrate=lambda x:float(np.sum(weight*x))
    pv=integrate((q*q-q0*q0*np.exp(-R*R))*kernel)
    source=integrate(chi*2*q*qz)
    transport=integrate(eta*((1-2*d['ur_over_r'])*chi-U[...,0]*chi_r-U[...,2]*kernel))
    residual=integrate(chi*res['eta'])
    moment=integrate(eta*chi)
    return dict(pv=pv,source=source,contact=S4*q0*q0/5,transport=transport,
                residual=residual,moment=moment)

def eta_endpoint(field, Rmax, n):
    R,wr=radial_grid(Rmax,n);mu,wm=roots_legendre(n)
    R=R[:,None];mu=mu[None,:];r=R*np.sqrt(1-mu*mu);z=R*mu
    d=field.cylindrical(r,z);res=field.reduced(r,z)
    measure=2*np.pi**2*wr[:,None]*wm[None,:]*(1-mu*mu)*R**4
    integrand=d['ur_over_r']*d['eta']**2+d['eta']*2*d['q'][0,0]*d['q'][0,1]+d['eta']*res['eta']
    volume=float(np.sum(measure*integrand))
    r=Rmax*np.sqrt(1-mu*mu);z=Rmax*mu;d=field.cylindrical(r,z)
    radial_u=d['U'][...,0]*np.sqrt(1-mu*mu)+d['U'][...,2]*mu
    boundary=float(np.sum(2*np.pi**2*wm[None,:]*(1-mu*mu)*Rmax**4*d['eta']**2*(field.c_l*Rmax+radial_u)))
    return volume,boundary

def main():
    started=time.time();exception=None
    try:
        f=PotentialField(ScalarExpansion([(.5,0,1,1.),(.1,1,1,1.),(-.05,0,3,1.)],kernel='gaussian'),
                         ScalarExpansion([(.7,0,0,1.),(.21,0,2,1.),(.07,1,0,1.),(.07,0,1,1.)],kernel='gaussian'),.6)
        for z0 in [0.,.3]:
            for z1 in [.8,1.4]:
                q=lambda z:float(f.q.evaluate(0.,z))
                w=lambda z:f.c_l*z+2*float(f.phi.evaluate(0.,z))
                rq=lambda z:float(f.reduced(0.,z)['q'])
                recon=q(z1)*(w(z0)/q(z0)+(1+f.c_l)*quad(lambda z:1/q(z),z0,z1,epsabs=1e-12,epsrel=1e-12)[0])
                defect=q(z1)*quad(lambda z:rq(z)/(q(z)**2),z0,z1,epsabs=1e-12,epsrel=1e-12)[0]
                check(f'axis_reconstruction_base_{z0}_end_{z1}',abs(recon-w(z1)-defect),2e-12)
        r=np.geomspace(1e-5,3.,33);q=f.q.evaluate(r*r,0.);ell=2*r*r*f.q.evaluate(r*r,0.,1,0)/q
        defect=(2+ell)*f.phi.evaluate(r*r,0.,0,1)-(1+f.c_l*ell)
        check('equatorial_algebraic_defect',np.max(np.abs(defect+f.reduced(r,0.)['q']/q)),4e-14)
        radial=PotentialField(ScalarExpansion([(.5,0,1,1.)],kernel='gaussian'),
                              ScalarExpansion([(.7,0,0,1.)],kernel='gaussian'),.6)
        for i,field in enumerate([radial,f]):
            fine=source_integrals(field,64);coarse=source_integrals(field,40)
            check(f'contact_distribution_{i}',abs(fine['source']+fine['pv']+fine['contact']),3e-12,fine)
            check(f'eta_source_balance_{i}',abs(fine['transport']+fine['pv']+fine['contact']-fine['residual']),3e-12)
            check(f'Green_S1_moment_{i}',abs(fine['moment']-S4/2),3e-12)
            check(f'source_quadrature_refinement_{i}',max(abs(fine[k]-coarse[k]) for k in fine),5e-12)
            if i==0:
                check('radial_q_principal_value_zero',abs(fine['pv']),2e-13)
                check('radial_q_contact_nonzero',abs(fine['source']+S4*.7**2/5),2e-13)
        c=2/3;alpha=(1-c)/c
        endpoint=PotentialField(ScalarExpansion([(.5,0,1,(alpha+1)/2)]),ScalarExpansion([(.7,0,0,(alpha+1)/2)]),c)
        mu,wm=roots_legendre(80);E=.5*(alpha*(3-alpha)+4)*mu
        target=float(np.sum(2*np.pi**2*wm*(1-mu*mu)*E*E)/3)
        errors=[]
        for R in [256.,1024.,4096.]:
            volume,boundary=eta_endpoint(endpoint,R,48)
            check(f'eta_endpoint_finite_ball_{R:g}',abs(2*volume-boundary)/(1+abs(boundary)),3e-12)
            errors.append(abs(volume-target))
        check('eta_endpoint_tail_convergence',max(errors[i+1]/errors[i] for i in range(len(errors)-1)),.3,
              dict(errors=errors,limit=target))
        fine=eta_endpoint(endpoint,256.,72)[0];coarse=eta_endpoint(endpoint,256.,48)[0]
        check('eta_endpoint_quadrature_refinement',abs(fine-coarse),2e-11)
        # Generalized Laguerre integrates the singular radial factor exactly.
        # The physical Gaussian field gives U dot y/R^2 = exp(-R^2)*(3 mu^2-1)/2.
        for p in [.25,1.,3.]:
            mu,wm=roots_jacobi(64,p,p)
            angular=float(np.dot(wm,(3*mu*mu-1)/2)/np.sum(wm))
            check(f'weighted_source_angular_{p}',abs(angular+p/(2*p+3)),3e-14)
            errors=[]
            for gap in [.1,.01,.001,.0001]:
                a=gap/2;x,w=roots_genlaguerre(96,a-1)
                value=angular*float(np.dot(w,np.exp(-x/p))/np.sum(w))
                reference=-p/(2*p+3)*(p/(p+1))**a
                check(f'weighted_source_Gaussian_{p}_{gap}',abs(value-reference),3e-13)
                errors.append(abs(value+p/(2*p+3)))
            check(f'weighted_source_limit_{p}',max(errors[i+1]/errors[i] for i in range(len(errors)-1)),.13)
    except Exception as exc:
        import traceback
        traceback.print_exc();exception=repr(exc)
    paths=[Path(__file__),ROOT/'src/independent_fields.py',ROOT.parent/'research/source_endpoint_identities/PROOF.md']
    result=dict(recorded_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),elapsed_seconds=time.time()-started,
                checks=ROWS,exception=exception,all_passed=exception is None and all(x['passed'] for x in ROWS),
                source_sha256={str(p.relative_to(ROOT.parent)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths},
                scope='Manufactured non-solutions. Every transport identity retains its residual source.')
    (ROOT/'results/source_endpoint_tests.json').write_text(json.dumps(result,indent=2,allow_nan=False)+'\n')
    print(json.dumps({k:result[k] for k in ['all_passed','elapsed_seconds','exception']}))
    raise SystemExit(0 if result['all_passed'] else 1)
if __name__=='__main__':main()
