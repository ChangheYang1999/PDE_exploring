"""Order20-origin stateless residual, full Jacobian and operator interface."""
from absolute_model import (np,AbsoluteLossProblem as ProblemV1,
    AbsoluteJacobianOperator as OperatorV1,FrozenLogMesh,tensor_gauss_mesh,array_hash)
from absolute_fields_v2 import residual as physical_residual,ORIGIN_ORDER


class AbsoluteLossProblem(ProblemV1):
    origin_order=ORIGIN_ORDER

    def fun(self,p=None,extra=None):
        self.fun_calls+=1;prepared=self.prepare(p,extra);result=np.empty(self.mesh.size)
        for start,stop,x,y in self.blocks():
            result[start:stop]=self.root[start:stop]*physical_residual(prepared,x,y)
        if not np.all(np.isfinite(result)):raise ValueError('Nonfinite absolute residual')
        return result

    def jacobian(self,p=None,extra=None):
        self.jac_calls+=1;prepared=self.prepare(p,extra);result=np.empty((self.mesh.size,self.physical_columns))
        for start,stop,x,y in self.blocks():
            _,draw=physical_residual(prepared,x,y,derivatives=True)
            if draw.shape!=(stop-start,self.physical_columns):raise ValueError('Every raw physical derivative is required')
            result[start:stop]=self.root[start:stop,None]*draw
        if not np.all(np.isfinite(result)):raise ValueError('Nonfinite absolute Jacobian')
        return result

    def operator(self,core_tangent,p=None,extra=None,extra_scales=None):
        return AbsoluteJacobianOperator(self,core_tangent,p,extra,extra_scales)


class AbsoluteJacobianOperator(OperatorV1):
    def _matvec(self,v):
        v=np.asarray(v,dtype=float).ravel();raw=np.r_[self.tangent@v[:19],self.scales*v[19:]]
        result=np.empty(self.shape[0])
        for start,stop,x,y in self.problem.blocks():
            _,draw=physical_residual(self.prepared,x,y,derivatives=True)
            result[start:stop]=self.problem.root[start:stop]*(draw@raw)
        return result

    def _rmatvec(self,w):
        w=np.asarray(w,dtype=float).ravel();raw=np.zeros(self.problem.physical_columns)
        for start,stop,x,y in self.problem.blocks():
            _,draw=physical_residual(self.prepared,x,y,derivatives=True)
            raw+=draw.T@(self.problem.root[start:stop]*w[start:stop])
        return np.r_[self.tangent.T@raw[:24],self.scales*raw[24:]]
