"""Matrix-free derivative and discrete adjoint for the stationary residual.

The adjoint transposes the actual quadrature, including extrapolation stencils
and exterior tails. It is checked against the dense derivative before use.
"""
import os
for key in ("OPENBLAS_NUM_THREADS","OMP_NUM_THREADS","MKL_NUM_THREADS"):
    os.environ[key]="1"
import numpy as np
from scipy.interpolate import CubicSpline
from scipy.linalg import solve_banded
from scipy.sparse.linalg import LinearOperator


def cubic_value_weights(x,point):
    """Adjoint of not-a-knot cubic interpolation, using linear storage."""
    n=len(x)
    if n<4:return CubicSpline(x,np.eye(n))(point)
    dx=np.diff(x)
    A=np.zeros((3,n))
    A[1,1:-1]=2*(dx[:-1]+dx[1:])
    A[0,2:]=dx[:-1];A[2,:-2]=dx[1:]
    left=x[2]-x[0];right=x[-1]-x[-3]
    A[1,0]=dx[1];A[0,1]=left
    A[1,-1]=dx[-2];A[2,-2]=right
    i=int(np.clip(np.searchsorted(x,point)-1,0,n-2))
    h=dx[i];u=(point-x[i])/h
    weights=np.zeros(n);derivative_bar=np.zeros(n)
    weights[i]=2*u**3-3*u**2+1;weights[i+1]=-2*u**3+3*u**2
    derivative_bar[i]=h*(u**3-2*u**2+u)
    derivative_bar[i+1]=h*(u**3-u**2)
    transpose=np.zeros_like(A);transpose[1]=A[1]
    transpose[0,1:]=A[2,:-1];transpose[2,:-1]=A[0,1:]
    bbar=solve_banded((1,1),transpose,derivative_bar,check_finite=False)
    slope_bar=np.zeros(n-1)
    slope_bar[:-1]+=3*dx[1:]*bbar[1:-1]
    slope_bar[1:]+=3*dx[:-1]*bbar[1:-1]
    slope_bar[0]+=(dx[0]+2*left)*dx[1]/left*bbar[0]
    slope_bar[1]+=dx[0]**2/left*bbar[0]
    slope_bar[-2]+=dx[-1]**2/right*bbar[-1]
    slope_bar[-1]+=(2*right+dx[-1])*dx[-2]/right*bbar[-1]
    weights[:-1]-=slope_bar/dx;weights[1:]+=slope_bar/dx
    return weights


class StationaryDerivative(LinearOperator):
    def __init__(self,shape,z,fixed=False):
        self.s=shape;self.p=shape.p;self.z=z.copy();self.fixed=fixed
        self.k=z[0];self.cl=1/z[0]
        _,self.f,self.L2,self.E,den=shape.evaluate(z)
        self.D=shape.objective_den(self.f,den)
        self.Uadv=(2*self.f["ux"]+self.f["uy"]+
                   self.f["ur"]*self.f["ht"]+self.f["ua"]*self.f["ha"])
        self.source=shape.source(self.f,self.L2,self.cl)
        self.interpolation=None
        if self.source and shape.source_weight:
            ts,_,at,bt=self.source
            self.interpolation=cubic_value_weights(self.p.t,ts)
            self.source_ratio=bt/at
        self.k_column=None
        if not fixed:
            eps=2e-6
            zp=z.copy();zm=z.copy();zp[0]+=eps;zm[0]-=eps
            values=[]
            for zz in (zp,zm):
                _,ff,LL,ee,dd=shape.evaluate(zz)
                dd=shape.objective_den(ff,dd)
                ss=shape.source(ff,LL,1/zz[0])
                values.append(np.r_[
                    ((ee/dd)[shape.rows][:,shape.cols]*shape.weight).ravel(),
                    shape.source_weight*(ss[1]-1) if ss else 0.])
            self.k_column=(values[0]-values[1])/(2*eps)
            shape.evaluate(z)
        self.mix=self.p.ct[1:-1]/self.p.st[1:-1]-2*self.p.st[1:-1]/self.p.ct[1:-1]
        super().__init__(dtype=np.dtype(float),
                         shape=(shape.weight.size+1,len(z)-int(fixed)))

    def _tail(self,drho,drt,dra):
        p=self.p;k=self.k
        if p.tail_terms==1:
            return (((k*drho)*p.ct-dra*p.st)/p.R)@p.project/(p.m-1-k)
        projector=p.weights[:,None]*p.sodd.T
        modes=drho@projector;modes_t=drt@projector
        second=(modes_t-k*modes)/(k-1)
        answer=np.zeros(len(p.m))
        for exponent,part in ((k,modes-second),(2*k-1,second)):
            answer+=((exponent-p.m+1)*part[:-1]+
                     (exponent+p.m+1)*part[1:])/(2*p.R*(p.m-1-exponent))
        return answer

    def _matvec(self,vector):
        vector=np.asarray(vector).reshape(-1)
        coef=vector if self.fixed else vector[1:]
        s=self.s;p=self.p;f=self.f;L2=self.L2
        if s.basis_k!=self.k:s.build_basis(self.k)
        dh,dht,dha=s.apply_basis(coef)
        drho=f["rho"]*dh
        drt=f["rt"]*dh+f["rho"]*dht
        dra=f["ra"]*dh+f["rho"]*dha
        df=p.project_sine((drt*p.ct-dra*p.st)/p.rr)
        boundary=self._tail(drho[-1],drt[-1],dra[-1])
        A,B=p.modal_integrals(df,np.zeros(len(p.m)),self.k,boundary)
        dq=(A+B)/(2*p.m);dv=(B-A)/2
        dur=-p.cosine_series(dq*p.m);dua=p.sine_series(dv)
        dquot=np.empty_like(dua)
        dquot[:,1:-1]=dua[:,1:-1]*self.mix
        dquot[:,0]=dv@p.m
        dquot[:,-1]=2*dv@(p.m*p.cos[:,-1])
        dc=(B[0,0]+df[0,0]/2)/2
        dL2=-L2*dc/f["c"]
        dUadv=((3+f["ht"])*dur+f["ha"]*dua+dquot+
               f["ur"]*dht+f["ua"]*dha)
        total=L2*dUadv+self.Uadv*dL2
        de=self.cl*dht+total
        dd=np.sign(3+f["ht"])*dht
        if s.objective=="normalized":dd+=np.sign(L2*self.Uadv)*total
        if s.objective=="absolute":dd[:]=0
        answer=((de/self.D-self.E*dd/self.D**2)[s.rows][:,s.cols]*s.weight).ravel()
        source=0.
        if self.interpolation is not None:
            tau=self.source_ratio
            da=L2*dur[:,0]+f["ux"][:,0]*dL2
            db=L2*(dur[:,0]+dv@p.m)+f["uy"][:,0]*dL2
            source=s.source_weight*np.dot(self.interpolation,db-tau*da)
        answer=np.r_[answer,source]
        if not self.fixed:answer+=vector[0]*self.k_column
        return answer

    def _rmatvec(self,vector):
        vector=np.asarray(vector).reshape(-1)
        s=self.s;p=self.p;f=self.f;L2=self.L2
        if s.basis_k!=self.k:s.build_basis(self.k)
        v=np.zeros_like(self.E)
        v[np.ix_(s.rows,s.cols)]=vector[:-1].reshape(s.weight.shape)*s.weight
        ge=v/self.D;gd=-v*self.E/self.D**2
        totalbar=ge.copy()
        if s.objective=="normalized":totalbar+=gd*np.sign(L2*self.Uadv)
        htbar=self.cl*ge
        if s.objective!="absolute":htbar+=gd*np.sign(3+f["ht"])
        ubar=L2*totalbar
        durbar=ubar*(3+f["ht"])
        duabar=ubar*f["ha"]
        dquotbar=ubar
        htbar+=ubar*f["ur"]
        habar=ubar*f["ua"]
        Lbar=np.sum(totalbar*self.Uadv)
        dvbar=np.zeros_like(f["v"])
        if self.interpolation is not None:
            sourcebar=vector[-1]*s.source_weight*self.interpolation
            tau=self.source_ratio
            durbar[:,0]+=L2*(1-tau)*sourcebar
            dvbar+=L2*sourcebar[:,None]*p.m
            Lbar+=np.dot(sourcebar,f["uy"][:,0]-tau*f["ux"][:,0])
        dqbar=-p.cosine_series_transpose(durbar)*p.m
        # The sine transform is symmetric on interior samples.
        from scipy.fft import dst
        dvbar+=dst(duabar[:,1:-1],type=1,axis=-1)/2
        dvbar+=dst(dquotbar[:,1:-1]*self.mix,type=1,axis=-1)/2
        dvbar+=dquotbar[:,0,None]*p.m
        dvbar+=2*dquotbar[:,-1,None]*(p.m*p.cos[:,-1])
        Abar=dqbar/(2*p.m)-dvbar/2
        Bbar=dqbar/(2*p.m)+dvbar/2
        cbar=-L2*Lbar/f["c"]
        Bbar[0,0]+=cbar/2
        dfbar,boundarybar=p.modal_integrals_transpose(Abar,Bbar)
        dfbar[0,0]+=cbar/4
        dfxbar=(2/p.nt)*p.sine_series(dfbar)
        drtbar=dfxbar*p.ct/p.rr
        drabar=-dfxbar*p.st/p.rr
        drhobar=np.zeros_like(self.E)
        if p.tail_terms==1:
            valuebar=(boundarybar/(p.m-1-self.k))@p.project.T/p.R
            drhobar[-1]+=self.k*p.ct*valuebar
            drabar[-1]-=p.st*valuebar
        else:
            partbars=[]
            for exponent in (self.k,2*self.k-1):
                partbar=np.zeros(p.nt)
                valuebar=boundarybar/(2*p.R*(p.m-1-exponent))
                partbar[:-1]+=(exponent-p.m+1)*valuebar
                partbar[1:]+=(exponent+p.m+1)*valuebar
                partbars.append(partbar)
            secondbar=partbars[1]-partbars[0]
            modesbar=partbars[0]-self.k*secondbar/(self.k-1)
            modestbar=secondbar/(self.k-1)
            projector=p.weights[:,None]*p.sodd.T
            drhobar[-1]+=modesbar@projector.T
            drtbar[-1]+=modestbar@projector.T
        hbar=f["rho"]*drhobar+f["rt"]*drtbar+f["ra"]*drabar
        htbar+=f["rho"]*drtbar
        habar+=f["rho"]*drabar
        answer=s.transpose_basis(hbar,htbar,habar)
        if not self.fixed:answer=np.r_[np.dot(vector,self.k_column),answer]
        return answer
