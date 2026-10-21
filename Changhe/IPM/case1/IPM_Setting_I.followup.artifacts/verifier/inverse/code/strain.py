"""Origin moment by angular integration and composite Gaussian integration in log r."""
import argparse,json,time
from pathlib import Path
import numpy as np
from numpy.polynomial.legendre import leggauss
from numpy.polynomial.chebyshev import chebval
from density import X3Density,cubic_gaussian
from collocation import NodalDensity


def strain(rho,nang=1024,order=16,panel=.25,rmin=1e-7,rmax=1e14):
    # Even x / odd y reduce the angular moment to a quadrant.
    theta=(np.arange(nang)+.5)*np.pi/(2*nang)
    weights=2*np.sin(3*theta)/nang
    z,w=leggauss(order)
    edges=np.linspace(np.log(rmin),np.log(rmax),int(np.ceil(np.log(rmax/rmin)/panel))+1)
    pieces=[];value=0.
    if isinstance(rho,NodalDensity):
        s=rho.map_inverse(theta)
        angular=np.cos(2*np.arange(rho.M)[:,None]*s[None,:])
    for a,b in zip(edges[:-1],edges[1:]):
        ts=(a+b)/2+(b-a)*z/2;rad=np.exp(ts)
        if isinstance(rho,NodalDensity):
            logbase=np.log1p((rad/rho.L)**2)
            q=-np.expm1(-(1-rho.k)*logbase/2)
            radial_co=chebval(2*q-1,rho.co)
            bvalues=radial_co.T@angular
            radial_density=rad**3*np.exp((rho.k-3)*logbase/2)
            values=radial_density[:,None]*np.cos(theta)**2*np.sin(theta)*bvalues
        else:values=rho(rad[:,None]*np.cos(theta),rad[:,None]*np.sin(theta))
        moment=values@weights
        part=(b-a)/2*np.sum(w*moment/rad)
        value+=part;pieces.append([a,b,part])
    return value,np.array(pieces)


def main():
    p=argparse.ArgumentParser();p.add_argument('density');p.add_argument('output')
    p.add_argument('--nang',type=int,default=1024);p.add_argument('--order',type=int,default=16)
    p.add_argument('--panel',type=float,default=.25);p.add_argument('--rmax',type=float,default=1e14)
    a=p.parse_args()
    if a.density=='cubic':rho=cubic_gaussian
    else:
        with np.load(a.density) as f:nodal='b' in f
        rho=NodalDensity(a.density) if nodal else X3Density(a.density)
    start=time.monotonic();c,pieces=strain(rho,a.nang,a.order,a.panel,rmax=a.rmax)
    out={'configuration':vars(a),'c':c,'seconds':time.monotonic()-start,
         'source_md5':getattr(rho,'md5',None),'identity_defect_3cl_1_c':3*rho.cl-1-c if hasattr(rho,'cl') else None}
    print(json.dumps(out,indent=2));Path(a.output).write_text(json.dumps(out,indent=2)+'\n')
    np.savez_compressed(Path(a.output).with_suffix('.panels.npz'),panels=pieces)

if __name__=='__main__':main()
