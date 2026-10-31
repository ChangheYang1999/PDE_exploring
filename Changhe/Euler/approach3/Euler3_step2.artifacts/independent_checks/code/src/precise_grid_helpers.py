"""More accurate arithmetic for the independent fixed-data holdout helpers.

This retains the saved source coefficients, including raw low moments. Source
and quadrature error are not bounded by the more accurate reconstruction.
"""
import numpy as np
from extended_grid import ExtendedGridField,DT,CT
from extended_pressure import ExtendedPressure

def extended_from_radial(pressure):
    if pressure.zero_moments:raise ValueError('raw source moments are required')
    result=object.__new__(ExtendedPressure);result.lmax=pressure.lmax
    result.labels=np.asarray(pressure.labels,dtype=int).copy()
    result.nodes=np.asarray(pressure.nodes,dtype=DT).copy();result.weights=np.asarray(pressure.weights,dtype=DT).copy()
    result.source_coefficients=np.asarray(pressure.source_coefficients,dtype=CT).copy()
    result.edges=np.asarray(pressure.metadata['radial_edges'],dtype=DT).copy();result.tail_start=DT(pressure.tail_start)
    result.tail=None
    if pressure.tail is not None:
        t=pressure.tail
        result.tail={'alpha':DT(t['alpha']),'kappa':DT(t['omega/c_l']),'coefficients':np.asarray(t['coefficients'],dtype=CT).copy(),'log_coefficients':np.asarray(t['log_coefficients'],dtype=CT).copy()}
    return result

def synthesize_precise(pressure,radii,directions):
    return extended_from_radial(pressure).values(np.asarray(radii,dtype=DT),directions)

def linear_grid_precise(grid,radii):
    if not hasattr(grid,'_precise_linear_grid'):
        grid._precise_linear_grid=ExtendedGridField(grid.field,grid.directions)
    eg=grid._precise_linear_grid;r=np.asarray(radii,dtype=DT).reshape(-1,1);q=r*r;ell=eg.ell
    f,g=eg.radial(radii,stable=True)
    coefficients=[f.v*r**ell,((ell+1)*g.v+2*q*g.d)*r**(ell-1),-2*ell*g.d*r**(ell+1)]
    result=sum(c@v for c,v in zip(coefficients,eg.vectors)).reshape(len(r),len(eg.directions),3)
    if not np.isfinite(result).all():raise FloatingPointError('nonfinite stable linear values')
    return result
