"""Value-only reconstruction and a second, projected derivative representation.

This module reads the documented scalar basis directly from metadata. It never
calls the Taylor arithmetic, spatial jets, or differentiated basis matrices of
the primary piecewise adapter. Interpolation derivatives are supplied by the
independent Chebyshev shell representation. Origin checks use the regular
Cartesian tests separately; this representation requires R > 0.
"""
from __future__ import annotations
import json
from pathlib import Path
import numpy as np
from numpy.polynomial.legendre import legvander
from numpy.polynomial.chebyshev import chebvander
from independent_fields import PotentialField
from independent_projection import ShellProjection


def jacobi_value_table(x, degree, beta):
    """P_j^(0,beta)(x) by the three-term recurrence, in extended precision.

    The primary adapter uses a finite binomial sum and Taylor arithmetic.
    This value-only path deliberately uses neither of those mechanisms.
    """
    x = np.asarray(x, dtype=np.longdouble)
    beta = np.longdouble(beta)
    table = np.empty(x.shape + (degree+1,), dtype=np.longdouble)
    table[..., 0] = 1
    if degree:
        table[..., 1] = ((beta+2)*x-beta)/2
    for j in range(2, degree+1):
        n = np.longdouble(j)
        denom = 2*n*(n+beta)*(2*n+beta-2)
        left = (2*n+beta-1)*((2*n+beta)*(2*n+beta-2)*x-beta*beta)
        right = 2*(n-1)*(n+beta-1)*(2*n+beta)
        table[..., j] = (left*table[..., j-1]-right*table[..., j-2])/denom
    return table


class PiecewiseValues:
    def __init__(self, metadata, coefficients, dilation=1.):
        self.metadata = metadata
        self.elements = metadata['elements']
        self.coefficients = coefficients
        self.dilation = float(dilation)
        self.c_l = float(metadata.get('cl', metadata.get('c_l')))
        self.alpha = (1-self.c_l)/self.c_l
        if len(self.elements) != 3 or [e['kind'] for e in self.elements] != ['ball','shell','exterior']:
            raise ValueError('only the documented three-element basis is supported')
        if self.elements[0].get('radial','cheb') not in ['cheb','chebyshev','jacobi']:
            raise ValueError('unsupported documented ball radial basis')
        if not np.isfinite(self.dilation) or self.dilation <= 0:
            raise ValueError('positive finite dilation required')

    @classmethod
    def load(cls, path, dilation=1.):
        with np.load(Path(path), allow_pickle=False) as data:
            meta = json.loads(str(data['meta_json']))
            coefficients = {f'{key}_el{i}': data[f'{key}_el{i}'].copy()
                            for i in range(3) for key in ['phi','q']}
        return cls(meta, coefficients, dilation=dilation)

    def evaluate(self, key, s, z, *, element=None):
        dtype = np.longdouble
        s, z = np.broadcast_arrays(np.asarray(s,dtype=dtype), np.asarray(z,dtype=dtype))
        if np.any(s < 0) or not np.all(np.isfinite(s)) or not np.all(np.isfinite(z)):
            raise ValueError('finite real coordinates and s >= 0 required')
        shape = s.shape
        ss = s.ravel()/dtype(self.dilation)**2
        zz = z.ravel()/dtype(self.dilation)
        R = np.sqrt(ss+zz*zz)
        mu = np.divide(zz, R, out=np.zeros_like(R), where=R!=0)
        if element is None:
            # Preserve the published float64 interface ownership convention.
            # Extended-precision sqrt can put a rounded boundary point on the
            # other trace of an imperfectly matched export. Projection calls
            # specify the element explicitly and never use this classifier.
            ownership_s = np.asarray(s,dtype=np.float64).ravel()/self.dilation**2
            ownership_z = np.asarray(z,dtype=np.float64).ravel()/self.dilation
            ownership_R = np.sqrt(ownership_s+ownership_z*ownership_z)
            ids = np.searchsorted([float(e['Rhi']) for e in self.elements[:-1]],ownership_R,side='left')
        else:
            if element not in range(3): raise ValueError('invalid element')
            ids = np.full(R.shape,element)
        out = np.zeros_like(R)
        for i,e in enumerate(self.elements):
            take = ids == i
            if not np.any(take): continue
            radii, angles = R[take],mu[take]
            labels = e.get('labels_'+key, e['labels'])
            coefficient = np.asarray(self.coefficients[f'{key}_el{i}'],dtype=dtype)
            if len(labels)!=len(coefficient): raise ValueError('coefficient/label mismatch')
            angular = legvander(angles,int(e['nmax']))
            if e['kind']=='ball':
                scale = radii/dtype(e['Rhi'])
                angular *= scale[:,None]**np.arange(int(e['nmax'])+1)
                if e.get('radial','cheb') == 'jacobi':
                    radial_by_n = {int(n):jacobi_value_table(2*scale*scale-1,
                        max(int(k) for nn,k in labels if nn == n),np.longdouble(n)+np.longdouble('.5'))
                        for n in {nn for nn,_ in labels}}
                    radial = None
                else:
                    radial = chebvander(2*scale*scale-1,max(int(k) for _,k in labels))
            elif e['kind']=='shell':
                x = 2*np.log(radii/dtype(e['Rlo']))/np.log(dtype(e['Rhi'])/dtype(e['Rlo']))-1
                radial = chebvander(x,max(int(k) for _,k in labels))
            value = np.zeros_like(radii)
            # Summation of scalar values, independent of adapter matrix assembly.
            for (n,k),c in zip(labels,coefficient):
                if e['kind']=='exterior':
                    factor = (radii/dtype(e['Rlo']))**(-dtype(k))
                elif e['kind']=='ball' and e.get('radial','cheb')=='jacobi':
                    factor = radial_by_n[int(n)][:,int(k)]
                else:
                    factor = radial[:,int(k)]
                value += c*angular[:,int(n)]*factor
            out[take] = value
        if key=='phi': out *= dtype(self.dilation)
        return out.reshape(shape)

    def project(self, lower, upper, *, element, radial_degree=32, angular_degree=24, trim_relative=2e-18):
        e = self.elements[element]
        lo = float(e.get('Rlo',0.))*self.dilation
        hi = np.inf if e.get('Rhi') is None else float(e['Rhi'])*self.dilation
        if lower < lo*(1-2e-13) or upper > hi*(1+2e-13):
            raise ValueError('projection must remain within one smooth element')
        factor = 0. if element==0 else self.alpha
        scalars = []
        for key in ['phi','q']:
            exponent = 0. if element==0 else factor+(key=='q')
            values = lambda s,z,key=key: self.evaluate(key,s,z,element=element)
            scalars.append(ShellProjection(values,lower,upper,radial_degree=radial_degree,
                angular_degree=angular_degree,trim_relative=trim_relative,factor_power=exponent,
                numeric_dtype=np.longdouble))
        return PotentialField(*scalars,self.c_l)
