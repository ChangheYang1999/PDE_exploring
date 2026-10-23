"""Independent shifted-basis reader. Derivation: dynamic_local_reconstruction/PROOF.md.
Numeric checkpoint loading only; no producer modules or unrestricted pickle.
"""
from pathlib import Path
from fractions import Fraction as F
import hashlib
import numpy as np
import gmpy2
from q_checkpoint_reader import QCheckpoint


def load_numeric(path):
    path=Path(path)
    if path.suffix!='.pt':
        with np.load(path,allow_pickle=False) as f:return {k:f[k] for k in f.files}
    import torch
    torch.set_num_threads(1)
    constructors=[np._core.multiarray.scalar,np.dtype,type(np.dtype('float64')),type(np.dtype('float32'))]
    with torch.serialization.safe_globals(constructors):
        return torch.load(path,map_location='cpu',weights_only=True)


def exact_affine_chebyshev(coeff,alpha,beta):
    """Exact ordinary Chebyshev coefficients of sum c_j T_j(alpha*t+beta)."""
    q=gmpy2.mpq
    def exact(v):
        if isinstance(v,F):return q(v.numerator,v.denominator)
        if isinstance(v,gmpy2.mpq):return v
        n,d=float(v).as_integer_ratio();return q(n,d)
    cc=list(map(exact,coeff));alpha=exact(alpha);beta=exact(beta)
    zero=q(0);N=len(cc)-1
    old=[q(1)];out=[zero for _ in cc];out[0]=cc[0]
    if N:
        cur=[beta,alpha]
        for i,v in enumerate(cur):out[i]+=cc[1]*v
        for j in range(1,N):
            nxt=[zero for _ in range(j+2)]
            for i,v in enumerate(cur):
                nxt[i]+=2*beta*v
                if i==0:nxt[1]+=2*alpha*v
                else:nxt[i-1]+=alpha*v;nxt[i+1]+=alpha*v
            for i,v in enumerate(old):nxt[i]-=v
            for i,v in enumerate(nxt):out[i]+=cc[j+1]*v
            old,cur=cur,nxt
    return [F(int(v.numerator),int(v.denominator)) for v in out]


class QLocalCheckpoint(QCheckpoint):
    def __init__(self,path):
        self.path=Path(path);d=load_numeric(path);self.data=d
        def number(key):
            v=d[key]
            if hasattr(v,'detach'):v=v.detach().cpu().numpy()
            return np.array(v,dtype=float)
        self.basis=str(d.get('basis','cheb'))
        if self.basis not in ('local','cheb'):raise ValueError('Unknown coefficient basis')
        self.N=int(d['N']);self.M=int(d['M']);self.u=number('u').reshape(-1)
        if not (1<=self.M<=self.N+1):raise ValueError('Invalid dimensions')
        self.coeff=[];start=0
        for k in range(self.M):
            size=self.N+1-k;self.coeff.append(self.u[start:start+size]);start+=size
        if start!=len(self.u):raise ValueError('Wrong coefficient count')
        self.node_values=number('beta') if 'beta' in d else None
        self.meta={k:float(d[k]) for k in ('cl','L','p','gamma','Lf','gK','mu','C','cw','cx','c','tau','rcond') if k in d and d[k] is not None}
        self.meta.update(N=self.N,M=self.M,basis=self.basis,source=str(self.path.resolve()),sha256=hashlib.sha256(self.path.read_bytes()).hexdigest())
        self.L=self.meta['L'];self.kappa=self.meta['p'];self.eta=1/self.kappa;self.p=1-self.eta
        self.cl=self.meta['cl'];self.mu=self.meta.get('mu',0.);self.Lf=self.meta.get('Lf',self.L)
        if self.kappa<=1 or self.L<=0:raise ValueError('Requires sublinear map')
        self.tk=number('tk') if 'tk' in d else -np.cos(2*np.pi*np.arange(self.N+1)/(2*self.N+1))
        if self.tk.shape!=(self.N+1,) or not np.isfinite(self.tk).all() or self.tk[0]!=-1. or self.tk[-1]>=1. or not np.all(np.diff(self.tk)>0):
            raise ValueError('Invalid stored basis nodes')
        self.meta['basis_nodes_source']='stored' if 'tk' in d else 'reconstructed Radau fallback' 
        self.dcoeff=[np.polynomial.chebyshev.chebder(cc) for cc in self.coeff]
        self._exact={}

    def polynomial(self,k,t):
        t=np.asarray(t,float)
        if k>=self.M:return np.zeros_like(t)
        s=(2*t-1-self.tk[k])/(1-self.tk[k]) if self.basis=='local' else t
        b1=np.zeros_like(s);b2=np.zeros_like(s)
        for v in self.coeff[k][:0:-1]:
            b0=v+2*s*b1-b2;b2,b1=b1,b0
        return self.coeff[k][0]+s*b1-b2

    def polynomial_derivative(self,k,t):
        t=np.asarray(t,float)
        if k>=self.M:return np.zeros_like(t)
        s=(2*t-1-self.tk[k])/(1-self.tk[k]) if self.basis=='local' else t
        fac=2/(1-self.tk[k]) if self.basis=='local' else 1.
        return fac*np.polynomial.chebyshev.chebval(s,self.dcoeff[k])

    def exact_coefficients(self,count=None):
        count=self.M if count is None else min(count,self.M)
        for k in range(count):
            if k in self._exact:continue
            if self.basis=='cheb':row=list(map(F,self.coeff[k]))
            else:
                tk=F(float(self.tk[k]));row=exact_affine_chebyshev(self.coeff[k],2/(1-tk),-(1+tk)/(1-tk))
            self._exact[k]=row
        return [self._exact[k] for k in range(count)]

    def node_reconstruction_details(self):
        if self.node_values is None:return None
        own=np.column_stack([self.polynomial(k,self.tk) for k in range(self.M)])
        if own.shape!=self.node_values.shape:raise ValueError('Wrong saved beta shape')
        delta=abs(own-self.node_values);mode_delta=delta*((1+self.tk[:,None])/2)**np.arange(self.M)[None,:]
        scale=np.maximum(abs(own),abs(self.node_values))
        return {'beta_absolute_max':float(delta.max()),'beta_scaled_max':float((delta/(1+scale)).max()),'mode_values_absolute_max':float(mode_delta.max()),'largest_saved_beta':float(abs(self.node_values).max())}

    def node_reconstruction_error(self):
        d=self.node_reconstruction_details();return d['beta_absolute_max'] if d else None

    def save_snapshot(self,path):
        scalars={k:self.meta[k] for k in ('N','M','L','p','gamma','cl','mu','Lf','gK','C','cw','cx','c','tau','rcond') if k in self.meta}
        np.savez_compressed(path,u=self.u,basis=self.basis,tk=self.tk,**scalars)

    def center_and_tail(self):
        raise NotImplementedError('Use exact_coefficients with q_exact_jets; do not evaluate shifted coefficients as unshifted.')
