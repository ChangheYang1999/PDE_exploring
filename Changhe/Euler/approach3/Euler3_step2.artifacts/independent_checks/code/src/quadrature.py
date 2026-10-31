"""Independent deterministic sphere and full-space radial quadrature."""
import numpy as np
from numpy.polynomial.legendre import leggauss


def sphere_grid(n_mu=10,n_phi=20,phase=0.0):
    mu,w=leggauss(n_mu)
    phi=2*np.pi*(np.arange(n_phi)+phase)/n_phi
    x=np.sqrt(1-mu[:,None]**2)*np.cos(phi)[None,:]
    y=np.sqrt(1-mu[:,None]**2)*np.sin(phi)[None,:]
    z=np.broadcast_to(mu[:,None],x.shape)
    points=np.stack((x,y,z),axis=-1).reshape(-1,3)
    weights=np.broadcast_to(w[:,None]*(2*np.pi/n_phi),x.shape).reshape(-1)
    return points,weights


def ray_grid(n_r=32,scale=1.0):
    t,w=leggauss(n_r)
    t=(t+1)/2
    w=w/2
    rho=scale*t/(1-t)
    weights=w*scale/(1-t)**2
    return rho,weights


def shell_points(seed=1701,per_shell=16,radii=(0.125,0.35,0.8,1.6,3.2,6.4,12.8)):
    rng=np.random.default_rng(seed)
    points=[]; labels=[]
    for j,r in enumerate(radii):
        n=rng.normal(size=(per_shell,3)); n/=np.linalg.norm(n,axis=1,keepdims=True)
        points.extend(r*n); labels.extend([j]*per_shell)
    # Origin and axis are explicit and are not omitted for coordinate convenience.
    for r in (0.,0.2,1.,4.):
        points.append([0.,0.,r]); labels.append(len(radii))
        if r: points.append([0.,0.,-r]); labels.append(len(radii))
    return np.array(points),np.array(labels),np.array(radii)
