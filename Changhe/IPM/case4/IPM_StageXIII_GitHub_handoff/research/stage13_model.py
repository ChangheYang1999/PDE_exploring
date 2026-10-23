"""Exact last-c_l field cache for all-column absolute-residual optimization.

The cache stores potential basis fields and their analytic c_l derivatives at
one *exact* floating-point c_l. It never interpolates in c_l, freezes a physical
parameter, changes a mode, or drops weak directions. Small-radius residuals
and their derivatives use the independently validated Decimal Taylor algebra.
"""
import os
import time
if not os.environ.get('IPM_RESOURCE_SESSION'):
    raise RuntimeError('Stage XIII arithmetic requires the resource supervisor')

import numpy as np
from threadpoolctl import threadpool_limits
from absolute_model import AbsoluteLossProblem
from absolute_fields import core_matrices, center_data, prepare_candidate
from spectral_basis import evaluate_modes
from highprecision_origin import residual_series, evaluate_series


KEYS=('f','fx','fy','psix','psiy','ratio')


class CachedAbsoluteProblem(AbsoluteLossProblem):
    """Same physical fun/Jacobian API with an exact one-c_l basis cache.

    ``workers`` controls BLAS threads only. There are no nested Python worker
    processes. The selected setting is recorded by the caller and benchmarked
    on the actual node-by-mode problem before an optimization campaign.
    """
    version='stage13_exact_last_cl_field_cache_v1'

    def __init__(self,candidate,mesh,a_ref,convention='center_chart',block_size=1024,workers=1):
        super().__init__(candidate,mesh,a_ref,convention,block_size)
        self.workers=int(workers)
        if self.workers<1:raise ValueError('A positive BLAS thread count is required')
        self.x,self.y=mesh.coordinates()
        self.small=np.hypot(self.x,self.y)<=.02
        self.direct=np.flatnonzero(~self.small)
        self._cl=None;self._basis=None;self._cl_basis=None;self._qcore=None
        self._evaluation_key=None;self._last_residual=None;self._last_jacobian=None
        self._prepared=None;self._last_fields=None
        self.cache_builds=0;self.cache_build_seconds=0.;self.evaluation_cache_hits=0

    @property
    def estimated_basis_cache_bytes(self):
        return int(8*len(self.direct)*(12*self.physical_columns+24))

    def cache_record(self):
        return {'version':self.version,'workers':self.workers,'cache_builds':self.cache_builds,
            'cache_build_seconds':self.cache_build_seconds,'basis_cache_bytes':self.estimated_basis_cache_bytes,
            'direct_nodes':int(len(self.direct)),'Taylor_nodes':int(np.count_nonzero(self.small)),
            'exact_cl_cache_key':True,'cl_interpolation_used':False,
            'all_raw_columns':self.physical_columns,'feasible_columns':self.physical_columns-5,
            'evaluation_cache_hits':self.evaluation_cache_hits}

    def _ensure_basis(self,cl):
        if self._cl==cl and self._basis is not None:return
        began=time.perf_counter();n=len(self.direct);columns=self.physical_columns
        # Reuse the existing allocation on a changed cl: no temporary second
        # full cache and no unbounded accumulation over accepted candidates.
        if self._basis is None:
            self._basis={key:np.empty((n,columns)) for key in KEYS}
            self._cl_basis={key:np.empty((n,columns)) for key in KEYS}
            self._qcore=np.empty((n,24))
        self._cl=None
        strain=center_data(cl)[0]
        for lo in range(0,n,self.block_size):
            hi=min(lo+self.block_size,n);ii=self.direct[lo:hi]
            xx,yy=self.x[ii],self.y[ii]
            matrices,cl_matrices=core_matrices(cl,xx,yy,True)
            for key in KEYS:
                self._basis[key][lo:hi,:24]=matrices[key]
                self._cl_basis[key][lo:hi,:24]=cl_matrices[key]
            self._qcore[lo:hi]=matrices['ratio']-strain[None,:]
            for first in range(0,len(self.extra),32):
                last=min(first+32,len(self.extra))
                values,cl_values=evaluate_modes(xx,yy,cl,self.case['modes'][first:last],True)
                for key in KEYS:
                    self._basis[key][lo:hi,24+first:24+last]=values[key]
                    self._cl_basis[key][lo:hi,24+first:24+last]=cl_values[key]
        self._cl=cl;self.cache_builds+=1;self.cache_build_seconds+=time.perf_counter()-began

    def _arguments(self,p,extra):
        p=self.p if p is None else np.asarray(p,dtype=float)
        extra=self.extra if extra is None else np.asarray(extra,dtype=float)
        if p.shape!=(24,) or extra.shape!=self.extra.shape:
            raise ValueError('Every original core parameter and extra coefficient is required')
        if not np.all(np.isfinite(p)) or not np.all(np.isfinite(extra)) or p[0]<=1:
            raise ValueError('Finite physical parameters with cl>1 are required')
        key=(p.tobytes(),extra.tobytes())
        return p,extra,key

    def _evaluate(self,p,extra,key,derivatives):
        if key==self._evaluation_key and (not derivatives or self._last_jacobian is not None):
            self.evaluation_cache_hits+=1
            return self._last_residual,self._last_jacobian
        if key!=self._evaluation_key:
            self._evaluation_key=None;self._last_jacobian=None
            self._prepared=prepare_candidate(self.case,self.convention,parameters=p,extra=extra)
            self._ensure_basis(float(p[0]))
            coeff=np.r_[self._prepared['coefficients'],extra]
            ff={key:mat@coeff for key,mat in self._basis.items()}
            ff['q']=self._qcore@coeff[:24]
            if len(extra):ff['q']+=self._basis['ratio'][:,24:]@extra
            xx,yy=self.x[self.direct],self.y[self.direct]
            wx=p[0]*xx-ff['psiy'];wy=p[0]*yy+ff['psix']
            rr=np.empty(self.mesh.size)
            rr[self.direct]=wx*ff['fx']+wy*ff['fy']+ff['q']*ff['f']
            if np.any(self.small):
                series=residual_series(self._prepared,order=12,derivatives=False)
                rr[self.small]=evaluate_series(series['residual'],self.x[self.small],self.y[self.small])
            self._last_residual=self.root*rr
            self._last_fields=ff
            self._evaluation_key=key
        if derivatives and self._last_jacobian is None:
            prepared=self._prepared;coeff=np.r_[prepared['coefficients'],extra]
            ff=self._last_fields;dc0=prepared['c0_derivative']
            xx,yy=self.x[self.direct],self.y[self.direct]
            wx=p[0]*xx-ff['psiy'];wy=p[0]*yy+ff['psix']
            result=np.empty((self.mesh.size,self.physical_columns))
            # Form only one N-by-all-columns derivative field at a time.
            # This keeps memory below the cache plus Jacobian plus one field.
            direct_result=np.zeros((len(self.direct),self.physical_columns))
            multipliers={'fx':wx,'fy':wy,'f':ff['q'],'psiy':-ff['fx'],'psix':ff['fy'],'ratio':ff['f']}
            for name,multiplier in multipliers.items():
                basis=self._basis[name]
                derivative=basis.copy()
                derivative[:,0]=self._cl_basis[name]@coeff+basis[:,0]*dc0[0]
                derivative[:,1:24]+=basis[:,:1]*dc0[None,1:]
                if name=='ratio':derivative[:,0]+=1
                direct_result+=multiplier[:,None]*derivative
            direct_result[:,0]+=xx*ff['fx']+yy*ff['fy']
            result[self.direct]=direct_result
            if np.any(self.small):
                series=residual_series(prepared,order=12,derivatives=True)
                for column,poly in enumerate(series['derivatives']):
                    result[self.small,column]=evaluate_series(poly,self.x[self.small],self.y[self.small])
            result*=self.root[:,None]
            self._last_jacobian=result
        if not np.all(np.isfinite(self._last_residual)) or (derivatives and not np.all(np.isfinite(self._last_jacobian))):
            raise ValueError('Nonfinite absolute residual/Jacobian')
        return self._last_residual,self._last_jacobian

    def fun(self,p=None,extra=None):
        self.fun_calls+=1;p,extra,key=self._arguments(p,extra)
        with threadpool_limits(limits=self.workers,user_api='blas'):
            value,_=self._evaluate(p,extra,key,False)
        return value.copy()

    def jacobian(self,p=None,extra=None):
        self.jac_calls+=1;p,extra,key=self._arguments(p,extra)
        with threadpool_limits(limits=self.workers,user_api='blas'):
            _,value=self._evaluate(p,extra,key,True)
        return value.copy()

    def clear_cache(self):
        """Release memory explicitly between independent epoch benchmarks."""
        self._cl=None;self._basis=None;self._cl_basis=None;self._qcore=None
        self._evaluation_key=None;self._last_residual=None;self._last_jacobian=None
        self._prepared=None;self._last_fields=None
