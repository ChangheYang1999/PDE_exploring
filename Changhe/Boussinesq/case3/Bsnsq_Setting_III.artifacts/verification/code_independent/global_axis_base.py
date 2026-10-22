"""Own explicit base-axis data and two independent ODE formulations.

The original Cartesian PDE supplies both systems. No lead/NUM code is used.
The second system integrates the axis integrating factor, not Q itself.
"""
from dataclasses import dataclass
import math
import numpy as np
from scipy.integrate import solve_ivp

@dataclass
class BaseAxis:
    beta: float
    a0: float=1.0

    def __post_init__(self):
        if self.beta<=2 or self.a0<=0:raise ValueError('beta>2 and a0>0 required')
        self.p=(self.beta-1)/(2*self.beta);self.c=1+self.beta/2
        self.mu=1+1.5*self.beta;self.L=3*self.c*math.sqrt(self.beta)/(4*self.a0)
        self.h=math.sqrt(self.beta)*self.L;self.S0=self.L**2+self.h**2
        self.ell=-self.c*self.S0/(2*self.p*self.h)
        self.B=-self.ell/self.S0**self.p

    def values(self,logr,side):
        r=np.exp(logr);y=side*r
        z=(y*y-2*self.h*y)/self.S0
        logbase=np.log1p(z)
        # expm1 preserves the cancellation in the moving-center subtraction.
        b=self.beta*y+self.ell*np.expm1(self.p*logbase)
        bp=self.beta+self.ell*self.p*(2*(y-self.h)/self.S0)*np.exp((self.p-1)*logbase)
        vr=b/y
        logS=np.log(self.S0)+logbase
        logqe=np.log(4*self.B*self.p)+(self.p-2)*logS+np.log(2*self.L**2+(self.p+1)*(y-self.h)**2)
        return vr,bp,logqe

    def solve(self,side,radii,form='direct',rtol=2e-11,eps=1e-8):
        ts=np.log(np.asarray(radii,dtype=float));t0=math.log(eps)
        if side not in [-1,1] or ts[0]<t0-1e-12:raise ValueError('invalid side or radii')
        if form=='direct':
            def rhs(t,z):
                vr,bp,_=self.values(t,side)
                return [(2*bp-3*self.beta-2)/vr,(2*math.exp(z[0]-z[1])-(2*self.beta+1-bp))/vr]
            initial=[math.log(self.a0),math.log(4*self.a0/self.beta)]
            method='DOP853'
        elif form=='integrating_factor':
            rho=(self.beta+1)/self.mu
            def rhs(t,z):
                vr,_,_=self.values(t,side)
                return [self.mu/vr-1,rho-1+math.exp(-rho*z[0]-z[1])]
            initial=[0,-math.log1p(-rho)];method='Radau'
        else:raise ValueError('unknown formulation')
        sol=solve_ivp(rhs,(t0,float(ts[-1])),initial,method=method,rtol=rtol,atol=rtol*.03,t_eval=ts,max_step=1.5)
        if not sol.success:raise RuntimeError(sol.message)
        vr,bp,lqe=self.values(ts,side)
        if form=='direct':la,lq=sol.y
        else:
            Z,LJ=sol.y;P=(2*self.beta+1)/self.mu
            la=np.log(self.a0)-2*np.log(self.mu)+2*np.log(vr)-2*Z
            lq=np.log(2*self.a0)-2*np.log(self.mu)+np.log(vr)-P*Z+LJ
        return {'log_a':la,'log_Q':lq,'Q_over_qe':np.exp(lq-lqe),'v_over_r':vr,'bprime':bp,
                'nfev':sol.nfev,'method':method,'eps':eps,'rtol':rtol,'form':form}
