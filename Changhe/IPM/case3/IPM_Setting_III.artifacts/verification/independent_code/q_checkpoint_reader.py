"""Independent Q/QL density reconstruction from numeric coefficient checkpoints.

The producer's modules, inverse and differentiation routines are never imported.
The fixed map is inverted by safeguarded Newton with separate endpoint variables.
Cartesian angular powers and scalar Clenshaw reconstruct the density.
"""
from pathlib import Path
import hashlib
import numpy as np
from scipy.integrate import quad

class QCheckpoint:
    def __init__(self,path):
        self.path=Path(path)
        if self.path.suffix=='.pt':
            import torch
            torch.set_num_threads(1)
            data=torch.load(self.path,map_location='cpu',weights_only=True)
            numbers=lambda key:np.array(data[key].detach().cpu(),dtype=float)
        else:
            data=np.load(self.path,allow_pickle=False)
            numbers=lambda key:np.array(data[key],dtype=float)
        basis=str(data.get('basis','cheb'))
        if basis != 'cheb':
            raise NotImplementedError(f'QCheckpoint requires unshifted Chebyshev coefficients; input basis={basis!r}. Use a separately validated basis-aware reader.')
        self.meta={k:float(data[k]) for k in ('cl','L','p','gamma','Lf','gK','mu') if k in data and data[k] is not None}
        self.N=int(data['N']);self.M=int(data['M'])
        self.meta.update(N=self.N,M=self.M,source=str(self.path.resolve()),sha256=hashlib.sha256(self.path.read_bytes()).hexdigest())
        self.u=numbers('u').reshape(-1)
        self.node_values=numbers('beta') if 'beta' in data else None
        expected=sum(self.N+1-k for k in range(self.M))
        if len(self.u)!=expected:raise ValueError(f'{len(self.u)} coefficients, expected {expected}')
        self.coeff=[];start=0
        for k in range(self.M):
            size=self.N+1-k;self.coeff.append(self.u[start:start+size]);start+=size
        self.L=self.meta['L'];self.kappa=self.meta['p'];self.eta=1/self.kappa
        self.p=1-self.eta;self.cl=self.meta['cl'];self.mu=self.meta.get('mu',0.)
        self.Lf=self.meta.get('Lf',self.L)
        if not self.kappa>1:raise ValueError('This evaluator requires a sublinear growing tail')
        self.meta.update(actual_density_exponent=self.p,recorded_gamma=self.meta.get('gamma'),map_kappa=self.kappa)

    def polynomial(self,k,t):
        t=np.asarray(t,float)
        if k>=self.M:return np.zeros_like(t)
        b1=np.zeros_like(t);b2=np.zeros_like(t)
        for ck in self.coeff[k][:0:-1]:
            b0=ck+2*t*b1-b2;b2,b1=b1,b0
        return self.coeff[k][0]+t*b1-b2

    def coordinates(self,r):
        """Return t, sigma and w, retaining both small endpoint factors."""
        r=np.asarray(r,float);shape=r.shape;rr=r.reshape(-1)
        s=np.log(np.maximum(rr,np.finfo(float).tiny)/self.L)
        positive=rr>0
        if np.any(rr<0):raise ValueError('Radius must be nonnegative')
        small=(s<=-.5*np.log(2.))&positive
        sig=np.zeros_like(rr);w=np.ones_like(rr);t=-np.ones_like(rr)
        for mask in (small,(~small)&positive):
            target=s[mask]
            if not target.size:continue
            lo=np.zeros_like(target)
            if mask is small:
                hi=np.full_like(target,.5)
                q=np.exp(np.clip(2*target+2*self.kappa*np.log(2.),-740,np.log(.5)))
            else:
                hi=np.ones_like(target)
                q=np.exp(np.clip(-target/self.kappa,-740,0.))
            done=np.zeros_like(q,dtype=bool)
            for _ in range(72):
                q=np.maximum(q,np.finfo(float).tiny)
                if mask is small:
                    f=np.log(q)-2*self.kappa*np.log1p(-q)-2*target-2*self.kappa*np.log(2.)
                    df=1/q+2*self.kappa/(1-q)
                else:
                    f=self.kappa*np.log(q)-.5*np.log1p(-q/2)+target
                    df=self.kappa/q+.25/(1-q/2)
                trial=q-f/df
                # Include the large cancelling kappa terms in the floating-point residual scale.
                fscale=1+abs(target)+self.kappa*np.log(2.)
                adjacent=(hi-lo)<=4*np.finfo(float).eps*np.maximum(q,np.finfo(float).tiny)
                done|=(abs(f)<=8*np.finfo(float).eps*fscale) | (trial==q) | adjacent
                if np.all(done):break
                hi=np.where((f>0)&~done,q,hi);lo=np.where((f<=0)&~done,q,lo)
                trial=np.where((trial>lo)&(trial<hi),trial,(lo+hi)/2)
                q=np.where(done,q,trial)
            if not np.all(done):raise ArithmeticError('Radial Newton did not converge')
            if mask is small:
                sig[mask]=q;w[mask]=1-q;t[mask]=2*q-1
            else:
                w[mask]=q/2;sig[mask]=1-q/2;t[mask]=1-q
        sig=np.where(rr==0,0.,sig);w=np.where(rr==0,1.,w);t=np.where(rr==0,-1.,t)
        return t.reshape(shape),sig.reshape(shape),w.reshape(shape)

    def rho(self,x,y):
        x,y=np.broadcast_arrays(np.asarray(x,float),np.asarray(y,float));shape=x.shape
        xx=x.reshape(-1);yy=y.reshape(-1);out=np.empty_like(xx)
        for lo in range(0,len(xx),16384):
            hi=min(lo+16384,len(xx));xr=xx[lo:hi];yr=yy[lo:hi];r=np.hypot(xr,yr)
            t,sig,w=self.coordinates(r)
            ex=np.divide(xr,r,out=np.ones_like(r),where=r>0)
            ey=np.divide(yr,r,out=np.zeros_like(r),where=r>0)
            z=sig*(ex+1j*ey)**2;power=np.ones_like(z);total=np.zeros_like(r)
            for k in range(self.M):
                total+=power.real*self.polynomial(k,t);power*=z
            out[lo:hi]=yr*w*total
        return out.reshape(shape)

    def polar_density(self,r,theta):
        r=np.asarray(r,float);theta=np.asarray(theta,float)
        t,sig,w=self.coordinates(r)
        modes=np.array([sig**k*self.polynomial(k,t) for k in range(self.M)])
        angular=np.cos(2*np.arange(self.M)[:,None]*theta[None,:])
        return (r*w)[:,None]*np.sin(theta)[None,:]*(modes.T@angular)

    def center_and_tail(self):
        endpoints=np.array([sum(c) for c in self.coeff])
        centers=np.array([sum(c*(-1.)**np.arange(len(c))) for c in self.coeff])
        j=np.arange(len(self.coeff[0]));b0prime=float(sum(self.coeff[0]*np.where(j==0,0.,-(-1.)**j*j*j)))
        a=float(centers[0]);b1=float(centers[1]) if self.M>1 else 0.
        alpha=2**(2*self.kappa+1)/self.L**2
        common=alpha*(b0prime-a/2)
        b=common+alpha*b1/2;e=common-alpha*b1/2
        def strain(t):
            z=1-t;sig=(1+t)/2
            return (z/16+self.kappa*sig/4)*(self.polynomial(1,t)-sig*self.polynomial(2,t))
        def harmonic(t):
            z=1-t;sig=(1+t)/2
            return z**(2*self.kappa)*(z/4+self.kappa*sig)/self.L**2*(self.polynomial(2,t)-sig*self.polynomial(3,t))
        rows=[]
        for tol in (1e-8,1e-10,1e-12):
            cc,ce=quad(strain,-1,1,epsabs=tol,epsrel=tol,limit=350)
            hh,he=quad(harmonic,-1,1,epsabs=tol,epsrel=tol,limit=350)
            rows.append({'requested_tolerance':tol,'c':-a/4+cc,'c_error_estimate':ce,'H':-alpha*b1/8+hh,'H_error_estimate':he})
        c=rows[-1]['c'];H=rows[-1]['H'];delta=self.cl+c-1;A=2*self.cl-1
        gK=float(sum(endpoints*(-1.)**np.arange(self.M)))
        K=self.L**self.eta*gK/2;defect=self.cl*self.p-1
        angles=np.linspace(0,np.pi/2,4097)
        reduced=self.L**self.eta/2*(endpoints@np.cos(2*np.arange(self.M)[:,None]*angles[None,:]))
        return {'a0':a,'b':b,'e':e,'quadrature':rows,'Delta':delta,'source_eigenvalues':[self.cl-c,self.cl+c],
                'forced_center_defect':a*delta-self.mu,'unforced_center_defect':delta,
                'forced_cubic_T1':(a-2*A+delta)*b-3*(2+3*delta)*e-8*self.mu/self.Lf**2,
                'forced_cubic_T2':(a-4*A+2*delta)*b-3*a*H-4*self.mu/self.Lf**2,
                'actual_axis_gK':gK,'actual_axis_K':K,'ell_times_actual_exponent_minus_one':defect,
                'lim_axis_R_Nf':abs(defect)/(self.cl*self.p+1),'lim_axis_R_Nv':abs(defect)/(1+self.p),
                'sampled_min_Theta0_over_sin':float(min(reduced)),'sampled_max_Theta0_over_sin':float(max(reduced)),
                'sampled_angle_count':len(angles),'Theta0_prime_at_zero':float(reduced[0])}

    def node_reconstruction_error(self):
        if self.node_values is None:return None
        nodes=-np.cos(2*np.pi*np.arange(self.N+1)/(2*self.N+1))
        own=np.column_stack([self.polynomial(k,nodes) for k in range(self.M)])
        if own.shape!=self.node_values.shape:raise ValueError('Unexpected beta node-value shape')
        return float(np.max(abs(own-self.node_values)))

    def save_snapshot(self,path):
        scalars={k:self.meta[k] for k in ('N','M','L','p','gamma','cl','mu','Lf','gK') if k in self.meta}
        np.savez_compressed(path,u=self.u,**scalars)
