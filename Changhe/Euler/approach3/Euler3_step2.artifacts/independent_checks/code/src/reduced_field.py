"""Independent complex 2x2 expansion of the inviscid tail constraints."""
import copy
import numpy as np
import torch
from parameter_field import ParameterField

def expand_coefficients(arrays,modes,c,w):
    alpha=(1-c)/c;kappa=w/c
    out={key:np.array(value,copy=True,dtype=float) for key,value in arrays.items()}
    derivatives={p:{key:np.zeros_like(value) for key,value in out.items()} for p in ['c_l','omega']}
    lookup={tuple(mode):q for q,mode in enumerate(modes)}
    for key,shift in [('A',0),('C',1)]:
        n=len(out[key]);k=np.arange(n,dtype=float);k2=k*k;K=(8/3)*k2*(k2-1)
        assert n>=2
        for qc,(ell,m,kind) in enumerate(modes):
            if kind:continue
            qs=lookup[(ell,m,1)] if m else None
            a=np.asarray(arrays[key][:n-2,qc],complex)
            if m:a=a+1j*arrays[key][:n-2,qs]
            P=(alpha+ell-shift)/2+1j*m*kappa/2
            matrix=np.array([[k2[-2],k2[-1]],[K[-2]-P,K[-1]-P]],complex)
            rhs=np.array([-k2[:-2]@a,-K[:-2]@a+P*a.sum()])
            tail=np.linalg.solve(matrix,rhs)
            out[key][-2:,qc]=tail.real
            if m:out[key][-2:,qs]=tail.imag
            total=a.sum()+tail.sum()
            for p,Pp in [('c_l',-.5/c**2-1j*m*w/(2*c*c)),('omega',1j*m/(2*c))]:
                tp=np.linalg.solve(matrix,np.array([0,Pp*total]))
                derivatives[p][key][-2:,qc]=tp.real
                if m:derivatives[p][key][-2:,qs]=tp.imag
    for key in ['B','D']:
        n=len(out[key])
        if n>=2:out[key][-1]=-(np.arange(n-1,dtype=float)**2@out[key][:-1])/(n-1)**2
    return out,derivatives

class ReducedParameterField(ParameterField):
    def __init__(self,directory,device='cpu',chunk=512):
        super().__init__(directory,device=device,chunk=chunk)
        self.free_source={key:np.array(self.arrays[key],copy=True) for key in ['A','C','B','D','E']}
        self._set_parameters(self.c_l,self.omega)
    def _set_parameters(self,c,w):
        self.c_l,self.omega=float(c),float(w)
        self.alpha=(1-self.c_l)/self.c_l;self.kappa=self.radial_ratio=self.omega/self.c_l
        coeff,partial=expand_coefficients(self.free_source,self.modes,self.c_l,self.omega)
        self.coeff={key:torch.tensor(value,device=self.device,dtype=torch.float64) for key,value in coeff.items()}
        self.coeff_partial={p:{key:torch.tensor(value,device=self.device,dtype=torch.float64) for key,value in dd.items()} for p,dd in partial.items()}
    def at(self,c_l,omega):
        other=copy.copy(self);other._set_parameters(c_l,omega);return other
    def torch_parameter_values(self,y,parameter=None,exterior=False):
        u,du=ParameterField.torch_parameter_values(self,y,parameter,exterior)
        if parameter is not None:
            extra=copy.copy(self);extra.coeff=self.coeff_partial[parameter]
            uc,duc=ParameterField.torch_parameter_values(extra,y,None,exterior)
            u=u+uc;du=du+duc
        return u,du
