"""Full-plane singular integral in centered log-polar coordinates.
Gauss-Legendre radial panels, periodic trapezoidal angular rule, Cartesian
finite differences outside the inverse. No modal Green solve or orbit code.
"""
import argparse
import json
import time
from pathlib import Path
import numpy as np
from numpy.polynomial.legendre import leggauss
from density import X3Density, potential_manufactured, potential_velocity, cubic_gaussian, gradient_fd
from collocation import NodalDensity


def velocity(rho, point, nang=512, order=12, panel=0.3, rmin=1e-7, rmax=1e12, offset=0.37):
    x,y=map(float,point)
    ang=(np.arange(nang)+offset)*2*np.pi/nang
    ct,st=np.cos(ang),np.sin(ang)
    kk=np.stack((-np.sin(2*ang),np.cos(2*ang)))/nang
    q,w=leggauss(order)
    edges=np.unique(np.r_[np.linspace(np.log(rmin),np.log(rmax),int(np.ceil(np.log(rmax/rmin)/panel))+1),0.])
    value=np.array([0.,-.5*float(rho(x,y))])
    pieces=[]
    # Only [0,pi) needed: pair is pi-periodic, but full grid permits parity tests.
    for left,right in zip(edges[:-1],edges[1:]):
        t=(left+right)/2+(right-left)*q/2
        radius=np.exp(t)
        dx=radius[:,None]*ct
        dy=radius[:,None]*st
        d=.5*(rho(x+dx,y+dy)+rho(x-dx,y-dy))
        d-=np.where(radius[:,None]<1.,float(rho(x,y)),0.)
        angular=d@kk.T
        contribution=(right-left)/2*(w@angular)
        value+=contribution
        pieces.append((left,right,*contribution))
    return value,np.asarray(pieces)


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--density',default='manufactured')
    p.add_argument('--points',default='0.3,0.7;1.2,0.4;0,0;2,1')
    p.add_argument('--nang',type=int,default=512)
    p.add_argument('--order',type=int,default=12)
    p.add_argument('--panel',type=float,default=.3)
    p.add_argument('--rmin',type=float,default=1e-7)
    p.add_argument('--rmax',type=float,default=1e12)
    p.add_argument('--offset',type=float,default=.37)
    p.add_argument('--output',required=True)
    a=p.parse_args()
    if a.density=='manufactured':rho=potential_manufactured
    elif a.density=='cubic':rho=cubic_gaussian
    else:
        with np.load(a.density) as f:is_nodal='b' in f
        rho=NodalDensity(a.density) if is_nodal else X3Density(a.density)
    points=[tuple(map(float,s.split(','))) for s in a.points.split(';')]
    result={'configuration':vars(a),'rows':[], 'method':'centered real-space full-plane kernel, Legendre panels, angular trapezoid'}
    if isinstance(rho,(X3Density,NodalDensity)):
        result.update(md5=rho.md5,cl=rho.cl,L=rho.L,p3=rho.p3,centre_fractional=rho.centre_fractional)
    for i,point in enumerate(points):
        start=time.monotonic()
        u,pieces=velocity(rho,point,a.nang,a.order,a.panel,a.rmin,a.rmax,a.offset)
        x,y=point
        row={'point':point,'U':u.tolist(),'elapsed_seconds':time.monotonic()-start}
        if a.density=='manufactured':
            exact=potential_velocity(x,y)
            row.update(exact=exact.tolist(),error=(u-exact).tolist())
        if isinstance(rho,(X3Density,NodalDensity)):
            g=gradient_fd(rho,x,y)
            W=rho.cl*np.array(point)+u
            rv=float(rho(x,y)); R=float(W@g-rv)
            nf=abs(rv)+abs(np.array(point)@g)+abs(u@g)
            nv=abs(rv)+np.sum(np.abs(W*g))
            row.update(rho=rv,gradient=g.tolist(),R=R,R_Nf=abs(R)/nf if nf else None,R_Nv=abs(R)/nv if nv else None)
        # Actual last-shell contribution, not asserted as a rigorous tail bound.
        row['tail_shell_sums']={str(r):pieces[pieces[:,0]>=np.log(r),2:].sum(0).tolist() for r in [1e3,1e5,1e7,1e9] if r<a.rmax}
        result['rows'].append(row)
        print(json.dumps(row),flush=True)
        Path(a.output).write_text(json.dumps(result,indent=2)+'\n')
        np.savez_compressed(Path(a.output).with_suffix('.pieces'+str(i)+'.npz'),panels=pieces)

if __name__=='__main__':main()
