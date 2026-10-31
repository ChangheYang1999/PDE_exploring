"""Orthonormal complex solid harmonics and Cartesian derivatives by recurrence.

Y_lm has integral |Y_lm|^2=1 and the Condon-Shortley phase. No polar-axis
quotients appear. See theory/radial_green/PROOF.md.
"""
import math
import numpy as np

def solid_harmonics(points,lmax):
    x=np.asarray(points,dtype=float);n=len(x)
    if x.shape!=(n,3):raise ValueError('points must have shape (N,3)')
    r2=np.sum(x*x,axis=1);z=x[:,2];w=x[:,0]+1j*x[:,1]
    dz=np.array([0.,0.,1.]);dw=np.array([1.,1j,0.])
    data={(0,0):(np.full(n,1/math.sqrt(4*math.pi),complex),np.zeros((n,3),complex))}
    for m in range(lmax+1):
        if m:
            prev,g=data[m-1,m-1];a=-math.sqrt((2*m+1)/(2*m))
            data[m,m]=(a*w*prev,a*(w[:,None]*g+prev[:,None]*dw))
        if m<lmax:
            prev,g=data[m,m];a=math.sqrt(2*m+3)
            data[m+1,m]=(a*z*prev,a*(z[:,None]*g+prev[:,None]*dz))
        for ell in range(m+2,lmax+1):
            h1,g1=data[ell-1,m];h2,g2=data[ell-2,m]
            a=math.sqrt((4*ell*ell-1)/(ell*ell-m*m))
            b=math.sqrt((2*ell+1)*((ell-1)**2-m*m)/((2*ell-3)*(ell*ell-m*m)))
            data[ell,m]=(a*z*h1-b*r2*h2,a*(z[:,None]*g1+h1[:,None]*dz)-b*(r2[:,None]*g2+2*x*h2[:,None]))
    labels=[];values=[];gradients=[]
    for ell in range(lmax+1):
        for m in range(-ell,ell+1):
            h,g=data[ell,abs(m)]
            if m<0:h=(-1)**m*h.conj();g=(-1)**m*g.conj()
            labels.append((ell,m));values.append(h);gradients.append(g)
    return np.stack(values,axis=1),np.stack(gradients,axis=1),np.array(labels,dtype=int)

def spherical_harmonics(directions,lmax):
    directions=np.asarray(directions,dtype=float)
    if not np.allclose(np.linalg.norm(directions,axis=1),1,rtol=1e-12,atol=1e-12):raise ValueError('unit directions required')
    y,g,labels=solid_harmonics(directions,lmax)
    gs=g-directions[:,None,:]*y[:,:,None]*labels[None,:,0,None]
    return y,gs,labels
