"""Coefficient-only normal correction in a versioned complete C5 chart.

cl remains one of the nineteen free tangent directions. Only the three normal
Newton correction directions have zero cl component, avoiding native rounded-
exponent center-strain discontinuities during implicit constraint solves.
"""
import os
if not os.environ.get('IPM_RESOURCE_SESSION'):
    raise RuntimeError('coefficient-normal C5 arithmetic requires the hardware supervisor')

import numpy as np
from continuation_chart import ContinuationChart


VERSION='stage11_coefficient_only_normal_v1'


class CoefficientNormalChart(ContinuationChart):
    def __init__(self,record,base=None,q=None):
        if record.get('coefficient_normal_version')!=VERSION:
            raise ValueError('an explicitly verified coefficient-normal chart record is required')
        free=list(record['free22']);cl_index=free.index(0)
        normal=np.asarray(record['normal_map22x3'],dtype=float)
        tangent=np.asarray(record['free_map22x19'],dtype=float)
        if normal.shape!=(22,3) or not np.array_equal(normal[cl_index],np.zeros(3)):
            raise ValueError('normal corrections must leave native cl exactly unchanged')
        if tangent.shape!=(22,19) or np.linalg.norm(tangent[cl_index])<=0:
            raise ValueError('cl must remain in the full nineteen-dimensional tangent family')
        self.cl_free_index=cl_index
        super().__init__(record,base,q)
        self.version=VERSION

    def _correct(self,dq,normal_seed,physical_seed):
        # Every iteration uses this same native binary64 cl. It is not held
        # fixed across free-coordinate perturbations or optimization steps.
        # Use the same whole-matrix multiplication/grouping as the parent;
        # a separate row dot product could differ by one binary64 ulp.
        expected=float((self.base[self.free22]+self.n@np.asarray(dq))[self.cl_free_index])
        p,z,geometry,history=super()._correct(dq,normal_seed,physical_seed)
        if float(p[0]).hex()!=expected.hex():
            raise ValueError('coefficient-only normal solve unexpectedly changed native cl')
        geometry['native_cl_fixed_through_normal_corrector']=True
        geometry['native_cl_hex']=float(p[0]).hex()
        return p,z,geometry,history


LocalCoefficientC5Chart=CoefficientNormalChart
