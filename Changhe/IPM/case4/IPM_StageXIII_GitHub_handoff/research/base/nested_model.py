"""Explicit coefficient-summation groups for exact numerical level embedding.

The frozen physical basis, native core, loss and analytic derivative formulas
are inherited unchanged. Only field summation uses recorded contiguous groups;
all-zero appended groups are skipped exactly. This controls floating-point BLAS
summation without adding or removing any physical approximation direction.
"""
from stage12_model import SpectralProblem, np, FIT_KEYS, core_fields


class NestedSpectralProblem(SpectralProblem):
    def __init__(self,modes,n=97,workers=1,sum_groups=None):
        super().__init__(modes,n,workers)
        count=len(modes)
        groups=([count] if count else []) if sum_groups is None else list(sum_groups)
        if any(isinstance(value,bool) or not isinstance(value,(int,np.integer)) or value<=0 for value in groups):
            raise ValueError('sum_groups must contain positive integer counts')
        if sum(groups)!=count:raise ValueError('sum_groups must partition every selected coefficient exactly')
        self.sum_groups=tuple(int(value) for value in groups)

    def fields(self,p,extra):
        extra=np.asarray(extra)
        if extra.shape!=(len(self.modes),):raise ValueError('extra coefficient length differs from selected modes')
        # This loop and arithmetic are copied exactly from frozen parent.fields.
        ff={key:np.empty(len(self.x)) for key in FIT_KEYS+('q',)}
        for lo in range(0,len(self.x),self.original.batch):
            hi=min(len(self.x),lo+self.original.batch)
            core=core_fields(p,self.x[lo:hi],self.y[lo:hi])
            for key in ff:ff[key][lo:hi]=core[key]
        if np.any(extra):
            values=self.basis(p[0]);start=0
            for count in self.sum_groups:
                stop=start+count;coefficients=np.ascontiguousarray(extra[start:stop])
                if np.any(coefficients):
                    # Both row stride and number of dot-product terms match the
                    # parent group. Padded zeros never alter its BLAS dimension.
                    for key in FIT_KEYS:
                        ff[key]+=np.ascontiguousarray(values[key][:,start:stop])@coefficients
                    ff['q']+=np.ascontiguousarray(values['ratio'][:,start:stop])@coefficients
                start=stop
        return ff
