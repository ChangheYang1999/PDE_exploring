"""Separate full-rank C5 coordinates with coefficient-only rightinverse normals.

Version 1 and its recorded failures remain immutable. This version changes
coordinates only: all five physical constraints and all nineteen feasible
directions remain. No base point is corrected and no profile is refitted.
"""
import os
if not os.environ.get('IPM_RESOURCE_SESSION'):
    raise RuntimeError('C5 chart diagnostics require a resource supervisor')

import numpy as np
from absolute_chart import AbsoluteC5Chart as ChartV1,constraint_jacobian,hp_report


class AbsoluteC5ChartV2(ChartV1):
    version='absolute_loss_analytic_center_full19_c5_rightinverse_v2'

    def __init__(self,p,tolerance=1e-10,target=3e-12):
        self.base=np.asarray(p,dtype=float).copy()
        self.tolerance=float(tolerance);self.target=float(target)
        self._verify(self.base)
        g=constraint_jacobian(self.base)
        norms=np.linalg.norm(g[:,1:],axis=1)
        if not np.all(np.isfinite(norms)) or np.any(norms<=0):
            raise ValueError('All five coefficient constraint rows must be nonzero')
        self.constraint_row_scales=1/norms
        b=self.constraint_row_scales[:,None]*g[:,1:]
        u,s,vt=np.linalg.svd(b,full_matrices=True)
        if len(s)!=5 or not np.all(np.isfinite(s)) or np.any(s<=0):
            raise ValueError('All five coefficient constraint singular values must be positive')
        # A numerical-rank failure refuses the chart; no singular pair is
        # removed to manufacture a reduced family or a successful solve.
        rank_floor=max(b.shape)*np.finfo(float).eps*s[0]
        if s[-1]<=rank_floor:
            raise ValueError('Full five-constraint coefficient rank is unresolved')
        self.normal=np.zeros((24,5))
        self.normal[1:]=vt[:5].T@((u.T/s[:,None])*self.constraint_row_scales[None,:])
        # Full five-row matrix: all 19 complementary right vectors form the
        # same feasible tangent family, with unit physical parameter norm.
        full=self.constraint_row_scales[:,None]*g
        _,sf,vf=np.linalg.svd(full,full_matrices=True)
        if len(sf)!=5 or np.any(sf<=max(full.shape)*np.finfo(float).eps*sf[0]):
            raise ValueError('Full five-constraint physical rank is unresolved')
        self.free=vf[5:].T.copy()
        if self.free.shape!=(24,19) or not np.array_equal(self.normal[0],np.zeros(5)):
            raise ValueError('C5 dimensions or coefficient-only correction policy changed')
        self.base_tangent=self.tangent(self.base)
        self.complete=np.column_stack((self.base_tangent,self.normal))
        if np.linalg.matrix_rank(self.complete)!=24 or np.linalg.matrix_rank(self.base_tangent)!=19:
            raise ValueError('A physical parameter or feasible tangent direction was lost')
        if np.linalg.norm(self.base_tangent[0])==0:
            raise ValueError('cl must remain a free tangent direction')
        self.geometry_diagnostics={
            'version':self.version,'constraint_row_scales':self.constraint_row_scales.tolist(),
            'coefficient_row_scaled_singular_values':s.tolist(),
            'coefficient_row_scaled_condition':float(s[0]/s[-1]),
            'all_five_singular_pairs_retained':True,
            'coefficient_rank_floor_diagnostic':float(rank_floor),
            'full_row_scaled_constraint_singular_values':sf.tolist(),
            'raw_G_normal_minus_identity_norm':float(np.linalg.norm(g@self.normal-np.eye(5))),
            'raw_G_normal_condition':float(np.linalg.cond(g@self.normal)),
            'tangent_constraint_error':float(np.linalg.norm(g@self.base_tangent)),
            'relative_tangent_backward_error':float(np.linalg.norm(g@self.base_tangent)/max(np.linalg.norm(g)*np.linalg.norm(self.base_tangent),1e-300)),
            'tangent_rank':int(np.linalg.matrix_rank(self.base_tangent)),
            'complete_24_rank':int(np.linalg.matrix_rank(self.complete)),
            'complete_24_condition':float(np.linalg.cond(self.complete)),
            'cl_tangent_row_norm':float(np.linalg.norm(self.base_tangent[0])),
            'base_HP':hp_report(self.base),'base_point_corrected':False,
            'constraint_tolerance':self.tolerance,'newton_target':self.target,
            'normal_corrections_leave_cl_fixed':True}
