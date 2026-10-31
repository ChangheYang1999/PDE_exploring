"""Expose interior/exterior terms of the independent radial Green integrator."""
import numpy as np
from solid_harmonics import spherical_harmonics,solid_harmonics
from radial_pressure import radius_groups

def split_values(pressure,points):
    if pressure.tail is not None or pressure.zero_moments:
        raise ValueError('This diagnostic requires direct full-space integration without moment constraints or tail subtraction')
    points=np.asarray(points,dtype=float);radii=np.linalg.norm(points,axis=1)
    ell=pressure.labels[:,0];denom=2*ell+1
    weighted=pressure.weights[:,None]*pressure.source_coefficients
    out={name:[np.zeros(len(points),complex),np.zeros((len(points),3),complex)] for name in ['interior','exterior']}
    centers,groups=radius_groups(radii)
    for radius,select in zip(centers,groups):
        if radius==0:
            h,dh,labels=solid_harmonics(points[select],pressure.lmax)
            out['exterior'][0][select]=h[:,0]*np.sum(weighted[:,0]*pressure.nodes)
            l1=ell==1
            out['exterior'][1][select]=np.einsum('nki,k->ni',dh[:,l1],np.sum(weighted[:,l1],axis=0)/3)
            continue
        directions=points[select]/radii[select,None]
        y,gs,_=spherical_harmonics(directions,pressure.lmax)
        inside=pressure.nodes<radius;outside=~inside
        inner=np.sum(weighted[inside]*radius*(pressure.nodes[inside,None]/radius)**(ell[None,:]+2),axis=0)
        outer=np.sum(weighted[outside]*pressure.nodes[outside,None]*(radius/pressure.nodes[outside,None])**ell[None,:],axis=0)
        for name,v,mult in [('interior',inner,-(ell+1)),('exterior',outer,ell)]:
            pc=v/denom;dp=mult*v/(radius*denom)
            out[name][0][select]=y@pc
            out[name][1][select]=directions*(y@dp)[:,None]+np.einsum('nki,k->ni',gs,pc/radius)
    return {key:(p.real,g.real) for key,(p,g) in out.items()}
