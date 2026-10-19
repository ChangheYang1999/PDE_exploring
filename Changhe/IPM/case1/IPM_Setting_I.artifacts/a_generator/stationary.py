"""Nonlinear positive-shape least squares, with the strain fixing the scale."""
import os
for key in ("OPENBLAS_NUM_THREADS","OMP_NUM_THREADS","MKL_NUM_THREADS","NUMEXPR_NUM_THREADS"):
    os.environ[key]="1"
import argparse
import json
import time
from pathlib import Path
import numpy as np
from numpy.polynomial.chebyshev import chebval, chebder
from scipy.optimize import least_squares
from scipy.optimize import OptimizeResult
from scipy.linalg import cho_factor,cho_solve
from scipy.interpolate import CubicSpline, BSpline
from scipy.optimize import brentq
from scipy.sparse.linalg import LinearOperator,lsmr
from solver import Problem


def normal_solve(fun,jac,x0,bounds,max_nfev=100,damping=1e-4):
    """Bounded, damped Gauss--Newton without a tall dense SVD.

    The normal equations are deliberately regularized. This is an optimizer,
    not a high-precision linear-system certificate. Every step must decrease
    the original nonlinear least-squares objective.
    """
    x=x0.copy();f=fun(x);nfev=1;cost=.5*np.dot(f,f)
    lower,upper=bounds;message="function evaluation limit"
    gradient_norm=float("inf")
    while nfev<max_nfev:
        stamp=time.monotonic()
        J=jac(x);jac_seconds=time.monotonic()-stamp
        stamp=time.monotonic()
        G=J.T@J;g=J.T@f
        print(json.dumps(dict(jacobian_seconds=jac_seconds,
                              gram_seconds=time.monotonic()-stamp)),flush=True)
        scale=1/np.sqrt(np.maximum(np.diag(G),1e-30))
        gs=scale*g
        G*=scale[:,None];G*=scale[None,:]
        gradient_norm=float(np.max(abs(gs)))
        if gradient_norm<1e-11:
            message="scaled gradient tolerance";break
        accepted=False
        for attempt in range(12):
            M=np.array(G,order="F",copy=True);M.flat[::len(x)+1]+=damping
            try:
                u=cho_solve(cho_factor(M,lower=True,check_finite=False,overwrite_a=True),-gs,
                            check_finite=False,overwrite_b=True)
            except np.linalg.LinAlgError:
                damping*=10;continue
            step=scale*u
            alpha=min(1.,2./max(np.max(abs(step)),1e-300))
            print(json.dumps(dict(damping=damping,
                                  largest_step=float(np.max(abs(step))),
                                  largest_step_index=int(np.argmax(abs(step))),
                                  initial_step_fraction=alpha)),flush=True)
            positive=step>0;negative=step<0
            if positive.any():
                alpha=min(alpha,float(np.min(.995*(upper[positive]-x[positive])/step[positive])))
            if negative.any():
                alpha=min(alpha,float(np.min(.995*(lower[negative]-x[negative])/step[negative])))
            for backtrack in range(8):
                trial=x+alpha*step
                ftrial=fun(trial);nfev+=1
                trialcost=.5*np.dot(ftrial,ftrial)
                if np.isfinite(trialcost) and trialcost<cost:
                    predicted=-alpha*np.dot(gs,u)-.5*alpha**2*np.dot(u,G@u)
                    ratio=(cost-trialcost)/max(predicted,1e-300)
                    if ratio>.75:damping=max(damping/3,1e-12)
                    elif ratio<.25:damping*=3
                    x=trial;f=ftrial;cost=trialcost;accepted=True
                    break
                alpha*=.5
                if nfev>=max_nfev:break
            if accepted or nfev>=max_nfev:break
            damping*=10
        if not accepted:
            message="no decreasing damped step";break
    return OptimizeResult(x=x,fun=f,nfev=nfev,optimality=gradient_norm,
                          message=message,damping=damping)


def krylov_solve(fun,linearize,x0,bounds,max_nfev=100,damping=1e-6,maxiter=300,
                 deadline=None,initial_step=None):
    """Inexact damped Gauss--Newton using an explicitly checked adjoint."""
    x=x0.copy();f=fun(x);nfev=1;cost=.5*np.dot(f,f)
    lower,upper=bounds;message="function evaluation limit";optimality=float("inf")
    def check_time():
        if deadline is not None and time.monotonic()>deadline:
            raise TimeoutError("matrix-free stationary chunk time budget reached")
    while nfev<max_nfev:
        check_time();stamp=time.monotonic();op=linearize(x)
        # A deterministic stochastic diagonal is used only as a preconditioner.
        # It does not modify the residual or determine acceptance.
        rng=np.random.default_rng(8128);diagonal=np.zeros(len(x))
        for _ in range(12):
            check_time()
            probe=rng.choice(np.array([-1.,1.]),size=len(f))
            diagonal+=op.rmatvec(probe)**2/12
        cutoff=max(float(np.max(diagonal))*1e-18,1e-24)
        scale=1/np.sqrt(np.maximum(diagonal,cutoff))
        scale[diagonal<cutoff]=0.
        def mv(u):
            check_time();return op@(scale*u)
        def rmv(v):
            check_time();return scale*op.rmatvec(v)
        scaled=LinearOperator(op.shape,matvec=mv,rmatvec=rmv,dtype=float)
        optimality=float(np.max(abs(rmv(f))))
        if optimality<1e-12:
            message="scaled gradient tolerance";break
        accepted=False
        for attempt in range(6):
            guess=None
            if initial_step is not None:
                guess=np.divide(initial_step,scale,out=np.zeros_like(scale),
                                where=scale!=0)
            if guess is None:
                linear=lsmr(scaled,-f,damp=np.sqrt(damping),atol=1e-9,btol=1e-9,
                            maxiter=maxiter)
            else:
                # Explicit augmentation keeps regularization centred at
                # zero even when LSMR starts from a nonzero guess.
                nrow,ncol=scaled.shape
                root_damping=np.sqrt(damping)
                augmented=LinearOperator((nrow+ncol,ncol),
                    matvec=lambda u:np.r_[scaled@u,root_damping*u],
                    rmatvec=lambda v:scaled.rmatvec(v[:nrow])+root_damping*v[nrow:],
                    dtype=float)
                linear=lsmr(augmented,np.r_[-f,np.zeros(ncol)],damp=0.,
                            atol=1e-9,btol=1e-9,maxiter=maxiter,x0=guess)
            initial_step=None
            u=linear[0]
            proposed=scale*u
            # Numerically weak coordinates should not shorten every other
            # coordinate's step. Clip them, then assess the actual direction.
            step=np.clip(proposed,-2.,2.)
            linear_step=op@step
            alpha=1.
            positive=step>0;negative=step<0
            if positive.any():
                alpha=min(alpha,float(np.min(.995*(upper[positive]-x[positive])/step[positive])))
            if negative.any():
                alpha=min(alpha,float(np.min(.995*(lower[negative]-x[negative])/step[negative])))
            print(json.dumps(dict(krylov_iterations=int(linear[2]),damping=damping,
                    predicted_linear_norm=float(np.linalg.norm(f+linear_step)),
                    largest_step=float(np.max(abs(step))),initial_step_fraction=alpha,
                    largest_proposed_step=float(np.max(abs(proposed))),
                    linear_seconds=time.monotonic()-stamp)),flush=True)
            for backtrack in range(8):
                trial=x+alpha*step;ftrial=fun(trial);nfev+=1
                trialcost=.5*np.dot(ftrial,ftrial)
                if np.isfinite(trialcost) and trialcost<cost:
                    predicted=cost-.5*np.dot(f+alpha*linear_step,f+alpha*linear_step)
                    ratio=(cost-trialcost)/max(predicted,1e-300)
                    if ratio>.75:damping=max(damping/5,1e-12)
                    elif ratio<.25:damping*=3
                    x=trial;f=ftrial;cost=trialcost;accepted=True;break
                alpha*=.5
                if nfev>=max_nfev:break
            if accepted or nfev>=max_nfev:break
            damping*=10
        if not accepted:
            message="no decreasing Krylov step";break
    return OptimizeResult(x=x,fun=f,nfev=nfev,optimality=optimality,
                          message=message,damping=damping)


class Shape:
    def __init__(self,nr=256,nt=48,R=1000.,degree=5,angular=5,compact="quadratic",
                 singular=0,angular_cap=0,rmin=1e-4):
        self.p=Problem(nr,nt,R,rmin=rmin,quadrature_order=4)
        self.degree,self.angular=degree,angular
        self.compact=compact
        self.singular=singular
        self.angular_cap=angular_cap
        self.radial_basis="chebyshev"
        self.spline_order=3
        self.origin_radius=0.
        p=self.p
        s=p.rr**2/(1+p.rr**2)
        self.s=s
        self.base=-1.5*np.log1p(p.rr**2)*np.ones_like(p.factor)
        self.base_k=.5*np.log1p(p.rr**2)*np.ones_like(p.factor)
        self.bt0=-3*s*np.ones_like(p.factor)
        self.btk=s*np.ones_like(p.factor)
        self.basis_k=None
        self.names=[(m,j) for m in range(angular+1) for j in range(degree)]
        self.names.extend([(-1,j) for j in range(singular)])
        self.rows=(p.r>.04)&(p.r<min(R*.9,300))
        self.cols=np.arange(p.nt+1)
        self.weight=np.ones_like(p.factor[self.rows])
        # Equal log-radius measure, including axis transverse equations.
        self.history=[];self.calls=0;self.best=np.inf;self.start=time.monotonic()
        self.source_weight=0.
        self.objective="normalized"
        self.best_z=None
        self.seconds=float("inf")

    def build_basis(self,k):
        if self.radial_basis=="spline":
            self._build_spline_tensor(k)
            return
        p=self.p;s=self.s
        if self.compact=="matched":
            q=-np.expm1(-(1-k)/2*np.log1p(p.rr**2))
            qt=(1-k)*s*(1-q)
        else:
            q=s;qt=2*s*(1-s)
        z=2*q-1
        count=(self.angular+1)*self.degree+self.singular
        # The basis is used synchronously. Refill its storage when changing k,
        # rather than retaining two large copies during every exponent
        # difference and every diagnostic reconstruction.
        def storage(name,shape):
            previous=getattr(self,name,None)
            return previous if previous is not None and previous.shape==shape else np.empty(shape)
        radial=storage("radial",(count,p.nr))
        radial_t=storage("radial_t",(count,p.nr))
        angular_values=storage("angular_values",(count,p.nt+1))
        angular_derivatives=storage("angular_derivatives",(count,p.nt+1))
        axis_second=storage("axis_second",(count,));names=[]
        if self.radial_basis=="spline":
            order=self.spline_order
            knots=getattr(self,"spline_knots",None)
            if knots is None:knots=np.r_[np.zeros(order+1),
                        np.linspace(0,1,self.degree-order+2)[1:-1]**1.3,
                        np.ones(order+1)]
            spline=BSpline(knots,np.eye(self.degree+1),order,extrapolate=False)
            spline_values=spline(q[:,0])[:,1:]
            spline_derivatives=spline(q[:,0],nu=1)[:,1:]*qt
        else:
            chebs=[];cheb_derivatives=[]
            for j in range(self.degree):
                coeff=np.zeros(j+1);coeff[j]=1
                chebs.append(chebval(z,coeff))
                cheb_derivatives.append(
                    chebval(z,chebder(coeff)) if j else np.zeros_like(z))
        for m in range(self.angular+1):
            power=max(m,1)
            if self.angular_cap:power=min(power,self.angular_cap)
            for j in range(self.degree):
                if self.radial_basis=="spline":
                    b=spline_values[:,j,None];bt=spline_derivatives[:,j,None]
                    if self.origin_radius>0 and m>1:
                        chi=p.rr**2/(p.rr**2+self.origin_radius**2)
                        multiplier=chi**(m-1)
                        bt=(bt+2*(m-1)*(1-chi)*b)*multiplier
                        b=b*multiplier
                else:
                    cheb=chebs[j];der=cheb_derivatives[j]
                    b=s**power*cheb
                    bt=power*s**(power-1)*cheb*2*s*(1-s)+2*s**power*der*qt
                idx=len(names)
                radial[idx]=b[:,0];radial_t[idx]=bt[:,0]
                angular_values[idx]=np.cos(2*m*p.theta)
                angular_derivatives[idx]=-2*m*np.sin(2*m*p.theta)
                axis_second[idx]=-4*m*m
                names.append((m,j))
        exponent=6+2*k/(2-k)
        for j in range(self.singular):
            coeff=np.zeros(j+1);coeff[j]=1
            cheb=chebval(z,coeff)
            der=chebval(z,chebder(coeff)) if j else np.zeros_like(z)
            angular=p.ct**(exponent-2)*p.st**2
            angularprime=2*p.ct**(exponent-1)*p.st-(exponent-2)*p.ct**(exponent-3)*p.st**3
            b=s**(exponent/2)*cheb
            bt=exponent*s**(exponent/2)*(1-s)*cheb+2*s**(exponent/2)*der*qt
            idx=len(names)
            radial[idx]=b[:,0];radial_t[idx]=bt[:,0]
            angular_values[idx]=angular;angular_derivatives[idx]=angularprime
            axis_second[idx]=2
            names.append((-1,j))
        self.radial=radial;self.radial_t=radial_t
        self.angular_values=angular_values;self.angular_derivatives=angular_derivatives
        self.axis_second=axis_second
        self.names=names
        self.basis_k=k

    def _build_spline_tensor(self,k):
        """Same basis without repeating every radial/angular factor."""
        p=self.p
        q=-np.expm1(-(1-k)/2*np.log1p(p.r**2)) if self.compact=="matched" else self.s[:,0]
        qt=(1-k)*self.s[:,0]*(1-q) if self.compact=="matched" else 2*q*(1-q)
        knots=getattr(self,"spline_knots",None)
        if knots is None:
            knots=np.r_[np.zeros(self.spline_order+1),
                         np.linspace(0,1,self.degree-self.spline_order+2)[1:-1]**1.3,
                         np.ones(self.spline_order+1)]
        spl=BSpline(knots,np.eye(self.degree+1),self.spline_order)
        self.tensor_b=spl(q)[:,1:]
        self.tensor_bt=spl(q,nu=1)[:,1:]*qt[:,None]
        m=np.arange(self.angular+1)
        j=np.maximum(m-1,0)
        chi=p.r**2/(p.r**2+self.origin_radius**2) if self.origin_radius else np.ones(p.nr)
        self.tensor_mult=chi[:,None]**j
        self.tensor_lt=2*j*(1-chi[:,None])
        self.tensor_cos=np.cos(2*m[:,None]*p.theta)
        self.tensor_sinprime=-2*m[:,None]*np.sin(2*m[:,None]*p.theta)
        exponent=6+2*k/(2-k)
        self.tensor_sg=np.empty((p.nr,self.singular))
        self.tensor_sgt=np.empty_like(self.tensor_sg)
        for j in range(self.singular):
            c=np.zeros(j+1);c[j]=1.
            val=chebval(2*q-1,c);dv=chebval(2*q-1,chebder(c)) if j else np.zeros_like(q)
            self.tensor_sg[:,j]=self.s[:,0]**(exponent/2)*val
            self.tensor_sgt[:,j]=exponent*(1-self.s[:,0])*self.tensor_sg[:,j]+2*self.s[:,0]**(exponent/2)*dv*qt
        self.tensor_sga=p.ct**(exponent-2)*p.st**2
        self.tensor_sgap=2*p.ct**(exponent-1)*p.st-(exponent-2)*p.ct**(exponent-3)*p.st**3
        self.names=[(m,j) for m in range(self.angular+1) for j in range(self.degree)]
        self.names.extend([(-1,j) for j in range(self.singular)])
        self.basis_k=k
        for name in ("radial","radial_t","angular_values","angular_derivatives","axis_second"):
            if hasattr(self,name):delattr(self,name)

    def apply_basis(self,coef):
        """Contract radial profiles before summing their angular factors."""
        if self.radial_basis=="spline":
            co=coef[:(self.angular+1)*self.degree].reshape(self.angular+1,self.degree)
            b=self.tensor_b@co.T
            bt=(self.tensor_bt@co.T+self.tensor_lt*b)*self.tensor_mult
            b=b*self.tensor_mult
            h=b@self.tensor_cos;ht=bt@self.tensor_cos;ha=b@self.tensor_sinprime
            if self.singular:
                sg=self.tensor_sg@coef[-self.singular:]
                sgt=self.tensor_sgt@coef[-self.singular:]
                h+=sg[:,None]*self.tensor_sga
                ht+=sgt[:,None]*self.tensor_sga
                ha+=sg[:,None]*self.tensor_sgap
            return h,ht,ha
        count=self.angular+1
        radial=np.empty((self.p.nr,count+self.singular))
        radial_t=np.empty_like(radial)
        indices=[]
        for m in range(count):
            sl=slice(m*self.degree,(m+1)*self.degree)
            radial[:,m]=coef[sl]@self.radial[sl]
            radial_t[:,m]=coef[sl]@self.radial_t[sl]
            indices.append(m*self.degree)
        for j in range(self.singular):
            i=count*self.degree+j
            radial[:,count+j]=coef[i]*self.radial[i]
            radial_t[:,count+j]=coef[i]*self.radial_t[i]
            indices.append(i)
        angles=self.angular_values[indices]
        return (radial@angles,radial_t@angles,
                radial@self.angular_derivatives[indices])

    def transpose_basis(self,h,ht,ha):
        if self.radial_basis=="spline":
            gh=(h@self.tensor_cos.T+ha@self.tensor_sinprime.T)*self.tensor_mult
            gt=(ht@self.tensor_cos.T)*self.tensor_mult
            co=(self.tensor_b.T@(gh+self.tensor_lt*gt)+self.tensor_bt.T@gt).T.ravel()
            if self.singular:
                sg=self.tensor_sg.T@(h@self.tensor_sga+ha@self.tensor_sgap)
                sg+=self.tensor_sgt.T@(ht@self.tensor_sga)
                co=np.r_[co,sg]
            return co
        count=self.angular+1
        indices=list(range(0,count*self.degree,self.degree))+list(
            range(count*self.degree,len(self.names)))
        gh=h@self.angular_values[indices].T
        gt=ht@self.angular_values[indices].T
        ga=ha@self.angular_derivatives[indices].T
        answer=np.empty(len(self.names))
        for m in range(count):
            sl=slice(m*self.degree,(m+1)*self.degree)
            answer[sl]=self.radial[sl]@(gh[:,m]+ga[:,m])+self.radial_t[sl]@gt[:,m]
        for j in range(self.singular):
            i=count*self.degree+j
            answer[i]=np.dot(self.radial[i],gh[:,count+j]+ga[:,count+j])+np.dot(
                self.radial_t[i],gt[:,count+j])
        return answer

    def evaluate(self,z,release_basis=False):
        k=z[0];coef=z[1:]
        if self.basis_k is None or ((self.compact=="matched" or self.singular) and k!=self.basis_k):self.build_basis(k)
        H,ht,ha=self.apply_basis(coef)
        H+=self.base+k*self.base_k
        ht+=self.bt0+k*self.btk
        if self.radial_basis=="spline":
            co=coef[:(self.angular+1)*self.degree].reshape(self.angular+1,self.degree)
            haa_axis=((self.tensor_b@co.T)*self.tensor_mult)@(-4*np.arange(self.angular+1)**2)
            if self.singular:haa_axis+=2*(self.tensor_sg@coef[-self.singular:])
        else:
            haa_axis=(coef*self.axis_second)@self.radial
        if release_basis:
            # A diagnostic evaluation needs no subsequent parameter
            # derivatives. Release these tables before forming the fields.
            for name in ("radial","radial_t","angular_values","angular_derivatives","axis_second",
                         "tensor_b","tensor_bt","tensor_mult","tensor_lt","tensor_cos",
                         "tensor_sinprime","tensor_sg","tensor_sgt","tensor_sga","tensor_sgap"):
                if hasattr(self,name):delattr(self,name)
        f=self.p.fields(H,tailk=k,ht=ht,ha=ha)
        f["haa_axis"]=haa_axis
        cl=1/k
        # Exact scaling identity c[L³F(X/L)] = L² c[F].
        L2=(3*cl-1)/f["c"]
        Uadv=2*f["ux"]+f["uy"]+f["ur"]*ht+f["ua"]*ha
        residual=cl*(3+ht)+L2*Uadv-1
        den=1+np.abs(3+ht)+np.abs(L2*Uadv)
        return H,f,L2,residual,den

    def fun(self,z):
        if time.monotonic()-self.start>self.seconds:
            raise TimeoutError("stationary chunk time budget reached")
        H,f,L2,res,den=self.evaluate(z)
        den=self.objective_den(f,den)
        if L2<=0 or not np.isfinite(L2):
            return np.full(self.weight.size+1,1e3)
        values=(res[self.rows][:,self.cols]/den[self.rows][:,self.cols])*self.weight
        source=self.source(f,L2,1/z[0])
        source_error=(source[1]-1) if source else 10.
        result=np.r_[values.ravel(),self.source_weight*source_error]
        self.calls+=1
        norm=np.linalg.norm(result)
        if norm<self.best*(1-1e-5):
            self.best=norm
            self.best_z=z.copy()
            info=dict(call=self.calls,seconds=time.monotonic()-self.start,
                      norm=norm,rms=norm/np.sqrt(len(result)),max=float(np.max(np.abs(values))),
                      k=z[0],cl=1/z[0],c=3/z[0]-1,c_shape=f["c"],
                      L=np.sqrt(L2),c_shape2=f["c2"],maxcoef=float(np.max(np.abs(z[1:]))),
                      source_mu2=source[1] if source else None,objective=self.objective)
            self.history.append(info)
            if getattr(self,"output",None):
                self.save(self.output,z)
            print(json.dumps(info),flush=True)
        return result

    def objective_den(self,f,den):
        if self.objective=="log":return 1+np.abs(3+f["ht"])
        if self.objective=="absolute":return np.ones_like(den)
        return den

    def source(self,f,L2,cl):
        a=cl+L2*f["ux"][:,0];b=cl+L2*f["uy"][:,0]
        inds=np.flatnonzero(a[:-1]*a[1:]<0)
        if not len(inds):return None
        i=inds[0];sa=CubicSpline(self.p.t,a);sb=CubicSpline(self.p.t,b)
        ts=brentq(sa,self.p.t[i],self.p.t[i+1])
        return ts,float(sb(ts)),float(sa(ts,1)),float(sb(ts,1))

    def jac(self,z):
        """Differentiate the linear velocity law and the strain normalization."""
        H,f,L2,res,den=self.evaluate(z)
        den=self.objective_den(f,den)
        p=self.p;k=z[0];cl=1/k
        # SciPy evaluates a new Jacobian only after accepting a step. Reuse
        # this buffer so references to J0 do not retain another dense matrix.
        shape=(self.weight.size+1,len(z))
        if not hasattr(self,"_jac_storage") or self._jac_storage.shape!=shape:
            self._jac_storage=np.empty(shape)
        J=self._jac_storage
        step=2e-6
        zp=z.copy();zm=z.copy();zp[0]+=step;zm[0]-=step
        _,fp,Lp,ep,dp=self.evaluate(zp)
        _,fm,Lm,em,dm=self.evaluate(zm)
        dp=self.objective_den(fp,dp);dm=self.objective_den(fm,dm)
        J[:-1,0]=((ep/dp-em/dm)[self.rows][:,self.cols]*self.weight).ravel()/(2*step)
        sp=self.source(fp,Lp,1/zp[0]);sm=self.source(fm,Lm,1/zm[0])
        J[-1,0]=self.source_weight*(sp[1]-sm[1])/(2*step) if sp and sm else 0.
        self.evaluate(z) # restore the basis at k
        source=self.source(f,L2,cl)
        Uadv=2*f["ux"]+f["uy"]+f["ur"]*f["ht"]+f["ua"]*f["ha"]
        angular_mix=p.ct[1:-1]/p.st[1:-1]-2*p.st[1:-1]/p.ct[1:-1]
        for start in range(0,len(z)-1,16):
            stop=min(start+16,len(z)-1)
            dh=self.radial[start:stop].T[:,:,None]*self.angular_values[None,start:stop,:]
            dht=self.radial_t[start:stop].T[:,:,None]*self.angular_values[None,start:stop,:]
            dha=self.radial[start:stop].T[:,:,None]*self.angular_derivatives[None,start:stop,:]
            drho=f["rho"][:,None,:]*dh
            drt=f["rt"][:,None,:]*dh+f["rho"][:,None,:]*dht
            dra=f["ra"][:,None,:]*dh+f["rho"][:,None,:]*dha
            dfx=(drt*p.ct-dra*p.st)/p.r[:,None,None]
            df=p.project_sine(dfx)
            dtail=((k*drho[-1])*p.ct-dra[-1]*p.st)/p.R@p.project
            dtail_B=None
            if p.tail_terms==2:
                projector=p.weights[:,None]*p.sodd.T
                modes=drho[-1]@projector
                modes_t=drt[-1]@projector
                second=(modes_t-k*modes)/(k-1)
                dtail_B=np.zeros_like(dtail)
                for exponent,part in ((k,modes-second),(2*k-1,second)):
                    ft=((exponent-p.m+1)*part[:,:-1]+
                        (exponent+p.m+1)*part[:,1:])/(2*p.R)
                    dtail_B+=ft/(p.m-1-exponent)
            A,B=p.modal_integrals(df,dtail,k,dtail_B)
            dq=(A+B)/(2*p.m);dv=(B-A)/2
            dur=-p.cosine_series(dq*p.m)
            dua=p.sine_series(dv)
            dquot=np.empty_like(dua)
            dquot[:,:,1:-1]=dua[:,:,1:-1]*angular_mix
            dquot[:,:,0]=np.sum(dv*p.m,axis=-1)
            dquot[:,:,-1]=2*np.sum(dv*(p.m*p.cos[:,-1]),axis=-1)
            dc=(B[0,:,0]+df[0,:,0]/2)/2
            dL2=-L2*dc/f["c"]
            dUadv=(3*dur+dquot+dur*f["ht"][:,None,:]+
                   f["ur"][:,None,:]*dht+dua*f["ha"][:,None,:]+f["ua"][:,None,:]*dha)
            dtotal=L2*dUadv+Uadv[:,None,:]*dL2[None,:,None]
            de=cl*dht+dtotal
            dd=np.sign(3+f["ht"])[:,None,:]*dht
            if self.objective=="normalized":dd+=np.sign(L2*Uadv)[:,None,:]*dtotal
            if self.objective=="absolute":dd=np.zeros_like(dd)
            dr=de/den[:,None,:]-res[:,None,:]*dd/den[:,None,:]**2
            J[:-1,start+1:stop+1]=np.moveaxis(
                dr[self.rows][:,:,self.cols]*self.weight[:,None,:],1,2).reshape(-1,stop-start)
            if source and self.source_weight:
                ts,_,at,bt=source
                da=L2*dur[:,:,0]+f["ux"][:,0,None]*dL2[None,:]
                db=L2*(dur[:,:,0]+np.sum(dv*p.m,axis=-1))+f["uy"][:,0,None]*dL2[None,:]
                J[-1,start+1:stop+1]=self.source_weight*(
                    CubicSpline(p.t,db)(ts)-bt/at*CubicSpline(p.t,da)(ts))
            else:J[-1,start+1:stop+1]=0.
        return J

    def save(self,path,z):
        H,f,L2,res,den=self.evaluate(z)
        L=np.sqrt(L2);p=self.p
        temporary=str(path)+".partial.npz"
        np.savez_compressed(temporary,z=z,names=np.asarray(self.names),degree=self.degree,
            angular=self.angular,compact=self.compact,singular=self.singular,
            angular_cap=self.angular_cap,radial_basis=self.radial_basis,
            spline_order=self.spline_order,origin_radius=self.origin_radius,
            tail_terms=self.p.tail_terms,
            r_shape=p.r,r=p.r*L,theta=p.theta,
            rho=L**3*f["rho"],H=H,c_l=1/z[0],c=3/z[0]-1,c_second=L2*f["c2"],
            L=L,k=z[0],R_shape=p.R,normalized_log_residual=res/den,
            residual=res*L**3*f["rho"],history=np.array([json.dumps(v) for v in self.history]),
            run_configuration=json.dumps(getattr(self,"run_configuration",{})))
        Path(temporary).replace(path)


def main():
    a=argparse.ArgumentParser()
    a.add_argument("--nr",type=int,default=256);a.add_argument("--nt",type=int,default=48)
    a.add_argument("--R",type=float,default=1000.)
    a.add_argument("--tail-terms",type=int,choices=[1,2],default=1)
    a.add_argument("--degree",type=int,default=4);a.add_argument("--angular",type=int,default=4)
    a.add_argument("--k",type=float,default=.5);a.add_argument("--load")
    a.add_argument("--compact",default="quadratic",choices=["quadratic","matched"])
    a.add_argument("--analytic-jac",action="store_true")
    a.add_argument("--min-k",type=float,default=.05)
    a.add_argument("--fixed-k",type=float)
    a.add_argument("--source-weight",type=float,default=0.)
    a.add_argument("--objective",choices=["normalized","log","absolute"],default="normalized")
    a.add_argument("--singular",type=int,default=0)
    a.add_argument("--angular-cap",type=int,default=0)
    a.add_argument("--radial-basis",choices=["chebyshev","spline"],default="chebyshev")
    a.add_argument("--spline-order",type=int,default=3)
    a.add_argument("--origin-radius",type=float,default=0.)
    a.add_argument("--tr-solver",choices=["exact","lsmr","normal","krylov"],default="exact")
    a.add_argument("--krylov-iterations",type=int,default=300)
    a.add_argument("--sample-normalize",action="store_true")
    a.add_argument("--radial-sample",type=int,default=1)
    a.add_argument("--angular-sample",type=int,default=1)
    a.add_argument("--fit-radius",type=float,default=300.)
    a.add_argument("--nfev",type=int,default=100)
    a.add_argument("--normal-damping",type=float,default=1e-4)
    a.add_argument("--seconds",type=float,default=460)
    a.add_argument("--output",default="stationary_candidate.npz")
    args=a.parse_args()
    s=Shape(args.nr,args.nt,args.R,args.degree,args.angular,args.compact,
            args.singular,args.angular_cap)
    s.run_configuration=vars(args)
    s.radial_basis=args.radial_basis
    s.p.tail_terms=args.tail_terms
    s.spline_order=args.spline_order
    s.origin_radius=args.origin_radius
    s.build_basis(args.k)
    s.source_weight=args.source_weight
    s.objective=args.objective
    s.rows=(s.p.r>.04)&(s.p.r<min(args.R*.9,args.fit_radius))
    indices=np.flatnonzero(s.rows)[::args.radial_sample]
    s.rows[:]=False;s.rows[indices]=True
    s.cols=np.unique(np.r_[np.arange(0,args.nt+1,args.angular_sample),args.nt])
    s.weight=np.ones((len(indices),len(s.cols)))
    if args.sample_normalize:s.weight*=np.sqrt(14000/s.weight.size)
    s.seconds=args.seconds
    z=np.zeros(len(s.names)+1);z[0]=args.k
    if args.load:
        old=np.load(args.load);z[0]=old["z"][0]
        for name,value in zip(old["names"].tolist(),old["z"][1:]):
            if tuple(name) in s.names:z[1+s.names.index(tuple(name))]=value
        oldcompact=str(old["compact"]) if "compact" in old else "quadratic"
        oldcap=int(old["angular_cap"]) if "angular_cap" in old else 0
        oldbasis=str(old["radial_basis"]) if "radial_basis" in old else "chebyshev"
        oldorder=int(old["spline_order"]) if "spline_order" in old else 3
        oldorigin=float(old["origin_radius"]) if "origin_radius" in old else 0.
        if (oldcompact!=args.compact or oldcap!=args.angular_cap or
            oldbasis!=args.radial_basis or
            oldorder!=args.spline_order or oldorigin!=args.origin_radius or
            (args.radial_basis=="spline" and int(old["degree"])!=args.degree)):
            s.build_basis(z[0])
            if (oldbasis==args.radial_basis=="spline" and oldcompact==args.compact
                and oldorder==args.spline_order and oldorigin==args.origin_radius):
                # Radial degree changes preserve each angular factor. Fit
                # the unmultiplied radial profiles separately, avoiding a
                # large, redundant two-dimensional projection.
                od=int(old["degree"]);oa=int(old["angular"])
                oldcoef=old["z"][1:1+(oa+1)*od].reshape(oa+1,od)
                knots=np.r_[np.zeros(oldorder+1),
                            np.linspace(0,1,od-oldorder+2)[1:-1]**1.3,
                            np.ones(oldorder+1)]
                if oldcompact=="matched":
                    oldq=1-np.exp(-(1-z[0])/2*np.log1p(s.p.r**2))
                else:
                    oldq=s.p.r**2/(1+s.p.r**2)
                oldradial=BSpline(knots,np.eye(od+1),oldorder)(oldq)[:,1:]
                profiles=oldradial@oldcoef.T
                newcoef=np.linalg.lstsq(s.radial[:s.degree].T,profiles,rcond=1e-12)[0]
                for m in range(min(oa,args.angular)+1):
                    z[1+m*s.degree:1+(m+1)*s.degree]=newcoef[:,m]
            else:
                oldshape=Shape(args.nr,args.nt,args.R,int(old["degree"]),
                               int(old["angular"]),oldcompact,
                               int(old["singular"]) if "singular" in old else 0,oldcap)
                oldshape.radial_basis=oldbasis;oldshape.spline_order=oldorder
                oldshape.origin_radius=oldorigin;oldshape.build_basis(z[0])
                oldH=oldshape.evaluate(old["z"])[0]
                target=oldH-s.base-z[0]*s.base_k
                design=(s.radial[:,s.rows,None]*s.angular_values[:,None,s.cols]).reshape(len(s.names),-1).T
                z[1:]=np.linalg.lstsq(design,
                                      target[s.rows][:,s.cols].ravel(),rcond=1e-8)[0]
                del design,target,oldH,oldshape
            z[1:]=np.clip(z[1:],-29.9,29.9)
    s.output=args.output
    fixed=args.fixed_k is not None
    if fixed:
        z[0]=args.fixed_k
        expand=lambda v:np.r_[args.fixed_k,v]
        objective=lambda v:s.fun(expand(v))
        jacobian=(lambda v:s.jac(expand(v))[:,1:]) if args.analytic_jac else "2-point"
        initial=z[1:]
        bounds=(np.full(len(initial),-30.),np.full(len(initial),30.))
    else:
        expand=lambda v:v
        objective=s.fun
        jacobian=s.jac if args.analytic_jac else "2-point"
        initial=z
        bounds=(np.r_[args.min_k,np.full(len(z)-1,-30)],
                np.r_[.98,np.full(len(z)-1,30)])
    try:
        if args.tr_solver=="krylov":
            from linearized import StationaryDerivative
            result=krylov_solve(objective,lambda v:StationaryDerivative(s,expand(v),fixed),
                    initial,bounds,args.nfev,args.normal_damping,args.krylov_iterations,
                    deadline=s.start+s.seconds)
        elif args.tr_solver=="normal":
            if not args.analytic_jac:raise ValueError("normal solver requires --analytic-jac")
            result=normal_solve(objective,jacobian,initial,bounds,args.nfev,args.normal_damping)
        else:
            result=least_squares(objective,initial,jac=jacobian,bounds=bounds,
                                 max_nfev=args.nfev,ftol=1e-10,xtol=1e-10,gtol=1e-9,
                                 x_scale="jac",verbose=0,tr_solver=args.tr_solver,
                                 tr_options={"maxiter":150} if args.tr_solver=="lsmr" else {})
        s.save(args.output,expand(result.x))
        message=result.message;nfev=result.nfev;optimality=result.optimality
    except TimeoutError as exc:
        if s.best_z is not None:s.save(args.output,s.best_z)
        message=str(exc);nfev=s.calls;optimality=None
    print("termination",message,"nfev",nfev,"optimality",optimality,flush=True)
    with open(args.output+".json","w") as f:
        json.dump(dict(message=message,nfev=nfev,optimality=optimality,
                       history=s.history),f,indent=2)

if __name__=="__main__":main()
