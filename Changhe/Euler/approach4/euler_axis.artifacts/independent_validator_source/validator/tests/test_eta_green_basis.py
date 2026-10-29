#!/usr/bin/env python3
"""Exact polynomial, direct integral and differential tests for the eta inverse."""
from pathlib import Path
from fractions import Fraction
import time
import numpy as np
import mpmath as mp
from eta_green_basis import angular_decomposition,gegenbauer_polynomial,solid_harmonic,radial_derivatives,GreenPotential,EtaGreenField
from independent_fields import ScalarExpansion
from independent_artifacts import atomic_json
ROOT=Path(__file__).resolve().parents[1]

def main():
    start=time.perf_counter();rows=[]
    def check(name,value,tol):
        value=float(np.max(np.abs(value)))
        if not np.isfinite(value) or value>tol:raise AssertionError((name,value,tol))
        rows.append(dict(name=name,error=value,tolerance=tol))
    for ell in range(13):
        lap={}
        for i,j,c in solid_harmonic(ell):
            if i:lap[i-1,j]=lap.get((i-1,j),0)+4*i*(i+1)*c
            if j>1:lap[i,j-2]=lap.get((i,j-2),0)+j*(j-1)*c
        check(f'solid degree {ell}',max([abs(x) for x in lap.values()],default=0),0)
    for i in range(4):
        for j in range(6):
            x=Fraction(2,7);actual=sum(c*sum(v*x**p for p,v in gegenbauer_polynomial(ell).items()) for ell,c in angular_decomposition(i,j))
            check(f'angular {i},{j}',actual-(1-x*x)**i*x**j,0)
    mp.mp.dps=55
    for ell,d,exponent in [(0,0,1.7),(1,5,23/6),(1,5,5.5),(5,5,6.2),(3,9,6.8)]:
        for t in [0.,1e-6,.7,10.,1e4]:
            ts=mp.mpf(str(t));R=mp.sqrt(ts);ee=mp.mpf(str(exponent));A=mp.mpf(ell+d+5)/2
            if t:
                inner=mp.quad(lambda u:u**(ell+d+4)/(1+u*u)**ee,[0,R/2,R])
                outer=mp.quad(lambda u:u**(d+1-ell)/(1+u*u)**ee,[R,max(R*2,mp.mpf(1)),mp.inf])
                ref=(R**(-2*ell-3)*inner+outer)/(2*ell+3)
            else:ref=mp.beta(ee-(d+2-ell)/2,(d+2-ell)/2)/(2*(2*ell+3))
            got=radial_derivatives(np.array(t),ell,d,exponent,3)
            check(f'integral ell{ell} d{d} beta{exponent} t{t}',(got[0]-float(ref))/float(ref),2e-11)
            source=t**((d-ell)//2)*(1+t)**(-exponent)
            check(f'ODE ell{ell} d{d} t{t}',(4*t*got[2]+(4*ell+10)*got[1]+source)/(1+source),2e-12)
    R=np.r_[0.,np.geomspace(1e-6,4096,34)];mu=np.linspace(-1.,1.,11)
    RR,MM=np.meshgrid(R,mu,indexing='ij');s=RR**2*(1-MM**2);z=RR*MM
    for c_l in [.505,.6,2/3,.74]:
        alpha=(1-c_l)/c_l
        source=ScalarExpansion([(1.,2,1,(alpha+7)/2),(-.7,2,3,(alpha+9)/2),(.4,3,1,(alpha+9)/2+1)])
        phi=GreenPotential(source);p=phi.jet(s,z,3);eta=source.jet(s,z,1)
        scale=(1+RR**2)**((alpha+2)/2)
        check(f'elliptic c_l{c_l}',(-8*p[1,0]-4*s*p[2,0]-p[0,2]-eta[0,0])*scale,1e-10)
        check(f'elliptic z c_l{c_l}',(-8*p[1,1]-4*s*p[2,1]-p[0,3]-eta[0,1])*scale*np.sqrt(1+RR**2),1e-9)
        check(f'elliptic s c_l{c_l}',(-12*p[2,0]-4*s*p[3,0]-p[1,2]-eta[1,0])*scale*(1+RR**2),1e-9)
        q=ScalarExpansion([(1.,1,1,(alpha+4)/2)]);field=EtaGreenField(source,q,c_l)
        xyz=np.array([[0.,0.,0.],[.2,-.1,.7],[-1.2,.4,.8],[0.,0.,2.]])
        U,J=field.cartesian(xyz,True);errors=[]
        for h in [1e-3,5e-4,2.5e-4]:
            FD=np.empty_like(J)
            for k in range(3):
                shift=np.zeros(3);shift[k]=h
                FD[...,k]=(field.cartesian(xyz+shift)-field.cartesian(xyz-shift))/(2*h)
            errors.append(float(np.max(abs(FD-J))))
        check(f'Cartesian finite differences {c_l}',errors[-1],2e-8)
        if errors[-1]>errors[0]/10:raise AssertionError(('FD convergence',errors))
        for L in [.4,2.3]:
            actual=field.dilate(L).cartesian(xyz)
            check(f'dilation {c_l} {L}',actual-L*field.cartesian(xyz/L),2e-13)
    atomic_json(ROOT/'results/eta_green_basis_tests.json',dict(all_passed=True,case_count=len(rows),rows=rows,elapsed_seconds=time.perf_counter()-start))
    print('PASS',len(rows),time.perf_counter()-start)
if __name__=='__main__':main()
