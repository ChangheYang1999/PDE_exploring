"""Canonical full-plane inverse of SmoothBasis through density moments.

Proof: research/smooth_density_moment_inverse/PROOF.md. No producer code.
The finite upper moment is polynomial Gaussian quadrature. Lower moments
use two bounded charts, whose quadrature order is an explicit parameter.
"""
from functools import lru_cache
import numpy as np
from numpy.polynomial.chebyshev import chebvander
from scipy.special import roots_jacobi


@lru_cache(maxsize=1024)
def power_rule(order, exponent):
    """Nodes and positive weights for integral_0^1 u^exponent f(u)du."""
    if not exponent > -1 or exponent >= 900:
        raise ValueError('Jacobi exponent outside this float64 implementation range')
    z, weights = roots_jacobi(int(order), 0., float(exponent))
    nodes = (z + 1.) / 2.
    weights = weights / np.sum(weights) / (exponent + 1.)
    if not (np.all(np.isfinite(weights)) and np.all(weights > 0.) and
            np.all(nodes > 0.) and np.all(nodes < 1.)):
        raise ArithmeticError('Invalid weighted quadrature')
    nodes.setflags(write=False); weights.setflags(write=False)
    return nodes, weights


class DensityMomentInverse:
    def __init__(self, basis, lower_order=128, upper_order=None, composite=False):
        self.basis = basis
        self.order = int(lower_order)
        self.upper_order = max(24, (basis.N + 2) // 2) if upper_order is None else int(upper_order)
        self.composite = bool(composite)
        if self.order < 1 or 2*self.upper_order-1 < basis.N or not basis.L > 0:
            raise ValueError('Invalid quadrature or length')

    def metadata(self):
        return dict(method='density moments, whole-plane two-chart quadrature',
                    lower_order=self.order, upper_order=self.upper_order,
                    composite=self.composite,
                    upper_integral='Gauss-Jacobi exact polynomial degree in exact arithmetic',
                    lower_integral='Gaussian approximation; convergence not certified')

    def lower(self, m, k, radius):
        b = self.basis; q = float(radius)/b.L
        if not q > 0 or not np.isfinite(q):
            raise ValueError('Positive finite dimensionless radius required')
        if q <= 1:
            nodes, weights = power_rule(self.order, float(m+1+2*k))
            den = 1.+(q*nodes)**2
            shape = (q*q/den)**k*den**(-b.a)
            w = den**(-b.a)
            return (weights*shape)@chebvander(1.-2.*w,b.N)
        if self.composite:
            panels = int(np.ceil(np.log2(q)))
            tail = np.exp2(-panels)
            result = tail**(m+2)*self.lower(m,k,q*tail*b.L)
            nodes, weights = power_rule(self.order,0.)
            left = np.exp2(-np.arange(1,panels+1,dtype=float))
            u = (left[:,None]*(1.+nodes[None,:])).reshape(-1)
            quadrature = (left[:,None]*weights[None,:]).reshape(-1)
            logden = 2.*np.log(np.hypot(1.,q*u))
            sigma = -np.expm1(-logden); w = np.exp(-b.a*logden)
            shape = quadrature*u**(m+b.p)*sigma**(b.a+k)
            result += np.exp(-2.*b.a*np.log(q))*(shape@chebvander(1.-2.*w,b.N))
            return result
        nodes, weights = power_rule(self.order, float(m+b.p))
        logden = 2.*np.log(np.hypot(1.,q*nodes))
        sigma = -np.expm1(-logden); w = np.exp(-b.a*logden)
        shape = sigma**(b.a+k)
        return np.exp(-2.*b.a*np.log(q))*(weights*shape)@chebvander(1.-2.*w,b.N)

    def upper(self, m, k, radius):
        b = self.basis; q = float(radius)/b.L; h = m//2; d = k-h
        if d not in (0,1) or m % 2 or m < 2:
            raise ValueError('Upper formula is only for its two density contributions')
        if not q > 0 or not np.isfinite(q):
            raise ValueError('Positive finite dimensionless radius required')
        logden = 2.*np.log(np.hypot(1.,q))
        w = np.exp(-b.a*logden); sigma = -np.expm1(-logden)
        beta = (h-1)/b.a
        nodes, weights = power_rule(self.upper_order,float(beta))
        result = weights@chebvander(1.-2.*w*nodes,b.N)
        if d:
            nodes2, weights2 = power_rule(self.upper_order,float(beta+1./b.a))
            result = result-np.exp(-logden)*(weights2@chebvander(1.-2.*w*nodes2,b.N))
        return sigma**(h-1)*w/(2.*b.a)*result

    def modal_rows(self, radius):
        """Rows psi_m/r^2 and psi_m'/r, even m=2,...,2M."""
        b = self.basis; q = float(radius)/b.L
        if not q > 0 or not np.isfinite(q):
            raise ValueError('Positive finite radius required')
        logden = 2.*np.log(np.hypot(1.,q))
        w = np.exp(-b.a*logden); sigma = -np.expm1(-logden)
        radial = w*sigma**np.arange(b.M)[:,None]*chebvander(1.-2.*w,b.N).reshape(-1)[None,:]
        A = np.zeros((b.M,b.size)); B = A.copy(); low=A.copy(); high=A.copy()
        for h in range(1,b.M+1):
            m=2*h
            for k,co in [(h-1,1. if h==1 else .5),(h,-.5)]:
                if k>=b.M:continue
                sl=slice(k*(b.N+1),(k+1)*(b.N+1))
                A[h-1,sl]+=co*self.lower(m,k,radius)
                low[h-1,sl]+=co*radial[k]
            for k,co in [(h,.5),(h+1,-.5)]:
                if k>=b.M:continue
                sl=slice(k*(b.N+1),(k+1)*(b.N+1))
                B[h-1,sl]+=co*self.upper(m,k,radius)
                high[h-1,sl]+=co*radial[k]
        modes=(2*np.arange(1,b.M+1))[:,None]
        return (B-A)/2.,(modes*(A+B)-low-high)/2.

    def stream_velocity_at_radius(self, radius, angles):
        b=self.basis;angles=np.asarray(angles,float).reshape(-1)
        if radius==0:
            zero=np.zeros((len(angles),b.size));return zero.copy(),zero.copy(),zero.copy()
        P,Q=self.modal_rows(radius);modes=2*np.arange(1,b.M+1)
        cosine=np.cos(angles[:,None]*modes);sine=np.sin(angles[:,None]*modes)
        psi=radius*radius*(sine@P)
        ur=-radius*((cosine*modes)@P);ut=radius*(sine@Q)
        ct=np.cos(angles)[:,None];st=np.sin(angles)[:,None]
        return psi,ct*ur-st*ut,st*ur+ct*ut

    def velocity_at_radius(self, radius, angles):
        return self.stream_velocity_at_radius(radius,angles)[1:]

    def velocity_matrix(self,x,y):
        _,ux,uy=self.stream_velocity_at_radius(np.hypot(x,y),[np.arctan2(y,x)])
        if x==0:ux[:]=0.
        if y==0:uy[:]=0.
        return np.stack((ux[0],uy[0]))
