"""Scaled raw Green sums at registered source-panel edges; no moment constraints."""
import numpy as np
import torch
from solid_harmonics import spherical_harmonics

def edge_coefficients(pressure,radii):
    rr=np.asarray(radii,dtype=float).reshape(-1)
    if not len(rr) or not np.isfinite(rr).all() or np.any(rr<=0) or np.any(np.diff(rr)<=0):
        raise ValueError('strictly increasing finite positive radii required')
    if pressure.zero_moments:raise ValueError('raw moment convention required')
    if rr[-1]>=pressure.tail_start:raise ValueError('all targets must precede the tail interval')
    edges=np.asarray(pressure.metadata['radial_edges'])
    if any(not np.any(np.isclose(r,edges,rtol=8*np.finfo(float).eps,atol=0)) for r in rr):
        raise ValueError('a target is not a source-panel edge')
    ell=pressure.labels[:,0];s=pressure.nodes
    if np.any(s[:,None]==rr[None,:]):raise ValueError('a quadrature node coincides with a target')
    q=pressure.weights[:,None]*pressure.source_coefficients
    inner=np.zeros((len(rr),len(ell)),complex);outer=np.zeros_like(inner)
    previous=0.;value=np.zeros(len(ell),complex)
    for i,r in enumerate(rr):
        select=(s>=previous)&(s<r)
        value=(previous/r)**(ell+1)*value+np.sum(q[select]*r*(s[select,None]/r)**(ell+2),axis=0)
        inner[i]=value;previous=r
    r=rr[-1];select=s>=r
    value=np.sum(q[select]*s[select,None]*(r/s[select,None])**ell,axis=0)
    if pressure.tail is not None:
        tail=pressure.tail;T=pressure.tail_start;alpha=tail['alpha'];kappa=tail['omega/c_l'];m=pressure.labels[:,1]
        e=-ell-2*alpha+1j*m*kappa
        if np.any(e.real>=0):raise ValueError('nonintegrable tail')
        value+=(r/T)**ell*T**(-2*alpha+1j*m*kappa)*(tail['coefficients']+tail['log_coefficients']*(np.log(T)-1/e))/(-e)
    outer[-1]=value
    for i in range(len(rr)-2,-1,-1):
        a,b=rr[i:i+2];select=(s>=a)&(s<b)
        value=(a/b)**ell*value+np.sum(q[select]*s[select,None]*(a/s[select,None])**ell,axis=0)
        outer[i]=value
    pc=(inner+outer)/(2*ell+1)
    dp=(-(ell+1)*inner+ell*outer)/(rr[:,None]*(2*ell+1))
    if not np.isfinite(pc).all() or not np.isfinite(dp).all():raise FloatingPointError('nonfinite Green coefficients')
    return pc,dp

def synthesize_grid(pressure,radii,directions,device='cpu'):
    radii=np.asarray(radii);directions=np.asarray(directions)
    pc,dp=edge_coefficients(pressure,radii)
    yy,gs,labels=spherical_harmonics(directions,pressure.lmax)
    if not np.array_equal(labels,pressure.labels):raise ValueError('angular label mismatch')
    with torch.no_grad():
        pc=torch.as_tensor(pc,device=device);dp=torch.as_tensor(dp,device=device)
        y=torch.as_tensor(yy.T.copy(),device=device);g=torch.as_tensor(gs.transpose(1,0,2).reshape(len(labels),-1).copy(),device=device)
        p=pc@y;radial=dp@y
        rr=torch.as_tensor(radii[:,None],device=device,dtype=torch.float64)
        tangent=((pc/rr)@g).reshape(len(radii),len(directions),3)
        gp=tangent+radial[:,:,None]*torch.as_tensor(directions[None,:,:],device=device)
        imag=max(float(p.imag.abs().max()),float(gp.imag.abs().max()))
        return p.real.cpu().numpy(),gp.real.cpu().numpy(),imag
