"""True residual-Jacobian products from cached physical basis fields.

No new residual Jacobian of shape (rows,new_modes) is constructed. The six
physical field caches remain O(rows*new_modes), as in SpectralProblem. This is
an operator for the Jacobian, not a claim of a cache-free PDE evaluator.
"""
from scipy.sparse.linalg import LinearOperator
from stage12_model import (
    np, e, FIT_KEYS, core_fields, residual_from_fields,
)


def residual_field_weights(p,fields,x,y,root):
    """Six exact first sensitivities of the existing stabilized residual.

    Write a=Wx*fx, b=Wy*fy, c=q*f, D=sqrt(a²+b²+c²+eps²),
    r=root*(a+b+c)/D. Then alpha_i=dr/d(a,b,c)_i. q has the
    core's native center subtraction; a new mode's q derivative is its ratio.
    Explicit c_l transport and regularizer derivatives are handled separately.
    """
    wx,wy=p[0]*x-fields['psiy'],p[0]*y+fields['psix']
    a,b,c=wx*fields['fx'],wy*fields['fy'],fields['q']*fields['f']
    w=(1+x*x+y*y)**((1/p[0]-1)/2)
    den=np.sqrt(a*a+b*b+c*c+(1e-8*w)**2);raw=(a+b+c)/den
    aa=root*(1/den-raw*a/den**2)
    bb=root*(1/den-raw*b/den**2)
    cc=root*(1/den-raw*c/den**2)
    weights={'f':cc*fields['q'],'fx':aa*wx,'fy':bb*wy,
             'psix':bb*fields['fy'],'psiy':-aa*fields['fx'],
             'ratio':cc*fields['f']}
    return weights


def core_jacobian(problem,p,extra,fields):
    """Only the old 24 columns; preserve the frozen dense model's arithmetic.

    The native core c_l FIELD stencil includes rounded exponents and c0;
    analytic new-field c_l derivatives and explicit transport/epsilon chains
    are copied without replacing them by residual finite differences.
    """
    answer=np.empty((len(problem.x),24))
    h=e.v.CL_STEP*max(1,abs(p[0]))
    for lo in range(0,len(problem.x),problem.original.batch):
        hi=min(len(problem.x),lo+problem.original.batch)
        xx,yy=problem.x[lo:hi],problem.y[lo:hi]
        block=e.a.Raw24(xx,yy);mats,strain=block.data(p[0])
        d={k:m[:,1:]-m[:,:1]*strain[None,1:]/strain[0] for k,m in mats.items()}
        qm=mats['ratio']-strain[None,:]
        d['q']=qm[:,1:]-qm[:,:1]*strain[None,1:]/strain[0]
        ff={k:v[lo:hi] for k,v in fields.items()}
        answer[lo:hi,1:24]=residual_from_fields(p,ff,xx,yy,problem.root[lo:hi],d)
        probes=[]
        for factor in [2,1,-1,-2]:
            pp=p.copy();pp[0]+=factor*h;probes.append(core_fields(pp,xx,yy))
        d={key:(-probes[0][key]+8*probes[1][key]-8*probes[2][key]+probes[3][key])/(12*h)
           for key in FIT_KEYS+('q',)}
        for key in FIT_KEYS:d[key]+=problem.extra_cl_matrices[key][lo:hi]@extra
        d['q']+=problem.extra_cl_matrices['ratio'][lo:hi]@extra
        wx,wy=p[0]*xx-ff['psiy'],p[0]*yy+ff['psix']
        a,b,c=wx*ff['fx'],wy*ff['fy'],ff['q']*ff['f']
        da=(xx-d['psiy'])*ff['fx']+wx*d['fx']
        db=(yy+d['psix'])*ff['fy']+wy*d['fy']
        dc=d['q']*ff['f']+ff['q']*d['f']
        w=(1+xx*xx+yy*yy)**((1/p[0]-1)/2)
        den=np.sqrt(a*a+b*b+c*c+(1e-8*w)**2);raw=(a+b+c)/den
        dw=w*(-np.log1p(xx*xx+yy*yy)/(2*p[0]**2))
        answer[lo:hi,0]=problem.root[lo:hi]*((da+db+dc)/den-raw*(a*da+b*db+c*dc+1e-16*w*dw)/den**2)
    return answer


class SpectralJacobianOperator(LinearOperator):
    """Jv and J^T w with optional full-rank feasible coordinate changes.

    core_tangent is 24×d (usually d=19); extra_scales is a nonzero diagonal.
    No singular direction is truncated. Caches and sensitivity weights bind
    the exact construction point and remain valid if a problem builds a later
    cache (the old arrays are retained by reference).
    """
    def __init__(self,problem,p,extra,core_tangent=None,extra_scales=None):
        self.problem=problem
        self.p=np.asarray(p,dtype=float).copy();self.extra=np.asarray(extra,dtype=float).copy()
        if len(self.p)!=24 or len(self.extra)!=len(problem.modes):raise ValueError('Wrong physical parameter dimensions')
        self.basis_fields=problem.basis(self.p[0])
        fields=problem.fields(self.p,self.extra)
        self.weights=residual_field_weights(self.p,fields,problem.x,problem.y,problem.root)
        core=core_jacobian(problem,self.p,self.extra,fields)
        self.core_tangent=np.eye(24) if core_tangent is None else np.asarray(core_tangent,dtype=float).copy()
        if self.core_tangent.ndim!=2 or self.core_tangent.shape[0]!=24:raise ValueError('Core tangent must have 24 rows')
        if np.linalg.matrix_rank(self.core_tangent)!=self.core_tangent.shape[1]:raise ValueError('Core coordinate map is not full rank')
        self.core=core@self.core_tangent
        self.extra_scales=np.ones(len(self.extra)) if extra_scales is None else np.asarray(extra_scales,dtype=float).copy()
        if self.extra_scales.shape!=self.extra.shape or not np.all(np.isfinite(self.extra_scales)) or np.any(self.extra_scales==0):
            raise ValueError('Extra coordinate scales must be finite and nonzero')
        self.core_dimension=self.core.shape[1]
        self.owned_bytes=sum(a.nbytes for a in self.weights.values())+self.core.nbytes+self.p.nbytes+self.extra.nbytes+self.core_tangent.nbytes+self.extra_scales.nbytes
        self.shared_basis_value_bytes=sum(a.nbytes for a in self.basis_fields.values())
        self.shared_basis_cl_bytes=sum(a.nbytes for a in problem.extra_cl_matrices.values())
        super().__init__(dtype=np.dtype(float),shape=(len(problem.x),self.core_dimension+len(self.extra)))

    def _matvec(self,value):
        value=np.asarray(value,dtype=float).ravel()
        out=self.core@value[:self.core_dimension]
        extras=self.extra_scales*value[self.core_dimension:]
        for key in FIT_KEYS:out+=self.weights[key]*(self.basis_fields[key]@extras)
        return out

    def _rmatvec(self,value):
        value=np.asarray(value,dtype=float).ravel()
        old=self.core.T@value
        new=np.zeros(len(self.extra))
        for key in FIT_KEYS:new+=self.basis_fields[key].T@(self.weights[key]*value)
        return np.r_[old,self.extra_scales*new]

    def _matmat(self,value):
        value=np.asarray(value)
        if value.shape[1]==0:return np.empty((self.shape[0],0))
        return np.column_stack([self._matvec(col) for col in value.T])

    def _rmatmat(self,value):
        value=np.asarray(value)
        if value.shape[1]==0:return np.empty((self.shape[1],0))
        return np.column_stack([self._rmatvec(col) for col in value.T])
