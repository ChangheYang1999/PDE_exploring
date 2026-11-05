"""FLOAT S1 HS multiplier for a pure angular-one density Mellin mode.

The exact Fourier kernel is scale invariant after rhohat(k)=|k|^-3 A(log|k|).
Set |eta|=exp(v), |xi|=exp(v+u), alpha=(argxi+argeta)/2,
delta=(argxi-argeta)/2. The kernel has only alpha Fourier modes -2,0,2.
The reflection traces reduce to two-dimensional (u,delta) quadrature and
finite Fourier moments. This screen is not a numerical certificate.
"""
import argparse,json,math
from datetime import datetime,timezone
from pathlib import Path
import numpy as np


def calculate(nodes=64,angles=1024):
    xx,ww=np.polynomial.legendre.leggauss(nodes)
    edges=[-16,-8,-4,-2,-1,-.5,-.2,-.05,0,.05,.2,.5,1,2,4,8,16]
    u=np.concatenate([(a+b)/2+(b-a)*xx/2 for a,b in zip(edges,edges[1:])])
    weights=np.concatenate([(b-a)*ww/2 for a,b in zip(edges,edges[1:])])
    delta=(np.arange(angles)+.5)*np.pi/angles;r=np.exp(u[:,None])
    z=(r-1)*np.cos(delta)+1j*(r+1)*np.sin(delta)
    a=np.abs(z);beta=np.angle(z);N=np.array([-2,0,2])
    H=(r-1)*np.sin(delta)*np.sin(2*delta)*a**-3
    f=np.stack([-.5*H*np.exp(-1j*beta),H*np.cos(beta),-.5*H*np.exp(1j*beta)],axis=-1)
    full_integrand=np.mean(np.sum(np.abs(f)**2,axis=-1),axis=1)/4
    numeric_full=float(np.dot(weights*np.exp(2*u),full_integrand))
    loga=np.log(a);shifts=(-1.)**(N//2)
    phase_difference=(-1.)**((N[:,None]-N[None,:])//2)-1
    exponentials=np.exp(-1j*delta[:,None]*N)
    exact_full=(10*np.log(2)-6.5)/64
    results=[]
    for sigma in [0,.25,.5,1,2,4,8,16,32]:
        ff=f*np.exp(1j*sigma*loga)[...,None]
        xy=np.real(np.mean(np.sum(ff*np.conj(np.roll(ff,angles//2,axis=1))*shifts,axis=-1),axis=1))/4
        J=np.einsum('udn,dm->unm',ff,exponentials,optimize=True)*(np.pi/angles)
        xy_difference=np.real(np.sum(J*np.conj(np.swapaxes(J,1,2))*phase_difference,axis=(1,2)))/(4*np.pi**2)
        Cxy=float(np.dot(weights*np.exp(2*u),xy))
        CxminusCy=float(np.dot(weights*np.exp(2*u),xy_difference))
        s1=(exact_full-Cxy+CxminusCy)/4
        results.append({'sigma':sigma,'S1_multiplier_float':s1,'full_multiplier':exact_full,
                        'ratio':s1/exact_full,'Cxy':Cxy,'Cx_minus_Cy':CxminusCy})
    return {'status':'FLOAT_MELLIN_MULTIPLIER_ONLY','angular_density_mode':1,
        'u_nodes':len(u),'delta_nodes':angles,'numeric_full_multiplier':numeric_full,
        'analytic_full_multiplier':exact_full,'full_multiplier_discrepancy':numeric_full-exact_full,
        'rows':results,'open_errors':['u and delta quadrature','u tails beyond16','no actual-source Mellin transform enclosure'],
        'finished_utc':datetime.now(timezone.utc).isoformat()}


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,required=True);ap.add_argument('--nodes',type=int,default=64);ap.add_argument('--angles',type=int,default=1024);args=ap.parse_args()
    result=calculate(args.nodes,args.angles);args.output.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2),flush=True)
if __name__=='__main__':main()
