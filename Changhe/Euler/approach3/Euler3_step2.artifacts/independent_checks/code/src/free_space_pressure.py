"""Pressure and gradient from target-centered full-space Newton integrals.

This is independent of the source-centered harmonic Green solve. The rational
radial quadrature covers (0,infinity); its truncation error is not certified.
"""
import numpy as np
from quadrature import sphere_grid, ray_grid


def newton_pressure(source, points, n_r=96, n_mu=32, n_phi=64, scale=1.,
                    phase=.317, point_batch=1024, progress=None):
    dirs, aw = sphere_grid(n_mu, n_phi, phase=phase)
    radius, rw = ray_grid(n_r, scale)
    offsets = (radius[:, None, None] * dirs[None, :, :]).reshape(-1, 3)
    direction = np.broadcast_to(dirs, (len(radius),) + dirs.shape).reshape(-1, 3)
    weight = (rw[:, None] * aw[None, :]).ravel() / (4*np.pi)
    radial = np.repeat(radius, len(dirs))
    values, gradients = [], []
    for index, point in enumerate(np.asarray(points, dtype=float)):
        value = 0.
        gradient = np.zeros(3)
        for lo in range(0, len(offsets), point_batch):
            hi = min(lo + point_batch, len(offsets))
            density = np.asarray(source(point + offsets[lo:hi]), dtype=float)
            if density.shape != (hi-lo,) or not np.isfinite(density).all():
                raise ValueError('Invalid scalar source values')
            weighted = weight[lo:hi] * density
            value += weighted @ radial[lo:hi]
            gradient += weighted @ direction[lo:hi]
            if progress:
                progress(index, hi, len(offsets))
        values.append(value)
        gradients.append(gradient)
    return np.asarray(values), np.asarray(gradients)
