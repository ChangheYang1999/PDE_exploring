"""Target-centered five-dimensional Green quadrature for callable sources.

The exact kernels are proved in research/axis_moments/PROOF.md. This module
uses one mapped Jacobi rule on (0,infinity), with no outer cutoff, modal
expansion, radial interpolation or numerics-lane evaluator.
"""
from __future__ import annotations
import numpy as np
from scipy.special import roots_jacobi


def axis_green(source, z0, alpha, *, nradial=64, nangle=96, scale=1.):
    if not (alpha > 0 and scale > 0):
        raise ValueError('positive decay exponent and mapping scale required')
    x, wx = roots_jacobi(nradial, alpha-1., 0.)
    x = (x+1.)/2.
    wx = wx/(2.**alpha)
    rho = scale*x/(1.-x)
    wr = wx*scale/(1.-x)**(alpha+1.)
    mu, wm = roots_jacobi(nangle, 1., 1.)
    r = rho[:, None]*np.sqrt(1.-mu[None, :]**2)
    z = z0+rho[:, None]*mu[None, :]
    eta = np.asarray(source(r, z), dtype=np.float64)
    if eta.shape != r.shape or not np.all(np.isfinite(eta)):
        raise ValueError('source must return finite values at every quadrature point')
    value = .25*np.dot(wr*rho, eta@wm)
    derivative = .75*np.dot(wr, eta@(mu*wm))
    return {'z0': float(z0), 'phi': float(value), 'phi_z': float(derivative),
            'alpha': float(alpha), 'scale': float(scale), 'nradial': nradial,
            'nangle': nangle, 'point_count': int(eta.size), 'dtype': str(eta.dtype),
            'outer_cutoff': None, 'principal_value_used': False}
