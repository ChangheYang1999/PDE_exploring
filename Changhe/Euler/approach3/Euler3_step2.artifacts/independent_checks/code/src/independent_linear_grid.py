"""Tensor-grid synthesis of the independently proved stable linear operator."""
import numpy as np
import torch
from independent_linear import _radial_first

def linear_grid_values(grid,radii):
    field=grid.field
    r=torch.as_tensor(np.asarray(radii),device=field.device,dtype=torch.float64).reshape(-1,1)
    if bool(torch.any(r<=0)):raise ValueError('positive tensor-grid radii required')
    with torch.no_grad():
        f,g,gq=_radial_first(field,r*r);ell=field.ls
        coefficients=[f*r**ell,((ell+1)*g+2*r*r*gq)*r**(ell-1),(-2*ell*gq)*r**(ell+1)]
        values=sum(c@v for c,v in zip(coefficients,grid.vectors))
        return values.reshape(len(r),len(grid.directions),3)
