"""Independent reconstruction of published/checkpoint density values.

Only the mathematical grid/representation and numeric checkpoint are read.
No numerics-lane module, inverse, or differentiation code is imported.
"""
from pathlib import Path
import hashlib
import numpy as np
from scipy.fft import dct
from numpy.polynomial import chebyshev as cheb


class Candidate:
    def __init__(self,path,project_center=False):
        self.path=Path(path)
        if self.path.suffix=='.pt':
            import torch
            torch.set_num_threads(1)
            d=torch.load(self.path,map_location='cpu',weights_only=True)
            self.values=d['b'].detach().numpy().astype(float)
            self.meta={k:float(d[k]) if k not in ['N','M'] else int(d[k]) for k in ['N','M','L','gamma','p','cl']}
        elif self.path.suffix=='.npz':
            d=np.load(self.path,allow_pickle=False)
            self.values=np.array(d['b'],float)
            self.meta={k:float(d[k]) if k not in ['N','M'] else int(d[k]) for k in ['N','M','L','gamma','p','cl']}
        else:
            raise ValueError('Expected numeric .pt or .npz checkpoint')
        for key in ('mu','beta','eps','forcing_width','Lf'):
            if key in d:self.meta[key]=float(d[key])
        N=self.meta['N']; M=self.meta['M']
        if self.values.shape!=(N+1,M): raise ValueError('Unexpected shape')
        self.nodes=-np.cos(2*np.pi*np.arange(N+1)/(2*N+1))
        angular=dct(self.values,type=2,axis=1)/M
        angular[:,0]/=2
        self.coefficients=np.linalg.solve(cheb.chebvander(self.nodes,N),angular)
        self.meta['sha256']=hashlib.sha256(self.path.read_bytes()).hexdigest()
        self.meta['source']=str(self.path.resolve())
        self._p=self.meta['p']; self._L=self.meta['L']; self._gamma=self.meta['gamma']
        self.project_center=project_center
        self.endpoint_modes=cheb.chebval(-1,self.coefficients)
        self.endpoint_modes[0]=0
        self.meta['center_projection']=bool(project_center)
        self.meta['max_projected_mode']=float(np.max(np.abs(self.endpoint_modes))) if project_center else 0.

    def compact_coordinate(self,r):
        """Solve p log(1-t)-log(1+t)=log(L/r) by safeguarded vector Newton.

        The variable z=1-t avoids cancellation when the physical radius is large.
        """
        r=np.asarray(r,float)
        safe=np.maximum(r,np.finfo(float).tiny)
        logratio=np.log(safe/self._L)
        p=self._p
        z=np.minimum(1.999999999999, np.exp(np.clip((np.log(2)-logratio)/p,-740,np.log(2))))
        small=logratio < -8
        # Near r=0 use t+1 as the Newton variable to retain endpoint derivatives.
        lo=np.zeros_like(z); hi=np.full_like(z,2.)
        done=np.zeros_like(z,dtype=bool)
        for _ in range(64):
            zz=np.clip(z,np.finfo(float).tiny,2-np.finfo(float).eps)
            fun=np.log(2-zz)-p*np.log(zz)-logratio
            delta=fun/(1/(2-zz)+p/zz)
            converged=(np.abs(fun)<=2*np.finfo(float).eps*(1+np.abs(logratio))) | (zz+delta==zz)
            done |= converged
            if np.all(done):break
            lo=np.where((fun>0)&~done,zz,lo); hi=np.where((fun<=0)&~done,zz,hi)
            trial=zz+delta
            next_z=np.where((trial>lo)&(trial<hi),trial,(lo+hi)/2)
            z=np.where(done,zz,next_z)
        t=1-z
        if np.any(small):
            # q=1+t, r/L=q/(2-q)^p; q is small here.
            q=np.minimum(1.,np.exp(np.clip(logratio[small]+p*np.log(2),-740,0)))
            target=logratio[small]
            for _ in range(14):
                fun=np.log(q)-p*np.log(2-q)-target
                qnew=q-fun/(1/q+p/(2-q))
                q=np.where(qnew>0,qnew,q/2)
            t=np.array(t,copy=True); t[small]=-1+q
        return np.where(r==0,-1.,t)

    def rho(self,x,y):
        x,y=np.broadcast_arrays(np.asarray(x,float),np.asarray(y,float))
        shape=x.shape
        xx=x.reshape(-1); yy=y.reshape(-1)
        r=np.hypot(xx,yy)
        t=self.compact_coordinate(r)
        # Chebyshev Clenshaw in r, then cos(2 theta) polynomial in angle.
        out=np.empty(len(r))
        for lo in range(0,len(r),32768):
            hi=min(lo+32768,len(r))
            modes=cheb.chebval(t[lo:hi],self.coefficients)
            if self.project_center: modes=modes-self.endpoint_modes[:,None]
            rr=r[lo:hi]
            z=np.divide(xx[lo:hi]**2-yy[lo:hi]**2,rr**2,out=np.ones_like(rr),where=rr>0)
            # Angle cos(2k theta)=T_k(cos(2 theta)), evaluated pointwise.
            b0=np.zeros_like(rr); b1=np.zeros_like(rr)
            for mode in modes[:0:-1]:
                b0,b1=mode+2*z*b0-b1,b0
            b=modes[0]+z*b0-b1
            logw=(self._gamma-1)*np.log(np.hypot(self._L,rr)/self._L)
            out[lo:hi]=yy[lo:hi]*np.exp(logw)*b
        return out.reshape(shape)

    def polar_density(self,r,theta):
        r=np.asarray(r,float)
        theta=np.asarray(theta,float)
        modes=cheb.chebval(self.compact_coordinate(r),self.coefficients)
        if self.project_center: modes=modes-self.endpoint_modes[:,None]
        angular=np.cos(2*np.arange(self.meta['M'])[:,None]*theta[None,:])
        b=modes.T@angular
        weight=np.exp((self._gamma-1)*np.log(np.hypot(self._L,r)/self._L))
        return (r*weight)[:,None]*np.sin(theta)[None,:]*b

    def endpoint_t_jets(self,order=4):
        return np.array([cheb.chebval(-1,cheb.chebder(self.coefficients,m=j,axis=0)) for j in range(order+1)])

    def save_snapshot(self,path):
        np.savez_compressed(path,b=self.values,**{k:self.meta[k] for k in ['N','M','L','gamma','p','cl','mu','beta','eps','forcing_width','Lf'] if k in self.meta})
