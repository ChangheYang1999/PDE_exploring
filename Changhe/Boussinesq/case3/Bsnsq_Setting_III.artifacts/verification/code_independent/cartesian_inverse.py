"""Independent whole-plane relative Biot-Savart quadrature.

No modal inverse and no fitting-lane imports. The finite square is integrated
with Cartesian Duffy triangles at each kernel singularity. The exterior uses
four square sides and a compactified radial coordinate extending to infinity.
K(z)=(z_y,-z_x)/(2*pi*|z|^2), so curl U=-omega.

The exterior source callable must define its actual continuation to all radii.
No field or multipole is inserted by this module. decay_power is a quadrature
map parameter, not an imposed tail. Uniform power-decaying sources are the
analytical class in research/03_inverse/PROOF.md.
"""
from __future__ import annotations
from dataclasses import dataclass
import numpy as np
from numpy.polynomial.legendre import leggauss


def gauss_interval(order, left=0.0, right=1.0):
    nodes, weights = leggauss(order)
    return left+(right-left)*(nodes+1)/2, weights*(right-left)/2


def radial_panels(length, order, first=0.125, ratio=1.6):
    edges=[0.0]
    step=min(1.0, first/length)
    while edges[-1]+step < 1.0:
        edges.append(edges[-1]+step)
        step*=ratio
    edges.append(1.0)
    g,w=gauss_interval(order)
    e=np.asarray(edges)
    nodes=e[:-1,None]+np.diff(e)[:,None]*g
    weights=np.diff(e)[:,None]*w
    return nodes.ravel(),weights.ravel()


@dataclass(frozen=True)
class InverseSettings:
    radius: float=12.0
    core_radial_order: int=12
    core_angular_order: int=32
    exterior_radial_order: int=48
    exterior_angular_order: int=48
    decay_power: float=1/3


class CartesianInverse:
    def __init__(self, omega, settings=InverseSettings()):
        self.omega=omega
        self.settings=settings
        if settings.radius <= 0 or settings.decay_power <= 0:
            raise ValueError('positive radius and radial compactification power required')
        self._core_origin=None

    def square_velocity(self, point):
        """Integral of K(X-Y) omega(Y) over the fixed square [-R,R]^2."""
        X=np.asarray(point,dtype=float)
        R=self.settings.radius
        if np.max(np.abs(X))>=R:
            raise ValueError('point must be strictly inside the integration square')
        v=np.zeros(2)
        s,ws=gauss_interval(self.settings.core_angular_order)
        for sx in (-1,1):
            for sy in (-1,1):
                lx=R-sx*X[0]
                ly=R-sy*X[1]
                t,wt=radial_panels(max(lx,ly),self.settings.core_radial_order)
                for swap in (False,True):
                    if not swap:
                        ex=np.full_like(s,sx*lx)
                        ey=sy*ly*s
                    else:
                        ex=sx*lx*s
                        ey=np.full_like(s,sy*ly)
                    xx=X[0]+t[:,None]*ex[None,:]
                    yy=X[1]+t[:,None]*ey[None,:]
                    values=np.asarray(self.omega(xx,yy))
                    # The radial t from the area measure cancels 1/t in K.
                    kx=-ey*lx*ly/(2*np.pi*(ex*ex+ey*ey))
                    ky= ex*lx*ly/(2*np.pi*(ex*ex+ey*ey))
                    integ=wt @ values
                    v+=np.array([np.dot(integ,ws*kx),np.dot(integ,ws*ky)])
        return v

    def exterior_relative(self, point):
        """Exact exterior region is all of R2 outside [-R,R]^2, by quadrature."""
        X=np.asarray(point,dtype=float)
        R=self.settings.radius
        delta=self.settings.decay_power
        if np.max(np.abs(X))>=R:
            raise ValueError('point must be inside core square')
        q,wq=gauss_interval(self.settings.exterior_radial_order)
        a,wa=gauss_interval(self.settings.exterior_angular_order,-1,1)
        r=R*q**(-1/delta)
        v=np.zeros(2)
        jx=np.array([X[1],-X[0]])
        x2=np.dot(X,X)
        for side in range(4):
            if side==0:
                e=np.column_stack((np.ones_like(a),a))
            elif side==1:
                e=np.column_stack((-np.ones_like(a),a))
            elif side==2:
                e=np.column_stack((a,np.ones_like(a)))
            else:
                e=np.column_stack((a,-np.ones_like(a)))
            ee=np.sum(e*e,axis=1)
            dot=e@X
            je=np.column_stack((e[:,1],-e[:,0]))
            den=np.sum((e[None,:,:]-X[None,None,:]/r[:,None,None])**2,axis=2)
            correction=(2*dot[None,:]-x2/r[:,None])/ee[None,:]
            # Stable evaluation of r^2 [K(X-r e)-K(-r e)].
            scaled=(jx[None,None,:]-je[None,:,:]*correction[:,:,None])/(2*np.pi*den[:,:,None])
            omega=np.asarray(self.omega(r[:,None]*e[None,:,0],r[:,None]*e[None,:,1]))
            weights=(wq/(delta*q))[:,None]*wa[None,:]
            v+=np.sum(scaled*(weights*omega)[:,:,None],axis=(0,1))
        return v

    def relative(self, points, include_exterior=True):
        points=np.asarray(points,dtype=float)
        one=points.ndim==1
        points=np.atleast_2d(points)
        if self._core_origin is None:
            self._core_origin=self.square_velocity([0,0])
        values=[]
        for point in points:
            if np.all(point==0):
                values.append(np.zeros(2))
                continue
            v=self.square_velocity(point)-self._core_origin
            if include_exterior:
                v+=self.exterior_relative(point)
            values.append(v)
        out=np.asarray(values)
        return out[0] if one else out

    def circular_center_moments(self, radius, order=48, panels=20):
        """Independent truncated v0 and c. Diagnostic only; no exterior closure."""
        # Tensor Cartesian-square quadrature is used elsewhere. This special
        # integral is nonsingular in polar variables and used only for moments.
        phi=2*np.pi*(np.arange(8*order)+0.5)/(8*order)
        er=np.geomspace(1e-6,max(radius,1e-5),panels)
        edges=np.r_[0,er]
        gn,gw=gauss_interval(order)
        r=(edges[:-1,None]+np.diff(edges)[:,None]*gn).ravel()
        wr=(np.diff(edges)[:,None]*gw).ravel()
        cp,sp=np.cos(phi),np.sin(phi)
        om=self.omega(r[:,None]*cp,r[:,None]*sp)
        v0=np.dot(wr,np.mean(om*cp,axis=1))
        c=2*np.dot(wr/r,np.mean(om*cp*sp,axis=1))
        return {'v0_circle':float(v0),'c_circle':float(c),'radius':float(radius)}
