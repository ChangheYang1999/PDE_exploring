"""Independent readers of the mathematical density representations.
No code from any other lane is imported. The X3 formula was transcribed from
its coefficient definition, rather than calling its evaluator.
"""
from pathlib import Path
import hashlib
import numpy as np
from scipy.interpolate import BSpline
from numpy.polynomial.chebyshev import chebval


class X3Density:
    def __init__(self, filename):
        self.filename = str(filename)
        self.md5 = hashlib.md5(Path(filename).read_bytes()).hexdigest()
        with np.load(filename) as f:
            self.k = float(f['k'])
            self.cl = float(f['c_l'])
            self.L = float(f['L'])
            self.order = int(f['spline_order'])
            self.mmax = int(f['angular'])
            self.degree = int(f['degree'])
            self.origin_radius = float(f['origin_radius'])
            self.knots = f['spline_knots'].copy()
            self.names = f['names'].copy()
            self.z = f['z'].copy()
        co = np.zeros((self.degree+1, self.mmax+1))
        sing = []
        for (m,j),v in zip(self.names, self.z[1:]):
            if m < 0:
                sing.append((int(j), float(v)))
            else:
                co[j+1,m] = v
        self.spline = BSpline(self.knots, co, self.order)
        self.singular = np.zeros(max((j for j,_ in sing), default=-1)+1)
        for j,v in sing:
            self.singular[j] = v
        self.p3 = 6 + 2/(2*self.cl-1)
        self.centre_fractional = chebval(-1., self.singular)/self.L**self.p3

    def h(self, x, y):
        x,y = np.broadcast_arrays(np.asarray(x,dtype=float), np.asarray(y,dtype=float))
        shape = x.shape
        xx,yy = x.ravel(),y.ravel()
        out = np.empty(xx.size)
        for a in range(0,xx.size,4096):
            b=min(a+4096,xx.size)
            xp,yp=xx[a:b],yy[a:b]
            r=np.hypot(xp,yp)
            u=r/self.L
            logbase=np.log1p(u*u)
            q=-np.expm1(-.5*(1-self.k)*logbase)
            q=np.minimum(q,1.)
            co=self.spline(q)
            s=(u*u)/(1+u*u)
            chi=(u*u)/(u*u+self.origin_radius**2)
            cosine=np.divide(xp*xp-yp*yp,r*r,out=np.ones_like(r),where=r!=0)
            # Damp the m-th coefficient by chi**(m-1) for m>=2.
            power=np.ones_like(r)
            for m in range(2,self.mmax+1):
                power*=chi
                co[:,m]*=power
            # Clenshaw recurrence for sum_m co_m cos(2m theta).
            b1=np.zeros_like(r); b2=np.zeros_like(r)
            for m in range(self.mmax,0,-1):
                cur=co[:,m]+2*cosine*b1-b2
                b2,b1=b1,cur
            h=co[:,0]+cosine*b1-b2 + .5*(self.k-3)*logbase
            ct=np.divide(np.abs(xp),r,out=np.zeros_like(r),where=r!=0)
            st=np.divide(yp,r,out=np.zeros_like(r),where=r!=0)
            h+=s**(.5*self.p3)*chebval(2*q-1,self.singular)*ct**(self.p3-2)*st**2
            out[a:b]=h
        return out.reshape(shape)

    def __call__(self, x, y):
        x,y=np.broadcast_arrays(np.asarray(x,dtype=float),np.asarray(y,dtype=float))
        return x*x*y*np.exp(self.h(x,y))


def potential_manufactured(x,y):
    """rho=-Laplace(y exp(-r^2)); U1=-phi_xy, U2=phi_xx."""
    r2=x*x+y*y
    return (8-4*r2)*y*np.exp(-r2)


def potential_velocity(x,y):
    e=np.exp(-x*x-y*y)
    return np.array([2*x*(1-2*y*y)*e, y*(4*x*x-2)*e])


def cubic_gaussian(x,y):
    return 8*x*x*y*np.exp(-x*x-y*y)


def gradient_fd(f,x,y,relative_step=0.001):
    """Eighth-order centered Cartesian difference. Explicit independent stencil."""
    h=relative_step*max(1.,abs(x),abs(y))
    out=[]
    weights=[4/5,-1/5,4/105,-1/280]
    for axis in (0,1):
        val=0.
        for j,w in enumerate(weights,1):
            dx=j*h if axis==0 else 0.
            dy=j*h if axis==1 else 0.
            val+=w*(float(f(x+dx,y+dy))-float(f(x-dx,y-dy)))
        out.append(val/h)
    return np.array(out)


def growing_manufactured(x,y,k=.6):
    """rho=-Laplace(phi), phi=y(1+r^2)^((k+1)/2); canonical sublinear U known."""
    p=(k+1)/2
    r2=x*x+y*y
    return -4*p*y*(1+r2)**(p-2)*(2+(p+1)*r2)


def growing_velocity(x,y,k=.6):
    p=(k+1)/2;r2=x*x+y*y
    base=2*p*(1+r2)**(p-2)
    return np.array([-base*x*((1+r2)+2*(p-1)*y*y),base*y*((1+r2)+2*(p-1)*x*x)])
